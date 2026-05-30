import pytest
from pydantic import ValidationError

from barangay.models import BarangayModel, AdminDivExtended, AdminDiv, AdminDivFlat


class TestBarangayModel:
    def test_valid_barangay_model(self):
        data = {
            "barangay": "Barangay 123",
            "province_or_huc": "Metro Manila",
            "municipality_or_city": "City of Manila",
            "psgc_id": "012345678",
        }
        model = BarangayModel(**data)
        assert model.barangay == "Barangay 123"
        assert model.province_or_huc == "Metro Manila"
        assert model.municipality_or_city == "City of Manila"
        assert model.psgc_id == "012345678"

    def test_barangay_model_missing_barangay(self):
        data = {
            "province_or_huc": "Metro Manila",
            "municipality_or_city": "City of Manila",
            "psgc_id": "012345678",
        }
        with pytest.raises(ValidationError):
            BarangayModel(**data)

    def test_barangay_model_missing_province_or_huc(self):
        data = {
            "barangay": "Barangay 123",
            "municipality_or_city": "City of Manila",
            "psgc_id": "012345678",
        }
        with pytest.raises(ValidationError):
            BarangayModel(**data)

    def test_barangay_model_missing_municipality_or_city(self):
        data = {
            "barangay": "Barangay 123",
            "province_or_huc": "Metro Manila",
            "psgc_id": "012345678",
        }
        with pytest.raises(ValidationError):
            BarangayModel(**data)

    def test_barangay_model_missing_psgc_id(self):
        data = {
            "barangay": "Barangay 123",
            "province_or_huc": "Metro Manila",
            "municipality_or_city": "City of Manila",
        }
        with pytest.raises(ValidationError):
            BarangayModel(**data)

    def test_barangay_model_empty_string(self):
        data = {
            "barangay": "",
            "province_or_huc": "",
            "municipality_or_city": "",
            "psgc_id": "",
        }
        model = BarangayModel(**data)
        assert model.barangay == ""
        assert model.province_or_huc == ""
        assert model.municipality_or_city == ""
        assert model.psgc_id == ""

    def test_barangay_model_with_unicode(self):
        data = {
            "barangay": "Barangay Malate",
            "province_or_huc": "Metro Manila",
            "municipality_or_city": "México City",
            "psgc_id": "012345678",
        }
        model = BarangayModel(**data)
        assert model.municipality_or_city == "México City"

    def test_barangay_model_model_dump(self):
        data = {
            "barangay": "Barangay 123",
            "province_or_huc": "Metro Manila",
            "municipality_or_city": "City of Manila",
            "psgc_id": "012345678",
        }
        model = BarangayModel(**data)
        dump = model.model_dump()
        assert dump == data


class TestAdminDivExtended:
    def test_valid_admin_div_extended(self):
        data = {
            "name": "National Capital Region",
            "type": "region",
            "psgc_id": "130000000",
            "parent_psgc_id": "000000000",
        }
        model = AdminDivExtended(**data)
        assert model.name == "National Capital Region"
        assert model.type == "region"
        assert model.psgc_id == "130000000"
        assert model.parent_psgc_id == "000000000"

    def test_admin_div_extended_with_nicknames(self):
        data = {
            "name": "Manila",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
            "nicknames": ["Pearl of the Orient", "Paris of Asia"],
        }
        model = AdminDivExtended(**data)
        assert model.nicknames == ["Pearl of the Orient", "Paris of Asia"]

    def test_admin_div_extended_with_components(self):
        data = {
            "name": "Manila",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
            "components": [
                {
                    "name": "Barangay 123",
                    "type": "barangay",
                    "psgc_id": "001",
                    "parent_psgc_id": "n/a",
                }
            ],
        }
        model = AdminDivExtended(**data)
        assert len(model.components) == 1
        assert model.components[0].name == "Barangay 123"

    def test_admin_div_extended_default_nicknames(self):
        data = {
            "name": "Manila",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
        }
        model = AdminDivExtended(**data)
        assert model.nicknames is None

    def test_admin_div_extended_default_components(self):
        data = {
            "name": "Manila",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
        }
        model = AdminDivExtended(**data)
        assert model.components == []

    def test_admin_div_extended_invalid_type(self):
        data = {
            "name": "Test",
            "type": "invalid_type",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
        }
        with pytest.raises(ValidationError):
            AdminDivExtended(**data)

    def test_admin_div_extended_missing_name(self):
        data = {
            "type": "region",
            "psgc_id": "130000000",
            "parent_psgc_id": "000000000",
        }
        with pytest.raises(ValidationError):
            AdminDivExtended(**data)

    def test_admin_div_extended_missing_type(self):
        data = {
            "name": "National Capital Region",
            "psgc_id": "130000000",
            "parent_psgc_id": "000000000",
        }
        with pytest.raises(ValidationError):
            AdminDivExtended(**data)

    def test_admin_div_extended_missing_psgc_id(self):
        data = {
            "name": "National Capital Region",
            "type": "region",
            "parent_psgc_id": "000000000",
        }
        with pytest.raises(ValidationError):
            AdminDivExtended(**data)

    def test_admin_div_extended_missing_parent_psgc_id(self):
        data = {
            "name": "National Capital Region",
            "type": "region",
            "psgc_id": "130000000",
        }
        with pytest.raises(ValidationError):
            AdminDivExtended(**data)

    @pytest.mark.parametrize(
        "type_value",
        [
            "country",
            "region",
            "province",
            "city",
            "municipality",
            "barangay",
            "special_geographic_area",
            "submunicipality",
        ],
    )
    def test_admin_div_extended_valid_types(self, type_value):
        data = {
            "name": "Test",
            "type": type_value,
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
        }
        model = AdminDivExtended(**data)
        assert model.type == type_value

    def test_admin_div_extended_psgc_id_na(self):
        data = {
            "name": "Test",
            "type": "country",
            "psgc_id": "n/a",
            "parent_psgc_id": "n/a",
        }
        model = AdminDivExtended(**data)
        assert model.psgc_id == "n/a"
        assert model.parent_psgc_id == "n/a"

    def test_admin_div_extended_empty_nicknames(self):
        data = {
            "name": "Test",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
            "nicknames": [],
        }
        model = AdminDivExtended(**data)
        assert model.nicknames == []


class TestAdminDiv:
    def test_admin_div_list_root(self):
        data = ["Manila", "Quezon City", "Makati"]
        model = AdminDiv(data)
        assert model.root == data

    def test_admin_div_empty_list(self):
        data = []
        model = AdminDiv(data)
        assert model.root == []

    def test_admin_div_model_dump(self):
        data = ["Manila", "Quezon City", "Makati"]
        model = AdminDiv(data)
        assert model.model_dump() == data


class TestAdminDivFlat:
    def test_valid_admin_div_flat(self):
        data = {
            "name": "National Capital Region",
            "type": "region",
            "psgc_id": "130000000",
            "parent_psgc_id": "000000000",
        }
        model = AdminDivFlat(**data)
        assert model.name == "National Capital Region"
        assert model.type == "region"
        assert model.psgc_id == "130000000"
        assert model.parent_psgc_id == "000000000"

    def test_admin_div_flat_with_nicknames(self):
        data = {
            "name": "Manila",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
            "nicknames": ["Pearl of the Orient", "Paris of Asia"],
        }
        model = AdminDivFlat(**data)
        assert model.nicknames == ["Pearl of the Orient", "Paris of Asia"]

    def test_admin_div_flat_default_nicknames(self):
        data = {
            "name": "Manila",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
        }
        model = AdminDivFlat(**data)
        assert model.nicknames is None

    def test_admin_div_flat_invalid_type(self):
        data = {
            "name": "Test",
            "type": "invalid_type",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
        }
        with pytest.raises(ValidationError):
            AdminDivFlat(**data)

    def test_admin_div_flat_missing_name(self):
        data = {
            "type": "region",
            "psgc_id": "130000000",
            "parent_psgc_id": "000000000",
        }
        with pytest.raises(ValidationError):
            AdminDivFlat(**data)

    def test_admin_div_flat_missing_type(self):
        data = {
            "name": "National Capital Region",
            "psgc_id": "130000000",
            "parent_psgc_id": "000000000",
        }
        with pytest.raises(ValidationError):
            AdminDivFlat(**data)

    def test_admin_div_flat_missing_psgc_id(self):
        data = {
            "name": "National Capital Region",
            "type": "region",
            "parent_psgc_id": "000000000",
        }
        with pytest.raises(ValidationError):
            AdminDivFlat(**data)

    def test_admin_div_flat_missing_parent_psgc_id(self):
        data = {
            "name": "National Capital Region",
            "type": "region",
            "psgc_id": "130000000",
        }
        with pytest.raises(ValidationError):
            AdminDivFlat(**data)

    @pytest.mark.parametrize(
        "type_value",
        [
            "country",
            "region",
            "province",
            "city",
            "municipality",
            "barangay",
            "special_geographic_area",
            "submunicipality",
        ],
    )
    def test_admin_div_flat_valid_types(self, type_value):
        data = {
            "name": "Test",
            "type": type_value,
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
        }
        model = AdminDivFlat(**data)
        assert model.type == type_value

    def test_admin_div_flat_psgc_id_na(self):
        data = {
            "name": "Test",
            "type": "country",
            "psgc_id": "n/a",
            "parent_psgc_id": "n/a",
        }
        model = AdminDivFlat(**data)
        assert model.psgc_id == "n/a"
        assert model.parent_psgc_id == "n/a"

    def test_admin_div_flat_empty_nicknames(self):
        data = {
            "name": "Test",
            "type": "city",
            "psgc_id": "013754000",
            "parent_psgc_id": "130000000",
            "nicknames": [],
        }
        model = AdminDivFlat(**data)
        assert model.nicknames == []

    def test_admin_div_flat_model_dump(self):
        data = {
            "name": "National Capital Region",
            "type": "region",
            "psgc_id": "130000000",
            "parent_psgc_id": "000000000",
            "nicknames": None,
        }
        model = AdminDivFlat(**data)
        assert model.model_dump(exclude={"extensions"}) == data
