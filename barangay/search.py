import warnings
from typing import TYPE_CHECKING, Any, Callable, List

import pandas as pd

from barangay.fuzz import (
    FuzzBase,
    _HOOK_GRANULARITY,
    _decode_column_hooks,
    create_fuzz_base,
    create_level_fuzz_base,
)
from barangay.types import MatchHook
from barangay.utils import _basic_sanitizer

if TYPE_CHECKING:
    from barangay.models import AdminLevel, SearchResult


def search(
    search_string: str,
    match_hooks: list[MatchHook] | None = None,
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

    raw_results = _run_scoring(fuzz_base, cleaned_sample, threshold, n, match_hooks)
    if not raw_results:
        return []

    for r in raw_results:
        city_parts: list[str] = []
        for cc in (
            "highly_urbanized_city",
            "independent_component_city",
            "component_city",
        ):
            if r.get(cc):
                city_parts.append(r[cc])
        r["municipality_or_city"] = r.get("municipality", "") or " ".join(city_parts)
        r["province_or_huc"] = r.get("province", "") or " ".join(city_parts)

    df: pd.DataFrame = pd.DataFrame(raw_results)
    n = min(n, len(df))
    results_df = df.sort_values(by="max_score", ascending=False)[:n]
    return results_df.to_dict(orient="records")


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
        match_hooks: Which fuzzy scoring columns to compute. Defaults to all four
            (region, province, municipality, barangay). Controls which name-levels
            participate in matching, unlike ``level`` which is a post-filter on
            result record types. The most granular level determines the record set
            searched — e.g. ``["province"]`` searches provinces directly, while
            ``["province", "barangay"]`` searches barangays within provinces.
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
    from barangay.models import SearchResult

    raw_results = _pick_base_and_score(query, threshold, limit, match_hooks, as_of)

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


def _pick_base_and_score(
    query: str,
    threshold: float,
    limit: int,
    match_hooks: list[MatchHook] | None,
    as_of: str | None,
) -> List[dict]:
    if match_hooks is None:
        match_hooks = ["province", "municipality", "barangay"]

    base_level = max(match_hooks, key=lambda h: _HOOK_GRANULARITY.get(h, -1))

    if base_level == "barangay":
        fuzz_base = create_fuzz_base(as_of=as_of)
    else:
        fuzz_base = create_level_fuzz_base(base_level, as_of=as_of)
    return _run_scoring(fuzz_base, query, threshold, limit, match_hooks)


def _run_scoring(
    fuzz_base: FuzzBase,
    query: str,
    threshold: float,
    limit: int,
    match_hooks: list[MatchHook] | None = None,
) -> List[dict]:
    if match_hooks is None:
        match_hooks = ["province", "municipality", "barangay"]

    cleaned = _basic_sanitizer(query)
    fb = fuzz_base.fuzzer_base

    f_cols = fuzz_base.resolve_f_columns(list(match_hooks))
    if not f_cols:
        return []

    score_data: dict[str, pd.Series] = {}
    for fc in f_cols:
        score_data[fc] = fb[fc].apply(lambda f: f(s2=cleaned))

    scores_df = pd.DataFrame(score_data)
    max_score = scores_df.max(axis=1)
    cutoff_mask = max_score >= threshold
    if not cutoff_mask.any():
        return []

    winning_col = scores_df.idxmax(axis=1)

    top = (
        fb[cutoff_mask]
        .copy()
        .assign(max_score=max_score[cutoff_mask], _winning_col=winning_col[cutoff_mask])
    )
    top = top.sort_values("max_score", ascending=False).head(limit)

    results = top.to_dict(orient="records")
    requested_set = set(match_hooks)
    for r in results:
        winning = r.pop("_winning_col", "")
        if winning and winning.startswith("f_"):
            raw_col = winning[2:]
            decoded = _decode_column_hooks(raw_col)
            r["_match_hooks"] = [h for h in decoded if h in requested_set]
        else:
            r["_match_hooks"] = []
    return results


def _infer_match_type(raw: dict) -> str:
    if "_match_hooks" in raw and raw["_match_hooks"]:
        return "+".join(raw["_match_hooks"])
    return "unknown"
