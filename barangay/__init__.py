"""
List of Barangay in the Philippines
"""

import json
import os
from functools import partial
from pathlib import Path
from typing import Callable, List, Literal
from rapidfuzz import fuzz

import pandas as pd
from pydantic import BaseModel

root_path = Path(os.path.abspath(__file__))
data_dir = root_path.parent / "data"

_BARANGAY_FILENAME = data_dir / "barangay.json"
_BARANGAY_EXTENDED_FILENAME = data_dir / "barangay_extended.json"
_BARANGAY_FLAT_FILENAME = data_dir / "barangay_flat.json"
_FUZZER_BASE_FILENAME = data_dir / "fuzzer_base.parquet"


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
    exclude=["(pob.)", "(pob)", ".", "-", "(", ")", "&", "pob.", ","],
)

_fuzzer_base = pd.read_parquet(_FUZZER_BASE_FILENAME)
_fuzzer_base["0p0b"] = (
    _fuzzer_base["province_or_huc"] + " " + _fuzzer_base["barangay"]
).apply(_basic_sanitizer)
_fuzzer_base["00mb"] = (
    _fuzzer_base["municipality_or_city"].astype(str)
    + " "
    + _fuzzer_base["barangay"].astype(str)
).apply(_basic_sanitizer)
_fuzzer_base["0pmb"] = (
    _fuzzer_base["province_or_huc"].astype(str)
    + " "
    + _fuzzer_base["municipality_or_city"].astype(str)
    + " "
    + _fuzzer_base["barangay"].astype(str)
).apply(_basic_sanitizer)

# TODO: Figure out correct approach here.
# pyright: reportArgumentType=false, reportCallIssue=false
_fuzzer_base["f_00mb_ratio"] = _fuzzer_base["00mb"].apply(
    lambda ref: partial(fuzz.token_sort_ratio, s1=ref)
)
_fuzzer_base["f_0p0b_ratio"] = _fuzzer_base["0p0b"].apply(
    lambda ref: partial(fuzz.token_sort_ratio, s1=ref)
)
_fuzzer_base["f_0pmb_ratio"] = _fuzzer_base["0pmb"].apply(
    lambda ref: partial(fuzz.token_sort_ratio, s1=ref)
)

with open(_BARANGAY_FILENAME, encoding="utf8", mode="r") as file:
    BARANGAY = json.load(file)

with open(_BARANGAY_EXTENDED_FILENAME, encoding="utf8", mode="r") as file:
    BARANGAY_EXTENDED = json.load(file)

with open(_BARANGAY_FLAT_FILENAME, encoding="utf8", mode="r") as file:
    BARANGAY_FLAT = json.load(file)


class BarangayModel(BaseModel):
    barangay: str
    province_or_huc: str
    municipality_or_city: str
    psgc_id: str


def search(
    search_string: str,
    match_hooks: List[Literal["province", "municipality", "barangay"]] = [
        "province",
        "municipality",
        "barangay",
    ],
    threshold: float = 60.0,
    n: int = 1,
    sanitizer: Callable[..., str] = _basic_sanitizer,
) -> List[dict]:
    """
    With a string search
    """
    cleaned_sample: str = sanitizer(search_string)

    active_ratios: List[str] = []
    df: pd.DataFrame = pd.DataFrame()

    # PB
    if "province" in match_hooks and "barangay" in match_hooks:
        df["f_0p0b_ratio" + "_score"] = _fuzzer_base["f_0p0b_ratio"].apply(
            lambda f: f(s2=cleaned_sample)
        )
        active_ratios.append("f_0p0b_ratio_score")

    # MB
    if "municipality" in match_hooks and "barangay" in match_hooks:
        df["f_00mb_ratio" + "_score"] = _fuzzer_base["f_00mb_ratio"].apply(
            lambda f: f(s2=cleaned_sample)
        )
        active_ratios.append("f_00mb_ratio_score")

    # PMB
    if (
        "province" in match_hooks
        and "municipality" in match_hooks
        and "barangay" in match_hooks
    ):
        df["f_0pmb_ratio" + "_score"] = _fuzzer_base["f_0pmb_ratio"].apply(
            lambda f: f(s2=cleaned_sample)
        )
        active_ratios.append("f_0pmb_ratio_score")

    df["max_score"] = df[active_ratios].max(axis=1)
    res_cutoff = pd.DataFrame(df[df["max_score"] >= threshold])
    len_res = len(res_cutoff)
    if len_res < 1:
        return []

    if len_res < n:
        n = len_res
    results = list(res_cutoff.sort_values(by="max_score", ascending=False).index)[0:n]
    truncated_results = pd.DataFrame(_fuzzer_base.loc[results])[
        ["barangay", "province_or_huc", "municipality_or_city", "psgc_id"]
    ]
    return truncated_results.to_dict(orient="records")
