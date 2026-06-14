from __future__ import annotations

from typing import Any

from barangay.config import (
    get_cache_dir,
    get_verbose,
    load_env_config,
    resolve_as_of,
)
from barangay.data import barangay, barangay_extended, barangay_flat
from barangay.data_manager import DataManager
from barangay.database import (
    Database,
    DatabaseView,
    EnrichedRecord,
    MultipleResultsError,
    RecordNotFoundError,
)
from barangay.date_resolver import get_available_dates, resolve_date
from barangay.fuzz import FuzzBase, create_fuzz_base
from barangay.models import (
    AdminDivRecord,
    AdminLevel,
    BarangayModel,
    PluginInfo,
    SearchResult,
    ValidationResult,
)
from barangay.plugin_loader import PluginLoader
from barangay.search import search, search_fuzzy
from barangay.utils import sanitize_input, to_python_identifier
from barangay.validate import validate, validate_many
from barangay.version import use_plugins, use_version

def __getattr__(name: str) -> Any: ...

# Module-level attributes
current: str
as_of: str | None
available_dates: list[str]

# Deprecated data dicts
BARANGAY: dict[str, Any]
BARANGAY_EXTENDED: dict[str, Any]
BARANGAY_FLAT: list[dict[str, Any]]

# Database namespace views
regions: DatabaseView
provinces: DatabaseView
municipalities: DatabaseView
cities: DatabaseView
hucs: DatabaseView
iccs: DatabaseView
component_cities: DatabaseView
submunicipalities: DatabaseView
barangays: DatabaseView
special_geographic_areas: DatabaseView

__all__ = [
    "search",
    "FuzzBase",
    "BarangayModel",
    "DataManager",
    "PluginLoader",
    "BARANGAY",
    "BARANGAY_EXTENDED",
    "BARANGAY_FLAT",
    "sanitize_input",
    "to_python_identifier",
    "create_fuzz_base",
    "get_available_dates",
    "resolve_date",
    "get_cache_dir",
    "get_verbose",
    "load_env_config",
    "resolve_as_of",
    "current",
    "as_of",
    "available_dates",
    "Database",
    "DatabaseView",
    "EnrichedRecord",
    "AdminLevel",
    "AdminDivRecord",
    "SearchResult",
    "ValidationResult",
    "PluginInfo",
    "regions",
    "provinces",
    "municipalities",
    "cities",
    "hucs",
    "iccs",
    "component_cities",
    "submunicipalities",
    "barangays",
    "special_geographic_areas",
    "search_fuzzy",
    "validate",
    "validate_many",
    "use_version",
    "use_plugins",
    "MultipleResultsError",
    "RecordNotFoundError",
    "barangay",
    "barangay_flat",
    "barangay_extended",
]
