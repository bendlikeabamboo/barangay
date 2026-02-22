"""Downloader for barangay package.

This module provides functions for downloading Philippine barangay data from the
GitHub repository. It supports downloading different data types and saving them
to a local cache directory.

Main Functions:
    :func:`get_github_url`: Get GitHub raw URL for a specific file
    :func:`download_data`: Download data from GitHub repository
    :func:`fetch_available_dates`: Fetch available dates from GitHub API

Data Types:
    The module supports downloading the following data types:
        - basic: Basic barangay data (barangay.json)
        - extended: Extended barangay data (barangay_extended.json)
        - flat: Flat barangay data (barangay_flat.json)
        - fuzzer_base: Pre-processed data for fuzzy matching (fuzzer_base.parquet)

Examples:
    Downloading data:

    >>> from barangay.downloader import download_data
    >>> from pathlib import Path
    >>> cache_dir = Path.home() / ".cache" / "barangay"
    >>> file_path = download_data("2025-07-08", "basic", cache_dir)
    >>> print(file_path)
    /home/user/.cache/barangay/2025-07-08_barangay.json

    Getting GitHub URL:

    >>> from barangay.downloader import get_github_url
    >>> url = get_github_url("2025-07-08", "barangay.json")
    >>> print(url)
    https://raw.githubusercontent.com/bendlikeabamboo/barangay-data-repository/main/2025-07-08/barangay.json

    Fetching available dates:

    >>> from barangay.downloader import fetch_available_dates
    >>> dates = fetch_available_dates()
    >>> print(dates[:3])
    ['2025-07-08', '2025-08-29', '2025-10-13']

See Also:
    :mod:`barangay.data_manager`: Data management module
    :mod:`barangay.date_resolver`: Date resolution module
"""

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
    """Get GitHub raw URL for a specific file.

    This function constructs the raw GitHub URL for downloading a specific
    data file from the repository.

    Args:
        resolved_date: Date string (YYYY-MM-DD) of the data file.
        filename: Name of the file to download (e.g., "barangay.json").

    Returns:
        str: The full GitHub raw URL for the specified file.

    Examples:
        Getting URL for basic data:

        >>> from barangay.downloader import get_github_url
        >>> url = get_github_url("2025-07-08", "barangay.json")
        >>> print(url)
        https://raw.githubusercontent.com/bendlikeabamboo/barangay-data-repository/main/2025-07-08/barangay.json

        Getting URL for fuzzer base:

        >>> from barangay.downloader import get_github_url
        >>> url = get_github_url("2025-08-29", "fuzzer_base.parquet")
        >>> print(url)
        https://raw.githubusercontent.com/bendlikeabamboo/barangay-data-repository/main/2025-08-29/fuzzer_base.parquet

    See Also:
        :func:`download_data`: Download data from GitHub repository
    """
    return GITHUB_RAW_URL.format(
        repo=GITHUB_REPO, date=resolved_date, filename=filename
    )


def download_data(resolved_date: str, data_type: str, cache_dir: Path) -> Path:
    """Download data from GitHub repository.

    This function downloads barangay data from the GitHub repository and saves
    it to the specified cache directory. The downloaded file is named
    using the pattern "{date}_{filename}" for easy identification.

    Args:
        resolved_date: Date string (YYYY-MM-DD) of the data to download.
        data_type: Type of data to download. Valid options are:
            - "basic": Basic barangay data (barangay.json)
            - "extended": Extended barangay data (barangay_extended.json)
            - "flat": Flat barangay data (barangay_flat.json)
            - "fuzzer_base": Pre-processed data for fuzzy matching (fuzzer_base.parquet)
        cache_dir: Directory to save the downloaded file.

    Returns:
        Path: Path to the downloaded file.

    Raises:
        ValueError: If data_type is invalid (not one of the supported types).
        RuntimeError: If the download fails due to network errors, invalid URL,
            or other issues.

    Examples:
        Downloading basic data:

        >>> from barangay.downloader import download_data
        >>> from pathlib import Path
        >>> cache_dir = Path.home() / ".cache" / "barangay"
        >>> file_path = download_data("2025-07-08", "basic", cache_dir)
        >>> print(file_path)
        /home/user/.cache/barangay/2025-07-08_barangay.json

        Downloading fuzzer base:

        >>> from barangay.downloader import download_data
        >>> from pathlib import Path
        >>> cache_dir = Path.home() / ".cache" / "barangay"
        >>> file_path = download_data("2025-08-29", "fuzzer_base", cache_dir)
        >>> print(file_path)
        /home/user/.cache/barangay/2025-08-29_fuzzer_base.parquet

    See Also:
        :func:`get_github_url`: Get GitHub raw URL for a specific file
        :func:`fetch_available_dates`: Fetch available dates from GitHub API
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
    """Fetch available dates from GitHub API.

    This function uses the GitHub API to get a list of available
    dataset dates from the repository. It filters the results to only
    include directories that match the YYYY-MM-DD date format.

    Returns:
        list[str]: A sorted list of date strings in YYYY-MM-DD format.
            Returns an empty list if fetching fails.

    Note:
        - The function validates that each directory name is a valid date
        - Results are sorted in ascending order
        - Network errors are logged but do not raise exceptions

    Examples:
        Fetching available dates:

        >>> from barangay.downloader import fetch_available_dates
        >>> dates = fetch_available_dates()
        >>> print(dates[:3])
        ['2025-07-08', '2025-08-29', '2025-10-13']

        Checking if a specific date is available:

        >>> from barangay.downloader import fetch_available_dates
        >>> dates = fetch_available_dates()
        >>> "2025-07-08" in dates
        True

    See Also:
        :func:`download_data`: Download data from GitHub repository
        :func:`get_github_url`: Get GitHub raw URL for a specific file
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
