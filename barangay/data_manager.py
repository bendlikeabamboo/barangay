import json
import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    pass

logger: logging.Logger = logging.getLogger(__name__)

# Current dataset date (matches the data bundled with the package)
CURRENT_DATE = "2026-04-13"

# Data type to filename mapping
DATA_TYPE_MAPPING: Dict[str, str] = {
    "basic": "barangay.json",
    "extended": "barangay_extended.json",
    "flat": "barangay_flat.json",
    "fuzzer_base": "fuzzer_base.parquet",
}

# File extensions for each data type
DATA_TYPE_EXTENSIONS = {
    "basic": ".json",
    "extended": ".json",
    "flat": ".json",
    "fuzzer_base": ".parquet",
}


class DataManager:
    """Manages data loading, caching, and downloading for barangay datasets."""

    def __init__(self):
        """Initialize DataManager with cache dir and logging state."""
        self._cache_dir: Path = self._get_cache_dir()
        self._logged_dataset = False

    def get_data(
        self, as_of: str | None = None, data_type: str = "basic"
    ) -> dict | object:
        """Load data from package, cache, or GitHub.

        Args:
            as_of: Target date or None for latest.
            data_type: Data type ('basic', 'extended', etc.).

        Returns:
            Data as dict or DataFrame.
        """
        if data_type not in DATA_TYPE_MAPPING:
            raise ValueError(
                f"Invalid data_type: {data_type}. Must be one of {list(DATA_TYPE_MAPPING.keys())}"
            )

        # Resolve date
        from .config import resolve_as_of, get_verbose
        from .date_resolver import resolve_date, get_available_dates

        as_of: str | None = resolve_as_of(as_of)
        available_dates = get_available_dates()
        resolved_date, status_message = resolve_date(
            as_of, available_dates, CURRENT_DATE
        )

        # Log dataset info (only once per session)
        self._log_dataset_info(status_message, get_verbose())

        # Load data
        if resolved_date is None:
            # Load from package (latest)
            return self._load_from_package(data_type)
        elif resolved_date == CURRENT_DATE:
            # Load from package (current date)
            return self._load_from_package(data_type)
        else:
            # Try cache first, then download
            cached_data = self._load_from_cache(resolved_date, data_type)
            if cached_data is not None:
                return cached_data

            # Download from GitHub
            return self._download_from_github(resolved_date, data_type)

    def _load_from_package(self, data_type: str) -> dict | object:
        """Load data from bundled package resources.

        Args:
            data_type: Type of data to load.

        Returns:
            Data as dict or DataFrame.
        """
        from importlib import resources

        filename = DATA_TYPE_MAPPING[data_type]

        # Try to load from package using importlib.resources
        try:
            # Use importlib.resources for Python 3.9+
            with resources.files("barangay.data").joinpath(filename).open("rb") as f:
                content = f.read()
        except (AttributeError, TypeError, FileNotFoundError):
            # Fallback for older Python versions or development mode
            try:
                with resources.path("barangay.data", filename) as path:
                    with open(path, "rb") as f:
                        content = f.read()
            except (FileNotFoundError, Exception):
                # Fallback to loading from source directory (development mode)
                data_dir = Path(__file__).parent / "data"
                file_path = data_dir / filename
                if file_path.exists():
                    with open(file_path, "rb") as f:
                        content = f.read()
                else:
                    raise FileNotFoundError(f"Data file not found: {file_path}")

        # Parse based on file type
        if filename.endswith(".json"):
            return json.loads(content.decode("utf-8"))
        elif filename.endswith(".parquet"):
            import pandas as pd
            from io import BytesIO

            return pd.read_parquet(BytesIO(content))
        else:
            raise ValueError(f"Unsupported file type: {filename}")

    def _load_from_cache(
        self, resolved_date: str, data_type: str
    ) -> dict | object | None:
        """Load data from local cache.

        Args:
            resolved_date: Date string for cache lookup.
            data_type: Type of data to load.

        Returns:
            Cached data or None if not found.
        """
        filename = DATA_TYPE_MAPPING[data_type]
        cache_key = f"{resolved_date}_{filename}"
        cache_file = self._cache_dir / cache_key

        if not cache_file.exists():
            return None

        try:
            if filename.endswith(".json"):
                with open(cache_file) as f:
                    return json.load(f)
            elif filename.endswith(".parquet"):
                import pandas as pd

                return pd.read_parquet(cache_file)
            else:
                return None
        except Exception as e:
            logger.warning(f"Failed to load from cache {cache_file}: {e}")
            return None

    def _download_from_github(
        self, resolved_date: str, data_type: str
    ) -> dict | object:
        """Download data from GitHub and cache it.

        Args:
            resolved_date: Target date string.
            data_type: Type of data to download.

        Returns:
            Downloaded data as dict or DataFrame.
        """
        from .downloader import download_data

        filename = DATA_TYPE_MAPPING[data_type]
        cache_file = download_data(resolved_date, data_type, self._cache_dir)

        # Load and return the downloaded data
        if filename.endswith(".json"):
            with open(cache_file) as f:
                return json.load(f)
        elif filename.endswith(".parquet"):
            import pandas as pd

            return pd.read_parquet(cache_file)
        else:
            raise ValueError(f"Unsupported file type: {filename}")

    def _save_to_cache(self, resolved_date: str, data_type: str, data) -> None:
        """Save data to local cache directory.

        Args:
            resolved_date: Date string for cache key.
            data_type: Type of data being cached.
            data: Data to save (dict or DataFrame).
        """
        filename = DATA_TYPE_MAPPING[data_type]
        cache_key = f"{resolved_date}_{filename}"
        cache_file = self._cache_dir / cache_key

        self._cache_dir.mkdir(parents=True, exist_ok=True)

        if filename.endswith(".json"):
            with open(cache_file, "w") as f:
                json.dump(data, f)
        elif filename.endswith(".parquet"):
            import pandas as pd

            if isinstance(data, pd.DataFrame):
                data.to_parquet(cache_file)
            else:
                raise ValueError("Data must be a DataFrame for parquet files")
        else:
            raise ValueError(f"Unsupported file type: {filename}")

    def _log_dataset_info(self, status_message: str, verbose: bool) -> None:
        """Log dataset info if verbose mode is enabled.

        Args:
            status_message: Information message to log.
            verbose: Whether to enable verbose logging.
        """
        if not verbose or self._logged_dataset:
            return

        logger.info(f"[barangay] {status_message}")
        self._logged_dataset = True

    def _get_cache_dir(self) -> Path:
        """Get cache directory path for the system.

        Returns:
            Path to cache directory.
        """
        # Try environment variable first
        cache_dir = os.getenv("BARANGAY_CACHE_DIR")
        if cache_dir:
            return Path(cache_dir)

        # System defaults
        if os.name == "nt":  # Windows
            local_app_data = os.getenv("LOCALAPPDATA")
            if local_app_data:
                return Path(local_app_data) / "barangay" / "cache"

        # Linux/Mac
        xdg_cache_home = os.getenv("XDG_CACHE_HOME")
        if xdg_cache_home:
            return Path(xdg_cache_home) / "barangay"

        return Path.home() / ".cache" / "barangay"
