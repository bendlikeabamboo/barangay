import pytest

from barangay.explode import (
    ExplodeError,
    classify_plugins,
    explode_array,
    explode_flat,
    flatten_scalar,
    validate_single_array,
)


def _make_plugin_index(entries):
    index = {}
    for psgc_id, plugins in entries.items():
        index[psgc_id] = {}
        for plugin_name, data in plugins.items():
            index[psgc_id][plugin_name] = {
                "metadata": {"name": plugin_name},
                "data": data,
            }
    return index


class TestClassifyPlugins:
    def test_scalar_plugin(self):
        index = _make_plugin_index(
            {
                "001": {"pop": {"population": 1000, "households": 200}},
                "002": {"pop": {"population": 2000}},
            }
        )
        scalar, array = classify_plugins(index)
        assert "pop" in scalar
        assert "population" in scalar["pop"]
        assert "households" in scalar["pop"]
        assert array == {}

    def test_array_plugin(self):
        index = _make_plugin_index(
            {
                "001": {"schools": [{"beiss_id": 1, "name": "School A"}]},
                "002": {"schools": [{"beiss_id": 2, "name": "School B"}]},
            }
        )
        scalar, array = classify_plugins(index)
        assert scalar == {}
        assert "schools" in array
        assert "beiss_id" in array["schools"]
        assert "name" in array["schools"]

    def test_mixed_scalar_and_array(self):
        index = _make_plugin_index(
            {
                "001": {
                    "pop": {"population": 1000},
                    "schools": [{"beiss_id": 1, "name": "School A"}],
                },
            }
        )
        scalar, array = classify_plugins(index)
        assert "pop" in scalar
        assert "schools" in array

    def test_empty_index(self):
        scalar, array = classify_plugins({})
        assert scalar == {}
        assert array == {}

    def test_no_data_skipped(self):
        index = _make_plugin_index(
            {
                "001": {"empty": None},
            }
        )
        scalar, array = classify_plugins(index)
        assert scalar == {}
        assert array == {}

    def test_inconsistent_data_type_raises(self):
        index = _make_plugin_index(
            {
                "001": {"mixed": {"key": "value"}},
                "002": {"mixed": [{"key": "value"}]},
            }
        )
        with pytest.raises(ExplodeError, match="inconsistent data types"):
            classify_plugins(index)

    def test_collects_all_field_names_across_records(self):
        index = _make_plugin_index(
            {
                "001": {"pop": {"population": 1000}},
                "002": {"pop": {"population": 2000, "area": 5.0}},
            }
        )
        scalar, array = classify_plugins(index)
        assert set(scalar["pop"]) == {"population", "area"}

    def test_collects_all_array_field_names(self):
        index = _make_plugin_index(
            {
                "001": {"schools": [{"name": "A"}]},
                "002": {"schools": [{"name": "B", "students": 500}]},
            }
        )
        scalar, array = classify_plugins(index)
        assert set(array["schools"]) == {"name", "students"}


class TestValidateSingleArray:
    def test_zero_array_plugins_ok(self):
        validate_single_array({})

    def test_one_array_plugin_ok(self):
        validate_single_array({"schools": ["beiss_id", "name"]})

    def test_two_array_plugins_raises(self):
        with pytest.raises(ExplodeError, match="Cannot enable more than one"):
            validate_single_array(
                {
                    "schools": ["beiss_id", "name"],
                    "hospitals": ["id", "name"],
                }
            )

    def test_error_includes_plugin_names(self):
        with pytest.raises(ExplodeError, match="hospitals.*schools"):
            validate_single_array(
                {
                    "schools": ["beiss_id"],
                    "hospitals": ["id"],
                }
            )


class TestFlattenScalar:
    def test_flattens_scalar_fields(self):
        index = _make_plugin_index(
            {
                "001": {"pop": {"population": 1000, "households": 200}},
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        result = flatten_scalar(record, index, {"pop": ["population", "households"]})
        assert result["pop.population"] == 1000
        assert result["pop.households"] == 200
        assert result["name"] == "Test"

    def test_no_match_leaves_record_unchanged(self):
        index = _make_plugin_index(
            {
                "001": {"pop": {"population": 1000}},
            }
        )
        record = {"psgc_id": "002", "name": "Test"}
        result = flatten_scalar(record, index, {"pop": ["population"]})
        assert "pop.population" not in result

    def test_does_not_mutate_original(self):
        index = _make_plugin_index(
            {
                "001": {"pop": {"population": 1000}},
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        flatten_scalar(record, index, {"pop": ["population"]})
        assert "pop.population" not in record

    def test_multiple_scalar_plugins(self):
        index = _make_plugin_index(
            {
                "001": {
                    "pop": {"population": 1000},
                    "elev": {"elevation": 50},
                },
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        result = flatten_scalar(
            record, index, {"pop": ["population"], "elev": ["elevation"]}
        )
        assert result["pop.population"] == 1000
        assert result["elev.elevation"] == 50


class TestExplodeArray:
    def test_single_element(self):
        index = _make_plugin_index(
            {
                "001": {"schools": [{"beiss_id": 1, "name": "School A"}]},
            }
        )
        record = {"psgc_id": "001", "name": "Test", "pop.population": 1000}
        rows = explode_array(record, index, "schools")
        assert len(rows) == 1
        assert rows[0]["schools.beiss_id"] == 1
        assert rows[0]["schools.name"] == "School A"
        assert rows[0]["pop.population"] == 1000

    def test_multiple_elements(self):
        index = _make_plugin_index(
            {
                "001": {
                    "schools": [
                        {"beiss_id": 1, "name": "School A"},
                        {"beiss_id": 2, "name": "School B"},
                    ],
                },
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        rows = explode_array(record, index, "schools")
        assert len(rows) == 2
        assert rows[0]["schools.name"] == "School A"
        assert rows[1]["schools.name"] == "School B"

    def test_no_data_returns_original(self):
        index = _make_plugin_index(
            {
                "002": {"schools": [{"name": "Other"}]},
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        rows = explode_array(record, index, "schools")
        assert len(rows) == 1
        assert rows[0] == {"psgc_id": "001", "name": "Test"}

    def test_empty_list_returns_original(self):
        index = _make_plugin_index(
            {
                "001": {"schools": []},
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        rows = explode_array(record, index, "schools")
        assert len(rows) == 1
        assert rows[0] == {"psgc_id": "001", "name": "Test"}

    def test_does_not_mutate_original(self):
        index = _make_plugin_index(
            {
                "001": {"schools": [{"name": "A"}]},
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        explode_array(record, index, "schools")
        assert "schools.name" not in record


class TestExplodeFlat:
    def test_empty_plugin_index(self):
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = explode_flat(flat_data, {})
        assert len(result) == 1
        assert result[0] == {"psgc_id": "001", "name": "Test"}

    def test_scalar_only_no_row_multiplication(self):
        index = _make_plugin_index(
            {
                "001": {"pop": {"population": 1000}},
            }
        )
        flat_data = [
            {"psgc_id": "001", "name": "Test"},
            {"psgc_id": "002", "name": "NoData"},
        ]
        result = explode_flat(flat_data, index)
        assert len(result) == 2
        assert result[0]["pop.population"] == 1000
        assert "pop.population" not in result[1]

    def test_array_plugin_explodes_rows(self):
        index = _make_plugin_index(
            {
                "001": {
                    "schools": [
                        {"beiss_id": 1, "name": "School A"},
                        {"beiss_id": 2, "name": "School B"},
                    ],
                },
            }
        )
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = explode_flat(flat_data, index)
        assert len(result) == 2
        assert result[0]["schools.name"] == "School A"
        assert result[1]["schools.name"] == "School B"

    def test_scalar_plus_array(self):
        index = _make_plugin_index(
            {
                "001": {
                    "pop": {"population": 1000},
                    "schools": [
                        {"beiss_id": 1, "name": "School A"},
                        {"beiss_id": 2, "name": "School B"},
                    ],
                },
            }
        )
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        result = explode_flat(flat_data, index)
        assert len(result) == 2
        assert result[0]["pop.population"] == 1000
        assert result[1]["pop.population"] == 1000
        assert result[0]["schools.name"] == "School A"
        assert result[1]["schools.name"] == "School B"

    def test_two_array_plugins_raises(self):
        index = _make_plugin_index(
            {
                "001": {
                    "schools": [{"name": "A"}],
                    "hospitals": [{"name": "H"}],
                },
            }
        )
        flat_data = [{"psgc_id": "001", "name": "Test"}]
        with pytest.raises(ExplodeError, match="Cannot enable more than one"):
            explode_flat(flat_data, index)

    def test_multiple_records_with_array(self):
        index = _make_plugin_index(
            {
                "001": {"schools": [{"name": "A"}, {"name": "B"}]},
                "002": {"schools": [{"name": "C"}]},
            }
        )
        flat_data = [
            {"psgc_id": "001", "name": "First"},
            {"psgc_id": "002", "name": "Second"},
        ]
        result = explode_flat(flat_data, index)
        assert len(result) == 3
        assert result[0]["schools.name"] == "A"
        assert result[1]["schools.name"] == "B"
        assert result[2]["schools.name"] == "C"

    def test_does_not_mutate_original_records(self):
        index = _make_plugin_index(
            {
                "001": {"pop": {"population": 1000}},
            }
        )
        record = {"psgc_id": "001", "name": "Test"}
        explode_flat([record], index)
        assert "pop.population" not in record

    def test_output_shape_scalar_only(self):
        index = _make_plugin_index(
            {
                "1380100000": {
                    "sample_population": {"population": 1662000, "households": 368000},
                },
            }
        )
        flat_data = [
            {
                "name": "City of Caloocan",
                "type": "highly_urbanized_city",
                "psgc_id": "1380100000",
                "parent_psgc_id": "1380100000",
            },
        ]
        result = explode_flat(flat_data, index)
        assert len(result) == 1
        row = result[0]
        assert row["sample_population.population"] == 1662000
        assert row["sample_population.households"] == 368000

    def test_output_shape_scalar_plus_array(self):
        index = _make_plugin_index(
            {
                "1380100001": {
                    "sample_population": {"population": 50000, "households": 12000},
                    "sample_schools": [
                        {
                            "beiss_id": 10001,
                            "name": "Caloocan North ES",
                            "classification": "Elementary",
                            "students": 1200,
                        },
                        {
                            "beiss_id": 10002,
                            "name": "North City NHS",
                            "classification": "Junior",
                            "students": 850,
                        },
                    ],
                },
            }
        )
        flat_data = [
            {
                "name": "Barangay 1",
                "type": "barangay",
                "psgc_id": "1380100001",
                "parent_psgc_id": "1380100000",
            },
        ]
        result = explode_flat(flat_data, index)
        assert len(result) == 2
        assert result[0]["sample_population.population"] == 50000
        assert result[0]["sample_schools.beiss_id"] == 10001
        assert result[1]["sample_schools.beiss_id"] == 10002
