import os
from pathlib import Path
from typing import Any, Collection

from pydantic import ValidationError

import pandas as pd

from barangay.data_manager import DataManager
from barangay.models import AdminDivFlat, AdminDivExtended, AdminDiv

import logging

_logger = logging.getLogger(name=__name__)

root_path = Path(os.path.abspath(__file__))
data_dir = root_path.parent / "data"

_BARANGAY_FILENAME = data_dir / "barangay.json"
_BARANGAY_EXTENDED_FILENAME = data_dir / "barangay_extended.json"
_BARANGAY_FLAT_FILENAME = data_dir / "barangay_flat.json"
_FUZZER_BASE_FILENAME = data_dir / "fuzzer_base.parquet"

_data_manager = DataManager()

__all__ = [  # noqa: F822
    "barangay",
    "barangay_extended",
    "barangay_flat",
    "load_barangay_data",
    "load_barangay_extended_data",
    "load_barangay_flat_data",
    "load_fuzzer_base",
]


def load_barangay_data(as_of: str | None = None) -> AdminDiv:
    maybe_data: Any = _data_manager.get_data(as_of=as_of, data_type="basic")
    data: AdminDiv = AdminDiv.model_validate(obj=maybe_data)
    return data


def load_barangay_extended_data(as_of: str | None = None) -> AdminDivExtended:
    maybe_data: Any = _data_manager.get_data(as_of=as_of, data_type="extended")
    data: AdminDivExtended = AdminDivExtended.model_validate(obj=maybe_data)
    return data


def load_barangay_flat_data(as_of: str | None = None) -> list[AdminDivFlat]:
    maybe_data: Any = _data_manager.get_data(as_of=as_of, data_type="flat")
    if not isinstance(maybe_data, Collection) or isinstance(maybe_data, (str, bytes)):
        raise ValueError("Invalid data fetched.")
    data: list[AdminDivFlat] = []
    for maybe_datum in maybe_data:
        try:
            data.append(AdminDivFlat.model_validate(obj=maybe_datum))
        except ValidationError as e:
            _logger.warning(
                "Invalid data, must conform to AdminDivFlat: %s", maybe_datum
            )
            _logger.warning(e)
    return data


def load_fuzzer_base(as_of: str | None = None) -> pd.DataFrame:
    data = _data_manager.get_data(as_of=as_of, data_type="fuzzer_base")
    return data


_barangay: AdminDiv | None = None
_barangay_extended: AdminDivExtended | None = None
_barangay_flat: list[AdminDivFlat] | None = None
_fuzzer_base_df: pd.DataFrame | None = None

_LAZY_ATTRS = {"barangay", "barangay_extended", "barangay_flat", "_fuzzer_base_df"}


def __getattr__(name: str):
    global _barangay, _barangay_extended, _barangay_flat, _fuzzer_base_df
    if name not in _LAZY_ATTRS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    if name == "barangay":
        if _barangay is None:
            _barangay = load_barangay_data()
        return _barangay
    if name == "barangay_extended":
        if _barangay_extended is None:
            _barangay_extended = load_barangay_extended_data()
        return _barangay_extended
    if name == "barangay_flat":
        if _barangay_flat is None:
            _barangay_flat = load_barangay_flat_data()
        return _barangay_flat
    if name == "_fuzzer_base_df":
        if _fuzzer_base_df is None:
            _fuzzer_base_df = load_fuzzer_base()
        return _fuzzer_base_df
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
