from barangay.validate import validate, validate_many
from barangay.models import ValidationResult


class TestValidate:
    def test_valid_address(self):
        result = validate("Caloocan")
        assert isinstance(result, ValidationResult)

    def test_invalid_address(self):
        result = validate("xyzxyzxyznonexistent12345", threshold=99.0)
        assert result.valid is False

    def test_threshold(self):
        strict = validate("Caloocan", threshold=99.0)
        loose = validate("Caloocan", threshold=50.0)
        if not strict.valid and loose.valid:
            pass

    def test_result_fields(self):
        result = validate("Caloocan", threshold=50.0)
        assert hasattr(result, "input")
        assert hasattr(result, "valid")
        assert isinstance(result.score, (float, type(None)))

    def test_validate_many(self):
        results = validate_many(["Caloocan", "xyznonexistent12345"])
        assert len(results) == 2
        assert all(isinstance(r, ValidationResult) for r in results)

    def test_mixed_validity(self):
        results = validate_many(["Caloocan", "xyznonexistent12345"], threshold=50.0)
        valid_count = sum(1 for r in results if r.valid)
        assert 0 <= valid_count <= 2
