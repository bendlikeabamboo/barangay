import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.request import Request, urlopen

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

# GitHub repository details
GITHUB_REPO = "bendlikeabamboo/barangay-data-repository"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/{repo}/main/{date}/{filename}"
GITHUB_API_URL = "https://api.github.com/repos/{repo}/contents/"

# Data type to filename mapping
DATA_TYPE_MAPPING = {
    "basic": "barangay.json",
    "extended": "barangay_extended.json",
    "flat": "barangay_flat.json",
    "fuzzer_base": "fuzzer_base.parquet",
}


def get_github_url(resolved_date: str, filename: str) -> str:
    """Construct GitHub raw URL for a file.

    Args:
        resolved_date: Date string in YYYY-MM-DD format.
        filename: Name of the file to retrieve.

    Returns:
        str: The complete GitHub raw URL.
    """
    return GITHUB_RAW_URL.format(
        repo=GITHUB_REPO, date=resolved_date, filename=filename
    )


def download_data(resolved_date: str, data_type: str, cache_dir: Path) -> Path:
    """Download data from GitHub and save to cache.

    Args:
        resolved_date: Date string in YYYY-MM-DD format.
        data_type: Type of data (basic, extended, flat, fuzzer_base).
        cache_dir: Directory path to cache the downloaded file.

    Returns:
        Path: Path to the cached file.

    Raises:
        ValueError: If data_type is invalid.
        RuntimeError: If download fails.
    """
    if data_type not in DATA_TYPE_MAPPING:
        raise ValueError(
            f"Invalid data_type: {data_type}. Must be one of {list(DATA_TYPE_MAPPING.keys())}"
        )

    filename = DATA_TYPE_MAPPING[data_type]
    url = get_github_url(resolved_date, filename)

    logger.info(f"Downloading {filename} for {resolved_date} from GitHub")

    try:
        request = Request(url, headers={"User-Agent": "barangay-package"})
        with urlopen(request, timeout=30) as response:
            content = response.read()

            # Save to cache
            cache_dir.mkdir(parents=True, exist_ok=True)
            cache_file = cache_dir / f"{resolved_date}_{filename}"

            with open(cache_file, "wb") as f:
                f.write(content)

            logger.info(f"Downloaded {filename} to {cache_file}")
            return cache_file

    except Exception as e:
        raise RuntimeError(f"Failed to download {filename} from {url}: {e}")


def fetch_available_dates() -> list[str]:
    """Fetch available date directories from GitHub repository.

    Returns:
        list[str]: Sorted list of date strings in YYYY-MM-DD format.
    """
    import re
    from datetime import datetime

    url = GITHUB_API_URL.format(repo=GITHUB_REPO)

    try:
        request = Request(
            url,
            headers={
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "barangay-package",
            },
        )
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())

            # Extract date directories (they should be in YYYY-MM-DD format)
            dates = []
            for item in data:
                if item["type"] == "dir":
                    name = item["name"]
                    # Validate date format
                    if re.match(r"^\d{4}-\d{2}-\d{2}$", name):
                        try:
                            datetime.strptime(name, "%Y-%m-%d")
                            dates.append(name)
                        except ValueError:
                            pass

            # Sort dates
            dates.sort()
            return dates

    except Exception as e:
        logger.warning(f"Failed to fetch available dates from GitHub: {e}")
        return []
