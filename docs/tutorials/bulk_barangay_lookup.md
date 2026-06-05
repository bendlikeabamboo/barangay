# Bulk Barangay Lookup in the Philippines with Python

Perform bulk lookups and searches across the complete PSGC dataset of 42,011 barangays, 1,488 municipalities, 146 cities, 82 provinces, and 17 regions.

## Why Bulk Lookup?

When cleaning large datasets of Philippine addresses or geographic references, you need efficient batch processing. The `barangay` package provides:

- Pre-computed fuzzy matching via `FuzzBase` for fast repeated lookups
- CLI batch commands for file-based processing
- Direct access to flat data models for filtering and joins

## Installation

```bash
pip install barangay
```

## Method 1: Python Batch Search (Recommended)

Reuse a `FuzzBase` instance to avoid reloading data on every search:

```python
from barangay import search, create_fuzz_base

fuzz_base = create_fuzz_base()
queries = [
    "Tongmageng, Tawi-Tawi",
    "Barangay 291, Manila",
    "Poblacion, Cebu City",
    "San Roque, Quezon Province",
    "Baluarte, City of San Fernando",
]

for query in queries:
    results = search(
        query,
        fuzz_base=fuzz_base,
        threshold=70.0,
        n=3,
    )
    if results:
        top = results[0]
        print(f"{query} → {top['barangay']}, {top['province_or_huc']}")
    else:
        print(f"{query} → NOT FOUND")
```

### Writing Results to JSON

```python
import json
from barangay import search, create_fuzz_base

fuzz_base = create_fuzz_base()
queries = ["Tongmageng, Tawi-Tawi", "Barangay 291, Manila"]

output = {}
for query in queries:
    results = search(query, fuzz_base=fuzz_base, threshold=70.0)
    output[query] = [
        {
            "barangay": r["barangay"],
            "municipality_or_city": r["municipality_or_city"],
            "province_or_huc": r["province_or_huc"],
            "psgc_id": r["psgc_id"],
        }
        for r in results
    ]

with open("results.json", "w") as f:
    json.dump(output, f, indent=2)
```

## Method 2: CLI Batch Search

Create a file with one query per line:

```bash
barangay batch batch-search queries.txt --limit 5 --output results.json
```

This reads `queries.txt` and writes matched results to `results.json`.

## Method 3: Direct Data Filtering

For exact or prefix matching, filter the flat data model directly:

```python
from barangay import barangay_flat

all_barangays = [item for item in barangay_flat if item.type == "barangay"]

barangays_in_manila = [
    b for b in all_barangays
    if "manila" in b.name.lower()
]

print(f"Found {len(barangays_in_manila)} barangays matching 'manila'")

pangasinan_barangays = [
    b for b in all_barangays
    if b.parent_psgc_id.startswith("1")
]
print(f"Pangasinan (Region I) has {len(pangasinan_barangays)} barangays")
```

## Method 4: Export Entire Dataset

Use the CLI to export all data for offline processing:

```bash
barangay export --model flat --format json --output all_barangays.json
```

Or with Python:

```python
from barangay import barangay_flat

data = [item.model_dump() for item in barangay_flat]

import json
with open("all_barangays.json", "w") as f:
    json.dump(data, f, indent=2)
```

## Performance Tips

| Approach | Speed | Use Case |
|----------|-------|----------|
| `FuzzBase` + `search()` | ~25-80ms/query | Fuzzy matching with typos |
| Filter `barangay_flat` | <1ms/query | Exact or prefix matching |
| CLI `batch-search` | Batch optimized | File-based processing |
| `export` + external tools | Fastest | Full dataset export |

## Historical Data

Bulk lookups also support historical PSGC data:

```python
from barangay import search, create_fuzz_base

fuzz_base = create_fuzz_base(as_of="2025-07-08")
results = search("Tongmageng", fuzz_base=fuzz_base, threshold=70.0)
```

```bash
barangay batch batch-search queries.txt --as-of "2025-07-08" --output historical_results.json
```

## Next Steps

- [Address Validation](address_validation.md) — validating individual addresses
- [API Reference](../api.md) — `search()` and `FuzzBase` documentation
- [CLI Reference](../cli.md) — batch command options
