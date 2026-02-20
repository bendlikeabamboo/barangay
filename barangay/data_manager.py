"""Data manager for barangay package.

This module provides the DataManager class for handling data loading, caching,
and downloading of Philippine barangay data. The DataManager supports multiple
data formats and can load data from bundled package files, local cache, or
download from GitHub.

Main Classes:
    :class:`DataManager`: Manages data loading, caching, and downloading

The DataManager supports the following data types:
    - basic: Basic barangay data (JSON format)
    - extended: Extended barangay data with recursive structure (JSON format)
    - flat: Flat barangay data with parent references (JSON format)
    - fuzzer_base: Pre-processed data for fuzzy matching (Parquet format)

Data Loading Priority:
    1. Bundled package data (for current date)
    2. Local cache (for historical dates)
    3. Download from GitHub (if not cached)

Examples:
    Using DataManager directly:

    >>> from barangay.data_manager import DataManager
    >>> dm = DataManager()
    >>> data = dm.get_data(as_of="2025-07-08", data_type="basic")

    The DataManager is also used internally by the data loading functions:

    >>> from barangay import load_barangay_data
    >>> data = load_barangay_data(as_of="2025-07-08")

See Also:
    :mod:`barangay.data`: Data loading module
    :mod:`barangay.downloader`: Data downloading module
"""

import json
import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    pass

logger: logging.Logger = logging.getLogger(__name__)

# Current dataset date (matches the data bundled with the package)
CURRENT_DATE = "2026-01-13"

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
    """Manages data loading, caching, and downloading.

    The DataManager class provides a unified interface for loading barangay data
    from multiple sources. It handles data loading from bundled package files,
    local cache, and downloading from GitHub repository.

    The class supports the following data types:
        - basic: Basic barangay data (nested dictionary structure)
        - extended: Extended barangay data (recursive with metadata)
        - flat: Flat barangay data (list with parent references)
        - fuzzer_base: Pre-processed data for fuzzy matching (DataFrame)

    Data Loading Strategy:
        1. If as_of is None or matches CURRENT_DATE: Load from bundled package
        2. If as_of is a historical date: Try cache first, then download from GitHub
        3. Cache downloaded data locally for faster subsequent access

    Attributes:
        _cache_dir: Path to the cache directory for storing downloaded data
        _logged_dataset: Flag to ensure dataset info is logged only once

    Examples:
        Basic usage:

        >>> from barangay.data_manager import DataManager
        >>> dm = DataManager()
        >>> data = dm.get_data(data_type="basic")

        Loading historical data:

        >>> from barangay.data_manager import DataManager
        >>> dm = DataManager()
        >>> data = dm.get_data(as_of="2025-07-08", data_type="basic")

        Loading fuzzer base:

        >>> from barangay.data_manager import DataManager
        >>> dm = DataManager()
        >>> df = dm.get_data(data_type="fuzzer_base")

    See Also:
        :func:`load_barangay_data`: Load basic barangay data
        :func:`load_barangay_extended_data`: Load extended barangay data
        :func:`load_barangay_flat_data`: Load flat barangay data
        :func:`load_fuzzer_base`: Load fuzzer base data
    """

    def __init__(self):
        """Initialize the DataManager.

        Sets up the cache directory and initializes the logging flag.
        The cache directory is determined by system defaults or the
        BARANGAY_CACHE_DIR environment variable.
        """
        self._cache_dir: Path = self._get_cache_dir()
        self._logged_dataset = False

    def get_data(
        self, as_of: str | None = None, data_type: str = "basic"
    ) -> dict | object:
        """Get data, loading from package, cache, or downloading from GitHub.

        This method provides a unified interface for loading barangay data from
        multiple sources. It automatically handles date resolution, caching, and
        downloading as needed.

        Args:
            as_of: Date string (YYYY-MM-DD) or None for latest data. If specified,
                the method will resolve the date to the closest available dataset.
                If None, the latest bundled data is used.
            data_type: Type of data to load. Valid options are:
                - "basic": Basic barangay data (nested dictionary)
                - "extended": Extended barangay data (recursive with metadata)
                - "flat": Flat barangay data (list with parent references)
                - "fuzzer_base": Pre-processed data for fuzzy matching (DataFrame)

        Returns:
            dict | object: The loaded data. The return type depends on data_type:
                - basic, extended, flat: dict
                - fuzzer_base: pandas.DataFrame

        Raises:
            ValueError: If data_type is invalid (not one of the supported types).

        Examples:
            Load latest basic data:

            >>> from barangay.data_manager import DataManager
            >>> dm = DataManager()
            >>> data = dm.get_data(data_type="basic")

            Load historical data:

            >>> from barangay.data_manager import DataManager
            >>> dm = DataManager()
            >>> data = dm.get_data(as_of="2025-07-08", data_type="basic")

            Load fuzzer base:

            >>> from barangay.data_manager import DataManager
            >>> dm = DataManager()
            >>> df = dm.get_data(data_type="fuzzer_base")

        See Also:
            :meth:`_load_from_package`: Load data from bundled package
            :meth:`_load_from_cache`: Load data from local cache
            :meth:`_download_from_github`: Download data from GitHub
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
        """Load data from package (bundled with installation).

        This method loads data from the package's bundled data files using
        importlib.resources. It supports both installed packages and development
        mode.

        Args:
            data_type: Type of data to load. Valid options are "basic", "extended",
                "flat", or "fuzzer_base".

        Returns:
            dict | object: The loaded data. Returns dict for JSON files and
                pandas.DataFrame for Parquet files.

        Raises:
            FileNotFoundError: If the data file is not found in the package.
            ValueError: If the file type is not supported.

        Note:
            This method uses multiple fallback strategies to load data:
            1. importlib.resources.files() (Python 3.9+)
            2. importlib.resources.path() (older Python versions)
            3. Direct file system access (development mode)

        See Also:
            :meth:`_load_from_cache`: Load data from local cache
            :meth:`_download_from_github`: Download data from GitHub
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
        """Load data from cache if available.

        This method attempts to load data from the local cache directory.
        Cached files are named using the pattern "{date}_{filename}".

        Args:
            resolved_date: Date string (YYYY-MM-DD) of the cached data.
            data_type: Type of data to load. Valid options are "basic", "extended",
                "flat", or "fuzzer_base".

        Returns:
            dict | object | None: The loaded data if found in cache, None otherwise.
                Returns dict for JSON files and pandas.DataFrame for Parquet files.

        Note:
            If loading from cache fails (e.g., corrupted file), the method logs
            a warning and returns None, allowing the caller to try downloading
            the data.

        See Also:
            :meth:`_save_to_cache`: Save data to cache
            :meth:`_download_from_github`: Download data from GitHub
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
        """Download data from GitHub and save to cache.

        This method downloads barangay data from the GitHub repository and saves
        it to the local cache for faster subsequent access. The downloaded file
        is automatically loaded and returned.

        Args:
            resolved_date: Date string (YYYY-MM-DD) of the data to download.
            data_type: Type of data to download. Valid options are "basic", "extended",
                "flat", or "fuzzer_base".

        Returns:
            dict | object: The downloaded and loaded data. Returns dict for JSON files
                and pandas.DataFrame for Parquet files.

        Raises:
            RuntimeError: If the download fails (network error, invalid URL, etc.).
            ValueError: If the file type is not supported.

        Note:
            The downloaded file is saved to the cache directory with the naming
            pattern "{date}_{filename}" for future use.

        See Also:
            :meth:`_load_from_cache`: Load data from local cache
            :meth:`_save_to_cache`: Save data to cache
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
        """Save data to cache.

        This method saves data to the local cache directory for faster subsequent
        access. The cache file is named using the pattern "{date}_{filename}".

        Args:
            resolved_date: Date string (YYYY-MM-DD) of the data.
            data_type: Type of data to save. Valid options are "basic", "extended",
                "flat", or "fuzzer_base".
            data: Data to save. Should be dict for JSON files or pandas.DataFrame
                for Parquet files.

        Raises:
            ValueError: If the file type is not supported or if data type is
                incompatible with the file format.

        Note:
            The cache directory is created automatically if it doesn't exist.

        See Also:
            :meth:`_load_from_cache`: Load data from local cache
            :meth:`_download_from_github`: Download data from GitHub
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
        """Log dataset info message (only once per session).

        This method logs a status message about which dataset is being used.
        The message is only logged once per session to avoid duplicate log entries.

        Args:
            status_message: Status message to log (e.g., "Using 2025-07-08 dataset").
            verbose: Whether verbose logging is enabled. If False, the message
                is not logged.

        Note:
            The method uses a flag to ensure the message is logged only once
            per DataManager instance, even if called multiple times.
        """
        if not verbose or self._logged_dataset:
            return

        logger.info(f"[barangay] {status_message}")
        self._logged_dataset = True

    def _get_cache_dir(self) -> Path:
        """Get cache directory for data files.

        This method determines the appropriate cache directory based on the
        operating system and environment variables.

        Returns:
            Path: The cache directory path. The location depends on the OS:
                - Windows: %LOCALAPPDATA%\\barangay\\cache
                - Linux/Mac with XDG_CACHE_HOME: $XDG_CACHE_HOME/barangay
                - Linux/Mac fallback: ~/.cache/barangay
                - Custom: $BARANGAY_CACHE_DIR if set

        Note:
            The BARANGAY_CACHE_DIR environment variable takes precedence over
            system defaults if set.
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
