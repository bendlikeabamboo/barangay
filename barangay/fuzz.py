"""Fuzzy matching functionality for the barangay package.

This module provides the FuzzBase class and related functions for performing
fuzzy string matching on Philippine barangay data. The module uses the RapidFuzz
library for fast and accurate fuzzy matching based on token sort ratio.

Main Classes and Functions:
    :class:`FuzzBase`: Class for pre-computing fuzzy matching functions
    :func:`create_fuzz_base`: Factory function to create FuzzBase instances

The FuzzBase class prepares a DataFrame with pre-computed partial functions for
efficient searching across different administrative levels. This pre-computation
significantly improves performance when performing multiple searches.

Matching Strategies:
    - B (Barangay only): Match against barangay names only
    - PB (Province + Barangay): Match against province and barangay names
    - MB (Municipality + Barangay): Match against municipality and barangay names
    - PMB (Province + Municipality + Barangay): Match against all three levels

Examples:
    Creating a FuzzBase instance:

    >>> from barangay import FuzzBase
    >>> fuzz_base = FuzzBase(fuzzer_base=your_dataframe)

    Using create_fuzz_base factory:

    >>> from barangay import create_fuzz_base
    >>> fuzz_base = create_fuzz_base(as_of="2025-07-08")

    Using FuzzBase with search:

    >>> from barangay import search, create_fuzz_base
    >>> fuzz_base = create_fuzz_base()
    >>> results = search("Tongmageng", fuzz_base=fuzz_base)

See Also:
    :mod:`barangay.search`: Search functionality module
    :mod:`barangay.data`: Data loading module
"""

from functools import partial
from typing import Any, Callable, cast

import pandas as pd
from rapidfuzz import fuzz

from barangay.data import load_fuzzer_base
from barangay.utils import _basic_sanitizer


class FuzzBase:
    """Base class for fuzzy matching operations on barangay data.

    This class prepares a DataFrame with pre-computed fuzzy matching functions
    for efficient searching across different administrative levels. The pre-computation
    uses RapidFuzz's token_sort_ratio algorithm to create partial functions that
    can be quickly applied to search strings.

    The class creates four different matching strategies:
        - 000b: Barangay name only
        - 0p0b: Province + Barangay names
        - 00mb: Municipality + Barangay names
        - 0pmb: Province + Municipality + Barangay names

    Each strategy has both a sanitized string version (e.g., "000b") and a
    pre-computed partial function (e.g., "f_000b_ratio") for fast matching.

    Attributes:
        fuzzer_base: DataFrame containing barangay data with pre-computed fuzzy
            matching functions. The DataFrame includes columns for barangay names,
            province/HUC names, municipality/city names, PSGC IDs, and the four
            matching strategies with their corresponding partial functions.
        sanitizer: Sanitizer function used to normalize strings before matching.
            The default sanitizer removes common prefixes/suffixes and converts
            to lowercase.

    Examples:
        Creating a FuzzBase instance:

        >>> from barangay import FuzzBase
        >>> import pandas as pd
        >>> data = pd.DataFrame({
        ...     'barangay': ['Barangay 1', 'Barangay 2'],
        ...     'province_or_huc': ['Province A', 'Province B'],
        ...     'municipality_or_city': ['City 1', 'City 2'],
        ... })
        >>> fuzz_base = FuzzBase(fuzzer_base=data)

        Using with search function:

        >>> from barangay import search, create_fuzz_base
        >>> fuzz_base = create_fuzz_base()
        >>> results = search("Tongmageng", fuzz_base=fuzz_base)

    See Also:
        :func:`create_fuzz_base`: Factory function to create FuzzBase instances
        :func:`search`: Search function using FuzzBase
    """

    def __init__(
        self,
        *,
        fuzzer_base: pd.DataFrame,
        sanitizer: Callable[..., str] = _basic_sanitizer,
    ):
        """Initialize the FuzzBase with a DataFrame and sanitizer.

        The constructor creates sanitized versions of the barangay data for each
        matching strategy and pre-computes partial functions for fuzzy matching.
        This pre-computation significantly improves performance when performing
        multiple searches.

        Args:
            fuzzer_base: DataFrame containing barangay data with the following
                required columns:
                - barangay: Barangay name
                - province_or_huc: Province or Highly Urbanized City name
                - municipality_or_city: Municipality or city name
                - psgc_id: Philippine Standard Geographic Code (optional but recommended)
            sanitizer: Function to sanitize input strings for matching. The function
                should take a string and return a sanitized version. The default
                sanitizer removes common prefixes/suffixes and converts to lowercase.

        Examples:
            Basic initialization:

            >>> from barangay import FuzzBase
            >>> fuzz_base = FuzzBase(fuzzer_base=your_dataframe)

            With custom sanitizer:

            >>> from barangay import FuzzBase, sanitize_input
            >>> custom_sanitizer = lambda x: sanitize_input(x, exclude=["city of "])
            >>> fuzz_base = FuzzBase(fuzzer_base=your_dataframe, sanitizer=custom_sanitizer)

        See Also:
            :func:`create_fuzz_base`: Factory function to create FuzzBase instances
            :func:`sanitize_input`: String sanitization utility
        """
        self.fuzzer_base = fuzzer_base.copy()
        self.sanitizer = sanitizer

        # rpmb = region, province, municipality, barangay
        self.fuzzer_base["000b"] = (
            self.fuzzer_base["barangay"].astype(str).apply(sanitizer)
        )
        self.fuzzer_base["0p0b"] = (
            self.fuzzer_base["province_or_huc"]
            .astype(str)
            .str.cat(self.fuzzer_base["barangay"].astype(str), sep=" ")
        ).apply(sanitizer)
        self.fuzzer_base["00mb"] = (
            self.fuzzer_base["municipality_or_city"]
            .astype(str)
            .str.cat(self.fuzzer_base["barangay"].astype(str), sep=" ")
        ).apply(sanitizer)
        self.fuzzer_base["0pmb"] = (
            self.fuzzer_base["province_or_huc"]
            .astype(str)
            .str.cat(self.fuzzer_base["municipality_or_city"].astype(str), sep=" ")
            .str.cat(self.fuzzer_base["barangay"].astype(str), sep=" ")
        ).apply(sanitizer)

        # Store partial functions for fuzzy matching - cast to Any since pandas doesn't
        # support callable column types
        self.fuzzer_base["f_000b_ratio"] = cast(
            Any,
            self.fuzzer_base["000b"].apply(
                cast(
                    Callable[[str], Any],
                    lambda ref: partial(fuzz.token_sort_ratio, s1=ref),
                )
            ),
        )
        self.fuzzer_base["f_00mb_ratio"] = cast(
            Any,
            self.fuzzer_base["00mb"].apply(
                cast(
                    Callable[[str], Any],
                    lambda ref: partial(fuzz.token_sort_ratio, s1=ref),
                )
            ),
        )
        self.fuzzer_base["f_0p0b_ratio"] = cast(
            Any,
            self.fuzzer_base["0p0b"].apply(
                cast(
                    Callable[[str], Any],
                    lambda ref: partial(fuzz.token_sort_ratio, s1=ref),
                )
            ),
        )
        self.fuzzer_base["f_0pmb_ratio"] = cast(
            Any,
            self.fuzzer_base["0pmb"].apply(
                cast(
                    Callable[[str], Any],
                    lambda ref: partial(fuzz.token_sort_ratio, s1=ref),
                )
            ),
        )


def create_fuzz_base(as_of: str | None = None) -> FuzzBase:
    """Create a FuzzBase instance with optional date resolution.

    This is a factory function that loads barangay data and creates a FuzzBase
    instance for fuzzy matching. It supports loading historical data by specifying
    an as_of date.

    Args:
        as_of: Date string (YYYY-MM-DD) or None for latest data. If specified,
            the function will attempt to load data from the closest available
            dataset on or before the requested date. If None, the latest bundled
            data is used.

    Returns:
        FuzzBase: A FuzzBase instance initialized with data from the specified
        date (or latest if as_of is None).

    Examples:
        Create FuzzBase with latest data:

        >>> from barangay import create_fuzz_base
        >>> fuzz_base = create_fuzz_base()

        Create FuzzBase with historical data:

        >>> from barangay import create_fuzz_base
        >>> fuzz_base = create_fuzz_base(as_of="2025-07-08")

        Use with search function:

        >>> from barangay import search, create_fuzz_base
        >>> fuzz_base = create_fuzz_base(as_of="2025-08-29")
        >>> results = search("Tongmageng", fuzz_base=fuzz_base)

    See Also:
        :class:`FuzzBase`: FuzzBase class for fuzzy matching operations
        :func:`load_fuzzer_base`: Load fuzzer base data
        :func:`search`: Search function using FuzzBase
    """
    fuzzer_base = load_fuzzer_base(as_of=as_of)
    return FuzzBase(fuzzer_base=fuzzer_base)


# Create default fuzz base instance (backward compatibility)
_default_fuzz_base = FuzzBase(fuzzer_base=load_fuzzer_base())
