# 🇵🇭 barangay

[![PyPI version](https://img.shields.io/pypi/v/barangay.svg)](https://pypi.org/project/barangay/)
[![PyPI Downloads](https://static.pepy.tech/badge/barangay)](https://pepy.tech/projects/barangay)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml/badge.svg)](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml)
[![Visit the Docs](https://img.shields.io/badge/Visit%20the%20Docs-red)](https://bendlikeabamboo.github.io/barangay/)
[![zread](https://img.shields.io/badge/Ask_Zread-_.svg?style=flat&color=00b0aa&labelColor=000000&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuOTYxNTYgMS42MDAxSDIuMjQxNTZDMS44ODgxIDEuNjAwMSAxLjYwMTU2IDEuODg2NjQgMS42MDE1NiAyLjI0MDFWNC45NjAxQzEuNjAxNTYgNS4zMTM1NiAxLjg4ODEgNS42MDAxIDIuMjQxNTYgNS42MDAxSDQuOTYxNTZDNS4zMTUwMiA1LjYwMDEgNS42MDE1NiA1LjMxMzU2IDUuNjAxNTYgNC45NjAxVjIuMjQwMUM1LjYwMTU2IDEuODg2NjQgNS4zMTUwMiAxLjYwMDEgNC45NjE1NiAxLjYwMDFaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00Ljk2MTU2IDEwLjM5OTlIMi4yNDE1NkMxLjg4ODEgMTAuMzk5OSAxLjYwMTU2IDEwLjY4NjQgMS42MDE1NiAxMS4wMzk5VjEzLjc1OTlDMS42MDE1NiAxNC4xMTM0IDEuODg4MSAxNC4zOTk5IDIuMjQxNTYgMTQuMzk5OUg0Ljk2MTU2QzUuMzE1MDIgMTQuMzk5OSA1LjYwMTU2IDE0LjExMzQgNS42MDE1NiAxMy43NTk5VjExLjAzOTlDNS42MDE1NiAxMC42ODY0IDUuMzE1MDIgMTAuMzk5OSA0Ljk2MTU2IDEwLjM5OTlaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik0xMy43NTg0IDEuNjAwMUgxMS4wMzg0QzEwLjY4NSAxLjYwMDEgMTAuMzk4NCAxLjg4NjY0IDEwLjM5ODQgMi4yNDAxVjQuOTYwMUMxMC4zOTg0IDUuMzEzNTYgMTAuNjg1IDUuNjAwMSAxMS4wMzg0IDUuNjAwMUgxMy43NTg0QzE0LjExMTkgNS42MDAxIDE0LjM5ODQgNS4zMTM1NiAxNC4zOTg0IDQuOTYwMVYyLjI0MDFDMTQuMzk4NCAxLjg4NjY0IDE0LjExMTkgMS42MDAxIDEzLjc1ODQgMS42MDAxWiIgZmlsbD0iI2ZmZiIvPgo8cGF0aCBkPSJNNCAxMkwxMiA0TDQgMTJaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00IDEyTDEyIDQiIHN0cm9rZT0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K&logoColor=ffffff)](https://zread.ai/bendlikeabamboo/barangay)

Philippine Standard Geographic Code (PSGC) Python package with fuzzy search for barangays, municipalities, cities, provinces, and regions. Based on the official April 2026 PSGC masterlist. Offline access to all 42,011 barangays — no API calls or database needed.

---

## Quick Start

```bash
pip install barangay
```

```python
from barangay import barangays, search_fuzzy

# Browse all 42,011 barangays
print(barangays)  # <PSGC barangay database: 42010 records>

# Get a specific barangay
brgy = barangays.get(name="Tongmageng")
print(brgy.region)    # Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)
print(brgy.province)  # Tawi-Tawi
print(brgy.psgc_id)   # 1907005010

# Fuzzy search
for r in search_fuzzy("Tongmagen, Tawi-Tawi"):
    print(f"{r.name} — score: {r.score}")
```

---

## Features

| Feature | Description |
|---------|-------------|
| 🔍 **Fuzzy Search** | Fast, customizable matching for unstandardized addresses |
| 🏛️ **Hierarchy Traversal** | Navigate parent, children, and ancestors of any admin division |
| 📊 **Pandas Export** | Direct `to_frame()` / `to_dicts()` export from database views |
| ✅ **Address Validation** | `validate()` and `validate_many()` for automated address checking |
| 📅 **Historical Data** | Access previous PSGC releases by date |
| 👩‍💻 **Command Line Interface** | Easy-to-use command line interface |
| 📚 **Multiple Data Models** | Choose the structure that fits your use case |
| 💾 **Smart Caching** | Automatic caching for faster subsequent loads |
| 🧩 **Plug-in System** | Enrich PSGC data with custom extensions via plug-ins |

---

## Installation

```bash
pip install barangay
```

**Requirements:** Python 3.13+

---

## CLI

```bash
# Search for barangays
barangay search "Tongmageng, Tawi-Tawi"

# Export data
barangay export --model flat --format json --output data.json

# Show information
barangay info version
barangay info stats

# Work with historical data
barangay history list-dates
barangay history search-history "Tongmageng" --as-of "2025-07-08"

# Manage cache
barangay cache info
barangay cache clear

# Search with plugin enrichment
barangay search "Tongmageng" --plugin psgc-aux-data --format json

# Export with plugin enrichment
barangay export --model flat --plugin psgc-aux-data --format json --output enriched.json

# Batch operations
barangay batch batch-search queries.txt --limit 5 --output results.json
barangay batch validate barangay_names.txt
```

📖 **Full CLI Reference:** [quarto-docs/reference/cli.qmd](https://bendlikeabamboo.github.io/barangay/reference/cli.html)
📖 **Plugin Guide:** [quarto-docs/plugins/index.qmd](https://bendlikeabamboo.github.io/barangay/plugins/)

---

## Python API

### Database Views

Pre-built views let you browse and search any admin level directly:

```python
from barangay import regions, provinces, municipalities, cities, barangays

print(regions)     # <PSGC region database: 18 records>
print(barangays)   # <PSGC barangay database: 42010 records>

# Look up by name
brgy = barangays.get(name="Tongmageng")
print(brgy.province)  # Tawi-Tawi

# Look up by PSGC ID
brgy = barangays.lookup("1907005010")
print(brgy)  # <barangay: Tongmageng (1907005010)>

# Iterate over records
for region in regions:
    print(region.name)
```

### Hierarchy Traversal

Each record exposes its position in the administrative hierarchy:

```python
brgy = barangays.get(name="Tongmageng")
print(brgy.region)      # Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)
print(brgy.province)    # Tawi-Tawi
print(brgy.municipality)  # Sitangkai
print(brgy.parent)      # <municipality: Sitangkai (1907005000)>
print(brgy.ancestors)   # [<municipality: Sitangkai ...>, <province: Tawi-Tawi ...>, ...]

manila = cities.get(name="City of Manila")
print(manila.children[:2])  # [<submunicipality: Tondo I/II ...>, <submunicipality: Binondo ...>]
```

### Fuzzy Search

```python
from barangay import search_fuzzy

results = search_fuzzy("Tongmagen, Tawi-Tawi", threshold=60.0, limit=5)
for r in results:
    print(f"{r.name} ({r.psgc_id}) — score: {r.score}")
# Tongmageng (1907005010) — score: 100.0
# Tonggosong (1907004005) — score: 84.21
# ...
```

### Address Validation

```python
from barangay import validate, validate_many

v = validate("Tongmageng, Tawi-Tawi")
print(v.valid, v.matched_name, v.score)  # True Tongmageng 100.0

results = validate_many(["Tongmageng, Tawi-Tawi", "Nonexistent Place"])
for r in results:
    print(f"{r.input!r} -> {'valid' if r.valid else 'invalid'}")
```

### Export to Pandas

```python
from barangay import barangays

df = barangays.to_frame()     # pd.DataFrame
data = barangays.to_dicts()   # List[dict]
```

### Data Access (Nested & Flat Models)

```python
from barangay import barangay, barangay_flat, barangay_extended

# Basic nested model (simple lookups)
ncr_cities = list(barangay["National Capital Region (NCR)"].keys())

# Extended model (recursive with metadata)
for region in barangay_extended.components:
    print(f"{region.name} ({region.type})")

# Flat model (search & filtering)
brgy = [loc for loc in barangay_flat if loc.name == "Marayos"][0]
```

### Search (Dict-based)

> **Deprecated:** The `search()` function returns raw dicts and will be removed in 2027.X.X.X. Use [`search_fuzzy()`](#fuzzy-search) instead for typed results.

```python
from barangay import search

# Simple search
results = search("Tongmageng, Tawi-Tawi")

# Custom search
search(
    "Tongmagen, Tawi-Tawi",
    n=4,                    # Number of results
    match_hooks=["municipality", "barangay"],  # Match levels
    threshold=70.0,         # Minimum similarity (0-100)
)
```

### Utilities

```python
from barangay import sanitize_input, resolve_date, get_available_dates, use_version

# Sanitize strings
cleaned = sanitize_input("City of San Jose", exclude=["city of "])
# Result: "san jose"

# Switch to historical data
use_version("2025-07-08")
brgy = barangays.lookup("1907005010")
use_version(None)  # back to latest
```

📖 **Full API Reference:** [quarto-docs/reference/index.qmd](https://bendlikeabamboo.github.io/barangay/reference/)

---

## Configuration

Configure via environment variables:

```bash
export BARANGAY_AS_OF="2025-07-08"      # Default dataset date
export BARANGAY_VERBOSE="true"          # Enable verbose logging
export BARANGAY_CACHE_DIR="/custom/path" # Custom cache directory
```

Or set programmatically:

```python
import barangay
barangay.as_of = "2025-07-08"
```

**Priority:** Function parameter → Module attribute → Environment variable → Default (latest)

📖 **Full Configuration Guide:** [quarto-docs/reference/configuration.qmd](https://bendlikeabamboo.github.io/barangay/reference/configuration.html)

---

## Data Models

Three data structures are available. Choose based on your use case:

| Model | Use Case | Structure |
|-------|----------|-----------|
| [`barangay`](https://bendlikeabamboo.github.io/barangay/api/#barangay-admindiv) | Simple lookups | Nested dictionary (region → city → barangay) |
| [`barangay_extended`](https://bendlikeabamboo.github.io/barangay/api/#barangay_extended-admindivextended) | Complex hierarchies | Recursive with rich metadata |
| [`barangay_flat`](https://bendlikeabamboo.github.io/barangay/api/#barangay_flat-listadmindivflat) | Search & filtering | Flat list with parent references |

**Note:** Pydantic models (`barangay`, `barangay_extended`, `barangay_flat`) are recommended. Dict versions (`BARANGAY`, `BARANGAY_EXTENDED`, `BARANGAY_FLAT`) are available for backward compatibility.

> **Deprecation:** `BARANGAY`, `BARANGAY_EXTENDED`, `BARANGAY_FLAT` dict aliases will be removed in 2027.X.X.X. Use the Database API instead (e.g. `from barangay import barangays; barangays.get(name="Tongmageng")`).

---

## Historical Data

Access previous PSGC releases by date. Data is automatically cached after first download.

**Current Data Version:** `2026-04-13` (April 13 2026 PSGC masterlist)

**Available Dates:**
- Current: `2026-04-13` (bundled)
- Historical: `2026-01-13`, `2025-07-08`, `2025-08-29`, `2025-10-13`

```python
import barangay
print(barangay.current)           # '2026-04-13'
print(barangay.available_dates)   # ['2026-04-13', '2026-01-13', '2025-08-29', '2025-10-13', '2025-07-08']
```

---

## Performance

Fuzzy search is optimized for speed:

| Configuration | Performance |
|---------------|-------------|
| Default (4 hooks) | ~80ms per search |
| Optimized (1–2 hooks) | ~10–25ms per search |

Use fewer `match_hooks` for better performance when appropriate.

---

## Resources

- 📚 [Full Documentation](https://bendlikeabamboo.github.io/barangay/) - Comprehensive guides and API reference
- 📩 [PSGC Source](https://psa.gov.ph/classification/psgc/node/1684083211) - April 2026 masterlist
- 📦 [PyPI Package](https://pypi.org/project/barangay/)
- 💻 [GitHub Repository](https://github.com/bendlikeabamboo/barangay)
- 📊 [Data Repository](https://github.com/bendlikeabamboo/barangay-data-repository) - Raw PSGC datasets (JSON, YAML)
- 🐳 [Barangay-API Docker](https://hub.docker.com/r/bendlikeabamboo/barangay-api) - REST API companion

---

## Contributing

Contributions are welcome! See our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

[MIT](LICENSE) © bendlikeabamboo
