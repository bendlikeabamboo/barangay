---
title: "Barangays in City of Cavite, Cavite — PSGC Codes"
description: "Complete list of 84 barangays in City of Cavite, Cavite with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Cavite, Cavite

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Cavite, Cavite",
  "description": "City in the Philippines with 84 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cavite",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cavite"
  }
}
</script>

City of Cavite is a **city** in Cavite (Philippines) with
**84 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Barangay 1 | 0402105001 |
| Barangay 10 | 0402105002 |
| Barangay 10-A | 0402105063 |
| Barangay 10-B | 0402105064 |
| Barangay 11 | 0402105004 |
| Barangay 12 | 0402105005 |
| Barangay 13 | 0402105006 |
| Barangay 14 | 0402105007 |
| Barangay 15 | 0402105008 |
| Barangay 16 | 0402105009 |
| Barangay 17 | 0402105010 |
| Barangay 18 | 0402105011 |
| Barangay 19 | 0402105012 |
| Barangay 2 | 0402105003 |
| Barangay 20 | 0402105013 |
| Barangay 21 | 0402105014 |
| Barangay 22 | 0402105015 |
| Barangay 22-A | 0402105065 |
| Barangay 23 | 0402105016 |
| Barangay 24 | 0402105017 |
| Barangay 25 | 0402105018 |
| Barangay 26 | 0402105019 |
| Barangay 27 | 0402105020 |
| Barangay 28 | 0402105021 |
| Barangay 29 | 0402105022 |
| Barangay 29-A | 0402105066 |
| Barangay 3 | 0402105023 |
| Barangay 30 | 0402105024 |
| Barangay 31 | 0402105025 |
| Barangay 32 | 0402105026 |
| Barangay 33 | 0402105027 |
| Barangay 34 | 0402105028 |
| Barangay 35 | 0402105029 |
| Barangay 36 | 0402105030 |
| Barangay 36-A | 0402105067 |
| Barangay 37 | 0402105031 |
| Barangay 37-A | 0402105068 |
| Barangay 38 | 0402105032 |
| Barangay 38-A | 0402105069 |
| Barangay 39 | 0402105033 |
| Barangay 4 | 0402105034 |
| Barangay 40 | 0402105035 |
| Barangay 41 | 0402105036 |
| Barangay 42 | 0402105037 |
| Barangay 42-A | 0402105070 |
| Barangay 42-B | 0402105071 |
| Barangay 42-C | 0402105072 |
| Barangay 43 | 0402105038 |
| Barangay 44 | 0402105039 |
| Barangay 45 | 0402105040 |
| Barangay 45-A | 0402105073 |
| Barangay 46 | 0402105041 |
| Barangay 47 | 0402105042 |
| Barangay 47-A | 0402105074 |
| Barangay 47-B | 0402105075 |
| Barangay 48 | 0402105043 |
| Barangay 48-A | 0402105076 |
| Barangay 49 | 0402105044 |
| Barangay 49-A | 0402105077 |
| Barangay 5 | 0402105045 |
| Barangay 50 | 0402105046 |
| Barangay 51 | 0402105047 |
| Barangay 52 | 0402105048 |
| Barangay 53 | 0402105049 |
| Barangay 53-A | 0402105078 |
| Barangay 53-B | 0402105079 |
| Barangay 54 | 0402105050 |
| Barangay 54-A | 0402105080 |
| Barangay 55 | 0402105051 |
| Barangay 56 | 0402105052 |
| Barangay 57 | 0402105053 |
| Barangay 58 | 0402105054 |
| Barangay 58-A | 0402105081 |
| Barangay 59 | 0402105055 |
| Barangay 6 | 0402105056 |
| Barangay 60 | 0402105057 |
| Barangay 61 | 0402105058 |
| Barangay 61-A | 0402105082 |
| Barangay 62 | 0402105059 |
| Barangay 62-A | 0402105083 |
| Barangay 62-B | 0402105084 |
| Barangay 7 | 0402105060 |
| Barangay 8 | 0402105061 |
| Barangay 9 | 0402105062 |

## Look up Cavite with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0402105000") or cities.lookup("0402105000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Cavite

```python
from barangay import search_fuzzy

for r in search_fuzzy("Cavite", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
