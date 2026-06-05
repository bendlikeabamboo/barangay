# barangay — Philippine Geographic Data Python Package

> Python package for accessing Philippine Standard Geographic Code (PSGC)
> data covering all 42,011 barangays, 1,488 municipalities, 146 cities,
> 82 provinces, and 17 regions — offline, no API calls needed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "barangay",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "programmingLanguage": "Python",
  "description": "Philippine Standard Geographic Code (PSGC) Python package with fuzzy search for barangays, municipalities, cities, provinces, and regions.",
  "installUrl": "https://pypi.org/project/barangay/",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "howTo": {
    "@type": "HowTo",
    "name": "Install and search Philippine barangays with Python",
    "step": [
      {
        "@type": "HowToStep",
        "text": "Install the package: pip install barangay"
      },
      {
        "@type": "HowToStep",
        "text": "Search for a barangay: from barangay import search_fuzzy; search_fuzzy('Tongmageng, Tawi-Tawi')"
      }
    ]
  }
}
</script>

<div style="display: flex; flex-direction: row; align-items: center; gap: 8px;">
<a href="https://pypi.org/project/barangay/">
    <img src="https://img.shields.io/pypi/v/barangay.svg" alt="PyPI version">
</a>
<a href="https://pepy.tech/projects/barangay">
    <img src="https://static.pepy.tech/badge/barangay" alt="PyPI Downloads">
</a>
<a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</a>
<a href="https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml">
    <img src="https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml/badge.svg" alt="Release Badge">
</a>
</div>

## Features

- **Bundled PSGC Dataset**: Native access to PSGC data, no database or API calls needed
- **Hierarchy Traversal**: Navigate parent, children, and ancestors of any admin division
- **Direct Pandas Export**: `to_frame()` and `to_dicts()` for immediate DataFrame access
- **Address Validation**: `validate()` and `validate_many()` for automated address checking
- **Fuzzy Search**: Fast, customizable fuzzy matching with typed `SearchResult` objects
- **Historical PSGC Data**: On-demand access to previous PSGC releases by date
- **Multiple Data Models**: Basic (nested), Extended (recursive), and Flat (list)
- **Plug-in System**: Enrich PSGC data with custom extensions via plug-ins (CSV, JSON, Parquet)

## Installation

```bash
pip install barangay
```

## Quick Start

```python
from barangay import barangays, search_fuzzy

# Browse all barangays
print(barangays)  # <PSGC barangay database: 42010 records>

# Get a specific barangay and traverse its hierarchy
brgy = barangays.get(name="Tongmageng")
print(brgy.region)    # Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)
print(brgy.province)  # Tawi-Tawi
print(brgy.psgc_id)   # 1907005010

# Fuzzy search with typed results
for r in search_fuzzy("Tongmagen, Tawi-Tawi"):
    print(f"{r.name} ({r.psgc_id}) — score: {r.score}")
```

## Explore Data

### Pandas Export

```python
from barangay import barangays

df = barangays.to_frame()
print(df.columns.tolist())
# ['name', 'type', 'psgc_id', 'parent_psgc_id', 'nicknames', 'extensions',
#  'region', 'province', 'municipality', 'city']
print(df.shape)  # (42010, 10)
```

### Hierarchy Traversal

```python
brgy = barangays.get(name="Tongmageng")
print(brgy.parent)     # <municipality: Sitangkai (1907005000)>
print(brgy.ancestors)  # [municipality, province, region]

manila = cities.get(name="City of Manila")
for child in manila.children[:3]:
    print(child)  # <submunicipality: Tondo I/II ...>, <submunicipality: Binondo ...>, ...
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

### CLI Usage

#### Search
```sh
# Search
barangay search "Tongmageng, Tawi-Tawi"
```
Output:

| Barangay | Municipality/City | Province/HUC | PSGC ID | Score |
|----------|-------------------|--------------|---------|-------|
| Tongmageng | Sitangkai | Tawi-Tawi | 1907005010 | 100.0 |
| Tonggosong | Simunul | Tawi-Tawi | 1907004005 | 84.2 |
| Tongbangkaw | Tandubas | Tawi-Tawi | 1907007042 | 82.1 |
| Tongusong | Sitangkai | Tawi-Tawi | 1907005012 | 81.1 |
| Tongehat | Sibutu | Tawi-Tawi | 1907011014 | 77.8 |

**Note:** The `Score` column shows the maximum score across all matching patterns (barangay only, province+barangay, municipality+barangay, province+municipality+barangay).


#### Export data
```sh
barangay export --model flat --format json --output data.json
```
#### Show info
```sh
barangay info version
```

Output:
```txt
Current version: 2026-04-13
Available dates: 2023-01-25, 2023-04-18, 2023-08-15, 2023-10-24, 2024-01-23, 2024-04-23, 2024-05-08, 2024-07-12, 2024-10-18, 2025-01-30, 2025-04-23, 2025-07-08, 2025-08-29, 2025-10-13, 2026-01-13, 2026-04-13
```

```sh
barangay info stats
```
Output:

| Model | Barangay Count |
|-------|----------------|
| Basic (nested) | 42011 |
| Flat (list) | 42011 |
| Extended (recursive) | 42011 |

## Data Version

Current data version: [**2026-04-13** (April 13 2026 PSGC masterlist)](https://psa.gov.ph/classification/psgc/node/1684083211)

## Documentation

- [Getting Started](tutorials/database_api.md) — Database API tutorial
- [API Reference](api.md)
- [CLI Reference](cli.md)
- [Configuration](configuration.md)
- [Plugins](plugins/index.md)
- [Contributing](contributing/index.md)
