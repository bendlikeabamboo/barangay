"""Barangay data package for Philippine administrative divisions."""

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
    barangay,
    barangay_extended,
    barangay_flat,
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

# Backward compatibility aliases
# Note: These convert Pydantic models to dicts at module import time.
# For better performance, use the 'barangay', 'barangay_extended', or 'barangay_flat'
# models directly instead of these dict aliases.

BARANGAY: dict[str, ...] = barangay.model_dump()
BARANGAY_EXTENDED: dict[str, ...] = barangay_extended.model_dump()
BARANGAY_FLAT: list[dict] = [x.model_dump() for x in barangay_flat]

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
