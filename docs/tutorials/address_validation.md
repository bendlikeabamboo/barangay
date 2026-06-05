# Address Validation in the Philippines with Python

Validate Philippine addresses against the official PSGC masterlist using the `barangay` package. Fuzzy matching handles common misspellings, abbreviations, and unstandardized address formats.

## Why Address Validation Matters

Philippine addresses are notoriously inconsistent. A single barangay might appear as:

- "Brgy. 291"
- "Barangay 291"
- "Barangay No. 291"
- "Brgy 291"

The `barangay` package solves this by matching addresses against the official Philippine Standard Geographic Code (PSGC) masterlist from the Philippine Statistics Authority (PSA), which covers all 42,011 barangays.

## Installation

```bash
pip install barangay
```

## Basic Validation

Use the `search()` function with a high threshold to validate addresses:

```python
from barangay import search

address = "Brgy 291, City of Manila, Metro Manila"
results = search(address, threshold=80.0)

if results and results[0].get("f_0pmb_ratio_score", 0) >= 90:
    print(f"Valid: {results[0]['barangay']}, {results[0]['province_or_huc']}")
else:
    print("Address not found or ambiguous")
```

## Handling Misspellings

Fuzzy search tolerates typos and alternative spellings:

```python
from barangay import search

results = search("Tongmagen, Tawi-Tawi", threshold=70.0)
for r in results[:3]:
    print(f"{r['barangay']} — score: {r.get('f_0pmb_ratio_score', 'N/A')}")
```

Output:

| Barangay | Municipality/City | Province | Score |
|----------|-------------------|----------|-------|
| Tongmageng | Sitangkai | Tawi-Tawi | 95.2 |
| Tonggosong | Simunul | Tawi-Tawi | 84.2 |
| Tongbangkaw | Tandubas | Tawi-Tawi | 82.1 |

## Batch Validation with CLI

Validate a list of addresses from a file:

```bash
barangay batch validate addresses.txt
```

Each line in `addresses.txt` should contain one barangay name.

## Batch Search with Python

For programmatic batch validation:

```python
from barangay import search, create_fuzz_base

fuzz_base = create_fuzz_base()
addresses = [
    "Brgy 291, Manila",
    "Tongmageng, Tawi-Tawi",
    "Poblacion, Davao City",
]

for addr in addresses:
    results = search(addr, fuzz_base=fuzz_base, threshold=70.0)
    if results:
        top = results[0]
        print(f"{addr} → {top['barangay']}, {top['municipality_or_city']}")
```

## Custom Sanitization

Strip common prefixes and suffixes before matching:

```python
from barangay import sanitize_input, search

raw = "(Pob.) San Jose City"
clean = sanitize_input(raw, exclude=["(pob.)", " city"])
results = search(clean, threshold=80.0)
```

## Next Steps

- [API Reference](../api.md) — full `search()` parameter documentation
- [CLI Reference](../cli.md) — `barangay batch validate` options
- [Bulk Barangay Lookup](bulk_barangay_lookup.md) — batch processing at scale
