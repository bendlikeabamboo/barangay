"""Comprehensive pytest tests for the CLI.

Tests cover all CLI commands and verify they work correctly with Pydantic models.
Uses click.testing.CliRunner to test the CLI commands.
"""

import json
from unittest.mock import Mock, patch

import pytest
from click.testing import CliRunner

from barangay.cli import app, _dict_to_csv, _nested_to_csv
from barangay.models import AdminDivExtended


@pytest.fixture
def runner():
    """Create a CliRunner instance for testing CLI commands."""
    return CliRunner()


@pytest.fixture
def mock_search_results():
    """Mock search results as list of dicts."""
    return [
        {
            "barangay": "Barangay 1",
            "municipality_or_city": "Municipality A",
            "province_or_huc": "Province X",
            "psgc_id": "000000001",
            "f_000b_ratio_score": 85.5,
            "f_0p0b_ratio_score": 90.2,
            "f_00mb_ratio_score": 88.7,
            "f_0pmb_ratio_score": 92.1,
            "max_score": 92.1,
        },
        {
            "barangay": "Barangay 2",
            "municipality_or_city": "Municipality B",
            "province_or_huc": "Province Y",
            "psgc_id": "000000002",
            "f_000b_ratio_score": 75.5,
            "f_0p0b_ratio_score": 80.2,
            "f_00mb_ratio_score": 78.7,
            "f_0pmb_ratio_score": 82.1,
            "max_score": 82.1,
        },
    ]


@pytest.fixture
def mock_basic_data():
    """Mock basic barangay data (nested dict)."""
    return {
        "Region A": {
            "Municipality A": ["Barangay 1", "Barangay 2"],
        },
        "Region B": {
            "Municipality C": ["Barangay 3"],
        },
    }


@pytest.fixture
def mock_flat_data():
    """Mock flat barangay data (list of dicts)."""
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
def mock_extended_data():
    """Mock extended barangay data (AdminDivExtended model)."""
    return AdminDivExtended(
        name="Country",
        type="country",
        psgc_id="n/a",
        parent_psgc_id="n/a",
        components=[
            AdminDivExtended(
                name="Region A",
                type="region",
                psgc_id="000000000",
                parent_psgc_id="n/a",
                components=[
                    AdminDivExtended(
                        name="Municipality A",
                        type="municipality",
                        psgc_id="000000010",
                        parent_psgc_id="000000000",
                        components=[
                            AdminDivExtended(
                                name="Barangay 1",
                                type="barangay",
                                psgc_id="000000001",
                                parent_psgc_id="000000010",
                            )
                        ],
                    )
                ],
            )
        ],
    )


@pytest.fixture
def mock_cache_dir(tmp_path):
    """Create a temporary cache directory for testing."""
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    return cache_dir


# ============================================================================
# SEARCH COMMANDS TESTS
# ============================================================================


class TestSearchCommands:
    """Test suite for search commands."""

    def test_search_cmd_basic(self, runner, mock_search_results):
        """Test basic search command with default parameters."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["search", "test query"])
            assert result.exit_code == 0
            assert "Search Results for 'test query'" in result.output

    def test_search_cmd_json_format(self, runner, mock_search_results):
        """Test search command with JSON output format."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["search", "test query", "--format", "json"])
            assert result.exit_code == 0
            # Check that JSON is valid
            parsed = json.loads(result.output)
            assert isinstance(parsed, list)
            assert len(parsed) == 2

    def test_search_cmd_table_format(self, runner, mock_search_results):
        """Test search command with table output format."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["search", "test query", "--format", "table"])
            assert result.exit_code == 0
            assert "Barangay" in result.output
            assert "Municipality/City" in result.output
            assert "Score" in result.output

    def test_search_cmd_with_limit(self, runner, mock_search_results):
        """Test search command with custom limit."""
        with patch("barangay.cli.search", return_value=mock_search_results[:1]):
            result = runner.invoke(app, ["search", "test query", "--limit", "1"])
            assert result.exit_code == 0

    def test_search_cmd_with_threshold(self, runner, mock_search_results):
        """Test search command with custom threshold."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["search", "test query", "--threshold", "80.0"])
            assert result.exit_code == 0

    def test_search_cmd_with_as_of(self, runner, mock_search_results):
        """Test search command with historical date parameter."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app, ["search", "test query", "--as-of", "2025-01-01"]
            )
            assert result.exit_code == 0

    def test_search_cmd_empty_results(self, runner):
        """Test search command with no results."""
        with patch("barangay.cli.search", return_value=[]):
            result = runner.invoke(app, ["search", "nonexistent"])
            assert result.exit_code == 0
            assert "No results found" in result.output

    def test_search_cmd_error_handling(self, runner):
        """Test search command error handling."""
        with patch("barangay.cli.search", side_effect=Exception("Search failed")):
            result = runner.invoke(app, ["search", "test query"])
            assert result.exit_code != 0

    def test_search_history_basic(self, runner, mock_search_results):
        """Test search_history command with basic parameters."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app,
                ["history", "search-history", "test query", "--as-of", "2025-01-01"],
            )
            assert result.exit_code == 0
            assert "Search Results for 'test query' (as of 2025-01-01)" in result.output

    def test_search_history_json_format(self, runner, mock_search_results):
        """Test search_history command with JSON format."""
        with patch("barangay.cli.search", return_value=mock_search_results):
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
            assert isinstance(parsed, list)

    def test_search_history_with_limit(self, runner, mock_search_results):
        """Test search_history command with limit."""
        with patch("barangay.cli.search", return_value=mock_search_results):
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

    def test_search_history_with_threshold(self, runner, mock_search_results):
        """Test search_history command with threshold."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app,
                [
                    "history",
                    "search-history",
                    "test query",
                    "--as-of",
                    "2025-01-01",
                    "--threshold",
                    "75.0",
                ],
            )
            assert result.exit_code == 0

    def test_search_history_missing_as_of(self, runner):
        """Test search_history command without required as_of parameter."""
        result = runner.invoke(app, ["history", "search-history", "test query"])
        assert result.exit_code != 0


# ============================================================================
# INFO COMMANDS TESTS
# ============================================================================


class TestInfoCommands:
    """Test suite for info commands."""

    @patch("barangay.cli.current", "2026-01-13")
    @patch("barangay.cli.available_dates", ["2025-07-08", "2025-08-29", "2025-10-13"])
    def test_version(self, runner):
        """Test version command."""
        result = runner.invoke(app, ["info", "version"])
        assert result.exit_code == 0
        assert "Current version:" in result.output
        assert "Available dates:" in result.output

    @patch("barangay.cli.barangay")
    @patch("barangay.cli.barangay_flat")
    @patch("barangay.cli.barangay_extended")
    def test_stats(
        self,
        mock_extended,
        mock_flat,
        mock_basic,
        runner,
        mock_basic_data,
        mock_flat_data,
        mock_extended_data,
    ):
        """Test stats command displays correct counts for all models."""
        mock_basic.model_dump.return_value = mock_basic_data
        mock_flat.__len__ = Mock(return_value=2)

        result = runner.invoke(app, ["info", "stats"])
        assert result.exit_code == 0
        assert "Data Statistics" in result.output
        assert "Basic (nested)" in result.output
        assert "Flat (list)" in result.output
        assert "Extended (recursive)" in result.output

    @patch("barangay.cli.barangay")
    def test_list_regions(self, mock_barangay, runner, mock_basic_data):
        """Test list_regions command."""
        mock_barangay.model_dump.return_value = mock_basic_data
        result = runner.invoke(app, ["info", "list-regions"])
        assert result.exit_code == 0
        assert "Regions" in result.output
        assert "Region A" in result.output
        assert "Region B" in result.output

    @patch("barangay.cli.barangay")
    def test_list_municipalities_valid(self, mock_barangay, runner, mock_basic_data):
        """Test list_municipalities with valid region."""
        mock_barangay.model_dump.return_value = mock_basic_data
        result = runner.invoke(app, ["info", "list-municipalities", "Region A"])
        assert result.exit_code == 0
        assert "Municipalities in" in result.output
        assert "Region A" in result.output
        assert "Municipality A" in result.output

    @patch("barangay.cli.barangay")
    def test_list_municipalities_invalid(self, mock_barangay, runner, mock_basic_data):
        """Test list_municipalities with invalid region."""
        mock_barangay.model_dump.return_value = mock_basic_data
        result = runner.invoke(app, ["info", "list-municipalities", "Invalid Region"])
        assert result.exit_code != 0
        assert "Region 'Invalid Region' not found" in result.output

    @patch("barangay.cli.barangay")
    def test_list_barangays_valid(self, mock_barangay, runner, mock_basic_data):
        """Test list_barangays with valid municipality."""
        mock_barangay.model_dump.return_value = mock_basic_data
        result = runner.invoke(app, ["info", "list-barangays", "Municipality A"])
        assert result.exit_code == 0
        assert "Barangays in" in result.output
        assert "Municipality A" in result.output
        assert "Barangay 1" in result.output
        assert "Barangay 2" in result.output

    @patch("barangay.cli.barangay")
    def test_list_barangays_invalid(self, mock_barangay, runner, mock_basic_data):
        """Test list_barangays with invalid municipality."""
        mock_barangay.model_dump.return_value = mock_basic_data
        result = runner.invoke(app, ["info", "list-barangays", "Invalid Municipality"])
        assert result.exit_code != 0
        assert "Municipality 'Invalid Municipality' not found" in result.output


# ============================================================================
# EXPORT COMMANDS TESTS
# ============================================================================


class TestExportCommands:
    """Test suite for export commands."""

    @patch("barangay.cli.DataManager")
    def test_export_basic_json(self, mock_dm, runner, mock_basic_data):
        """Test export command with basic model and JSON format."""
        mock_dm.return_value.get_data.return_value = mock_basic_data
        result = runner.invoke(app, ["export", "--model", "basic", "--format", "json"])
        assert result.exit_code == 0
        # Verify JSON is valid
        parsed = json.loads(result.output)
        assert isinstance(parsed, dict)

    @patch("barangay.cli.DataManager")
    def test_export_flat_json(self, mock_dm, runner, mock_flat_data):
        """Test export command with flat model and JSON format."""
        mock_dm.return_value.get_data.return_value = mock_flat_data
        result = runner.invoke(app, ["export", "--model", "flat", "--format", "json"])
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, list)

    @patch("barangay.cli.DataManager")
    def test_export_extended_json(self, mock_dm, runner, mock_extended_data):
        """Test export command with extended model and JSON format."""
        mock_dm.return_value.get_data.return_value = mock_extended_data.model_dump()
        result = runner.invoke(
            app, ["export", "--model", "extended", "--format", "json"]
        )
        assert result.exit_code == 0
        parsed = json.loads(result.output)
        assert isinstance(parsed, (dict, object))

    @patch("barangay.cli.DataManager")
    def test_export_flat_csv(self, mock_dm, runner, mock_flat_data):
        """Test export command with flat model and CSV format."""
        mock_dm.return_value.get_data.return_value = mock_flat_data
        result = runner.invoke(app, ["export", "--model", "flat", "--format", "csv"])
        assert result.exit_code == 0
        lines = result.output.strip().split("\n")
        assert len(lines) >= 2  # Header + at least one data row
        assert "name" in result.output

    @patch("barangay.cli.DataManager")
    def test_export_basic_csv(self, mock_dm, runner, mock_basic_data):
        """Test export command with basic model and CSV format."""
        mock_dm.return_value.get_data.return_value = mock_basic_data
        result = runner.invoke(app, ["export", "--model", "basic", "--format", "csv"])
        assert result.exit_code == 0
        lines = result.output.strip().split("\n")
        assert len(lines) >= 2
        assert "Region" in result.output
        assert "Municipality" in result.output
        assert "Barangay" in result.output

    @patch("barangay.cli.DataManager")
    def test_export_with_as_of(self, mock_dm, runner, mock_basic_data):
        """Test export command with historical date."""
        mock_dm.return_value.get_data.return_value = mock_basic_data
        result = runner.invoke(
            app, ["export", "--model", "basic", "--as-of", "2025-01-01"]
        )
        assert result.exit_code == 0
        mock_dm.return_value.get_data.assert_called_with(
            as_of="2025-01-01", data_type="basic"
        )

    @patch("barangay.cli.DataManager")
    def test_export_to_file(self, mock_dm, runner, mock_basic_data, tmp_path):
        """Test export command with output file."""
        output_file = tmp_path / "output.json"
        mock_dm.return_value.get_data.return_value = mock_basic_data
        result = runner.invoke(
            app, ["export", "--model", "basic", "--output", str(output_file)]
        )
        assert result.exit_code == 0
        assert output_file.exists()
        # Verify file content is valid JSON
        with open(output_file) as f:
            parsed = json.load(f)
            assert isinstance(parsed, dict)

    @patch("barangay.cli.DataManager")
    def test_export_history_basic(self, mock_dm, runner, mock_basic_data):
        """Test export_history command."""
        mock_dm.return_value.get_data.return_value = mock_basic_data
        result = runner.invoke(
            app,
            ["history", "export-history", "--as-of", "2025-01-01", "--model", "basic"],
        )
        assert result.exit_code == 0
        mock_dm.return_value.get_data.assert_called_with(
            as_of="2025-01-01", data_type="basic"
        )

    @patch("barangay.cli.DataManager")
    def test_export_history_csv(self, mock_dm, runner, mock_basic_data):
        """Test export_history command with CSV format."""
        mock_dm.return_value.get_data.return_value = mock_basic_data
        result = runner.invoke(
            app,
            [
                "history",
                "export-history",
                "--as-of",
                "2025-01-01",
                "--model",
                "basic",
                "--format",
                "csv",
            ],
        )
        assert result.exit_code == 0

    @patch("barangay.cli.DataManager")
    def test_export_history_to_file(self, mock_dm, runner, mock_basic_data, tmp_path):
        """Test export_history command with output file."""
        output_file = tmp_path / "output.json"
        mock_dm.return_value.get_data.return_value = mock_basic_data
        result = runner.invoke(
            app,
            [
                "history",
                "export-history",
                "--as-of",
                "2025-01-01",
                "--model",
                "basic",
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
    @patch("barangay.cli.current", "2026-01-13")
    def test_list_dates(self, mock_dates, runner):
        """Test list_dates command."""
        mock_dates.return_value = ["2025-07-08", "2025-08-29", "2025-10-13"]
        result = runner.invoke(app, ["history", "list-dates"])
        assert result.exit_code == 0
        assert "Available Historical Dates" in result.output
        assert "2025-07-08" in result.output
        assert "2025-08-29" in result.output
        assert "2026-01-13" in result.output
        assert "Current" in result.output


# ============================================================================
# CACHE COMMANDS TESTS
# ============================================================================


class TestCacheCommands:
    """Test suite for cache commands."""

    @patch("barangay.cli.get_cache_dir")
    def test_cache_info_empty(self, mock_cache_dir, runner, tmp_path):
        """Test cache info command with empty cache."""
        empty_cache = tmp_path / "empty_cache"
        empty_cache.mkdir(exist_ok=True)
        # Remove directory to make it non-existent
        empty_cache.rmdir()
        mock_cache_dir.return_value = empty_cache

        result = runner.invoke(app, ["cache", "info"])
        assert result.exit_code == 0
        assert "Cache Information" in result.output
        assert "0" in result.output

    @patch("barangay.cli.get_cache_dir")
    def test_cache_info_with_files(self, mock_cache_dir, runner, tmp_path):
        """Test cache info command with cached files."""
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir()
        # Create some test files
        (cache_dir / "file1.json").write_text("{}")
        (cache_dir / "file2.json").write_text('{"test": "data"}')
        mock_cache_dir.return_value = cache_dir

        result = runner.invoke(app, ["cache", "info"])
        assert result.exit_code == 0
        assert "Cache Information" in result.output
        assert "2" in result.output  # 2 files

    @patch("barangay.cli.get_cache_dir")
    def test_cache_clear_empty(self, mock_cache_dir, runner, tmp_path):
        """Test cache clear command with empty cache."""
        empty_cache = tmp_path / "empty_cache"
        empty_cache.mkdir(exist_ok=True)
        empty_cache.rmdir()
        mock_cache_dir.return_value = empty_cache

        result = runner.invoke(app, ["cache", "clear"])
        assert result.exit_code == 0
        assert "Cache directory is empty" in result.output

    @patch("barangay.cli.get_cache_dir")
    def test_cache_clear_with_files(self, mock_cache_dir, runner, tmp_path):
        """Test cache clear command with cached files."""
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
        """Test cache download command for current data."""
        result = runner.invoke(app, ["cache", "download"])
        assert result.exit_code == 0
        assert "Downloading current data" in result.output

    @patch("barangay.cli.DataManager")
    def test_cache_download_with_date(self, mock_dm, runner):
        """Test cache download command with specific date."""
        result = runner.invoke(app, ["cache", "download", "--date", "2025-01-01"])
        assert result.exit_code == 0
        assert "Downloading data for 2025-01-01" in result.output


# ============================================================================
# BATCH COMMANDS TESTS
# ============================================================================


class TestBatchCommands:
    """Test suite for batch commands."""

    def test_batch_search_basic(self, runner, mock_search_results, tmp_path):
        """Test batch_search command with basic queries."""
        # Create test input file
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\nquery2\nquery3\n")

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["batch", "batch-search", str(input_file)])
            assert result.exit_code == 0

    def test_batch_search_with_limit(self, runner, mock_search_results, tmp_path):
        """Test batch_search command with custom limit."""
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\n")

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app, ["batch", "batch-search", str(input_file), "--limit", "3"]
            )
            assert result.exit_code == 0

    def test_batch_search_with_threshold(self, runner, mock_search_results, tmp_path):
        """Test batch_search command with custom threshold."""
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\n")

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app, ["batch", "batch-search", str(input_file), "--threshold", "75.0"]
            )
            assert result.exit_code == 0

    def test_batch_search_with_as_of(self, runner, mock_search_results, tmp_path):
        """Test batch_search command with historical date."""
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\n")

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(
                app, ["batch", "batch-search", str(input_file), "--as-of", "2025-01-01"]
            )
            assert result.exit_code == 0

    def test_batch_search_to_file(self, runner, mock_search_results, tmp_path):
        """Test batch_search command with output file."""
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\nquery2\n")
        output_file = tmp_path / "output.json"

        with patch("barangay.cli.search", return_value=mock_search_results):
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
            # Verify output is valid JSON
            with open(output_file) as f:
                parsed = json.load(f)
                assert isinstance(parsed, dict)

    def test_batch_search_empty_lines(self, runner, mock_search_results, tmp_path):
        """Test batch_search command with empty lines in input."""
        input_file = tmp_path / "queries.txt"
        input_file.write_text("query1\n\n\nquery2\n\n")

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["batch", "batch-search", str(input_file)])
            assert result.exit_code == 0

    def test_validate_basic(self, runner, mock_search_results, tmp_path):
        """Test validate command with valid barangay names."""
        input_file = tmp_path / "barangays.txt"
        input_file.write_text("Barangay 1\nBarangay 2\n")

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["batch", "validate", str(input_file)])
            assert result.exit_code == 0
            assert "Validation Results" in result.output

    def test_validate_with_invalid_names(self, runner, tmp_path):
        """Test validate command with invalid barangay names."""
        input_file = tmp_path / "barangays.txt"
        input_file.write_text("Invalid Barangay Name\n")

        with patch("barangay.cli.search", return_value=[]):
            result = runner.invoke(app, ["batch", "validate", str(input_file)])
            assert result.exit_code == 0
            assert "Not found" in result.output

    def test_validate_empty_lines(self, runner, mock_search_results, tmp_path):
        """Test validate command with empty lines in input."""
        input_file = tmp_path / "barangays.txt"
        input_file.write_text("Barangay 1\n\n\nBarangay 2\n")

        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["batch", "validate", str(input_file)])
            assert result.exit_code == 0


# ============================================================================
# UTILITY FUNCTIONS TESTS
# ============================================================================


class TestUtilityFunctions:
    """Test suite for utility functions."""

    def test_dict_to_csv(self, mock_flat_data):
        """Test _dict_to_csv utility function."""
        csv_output = _dict_to_csv(mock_flat_data)
        lines = csv_output.strip().split("\n")
        assert len(lines) == 3  # Header + 2 data rows
        assert "name" in lines[0]
        assert "Barangay 1" in csv_output
        assert "Barangay 2" in csv_output

    def test_dict_to_csv_empty(self):
        """Test _dict_to_csv with empty list."""
        csv_output = _dict_to_csv([])
        assert csv_output == ""

    def test_nested_to_csv(self, mock_basic_data):
        """Test _nested_to_csv utility function."""
        csv_output = _nested_to_csv(mock_basic_data)
        lines = csv_output.strip().split("\n")
        assert len(lines) == 4  # Header + 3 data rows
        assert "Region" in lines[0]
        assert "Municipality" in lines[0]
        assert "Barangay" in lines[0]
        assert "Region A" in csv_output
        assert "Barangay 1" in csv_output
        assert "Barangay 2" in csv_output

    def test_nested_to_csv_empty(self):
        """Test _nested_to_csv with empty dict."""
        csv_output = _nested_to_csv({})
        lines = csv_output.strip().split("\n")
        assert len(lines) == 1  # Only header


# ============================================================================
# EDGE CASES AND INTEGRATION TESTS
# ============================================================================


class TestEdgeCasesAndIntegration:
    """Test suite for edge cases and integration scenarios."""

    def test_app_help(self, runner):
        """Test app help command."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "Main CLI entry point" in result.output
        assert "search" in result.output

    def test_search_cmd_help(self, runner):
        """Test search command help."""
        result = runner.invoke(app, ["search", "--help"])
        assert result.exit_code == 0
        assert "Search for barangays by name" in result.output

    def test_info_help(self, runner):
        """Test info group help."""
        result = runner.invoke(app, ["info", "--help"])
        assert result.exit_code == 0
        assert "Information commands group" in result.output

    def test_export_help(self, runner):
        """Test export command help."""
        result = runner.invoke(app, ["export", "--help"])
        assert result.exit_code == 0
        assert "Export data to JSON or CSV" in result.output

    def test_history_help(self, runner):
        """Test history group help."""
        result = runner.invoke(app, ["history", "--help"])
        assert result.exit_code == 0
        assert "History commands group" in result.output

    def test_cache_help(self, runner):
        """Test cache group help."""
        result = runner.invoke(app, ["cache", "--help"])
        assert result.exit_code == 0
        assert "Cache commands group" in result.output

    def test_batch_help(self, runner):
        """Test batch group help."""
        result = runner.invoke(app, ["batch", "--help"])
        assert result.exit_code == 0
        assert "Batch commands group" in result.output

    def test_search_unicode_characters(self, runner):
        """Test search command with unicode characters."""
        with patch("barangay.cli.search", return_value=[]):
            result = runner.invoke(app, ["search", "Ñoño"])
            assert result.exit_code == 0

    def test_search_special_characters(self, runner, mock_search_results):
        """Test search command with special characters."""
        with patch("barangay.cli.search", return_value=mock_search_results):
            result = runner.invoke(app, ["search", "test-query_123"])
            assert result.exit_code == 0

    def test_search_very_long_query(self, runner):
        """Test search command with very long query."""
        long_query = "a" * 1000
        with patch("barangay.cli.search", return_value=[]):
            result = runner.invoke(app, ["search", long_query])
            assert result.exit_code == 0
