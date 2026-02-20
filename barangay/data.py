"""Data loading functionality for the barangay package.

This module provides functions for loading Philippine barangay data in different
formats. It supports loading data from bundled package files, local cache,
or downloading from GitHub repository.

Main Functions:
    :func:`load_barangay_data`: Load basic barangay data
    :func:`load_barangay_extended_data`: Load extended barangay data
    :func:`load_barangay_flat_data`: Load flat barangay data
    :func:`load_fuzzer_base`: Load fuzzer base data for fuzzy matching

Data Structures:
    :data:`BARANGAY`: Basic barangay data dictionary (nested structure)
    :data:`BARANGAY_EXTENDED`: Extended barangay data dictionary (recursive with metadata)
    :data:`BARANGAY_FLAT`: Flat barangay data dictionary (list with parent references)

Data Models:
    Basic (BARANGAY):
        Nested dictionary structure: region -> city/municipality -> barangay
        Best for: Simple lookups and hierarchical access

    Extended (BARANGAY_EXTENDED):
        Recursive structure with rich metadata
        Best for: Complex hierarchies and detailed information

    Flat (BARANGAY_FLAT):
        Flat list with parent references
        Best for: Search, filtering, and DataFrame operations

Examples:
    Loading basic data:

    >>> from barangay import load_barangay_data
    >>> data = load_barangay_data()
    >>> print(list(data.keys())[:3])
    ['National Capital Region (NCR)', 'Region I (Ilocos Region)', 'Region II (Cagayan Valley)']

    Loading historical data:

    >>> from barangay import load_barangay_data
    >>> data = load_barangay_data(as_of="2025-07-08")

    Loading extended data:

    >>> from barangay import load_barangay_extended_data
    >>> data = load_barangay_extended_data()

    Loading flat data:

    >>> from barangay import load_barangay_flat_data
    >>> data = load_barangay_flat_data()

    Loading fuzzer base:

    >>> from barangay import load_fuzzer_base
    >>> df = load_fuzzer_base()
    >>> print(df.columns.tolist())
    ['barangay', 'province_or_huc', 'municipality_or_city', 'psgc_id', ...]

See Also:
    :mod:`barangay.data_manager`: Data management module
    :mod:`barangay.fuzz`: Fuzzy matching module
"""

import os
from pathlib import Path
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    pass

# Import new modules
from barangay.data_manager import DataManager

# Define paths
root_path = Path(os.path.abspath(__file__))
data_dir = root_path.parent / "data"

_BARANGAY_FILENAME = data_dir / "barangay.json"
_BARANGAY_EXTENDED_FILENAME = data_dir / "barangay_extended.json"
_BARANGAY_FLAT_FILENAME = data_dir / "barangay_flat.json"
_FUZZER_BASE_FILENAME = data_dir / "fuzzer_base.parquet"

# DataManager instance for lazy loading
_data_manager = DataManager()


def load_barangay_data(as_of: str | None = None) -> dict:
    """Load basic barangay data from JSON file.

    This function loads the basic barangay data, which is organized as a
    nested dictionary structure: region -> city/municipality -> barangay.

    The data can be loaded from the bundled package files, local cache,
    or downloaded from GitHub repository depending on the as_of parameter.

    Args:
        as_of: Date string (YYYY-MM-DD) or None for latest data.
            If specified, the function will attempt to load data from the
            closest available dataset on or before the requested date.

    Returns:
        dict: A nested dictionary containing barangay data. The structure is:
            {
                "Region Name": {
                    "City/Municipality Name": {
                        "Barangay Name": "PSGC Code",
                        ...
                    },
                    ...
                },
                ...
            }

    Examples:
        Loading latest data:

        >>> from barangay import load_barangay_data
        >>> data = load_barangay_data()
        >>> ncr = data["National Capital Region (NCR)"]
        >>> print(list(ncr.keys())[:3])
        ['City of Manila', 'Quezon City', 'Caloocan City']

        Loading historical data:

        >>> from barangay import load_barangay_data
        >>> data = load_barangay_data(as_of="2025-07-08")

    See Also:
        :func:`load_barangay_extended_data`: Load extended barangay data
        :func:`load_barangay_flat_data`: Load flat barangay data
        :data:`BARANGAY`: Pre-loaded basic barangay data
    """
    data = _data_manager.get_data(as_of=as_of, data_type="basic")
    return data  # type: ignore[return-value]


def load_barangay_extended_data(as_of: str | None = None) -> dict:
    """Load extended barangay data from JSON file.

    This function loads the extended barangay data, which is organized as
    a recursive structure with rich metadata including population, area, and
    other administrative information.

    The data can be loaded from the bundled package files, local cache,
    or downloaded from GitHub repository depending on the as_of parameter.

    Args:
        as_of: Date string (YYYY-MM-DD) or None for latest data.
            If specified, the function will attempt to load data from the
            closest available dataset on or before the requested date.

    Returns:
        dict: A recursive dictionary containing extended barangay data with
            metadata. The structure includes nested administrative levels
            with additional information for each level.

    Examples:
        Loading latest data:

        >>> from barangay import load_barangay_extended_data
        >>> data = load_barangay_extended_data()
        >>> print(list(data.keys())[:3])
        ['National Capital Region (NCR)', 'Region I (Ilocos Region)', ...]

        Loading historical data:

        >>> from barangay import load_barangay_extended_data
        >>> data = load_barangay_extended_data(as_of="2025-07-08")

    See Also:
        :func:`load_barangay_data`: Load basic barangay data
        :func:`load_barangay_flat_data`: Load flat barangay data
        :data:`BARANGAY_EXTENDED`: Pre-loaded extended barangay data
    """
    data = _data_manager.get_data(as_of=as_of, data_type="extended")
    return data  # type: ignore[return-value]


def load_barangay_flat_data(as_of: str | None = None) -> dict:
    """Load flat barangay data from JSON file.

    This function loads the flat barangay data, which is organized as a
    flat list with parent references. This format is ideal for search
    operations, filtering, and conversion to pandas DataFrames.

    The data can be loaded from the bundled package files, local cache,
    or downloaded from GitHub repository depending on the as_of parameter.

    Args:
        as_of: Date string (YYYY-MM-DD) or None for latest data.
            If specified, the function will attempt to load data from the
            closest available dataset on or before the requested date.

    Returns:
        dict: A dictionary containing a flat list of barangay data with
            parent references. The structure is:
            {
                "barangays": [
                    {
                        "barangay": "Barangay Name",
                        "province_or_huc": "Province Name",
                        "municipality_or_city": "City/Municipality Name",
                        "psgc_id": "PSGC Code",
                        ...
                    },
                    ...
                ]
            }

    Examples:
        Loading latest data:

        >>> from barangay import load_barangay_flat_data
        >>> data = load_barangay_flat_data()
        >>> barangays = data.get("barangays", [])
        >>> print(barangays[0])
        {'barangay': 'Barangay 1', 'province_or_huc': 'Province A', ...}

        Loading historical data:

        >>> from barangay import load_barangay_flat_data
        >>> data = load_barangay_flat_data(as_of="2025-07-08")

        Converting to DataFrame:

        >>> import pandas as pd
        >>> from barangay import load_barangay_flat_data
        >>> data = load_barangay_flat_data()
        >>> df = pd.DataFrame(data["barangays"])
        >>> print(df.head())

    See Also:
        :func:`load_barangay_data`: Load basic barangay data
        :func:`load_barangay_extended_data`: Load extended barangay data
        :data:`BARANGAY_FLAT`: Pre-loaded flat barangay data
    """
    data = _data_manager.get_data(as_of=as_of, data_type="flat")
    return data  # type: ignore[return-value]


def load_fuzzer_base(as_of: str | None = None) -> pd.DataFrame:
    """Load fuzzer base data from parquet file.

    This function loads the pre-processed fuzzer base data, which is used
    for efficient fuzzy matching operations. The data includes sanitized versions
    of barangay names and pre-computed partial functions for matching.

    The data can be loaded from the bundled package files, local cache,
    or downloaded from GitHub repository depending on the as_of parameter.

    Args:
        as_of: Date string (YYYY-MM-DD) or None for latest data.
            If specified, the function will attempt to load data from the
            closest available dataset on or before the requested date.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the pre-processed fuzzer
            base data. The DataFrame includes columns for:
            - barangay: Barangay name
            - province_or_huc: Province or HUC name
            - municipality_or_city: Municipality or city name
            - psgc_id: Philippine Standard Geographic Code
            - 000b: Sanitized barangay name only
            - 0p0b: Sanitized province + barangay string
            - 00mb: Sanitized municipality + barangay string
            - 0pmb: Sanitized province + municipality + barangay string
            - f_000b_ratio: Pre-computed partial function for barangay-only matching
            - f_0p0b_ratio: Pre-computed partial function for province + barangay matching
            - f_00mb_ratio: Pre-computed partial function for municipality + barangay matching
            - f_0pmb_ratio: Pre-computed partial function for all three levels matching

    Examples:
        Loading latest data:

        >>> from barangay import load_fuzzer_base
        >>> df = load_fuzzer_base()
        >>> print(df.columns.tolist())
        ['barangay', 'province_or_huc', 'municipality_or_city', 'psgc_id', ...]

        Loading historical data:

        >>> from barangay import load_fuzzer_base
        >>> df = load_fuzzer_base(as_of="2025-07-08")

        Using with FuzzBase:

        >>> from barangay import load_fuzzer_base, FuzzBase
        >>> df = load_fuzzer_base()
        >>> fuzz_base = FuzzBase(fuzzer_base=df)

    See Also:
        :class:`FuzzBase`: Fuzzy matching class
        :func:`create_fuzz_base`: Factory function to create FuzzBase instances
    """
    data = _data_manager.get_data(as_of=as_of, data_type="fuzzer_base")
    return data  # type: ignore[return-value]


# Load data at module import (backward compatibility)
BARANGAY = load_barangay_data()
BARANGAY_EXTENDED = load_barangay_extended_data()
BARANGAY_FLAT = load_barangay_flat_data()
_FUZZER_BASE_DF = load_fuzzer_base()
