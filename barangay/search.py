"""Search functionality for the barangay package.

This module provides fuzzy string matching capabilities for searching Philippine
barangay data across different administrative levels (province, municipality,
barangay). The search function uses the RapidFuzz library for fast and accurate
fuzzy matching.

Main Functions:
    :func:`search`: Main search function for finding barangays using fuzzy matching

Examples:
    Basic search:

    >>> from barangay import search
    >>> results = search("San Jose, Manila")
    >>> for result in results:
    ...     print(f"{result['barangay']}, {result['municipality_or_city']}")

    Search with custom parameters:

    >>> from barangay import search
    >>> results = search(
    ...     "Tongmagen, Tawi-Tawi",
    ...     n=4,
    ...     match_hooks=["municipality", "barangay"],
    ...     threshold=70.0,
    ... )

    Historical data search:

    >>> from barangay import search
    >>> results = search("Tongmageng", as_of="2025-07-08")

See Also:
    :mod:`barangay.fuzz`: Fuzzy matching module
    :mod:`barangay.data`: Data loading module
"""

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
    """Search for barangays using fuzzy string matching.

    This function performs fuzzy matching on barangay names across different
    administrative levels (province, municipality, barangay) using the
    RapidFuzz library's token_sort_ratio algorithm. It returns the top matching
    results sorted by similarity score.

    The function supports multiple matching strategies based on the combination
    of match_hooks:
        - B (Barangay only): Match against barangay names only
        - PB (Province + Barangay): Match against province and barangay names
        - MB (Municipality + Barangay): Match against municipality and barangay names
        - PMB (Province + Municipality + Barangay): Match against all three levels

    Args:
        search_string: The string to search for. This can be a partial address,
            a barangay name, or any combination of administrative levels.
        match_hooks: List of administrative levels to match against. Valid options
            are "province", "municipality", and "barangay". Default is all three.
        threshold: Minimum similarity score (0-100) for a match to be included in
            the results. Lower values return more results but with lower confidence.
        n: Maximum number of results to return. Results are sorted by similarity
            score in descending order.
        search_sanitizer: Function to sanitize the search string before matching.
            The default sanitizer removes common prefixes/suffixes and normalizes
            the string.
        fuzz_base: FuzzBase instance with pre-computed matching functions. If None,
            a new instance is created using the as_of date. Reusing a FuzzBase
            instance can improve performance for multiple searches.
        as_of: Date string (YYYY-MM-DD) or None for latest data. Only used if
            fuzz_base is None. Allows searching historical data from specific dates.

    Returns:
        List[dict]: A list of dictionaries containing matching barangay data with
        scores. Each dictionary includes:

        - barangay (str): Barangay name
        - province_or_huc (str): Province or Highly Urbanized City name
        - municipality_or_city (str): Municipality or city name
        - psgc_id (str): Philippine Standard Geographic Code
        - max_score (float): Maximum similarity score across all active match types
        - f_000b_ratio_score (float): Score for barangay-only matching
        - f_0p0b_ratio_score (float): Score for province + barangay matching
        - f_00mb_ratio_score (float): Score for municipality + barangay matching
        - f_0pmb_ratio_score (float): Score for all three levels matching
        - 000b (str): Sanitized barangay name
        - 0p0b (str): Sanitized province + barangay string
        - 00mb (str): Sanitized municipality + barangay string
        - 0pmb (str): Sanitized province + municipality + barangay string

    Raises:
        ValueError: If match_hooks contains invalid values.

    Examples:
        Basic search:

        >>> from barangay import search
        >>> results = search("Tongmageng, Tawi-Tawi")
        >>> print(results[0]['barangay'])
        Tongmageng

        Search with custom parameters:

        >>> from barangay import search
        >>> results = search(
        ...     "Tongmagen, Tawi-Tawi",
        ...     n=4,
        ...     match_hooks=["municipality", "barangay"],
        ...     threshold=70.0,
        ... )
        >>> for result in results:
        ...     print(f"{result['barangay']} (score: {result['max_score']})")

        Historical data search:

        >>> from barangay import search
        >>> results = search("Tongmageng", as_of="2025-07-08")

        Using a custom sanitizer:

        >>> from barangay import search, sanitize_input
        >>> results = search(
        ...     "City of San Jose",
        ...     search_sanitizer=lambda x: sanitize_input(x, exclude=["city of "]),
        ... )

    See Also:
        :class:`FuzzBase`: Class for pre-computing fuzzy matching functions
        :func:`create_fuzz_base`: Factory function to create FuzzBase instances
        :func:`sanitize_input`: String sanitization utility
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
