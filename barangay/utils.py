from __future__ import annotations

import re
from functools import partial

__all__ = [
    "_basic_sanitizer",
    "sanitize_input",
    "to_python_identifier",
]

_NON_IDENT = re.compile(r"[^0-9A-Za-z_]+")


def to_python_identifier(name: str) -> str:
    s = _NON_IDENT.sub("_", name)
    if not s:
        return "_"
    while "__" in s:
        s = s.replace("__", "_")
    s = s.strip("_")
    if not s:
        return "_"
    if s[0].isdigit():
        s = f"_{s}"
    return s


def sanitize_input(
    input_str: str | None, exclude: list[str] | str | None = None
) -> str:
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
