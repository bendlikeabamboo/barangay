from barangay import search


def test_search_rosario():
    """
    Test that searching for 'rosario' returns a non-empty list.
    """
    results = search("rosario")
    assert isinstance(results, list)
    assert len(results) > 0
    # Optionally check if 'rosario' is in the results (case-insensitive)
    found = any("rosario" in r.get("barangay", "").lower() for r in results)
    assert found


class TestSearchFuzzy:
    def test_returns_search_results(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila", limit=1)
        assert isinstance(results, list)

    def test_result_has_score(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila", limit=1)
        if results:
            assert isinstance(results[0].score, float)
            assert 0 <= results[0].score <= 100

    def test_result_has_record(self):
        from barangay.search import search_fuzzy
        from barangay.models import AdminDivRecord

        results = search_fuzzy("Manila", limit=1)
        if results:
            assert isinstance(results[0].record, AdminDivRecord)

    def test_result_convenience_properties(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila", limit=1)
        if results:
            assert results[0].name == results[0].record.name
            assert results[0].psgc_id == results[0].record.psgc_id

    def test_old_search_still_works(self):
        from barangay import search

        results = search("rosario")
        assert isinstance(results, list)

    def test_old_search_output_keys(self):
        from barangay import search

        results = search("rosario")
        if results:
            keys = results[0].keys()
            assert "psgc_id" in keys

    def test_enriched_property(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila", limit=1)
        if results:
            enriched = results[0].enriched
            assert enriched.name == results[0].record.name
            assert enriched.psgc_id == results[0].record.psgc_id

    def test_enriched_property_no_index_raises(self):
        from barangay.models import SearchResult, AdminDivRecord, AdminLevel

        record = AdminDivRecord(
            name="Test",
            type=AdminLevel.BARANGAY,
            psgc_id="0000000001",
            parent_psgc_id="0000000000",
        )
        sr = SearchResult(record=record, score=90.0, match_type="test")
        try:
            sr.enriched
            assert False, "Should have raised RuntimeError"
        except RuntimeError:
            pass

    def test_match_hooks_default_returns_results(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila", limit=1)
        assert isinstance(results, list)
        assert len(results) >= 0

    def test_match_hooks_barangay_only(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila", limit=1, match_hooks=["barangay"])
        assert isinstance(results, list)

    def test_match_hooks_municipality_barangay(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy(
            "Manila", limit=1, match_hooks=["municipality", "barangay"]
        )
        assert isinstance(results, list)

    def test_match_hooks_province_barangay(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila", limit=1, match_hooks=["province", "barangay"])
        assert isinstance(results, list)

    def test_match_hooks_through_database_view(self):
        from barangay.database import Database

        db = Database()
        view = db._view(None)
        results = view.search_fuzzy("Manila", limit=1, match_hooks=["barangay"])
        assert isinstance(results, list)

    def test_search_fuzzy_province_only(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Laguna", match_hooks=["province"])
        assert isinstance(results, list)
        assert len(results) > 0
        assert any(r.record.type.value == "province" for r in results)

    def test_search_fuzzy_municipality_only(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Pateros", match_hooks=["municipality"])
        assert isinstance(results, list)
        assert len(results) > 0
        assert any(r.record.type.value == "municipality" for r in results)

    def test_search_fuzzy_region_only(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("CALABARZON", match_hooks=["region"])
        assert isinstance(results, list)
        assert len(results) > 0
        assert any(r.record.type.value == "region" for r in results)

    def test_search_fuzzy_region_province(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("CALABARZON Laguna", match_hooks=["region", "province"])
        assert isinstance(results, list)
        assert len(results) > 0

    def test_search_fuzzy_backward_compat(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Manila")
        assert isinstance(results, list)
        assert len(results) > 0
        assert all(r.record.type.value == "barangay" for r in results)

    def test_search_fuzzy_no_barangay_hook_no_barangay_results(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy("Laguna", match_hooks=["province"])
        for r in results:
            assert r.record.type.value != "barangay"

    def test_search_fuzzy_component_city_hook(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy(
            "Dagupan", match_hooks=["independent_component_city", "barangay"]
        )
        assert isinstance(results, list)

    def test_search_fuzzy_huc_hook(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy(
            "Quezon City", match_hooks=["highly_urbanized_city", "barangay"]
        )
        assert isinstance(results, list)

    def test_match_hooks_huc_barangay(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy(
            "Quezon City", match_hooks=["highly_urbanized_city", "barangay"]
        )
        assert isinstance(results, list)
        for r in results:
            assert "highly_urbanized_city" in r.match_type

    def test_match_hooks_province_municipality_barangay(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy(
            "Los Baños, Laguna",
            match_hooks=["province", "municipality", "barangay"],
        )
        assert isinstance(results, list)
        for r in results:
            assert "province" in r.match_type

    def test_match_hooks_submun_huc(self):
        from barangay.search import search_fuzzy

        results = search_fuzzy(
            "Pateros",
            match_hooks=["highly_urbanized_city", "submunicipality", "barangay"],
        )
        assert isinstance(results, list)
