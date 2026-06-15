from __future__ import annotations

import re

__all__ = [
    "_basic_sanitizer",
    "sanitize_input",
    "to_python_identifier",
]

_NON_IDENT = re.compile(r"[^0-9A-Za-z_]+")

_ROMAN_TO_ARABIC: dict[re.Pattern[str], str] = {}
for _roman, _arabic in sorted(
    {
        "ix": "9",
        "viii": "8",
        "vii": "7",
        "vi": "6",
        "iv": "4",
        "v": "5",
        "iii": "3",
        "ii": "2",
        "i": "1",
    }.items(),
    key=lambda item: len(item[0]),
    reverse=True,
):
    _ROMAN_TO_ARABIC[re.compile(rf"\b{_roman}\b", re.IGNORECASE)] = _arabic

_BASIC_EXCLUDE: list[str] = [
    "(pob.)",
    "(pob)",
    "pob.",
    "city of ",
    " city",
    "cluster ",
    " cluster",
    ".",
    "-",
    "(",
    ")",
    "&",
    ",",
]


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


def _basic_sanitizer(input_str: str | None) -> str:
    if input_str is None:
        return ""
    s = input_str.lower()
    for pattern, replacement in _ROMAN_TO_ARABIC.items():
        s = pattern.sub(replacement, s)
    for item in _BASIC_EXCLUDE:
        s = s.replace(item.lower(), "")
    return s
