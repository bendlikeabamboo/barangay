"""Date resolver for barangay package.

This module provides functions for resolving approximate dates to the closest available
dataset. It supports fetching available dates from GitHub API and caching the
results locally for improved performance.

Main Functions:
    :func:`resolve_date`: Resolve requested date to closest available dataset
    :func:`get_available_dates`: Fetch available dates from GitHub API
    :func:`_is_valid_date`: Check if string is a valid date in YYYY-MM-DD format

Date Resolution Logic:
    The date resolution follows these rules:
        1. If as_of is None: Use latest bundled data
        2. If exact match exists: Use that date
        3. If no exact match: Use the closest date <= requested date
        4. If requested date is before all available dates: Use the earliest date

Examples:
    Resolving a date:

    >>> from barangay.date_resolver import resolve_date
    >>> resolved, message = resolve_date(
    ...     "2026-01-01",
    ...     ["2025-07-08", "2025-08-29", "2025-10-13"],
    ...     "2026-01-13"
    ... )
    >>> print(resolved)
    2025-10-13

    Getting available dates:

    >>> from barangay.date_resolver import get_available_dates
    >>> dates = get_available_dates()
    >>> print(dates[:3])
    ['2025-07-08', '2025-08-29', '2025-10-13']

See Also:
    :mod:`barangay.config`: Configuration module
    :mod:`barangay.data_manager`: Data management module
"""

import json
import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

# GitHub API endpoint
GITHUB_API_URL = (
    "https://api.github.com/repos/bendlikeabamboo/barangay-data-repository/contents/"
)

# Cache file for available dates
AVAILABLE_DATES_CACHE_FILE = "available_dates.json"


def resolve_date(
    as_of: str | None, available_dates: list[str], current_date: str
) -> tuple[str | None, str]:
    """Resolve requested date to closest available dataset.

    This function resolves a requested date to the closest available dataset
    using a set of resolution rules. It returns both the resolved date
    and a status message describing which dataset is being used.

    Resolution Logic:
        1. If as_of is None: Return None (use latest bundled data)
        2. If exact match exists: Return that date
        3. If no exact match: Return the closest date <= requested date
        4. If requested date is before all available dates: Return the earliest date

    Args:
        as_of: Requested date (YYYY-MM-DD) or None for latest data.
        available_dates: Sorted list of available dates from GitHub.
        current_date: Current dataset date in package (bundled with installation).

    Returns:
        tuple[str | None, str]: A tuple containing:
            - resolved_date: The resolved date string or None for latest
            - status_message: A descriptive message about which dataset is being used

    Examples:
        Exact match:

        >>> from barangay.date_resolver import resolve_date
        >>> resolved, message = resolve_date(
        ...     "2025-07-08",
        ...     ["2025-07-08", "2025-08-29", "2025-10-13"],
        ...     "2026-01-13"
        ... )
        >>> print(resolved)
        2025-07-08
        >>> print(message)
        Using 2025-07-08 dataset

        Closest match:

        >>> from barangay.date_resolver import resolve_date
        >>> resolved, message = resolve_date(
        ...     "2026-01-01",
        ...     ["2025-07-08", "2025-08-29", "2025-10-13"],
        ...     "2026-01-13"
        ... )
        >>> print(resolved)
        2025-10-13
        >>> print(message)
        Using 2025-10-13 dataset (closest to 2026-01-01)

        Latest (None):

        >>> from barangay.date_resolver import resolve_date
        >>> resolved, message = resolve_date(
        ...     None,
        ...     ["2025-07-08", "2025-08-29", "2025-10-13"],
        ...     "2026-01-13"
        ... )
        >>> print(resolved)
        None
        >>> print(message)
        Using latest dataset

    See Also:
        :func:`get_available_dates`: Fetch available dates from GitHub API
        :func:`resolve_as_of`: Resolve as_of date from multiple layers
    """
    # Combine github dates with current date
    all_dates = sorted(set(available_dates + [current_date]))

    if as_of is None:
        return None, "Using latest dataset"

    # Try exact match first
    if as_of in all_dates:
        return as_of, f"Using {as_of} dataset"

    # Find closest date <= requested date
    dates_before = [d for d in all_dates if d <= as_of]

    if dates_before:
        closest = max(dates_before)
        return closest, f"Using {closest} dataset (closest to {as_of})"
    else:
        # Requested date is before all available dates
        earliest = all_dates[0]
        return earliest, f"Using {earliest} dataset (closest to {as_of})"


def get_cache_dir() -> Path:
    """Get cache directory for available dates cache.

    This function determines the appropriate cache directory based on the operating
    system and environment variables. The cache directory is used to store
    the available dates list to avoid repeated GitHub API calls.

    Returns:
        Path: The cache directory path. The location depends on the OS:
            - Windows: %LOCALAPPDATA%\\barangay\\cache
            - Linux/Mac with XDG_CACHE_HOME: $XDG_CACHE_HOME/barangay
            - Linux/Mac fallback: ~/.cache/barangay

    Note:
        The BARANGAY_CACHE_DIR environment variable takes precedence over
        system defaults if set.

    See Also:
        :func:`get_available_dates`: Fetch available dates from GitHub API
    """
    if os.name == "nt":  # Windows
        local_app_data = os.getenv("LOCALAPPDATA")
        if local_app_data:
            return Path(local_app_data) / "barangay" / "cache"

    # Linux/Mac or fallback
    xdg_cache_home = os.getenv("XDG_CACHE_HOME")
    if xdg_cache_home:
        return Path(xdg_cache_home) / "barangay"

    return Path.home() / ".cache" / "barangay"


def get_available_dates() -> list[str]:
    """Fetch available dates from GitHub API.

    This function fetches the list of available dataset dates from the GitHub
    repository. The results are cached locally for 1 hour to reduce API calls
    and improve performance.

    The cache file is stored at:
        ~/.cache/barangay/available_dates.json (Linux/Mac)
        %LOCALAPPDATA%\\barangay\\cache\\available_dates.json (Windows)

    Returns:
        list[str]: A sorted list of available date strings in YYYY-MM-DD format.
            Returns an empty list if fetching fails and no cached data is available.

    Note:
        - The cache has a 1-hour TTL (time to live)
        - If the GitHub API call fails, cached data is returned if available
        - If both the API call and cache fail, an empty list is returned

    Examples:
        Getting available dates:

        >>> from barangay.date_resolver import get_available_dates
        >>> dates = get_available_dates()
        >>> print(dates[:3])
        ['2025-07-08', '2025-08-29', '2025-10-13']

    See Also:
        :func:`resolve_date`: Resolve requested date to closest available dataset
        :func:`_is_valid_date`: Check if string is a valid date
    """
    import time
    from urllib.request import Request, urlopen

    cache_dir = get_cache_dir()
    cache_file = cache_dir / AVAILABLE_DATES_CACHE_FILE

    # Check cache first (1 hour TTL)
    if cache_file.exists():
        try:
            cache_age = time.time() - cache_file.stat().st_mtime
            if cache_age < 3600:  # 1 hour
                with open(cache_file) as f:
                    cached_data = json.load(f)
                    return cached_data.get("dates", [])
        except (json.JSONDecodeError, IOError):
            pass

    # Fetch from GitHub API
    try:
        request = Request(
            GITHUB_API_URL, headers={"Accept": "application/vnd.github.v3+json"}
        )
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())

            # Extract date directories (they should be in YYYY-MM-DD format)
            dates = [
                item["name"]
                for item in data
                if item["type"] == "dir" and _is_valid_date(item["name"])
            ]

            # Sort dates
            dates.sort()

            # Save to cache
            cache_dir.mkdir(parents=True, exist_ok=True)
            with open(cache_file, "w") as f:
                json.dump({"dates": dates, "timestamp": time.time()}, f)

            return dates

    except Exception as e:
        logger.warning(f"Failed to fetch available dates from GitHub: {e}")

        # Return cached data if available
        if cache_file.exists():
            try:
                with open(cache_file) as f:
                    cached_data = json.load(f)
                    return cached_data.get("dates", [])
            except (json.JSONDecodeError, IOError):
                pass

        return []


def _is_valid_date(date_str: str) -> bool:
    """Check if string is a valid date in YYYY-MM-DD format.

    This function validates that a string matches the YYYY-MM-DD format and
    represents a valid calendar date.

    Args:
        date_str: String to validate.

    Returns:
        bool: True if the string is a valid date in YYYY-MM-DD format,
            False otherwise.

    Examples:
        Valid dates:

        >>> from barangay.date_resolver import _is_valid_date
        >>> _is_valid_date("2025-07-08")
        True
        >>> _is_valid_date("2026-01-13")
        True

        Invalid dates:

        >>> from barangay.date_resolver import _is_valid_date
        >>> _is_valid_date("2025-13-01")
        False
        >>> _is_valid_date("2025-02-30")
        False
        >>> _is_valid_date("not-a-date")
        False

    Note:
        This is a private function intended for internal use by the
        date_resolver module.
    """
    import re
    from datetime import datetime

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        return False

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
