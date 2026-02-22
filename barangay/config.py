"""Configuration resolver for barangay package.

This module provides functions for resolving configuration settings from multiple
sources, including environment variables, module attributes, and function parameters.
The configuration follows a priority-based resolution system.

Main Functions:
    :func:`load_env_config`: Load configuration from environment variables
    :func:`resolve_as_of`: Resolve as_of date from multiple layers with priority
    :func:`get_verbose`: Get verbose logging setting from environment
    :func:`get_cache_dir`: Get cache directory from environment or use system default

Environment Variables:
    BARANGAY_AS_OF: Default dataset date (YYYY-MM-DD format). If set, this
        date will be used for all searches unless overridden by function parameters
        or module attributes.
    BARANGAY_VERBOSE: Enable verbose logging. Valid values are "true", "1",
        "yes", "on" (case-insensitive). Default is "true".
    BARANGAY_CACHE_DIR: Custom cache directory path. If set, downloaded data
        will be stored in this directory instead of the system default.

Configuration Priority:
    The as_of date is resolved in the following priority order (highest to lowest):
        1. Function parameter (if provided)
        2. Module attribute (barangay.as_of)
        3. Environment variable (BARANGAY_AS_OF)
        4. Default: None (use latest bundled data)

Examples:
    Setting configuration via environment variables:

    >>> import os
    >>> os.environ["BARANGAY_AS_OF"] = "2025-07-08"
    >>> os.environ["BARANGAY_VERBOSE"] = "true"

    Using resolve_as_of:

    >>> from barangay.config import resolve_as_of
    >>> date = resolve_as_of(as_of_param="2025-08-29")
    >>> print(date)
    2025-08-29

    Getting verbose setting:

    >>> from barangay.config import get_verbose
    >>> verbose = get_verbose()
    >>> print(verbose)
    True

    Getting cache directory:

    >>> from barangay.config import get_cache_dir
    >>> cache_dir = get_cache_dir()
    >>> print(cache_dir)
    /home/user/.cache/barangay

See Also:
    :mod:`barangay.date_resolver`: Date resolution module
    :mod:`barangay.data_manager`: Data management module
"""

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

# Environment variable defaults
DEFAULT_VERBOSE = "true"
DEFAULT_CACHE_DIR = None


def load_env_config() -> dict:
    """Load configuration from environment variables.

    This function reads configuration values from environment variables and returns
    them as a dictionary. It handles default values for variables that are not set.

    Returns:
        dict: A dictionary containing the following keys:
            - BARANGAY_AS_OF: Dataset date from environment or None
            - BARANGAY_VERBOSE: Verbose logging flag (default: "true")
            - BARANGAY_CACHE_DIR: Cache directory path or None

    Examples:
        Loading configuration:

        >>> from barangay.config import load_env_config
        >>> config = load_env_config()
        >>> print(config["BARANGAY_VERBOSE"])
        true

        With custom environment variables:

        >>> import os
        >>> os.environ["BARANGAY_AS_OF"] = "2025-07-08"
        >>> config = load_env_config()
        >>> print(config["BARANGAY_AS_OF"])
        2025-07-08

    See Also:
        :func:`resolve_as_of`: Resolve as_of date with priority
        :func:`get_verbose`: Get verbose logging setting
        :func:`get_cache_dir`: Get cache directory path
    """
    config = {
        "BARANGAY_AS_OF": os.getenv("BARANGAY_AS_OF"),
        "BARANGAY_VERBOSE": os.getenv("BARANGAY_VERBOSE", DEFAULT_VERBOSE),
        "BARANGAY_CACHE_DIR": os.getenv("BARANGAY_CACHE_DIR", DEFAULT_CACHE_DIR),
    }
    return config


def resolve_as_of(as_of_param: str | None = None) -> str | None:
    """Resolve as_of date from multiple layers with priority.

    This function resolves the as_of date for dataset selection using a priority
    system. It checks function parameters, module attributes, and environment
    variables in that order.

    Priority order (highest to lowest):
        1. Function parameter (if provided)
        2. Module attribute (barangay.as_of)
        3. Environment variable (BARANGAY_AS_OF)
        4. Default: None (use latest bundled data)

    Args:
        as_of_param: Date string from function parameter in YYYY-MM-DD format,
            or None to use the next priority level.

    Returns:
        str | None: The resolved date string in YYYY-MM-DD format, or None
        to use the latest bundled data.

    Examples:
        Using function parameter (highest priority):

        >>> from barangay.config import resolve_as_of
        >>> date = resolve_as_of(as_of_param="2025-08-29")
        >>> print(date)
        2025-08-29

        Using module attribute:

        >>> import barangay
        >>> barangay.as_of = "2025-07-08"
        >>> from barangay.config import resolve_as_of
        >>> date = resolve_as_of()
        >>> print(date)
        2025-07-08

        Using environment variable:

        >>> import os
        >>> os.environ["BARANGAY_AS_OF"] = "2025-10-13"
        >>> from barangay.config import resolve_as_of
        >>> date = resolve_as_of()
        >>> print(date)
        2025-10-13

        Using default (None):

        >>> from barangay.config import resolve_as_of
        >>> date = resolve_as_of()
        >>> print(date)
        None

    See Also:
        :func:`load_env_config`: Load configuration from environment variables
        :func:`resolve_date`: Resolve approximate dates to closest available dataset
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

    This function reads the BARANGAY_VERBOSE environment variable and returns
    a boolean indicating whether verbose logging is enabled.

    Returns:
        bool: True if verbose logging is enabled, False otherwise. The following
        values are considered True (case-insensitive): "true", "1", "yes", "on".
        All other values (including None) are considered False.

    Examples:
        Getting verbose setting (default):

        >>> from barangay.config import get_verbose
        >>> verbose = get_verbose()
        >>> print(verbose)
        True

        With custom environment variable:

        >>> import os
        >>> os.environ["BARANGAY_VERBOSE"] = "false"
        >>> from barangay.config import get_verbose
        >>> verbose = get_verbose()
        >>> print(verbose)
        False

    See Also:
        :func:`load_env_config`: Load configuration from environment variables
    """
    env_config = load_env_config()
    return env_config["BARANGAY_VERBOSE"].lower() in ("true", "1", "yes", "on")


def get_cache_dir() -> Path:
    """Get cache directory from environment or use system default.

    This function determines the appropriate cache directory based on the operating
    system and environment variables. The cache directory is used to store
    downloaded historical data.

    Returns:
        Path: The cache directory path. The location depends on the OS:
            - Windows: %LOCALAPPDATA%\\barangay\\cache
            - Linux/Mac with XDG_CACHE_HOME: $XDG_CACHE_HOME/barangay
            - Linux/Mac fallback: ~/.cache/barangay
            - Custom: $BARANGAY_CACHE_DIR if set

    Note:
        The BARANGAY_CACHE_DIR environment variable takes precedence over
        system defaults if set.

    Examples:
        Getting default cache directory:

        >>> from barangay.config import get_cache_dir
        >>> cache_dir = get_cache_dir()
        >>> print(cache_dir)
        /home/user/.cache/barangay

        With custom environment variable:

        >>> import os
        >>> os.environ["BARANGAY_CACHE_DIR"] = "/custom/cache/path"
        >>> from barangay.config import get_cache_dir
        >>> cache_dir = get_cache_dir()
        >>> print(cache_dir)
        /custom/cache/path

    See Also:
        :func:`load_env_config`: Load configuration from environment variables
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
