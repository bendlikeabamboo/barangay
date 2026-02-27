# 🇵🇭 barangay

[![PyPI version](https://img.shields.io/pypi/v/barangay.svg)](https://pypi.org/project/barangay/)
[![PyPI Downloads](https://static.pepy.tech/badge/barangay)](https://pepy.tech/projects/barangay)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml/badge.svg)](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml)
[![Visit the Docs](https://img.shields.io/badge/Visit%20the%20Docs-red)](https://bendlikeabamboo.github.io/barangay/)

Philippine geographic data with fuzzy search. Based on the January 2026 PSGC masterlist.

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

## Table of Contents

- [🇵🇭 barangay](#-barangay)
  - [Quick Start](#quick-start)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Fuzzy Search](#fuzzy-search)
    - [Basic Usage](#basic-usage)
    - [Custom Search](#custom-search)
    - [Parameters](#parameters)
    - [Match Hooks](#match-hooks)
  - [Data Models](#data-models)
    - [BARANGAY](#barangay)
    - [BARANGAY\_EXTENDED](#barangay_extended)
    - [BARANGAY\_FLAT](#barangay_flat)
  - [Historical Data](#historical-data)
    - [Available Dates](#available-dates)
    - [Module Attributes](#module-attributes)
  - [Performance](#performance)
  - [Resources](#resources)
  - [Contributing](#contributing)
  - [License](#license)

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

**Requirements:** Python 3.10+

---

## Fuzzy Search

The `search()` function performs fuzzy string matching across administrative levels.

### Basic Usage

```python
from barangay import search

# Simple search
search("Tongmageng, Tawi-Tawi")
```

### Custom Search

```python
from barangay import search

search(
    "Tongmagen, Tawi-Tawi",
    n=4,                    # Number of results
    match_hooks=["municipality", "barangay"],  # Match levels
    threshold=70.0,         # Minimum similarity (0-100)
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `search_string` | `str` | — | Text to search for |
| `n` | `int` | `5` | Maximum results to return |
| `match_hooks` | `list` | `["province", "municipality", "barangay"]` | Administrative levels to match |
| `threshold` | `float` | `60.0` | Minimum similarity score (0-100) |
| `as_of` | `str \| None` | `None` | Date for historical data (YYYY-MM-DD) |

### Match Hooks

Choose which administrative levels to include in matching:

- `"barangay"` - Barangay names only
- `"municipality"` - Municipality/city names
- `"province"` - Province/HUC names

Combine any of these options. Fewer hooks = faster performance.

---

## Data Models

Three data structures are available. Choose based on your use case:

| Model | Use Case | Structure |
|-------|----------|-----------|
| [`BARANGAY`](#barangay) | Simple lookups | Nested dictionary (region → city → barangay) |
| [`BARANGAY_EXTENDED`](#barangay_extended) | Complex hierarchies | Recursive with rich metadata |
| [`BARANGAY_FLAT`](#barangay_flat) | Search & filtering | Flat list with parent references |

### BARANGAY

Simple nested dictionary. Best for straightforward lookups.

```python
from barangay import BARANGAY

# Access NCR cities
ncr_cities = list(BARANGAY["National Capital Region (NCR)"].keys())

# Access Manila barangays
manila_brgys = BARANGAY["National Capital Region (NCR)"]["City of Manila"]["Binondo"]
```

### BARANGAY_EXTENDED

Metadata-rich recursive model. Handles complex hierarchies (e.g., HUCs, municipalities directly under regions).

```python
from barangay import BARANGAY_EXTENDED

# Get NCR components
ncr = [item for item in BARANGAY_EXTENDED["components"]
       if item["name"] == "National Capital Region (NCR)"][0]

# List all NCR cities/municipalities with types
for component in ncr["components"]:
    print(f"{component['name']} ({component['type']})")
```

### BARANGAY_FLAT

Flat list with parent references. Ideal for search, filtering, and DataFrame operations.

```python
from barangay import BARANGAY_FLAT

# Find a specific barangay
brgy = [loc for loc in BARANGAY_FLAT if loc["name"] == "Marayos"][0]

# Trace hierarchy using parent_psgc_id
parent = [loc for loc in BARANGAY_FLAT
          if loc["psgc_id"] == brgy["parent_psgc_id"]][0]
```

---

## Historical Data

Access previous PSGC releases by date. Data is automatically cached after first download.

```python
from barangay import search

# Search using data from a specific date
search("Tongmageng", as_of="2025-07-08")
```

### Available Dates

- Current: `2026-01-13` (bundled)
- Historical: `2025-07-08`, `2025-08-29`, `2025-10-13`

### Module Attributes

```python
from barangay import current, available_dates, as_of

print(current)           # '2026-01-13'
print(available_dates)   # ['2025-07-08', '2025-08-29', '2025-10-13']
print(as_of)             # None (uses latest)
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
- 🐳 [Barangay-API Docker](https://hub.docker.com/r/bendlikeabamboo/barangay-api) - REST API companion

---

## Contributing

Contributions are welcome! See our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

[MIT](LICENSE) © bendlikeabamboo

---
