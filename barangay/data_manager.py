import json
import logging
import os
from pathlib import Path
from typing import Dict, Literal, overload

import pandas as pd

logger: logging.Logger = logging.getLogger(__name__)

CURRENT_DATE = "2026-04-13"

DATA_TYPE_MAPPING: Dict[str, str] = {
    "basic": "barangay.json",
    "extended": "barangay_extended.json",
    "flat": "barangay_flat.json",
    "fuzzer_base": "fuzzer_base.parquet",
}

DATA_TYPE_EXTENSIONS = {
    "basic": ".json",
    "extended": ".json",
    "flat": ".json",
    "fuzzer_base": ".parquet",
}

__all__ = [
    "CURRENT_DATE",
    "DATA_TYPE_EXTENSIONS",
    "DATA_TYPE_MAPPING",
    "DataManager",
]


class DataManager:
    def __init__(self):
        self._cache_dir: Path = self._get_cache_dir()
        self._logged_dataset = False

    @overload
    def get_data(self, as_of: str | None, data_type: Literal["basic"]) -> dict: ...
    @overload
    def get_data(self, as_of: str | None, data_type: Literal["extended"]) -> dict: ...
    @overload
    def get_data(self, as_of: str | None, data_type: Literal["flat"]) -> list[dict]: ...
    @overload
    def get_data(
        self, as_of: str | None, data_type: Literal["fuzzer_base"]
    ) -> pd.DataFrame: ...

    def get_data(
        self, as_of: str | None = None, data_type: str = "basic"
    ) -> dict | list[dict] | pd.DataFrame:
        if data_type not in DATA_TYPE_MAPPING:
            raise ValueError(
                f"Invalid data_type: {data_type}. Must be one of {list(DATA_TYPE_MAPPING.keys())}"
            )

        from .config import resolve_as_of, get_verbose
        from .date_resolver import resolve_date, get_available_dates

        resolved_as_of: str | None = resolve_as_of(as_of)
        available_dates = get_available_dates()
        resolved_date, status_message = resolve_date(
            resolved_as_of, available_dates, CURRENT_DATE
        )

        self._log_dataset_info(status_message, get_verbose())

        if resolved_date is None:
            return self._load_from_package(data_type)
        elif resolved_date == CURRENT_DATE:
            return self._load_from_package(data_type)
        else:
            cached_data = self._load_from_cache(resolved_date, data_type)
            if cached_data is not None:
                return cached_data

            return self._download_from_github(resolved_date, data_type)

    def _load_from_package(self, data_type: str) -> dict | list[dict] | pd.DataFrame:
        from importlib import resources

        filename = DATA_TYPE_MAPPING[data_type]

        try:
            with resources.files("barangay.data").joinpath(filename).open("rb") as f:
                content = f.read()
        except (AttributeError, TypeError, FileNotFoundError):
            try:
                with resources.path("barangay.data", filename) as path:
                    with open(path, "rb") as f:
                        content = f.read()
            except (FileNotFoundError, Exception):
                data_dir = Path(__file__).parent / "data"
                file_path = data_dir / filename
                if file_path.exists():
                    with open(file_path, "rb") as f:
                        content = f.read()
                else:
                    raise FileNotFoundError(f"Data file not found: {file_path}")

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
    ) -> dict | list[dict] | pd.DataFrame | None:
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
    ) -> dict | list[dict] | pd.DataFrame:
        from .downloader import download_data

        filename = DATA_TYPE_MAPPING[data_type]
        cache_file = download_data(resolved_date, data_type, self._cache_dir)

        if filename.endswith(".json"):
            with open(cache_file) as f:
                return json.load(f)
        elif filename.endswith(".parquet"):
            import pandas as pd

            return pd.read_parquet(cache_file)
        else:
            raise ValueError(f"Unsupported file type: {filename}")

    def _save_to_cache(self, resolved_date: str, data_type: str, data) -> None:
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
        if not verbose or self._logged_dataset:
            return

        logger.info(f"[barangay] {status_message}")
        self._logged_dataset = True

    def _get_cache_dir(self) -> Path:
        cache_dir = os.getenv("BARANGAY_CACHE_DIR")
        if cache_dir:
            return Path(cache_dir)

        if os.name == "nt":
            local_app_data = os.getenv("LOCALAPPDATA")
            if local_app_data:
                return Path(local_app_data) / "barangay" / "cache"

        xdg_cache_home = os.getenv("XDG_CACHE_HOME")
        if xdg_cache_home:
            return Path(xdg_cache_home) / "barangay"

        return Path.home() / ".cache" / "barangay"
