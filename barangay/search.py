import warnings
from typing import TYPE_CHECKING, Any, Callable, List, Literal

import pandas as pd

from barangay.data import load_fuzzer_base
from barangay.fuzz import FuzzBase, create_fuzz_base
from barangay.types import MatchHook
from barangay.utils import _basic_sanitizer

if TYPE_CHECKING:
    from barangay.models import AdminLevel, SearchResult


# Create default fuzz base instance (backward compatibility)
_default_fuzz_base = FuzzBase(fuzzer_base=load_fuzzer_base())


def search(
    search_string: str,
    match_hooks: List[Literal["province", "municipality", "barangay"]] = [
        "province",
        "municipality",
        "barangay",
    ],
    threshold: float = 60.0,
    n: int = 5,
    search_sanitizer: Callable[..., str] = _basic_sanitizer,
    fuzz_base: FuzzBase | None = None,
    as_of: str | None = None,
) -> List[dict]:
    """Search barangay data with fuzzy matching.

    .. deprecated::
        search() is deprecated and will be removed in 2027.X.X.X.
        Use search_fuzzy() instead for typed SearchResult objects.

    Args:
        search_string: String to search for in barangay data.
        match_hooks: List of location levels to match. Defaults to all.
        threshold: Minimum similarity score (0-100). Defaults to 60.0.
        n: Maximum number of results to return. Defaults to 5.
        search_sanitizer: Function to clean search input.
        fuzz_base: FuzzBase instance for scoring. Auto-created if None.
        as_of: Date string for data version. Used with fuzz_base.

    Returns:
        List of matching barangay records as dictionaries.
    """
    warnings.warn(
        "search() is deprecated and will be removed in 2027.X.X.X. "
        "Use search_fuzzy() instead for typed SearchResult objects.",
        DeprecationWarning,
        stacklevel=2,
    )
    # Create fuzz_base if not provided
    if fuzz_base is None:
        fuzz_base = create_fuzz_base(as_of=as_of)

    cleaned_sample: str = search_sanitizer(search_string)

    active_ratios: List[str] = []
    df: pd.DataFrame = pd.DataFrame()

    # B - Barangay only
    if len(match_hooks) == 1 and "barangay" in match_hooks:
        df["f_000b_ratio" + "_score"] = fuzz_base.fuzzer_base["f_000b_ratio"].apply(
            lambda f: f(s2=cleaned_sample)
        )
        active_ratios.append("f_000b_ratio_score")

    # PB - Province + Barangay
    if "province" in match_hooks and "barangay" in match_hooks:
        df["f_0p0b_ratio" + "_score"] = fuzz_base.fuzzer_base["f_0p0b_ratio"].apply(
            lambda f: f(s2=cleaned_sample)
        )
        active_ratios.append("f_0p0b_ratio_score")

    # MB - Municipality + Barangay
    if "municipality" in match_hooks and "barangay" in match_hooks:
        df["f_00mb_ratio" + "_score"] = fuzz_base.fuzzer_base["f_00mb_ratio"].apply(
            lambda f: f(s2=cleaned_sample)
        )
        active_ratios.append("f_00mb_ratio_score")

    # PMB - Province + Municipality + Barangay
    if (
        "province" in match_hooks
        and "municipality" in match_hooks
        and "barangay" in match_hooks
    ):
        df["f_0pmb_ratio" + "_score"] = fuzz_base.fuzzer_base["f_0pmb_ratio"].apply(
            lambda f: f(s2=cleaned_sample)
        )
        active_ratios.append("f_0pmb_ratio_score")

    df["max_score"] = df[active_ratios].max(axis=1)
    df["search_string"] = cleaned_sample
    res_cutoff = pd.DataFrame(df[df["max_score"] >= threshold])
    len_res = len(res_cutoff)
    if len_res < 1:
        return []

    if len_res < n:
        n = len_res
    results_df = res_cutoff.sort_values(by="max_score", ascending=False)[:n]
    truncated_results = pd.concat(
        [fuzz_base.fuzzer_base.loc[results_df.index], results_df], axis=1
    )[
        [
            "barangay",
            "province_or_huc",
            "municipality_or_city",
            "psgc_id",
            *active_ratios,
            "000b",
            "0p0b",
            "00mb",
            "0pmb",
        ]
    ]
    return truncated_results.to_dict(orient="records")


def search_fuzzy(
    query: str,
    *,
    level: "AdminLevel | None" = None,
    match_hooks: list[MatchHook] | None = None,
    threshold: float = 60.0,
    limit: int = 5,
    as_of: str | None = None,
) -> List["SearchResult"]:
    """Fuzzy search PSGC data, returning rich SearchResult objects.

    This is the new API entry point. The old search() is preserved unchanged.

    Args:
        query: Search string (e.g. "Tongmageng, Tawi-Tawi").
        level: Filter to a specific admin level, or None for all.
        match_hooks: Which fuzzy scoring columns to compute. Defaults to all three
            (province, municipality, barangay). Controls which name-levels
            participate in matching, unlike ``level`` which is a post-filter on
            result record types.
        threshold: Minimum score (0-100).
        limit: Max results.
        as_of: Historical date.

    Returns:
        List of SearchResult, sorted by score descending.
    """
    from barangay.database import Database

    db = Database()
    view = db._view(level)
    return view.search_fuzzy(
        query, threshold=threshold, limit=limit, as_of=as_of, match_hooks=match_hooks
    )


def _search_fuzzy_new(
    query: str,
    *,
    level: "AdminLevel | None",
    threshold: float,
    limit: int,
    index: Any,
    as_of: str | None = None,
    match_hooks: list[MatchHook] | None = None,
) -> List["SearchResult"]:
    """Bridge from new API to existing FuzzBase infrastructure."""
    from barangay.fuzz import create_fuzz_base
    from barangay.models import SearchResult

    fuzz_base = create_fuzz_base(as_of=as_of)
    raw_results = _run_fuzz_scoring(
        fuzz_base, query, threshold, limit, match_hooks=match_hooks
    )

    results: List[SearchResult] = []
    for raw in raw_results:
        psgc_id = raw["psgc_id"]
        record = index.get(psgc_id)
        if record is None:
            continue
        if level is not None and record.type != level:
            continue

        sr = SearchResult(
            record=record,
            score=raw["max_score"],
            match_type=_infer_match_type(raw),
        )
        sr._index = index
        results.append(sr)

    return results


def _run_fuzz_scoring(
    fuzz_base: FuzzBase,
    query: str,
    threshold: float,
    limit: int,
    match_hooks: list[MatchHook] | None = None,
) -> List[dict]:
    """Extracted scoring loop from existing search()."""
    if match_hooks is None:
        match_hooks = ["province", "municipality", "barangay"]

    cleaned = _basic_sanitizer(query)
    df = pd.DataFrame()

    active_ratios: List[str] = []

    if len(match_hooks) == 1 and "barangay" in match_hooks:
        if "f_000b_ratio" in fuzz_base.fuzzer_base.columns:
            df["f_000b_ratio_score"] = fuzz_base.fuzzer_base["f_000b_ratio"].apply(
                lambda f: f(s2=cleaned)
            )
            active_ratios.append("f_000b_ratio_score")

    if "province" in match_hooks and "barangay" in match_hooks:
        if "f_0p0b_ratio" in fuzz_base.fuzzer_base.columns:
            df["f_0p0b_ratio_score"] = fuzz_base.fuzzer_base["f_0p0b_ratio"].apply(
                lambda f: f(s2=cleaned)
            )
            active_ratios.append("f_0p0b_ratio_score")

    if "municipality" in match_hooks and "barangay" in match_hooks:
        if "f_00mb_ratio" in fuzz_base.fuzzer_base.columns:
            df["f_00mb_ratio_score"] = fuzz_base.fuzzer_base["f_00mb_ratio"].apply(
                lambda f: f(s2=cleaned)
            )
            active_ratios.append("f_00mb_ratio_score")

    if (
        "province" in match_hooks
        and "municipality" in match_hooks
        and "barangay" in match_hooks
    ):
        if "f_0pmb_ratio" in fuzz_base.fuzzer_base.columns:
            df["f_0pmb_ratio_score"] = fuzz_base.fuzzer_base["f_0pmb_ratio"].apply(
                lambda f: f(s2=cleaned)
            )
            active_ratios.append("f_0pmb_ratio_score")

    if not active_ratios:
        return []

    df["max_score"] = df[active_ratios].max(axis=1)
    cutoff = df[df["max_score"] >= threshold]
    if cutoff.empty:
        return []

    n = min(limit, len(cutoff))
    top = cutoff.sort_values("max_score", ascending=False).head(n)

    result = pd.concat(
        [fuzz_base.fuzzer_base.loc[top.index], top[["max_score", *active_ratios]]],
        axis=1,
    )
    return result.to_dict(orient="records")


def _infer_match_type(raw: dict) -> str:
    """Infer match type from scoring columns."""
    parts = []
    if "f_0p0b_ratio_score" in raw and raw.get("f_0p0b_ratio_score", 0) == raw.get(
        "max_score", 0
    ):
        parts.append("province")
    if "f_00mb_ratio_score" in raw and raw.get("f_00mb_ratio_score", 0) == raw.get(
        "max_score", 0
    ):
        parts.append("municipality")
    if "f_000b_ratio_score" in raw and raw.get("f_000b_ratio_score", 0) == raw.get(
        "max_score", 0
    ):
        parts.append("barangay")
    if "f_0pmb_ratio_score" in raw and raw.get("f_0pmb_ratio_score", 0) == raw.get(
        "max_score", 0
    ):
        parts.append("province+municipality+barangay")
    return "+".join(parts) if parts else "unknown"
