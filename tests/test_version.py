from barangay.database import Database
from barangay.version import use_version


class TestUseVersion:
    def test_none_resets(self):
        db = Database()
        db._ensure_loaded()
        use_version(None)
        assert db._version_state.as_of is None

    def test_cache_invalidation(self):
        db = Database()
        db._ensure_loaded()
        assert db._raw_records is not None
        use_version(None)
        assert db._raw_records is None

    def test_old_date_resolves_to_earliest(self):
        db = Database()
        use_version("1800-01-01")
        assert db._version_state.as_of is not None
        use_version(None)
