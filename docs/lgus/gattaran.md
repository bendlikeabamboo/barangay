---
title: "Barangays in Gattaran, Cagayan — PSGC Codes"
description: "Complete list of 50 barangays in Gattaran, Cagayan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Gattaran, Cagayan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Gattaran, Cagayan",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cagayan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cagayan"
  }
}
</script>

Gattaran is a **municipality** in Cagayan (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abra | 0201513001 |
| Aguiguican | 0201513005 |
| Bangatan Ngagan | 0201513006 |
| Baracaoit | 0201513007 |
| Baraoidan | 0201513008 |
| Barbarit | 0201513009 |
| Basao | 0201513010 |
| Bolos Point | 0201513056 |
| Cabayu | 0201513011 |
| Calaoagan Bassit | 0201513012 |
| Calaoagan Dackel | 0201513013 |
| Capiddigan | 0201513014 |
| Capissayan Norte | 0201513015 |
| Capissayan Sur | 0201513016 |
| Casicallan Norte | 0201513019 |
| Casicallan Sur | 0201513018 |
| Centro Norte | 0201513020 |
| Centro Sur | 0201513021 |
| Cullit | 0201513022 |
| Cumao | 0201513023 |
| Cunig | 0201513024 |
| Dummun | 0201513025 |
| Fugu | 0201513026 |
| Ganzano | 0201513027 |
| Guising | 0201513028 |
| L. Adviento | 0201513031 |
| Langgan | 0201513029 |
| Lapogan | 0201513030 |
| Mabuno | 0201513033 |
| Nabaccayan | 0201513035 |
| Naddungan | 0201513036 |
| Nagatutuan | 0201513037 |
| Nassiping | 0201513038 |
| Newagac | 0201513039 |
| Palagao Norte | 0201513040 |
| Palagao Sur | 0201513041 |
| Piña Este | 0201513042 |
| Piña Weste | 0201513043 |
| San Carlos | 0201513057 |
| San Vicente | 0201513044 |
| Santa Maria | 0201513045 |
| Sidem | 0201513046 |
| Sta. Ana | 0201513047 |
| T. Elizaga | 0201513052 |
| Tagumay | 0201513048 |
| Takiki | 0201513049 |
| Taligan | 0201513050 |
| Tanglagan | 0201513051 |
| Tubungan Este | 0201513053 |
| Tubungan Weste | 0201513054 |

## Look up Gattaran with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0201513000") or cities.lookup("0201513000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Gattaran

```python
from barangay import search_fuzzy

for r in search_fuzzy("Gattaran", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
