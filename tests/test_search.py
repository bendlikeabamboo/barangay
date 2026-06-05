from barangay import search


def test_search_rosario():
    """
    Test that searching for 'rosario' returns a non-empty list.
    """
    results = search("rosario")
    assert isinstance(results, list)
    assert len(results) > 0
    # Optionally check if 'rosario' is in the results (case-insensitive)
    found = any("rosario" in r["barangay"].lower() for r in results)
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
            assert "barangay" in keys
            assert "province_or_huc" in keys
            assert "municipality_or_city" in keys
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
