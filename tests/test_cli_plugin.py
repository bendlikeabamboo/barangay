import json
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from barangay.cli import app


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def mock_flat_data():
    return [
        {
            "name": "Barangay 1",
            "type": "barangay",
            "psgc_id": "000000001",
            "parent_psgc_id": "000000010",
            "nicknames": None,
        },
        {
            "name": "Barangay 2",
            "type": "barangay",
            "psgc_id": "000000002",
            "parent_psgc_id": "000000020",
            "nicknames": None,
        },
    ]


@pytest.fixture
def mock_search_results():
    return [
        {
            "psgc_id": "000000001",
            "province": "",
            "highly_urbanized_city": "",
            "independent_component_city": "",
            "component_city": "",
            "municipality": "Municipality A",
            "submunicipality": "",
            "special_geographic_area": "",
            "barangay": "Barangay 1",
            "max_score": 92.1,
        },
    ]


class TestExportWithPlugin:
    @patch("barangay.cli.PluginLoader")
    @patch("barangay.cli.DataManager")
    def test_export_flat_with_scalar_plugin_json(
        self, mock_dm, mock_loader_cls, runner, mock_flat_data
    ):
        mock_dm.return_value.get_data.return_value = mock_flat_data
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "pop": {"metadata": {"name": "pop"}, "data": {"population": 1000}},
            },
        }
        mock_loader_cls.return_value = mock_loader

        result = runner.invoke(
            app, ["export", "--model", "flat", "--plugin", "pop", "--format", "json"]
        )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, list)
        assert parsed[0]["pop.population"] == 1000
        assert "000000001" in result.output

    @patch("barangay.cli.PluginLoader")
    @patch("barangay.cli.DataManager")
    def test_export_flat_with_scalar_plugin_csv(
        self, mock_dm, mock_loader_cls, runner, mock_flat_data
    ):
        mock_dm.return_value.get_data.return_value = mock_flat_data
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "pop": {"metadata": {"name": "pop"}, "data": {"population": 1000}},
            },
        }
        mock_loader_cls.return_value = mock_loader

        result = runner.invoke(
            app, ["export", "--model", "flat", "--plugin", "pop", "--format", "csv"]
        )
        assert result.exit_code == 0
        assert "pop.population" in result.output

    @patch("barangay.cli.PluginLoader")
    @patch("barangay.cli.DataManager")
    def test_export_flat_with_array_plugin_explodes(
        self, mock_dm, mock_loader_cls, runner, mock_flat_data
    ):
        mock_dm.return_value.get_data.return_value = mock_flat_data
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "schools": {
                    "metadata": {"name": "schools"},
                    "data": [
                        {"beiss_id": 1, "name": "School A"},
                        {"beiss_id": 2, "name": "School B"},
                    ],
                },
            },
        }
        mock_loader_cls.return_value = mock_loader

        result = runner.invoke(
            app,
            ["export", "--model", "flat", "--plugin", "schools", "--format", "json"],
        )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        school_rows = [r for r in parsed if "schools.name" in r]
        assert len(school_rows) == 2

    @patch("barangay.cli.PluginLoader")
    @patch("barangay.cli.DataManager")
    def test_export_flat_with_two_array_plugins_raises(
        self, mock_dm, mock_loader_cls, runner, mock_flat_data
    ):
        mock_dm.return_value.get_data.return_value = mock_flat_data
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "schools": {
                    "metadata": {"name": "schools"},
                    "data": [{"name": "A"}],
                },
                "hospitals": {
                    "metadata": {"name": "hospitals"},
                    "data": [{"name": "H"}],
                },
            },
        }
        mock_loader_cls.return_value = mock_loader

        result = runner.invoke(
            app,
            [
                "export",
                "--model",
                "flat",
                "--plugin",
                "schools",
                "--plugin",
                "hospitals",
                "--format",
                "json",
            ],
        )
        assert result.exit_code != 0
        assert "Cannot enable more than one" in result.output

    @patch("barangay.cli.DataManager")
    def test_export_without_plugins_unchanged(self, mock_dm, runner, mock_flat_data):
        mock_dm.return_value.get_data.return_value = mock_flat_data

        result = runner.invoke(app, ["export", "--model", "flat", "--format", "json"])
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert len(parsed) == 2
        assert "pop.population" not in str(parsed)

    @patch("barangay.cli.PluginLoader")
    @patch("barangay.cli.DataManager")
    def test_export_with_plugin_writes_to_file(
        self, mock_dm, mock_loader_cls, runner, mock_flat_data, tmp_path
    ):
        output_file = tmp_path / "output.json"
        mock_dm.return_value.get_data.return_value = mock_flat_data
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "pop": {"metadata": {"name": "pop"}, "data": {"population": 1000}},
            },
        }
        mock_loader_cls.return_value = mock_loader

        result = runner.invoke(
            app,
            [
                "export",
                "--model",
                "flat",
                "--plugin",
                "pop",
                "--format",
                "json",
                "--output",
                str(output_file),
            ],
        )
        assert result.exit_code == 0
        assert output_file.exists()
        with open(output_file) as f:
            parsed = json.load(f)
        assert parsed[0]["pop.population"] == 1000

    @patch("barangay.cli.DataManager")
    def test_export_basic_model_with_plugin_raises(self, mock_dm, runner):
        mock_dm.return_value.get_data.return_value = {"Region A": {"Mun A": ["B1"]}}

        result = runner.invoke(
            app,
            ["export", "--model", "basic", "--plugin", "pop", "--format", "json"],
        )
        assert result.exit_code != 0
        assert "only supported with --model flat" in result.output


class TestSearchWithPlugin:
    @patch("barangay.cli.PluginLoader")
    def test_search_with_scalar_plugin_json(
        self, mock_loader_cls, runner, mock_search_results
    ):
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "pop": {"metadata": {"name": "pop"}, "data": {"population": 1000}},
            },
        }
        mock_loader_cls.return_value = mock_loader

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app,
                ["search", "test", "--plugin", "pop", "--format", "json"],
            )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, list)
        assert parsed[0]["pop.population"] == 1000

    @patch("barangay.cli.PluginLoader")
    def test_search_with_scalar_plugin_table(
        self, mock_loader_cls, runner, mock_search_results
    ):
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "pop": {"metadata": {"name": "pop"}, "data": {"population": 1000}},
            },
        }
        mock_loader_cls.return_value = mock_loader

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app,
                ["search", "test", "--plugin", "pop", "--format", "table"],
            )
        assert result.exit_code == 0
        assert "pop.populati" in result.output

    @patch("barangay.cli.PluginLoader")
    def test_search_without_plugin_unchanged(
        self, mock_loader_cls, runner, mock_search_results
    ):
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["search", "test"])
        assert result.exit_code == 0
        assert "pop.population" not in result.output

    @patch("barangay.cli.PluginLoader")
    def test_search_with_plugin_no_matching_data(
        self, mock_loader_cls, runner, mock_search_results
    ):
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {}
        mock_loader_cls.return_value = mock_loader

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app,
                ["search", "test", "--plugin", "pop", "--format", "json"],
            )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert "pop.population" not in parsed[0]

    @patch("barangay.cli.PluginLoader")
    def test_search_with_multiple_plugins(
        self, mock_loader_cls, runner, mock_search_results
    ):
        mock_loader = MagicMock()
        mock_loader.build_index.return_value = {
            "000000001": {
                "pop": {"metadata": {"name": "pop"}, "data": {"population": 1000}},
                "elev": {"metadata": {"name": "elev"}, "data": {"elevation": 50}},
            },
        }
        mock_loader_cls.return_value = mock_loader

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app,
                [
                    "search",
                    "test",
                    "--plugin",
                    "pop",
                    "--plugin",
                    "elev",
                    "--format",
                    "json",
                ],
            )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert parsed[0]["pop.population"] == 1000
        assert parsed[0]["elev.elevation"] == 50
