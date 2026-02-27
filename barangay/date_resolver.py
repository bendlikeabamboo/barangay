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
    """Resolve the requested date to the best matching available date.

    Args:
        as_of: The requested date string or None for latest.
        available_dates: List of available date strings.
        current_date: The current date string.

    Returns:
        Tuple of resolved date and status message.
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
    """Get the cache directory path for storing cached data.

    Returns:
        Path object pointing to the cache directory.
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
    """Fetch available dataset dates from GitHub API.

    Returns:
        List of available date strings in YYYY-MM-DD format.
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
    """Validate if a string matches YYYY-MM-DD date format.

    Args:
        date_str: The string to validate.

    Returns:
        True if valid date format, False otherwise.
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
