import pytest

from barangay.database import (
    Database,
    HierarchyIndex,
    DatabaseView,
    EnrichedRecord,
)
from barangay.models import AdminDivRecord, AdminLevel


@pytest.fixture
def sample_records():
    country = AdminDivRecord(
        name="Philippines",
        type=AdminLevel.COUNTRY,
        psgc_id="0000000000",
        parent_psgc_id="n/a",
    )
    region = AdminDivRecord(
        name="National Capital Region (NCR)",
        type=AdminLevel.REGION,
        psgc_id="0133000000",
        parent_psgc_id="0000000000",
    )
    province = AdminDivRecord(
        name="Laguna",
        type=AdminLevel.PROVINCE,
        psgc_id="0136000000",
        parent_psgc_id="0133000000",
    )
    huc = AdminDivRecord(
        name="City of Caloocan",
        type=AdminLevel.HIGHLY_URBANIZED_CITY,
        psgc_id="1380100000",
        parent_psgc_id="0133000000",
    )
    municipality = AdminDivRecord(
        name="Bay",
        type=AdminLevel.MUNICIPALITY,
        psgc_id="043421000",
        parent_psgc_id="0136000000",
    )
    barangay = AdminDivRecord(
        name="Barangay 1",
        type=AdminLevel.BARANGAY,
        psgc_id="1380100001",
        parent_psgc_id="1380100000",
    )
    sga = AdminDivRecord(
        name="Special Geographic Area",
        type=AdminLevel.SPECIAL_GEOGRAPHIC_AREA,
        psgc_id="1999900000",
        parent_psgc_id="0126000000",
    )
    return [country, region, province, huc, municipality, barangay, sga]


@pytest.fixture
def index(sample_records):
    return HierarchyIndex(sample_records)


class TestHierarchyIndex:
    def test_build_from_records(self, index):
        assert len(index._by_id) == 7

    def test_get_by_psgc_id(self, index):
        r = index.get("0133000000")
        assert r is not None
        assert r.name == "National Capital Region (NCR)"

    def test_get_missing_psgc_id(self, index):
        assert index.get("9999999999") is None

    def test_parent_of_barangay(self, index):
        brgy = index.get("1380100001")
        parent = index.parent(brgy)
        assert parent is not None
        assert parent.name == "City of Caloocan"

    def test_parent_of_country(self, index):
        country = index.get("0000000000")
        assert index.parent(country) is None

    def test_children_of_region(self, index):
        children = index.children("0133000000")
        names = [c.name for c in children]
        assert "City of Caloocan" in names

    def test_children_of_barangay(self, index):
        assert index.children("1380100001") == []

    def test_ancestors_of_barangay(self, index):
        brgy = index.get("1380100001")
        ancestors = index.ancestors(brgy)
        names = [a.name for a in ancestors]
        assert "City of Caloocan" in names
        assert "National Capital Region (NCR)" in names
        assert "Philippines" in names

    def test_resolve_region_from_barangay(self, index):
        brgy = index.get("1380100001")
        region = index.resolve_region(brgy)
        assert region is not None
        assert region.name == "National Capital Region (NCR)"

    def test_resolve_province_for_huc(self, index):
        brgy = index.get("1380100001")
        province = index.resolve_province(brgy)
        assert province is None

    def test_resolve_city_for_barangay_under_huc(self, index):
        brgy = index.get("1380100001")
        city = index.resolve_city(brgy)
        assert city is not None
        assert city.name == "City of Caloocan"
        assert city.type == AdminLevel.HIGHLY_URBANIZED_CITY

    def test_resolve_municipality_for_barangay(self, index):
        municipality = index.get("043421000")
        resolved = index.resolve_municipality(municipality)
        assert resolved is not None
        assert resolved.name == "Bay"

    def test_records_of_type(self, index):
        barangays = index.records_of_type(AdminLevel.BARANGAY)
        assert len(barangays) == 1
        assert barangays[0].name == "Barangay 1"

    def test_records_of_types(self, index):
        from barangay.database import _CITY_ADMIN_LEVELS

        cities = index.records_of_types(_CITY_ADMIN_LEVELS)
        assert len(cities) == 1
        assert cities[0].name == "City of Caloocan"


class TestEnrichedRecord:
    def test_stored_fields(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        assert brgy.name == "Barangay 1"
        assert brgy.psgc_id == "1380100001"
        assert brgy.type == AdminLevel.BARANGAY

    def test_region(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        assert brgy.region == "National Capital Region (NCR)"

    def test_province_none_for_huc(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        assert brgy.province is None

    def test_city_for_barangay_under_huc(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        assert brgy.city == "City of Caloocan"

    def test_municipality_none_for_huc(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        assert brgy.municipality is None

    def test_parent_navigation(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        parent = brgy.parent
        assert parent is not None
        assert parent.name == "City of Caloocan"

    def test_parent_chain(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        grandparent = brgy.parent.parent
        assert grandparent is not None
        assert grandparent.type == AdminLevel.REGION

    def test_children_of_region(self, index):
        region = EnrichedRecord(index.get("0133000000"), index)
        children = region.children
        names = [c.name for c in children]
        assert "City of Caloocan" in names

    def test_children_of_barangay_empty(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        assert brgy.children == []

    def test_ancestors(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        ancestor_names = [a.name for a in brgy.ancestors]
        assert "City of Caloocan" in ancestor_names
        assert "Philippines" in ancestor_names

    def test_to_dict(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        d = brgy.to_dict()
        assert d["name"] == "Barangay 1"
        assert d["region"] == "National Capital Region (NCR)"
        assert d["province"] is None
        assert d["highly_urbanized_city"] == "City of Caloocan"
        assert d["city"] == "City of Caloocan"

    def test_repr(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        r = repr(brgy)
        assert "barangay" in r
        assert "Barangay 1" in r

    def test_equality(self, index):
        r1 = EnrichedRecord(index.get("1380100001"), index)
        r2 = EnrichedRecord(index.get("1380100001"), index)
        assert r1 == r2

    def test_hash(self, index):
        r1 = EnrichedRecord(index.get("1380100001"), index)
        r2 = EnrichedRecord(index.get("1380100001"), index)
        assert hash(r1) == hash(r2)
        assert len({r1, r2}) == 1

    def test_delegates_model_dump(self, index):
        brgy = EnrichedRecord(index.get("1380100001"), index)
        d = brgy.model_dump()
        assert d["name"] == "Barangay 1"
        assert d["psgc_id"] == "1380100001"


class TestDatabaseView:
    def test_len(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        assert len(view) == 1

    def test_len_with_levels(self, sample_records, index):
        from barangay.database import _VersionState, _CITY_ADMIN_LEVELS

        view = DatabaseView(
            records=sample_records,
            index=index,
            levels=_CITY_ADMIN_LEVELS,
            plugin_index=None,
            version_state=_VersionState(),
        )
        assert len(view) == 1

    def test_iter(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        records = list(view)
        assert len(records) == 1
        assert isinstance(records[0], EnrichedRecord)

    def test_contains(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        assert "1380100001" in view
        assert "0133000000" not in view

    def test_get_by_psgc_id(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        result = view.get(psgc_id="1380100001")
        assert result is not None
        assert result.name == "Barangay 1"

    def test_get_by_psgc_id_wrong_level(self, sample_records, index):
        from barangay.database import RecordNotFoundError, _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.PROVINCE,
            plugin_index=None,
            version_state=_VersionState(),
        )
        with pytest.raises(RecordNotFoundError):
            view.get(psgc_id="1380100001")

    def test_get_by_name_single(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        result = view.get(name="Barangay 1")
        assert result is not None
        assert result.name == "Barangay 1"

    def test_get_by_name_missing(self, sample_records, index):
        from barangay.database import RecordNotFoundError, _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        with pytest.raises(RecordNotFoundError):
            view.get(name="Nonexistent")

    def test_get_no_args_raises(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        with pytest.raises(ValueError):
            view.get()

    def test_get_both_args_raises(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        with pytest.raises(ValueError):
            view.get(psgc_id="1380100001", name="Barangay 1")

    def test_to_dicts_includes_hierarchy(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        dicts = view.to_dicts()
        assert len(dicts) == 1
        assert "region" in dicts[0]
        assert "province" in dicts[0]

    def test_repr(self, sample_records, index):
        from barangay.database import _VersionState

        view = DatabaseView(
            records=sample_records,
            index=index,
            level=AdminLevel.BARANGAY,
            plugin_index=None,
            version_state=_VersionState(),
        )
        r = repr(view)
        assert "barangay" in r
        assert "1 records" in r


class TestDatabase:
    def test_singleton(self):
        db1 = Database()
        db2 = Database()
        assert db1 is db2

    def test_all_levels_accessible(self):
        db = Database()
        assert isinstance(db.regions, DatabaseView)
        assert isinstance(db.provinces, DatabaseView)
        assert isinstance(db.cities, DatabaseView)
        assert isinstance(db.hucs, DatabaseView)
        assert isinstance(db.iccs, DatabaseView)
        assert isinstance(db.component_cities, DatabaseView)
        assert isinstance(db.municipalities, DatabaseView)
        assert isinstance(db.barangays, DatabaseView)
        assert isinstance(db.submunicipalities, DatabaseView)
        assert isinstance(db.special_geographic_areas, DatabaseView)

    def test_all_records_view(self):
        db = Database()
        total = len(db.all_records)
        assert total > 40000

    def test_total_count(self):
        db = Database()
        total = (
            len(db.regions)
            + len(db.provinces)
            + len(db.cities)
            + len(db.municipalities)
            + len(db.submunicipalities)
            + len(db.barangays)
            + len(db.special_geographic_areas)
        )
        assert total == len(db.all_records)

    def test_cities_equals_sum_of_subtypes(self):
        db = Database()
        assert len(db.cities) == len(db.hucs) + len(db.iccs) + len(db.component_cities)

    def test_invalidate_cache(self):
        db = Database()
        db._ensure_loaded()
        assert db._raw_records is not None
        db.invalidate_cache()
        assert db._raw_records is None


class TestDatabaseIntegration:
    def test_search_then_get(self):
        db = Database()
        results = db.barangays.search_fuzzy("Caloocan", limit=1)
        if results:
            record = results[0].record
            found = db.barangays.lookup(record.psgc_id)
            assert found is not None

    def test_no_orphan_records(self):
        db = Database()
        for record in db.all_records:
            if record.type not in (AdminLevel.COUNTRY, AdminLevel.REGION):
                assert db._index.parent(record) is not None

    def test_psgc_id_uniqueness(self):
        db = Database()
        ids = [r.psgc_id for r in db.all_records]
        assert len(ids) == len(set(ids))

    def test_all_barangays_have_parent(self):
        db = Database()
        for brgy in db.barangays:
            assert brgy.parent is not None

    def test_navigation_roundtrip(self):
        db = Database()
        for brgy in db.barangays:
            if brgy.region and brgy.province:
                parent = brgy.parent
                if parent:
                    assert parent.psgc_id == brgy.parent_psgc_id
                break

    def test_hucs_have_no_province(self):
        db = Database()
        for huc in db.hucs:
            assert huc.province is None

    def test_component_cities_have_province(self):
        db = Database()
        for cc in db.component_cities:
            if cc.name == "City of Isabela":
                continue
            assert cc.province is not None
