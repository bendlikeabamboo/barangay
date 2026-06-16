---
title: "Validate Philippine Addresses in Python with PSGC"
description: "How to validate Philippine addresses against the official PSGC masterlist in Python using the barangay package. Fuzzy matching handles misspellings and unstandardized formats with validate() and validate_many()."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# Validate Philippine Addresses in Python with PSGC

Address validation is one of the most common reasons teams adopt the
**Philippine Standard Geographic Code (PSGC)**. Misspelled barangays, missing
provinces, and inconsistent casing make user-entered Philippine addresses
notoriously hard to clean. This post shows how to validate them in Python —
fully offline — with the `barangay` package.

## Why address validation is hard in the Philippines

- **42,011 barangays** with similar or duplicated names across provinces.
- Users often omit the municipality or use abbreviations ("San", "Sta.").
- Free-text fields mix barangay, city, and province in arbitrary order.
- Spellings drift ("Tongmageng" vs "Tongmagen").

## Install

```bash
pip install barangay
```

## Validate a single address

```python
from barangay import validate

result = validate("Tongmageng, Tawi-Tawi")
print(result.valid, result.matched_name, result.score)
# True Tongmageng 100.0
```

`validate()` returns a `ValidationResult` with `valid`, `matched_name`,
`matched_psgc_id`, and a fuzzy `score` (0–100). The default threshold is 95.0.

## Validate in bulk

```python
from barangay import validate_many

addresses = [
    "Tongmageng, Tawi-Tawi",
    "Bagumbayan, Quezon City",
    "Nonexistent Place, Nowhere",
]
for r in validate_many(addresses):
    print(f"{r.input!r} -> {'valid' if r.valid else 'invalid'} ({r.score})")
```

## Tuning the threshold

Lower the threshold to catch more approximate matches, or raise it to be
stricter:

```python
validate("Tongmagen, Tawi-Tawi", threshold=80.0)
```

## Why do it offline?

`barangay` bundles the complete PSGC dataset, so validation runs in-process
with no API calls, rate limits, or network dependency — perfect for batch
cleaning of large datasets, ETL pipelines, and CI checks.

---

Read the full [address validation tutorial](../tutorials/address_validation.md)
or browse the [API reference](../api.md).
