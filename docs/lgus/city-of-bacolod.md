---
title: "Barangays in City of Bacolod, Negros Island Region (NIR) — PSGC Codes"
description: "Complete list of 61 barangays in City of Bacolod, Negros Island Region (NIR) with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Bacolod, Negros Island Region (NIR)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Bacolod, Negros Island Region (NIR)",
  "description": "City in the Philippines with 61 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Negros Island Region (NIR)",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Negros Island Region (NIR)"
  }
}
</script>

City of Bacolod is a **city** in Negros Island Region (NIR) (Philippines) with
**61 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alangilan | 1830200001 |
| Alijis | 1830200002 |
| Banago | 1830200003 |
| Barangay 1 | 1830200004 |
| Barangay 10 | 1830200005 |
| Barangay 11 | 1830200006 |
| Barangay 12 | 1830200007 |
| Barangay 13 | 1830200008 |
| Barangay 14 | 1830200009 |
| Barangay 15 | 1830200010 |
| Barangay 16 | 1830200011 |
| Barangay 17 | 1830200012 |
| Barangay 18 | 1830200013 |
| Barangay 19 | 1830200014 |
| Barangay 2 | 1830200015 |
| Barangay 20 | 1830200016 |
| Barangay 21 | 1830200017 |
| Barangay 22 | 1830200018 |
| Barangay 23 | 1830200019 |
| Barangay 24 | 1830200020 |
| Barangay 25 | 1830200021 |
| Barangay 26 | 1830200022 |
| Barangay 27 | 1830200023 |
| Barangay 28 | 1830200024 |
| Barangay 29 | 1830200025 |
| Barangay 3 | 1830200026 |
| Barangay 30 | 1830200027 |
| Barangay 31 | 1830200028 |
| Barangay 32 | 1830200029 |
| Barangay 33 | 1830200030 |
| Barangay 34 | 1830200031 |
| Barangay 35 | 1830200032 |
| Barangay 36 | 1830200033 |
| Barangay 37 | 1830200034 |
| Barangay 38 | 1830200035 |
| Barangay 39 | 1830200036 |
| Barangay 4 | 1830200037 |
| Barangay 40 | 1830200038 |
| Barangay 41 | 1830200039 |
| Barangay 5 | 1830200040 |
| Barangay 6 | 1830200041 |
| Barangay 7 | 1830200042 |
| Barangay 8 | 1830200043 |
| Barangay 9 | 1830200044 |
| Bata | 1830200045 |
| Cabug | 1830200046 |
| Estefania | 1830200047 |
| Felisa | 1830200048 |
| Granada | 1830200049 |
| Handumanan | 1830200061 |
| Mandalagan | 1830200050 |
| Mansilingan | 1830200051 |
| Montevista | 1830200052 |
| Pahanocoy | 1830200053 |
| Punta Taytay | 1830200054 |
| Singcang-Airport | 1830200055 |
| Sum-ag | 1830200056 |
| Taculing | 1830200057 |
| Tangub | 1830200058 |
| Villamonte | 1830200059 |
| Vista Alegre | 1830200060 |

## Look up Bacolod with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1830200000") or cities.lookup("1830200000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Bacolod

```python
from barangay import search_fuzzy

for r in search_fuzzy("Bacolod", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
