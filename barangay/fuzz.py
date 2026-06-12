from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Any, Callable, cast

import pandas as pd
from rapidfuzz import fuzz

from barangay.data import load_fuzzer_base
from barangay.models import AdminLevel
from barangay.utils import _basic_sanitizer

if TYPE_CHECKING:
    from barangay.database import HierarchyIndex
    from barangay.models import AdminDivFlat

__all__ = [
    "FuzzBase",
    "create_fuzz_base",
    "create_level_fuzz_base",
    "invalidate_fuzz_cache",
]

_HOOK_GRANULARITY: dict[str, int] = {
    "region": 0,
    "province": 1,
    "municipality": 2,
    "barangay": 3,
}

_LEVEL_TO_ADMIN: dict[str, AdminLevel] = {}
for _lvl in ("region", "province", "municipality", "barangay"):
    _LEVEL_TO_ADMIN[_lvl] = AdminLevel(_lvl)


def _make_scorer(df: pd.DataFrame, col: str) -> pd.Series:
    return cast(
        Any,
        df[col].apply(
            cast(
                Callable[[str], Any],
                lambda ref: partial(fuzz.token_sort_ratio, s1=ref),
            )
        ),
    )


class FuzzBase:
    def __init__(
        self,
        *,
        fuzzer_base: pd.DataFrame,
        sanitizer: Callable[[str | None], str] = _basic_sanitizer,
    ):
        self.fuzzer_base = fuzzer_base.copy()
        self.sanitizer = sanitizer
        self._level: str | None = None

        if "barangay" in self.fuzzer_base.columns:
            self._build_barangay_columns()
        elif "name" in self.fuzzer_base.columns:
            self._build_generic_columns()
        else:
            raise ValueError(
                "FuzzBase requires a DataFrame with either 'barangay' or 'name' column"
            )

    def _build_barangay_columns(self) -> None:
        self.fuzzer_base["000b"] = (
            self.fuzzer_base["barangay"].fillna("").astype(str).apply(self.sanitizer)
        )
        self.fuzzer_base["0p0b"] = (
            self.fuzzer_base["province_or_huc"]
            .fillna("")
            .astype(str)
            .str.cat(self.fuzzer_base["barangay"].fillna("").astype(str), sep=" ")
        ).apply(self.sanitizer)
        self.fuzzer_base["00mb"] = (
            self.fuzzer_base["municipality_or_city"]
            .fillna("")
            .astype(str)
            .str.cat(self.fuzzer_base["barangay"].fillna("").astype(str), sep=" ")
        ).apply(self.sanitizer)
        self.fuzzer_base["0pmb"] = (
            self.fuzzer_base["province_or_huc"]
            .fillna("")
            .astype(str)
            .str.cat(
                self.fuzzer_base["municipality_or_city"].fillna("").astype(str), sep=" "
            )
            .str.cat(self.fuzzer_base["barangay"].fillna("").astype(str), sep=" ")
        ).apply(self.sanitizer)

        self.fuzzer_base["f_000b_ratio"] = _make_scorer(self.fuzzer_base, "000b")
        self.fuzzer_base["f_00mb_ratio"] = _make_scorer(self.fuzzer_base, "00mb")
        self.fuzzer_base["f_0p0b_ratio"] = _make_scorer(self.fuzzer_base, "0p0b")
        self.fuzzer_base["f_0pmb_ratio"] = _make_scorer(self.fuzzer_base, "0pmb")

    def _build_generic_columns(self) -> None:
        fb = self.fuzzer_base
        fb["self_name"] = fb["name"].fillna("").astype(str).apply(self.sanitizer)

        for ancestor in ("region", "province", "municipality"):
            if ancestor in fb.columns and (fb[ancestor].fillna("") != "").any():
                a = fb[ancestor].fillna("").astype(str)
                n = fb["name"].fillna("").astype(str)
                combined = (a + " " + n).where(a != "", n)
                fb[f"{ancestor}_name"] = combined.apply(self.sanitizer)

        has_ancestor = any(
            col in fb.columns and (fb[col].fillna("") != "").any()
            for col in ("region", "province", "municipality")
        )
        if has_ancestor:

            def _join_nonempty(row: pd.Series) -> str:
                parts: list[str] = []
                for col in ("region", "province", "municipality", "name"):
                    val = row.get(col, "")
                    if val:
                        parts.append(val)
                return " ".join(parts)

            fb["full_name"] = fb.apply(_join_nonempty, axis=1).apply(self.sanitizer)

        fb["f_self_name_ratio"] = _make_scorer(fb, "self_name")
        for ancestor in ("region", "province", "municipality"):
            if f"{ancestor}_name" in fb.columns:
                fb[f"f_{ancestor}_name_ratio"] = _make_scorer(fb, f"{ancestor}_name")
        if "full_name" in fb.columns:
            fb["f_full_name_ratio"] = _make_scorer(fb, "full_name")


_fuzz_base_cache: dict[str | None, FuzzBase] = {}
_level_fuzz_cache: dict[tuple[str | None, str], FuzzBase] = {}
_level_index_cache: dict[str | None, tuple[list[AdminDivFlat], HierarchyIndex]] = {}


def create_fuzz_base(as_of: str | None = None) -> FuzzBase:
    if as_of in _fuzz_base_cache:
        return _fuzz_base_cache[as_of]
    fuzzer_base = load_fuzzer_base(as_of=as_of)
    fb = FuzzBase(fuzzer_base=fuzzer_base)
    _fuzz_base_cache[as_of] = fb
    return fb


def _build_level_index(
    as_of: str | None = None,
) -> tuple[list[AdminDivFlat], HierarchyIndex]:
    if as_of in _level_index_cache:
        return _level_index_cache[as_of]
    from barangay.data import load_barangay_flat_data
    from barangay.database import HierarchyIndex
    from barangay.models import AdminDivRecord

    flat_models = load_barangay_flat_data(as_of=as_of)
    records = [AdminDivRecord.model_validate(f.model_dump()) for f in flat_models]
    index = HierarchyIndex(records)
    result = (flat_models, index)
    _level_index_cache[as_of] = result
    return result


def _build_level_dataframe(
    level: str,
    records: list[AdminDivFlat],
    index: HierarchyIndex,
) -> pd.DataFrame:
    admin_level = _LEVEL_TO_ADMIN[level]
    level_records = index.records_of_type(admin_level)

    rows: list[dict[str, str]] = []
    for rec in level_records:
        region_rec = index.resolve_region(rec)
        province_rec = index.resolve_province(rec)
        municipality_rec = index.resolve_municipality(rec)
        rows.append(
            {
                "name": rec.name,
                "region": region_rec.name if region_rec else "",
                "province": province_rec.name if province_rec else "",
                "municipality": municipality_rec.name if municipality_rec else "",
                "psgc_id": rec.psgc_id,
            }
        )

    return pd.DataFrame(rows)


def create_level_fuzz_base(level: str, as_of: str | None = None) -> FuzzBase:
    cache_key = (as_of, level)
    if cache_key in _level_fuzz_cache:
        return _level_fuzz_cache[cache_key]

    flat_models, index = _build_level_index(as_of=as_of)
    df = _build_level_dataframe(level, flat_models, index)
    fb = FuzzBase(fuzzer_base=df)
    fb._level = level
    _level_fuzz_cache[cache_key] = fb
    return fb


def invalidate_fuzz_cache() -> None:
    _fuzz_base_cache.clear()
    _level_fuzz_cache.clear()
    _level_index_cache.clear()
