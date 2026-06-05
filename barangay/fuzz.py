from functools import partial
from typing import Any, Callable, cast

import pandas as pd
from rapidfuzz import fuzz

from barangay.data import load_fuzzer_base
from barangay.utils import _basic_sanitizer

__all__ = [
    "FuzzBase",
    "create_fuzz_base",
]


class FuzzBase:
    def __init__(
        self,
        *,
        fuzzer_base: pd.DataFrame,
        sanitizer: Callable[[str | None], str] = _basic_sanitizer,
    ):
        self.fuzzer_base = fuzzer_base.copy()
        self.sanitizer = sanitizer

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
    fuzzer_base = load_fuzzer_base(as_of=as_of)
    return FuzzBase(fuzzer_base=fuzzer_base)


_default_fuzz_base = FuzzBase(fuzzer_base=load_fuzzer_base())
