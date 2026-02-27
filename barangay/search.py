from typing import Callable, List, Literal

import pandas as pd

from barangay.data import load_fuzzer_base
from barangay.fuzz import FuzzBase, create_fuzz_base
from barangay.utils import _basic_sanitizer


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
