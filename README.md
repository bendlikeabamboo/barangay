# 🇵🇭 barangay

[![PyPI version](https://img.shields.io/pypi/v/barangay.svg)](https://pypi.org/project/barangay/)
[![PyPI Downloads](https://static.pepy.tech/badge/barangay)](https://pepy.tech/projects/barangay)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml/badge.svg)](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml)
[![Visit the Docs](https://img.shields.io/badge/Visit%20the%20Docs-red)](https://bendlikeabamboo.github.io/barangay/)

Philippine geographic data with fuzzy search. Based on the April 2026 PSGC masterlist.

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
- 📩 [PSGC Source](https://psa.gov.ph/classification/psgc/node/1684082306) - January 2026 masterlist
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
