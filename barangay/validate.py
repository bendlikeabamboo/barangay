from barangay.models import ValidationResult
from barangay.search import search_fuzzy


def validate(
    address: str,
    *,
    threshold: float = 95.0,
    as_of: str | None = None,
) -> ValidationResult:
    """Validate a barangay address string against PSGC data.

    Uses fuzzy matching with a high default threshold (95.0).

    Args:
        address: Address string to validate.
        threshold: Minimum score for a match (default 95.0).
        as_of: Historical date.

    Returns:
        ValidationResult with valid flag and matched record if found.
    """
    results = search_fuzzy(address, threshold=threshold, limit=1, as_of=as_of)
    if results and results[0].score >= threshold:
        return ValidationResult(
            input=address,
            valid=True,
            matched_record=results[0].record,
            score=results[0].score,
        )
    return ValidationResult(input=address, valid=False)


def validate_many(
    addresses: list[str],
    *,
    threshold: float = 95.0,
    as_of: str | None = None,
) -> list[ValidationResult]:
    """Validate multiple addresses. Returns list of ValidationResult.

    Args:
        addresses: List of address strings to validate.
        threshold: Minimum score for a match (default 95.0).
        as_of: Historical date.

    Returns:
        List of ValidationResult objects.
    """
    return [validate(addr, threshold=threshold, as_of=as_of) for addr in addresses]
