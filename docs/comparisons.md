---
title: "barangay vs psgc-api vs raw PSA CSV — Comparison"
description: "Compare the barangay Python package against psgc-api and raw PSA PSGC CSVs: offline access, fuzzy search, address validation, Python-native data models, and historical versions."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# Comparing PSGC Data Sources

There are several ways to work with Philippine Standard Geographic Code (PSGC)
data. This page compares the **`barangay` Python package** against a hosted
**PSGC HTTP API** (e.g. `psgc-api`) and **raw PSA CSV downloads**.

## At a glance

| Capability | `barangay` package | PSGC HTTP API | Raw PSA CSV |
|------------|:------------------:|:-------------:|:-----------:|
| Works fully **offline** | ✅ | ❌ (network required) | ⚠️ (download once) |
| Bundled, queryable dataset | ✅ 42,011 barangays | ✅ | ❌ (parse yourself) |
| **Fuzzy search** (misspellings) | ✅ built-in | ⚠️ partial/limited | ❌ |
| **Address validation** | ✅ `validate()` / `validate_many()` | ⚠️ build-your-own | ❌ |
| Typed Python data models | ✅ pydantic | ❌ JSON over HTTP | ❌ |
| Pandas export | ✅ `to_frame()` | ⚠️ manual | ⚠️ manual |
| Hierarchy traversal (`parent`, `ancestors`, `children`) | ✅ | ⚠️ | ❌ |
| Historical PSGC versions | ✅ bundled (2023–2026) | ⚠️ varies | ✅ manual |
| CLI included | ✅ | ❌ | ❌ |
| Plugin system (population, income, old names) | ✅ | ❌ | ❌ |
| Rate limits / availability concerns | ✅ none | ⚠️ yes | ✅ none |
| Zero infrastructure | ✅ `pip install` | ❌ host/deploy | ✅ |

## When to choose `barangay`

- You want **offline, in-process** access with no network dependency or rate
  limits — ideal for batch jobs, notebooks, CI, and air-gapped environments.
- You need **fuzzy search** and **address validation** that tolerate
  misspellings, abbreviations, and unstandardized formats.
- You want **typed Python objects** and one-call **pandas** export instead of
  hand-parsing CSVs.

## When an HTTP API may suit you

- Your stack is non-Python and you only need occasional lookups over HTTP.
- You want a thin read-only JSON endpoint and are fine managing latency,
  caching, and rate limits.

## When raw PSA CSVs may suit you

- You need the absolute upstream files for archival or one-off analysis.
- You're comfortable writing your own parser, dedup, and hierarchy logic.

## Quick example: offline fuzzy search

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tongmagen, Tawi-Tawi"):
    print(r.name, r.psgc_id, r.score)
```

No API key, no network — runs entirely from bundled data.

---

Data source: [Philippine Statistics Authority — PSGC](https://psa.gov.ph/classification/psgc/).
See the [full documentation](index.md) for installation, tutorials, and the
plugin system.
