"""Barangay data package for Philippine administrative divisions."""

import warnings
from pathlib import Path
from typing import Any

# Read CURRENT_VERSION file to set module attribute
_current_version_path = Path(__file__).parent / "data" / "CURRENT_VERSION"
_current = (
    _current_version_path.read_text().strip()
    if _current_version_path.exists()
    else "2026-07-13"
)

# Module-level attributes
current: str = _current
as_of: str | None = None
available_dates: list[str] = []

# Import data (lazy - actual data loads deferred until first access)
import barangay.data as _data_module  # noqa:E402

from barangay.config import (  # noqa:E402
    get_cache_dir,
    get_verbose,
    load_env_config,
    resolve_as_of,
)

# Import new components
from barangay.data_manager import DataManager  # noqa:E402

# Import Database API
from barangay.database import (  # noqa:E402  # noqa:E402
    Database,
    DatabaseView,
    EnrichedRecord,
    MultipleResultsError,
    RecordNotFoundError,
)
from barangay.date_resolver import (  # noqa:E402
    get_available_dates,
    resolve_date,
)

# Import fuzzy matching
from barangay.fuzz import FuzzBase, create_fuzz_base  # noqa:E402

# Import models
from barangay.models import (  # noqa:E402
    AdminDivRecord,
    AdminLevel,
    BarangayModel,  # noqa:E402
    PluginInfo,
    SearchResult,
    ValidationResult,
)

# Import plugin system
from barangay.plugin_loader import PluginLoader  # noqa:E402

# Import search functionality
from barangay.search import search, search_fuzzy  # noqa:E402

# Import utilities
from barangay.utils import sanitize_input, to_python_identifier  # noqa:E402
from barangay.validate import validate, validate_many  # noqa:E402
from barangay.version import use_plugins, use_version  # noqa:E402

# Update available_dates at module import
available_dates = list(set(get_available_dates() + [current]))

_db = Database()

_VIEW_NAMES = frozenset(
    {
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
    }
)

_DEPRECATED_NAMES = frozenset({"BARANGAY", "BARANGAY_EXTENDED", "BARANGAY_FLAT"})
_LAZY_DATA_NAMES = frozenset({"barangay", "barangay_extended", "barangay_flat"})

_BARANGAY_CACHE: dict[str, Any] | None = None
_BARANGAY_EXTENDED_CACHE: dict[str, Any] | None = None
_BARANGAY_FLAT_CACHE: list[dict[str, Any]] | None = None

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


def __getattr__(name: str):
    global _BARANGAY_CACHE, _BARANGAY_EXTENDED_CACHE, _BARANGAY_FLAT_CACHE

    if name in _VIEW_NAMES:
        return getattr(_db, name)

    if name in _LAZY_DATA_NAMES:
        return getattr(_data_module, name)

    if name == "BARANGAY":
        if _BARANGAY_CACHE is None:
            warnings.warn(
                "BARANGAY is deprecated and will be removed in 2027.X.X.X. "
                "Use the Database API instead: "
                "from barangay import barangays; barangays.get(name='Tongmageng')",
                DeprecationWarning,
                stacklevel=2,
            )
            _BARANGAY_CACHE = _data_module.barangay.model_dump()
        return _BARANGAY_CACHE

    if name == "BARANGAY_EXTENDED":
        if _BARANGAY_EXTENDED_CACHE is None:
            warnings.warn(
                "BARANGAY_EXTENDED is deprecated and will be removed in 2027.X.X.X. "
                "Use the Database API instead: hierarchy traversal via .parent, .ancestors, .children "
                "(e.g. from barangay import barangays; rec = barangays.get(name='Tongmageng'); rec.parent)",
                DeprecationWarning,
                stacklevel=2,
            )
            _BARANGAY_EXTENDED_CACHE = _data_module.barangay_extended.model_dump()
        return _BARANGAY_EXTENDED_CACHE

    if name == "BARANGAY_FLAT":
        if _BARANGAY_FLAT_CACHE is None:
            warnings.warn(
                "BARANGAY_FLAT is deprecated and will be removed in 2027.X.X.X. "
                "Use the Database API instead: to_frame(), to_dicts(), iteration "
                "(e.g. from barangay import barangays; barangays.to_frame())",
                DeprecationWarning,
                stacklevel=2,
            )
            _BARANGAY_FLAT_CACHE = [x.model_dump() for x in _data_module.barangay_flat]
        return _BARANGAY_FLAT_CACHE

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
