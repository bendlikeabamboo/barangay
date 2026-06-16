---
title: "Barangays in Pilar, Sorsogon — PSGC Codes"
description: "Complete list of 49 barangays in Pilar, Sorsogon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Pilar, Sorsogon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Pilar, Sorsogon",
  "description": "Municipality in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Sorsogon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Sorsogon"
  }
}
</script>

Pilar is a **municipality** in Sorsogon (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abas | 0506213001 |
| Abucay | 0506213002 |
| Bantayan | 0506213003 |
| Banuyo | 0506213004 |
| Bayasong | 0506213005 |
| Bayawas | 0506213006 |
| Binanuahan | 0506213007 |
| Cabiguan | 0506213009 |
| Cagdongon | 0506213010 |
| Calongay | 0506213011 |
| Calpi | 0506213012 |
| Catamlangan | 0506213013 |
| Comapo-capo | 0506213014 |
| Danlog | 0506213015 |
| Dao | 0506213016 |
| Dapdap | 0506213017 |
| Del Rosario | 0506213018 |
| Esmerada | 0506213019 |
| Esperanza | 0506213020 |
| Ginablan | 0506213022 |
| Guiron | 0506213021 |
| Inang | 0506213023 |
| Inapugan | 0506213024 |
| Leona | 0506213026 |
| Lipason | 0506213027 |
| Lourdes | 0506213028 |
| Lubiano | 0506213025 |
| Lumbang | 0506213030 |
| Lungib | 0506213029 |
| Mabanate | 0506213031 |
| Malbog | 0506213032 |
| Marifosque | 0506213033 |
| Mercedes | 0506213034 |
| Migabod | 0506213035 |
| Naspi | 0506213036 |
| Palanas | 0506213037 |
| Pangpang | 0506213038 |
| Pinagsalog | 0506213039 |
| Pineda | 0506213040 |
| Poctol | 0506213042 |
| Pudo | 0506213043 |
| Putiao | 0506213044 |
| Sacnangan | 0506213045 |
| Salvacion | 0506213046 |
| San Antonio (Millabas) | 0506213047 |
| San Antonio (Sapa) | 0506213048 |
| San Jose | 0506213049 |
| San Rafael | 0506213050 |
| Santa Fe | 0506213051 |

## Look up Pilar with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0506213000") or cities.lookup("0506213000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Pilar

```python
from barangay import search_fuzzy

for r in search_fuzzy("Pilar", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
