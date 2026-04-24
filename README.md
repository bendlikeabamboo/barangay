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
from barangay import search

# Find barangays with fuzzy matching
results = search("Tongmageng, Tawi-Tawi")
print(results[0]['barangay'])  # Tongmageng
```

---

## Features

| Feature | Description |
|---------|-------------|
| 🔍 **Fuzzy Search** | Fast, customizable matching for unstandardized addresses |
| 📅 **Historical Data** | Access previous PSGC releases by date |
| 👩‍💻 **Command Line Interface** | Easy-to-use command line interface |
| 📚 **Multiple Data Models** | Choose the structure that fits your use case |
| 💾 **Smart Caching** | Automatic caching for faster subsequent loads |
| 📦 **Ready-to-Use** | JSON, YAML, and Python dictionary formats included |

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

# Batch operations
barangay batch batch-search queries.txt --limit 5 --output results.json
barangay batch validate barangay_names.txt
```

📖 **Full CLI Reference:** [docs/cli.md](https://bendlikeabamboo.github.io/barangay/cli/)

---

## Python API

### Fuzzy Search

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

# Historical data
search("Tongmageng", as_of="2025-07-08")
```

### Data Access

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

### Utilities

```python
from barangay import sanitize_input, resolve_date, get_available_dates

# Sanitize strings
cleaned = sanitize_input("City of San Jose", exclude=["city of "])
# Result: "san jose"

# Resolve to closest available date
resolved_date, status = resolve_date("2025-07-01", get_available_dates(), "2026-04-13")
# Result: '2025-07-08'

# Get all available dates
dates = get_available_dates()
# ['2026-04-13', '2026-01-13', '2025-08-29', '2025-10-13', '2025-07-08']
```

📖 **Full API Reference:** [docs/api.md](https://bendlikeabamboo.github.io/barangay/api/)

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

📖 **Full Configuration Guide:** [docs/configuration.md](https://bendlikeabamboo.github.io/barangay/configuration/)

---

## Data Models

Three data structures are available. Choose based on your use case:

| Model | Use Case | Structure |
|-------|----------|-----------|
| [`barangay`](https://bendlikeabamboo.github.io/barangay/api/#barangay-admindiv) | Simple lookups | Nested dictionary (region → city → barangay) |
| [`barangay_extended`](https://bendlikeabamboo.github.io/barangay/api/#barangay_extended-admindivextended) | Complex hierarchies | Recursive with rich metadata |
| [`barangay_flat`](https://bendlikeabamboo.github.io/barangay/api/#barangay_flat-listadmindivflat) | Search & filtering | Flat list with parent references |

**Note:** Pydantic models (`barangay`, `barangay_extended`, `barangay_flat`) are recommended. Dict versions (`BARANGAY`, `BARANGAY_EXTENDED`, `BARANGAY_FLAT`) are available for backward compatibility.

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
| Default (3 hooks) | ~80ms per search |
| Optimized (2 hooks) | ~25ms per search |

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
