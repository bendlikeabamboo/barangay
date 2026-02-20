"""Utility functions for barangay package.

This module provides utility functions for string sanitization and data processing.
These utilities are used internally by the search and fuzzy matching modules.

Main Functions:
    :func:`sanitize_input`: Remove whitespaces, lowercase, and remove excluded strings

Constants:
    :data:`_basic_sanitizer`: Pre-configured sanitizer with common exclusions

Examples:
    Basic sanitization:

    >>> from barangay import sanitize_input
    >>> sanitized = sanitize_input("City of San Jose")
    >>> print(sanitized)
    san jose

    With custom exclusions:

    >>> from barangay import sanitize_input
    >>> sanitized = sanitize_input("Barangay (Pob.)", exclude=["(pob.)"])
    >>> print(sanitized)
    barangay

    Using the basic sanitizer:

    >>> from barangay.utils import _basic_sanitizer
    >>> sanitized = _basic_sanitizer("City of Manila")
    >>> print(sanitized)
    manila

See Also:
    :mod:`barangay.search`: Search functionality module
    :mod:`barangay.fuzz`: Fuzzy matching module
"""

from functools import partial
from typing import List


def sanitize_input(
    input_str: str | None, exclude: List[str] | str | None = None
) -> str:
    """Remove whitespaces, lowercase, and remove all strings listed in exclude.

    This function sanitizes input strings by:
        1. Converting to lowercase
        2. Removing leading/trailing whitespace
        3. Removing all strings specified in the exclude parameter

    If the input is None or not a string, it is converted to an empty string.

    Args:
        input_str: Input string to sanitize. Can be None, which will be
            converted to an empty string.
        exclude: String or list of strings to remove from the input after
            lowercasing. If None, no additional strings are removed beyond
            the default lowercasing and whitespace removal.

    Returns:
        str: The sanitized string in lowercase with excluded strings removed.

    Examples:
        Basic sanitization:

        >>> from barangay import sanitize_input
        >>> sanitized = sanitize_input("City of San Jose")
        >>> print(sanitized)
        san jose

        With None input:

        >>> from barangay import sanitize_input
        >>> sanitized = sanitize_input(None)
        >>> print(sanitized)

        With custom exclusions:

        >>> from barangay import sanitize_input
        >>> sanitized = sanitize_input(
        ...     "Barangay (Pob.)",
        ...     exclude=["(pob.)"]
        ... )
        >>> print(sanitized)
        barangay

        With multiple exclusions:

        >>> from barangay import sanitize_input
        >>> sanitized = sanitize_input(
        ...     "City of Manila, NCR",
        ...     exclude=["city of ", ", ncr"]
        ... )
        >>> print(sanitized)
        manila

        With non-string input:

        >>> from barangay import sanitize_input
        >>> sanitized = sanitize_input(123)
        >>> print(sanitized)

    See Also:
        :data:`_basic_sanitizer`: Pre-configured sanitizer with common exclusions
    """
    if input_str is None:
        input_str = ""
    if not isinstance(input_str, str):
        input_str = ""
    sanitized_str = input_str.lower()
    if exclude is None:
        return sanitized_str

    if isinstance(exclude, list):
        exclude = [x.lower() for x in exclude if isinstance(x, str)]
        for item in exclude:
            sanitized_str = sanitized_str.replace(item, "")
        return sanitized_str

    return sanitized_str.replace(exclude.lower(), "")


_basic_sanitizer = partial(
    sanitize_input,
    exclude=[
        "(pob.)",
        "(pob)",
        "pob.",
        "city of ",
        " city",
        ".",
        "-",
        "(",
        ")",
        "&",
        ",",
    ],
)
"""Pre-configured sanitizer with common exclusions.

This is a partial function of :func:`sanitize_input` with a predefined
list of common strings to exclude from barangay names and addresses.

The exclusions include:
    - "(pob.)": Place of birth abbreviation
    - "(pob)": Place of birth abbreviation
    - "pob.": Place of birth abbreviation
    - "city of ": Common prefix
    - " city": Common suffix
    ".": Periods
    "-": Hyphens
    "(": Opening parentheses
    ")": Closing parentheses
    "&": Ampersands
    ",": Commas

Examples:
    Using the basic sanitizer:

    >>> from barangay.utils import _basic_sanitizer
    >>> sanitized = _basic_sanitizer("City of Manila")
    >>> print(sanitized)
    manila

    >>> from barangay.utils import _basic_sanitizer
    >>> sanitized = _basic_sanitizer("Barangay (Pob.)")
    >>> print(sanitized)
    barangay

    >>> from barangay.utils import _basic_sanitizer
    >>> sanitized = _basic_sanitizer("San Jose, City")
    >>> print(sanitized)
    san jose

See Also:
    :func:`sanitize_input`: String sanitization function
"""
