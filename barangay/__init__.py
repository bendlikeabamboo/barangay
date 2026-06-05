"""Barangay data package for Philippine administrative divisions."""

from pathlib import Path
from typing import Any

# Read CURRENT_VERSION file to set module attribute
_current_version_path = Path(__file__).parent / "data" / "CURRENT_VERSION"
_current = (
    _current_version_path.read_text().strip()
    if _current_version_path.exists()
    else "2026-04-13"
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

# Import plugin system
from barangay.plugin_loader import PluginLoader  # noqa:E402
from barangay.database import Database  # noqa:E402
from barangay.models import (  # noqa:E402
    AdminDivRecord,
    AdminLevel,
    PluginInfo,
    SearchResult,
    ValidationResult,
)
from barangay.search import search_fuzzy  # noqa:E402
from barangay.validate import validate, validate_many  # noqa:E402
from barangay.version import use_plugins, use_version  # noqa:E402

# Update available_dates at module import
available_dates = list(set(get_available_dates() + [current]))

_db = Database()

regions = _db.regions
provinces = _db.provinces
municipalities = _db.municipalities
cities = _db.cities
submunicipalities = _db.submunicipalities
barangays = _db.barangays
special_geographic_areas = _db.special_geographic_areas

# Backward compatibility aliases
# Note: These convert Pydantic models to dicts at module import time.
# For better performance, use the 'barangay', 'barangay_extended', or 'barangay_flat'
# models directly instead of these dict aliases.

BARANGAY: dict[str, Any] = barangay.model_dump()
BARANGAY_EXTENDED: dict[str, Any] = barangay_extended.model_dump()
BARANGAY_FLAT: list[dict[str, Any]] = [x.model_dump() for x in barangay_flat]

__all__ = [
    # Main search function
    "search",
    # Classes
    "FuzzBase",
    "BarangayModel",
    "DataManager",
    "PluginLoader",
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
    # Database API
    "Database",
    "AdminLevel",
    "AdminDivRecord",
    "SearchResult",
    "ValidationResult",
    "PluginInfo",
    # Database namespaces
    "regions",
    "provinces",
    "municipalities",
    "cities",
    "submunicipalities",
    "barangays",
    "special_geographic_areas",
    # New functions
    "search_fuzzy",
    "validate",
    "validate_many",
    "use_version",
    "use_plugins",
]
