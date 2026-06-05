import json
import logging
from pathlib import Path
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)

GITHUB_REPO = "bendlikeabamboo/barangay-data-repository"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/{repo}/main/{date}/{filename}"
GITHUB_API_URL = "https://api.github.com/repos/{repo}/contents/"

DATA_TYPE_MAPPING = {
    "basic": "barangay.json",
    "extended": "barangay_extended.json",
    "flat": "barangay_flat.json",
    "fuzzer_base": "fuzzer_base.parquet",
}

__all__ = [
    "DATA_TYPE_MAPPING",
    "GITHUB_API_URL",
    "GITHUB_RAW_URL",
    "GITHUB_REPO",
    "download_data",
    "fetch_available_dates",
    "get_github_url",
]


def get_github_url(resolved_date: str, filename: str) -> str:
    return GITHUB_RAW_URL.format(
        repo=GITHUB_REPO, date=resolved_date, filename=filename
    )


def download_data(resolved_date: str, data_type: str, cache_dir: Path) -> Path:
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

            cache_dir.mkdir(parents=True, exist_ok=True)
            cache_file = cache_dir / f"{resolved_date}_{filename}"

            with open(cache_file, "wb") as f:
                f.write(content)

            logger.info(f"Downloaded {filename} to {cache_file}")
            return cache_file

    except Exception as e:
        raise RuntimeError(f"Failed to download {filename} from {url}: {e}")


def fetch_available_dates() -> list[str]:
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

            dates = []
            for item in data:
                if item["type"] == "dir":
                    name = item["name"]
                    if re.match(r"^\d{4}-\d{2}-\d{2}$", name):
                        try:
                            datetime.strptime(name, "%Y-%m-%d")
                            dates.append(name)
                        except ValueError:
                            pass

            dates.sort()
            return dates

    except Exception as e:
        logger.warning(f"Failed to fetch available dates from GitHub: {e}")
        return []
