from functools import partial
from typing import Any, Callable, cast

import pandas as pd
from rapidfuzz import fuzz

from barangay.data import load_fuzzer_base
from barangay.utils import _basic_sanitizer

__all__ = [
    "FuzzBase",
    "create_fuzz_base",
    "invalidate_fuzz_cache",
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
            self.fuzzer_base["barangay"].fillna("").astype(str).apply(sanitizer)
        )
        self.fuzzer_base["0p0b"] = (
            self.fuzzer_base["province_or_huc"]
            .fillna("")
            .astype(str)
            .str.cat(self.fuzzer_base["barangay"].fillna("").astype(str), sep=" ")
        ).apply(sanitizer)
        self.fuzzer_base["00mb"] = (
            self.fuzzer_base["municipality_or_city"]
            .fillna("")
            .astype(str)
            .str.cat(self.fuzzer_base["barangay"].fillna("").astype(str), sep=" ")
        ).apply(sanitizer)
        self.fuzzer_base["0pmb"] = (
            self.fuzzer_base["province_or_huc"]
            .fillna("")
            .astype(str)
            .str.cat(
                self.fuzzer_base["municipality_or_city"].fillna("").astype(str), sep=" "
            )
            .str.cat(self.fuzzer_base["barangay"].fillna("").astype(str), sep=" ")
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


_fuzz_base_cache: dict[str | None, FuzzBase] = {}


def create_fuzz_base(as_of: str | None = None) -> FuzzBase:
    if as_of in _fuzz_base_cache:
        return _fuzz_base_cache[as_of]
    fuzzer_base = load_fuzzer_base(as_of=as_of)
    fb = FuzzBase(fuzzer_base=fuzzer_base)
    _fuzz_base_cache[as_of] = fb
    return fb


def invalidate_fuzz_cache() -> None:
    _fuzz_base_cache.clear()
