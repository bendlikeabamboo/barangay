"""Comprehensive pytest tests for the CLI.

Tests cover all CLI commands and verify the hierarchy-loyal behaviour:
9-column tables, the ``rphicmsgb`` indicator, ``EnrichedRecord.to_dict()``
JSON output, the generic ``info list``, ``search_fuzzy``/``validate``
migration, and the ``flat``/``extended`` export models.
"""

import json
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from barangay.cli import (
    _build_hierarchy_table,
    _dict_to_csv,
    app,
    rphicmsgb,
    to_result_dict,
)
from barangay.database import EnrichedRecord, HierarchyIndex
from barangay.models import AdminDivRecord, AdminLevel, SearchResult


# ----------------------------------------------------------------------------
# Test hierarchy fixtures
# ----------------------------------------------------------------------------


def _build_index():
    records = [
        AdminDivRecord(
            name="Region X",
            type=AdminLevel.REGION,
            psgc_id="1000000000",
            parent_psgc_id="n/a",
        ),
        AdminDivRecord(
            name="Province X",
            type=AdminLevel.PROVINCE,
            psgc_id="1000000001",
            parent_psgc_id="1000000000",
        ),
        AdminDivRecord(
            name="Municipality X",
            type=AdminLevel.MUNICIPALITY,
            psgc_id="1000000010",
            parent_psgc_id="1000000001",
        ),
        AdminDivRecord(
            name="Barangay One",
            type=AdminLevel.BARANGAY,
            psgc_id="1000000017",
            parent_psgc_id="1000000010",
        ),
        AdminDivRecord(
            name="Barangay Two",
            type=AdminLevel.BARANGAY,
            psgc_id="1000000018",
            parent_psgc_id="1000000010",
        ),
    ]
    return HierarchyIndex(records), records


class _FakeView:
    """Minimal stand-in for DatabaseView over a list of EnrichedRecord."""

    def __init__(self, enriched: list[EnrichedRecord]):
        self._enriched = enriched

    def __iter__(self):
        return iter(self._enriched)

    def __len__(self):
        return len(self._enriched)

    def __contains__(self, psgc_id):
        return any(e.psgc_id == psgc_id for e in self._enriched)

    def lookup(self, psgc_id):
        for e in self._enriched:
            if e.psgc_id == psgc_id:
                return e
        return None


@pytest.fixture
def runner():
    """Create a CliRunner instance for testing CLI commands."""
    return CliRunner()


@pytest.fixture
def index():
    """A small HierarchyIndex."""
    idx, _ = _build_index()
    return idx


@pytest.fixture
def enriched_barangay(index):
    """An EnrichedRecord for Barangay One."""
    return EnrichedRecord(index.get("1000000017"), index)


@pytest.fixture
def search_results(index):
    """A list of SearchResult objects backed by the test index."""
    rec = index.get("1000000017")
    sr = SearchResult(record=rec, score=92.1, match_type="barangay")
    sr._index = index
    return [sr]


@pytest.fixture
def mock_flat_dicts():
    """Flat export data as list of dicts."""
    return [
        {
            "name": "Barangay 1",
            "type": "barangay",
            "psgc_id": "000000001",
            "parent_psgc_id": "000000010",
            "nicknames": ["BRGY1"],
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
def mock_db(mock_flat_dicts):
    """A mocked Database whose all_records.to_dicts() returns flat data."""
    db = MagicMock()
    db.all_records.to_dicts.return_value = mock_flat_dicts
    db._version_state = MagicMock()
    db.use_plugins = MagicMock()
    db.invalidate_cache = MagicMock()
    return db


# ============================================================================
# SHARED HELPERS TESTS
# ============================================================================


class TestSharedHelpers:
    """Tests for rphicmsgb / to_result_dict / table factory."""

    def test_rphicmsgb_resolved_levels(self, enriched_barangay):
        indicator = rphicmsgb(enriched_barangay)
        assert indicator == "rp000m00b"

    def test_rphicmsgb_length(self, enriched_barangay):
        assert len(rphicmsgb(enriched_barangay)) == 9

    def test_to_result_dict_shape(self, search_results):
        d = to_result_dict(search_results[0])
        assert d["rphicmsgb"] == "rp000m00b"
        assert d["score"] == 92.1
        assert d["match_type"] == "barangay"
        assert d["barangay"] == "Barangay One"
        assert d["region"] == "Region X"
        assert d["municipality"] == "Municipality X"
        assert d["province"] == "Province X"
        assert "extensions" not in d

    def test_build_hierarchy_table_columns(self):
        table = _build_hierarchy_table("Title", plugin_columns=["pop.x"])
        assert len(table.columns) == 9 + 3 + 1  # levels + rphicmsgb/PSGC/Score + plugin

    def test_build_hierarchy_table_omits_blank_levels(self):
        table = _build_hierarchy_table("Title", active_levels=["region", "barangay"])
        assert len(table.columns) == 2 + 3  # 2 levels + rphicmsgb/PSGC/Score


# ============================================================================
# SEARCH COMMANDS TESTS
# ============================================================================


class TestSearchCommands:
    """Test suite for search commands."""

    def test_search_cmd_basic(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["search", "test query"])
            assert result.exit_code == 0
            assert "Search Results for 'test query'" in result.output

    def test_search_cmd_json_format(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["search", "test query", "--format", "json"])
            assert result.exit_code == 0
            parsed = json.loads(result.output)
            assert isinstance(parsed, list)
            assert parsed[0]["rphicmsgb"] == "rp000m00b"

    def test_search_cmd_table_has_rphicmsgb(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(
                app,
                ["search", "test query", "--format", "table"],
                env={"COLUMNS": "300"},
            )
            assert result.exit_code == 0
            assert "rphicmsgb" in result.output
            assert "rp000m00b" in result.output
            assert "Score" in result.output

    def test_search_cmd_with_limit(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["search", "test query", "--limit", "1"])
            assert result.exit_code == 0

    def test_search_cmd_with_threshold(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["search", "test query", "--threshold", "80.0"])
            assert result.exit_code == 0

    def test_search_cmd_with_as_of(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(
                app, ["search", "test query", "--as-of", "2025-01-01"]
            )
            assert result.exit_code == 0

    def test_search_cmd_empty_results(self, runner):
        with patch("barangay.cli.search_fuzzy", return_value=[]):
            result = runner.invoke(app, ["search", "nonexistent"])
            assert result.exit_code == 0
            assert "No results found" in result.output

    def test_search_cmd_error_handling(self, runner):
        with patch("barangay.cli.search_fuzzy", side_effect=Exception("Search failed")):
            result = runner.invoke(app, ["search", "test query"])
            assert result.exit_code != 0

    def test_search_history_basic(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(
                app,
                ["history", "search-history", "test query", "--as-of", "2025-01-01"],
            )
            assert result.exit_code == 0
            assert "Search Results for 'test query' (as of 2025-01-01)" in result.output

    def test_search_history_json_format(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(
                app,
                [
                    "history",
                    "search-history",
                    "test query",
                    "--as-of",
                    "2025-01-01",
                    "--format",
                    "json",
                ],
            )
            assert result.exit_code == 0
            parsed = json.loads(result.output)
            assert parsed[0]["rphicmsgb"] == "rp000m00b"

    def test_search_history_with_limit(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(
                app,
                [
                    "history",
                    "search-history",
                    "test query",
                    "--as-of",
                    "2025-01-01",
                    "--limit",
                    "3",
                ],
            )
            assert result.exit_code == 0

    def test_search_history_missing_as_of(self, runner):
        result = runner.invoke(app, ["history", "search-history", "test query"])
        assert result.exit_code != 0

    def test_search_cmd_level_filter(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results) as mock_sf:
            result = runner.invoke(app, ["search", "test", "--level", "barangay"])
            assert result.exit_code == 0
            _, kwargs = mock_sf.call_args
            assert kwargs["level"] == AdminLevel.BARANGAY

    def test_search_cmd_match_hooks(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results) as mock_sf:
            result = runner.invoke(
                app,
                [
                    "search",
                    "test",
                    "--match-hook",
                    "province",
                    "--match-hook",
                    "barangay",
                ],
            )
            assert result.exit_code == 0
            _, kwargs = mock_sf.call_args
            assert kwargs["match_hooks"] == ["province", "barangay"]

    def test_search_cmd_match_hooks_default_none(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results) as mock_sf:
            result = runner.invoke(app, ["search", "test"])
            assert result.exit_code == 0
            _, kwargs = mock_sf.call_args
            assert kwargs["match_hooks"] is None
            assert kwargs["level"] is None


# ============================================================================
# INFO COMMANDS TESTS
# ============================================================================


class TestInfoCommands:
    """Test suite for info commands."""

    @patch("barangay.cli.current", "2026-04-13")
    @patch("barangay.cli.available_dates", ["2025-07-08", "2026-01-13"])
    def test_version(self, runner):
        result = runner.invoke(app, ["info", "version"])
        assert result.exit_code == 0
        assert "Current version:" in result.output
        assert "Available dates:" in result.output

    def test_stats(self, runner, mock_db):
        mock_db.regions.__len__.return_value = 17
        mock_db.provinces.__len__.return_value = 82
        mock_db.hucs.__len__.return_value = 33
        mock_db.iccs.__len__.return_value = 5
        mock_db.component_cities.__len__.return_value = 120
        mock_db.municipalities.__len__.return_value = 1493
        mock_db.submunicipalities.__len__.return_value = 12
        mock_db.special_geographic_areas.__len__.return_value = 1
        mock_db.barangays.__len__.return_value = 42011
        mock_db.all_records.__len__.return_value = 42011
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(app, ["info", "stats"])
        assert result.exit_code == 0
        assert "PSGC Record Statistics" in result.output
        assert "Total" in result.output
        assert "Barangay" in result.output

    def test_list_level(self, runner, index):
        view = _FakeView(
            [
                EnrichedRecord(index.get("1000000017"), index),
                EnrichedRecord(index.get("1000000018"), index),
            ]
        )
        mock_db = MagicMock()
        mock_db._view.return_value = view
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(app, ["info", "list", "barangay"])
        assert result.exit_code == 0
        assert "Barangay One" in result.output
        assert "Barangay Two" in result.output
        assert "PSGC ID" in result.output

    def test_list_cities(self, runner, index):
        view = _FakeView([EnrichedRecord(index.get("1000000017"), index)])
        mock_db = MagicMock()
        mock_db.cities = view
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(app, ["info", "list", "cities"])
        assert result.exit_code == 0
        assert "Cities" in result.output

    def test_list_with_parent(self, runner, index):
        all_enriched = [EnrichedRecord(r, index) for r in index._by_id.values()]
        brgy_view = _FakeView(
            [
                EnrichedRecord(index.get("1000000017"), index),
                EnrichedRecord(index.get("1000000018"), index),
            ]
        )
        mock_db = MagicMock()
        mock_db._view.return_value = brgy_view
        mock_db.all_records = _FakeView(all_enriched)
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app, ["info", "list", "barangay", "--parent", "Municipality X"]
            )
        assert result.exit_code == 0
        assert "under 'Municipality X'" in result.output

    def test_list_parent_not_found(self, runner, index):
        all_enriched = [EnrichedRecord(r, index) for r in index._by_id.values()]
        brgy_view = _FakeView([EnrichedRecord(index.get("1000000017"), index)])
        mock_db = MagicMock()
        mock_db._view.return_value = brgy_view
        mock_db.all_records = _FakeView(all_enriched)
        with (
            patch("barangay.cli.Database", return_value=mock_db),
            patch("barangay.cli.search_fuzzy", return_value=[]),
        ):
            result = runner.invoke(
                app, ["info", "list", "barangay", "--parent", "Nope"]
            )
        assert result.exit_code != 0
        assert "not found" in result.output


# ============================================================================
# EXPORT COMMANDS TESTS
# ============================================================================


class TestExportCommands:
    """Test suite for export commands."""

    def test_export_flat_json(self, runner, mock_db):
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app, ["export", "--model", "flat", "--format", "json"]
            )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, list)

    def test_export_flat_csv(self, runner, mock_db):
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app, ["export", "--model", "flat", "--format", "csv"]
            )
        assert result.exit_code == 0
        assert "name" in result.output

    def test_export_rejects_basic(self, runner):
        result = runner.invoke(app, ["export", "--model", "basic", "--format", "json"])
        assert result.exit_code != 0
        assert "basic" in result.output

    def test_export_extended_csv_rejected(self, runner, mock_db):
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app, ["export", "--model", "extended", "--format", "csv"]
            )
        assert result.exit_code != 0
        assert "CSV export is only supported" in result.output

    def test_export_extended_json(self, runner, mock_db):
        extended = {"name": "Country", "type": "country", "components": []}
        mock_dm = MagicMock()
        mock_dm.get_data.return_value = extended
        with (
            patch("barangay.cli.Database", return_value=mock_db),
            patch("barangay.cli.DataManager", return_value=mock_dm),
        ):
            result = runner.invoke(
                app, ["export", "--model", "extended", "--format", "json"]
            )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert parsed["type"] == "country"

    def test_export_with_as_of_sets_version(self, runner, mock_db):
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app, ["export", "--model", "flat", "--as-of", "2025-01-01"]
            )
        assert result.exit_code == 0
        mock_db._version_state.set.assert_called_with("2025-01-01")

    def test_export_to_file(self, runner, mock_db, tmp_path):
        output_file = tmp_path / "output.json"
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app, ["export", "--model", "flat", "--output", str(output_file)]
            )
        assert result.exit_code == 0
        assert output_file.exists()
        with open(output_file) as f:
            parsed = json.load(f)
            assert isinstance(parsed, list)

    def test_export_history_flat(self, runner, mock_db):
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app,
                [
                    "history",
                    "export-history",
                    "--as-of",
                    "2025-01-01",
                    "--model",
                    "flat",
                ],
            )
        assert result.exit_code == 0
        mock_db._version_state.set.assert_called_with("2025-01-01")

    def test_export_history_rejects_basic(self, runner):
        result = runner.invoke(
            app,
            ["history", "export-history", "--as-of", "2025-01-01", "--model", "basic"],
        )
        assert result.exit_code != 0

    def test_export_history_to_file(self, runner, mock_db, tmp_path):
        output_file = tmp_path / "output.json"
        with patch("barangay.cli.Database", return_value=mock_db):
            result = runner.invoke(
                app,
                [
                    "history",
                    "export-history",
                    "--as-of",
                    "2025-01-01",
                    "--model",
                    "flat",
                    "--output",
                    str(output_file),
                ],
            )
        assert result.exit_code == 0
        assert output_file.exists()


# ============================================================================
# HISTORY COMMANDS TESTS
# ============================================================================


class TestHistoryCommands:
    """Test suite for history commands."""

    @patch("barangay.cli.get_available_dates")
    @patch("barangay.cli.current", "2026-04-13")
    def test_list_dates(self, mock_dates, runner):
        mock_dates.return_value = ["2025-07-08", "2026-01-13"]
        result = runner.invoke(app, ["history", "list-dates"])
        assert result.exit_code == 0
        assert "Available Historical Dates" in result.output
        assert "2025-07-08" in result.output
        assert "Current" in result.output


# ============================================================================
# CACHE COMMANDS TESTS
# ============================================================================


class TestCacheCommands:
    """Test suite for cache commands."""

    @patch("barangay.cli.get_cache_dir")
    def test_cache_info_empty(self, mock_cache_dir, runner, tmp_path):
        empty_cache = tmp_path / "empty_cache"
        mock_cache_dir.return_value = empty_cache

        result = runner.invoke(app, ["cache", "info"])
        assert result.exit_code == 0
        assert "Cache Information" in result.output

    @patch("barangay.cli.get_cache_dir")
    def test_cache_info_with_files(self, mock_cache_dir, runner, tmp_path):
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        (cache_dir / "file1.json").write_text("{}")
        (cache_dir / "file2.json").write_text('{"test": "data"}')
        mock_cache_dir.return_value = cache_dir

        result = runner.invoke(app, ["cache", "info"])
        assert result.exit_code == 0
        assert "2" in result.output

    @patch("barangay.cli.get_cache_dir")
    def test_cache_clear_empty(self, mock_cache_dir, runner, tmp_path):
        empty_cache = tmp_path / "empty_cache"
        mock_cache_dir.return_value = empty_cache

        result = runner.invoke(app, ["cache", "clear"])
        assert result.exit_code == 0
        assert "Cache directory is empty" in result.output

    @patch("barangay.cli.get_cache_dir")
    def test_cache_clear_with_files(self, mock_cache_dir, runner, tmp_path):
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        (cache_dir / "file1.json").write_text("{}")
        mock_cache_dir.return_value = cache_dir

        result = runner.invoke(app, ["cache", "clear"])
        assert result.exit_code == 0
        assert "Cache cleared" in result.output
        assert not cache_dir.exists()

    @patch("barangay.cli.DataManager")
    def test_cache_download_current(self, mock_dm, runner):
        result = runner.invoke(app, ["cache", "download"])
        assert result.exit_code == 0
        assert "Downloading current data" in result.output

    @patch("barangay.cli.DataManager")
    def test_cache_download_with_date(self, mock_dm, runner):
        result = runner.invoke(app, ["cache", "download", "--date", "2025-01-01"])
        assert result.exit_code == 0
        assert "Downloading data for 2025-01-01" in result.output


# ============================================================================
# BATCH COMMANDS TESTS
# ============================================================================


class TestBatchCommands:
    """Test suite for batch commands."""

    def test_batch_search_basic(self, runner, search_results, tmp_path):
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\nquery2\nquery3\n")
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["batch", "batch-search", str(input_file)])
        assert result.exit_code == 0

    def test_batch_search_level_and_hooks(self, runner, search_results, tmp_path):
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\n")
        with patch("barangay.cli.search_fuzzy", return_value=search_results) as mock_sf:
            result = runner.invoke(
                app,
                [
                    "batch",
                    "batch-search",
                    str(input_file),
                    "--level",
                    "province",
                    "--match-hook",
                    "province",
                ],
            )
        assert result.exit_code == 0
        _, kwargs = mock_sf.call_args
        assert kwargs["level"] == AdminLevel.PROVINCE
        assert kwargs["match_hooks"] == ["province"]

    def test_batch_search_json_serializable(self, runner, search_results, tmp_path):
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\n")
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["batch", "batch-search", str(input_file)])
        # batch-search always emits JSON to stdout
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert parsed["query1"][0]["rphicmsgb"] == "rp000m00b"

    def test_batch_search_to_file(self, runner, search_results, tmp_path):
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\nquery2\n")
        output_file = tmp_path / "output.json"
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(
                app,
                [
                    "batch",
                    "batch-search",
                    str(input_file),
                    "--output",
                    str(output_file),
                ],
            )
        assert result.exit_code == 0
        assert output_file.exists()
        with open(output_file) as f:
            parsed = json.load(f)
            assert isinstance(parsed, dict)

    def test_batch_search_empty_lines(self, runner, search_results, tmp_path):
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\n\n\nquery2\n\n")
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["batch", "batch-search", str(input_file)])
        assert result.exit_code == 0

    def test_validate_valid_address(self, runner, index, tmp_path):
        from barangay.models import ValidationResult

        input_file = tmp_path / "addresses.txt"
        input_file.write_text("Barangay One, Municipality X\n")
        rec = index.get("1000000017")
        vr = ValidationResult(
            input="Barangay One", valid=True, matched_record=rec, score=100.0
        )
        with (
            patch("barangay.cli.validate", return_value=vr),
            patch(
                "barangay.cli._resolve_enriched",
                return_value=EnrichedRecord(rec, index),
            ),
        ):
            result = runner.invoke(app, ["batch", "validate", str(input_file)])
        assert result.exit_code == 0
        assert "Validation Results" in result.output
        assert "Valid" in result.output
        assert "rp000m00b" in result.output

    def test_validate_invalid_address(self, runner, tmp_path):
        from barangay.models import ValidationResult

        input_file = tmp_path / "addresses.txt"
        input_file.write_text("Invalid Address\n")
        vr = ValidationResult(input="Invalid Address", valid=False)
        with patch("barangay.cli.validate", return_value=vr):
            result = runner.invoke(app, ["batch", "validate", str(input_file)])
        assert result.exit_code == 0
        assert "Not found" in result.output
        assert "000000000" in result.output

    def test_validate_threshold_forwarded(self, runner, index, tmp_path):
        from barangay.models import ValidationResult

        input_file = tmp_path / "addresses.txt"
        input_file.write_text("Barangay One\n")
        vr = ValidationResult(input="Barangay One", valid=False)
        with patch("barangay.cli.validate", return_value=vr) as mock_v:
            result = runner.invoke(
                app, ["batch", "validate", str(input_file), "--threshold", "70.0"]
            )
        assert result.exit_code == 0
        _, kwargs = mock_v.call_args
        assert kwargs["threshold"] == 70.0

    def test_validate_empty_lines(self, runner, search_results, tmp_path):
        from barangay.models import ValidationResult

        input_file = tmp_path / "addresses.txt"
        input_file.write_text("Barangay One\n\n\nBarangay Two\n")
        vr = ValidationResult(input="x", valid=False)
        with patch("barangay.cli.validate", return_value=vr):
            result = runner.invoke(app, ["batch", "validate", str(input_file)])
        assert result.exit_code == 0


# ============================================================================
# UTILITY FUNCTIONS TESTS
# ============================================================================


class TestUtilityFunctions:
    """Test suite for utility functions."""

    def test_dict_to_csv(self, mock_flat_dicts):
        csv_output = _dict_to_csv(mock_flat_dicts)
        lines = csv_output.strip().split("\n")
        assert len(lines) == 3
        assert "name" in lines[0]
        assert "Barangay 1" in csv_output

    def test_dict_to_csv_empty(self):
        assert _dict_to_csv([]) == ""

    def test_dict_to_csv_collects_all_fields(self):
        data = [{"a": 1, "b": 2}, {"b": 3, "c": 4}]
        csv_output = _dict_to_csv(data)
        header = csv_output.strip().split("\n")[0]
        assert "a" in header
        assert "b" in header
        assert "c" in header


# ============================================================================
# EDGE CASES AND INTEGRATION TESTS
# ============================================================================


class TestEdgeCasesAndIntegration:
    """Test suite for edge cases and integration scenarios."""

    def test_app_help(self, runner):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "Main CLI entry point" in result.output
        assert "search" in result.output

    def test_search_cmd_help(self, runner):
        result = runner.invoke(app, ["search", "--help"])
        assert result.exit_code == 0
        assert "Search PSGC records" in result.output

    def test_info_help_lists_list(self, runner):
        result = runner.invoke(app, ["info", "--help"])
        assert result.exit_code == 0
        assert "list" in result.output

    def test_export_help(self, runner):
        result = runner.invoke(app, ["export", "--help"])
        assert result.exit_code == 0
        assert "Export data to JSON or CSV" in result.output

    def test_search_unicode_characters(self, runner):
        with patch("barangay.cli.search_fuzzy", return_value=[]):
            result = runner.invoke(app, ["search", "Ñoño"])
            assert result.exit_code == 0

    def test_search_special_characters(self, runner, search_results):
        with patch("barangay.cli.search_fuzzy", return_value=search_results):
            result = runner.invoke(app, ["search", "test-query_123"])
            assert result.exit_code == 0

    def test_search_very_long_query(self, runner):
        with patch("barangay.cli.search_fuzzy", return_value=[]):
            result = runner.invoke(app, ["search", "a" * 1000])
            assert result.exit_code == 0
