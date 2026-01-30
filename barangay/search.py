"""
Search functionality for the barangay package.
"""

from typing import Callable, List, Literal

import pandas as pd

from barangay.data import _FUZZER_BASE_DF
from barangay.fuzz import FuzzBase
from barangay.utils import _basic_sanitizer


# Create default fuzz base instance
_default_fuzz_base = FuzzBase(fuzzer_base=_FUZZER_BASE_DF)


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
    fuzz_base: FuzzBase = _default_fuzz_base,
) -> List[dict]:
    """
    Search for barangays using fuzzy string matching.

    This function performs fuzzy matching on barangay names across different
    administrative levels (province, municipality, barangay) and returns
    the top matching results.

    Args:
        search_string: The string to search for
        match_hooks: List of administrative levels to match against.
            Options: "province", "municipality", "barangay"
        threshold: Minimum similarity score (0-100) for a match to be included
        n: Maximum number of results to return
        search_sanitizer: Function to sanitize the search string
        fuzz_base: FuzzBase instance with pre-computed matching functions

    Returns:
        List of dictionaries containing matching barangay data with scores.
        Each dictionary includes:
        - barangay: Barangay name
        - province_or_huc: Province or HUC name
        - municipality_or_city: Municipality or city name
        - psgc_id: Philippine Standard Geographic Code
        - Score columns for each active match type
        - Sanitized versions of the matched strings

    Example:
        >>> results = search("San Jose, Manila")
        >>> for result in results:
        ...     print(f"{result['barangay']}, {result['municipality_or_city']}")
    """
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
