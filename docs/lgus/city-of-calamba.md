---
title: "Barangays in City of Calamba, Laguna — PSGC Codes"
description: "Complete list of 54 barangays in City of Calamba, Laguna with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Calamba, Laguna

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Calamba, Laguna",
  "description": "City in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Laguna",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Laguna"
  }
}
</script>

City of Calamba is a **city** in Laguna (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Bagong Kalsada | 0403405001 |
| Banadero | 0403405002 |
| Banlic | 0403405003 |
| Barandal | 0403405004 |
| Barangay 1 | 0403405038 |
| Barangay 2 | 0403405039 |
| Barangay 3 | 0403405040 |
| Barangay 4 | 0403405041 |
| Barangay 5 | 0403405042 |
| Barangay 6 | 0403405043 |
| Barangay 7 | 0403405044 |
| Batino | 0403405061 |
| Bubuyan | 0403405005 |
| Bucal | 0403405006 |
| Bunggo | 0403405007 |
| Burol | 0403405009 |
| Camaligan | 0403405010 |
| Canlubang | 0403405011 |
| Halang | 0403405013 |
| Hornalan | 0403405014 |
| Kay-Anlog | 0403405016 |
| La Mesa | 0403405018 |
| Laguerta | 0403405017 |
| Lawa | 0403405019 |
| Lecheria | 0403405020 |
| Lingga | 0403405021 |
| Looc | 0403405023 |
| Mabato | 0403405024 |
| Majada Labas | 0403405062 |
| Makiling | 0403405026 |
| Mapagong | 0403405028 |
| Masili | 0403405029 |
| Maunong | 0403405031 |
| Mayapa | 0403405032 |
| Milagrosa | 0403405057 |
| Paciano Rizal | 0403405033 |
| Palingon | 0403405034 |
| Palo-Alto | 0403405035 |
| Pansol | 0403405036 |
| Parian | 0403405037 |
| Prinza | 0403405045 |
| Punta | 0403405046 |
| Puting Lupa | 0403405047 |
| Real | 0403405049 |
| Saimsim | 0403405051 |
| Sampiruhan | 0403405052 |
| San Cristobal | 0403405053 |
| San Jose | 0403405054 |
| San Juan | 0403405055 |
| Sirang Lupa | 0403405056 |
| Sucol | 0403405050 |
| Turbina | 0403405058 |
| Ulango | 0403405059 |
| Uwisan | 0403405060 |

## Look up Calamba with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0403405000") or cities.lookup("0403405000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Calamba

```python
from barangay import search_fuzzy

for r in search_fuzzy("Calamba", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
