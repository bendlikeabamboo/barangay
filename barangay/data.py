import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, List

from pydantic import ValidationError

import pandas as pd

if TYPE_CHECKING:
    pass

# Import new modules
from barangay.data_manager import DataManager
from barangay.models import AdminDivFlat, AdminDivExtended, AdminDiv

import logging

_logger = logging.getLogger(name=__name__)


# Define paths
root_path = Path(os.path.abspath(__file__))
data_dir = root_path.parent / "data"

_BARANGAY_FILENAME = data_dir / "barangay.json"
_BARANGAY_EXTENDED_FILENAME = data_dir / "barangay_extended.json"
_BARANGAY_FLAT_FILENAME = data_dir / "barangay_flat.json"
_FUZZER_BASE_FILENAME = data_dir / "fuzzer_base.parquet"

# DataManager instance for lazy loading
_data_manager = DataManager()


def load_barangay_data(as_of: str | None = None) -> AdminDiv:
    """Loads basic administrative division data.

    Args:
        as_of: Optional date string for specific data version.

    Returns:
        AdminDiv: Validated administrative division data.
    """
    maybe_data: Any = _data_manager.get_data(as_of=as_of, data_type="basic")
    data: AdminDiv = AdminDiv.model_validate(obj=maybe_data)
    return data


def load_barangay_extended_data(as_of: str | None = None) -> AdminDivExtended:
    """Loads extended administrative division data.

    Args:
        as_of: Optional date string for specific data version.

    Returns:
        AdminDivExtended: Validated extended admin division data.
    """
    maybe_data: Any = _data_manager.get_data(as_of=as_of, data_type="extended")
    data: AdminDivExtended = AdminDivExtended.model_validate(obj=maybe_data)
    return data


def load_barangay_flat_data(as_of: str | None = None) -> List[AdminDivFlat]:
    """Loads flat list of administrative division data.

    Args:
        as_of: Optional date string for specific data version.

    Returns:
        List[AdminDivFlat]: List of validated flat admin division entries.
    """
    maybe_data: Any = _data_manager.get_data(as_of=as_of, data_type="flat")
    data: List[AdminDivFlat] = []
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
    """Loads fuzzer base dataframe for fuzzy matching.

    Args:
        as_of: Optional date string for specific data version.

    Returns:
        pd.DataFrame: DataFrame with fuzzer base data.
    """
    data = _data_manager.get_data(as_of=as_of, data_type="fuzzer_base")
    return data  # type: ignore[return-value]


# Load data at module import (backward compatibility)
barangay: AdminDivFlat = load_barangay_data()
barangay_extended: AdminDivExtended = load_barangay_extended_data()
barangay_flat: List[AdminDivFlat] = load_barangay_flat_data()
_fuzzer_base_df = load_fuzzer_base()
