import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

from barangay.plugin_loader import (
    PluginLoader,
    PluginManifestError,
    _fetch_remote_data_file,
    _fetch_remote_dates,
    build_plugin_index,
    enrich_extended,
    enrich_flat,
    load_manifest,
    load_plugin_config,
    load_plugin_data,
    resolve_plugin_date,
)
from barangay.models import (
    PluginExtension,
    PluginExtensionMetadata,
    AdminDivExtended,
    AdminDivFlat,
)


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


class TestResolvePluginDate:
    def test_none_returns_current(self):
        assert (
            resolve_plugin_date(None, ["2020-01-01", "2021-01-01"], "2021-01-01")
            == "2021-01-01"
        )

    def test_exact_match(self):
        assert (
            resolve_plugin_date(
                "2020-01-01", ["2020-01-01", "2021-01-01"], "2021-01-01"
            )
            == "2020-01-01"
        )

    def test_closest_before(self):
        assert (
            resolve_plugin_date(
                "2020-06-15", ["2020-01-01", "2021-01-01"], "2021-01-01"
            )
            == "2020-01-01"
        )

    def test_before_all_dates(self):
        assert (
            resolve_plugin_date(
                "2019-01-01", ["2020-01-01", "2021-01-01"], "2021-01-01"
            )
            == "2020-01-01"
        )

    def test_after_all_dates(self):
        assert (
            resolve_plugin_date(
                "2022-06-01", ["2020-01-01", "2021-01-01"], "2021-01-01"
            )
            == "2021-01-01"
        )


class TestLoadPluginConfig:
    def test_loads_from_plugin_dirs(self, tmp_path):
        plugins_yaml = tmp_path / "plugins.yaml"
        plugins_yaml.write_text(
            yaml.dump(
                {
                    "plugins": [
                        {"name": "pop", "enabled": True},
                        {"name": "elevation", "enabled": False},
                    ]
                }
            )
        )
        config = load_plugin_config(plugin_dirs=[tmp_path])
        assert config == {"pop": True, "elevation": False}

    def test_higher_priority_overrides(self, tmp_path):
        lower = tmp_path / "lower"
        lower.mkdir()
        (lower / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": True}]})
        )
        higher = tmp_path / "higher"
        higher.mkdir()
        (higher / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": False}]})
        )
        config = load_plugin_config(plugin_dirs=[lower, higher])
        assert config["pop"] is False

    def test_missing_plugins_yaml_returns_empty(self, tmp_path):
        config = load_plugin_config(plugin_dirs=[tmp_path])
        assert config == {}


class TestLoadManifest:
    def test_valid_manifest(self, tmp_path):
        _create_plugin(
            tmp_path,
            "demo",
            _make_manifest("demo", description="A demo", version="1.0"),
            {},
        )
        manifest = load_manifest("demo", plugin_dirs=[tmp_path])
        assert manifest["name"] == "demo"
        assert manifest["format"] == "csv"
        assert manifest["key"] == "psgc_id"
        assert manifest["description"] == "A demo"
        assert manifest["version"] == "1.0"

    def test_missing_required_field(self, tmp_path):
        bad_manifest = {"name": "demo", "key": "psgc_id"}
        _create_plugin(tmp_path, "bad", bad_manifest, {})
        with pytest.raises(PluginManifestError, match="format"):
            load_manifest("bad", plugin_dirs=[tmp_path])

    def test_plugin_not_found(self, tmp_path):
        with pytest.raises(PluginManifestError, match="not_found"):
            load_manifest("not_found", plugin_dirs=[tmp_path])


class TestLoadPluginData:
    def test_load_csv_data(self, tmp_path):
        csv_content = "psgc_id,population,area\n001,1000,5.2\n002,2000,10.1\n"
        manifest = _make_manifest("pop", fmt="csv")
        _create_plugin(tmp_path, "pop", manifest, {"pop.csv": csv_content})
        data = load_plugin_data(manifest, plugin_dirs=[tmp_path])
        assert data["001"]["population"] == "1000"
        assert data["001"]["area"] == "5.2"
        assert data["002"]["population"] == "2000"
        assert "psgc_id" not in data["001"]

    def test_load_json_data(self, tmp_path):
        json_content = json.dumps(
            [
                {"psgc_id": "001", "elevation": 100, "zone": "urban"},
                {"psgc_id": "002", "elevation": 50, "zone": "rural"},
            ]
        )
        manifest = _make_manifest("elev", fmt="json")
        _create_plugin(tmp_path, "elev", manifest, {"elev.json": json_content})
        data = load_plugin_data(manifest, plugin_dirs=[tmp_path])
        assert data["001"]["elevation"] == 100
        assert data["002"]["zone"] == "rural"
        assert "psgc_id" not in data["001"]

    def test_missing_data_dir_returns_empty(self, tmp_path):
        _create_plugin(tmp_path, "nodata", _make_manifest("nodata"), {})
        manifest = _make_manifest("nodata")
        data = load_plugin_data(manifest, plugin_dirs=[tmp_path])
        assert data == {}

    def test_unmatched_psgc_id_excluded(self, tmp_path):
        csv_content = "psgc_id,value\n001,10\n002,20\n"
        manifest = _make_manifest("val", fmt="csv")
        _create_plugin(tmp_path, "val", manifest, {"val.csv": csv_content})
        data = load_plugin_data(manifest, plugin_dirs=[tmp_path])
        assert "001" in data
        assert "002" in data
        assert len(data) == 2


class TestBuildPluginIndex:
    def test_builds_index_from_enabled_plugins(self, tmp_path):
        csv_content = "psgc_id,population\n133900000,50000\n"
        _create_plugin(tmp_path, "pop", _make_manifest("pop"), {"pop.csv": csv_content})
        (tmp_path / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": True}]})
        )
        config = load_plugin_config(plugin_dirs=[tmp_path])
        index = build_plugin_index(plugin_config=config, plugin_dirs=[tmp_path])
        assert "133900000" in index
        assert "pop" in index["133900000"]
        assert index["133900000"]["pop"]["data"]["population"] == "50000"

    def test_disabled_plugins_skipped(self, tmp_path):
        csv_content = "psgc_id,population\n133900000,50000\n"
        _create_plugin(tmp_path, "pop", _make_manifest("pop"), {"pop.csv": csv_content})
        (tmp_path / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": False}]})
        )
        config = load_plugin_config(plugin_dirs=[tmp_path])
        index = build_plugin_index(plugin_config=config, plugin_dirs=[tmp_path])
        assert "133900000" not in index

    def test_plugin_with_manifest_error_skipped(self, tmp_path):
        bad_dir = tmp_path / "bad"
        bad_dir.mkdir()
        (bad_dir / "manifest.yaml").write_text("not: a: valid: yaml: [")
        config = {"bad": True}
        index = build_plugin_index(plugin_config=config, plugin_dirs=[tmp_path])
        assert index == {}

    def test_empty_index_when_no_plugins_enabled(self, tmp_path):
        config = {}
        index = build_plugin_index(plugin_config=config, plugin_dirs=[tmp_path])
        assert index == {}


class TestEnrichFlat:
    def test_records_with_matching_psgc_id_get_extensions(self):
        meta = PluginExtensionMetadata(name="pop", description="population data")
        plugin_index = {
            "001": {
                "pop": {"metadata": meta, "data": {"population": "1000"}},
            }
        }
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = enrich_flat(flat_data, plugin_index)
        assert len(result[0]["extensions"]) == 1
        assert result[0]["extensions"][0]["field_group"] == "pop"
        assert result[0]["extensions"][0]["data"]["population"] == "1000"

    def test_records_without_match_get_empty_extensions(self):
        plugin_index = {}
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = enrich_flat(flat_data, plugin_index)
        assert result[0]["extensions"] == []

    def test_multiple_plugins_per_record(self):
        meta1 = PluginExtensionMetadata(name="pop", description="population")
        meta2 = PluginExtensionMetadata(name="elev", description="elevation")
        plugin_index = {
            "001": {
                "pop": {"metadata": meta1, "data": {"population": "1000"}},
                "elev": {"metadata": meta2, "data": {"elevation": 100}},
            }
        }
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = enrich_flat(flat_data, plugin_index)
        assert len(result[0]["extensions"]) == 2
        groups = {e["field_group"] for e in result[0]["extensions"]}
        assert groups == {"pop", "elev"}


class TestEnrichExtended:
    def test_matching_node_gets_extensions(self):
        meta = PluginExtensionMetadata(name="pop", description="population")
        plugin_index = {
            "130000000": {
                "pop": {"metadata": meta, "data": {"population": "50000"}},
            }
        }
        node = {
            "psgc_id": "130000000",
            "name": "NCR",
            "type": "region",
            "components": [],
        }
        result = enrich_extended(node, plugin_index)
        assert len(result["extensions"]) == 1
        assert result["extensions"][0]["field_group"] == "pop"

    def test_non_matching_node_gets_empty_extensions(self):
        plugin_index = {}
        node = {
            "psgc_id": "130000000",
            "name": "NCR",
            "type": "region",
            "components": [],
        }
        result = enrich_extended(node, plugin_index)
        assert result["extensions"] == []

    def test_children_also_enriched(self):
        meta = PluginExtensionMetadata(name="pop", description="population")
        plugin_index = {
            "013754000": {
                "pop": {"metadata": meta, "data": {"population": "2000"}},
            }
        }
        child = {
            "psgc_id": "013754000",
            "name": "Barangay 1",
            "type": "barangay",
            "components": [],
        }
        node = {
            "psgc_id": "130000000",
            "name": "NCR",
            "type": "region",
            "components": [child],
        }
        result = enrich_extended(node, plugin_index)
        assert result["extensions"] == []
        assert len(result["components"][0]["extensions"]) == 1
        assert result["components"][0]["extensions"][0]["data"]["population"] == "2000"


class TestTimeAwareness:
    def test_date_folder_triggers_time_aware(self, tmp_path):
        plugin_dir = _create_plugin(tmp_path, "ta", _make_manifest("ta"), {})
        date_dir = plugin_dir / "data" / "2024-01-01"
        date_dir.mkdir(parents=True)
        (date_dir / "ta.csv").write_text("psgc_id,val\n001,10\n")
        from barangay.plugin_loader import _is_time_aware

        assert _is_time_aware("ta", plugin_dirs=[tmp_path]) is True

    def test_plain_filename_triggers_time_unaware(self, tmp_path):
        _create_plugin(
            tmp_path, "tu", _make_manifest("tu"), {"tu.csv": "psgc_id,val\n001,10\n"}
        )
        from barangay.plugin_loader import _is_time_aware

        assert _is_time_aware("tu", plugin_dirs=[tmp_path]) is False


class TestPluginLoader:
    def test_enable_disable_plugin(self, tmp_path):
        loader = PluginLoader(env=False, extra_dirs=[])
        loader.enable_plugin("pop")
        assert loader._plugin_config["pop"] is True
        loader.disable_plugin("pop")
        assert loader._plugin_config["pop"] is False

    def test_add_plugin_dir(self, tmp_path):
        csv_content = "psgc_id,population\n001,1000\n"
        _create_plugin(tmp_path, "pop", _make_manifest("pop"), {"pop.csv": csv_content})
        (tmp_path / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": True}]})
        )
        loader = PluginLoader(env=False, extra_dirs=[])
        assert "pop" not in loader._plugin_config
        loader.add_plugin_dir(tmp_path)
        assert loader._plugin_config.get("pop") is True

    def test_enrich_flat_with_loader(self, tmp_path):
        csv_content = "psgc_id,population\n001,1000\n"
        _create_plugin(tmp_path, "pop", _make_manifest("pop"), {"pop.csv": csv_content})
        (tmp_path / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": True}]})
        )
        loader = PluginLoader(env=False, extra_dirs=[tmp_path])
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = loader.enrich_flat(flat_data)
        assert len(result[0]["extensions"]) == 1
        assert result[0]["extensions"][0]["data"]["population"] == "1000"

    def test_enrich_extended_with_loader(self, tmp_path):
        csv_content = "psgc_id,population\n001,1000\n"
        _create_plugin(tmp_path, "pop", _make_manifest("pop"), {"pop.csv": csv_content})
        (tmp_path / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "pop", "enabled": True}]})
        )
        loader = PluginLoader(env=False, extra_dirs=[tmp_path])
        node = {"psgc_id": "001", "name": "Test", "type": "barangay", "components": []}
        result = loader.enrich_extended(node)
        assert len(result["extensions"]) == 1
        assert result["extensions"][0]["data"]["population"] == "1000"


class TestModelsExtensionField:
    def test_admin_div_extended_accepts_extensions(self):
        ext = PluginExtension(
            field_group="pop",
            metadata=PluginExtensionMetadata(name="pop"),
            data={"population": 1000},
        )
        model = AdminDivExtended(
            name="Test",
            type="region",
            psgc_id="130000000",
            parent_psgc_id="000000000",
            extensions=[ext],
        )
        assert len(model.extensions) == 1
        assert model.extensions[0].field_group == "pop"

    def test_admin_div_flat_accepts_extensions(self):
        ext = PluginExtension(
            field_group="pop",
            metadata=PluginExtensionMetadata(name="pop"),
            data={"population": 1000},
        )
        model = AdminDivFlat(
            name="Test",
            type="region",
            psgc_id="130000000",
            parent_psgc_id="000000000",
            extensions=[ext],
        )
        assert len(model.extensions) == 1
        assert model.extensions[0].field_group == "pop"

    def test_default_extensions_is_empty_list(self):
        ext_model = AdminDivExtended(
            name="Test",
            type="region",
            psgc_id="130000000",
            parent_psgc_id="000000000",
        )
        assert ext_model.extensions == []
        flat_model = AdminDivFlat(
            name="Test",
            type="region",
            psgc_id="130000000",
            parent_psgc_id="000000000",
        )
        assert flat_model.extensions == []

    def test_plugin_extension_validation(self):
        meta = PluginExtensionMetadata(name="demo", version="1.0")
        ext = PluginExtension(field_group="demo", metadata=meta, data={"key": "val"})
        assert ext.field_group == "demo"
        assert ext.metadata.name == "demo"
        assert ext.metadata.version == "1.0"
        assert ext.data == {"key": "val"}


class TestArrayDataSupport:
    def test_plugin_extension_accepts_list_data(self):
        meta = PluginExtensionMetadata(name="schools", description="school list")
        ext = PluginExtension(
            field_group="schools",
            metadata=meta,
            data=[
                {"beiss_id": 123, "name": "School A", "classification": "Elementary"},
                {"beiss_id": 456, "name": "School B", "classification": "Junior"},
            ],
        )
        assert isinstance(ext.data, list)
        assert len(ext.data) == 2
        assert ext.data[0]["beiss_id"] == 123

    def test_plugin_extension_accepts_dict_data(self):
        meta = PluginExtensionMetadata(name="pop", description="population")
        ext = PluginExtension(
            field_group="pop",
            metadata=meta,
            data={"population": 1000, "area": 5.2},
        )
        assert isinstance(ext.data, dict)
        assert ext.data["population"] == 1000

    def test_enrich_flat_with_array_data(self):
        meta = PluginExtensionMetadata(name="schools", description="schools")
        plugin_index = {
            "001": {
                "schools": {
                    "metadata": meta,
                    "data": [
                        {"beiss_id": 123, "name": "School A"},
                        {"beiss_id": 456, "name": "School B"},
                    ],
                },
            }
        }
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = enrich_flat(flat_data, plugin_index)
        assert len(result[0]["extensions"]) == 1
        assert isinstance(result[0]["extensions"][0]["data"], list)
        assert result[0]["extensions"][0]["data"][0]["name"] == "School A"

    def test_enrich_extended_with_array_data(self):
        meta = PluginExtensionMetadata(name="schools", description="schools")
        plugin_index = {
            "001": {
                "schools": {
                    "metadata": meta,
                    "data": [{"beiss_id": 123, "name": "School A"}],
                },
            }
        }
        node = {"psgc_id": "001", "name": "Test", "type": "barangay", "components": []}
        result = enrich_extended(node, plugin_index)
        assert len(result["extensions"]) == 1
        assert isinstance(result["extensions"][0]["data"], list)

    def test_load_json_plugin_with_array_data(self, tmp_path):
        json_content = json.dumps(
            [
                {"psgc_id": "001", "data": [{"beiss_id": 123, "name": "School A"}]},
                {"psgc_id": "002", "data": [{"beiss_id": 456, "name": "School B"}]},
            ]
        )
        manifest = _make_manifest("schools", fmt="json")
        _create_plugin(tmp_path, "schools", manifest, {"schools.json": json_content})
        data = load_plugin_data(manifest, plugin_dirs=[tmp_path])
        assert isinstance(data["001"]["data"], list)
        assert data["001"]["data"][0]["beiss_id"] == 123
        assert "psgc_id" not in data["001"]


class TestRemoteFetchDates:
    @patch("barangay.plugin_loader.urlopen")
    def test_parses_github_api_response(self, mock_urlopen):
        api_response = [
            {"name": "2024-04-13", "type": "dir"},
            {"name": "README.md", "type": "file"},
            {"name": "2024-07-13", "type": "dir"},
            {"name": "not-a-date", "type": "dir"},
        ]
        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps(api_response).encode()
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_resp

        dates = _fetch_remote_dates(
            "https://github.com/user/repo", cache_dir=tmp_path_factory()
        )
        assert dates == ["2024-04-13", "2024-07-13"]

    @patch("barangay.plugin_loader.urlopen")
    def test_returns_empty_on_failure(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("network error")
        dates = _fetch_remote_dates(
            "https://github.com/user/repo", cache_dir=tmp_path_factory()
        )
        assert dates == []

    @patch("barangay.plugin_loader.urlopen")
    def test_caches_dates_response(self, mock_urlopen, tmp_path):
        api_response = [{"name": "2024-01-01", "type": "dir"}]
        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps(api_response).encode()
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_resp

        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        dates1 = _fetch_remote_dates(
            "https://github.com/user/repo", cache_dir=cache_dir
        )
        assert dates1 == ["2024-01-01"]
        assert len(mock_urlopen.call_args_list) == 1

        dates2 = _fetch_remote_dates(
            "https://github.com/user/repo", cache_dir=cache_dir
        )
        assert dates2 == ["2024-01-01"]
        assert len(mock_urlopen.call_args_list) == 1


class TestRemoteFetchDataFile:
    @patch("barangay.plugin_loader.urlopen")
    def test_downloads_and_caches(self, mock_urlopen, tmp_path):
        content = b'{"psgc_id": "001", "value": 42}'
        mock_resp = MagicMock()
        mock_resp.read.return_value = content
        mock_resp.__enter__ = MagicMock(return_value=mock_resp)
        mock_resp.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_resp

        url = "https://raw.githubusercontent.com/user/repo/main/data.json"
        result = _fetch_remote_data_file(url, "demo", cache_dir=tmp_path)
        assert result.name == "demo_data.json"
        assert result.read_bytes() == content

    @patch("barangay.plugin_loader.urlopen")
    def test_returns_cached_file(self, mock_urlopen, tmp_path):
        cache_file = tmp_path / "demo_data.json"
        cache_file.write_bytes(b'{"cached": true}')

        url = "https://raw.githubusercontent.com/user/repo/main/data.json"
        result = _fetch_remote_data_file(url, "demo", cache_dir=tmp_path)
        assert result == cache_file
        mock_urlopen.assert_not_called()

    @patch("barangay.plugin_loader.urlopen")
    def test_raises_on_download_failure(self, mock_urlopen, tmp_path):
        mock_urlopen.side_effect = Exception("connection refused")
        url = "https://raw.githubusercontent.com/user/repo/main/data.json"
        from barangay.plugin_loader import PluginDataError

        with pytest.raises(PluginDataError, match="Failed to fetch"):
            _fetch_remote_data_file(url, "demo", cache_dir=tmp_path)


class TestRemotePluginLoading:
    @patch("barangay.plugin_loader._fetch_remote_data_file")
    def test_load_plugin_data_with_repository(self, mock_fetch, tmp_path):
        json_content = json.dumps(
            [
                {"psgc_id": "001", "schools": [{"name": "School A"}]},
            ]
        )
        cache_file = tmp_path / "demo_data.json"
        cache_file.write_text(json_content)
        mock_fetch.return_value = cache_file

        manifest = _make_manifest(
            "demo", fmt="json", repository="https://github.com/user/repo"
        )
        _create_plugin(tmp_path, "demo", manifest, {})

        data = load_plugin_data(
            manifest, resolved_date="2024-07-13", plugin_dirs=[tmp_path]
        )
        assert "001" in data
        assert data["001"]["schools"][0]["name"] == "School A"

    def test_load_plugin_data_local_wins_over_remote(self, tmp_path):
        local_json = json.dumps(
            [
                {"psgc_id": "001", "value": "local"},
            ]
        )
        manifest = _make_manifest(
            "demo", fmt="json", repository="https://github.com/user/repo"
        )
        _create_plugin(tmp_path, "demo", manifest, {"demo.json": local_json})

        data = load_plugin_data(manifest, plugin_dirs=[tmp_path])
        assert data["001"]["value"] == "local"


class TestRemoteBuildIndex:
    @patch("barangay.plugin_loader._fetch_remote_dates")
    @patch("barangay.plugin_loader._fetch_remote_data_file")
    def test_remote_plugin_auto_discovers_dates(
        self, mock_fetch_data, mock_fetch_dates, tmp_path
    ):
        mock_fetch_dates.return_value = ["2024-04-13", "2024-07-13"]
        json_content = json.dumps(
            [
                {"psgc_id": "001", "value": 42},
            ]
        )
        cache_file = tmp_path / "remote_data.json"
        cache_file.write_text(json_content)
        mock_fetch_data.return_value = cache_file

        manifest = _make_manifest(
            "remote",
            fmt="json",
            repository="https://github.com/user/repo",
            current="2024-07-13",
        )
        _create_plugin(tmp_path, "remote", manifest, {})
        (tmp_path / "plugins.yaml").write_text(
            yaml.dump({"plugins": [{"name": "remote", "enabled": True}]})
        )
        config = load_plugin_config(plugin_dirs=[tmp_path])
        index = build_plugin_index(plugin_config=config, plugin_dirs=[tmp_path])
        assert "001" in index
        assert "remote" in index["001"]


def tmp_path_factory():
    from tempfile import mkdtemp

    return Path(mkdtemp())
