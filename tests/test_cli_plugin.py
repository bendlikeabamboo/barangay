"""Tests for plugin enrichment in the CLI (flat export + search).

These exercise the CLI plumbing: that ``--plugin`` triggers
``Database.use_plugins()`` before export, and that plugin fields on typed
``SearchResult`` objects are flattened as ``plugin.field``. The actual
explosion logic lives in the package (``DatabaseView.to_dicts`` /
``explode_flat``) and is mocked here.
"""

import json
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from barangay.cli import app
from barangay.database import HierarchyIndex
from barangay.models import (
    AdminDivRecord,
    AdminLevel,
    PluginExtension,
    PluginExtensionMetadata,
    SearchResult,
)


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
            "pop.population": 1000,
        },
        {
            "name": "Barangay 2",
            "type": "barangay",
            "psgc_id": "000000002",
            "parent_psgc_id": "000000020",
            "nicknames": None,
        },
    ]


def _make_db(to_dicts_data):
    db = MagicMock()
    db.all_records.to_dicts.return_value = to_dicts_data
    db._version_state = MagicMock()
    db.use_plugins = MagicMock()
    db.invalidate_cache = MagicMock()
    return db


def _make_search_result(extensions):
    rec = AdminDivRecord(
        name="Barangay One",
        type=AdminLevel.BARANGAY,
        psgc_id="000000001",
        parent_psgc_id="000000010",
        extensions=extensions,
    )
    index = HierarchyIndex([rec])
    sr = SearchResult(record=rec, score=92.1, match_type="barangay")
    sr._index = index
    return sr


class TestExportWithPlugin:
    @patch("barangay.cli.Database")
    def test_export_flat_with_scalar_plugin_json(
        self, mock_db_cls, runner, mock_flat_data
    ):
        mock_db_cls.return_value = _make_db(mock_flat_data)

        result = runner.invoke(
            app, ["export", "--model", "flat", "--plugin", "pop", "--format", "json"]
        )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, list)
        assert parsed[0]["pop.population"] == 1000
        mock_db_cls.return_value.use_plugins.assert_called_with(["pop"])

    @patch("barangay.cli.Database")
    def test_export_flat_with_scalar_plugin_csv(
        self, mock_db_cls, runner, mock_flat_data
    ):
        mock_db_cls.return_value = _make_db(mock_flat_data)

        result = runner.invoke(
            app, ["export", "--model", "flat", "--plugin", "pop", "--format", "csv"]
        )
        assert result.exit_code == 0
        assert "pop.population" in result.output

    @patch("barangay.cli.Database")
    def test_export_flat_with_array_plugin_explodes(self, mock_db_cls, runner):
        exploded = [
            {
                "name": "Barangay 1",
                "type": "barangay",
                "psgc_id": "000000001",
                "parent_psgc_id": "000000010",
                "schools.name": "School A",
            },
            {
                "name": "Barangay 1",
                "type": "barangay",
                "psgc_id": "000000001",
                "parent_psgc_id": "000000010",
                "schools.name": "School B",
            },
        ]
        mock_db_cls.return_value = _make_db(exploded)

        result = runner.invoke(
            app,
            ["export", "--model", "flat", "--plugin", "schools", "--format", "json"],
        )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        school_rows = [r for r in parsed if "schools.name" in r]
        assert len(school_rows) == 2

    @patch("barangay.cli.Database")
    def test_export_flat_with_two_array_plugins_raises(self, mock_db_cls, runner):
        from barangay.explode import ExplodeError

        db = _make_db([])
        db.all_records.to_dicts.side_effect = ExplodeError(
            "Cannot enable more than one array-type plugin (found: hospitals, schools)"
        )
        mock_db_cls.return_value = db

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

    @patch("barangay.cli.Database")
    def test_export_without_plugins_unchanged(
        self, mock_db_cls, runner, mock_flat_data
    ):
        mock_db_cls.return_value = _make_db(mock_flat_data)

        result = runner.invoke(app, ["export", "--model", "flat", "--format", "json"])
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert len(parsed) == 2
        mock_db_cls.return_value.use_plugins.assert_not_called()

    @patch("barangay.cli.Database")
    def test_export_with_plugin_writes_to_file(
        self, mock_db_cls, runner, mock_flat_data, tmp_path
    ):
        output_file = tmp_path / "output.json"
        mock_db_cls.return_value = _make_db(mock_flat_data)

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

    def test_export_extended_with_plugin_raises(self, runner):
        result = runner.invoke(
            app,
            ["export", "--model", "extended", "--plugin", "pop", "--format", "json"],
        )
        assert result.exit_code != 0
        assert "only supported with --model flat" in result.output

    def test_export_basic_model_rejected(self, runner):
        result = runner.invoke(
            app,
            ["export", "--model", "basic", "--plugin", "pop", "--format", "json"],
        )
        assert result.exit_code != 0
        assert "basic" in result.output


class TestSearchWithPlugin:
    @patch("barangay.cli.Database")
    @patch("barangay.cli.search_fuzzy")
    def test_search_with_scalar_plugin_json(self, mock_search, mock_db_cls, runner):
        ext = [
            PluginExtension(
                field_group="pop",
                metadata=PluginExtensionMetadata(name="pop"),
                data={"population": 1000},
            )
        ]
        mock_search.return_value = [_make_search_result(ext)]
        mock_db_cls.return_value.use_plugins = MagicMock()

        result = runner.invoke(
            app, ["search", "test", "--plugin", "pop", "--format", "json"]
        )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, list)
        assert parsed[0]["pop.population"] == 1000
        assert parsed[0]["rphicmsgb"] == "00000000b"
        mock_db_cls.return_value.use_plugins.assert_called_with(["pop"])

    @patch("barangay.cli.Database")
    @patch("barangay.cli.search_fuzzy")
    def test_search_with_scalar_plugin_table(self, mock_search, mock_db_cls, runner):
        ext = [
            PluginExtension(
                field_group="pop",
                metadata=PluginExtensionMetadata(name="pop"),
                data={"population": 1000},
            )
        ]
        mock_search.return_value = [_make_search_result(ext)]
        mock_db_cls.return_value.use_plugins = MagicMock()

        result = runner.invoke(
            app,
            ["search", "test", "--plugin", "pop", "--format", "table"],
            env={"COLUMNS": "300"},
        )
        assert result.exit_code == 0
        assert "pop.population" in result.output

    @patch("barangay.cli.search_fuzzy")
    def test_search_without_plugin_unchanged(self, mock_search, runner):
        mock_search.return_value = [_make_search_result([])]

        result = runner.invoke(app, ["search", "test"])
        assert result.exit_code == 0
        assert "pop.population" not in result.output

    @patch("barangay.cli.Database")
    @patch("barangay.cli.search_fuzzy")
    def test_search_with_multiple_plugins(self, mock_search, mock_db_cls, runner):
        ext = [
            PluginExtension(
                field_group="pop",
                metadata=PluginExtensionMetadata(name="pop"),
                data={"population": 1000},
            ),
            PluginExtension(
                field_group="elev",
                metadata=PluginExtensionMetadata(name="elev"),
                data={"elevation": 50},
            ),
        ]
        mock_search.return_value = [_make_search_result(ext)]
        mock_db_cls.return_value.use_plugins = MagicMock()

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
