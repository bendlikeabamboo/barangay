import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

# Environment variable defaults
DEFAULT_VERBOSE = "true"
DEFAULT_CACHE_DIR = None


def load_env_config() -> dict:
    """Load configuration from environment variables.

    Returns:
        dict: Configuration with BARANGAY_AS_OF, BARANGAY_VERBOSE, and
            BARANGAY_CACHE_DIR.
    """
    config = {
        "BARANGAY_AS_OF": os.getenv("BARANGAY_AS_OF"),
        "BARANGAY_VERBOSE": os.getenv("BARANGAY_VERBOSE", DEFAULT_VERBOSE),
        "BARANGAY_CACHE_DIR": os.getenv("BARANGAY_CACHE_DIR", DEFAULT_CACHE_DIR),
    }
    return config


def resolve_as_of(as_of_param: str | None = None) -> str | None:
    """Resolve the "as of" date for data queries.

    Args:
        as_of_param: Optional date string from function parameter.

    Returns:
        str | None: The resolved date string, or None for latest data.
    """
    # Priority 1: Function parameter
    if as_of_param is not None:
        return as_of_param

    # Priority 2: Module attribute
    try:
        import barangay

        if hasattr(barangay, "as_of") and barangay.as_of is not None:
            return barangay.as_of
    except ImportError:
        pass

    # Priority 3: .env file
    env_config = load_env_config()
    if env_config["BARANGAY_AS_OF"]:
        return env_config["BARANGAY_AS_OF"]

    # Priority 4: Default (None for latest)
    return None


def get_verbose() -> bool:
    """Get verbose logging setting from environment.

    Returns:
        bool: True if verbose logging is enabled.
    """
    env_config = load_env_config()
    return env_config["BARANGAY_VERBOSE"].lower() in ("true", "1", "yes", "on")


def get_cache_dir() -> Path:
    """Get the cache directory path for the application.

    Returns:
        Path: The cache directory path.
    """
    env_config = load_env_config()

    if env_config["BARANGAY_CACHE_DIR"]:
        return Path(env_config["BARANGAY_CACHE_DIR"])

    # System defaults
    if os.name == "nt":  # Windows
        local_app_data = os.getenv("LOCALAPPDATA")
        if local_app_data:
            return Path(local_app_data) / "barangay" / "cache"

    # Linux/Mac or fallback
    xdg_cache_home = os.getenv("XDG_CACHE_HOME")
    if xdg_cache_home:
        return Path(xdg_cache_home) / "barangay"

    return Path.home() / ".cache" / "barangay"
