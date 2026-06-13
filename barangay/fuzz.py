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
    "highly_urbanized_city": 2,
    "independent_component_city": 3,
    "component_city": 4,
    "municipality": 5,
    "submunicipality": 6,
    "special_geographic_area": 7,
    "barangay": 8,
}

_HOOK_TO_LETTER: dict[str, str] = {
    "region": "r",
    "province": "p",
    "highly_urbanized_city": "h",
    "independent_component_city": "i",
    "component_city": "c",
    "municipality": "m",
    "submunicipality": "s",
    "special_geographic_area": "g",
    "barangay": "b",
}

_PRE_CONCAT_COLS: list[str] = [
    "r0h00000b",
    "r0h000s0b",
    "r0000m00b",
    "rp000m00b",
    "rp00c000b",
    "rp0i0000b",
    "r0000m0gb",
]

_POS_TO_COL: list[str] = [
    "region",
    "province",
    "highly_urbanized_city",
    "independent_component_city",
    "component_city",
    "municipality",
    "submunicipality",
    "special_geographic_area",
    "barangay",
]

_LEVEL_TO_ADMIN: dict[str, AdminLevel] = {}
for _lvl in _POS_TO_COL:
    _LEVEL_TO_ADMIN[_lvl] = AdminLevel(_lvl)


def _hooks_to_indicator(hooks: tuple[str, ...]) -> str:
    indicator = ["0"] * 9
    for hook in hooks:
        pos = _HOOK_GRANULARITY.get(hook)
        if pos is not None:
            indicator[pos] = _HOOK_TO_LETTER[hook]
    return "".join(indicator)


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
        level: str | None = None,
    ):
        self.fuzzer_base = fuzzer_base.copy()
        self.sanitizer = sanitizer
        self._level = level

        if "barangay" in self.fuzzer_base.columns:
            self._build_barangay_columns()
        elif "name" in self.fuzzer_base.columns:
            self._build_generic_columns()
        else:
            raise ValueError(
                "FuzzBase requires a DataFrame with either 'barangay' or 'name' column"
            )

    def _build_barangay_columns(self) -> None:
        fb = self.fuzzer_base
        self._pre_concat_meta: dict[str, set[str]] = {}
        self._indicator_cache: dict[str, str] = {}

        for col in _PRE_CONCAT_COLS:
            if col not in fb.columns:
                continue
            letters = {col[i] for i in range(9) if col[i] != "0"}
            self._pre_concat_meta[col] = letters
            sanitized = fb[col].apply(self.sanitizer)
            tmp_col = f"_tmp_{col}"
            fb[tmp_col] = sanitized
            fb[f"f_{col}"] = _make_scorer(fb, tmp_col)
            fb.pop(tmp_col)

    def _build_indicator_column(self, indicator: str) -> str:
        f_col = f"f_{indicator}"
        if f_col in self.fuzzer_base.columns:
            return f_col
        if indicator in self._indicator_cache:
            return self._indicator_cache[indicator]

        fb = self.fuzzer_base
        active_cols: list[str] = []
        for pos, letter in enumerate(indicator):
            if letter != "0":
                admin_col = _POS_TO_COL[pos]
                if admin_col in fb.columns:
                    active_cols.append(admin_col)

        if active_cols:

            def _join(row: pd.Series) -> str:
                parts: list[str] = []
                for c in active_cols:
                    val = row.get(c, "")
                    if val:
                        parts.append(str(val))
                return " ".join(parts)

            combined = fb.apply(_join, axis=1).apply(self.sanitizer)
            tmp_col = f"_tmp_{indicator}"
            fb[tmp_col] = combined
            fb[f_col] = _make_scorer(fb, tmp_col)
            fb.pop(tmp_col)

        letters = {indicator[i] for i in range(9) if indicator[i] != "0"}
        self._pre_concat_meta[indicator] = letters
        self._indicator_cache[indicator] = f_col
        return f_col

    def resolve_f_columns(self, match_hooks: list[str]) -> list[str]:
        requested_letters = {_HOOK_TO_LETTER[h] for h in match_hooks}
        matched: list[str] = []

        for col, letters in self._pre_concat_meta.items():
            if requested_letters.issubset(letters):
                matched.append(f"f_{col}")

        exact_indicator = _hooks_to_indicator(tuple(match_hooks))
        exact_f = self._build_indicator_column(exact_indicator)
        if exact_f not in matched:
            matched.append(exact_f)

        return matched

    def _build_generic_columns(self) -> None:
        fb = self.fuzzer_base
        self._pre_concat_meta: dict[str, set[str]] = {}
        self._indicator_cache: dict[str, str] = {}

        if self._level is not None:
            pos = _HOOK_GRANULARITY.get(self._level)
            if pos is not None:
                admin_col = _POS_TO_COL[pos]
                fb[admin_col] = fb["name"]


def _decode_column_hooks(col_name: str) -> list[str]:
    _LETTER_TO_HOOK: dict[str, str] = {v: k for k, v in _HOOK_TO_LETTER.items()}
    return [_LETTER_TO_HOOK[ch] for ch in col_name if ch != "0"]


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
        city_rec = index.resolve_city(rec)
        row: dict[str, str] = {
            "name": rec.name,
            "region": region_rec.name if region_rec else "",
            "province": province_rec.name if province_rec else "",
            "municipality": municipality_rec.name if municipality_rec else "",
            "psgc_id": rec.psgc_id,
        }
        if city_rec is not None:
            if city_rec.type == AdminLevel.HIGHLY_URBANIZED_CITY:
                row["highly_urbanized_city"] = city_rec.name
            elif city_rec.type == AdminLevel.INDEPENDENT_COMPONENT_CITY:
                row["independent_component_city"] = city_rec.name
            elif city_rec.type == AdminLevel.COMPONENT_CITY:
                row["component_city"] = city_rec.name
        rows.append(row)

    return pd.DataFrame(rows)


def create_level_fuzz_base(level: str, as_of: str | None = None) -> FuzzBase:
    cache_key = (as_of, level)
    if cache_key in _level_fuzz_cache:
        return _level_fuzz_cache[cache_key]

    flat_models, index = _build_level_index(as_of=as_of)
    df = _build_level_dataframe(level, flat_models, index)
    fb = FuzzBase(fuzzer_base=df, level=level)
    _level_fuzz_cache[cache_key] = fb
    return fb


def invalidate_fuzz_cache() -> None:
    _fuzz_base_cache.clear()
    _level_fuzz_cache.clear()
    _level_index_cache.clear()
