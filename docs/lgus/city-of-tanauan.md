---
title: "Barangays in City of Tanauan, Batangas — PSGC Codes"
description: "Complete list of 48 barangays in City of Tanauan, Batangas with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Tanauan, Batangas

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Tanauan, Batangas",
  "description": "City in the Philippines with 48 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Batangas",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Batangas"
  }
}
</script>

City of Tanauan is a **city** in Batangas (Philippines) with
**48 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Altura Bata | 0401031001 |
| Altura Matanda | 0401031002 |
| Altura-South | 0401031003 |
| Ambulong | 0401031004 |
| Bagbag | 0401031006 |
| Bagumbayan | 0401031007 |
| Balele | 0401031008 |
| Banadero | 0401031005 |
| Banjo East | 0401031010 |
| Banjo Laurel | 0401031011 |
| Bilog-bilog | 0401031013 |
| Boot | 0401031014 |
| Cale | 0401031015 |
| Darasa | 0401031016 |
| Gonzales | 0401031018 |
| Hidalgo | 0401031019 |
| Janopol | 0401031020 |
| Janopol Oriental | 0401031021 |
| Laurel | 0401031022 |
| Luyos | 0401031023 |
| Mabini | 0401031024 |
| Malaking Pulo | 0401031025 |
| Maria Paz | 0401031026 |
| Maugat | 0401031027 |
| Montaña | 0401031028 |
| Natatas | 0401031029 |
| Pagaspas | 0401031017 |
| Pantay Bata | 0401031031 |
| Pantay Matanda | 0401031030 |
| Poblacion Barangay 1 | 0401031032 |
| Poblacion Barangay 2 | 0401031033 |
| Poblacion Barangay 3 | 0401031034 |
| Poblacion Barangay 4 | 0401031035 |
| Poblacion Barangay 5 | 0401031036 |
| Poblacion Barangay 6 | 0401031037 |
| Poblacion Barangay 7 | 0401031038 |
| Sala | 0401031039 |
| Sambat | 0401031040 |
| San Jose | 0401031041 |
| Santol | 0401031042 |
| Santor | 0401031043 |
| Sulpoc | 0401031044 |
| Suplang | 0401031045 |
| Talaga | 0401031046 |
| Tinurik | 0401031047 |
| Trapiche | 0401031048 |
| Ulango | 0401031049 |
| Wawa | 0401031050 |

## Look up Tanauan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0401031000") or cities.lookup("0401031000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tanauan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tanauan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
