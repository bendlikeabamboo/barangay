"""
Utility functions for the barangay package.
"""

from functools import partial
from typing import List


def sanitize_input(
    input_str: str | None, exclude: List[str] | str | None = None
) -> str:
    """
    Removes whitespaces, lowers, and remove all strings listed in exclude. If
    data is incompatible, will coerce to empty string.
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
