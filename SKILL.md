---
name: barangay-cli
description: "Search, export, and manage Philippine barangay geographic data via the barangay CLI and Python API. Use when querying Philippine administrative units, fuzzy-matching barangay names, exporting PSGC data to CSV or JSON, browsing historical PSGC releases, batch-validating barangay codes, or listing regions and municipalities."
---

# Barangay CLI

Search, export, and manage Philippine geographic data (barangays, municipalities, regions) from the PSGC masterlist via the `barangay` CLI or Python API.

## Workflow

1. **Search** barangays by name with fuzzy matching
2. **Browse** regions, municipalities, and barangays hierarchically
3. **Export** data in JSON or CSV using basic, flat, or extended models
4. **Query historical** PSGC snapshots by date
5. **Batch process** multiple queries or validate barangay codes from a file

## Commands

### Search

```bash
barangay search "Santo Nino" --limit 5 --format json
barangay search "Manila" --as-of 2025-01-13 --format table
```

- `--limit N` — max results (default: 5)
- `--threshold 0-100` — match sensitivity (default: 60.0)
- `--as-of YYYY-MM-DD` — search a historical snapshot
- `--format {json,table}` — output format (default: table)

### Info

```bash
barangay info version
barangay info stats
barangay info list-regions
barangay info list-municipalities "National Capital Region (NCR)"
barangay info list-barangays "Manila"
```

### Export

```bash
barangay export --model extended --format csv --output data.csv
barangay export --model flat --format json --output data.json
barangay export --as-of 2025-07-08 --output historical.json
```

- `--model {basic,flat,extended}` — basic (nested), flat (list), extended (recursive with metadata)
- `--format {json,csv}` — default: json
- `--output PATH` — destination file

### History

```bash
barangay history list-dates
barangay history search-history "Tongmageng" --as-of 2025-07-08
barangay history export-history --as-of 2025-07-08
```

`--as-of` is required for `search-history` and `export-history`.

### Cache

```bash
barangay cache info
barangay cache clear
barangay cache download          # latest
barangay cache download --date 2025-07-08
```

### Batch

```bash
barangay batch batch-search queries.txt --limit 5 --output results.json
barangay batch validate barangay_names.txt
```

## Python API

```python
from barangay import search, barangay, barangay_flat, barangay_extended

# Fuzzy search
results = search("Tongmageng, Tawi-Tawi")

# Custom search with hooks and threshold
results = search("Tongmagen", n=4, match_hooks=["municipality", "barangay"], threshold=70.0)

# Historical search
results = search("Tongmageng", as_of="2025-07-08")

# Nested model — region lookups
ncr_cities = list(barangay["National Capital Region (NCR)"].keys())

# Flat model — filtering
matches = [loc for loc in barangay_flat if loc.name == "Marayos"]
```

## Notes

- Dates use `YYYY-MM-DD` format
- Models: basic (nested dict), flat (list with parent refs), extended (recursive with metadata)
- Search threshold: lower = more results, higher = stricter
- Data is cached locally after first download; use `cache clear` to reset
