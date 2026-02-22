"""Barangay: Philippine Geographic/Administrative Data Package

This package provides comprehensive tools for searching and working with Philippine
barangay data, including fuzzy matching capabilities, multiple data formats,
and historical data access.

Features:
    - **Fuzzy Search**: Fast, customizable matching for unstandardized addresses
    - **Multiple Data Models**: Basic (nested), Extended (recursive), and Flat (list)
    - **Historical Data**: Access previous PSGC releases by date
    - **Smart Caching**: Automatic caching for faster subsequent loads
    - **On-demand Download**: Download historical data from GitHub repository

Main Exports:
    - :func:`search`: Main search function for finding barangays
    - :class:`FuzzBase`: Class for fuzzy matching operations
    - :class:`BarangayModel`: Pydantic model for barangay data
    - :class:`DataManager`: Manages data loading, caching, and downloading
    - :data:`BARANGAY`: Basic barangay data dictionary
    - :data:`BARANGAY_EXTENDED`: Extended barangay data dictionary
    - :data:`BARANGAY_FLAT`: Flat barangay data dictionary
    - :func:`sanitize_input`: Utility function for string sanitization
    - :func:`create_fuzz_base`: Factory function to create FuzzBase instances
    - :func:`get_available_dates`: Get list of available historical dates
    - :func:`resolve_date`: Resolve approximate dates to closest available dataset
    - :func:`load_env_config`: Load configuration from environment variables
    - :func:`resolve_as_of`: Resolve as_of date from multiple layers
    - :func:`get_verbose`: Get verbose logging setting
    - :func:`get_cache_dir`: Get cache directory path

Module-Level Attributes:
    - :data:`current`: Current dataset date (from CURRENT_VERSION file)
    - :data:`as_of`: Default dataset date for this session (default: None)
    - :data:`available_dates`: All available dataset dates (including current)

Examples:
    Basic search:

    >>> from barangay import search
    >>> results = search("Tongmageng, Tawi-Tawi")
    >>> print(results[0]['barangay'])
    Tongmageng

    Access data directly:

    >>> from barangay import BARANGAY
    >>> ncr_cities = list(BARANGAY["National Capital Region (NCR)"].keys())
    >>> print(ncr_cities[:3])
    ['City of Manila', 'Quezon City', 'Caloocan City']

    Search with custom parameters:

    >>> from barangay import search
    >>> results = search(
    ...     "Tongmagen, Tawi-Tawi",
    ...     n=4,
    ...     match_hooks=["municipality", "barangay"],
    ...     threshold=70.0,
    ... )
    >>> for result in results:
    ...     print(f"{result['barangay']} (score: {result['max_score']})")

    Historical data search:

    >>> from barangay import search
    >>> results = search("Tongmageng", as_of="2025-07-08")

See Also:
    :mod:`barangay.search`: Search functionality module
    :mod:`barangay.fuzz`: Fuzzy matching module
    :mod:`barangay.data_manager`: Data management module
    :mod:`barangay.models`: Pydantic models module
    :mod:`barangay.config`: Configuration module
    :mod:`barangay.date_resolver`: Date resolution module
"""

from pathlib import Path

# Read CURRENT_VERSION file to set module attribute
_current_version_path = Path(__file__).parent / "data" / "CURRENT_VERSION"
_current = (
    _current_version_path.read_text().strip()
    if _current_version_path.exists()
    else "2026-01-13"
)

# Module-level attributes
current: str = _current
as_of: str | None = None
available_dates: list[str] = []

# Import data
from barangay.data import (  # noqa:E402
    BARANGAY,
    BARANGAY_EXTENDED,
    BARANGAY_FLAT,
)

# Import models
from barangay.models import BarangayModel  # noqa:E402

# Import fuzzy matching
from barangay.fuzz import FuzzBase, create_fuzz_base  # noqa:E402

# Import search functionality
from barangay.search import search  # noqa:E402

# Import utilities
from barangay.utils import sanitize_input  # noqa:E402

# Import new components
from barangay.data_manager import DataManager  # noqa:E402
from barangay.date_resolver import (  # noqa:E402
    get_available_dates,
    resolve_date,
)
from barangay.config import (  # noqa:E402
    get_cache_dir,
    get_verbose,
    load_env_config,
    resolve_as_of,
)

# Update available_dates at module import
available_dates = list(set(get_available_dates() + [current]))

__all__ = [
    # Main search function
    "search",
    # Classes
    "FuzzBase",
    "BarangayModel",
    "DataManager",
    # Data
    "BARANGAY",
    "BARANGAY_EXTENDED",
    "BARANGAY_FLAT",
    # Utilities
    "sanitize_input",
    # New components
    "create_fuzz_base",
    "get_available_dates",
    "resolve_date",
    "get_cache_dir",
    "get_verbose",
    "load_env_config",
    "resolve_as_of",
    # Module-level attributes
    "current",
    "as_of",
    "available_dates",
]
