import json
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

GITHUB_API_URL = (
    "https://api.github.com/repos/bendlikeabamboo/barangay-data-repository/contents/"
)

AVAILABLE_DATES_CACHE_FILE = "available_dates.json"

__all__ = [
    "AVAILABLE_DATES_CACHE_FILE",
    "GITHUB_API_URL",
    "get_available_dates",
    "get_cache_dir",
    "resolve_date",
]


def resolve_date(
    as_of: str | None, available_dates: list[str], current_date: str
) -> tuple[str | None, str]:
    all_dates = sorted(set(available_dates + [current_date]))

    if as_of is None:
        return None, "Using latest dataset"

    if as_of in all_dates:
        return as_of, f"Using {as_of} dataset"

    dates_before = [d for d in all_dates if d <= as_of]

    if dates_before:
        closest = max(dates_before)
        return closest, f"Using {closest} dataset (closest to {as_of})"
    else:
        earliest = all_dates[0]
        return earliest, f"Using {earliest} dataset (closest to {as_of})"


def get_cache_dir() -> Path:
    if os.name == "nt":
        local_app_data = os.getenv("LOCALAPPDATA")
        if local_app_data:
            return Path(local_app_data) / "barangay" / "cache"

    xdg_cache_home = os.getenv("XDG_CACHE_HOME")
    if xdg_cache_home:
        return Path(xdg_cache_home) / "barangay"

    return Path.home() / ".cache" / "barangay"


def get_available_dates() -> list[str]:
    import time
    from urllib.request import Request, urlopen

    cache_dir = get_cache_dir()
    cache_file = cache_dir / AVAILABLE_DATES_CACHE_FILE

    if cache_file.exists():
        try:
            cache_age = time.time() - cache_file.stat().st_mtime
            if cache_age < 3600:
                with open(cache_file) as f:
                    cached_data = json.load(f)
                    return cached_data.get("dates", [])
        except (json.JSONDecodeError, IOError):
            pass

    try:
        request = Request(
            GITHUB_API_URL, headers={"Accept": "application/vnd.github.v3+json"}
        )
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())

            dates = [
                item["name"]
                for item in data
                if item["type"] == "dir" and _is_valid_date(item["name"])
            ]

            dates.sort()

            cache_dir.mkdir(parents=True, exist_ok=True)
            with open(cache_file, "w") as f:
                json.dump({"dates": dates, "timestamp": time.time()}, f)

            return dates

    except Exception as e:
        logger.warning(f"Failed to fetch available dates from GitHub: {e}")

        if cache_file.exists():
            try:
                with open(cache_file) as f:
                    cached_data = json.load(f)
                    return cached_data.get("dates", [])
            except (json.JSONDecodeError, IOError):
                pass

        return []


def _is_valid_date(date_str: str) -> bool:
    import re
    from datetime import datetime

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        return False

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
