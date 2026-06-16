---
title: "barangay — Philippine PSGC Python Package"
description: "Offline Python package for the Philippine Standard Geographic Code (PSGC): 42,011 barangays, municipalities, cities, provinces, and regions with fuzzy search and address validation. No API calls needed."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

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

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Philippine Standard Geographic Code (PSGC) — barangay dataset",
  "description": "Offline Python-accessible dataset of the Philippine Standard Geographic Code (PSGC) covering all 42,011 barangays, 1,488 municipalities, 146 cities, 82 provinces, and 17 regions, with hierarchy relationships and historical snapshots.",
  "keywords": ["PSGC", "Philippines", "barangay", "geographic code", "administrative divisions", "geocoding", "open data"],
  "license": "https://opensource.org/licenses/MIT",
  "isAccessibleForFree": true,
  "creator": {
    "@type": "Organization",
    "name": "Philippine Statistics Authority",
    "url": "https://psa.gov.ph/classification/psgc/"
  },
  "publisher": {
    "@type": "Person",
    "name": "bendlikeabamboo"
  },
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://pypi.org/project/barangay/",
    "encodingFormat": "application/python-package",
    "name": "barangay (PyPI)"
  },
  "temporalCoverage": "2026-04-13",
  "spatialCoverage": {
    "@type": "Place",
    "name": "Republic of the Philippines"
  },
  "inLanguage": "en"
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the PSGC (Philippine Standard Geographic Code)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The PSGC is the official classification system of the Philippine Statistics Authority that assigns a unique 10-digit code to every administrative unit in the Philippines — regions, provinces, cities, municipalities, sub-municipalities, and the country's 42,011 barangays. The barangay package provides offline access to the complete PSGC masterlist."
      }
    },
    {
      "@type": "Question",
      "name": "How do I validate a Philippine address in Python?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Install the barangay package (pip install barangay), then call validate('Tongmageng, Tawi-Tawi'). It returns a ValidationResult with .valid, .matched_name, and a fuzzy .score. Use validate_many() to check addresses in bulk."
      }
    },
    {
      "@type": "Question",
      "name": "Does the barangay package work offline?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The full PSGC dataset is bundled with the package, so all lookups, fuzzy search, validation, and export work without any API calls, database, or internet connection."
      }
    },
    {
      "@type": "Question",
      "name": "Which Python version is required?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Python 3.13 or newer. The package uses modern type hints (PEP 604 unions) and is classified as Programming Language :: Python :: 3 :: Only."
      }
    },
    {
      "@type": "Question",
      "name": "Does it support historical PSGC data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Use use_version('2025-07-08') to switch to a previous PSGC masterlist release. Historical snapshots from 2023 through 2026 are included, and use_version(None) returns to the latest."
      }
    },
    {
      "@type": "Question",
      "name": "How do I fuzzy search barangays with misspellings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Call search_fuzzy('Tongmagen, Tawi-Tawi'). It returns typed SearchResult objects ranked by a fuzzy score using rapidfuzz, tolerant of common misspellings and unstandardized address formats."
      }
    }
  ]
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
#  'region', 'province', 'highly_urbanized_city', 'independent_component_city',
#  'component_city', 'municipality', 'submunicipality',
#  'special_geographic_area', 'barangay']
print(df.shape)  # (42010, 16)
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

!!! warning "Deprecation Notice"
    `BARANGAY`/`BARANGAY_EXTENDED`/`BARANGAY_FLAT` dict aliases and `search()` are deprecated and will be removed in 2027.X.X.X. Use the Database API for new code (e.g. `barangays.get(name="Tongmageng")`, `search_fuzzy("query")`). See the [API Reference](api.md) and [Database API tutorial](tutorials/database_api.md).
