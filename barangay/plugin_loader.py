import csv
import json
import logging
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

import yaml

from barangay.config import get_cache_dir
from barangay.models import (
    PluginExtensionMetadata,
)
from barangay.utils import to_python_identifier

logger = logging.getLogger(__name__)

_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

_BUILTIN_PLUGINS_DIR = Path(__file__).parent / "plugins"

__all__ = [
    "PluginDataError",
    "PluginLoader",
    "PluginManifestError",
    "build_plugin_index",
    "enrich_extended",
    "enrich_flat",
    "load_manifest",
    "load_plugin_config",
    "load_plugin_data",
    "resolve_plugin_date",
    "resolve_plugin_sources",
]


class PluginManifestError(Exception):
    pass


class PluginDataError(Exception):
    pass


def resolve_plugin_sources(
    env: bool = True,
    config_file: str | Path | None = None,
    extra_dirs: list[str | Path] | None = None,
) -> list[Path]:
    dirs: list[Path] = []

    if _BUILTIN_PLUGINS_DIR.is_dir():
        dirs.append(_BUILTIN_PLUGINS_DIR)

    if env:
        env_path = os.environ.get("BARANGAY_PLUGINS_DIR")
        if env_path:
            dirs.extend(Path(p) for p in env_path.split(os.pathsep))

    cfg = _load_project_config(config_file)
    if cfg and "plugin_dirs" in cfg:
        for d in cfg["plugin_dirs"]:
            dirs.append(Path(d))

    if extra_dirs:
        dirs.extend(Path(d) for d in extra_dirs)

    return dirs


def _load_project_config(config_file: str | Path | None = None) -> dict | None:
    if config_file:
        path = Path(config_file)
        if path.is_file():
            cfg = yaml.safe_load(path.read_text())
            return cfg if isinstance(cfg, dict) else None
        return None

    cwd = Path.cwd()
    candidates = ["barangay.yaml", "barangay_config.yaml"]
    current = cwd
    while True:
        for name in candidates:
            path = current / name
            if path.is_file():
                cfg = yaml.safe_load(path.read_text())
                return cfg if isinstance(cfg, dict) else None
        parent = current.parent
        if parent == current:
            break
        current = parent

    return None


def load_plugin_config(
    plugin_dirs: list[Path] | None = None,
) -> dict[str, bool]:
    if plugin_dirs is None:
        plugin_dirs = resolve_plugin_sources()

    merged: dict[str, bool] = {}

    for plugin_dir in plugin_dirs:
        config_path = plugin_dir / "plugins.yaml"
        if not config_path.is_file():
            continue
        try:
            cfg = yaml.safe_load(config_path.read_text())
        except (yaml.YAMLError, OSError) as e:
            logger.warning("Failed to load %s: %s", config_path, e)
            continue

        plugins_list = cfg.get("plugins")
        if not plugins_list or not isinstance(plugins_list, list):
            continue

        for entry in plugins_list:
            name = entry.get("name")
            if not name:
                continue
            merged[name] = entry.get("enabled", False)

    return merged


def _find_plugin_dir(plugin_name: str, plugin_dirs: list[Path]) -> Path | None:
    result: Path | None = None
    for plugin_dir in plugin_dirs:
        candidate = plugin_dir / plugin_name
        if candidate.is_dir():
            result = candidate
    return result


def load_manifest(
    plugin_name: str,
    plugin_dirs: list[Path] | None = None,
) -> dict[str, Any]:
    if plugin_dirs is None:
        plugin_dirs = resolve_plugin_sources()

    plugin_path = _find_plugin_dir(plugin_name, plugin_dirs)
    if plugin_path is None:
        raise PluginManifestError(
            f"Plugin '{plugin_name}' not found in any plugin directory"
        )

    manifest_path = plugin_path / "manifest.yaml"
    if not manifest_path.is_file():
        raise PluginManifestError(f"Missing manifest.yaml for plugin '{plugin_name}'")

    try:
        manifest = yaml.safe_load(manifest_path.read_text())
    except (yaml.YAMLError, OSError) as e:
        raise PluginManifestError(f"Failed to parse manifest for '{plugin_name}': {e}")

    if not isinstance(manifest, dict):
        raise PluginManifestError(f"Invalid manifest format for '{plugin_name}'")

    for required in ("name", "format", "key"):
        if required not in manifest:
            raise PluginManifestError(
                f"Missing required field '{required}' in manifest for '{plugin_name}'"
            )

    return manifest


def _is_time_aware(plugin_name: str, plugin_dirs: list[Path] | None = None) -> bool:
    if plugin_dirs is None:
        plugin_dirs = resolve_plugin_sources()

    plugin_path = _find_plugin_dir(plugin_name, plugin_dirs)
    if plugin_path is None:
        return False

    data_dir = plugin_path / "data"
    if not data_dir.is_dir():
        return False

    for entry in data_dir.iterdir():
        if entry.is_dir() and _DATE_PATTERN.match(entry.name):
            return True

    return False


def resolve_plugin_date(
    as_of: str | None,
    plugin_dates: list[str],
    plugin_current: str,
) -> str:
    if as_of is None:
        return plugin_current

    if as_of in plugin_dates:
        return as_of

    dates_before = [d for d in plugin_dates if d <= as_of]
    if dates_before:
        return max(dates_before)

    return min(plugin_dates)


def load_plugin_data(
    manifest: dict[str, Any],
    resolved_date: str | None = None,
    plugin_dirs: list[Path] | None = None,
) -> dict[str, dict[str, Any]]:
    if plugin_dirs is None:
        plugin_dirs = resolve_plugin_sources()

    plugin_name = manifest["name"]
    fmt = manifest["format"]
    key = manifest.get("key", "psgc_id")

    plugin_path = _find_plugin_dir(plugin_name, plugin_dirs)
    if plugin_path is None:
        return {}

    data_dir = plugin_path / "data"

    if data_dir.is_dir():
        data_file = _resolve_data_file(
            data_dir, resolved_date, fmt, plugin_name=plugin_name
        )
        if data_file is not None:
            return _read_data_file(data_file, fmt, key)

    repository = manifest.get("repository")
    if repository:
        repo = repository.rstrip("/").split("github.com/")[-1]
        extensions = {"csv": ".csv", "json": ".json", "parquet": ".parquet"}
        ext = extensions.get(fmt, f".{fmt}")
        filename = f"{plugin_name}{ext}"

        ref = manifest.get("ref", "main")
        if resolved_date:
            url = f"https://raw.githubusercontent.com/{repo}/{ref}/{resolved_date}/{filename}"
        else:
            url = f"https://raw.githubusercontent.com/{repo}/{ref}/{filename}"

        cache_dir = get_cache_dir() / "plugins"
        cache_file = cache_dir / f"{plugin_name}_{filename}"

        if cache_file.is_file():
            return _read_data_file(cache_file, fmt, key)

        remote_file = _fetch_remote_data_file(url, plugin_name, cache_dir=cache_dir)
        return _read_data_file(remote_file, fmt, key)

    return {}


def _fetch_remote_data_file(
    url: str,
    plugin_name: str,
    cache_dir: Path | None = None,
) -> Path:
    if cache_dir is None:
        cache_dir = get_cache_dir() / "plugins"
    cache_dir.mkdir(parents=True, exist_ok=True)

    filename = url.rsplit("/", 1)[-1]
    cache_key = f"{plugin_name}_{filename}"
    cache_file = cache_dir / cache_key

    if cache_file.is_file():
        return cache_file

    try:
        request = Request(url, headers={"User-Agent": "barangay-package"})
        with urlopen(request, timeout=30) as response:
            content = response.read()
        with open(cache_file, "wb") as f:
            f.write(content)
        return cache_file
    except Exception as e:
        raise PluginDataError(f"Failed to fetch remote file {url}: {e}") from e


def _fetch_remote_dates(
    repo_url: str,
    cache_dir: Path | None = None,
) -> list[str]:
    repo = repo_url.rstrip("/").split("github.com/")[-1]
    api_url = f"https://api.github.com/repos/{repo}/contents/"

    if cache_dir is None:
        cache_dir = get_cache_dir() / "plugins"
    cache_dir.mkdir(parents=True, exist_ok=True)

    safe_name = repo.replace("/", "_")
    cache_file = cache_dir / f"{safe_name}_dates.json"

    if cache_file.is_file():
        try:
            cached = json.loads(cache_file.read_text())
            if isinstance(cached, list):
                return cached
        except (json.JSONDecodeError, OSError):
            pass

    try:
        request = Request(
            api_url,
            headers={
                "Accept": "application/vnd.github.v3+json",
                "User-Agent": "barangay-package",
            },
        )
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())

        dates = []
        for item in data:
            if item.get("type") == "dir":
                name = item["name"]
                if _DATE_PATTERN.match(name):
                    try:
                        datetime.strptime(name, "%Y-%m-%d")
                        dates.append(name)
                    except ValueError:
                        pass

        dates.sort()
        cache_file.write_text(json.dumps(dates))
        return dates
    except Exception as e:
        logger.warning("Failed to fetch remote dates for %s: %s", repo_url, e)
        return []


def _resolve_data_file(
    data_dir: Path,
    resolved_date: str | None,
    fmt: str,
    plugin_name: str | None = None,
) -> Path | None:
    extensions = {"csv": ".csv", "json": ".json", "parquet": ".parquet"}
    ext = extensions.get(fmt, f".{fmt}")

    if resolved_date and plugin_name:
        date_folder_file = data_dir / resolved_date / f"{plugin_name}{ext}"
        if date_folder_file.is_file():
            return date_folder_file

    if plugin_name:
        named_file = data_dir / f"{plugin_name}{ext}"
        if named_file.is_file():
            return named_file

    if plugin_name:
        for d in sorted(data_dir.iterdir()):
            if d.is_dir() and _DATE_PATTERN.match(d.name):
                candidate = d / f"{plugin_name}{ext}"
                if candidate.is_file():
                    return candidate

    return None


def _read_data_file(
    data_file: Path,
    fmt: str,
    key: str,
) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}

    try:
        if fmt == "csv":
            with open(data_file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    psgc_id = row.get(key)
                    if psgc_id is None:
                        continue
                    result[psgc_id] = {k: v for k, v in row.items() if k != key}

        elif fmt == "json":
            data = json.loads(data_file.read_text(encoding="utf-8"))
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, dict):
                        continue
                    psgc_id = item.get(key)
                    if psgc_id is None:
                        continue
                    result[str(psgc_id)] = {k: v for k, v in item.items() if k != key}

        elif fmt == "parquet":
            import pandas as pd

            df = pd.read_parquet(data_file)
            if key not in df.columns:
                return {}
            for _, row in df.iterrows():
                psgc_id = str(row[key])
                result[psgc_id] = {col: row[col] for col in df.columns if col != key}
    except (OSError, csv.Error, ValueError, json.JSONDecodeError) as e:
        raise PluginDataError(
            f"Failed to read plugin data file {data_file}: {e}"
        ) from e
    except Exception as e:
        raise PluginDataError(
            f"Failed to read plugin data file {data_file}: {e}"
        ) from e

    return result


def _extract_metadata(
    manifest: dict[str, Any],
    resolved_date: str | None = None,
) -> PluginExtensionMetadata:
    return PluginExtensionMetadata(
        name=manifest["name"],
        description=manifest.get("description"),
        version=manifest.get("version"),
        repository=manifest.get("repository"),
        format=manifest.get("format"),
        as_of=resolved_date,
    )


def build_plugin_index(
    as_of: str | None = None,
    plugin_config: dict[str, bool] | None = None,
    plugin_dirs: list[Path] | None = None,
) -> dict[str, dict[str, dict[str, Any]]]:
    if plugin_config is None:
        plugin_config = load_plugin_config(plugin_dirs=plugin_dirs)

    if plugin_dirs is None:
        plugin_dirs = resolve_plugin_sources()

    index: dict[str, dict[str, dict[str, Any]]] = {}

    for name, enabled in plugin_config.items():
        if not enabled:
            continue

        try:
            manifest = load_manifest(name, plugin_dirs=plugin_dirs)
        except PluginManifestError as e:
            logger.warning("Skipping plugin '%s': %s", name, e)
            continue

        time_aware = _is_time_aware(name, plugin_dirs=plugin_dirs)
        repository = manifest.get("repository")
        resolved_date: str | None = None

        if repository and not time_aware:
            plugin_dates = manifest.get("dates", [])
            if not plugin_dates:
                plugin_dates = _fetch_remote_dates(repository)
            plugin_current = manifest.get("current", "")
            if plugin_dates:
                time_aware = True
                manifest["dates"] = plugin_dates
                resolved_date = resolve_plugin_date(as_of, plugin_dates, plugin_current)

        if time_aware and resolved_date is None:
            plugin_dates = manifest.get("dates", [])
            plugin_current = manifest.get("current", "")
            if plugin_dates:
                resolved_date = resolve_plugin_date(as_of, plugin_dates, plugin_current)

        plugin_data = load_plugin_data(manifest, resolved_date, plugin_dirs=plugin_dirs)
        meta = _extract_metadata(manifest, resolved_date=resolved_date)
        attr_name = to_python_identifier(name)

        seen: dict[str, str] = {}
        for psgc_id, fields in plugin_data.items():
            if attr_name in index.get(psgc_id, {}):
                existing = seen.get(attr_name, name)
                if existing == name:
                    logger.warning(
                        "Plugin name collision: '%s' and an already-loaded plugin "
                        "both map to attribute name '%s'",
                        name,
                        attr_name,
                    )
                    seen[attr_name] = name
            index.setdefault(psgc_id, {})[attr_name] = {
                "metadata": meta,
                "data": fields,
            }

    return index


def enrich_flat(
    flat_data: list[dict[str, Any]],
    plugin_index: dict[str, dict[str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    for record in flat_data:
        psgc_id = str(record.get("psgc_id", ""))
        if psgc_id in plugin_index:
            record["extensions"] = [
                {
                    "field_group": group_name,
                    "metadata": entry["metadata"],
                    "data": entry["data"],
                }
                for group_name, entry in plugin_index[psgc_id].items()
            ]
        else:
            record["extensions"] = []
    return flat_data


def enrich_extended(
    node: dict[str, Any],
    plugin_index: dict[str, dict[str, dict[str, Any]]],
) -> dict[str, Any]:
    psgc_id = str(node.get("psgc_id", ""))
    if psgc_id in plugin_index:
        node["extensions"] = [
            {
                "field_group": group_name,
                "metadata": entry["metadata"],
                "data": entry["data"],
            }
            for group_name, entry in plugin_index[psgc_id].items()
        ]
    else:
        node["extensions"] = []
    for child in node.get("components", []):
        enrich_extended(child, plugin_index)
    return node


class PluginLoader:
    def __init__(
        self,
        env: bool = True,
        config_file: str | Path | None = None,
        extra_dirs: list[str | Path] | None = None,
    ):
        self._plugin_dirs = resolve_plugin_sources(
            env=env,
            config_file=config_file,
            extra_dirs=extra_dirs,
        )
        self._plugin_config: dict[str, bool] = load_plugin_config(self._plugin_dirs)

    def add_plugin_dir(self, path: str | Path) -> None:
        self._plugin_dirs.append(Path(path))
        self._plugin_config = load_plugin_config(self._plugin_dirs)

    def enable_plugin(self, name: str) -> None:
        self._plugin_config[name] = True

    def disable_plugin(self, name: str) -> None:
        self._plugin_config[name] = False

    def build_index(
        self, as_of: str | None = None
    ) -> dict[str, dict[str, dict[str, Any]]]:
        return build_plugin_index(
            as_of=as_of,
            plugin_config=self._plugin_config,
            plugin_dirs=self._plugin_dirs,
        )

    def enrich_flat(
        self,
        flat_data: list[dict[str, Any]],
        as_of: str | None = None,
    ) -> list[dict[str, Any]]:
        index = self.build_index(as_of=as_of)
        return enrich_flat(flat_data, index)

    def enrich_extended(
        self,
        node: dict[str, Any],
        as_of: str | None = None,
    ) -> dict[str, Any]:
        index = self.build_index(as_of=as_of)
        return enrich_extended(node, index)
