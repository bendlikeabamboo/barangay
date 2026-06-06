import json
from unittest.mock import MagicMock, patch

import pytest
import yaml

from barangay.data_manager import DataManager
from barangay.database import Database
from barangay.fuzz import _fuzz_base_cache, create_fuzz_base, invalidate_fuzz_cache
from barangay.plugin_loader import (
    PluginLoader,
    load_plugin_data,
)
from barangay.version import use_version


def _create_plugin(tmp_path, name, manifest, data_files):
    plugin_dir = tmp_path / name
    plugin_dir.mkdir()
    (plugin_dir / "manifest.yaml").write_text(yaml.dump(manifest))
    data_dir = plugin_dir / "data"
    data_dir.mkdir()
    for filename, content in data_files.items():
        filepath = data_dir / filename
        filepath.write_text(content) if isinstance(
            content, str
        ) else filepath.write_bytes(content)
    return plugin_dir


def _make_manifest(name, fmt="csv", key="psgc_id", **overrides):
    manifest = {"name": name, "format": fmt, "key": key, **overrides}
    return manifest


@pytest.fixture(autouse=True)
def reset_global_state():
    yield
    use_version(None)
    invalidate_fuzz_cache()


class TestDataManagerMemoryCacheWithAsOf:
    @patch("barangay.date_resolver.get_available_dates", return_value=["2025-01-01"])
    def test_historical_date_creates_dated_cache_key(self, _mock_dates):
        dm = DataManager()
        fixture_data = {"test": True}
        with patch.object(dm, "_download_from_github", return_value=fixture_data):
            result = dm.get_data(as_of="2025-01-01", data_type="basic")

        assert "2025-01-01_basic" in dm._memory_cache
        assert dm._memory_cache["2025-01-01_basic"] is result

    @patch("barangay.date_resolver.get_available_dates", return_value=["2025-01-01"])
    def test_same_as_of_returns_cached_result(self, _mock_dates):
        dm = DataManager()
        fixture_data = {"test": True}
        with patch.object(
            dm, "_download_from_github", return_value=fixture_data
        ) as mock_dl:
            dm.get_data(as_of="2025-01-01", data_type="basic")
            dm.get_data(as_of="2025-01-01", data_type="basic")

        mock_dl.assert_called_once()

    @patch(
        "barangay.date_resolver.get_available_dates",
        return_value=["2025-01-01", "2025-06-01"],
    )
    def test_different_as_of_creates_separate_cache_entry(self, _mock_dates):
        dm = DataManager()
        data_1 = {"version": 1}
        data_2 = {"version": 2}
        with patch.object(dm, "_download_from_github", side_effect=[data_1, data_2]):
            r1 = dm.get_data(as_of="2025-01-01", data_type="basic")
            r2 = dm.get_data(as_of="2025-06-01", data_type="basic")

        assert r1 is not r2
        assert "2025-01-01_basic" in dm._memory_cache
        assert "2025-06-01_basic" in dm._memory_cache
        assert dm._memory_cache["2025-01-01_basic"] == {"version": 1}
        assert dm._memory_cache["2025-06-01_basic"] == {"version": 2}

    @patch("barangay.date_resolver.get_available_dates", return_value=["2025-01-01"])
    def test_default_key_is_separate_from_historical(self, _mock_dates):
        dm = DataManager()
        default_result = dm.get_data(as_of=None, data_type="basic")

        assert "default_basic" in dm._memory_cache
        assert "2025-01-01_basic" not in dm._memory_cache

        fixture_data = {"historical": True}
        with patch.object(dm, "_download_from_github", return_value=fixture_data):
            hist_result = dm.get_data(as_of="2025-01-01", data_type="basic")

        assert dm._memory_cache["default_basic"] is default_result
        assert dm._memory_cache["2025-01-01_basic"] is hist_result


class TestFuzzBaseCacheWithAsOf:
    def test_same_as_of_returns_same_object(self):
        fb1 = create_fuzz_base(as_of=None)
        fb2 = create_fuzz_base(as_of=None)
        assert fb1 is fb2

    def test_historical_as_of_is_cached(self):
        fb1 = create_fuzz_base(as_of=None)
        assert None in _fuzz_base_cache
        assert _fuzz_base_cache[None] is fb1

    def test_different_as_of_creates_separate_entry(self):
        invalidate_fuzz_cache()
        create_fuzz_base(as_of=None)
        assert len(_fuzz_base_cache) == 1

    def test_invalidate_clears_all_entries(self):
        create_fuzz_base(as_of=None)
        assert len(_fuzz_base_cache) >= 1
        invalidate_fuzz_cache()
        assert len(_fuzz_base_cache) == 0


class TestDatabaseSingletonCacheWithAsOf:
    @pytest.fixture(autouse=True)
    def reset_db_singleton(self):
        Database._instance = None
        yield
        Database._instance = None

    def test_ensure_loaded_short_circuits(self):
        db = Database()
        db._ensure_loaded()
        assert db._raw_records is not None

        records_id = id(db._raw_records)
        db._ensure_loaded()
        assert id(db._raw_records) == records_id

    def test_version_switch_invalidates_cache(self):
        db = Database()
        db._ensure_loaded()
        assert db._raw_records is not None

        use_version("2025-07-08")
        assert db._raw_records is None

        db._ensure_loaded()
        assert db._raw_records is not None

    def test_ensure_loaded_with_plugin_calls_build_index_once(self, tmp_path):
        csv_content = "psgc_id,population\n001,1000\n"
        _create_plugin(tmp_path, "pop", _make_manifest("pop"), {"pop.csv": csv_content})
        (tmp_path / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": True}]})
        )

        loader = PluginLoader(env=False, extra_dirs=[tmp_path])
        mock_loader = MagicMock(wraps=loader)
        mock_loader.build_index = MagicMock(wraps=loader.build_index)

        db = Database()
        db.use_plugins(plugins=["pop"], loader=mock_loader)

        db._ensure_loaded()
        db._ensure_loaded()

        mock_loader.build_index.assert_called_once()


class TestPluginDiskCacheWithAsOf:
    @patch("barangay.plugin_loader._fetch_remote_data_file")
    def test_disk_cache_hit_avoids_network(self, mock_fetch, tmp_path):
        json_content = json.dumps([{"psgc_id": "001", "value": 42}])
        cache_dir = tmp_path / "cache"
        plugin_cache_dir = cache_dir / "plugins"
        plugin_cache_dir.mkdir(parents=True)

        def write_and_return(url, plugin_name, cache_dir=None):
            actual_dir = cache_dir if cache_dir else plugin_cache_dir
            actual_dir.mkdir(parents=True, exist_ok=True)
            out = actual_dir / "demo_demo.json"
            out.write_text(json_content)
            return out

        mock_fetch.side_effect = write_and_return

        manifest = _make_manifest(
            "demo", fmt="json", repository="https://github.com/user/repo"
        )
        _create_plugin(tmp_path, "demo", manifest, {})

        with patch("barangay.plugin_loader.get_cache_dir", return_value=cache_dir):
            load_plugin_data(
                manifest, resolved_date="2025-01-01", plugin_dirs=[tmp_path]
            )
            load_plugin_data(
                manifest, resolved_date="2025-01-01", plugin_dirs=[tmp_path]
            )

        mock_fetch.assert_called_once()
