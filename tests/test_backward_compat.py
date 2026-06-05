import barangay
from barangay.models import AdminDiv, AdminDivExtended, AdminDivFlat, BarangayModel


class TestBackwardCompatImport:
    def test_import_search(self):
        from barangay import search

        assert callable(search)

    def test_import_barangay(self):
        from barangay import barangay

        assert isinstance(barangay, AdminDiv)

    def test_import_barangay_extended(self):
        from barangay import barangay_extended

        assert isinstance(barangay_extended, AdminDivExtended)

    def test_import_barangay_flat(self):
        from barangay import barangay_flat

        assert isinstance(barangay_flat, list)

    def test_import_BARGAY_DICT(self):
        from barangay import BARANGAY

        assert isinstance(BARANGAY, dict)

    def test_import_BARANGAY_EXTENDED_DICT(self):
        from barangay import BARANGAY_EXTENDED

        assert isinstance(BARANGAY_EXTENDED, dict)

    def test_import_BARANGAY_FLAT_DICT(self):
        from barangay import BARANGAY_FLAT

        assert isinstance(BARANGAY_FLAT, list)

    def test_import_FuzzBase(self):
        from barangay import FuzzBase

        assert FuzzBase is not None

    def test_import_BarangayModel(self):
        from barangay import BarangayModel

        assert BarangayModel is not None

    def test_import_DataManager(self):
        from barangay import DataManager

        assert DataManager is not None

    def test_import_sanitize_input(self):
        from barangay import sanitize_input

        assert callable(sanitize_input)

    def test_import_create_fuzz_base(self):
        from barangay import create_fuzz_base

        assert callable(create_fuzz_base)

    def test_import_all_names(self):
        for name in barangay.__all__:
            assert hasattr(barangay, name), f"Missing: {name}"


class TestBackwardCompatSearch:
    def test_search_returns_list_of_dicts(self):
        results = barangay.search("rosario")
        assert isinstance(results, list)
        if results:
            assert isinstance(results[0], dict)

    def test_search_dict_keys(self):
        results = barangay.search("rosario")
        if results:
            keys = results[0].keys()
            assert "barangay" in keys
            assert "psgc_id" in keys

    def test_search_rosario_finds_results(self):
        results = barangay.search("rosario")
        assert len(results) > 0

    def test_search_empty_returns_empty(self):
        results = barangay.search("", threshold=100.0)
        assert results == []

    def test_search_default_params(self):
        results = barangay.search("test")
        assert isinstance(results, list)

    def test_search_custom_fuzz_base(self):
        from barangay import create_fuzz_base

        fb = create_fuzz_base()
        results = barangay.search("test", fuzz_base=fb)
        assert isinstance(results, list)

    def test_search_as_of(self):
        results = barangay.search("test", as_of=None)
        assert isinstance(results, list)


class TestBackwardCompatData:
    def test_BARANGAY_is_dict(self):
        assert isinstance(barangay.BARANGAY, dict)

    def test_BARANGAY_has_regions(self):
        assert len(barangay.BARANGAY) > 0

    def test_BARANGAY_nested_access(self):
        barangay_dict = barangay.BARANGAY
        for region in barangay_dict:
            if isinstance(barangay_dict[region], dict):
                break

    def test_BARANGAY_EXTENDED_is_dict(self):
        assert isinstance(barangay.BARANGAY_EXTENDED, dict)

    def test_BARANGAY_FLAT_is_list_of_dicts(self):
        assert isinstance(barangay.BARANGAY_FLAT, list)
        if barangay.BARANGAY_FLAT:
            assert isinstance(barangay.BARANGAY_FLAT[0], dict)

    def test_BARANGAY_FLAT_record_keys(self):
        if barangay.BARANGAY_FLAT:
            record = barangay.BARANGAY_FLAT[0]
            assert "name" in record
            assert "psgc_id" in record

    def test_barangay_model_is_admindiv(self):
        assert isinstance(barangay.barangay, AdminDiv)

    def test_barangay_extended_is_admindiv_extended(self):
        assert isinstance(barangay.barangay_extended, AdminDivExtended)

    def test_barangay_flat_is_list(self):
        assert isinstance(barangay.barangay_flat, list)
        if barangay.barangay_flat:
            assert isinstance(barangay.barangay_flat[0], AdminDivFlat)


class TestBackwardCompatModels:
    def test_BarangayModel_fields(self):
        assert hasattr(BarangayModel, "model_fields")
        fields = BarangayModel.model_fields
        assert "barangay" in fields
        assert "psgc_id" in fields

    def test_AdminDivFlat_fields(self):
        assert hasattr(AdminDivFlat, "model_fields")
        fields = AdminDivFlat.model_fields
        assert "name" in fields
        assert "psgc_id" in fields

    def test_AdminDiv_dict_access(self):
        assert hasattr(barangay.barangay, "__contains__")
        assert hasattr(barangay.barangay, "keys")


class TestBackwardCompatAttributes:
    def test_current_is_string(self):
        assert isinstance(barangay.current, str)

    def test_as_of_default_none(self):
        assert barangay.as_of is None

    def test_available_dates_is_list(self):
        assert isinstance(barangay.available_dates, list)
