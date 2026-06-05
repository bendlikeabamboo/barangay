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

__all__ = [
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


barangay: AdminDiv = load_barangay_data()
barangay_extended: AdminDivExtended = load_barangay_extended_data()
barangay_flat: list[AdminDivFlat] = load_barangay_flat_data()
_fuzzer_base_df = load_fuzzer_base()
