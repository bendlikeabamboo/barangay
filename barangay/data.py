"""
Data loading functionality for the barangay package.
"""

import json
import os
from pathlib import Path

import pandas as pd


# Define paths
root_path = Path(os.path.abspath(__file__))
data_dir = root_path.parent / "data"

_BARANGAY_FILENAME = data_dir / "barangay.json"
_BARANGAY_EXTENDED_FILENAME = data_dir / "barangay_extended.json"
_BARANGAY_FLAT_FILENAME = data_dir / "barangay_flat.json"
_FUZZER_BASE_FILENAME = data_dir / "fuzzer_base.parquet"


def load_barangay_data() -> dict:
    """
    Load the basic barangay data from JSON file.

    Returns:
        Dictionary containing barangay data
    """
    with open(_BARANGAY_FILENAME, encoding="utf8", mode="r") as file:
        return json.load(file)


def load_barangay_extended_data() -> dict:
    """
    Load the extended barangay data from JSON file.

    Returns:
        Dictionary containing extended barangay data
    """
    with open(_BARANGAY_EXTENDED_FILENAME, encoding="utf8", mode="r") as file:
        return json.load(file)


def load_barangay_flat_data() -> dict:
    """
    Load the flat barangay data from JSON file.

    Returns:
        Dictionary containing flat barangay data
    """
    with open(_BARANGAY_FLAT_FILENAME, encoding="utf8", mode="r") as file:
        return json.load(file)


def load_fuzzer_base() -> pd.DataFrame:
    """
    Load the fuzzer base data from parquet file.

    Returns:
        DataFrame containing pre-processed data for fuzzy matching
    """
    return pd.read_parquet(_FUZZER_BASE_FILENAME)


# Load data at module import
BARANGAY = load_barangay_data()
BARANGAY_EXTENDED = load_barangay_extended_data()
BARANGAY_FLAT = load_barangay_flat_data()
_FUZZER_BASE_DF = load_fuzzer_base()
