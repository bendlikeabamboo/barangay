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
