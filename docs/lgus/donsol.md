---
title: "Barangays in Donsol, Sorsogon — PSGC Codes"
description: "Complete list of 51 barangays in Donsol, Sorsogon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Donsol, Sorsogon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Donsol, Sorsogon",
  "description": "Municipality in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Donsol is a **municipality** in Sorsogon (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alin | 0506207001 |
| Awai | 0506207002 |
| Banban | 0506207003 |
| Bandi | 0506207004 |
| Banuang Gurang | 0506207005 |
| Baras | 0506207006 |
| Bayawas | 0506207007 |
| Bororan Barangay 1 | 0506207008 |
| Cabugao | 0506207009 |
| Central Barangay 2 | 0506207010 |
| Cristo | 0506207011 |
| Dancalan | 0506207012 |
| De Vera | 0506207013 |
| Gimagaan | 0506207014 |
| Girawan | 0506207015 |
| Gogon | 0506207016 |
| Gura | 0506207017 |
| Juan Adre | 0506207018 |
| Lourdes | 0506207019 |
| Mabini | 0506207020 |
| Malapoc | 0506207021 |
| Malinao | 0506207022 |
| Market Site Barangay 3 | 0506207023 |
| New Maguisa | 0506207024 |
| Ogod | 0506207025 |
| Old Maguisa | 0506207026 |
| Orange | 0506207027 |
| Pangpang | 0506207028 |
| Parina | 0506207029 |
| Pawala | 0506207030 |
| Pinamanaan | 0506207031 |
| Poso Pob. | 0506207032 |
| Punta Waling-Waling Pob. | 0506207033 |
| Rawis | 0506207034 |
| San Antonio | 0506207035 |
| San Isidro | 0506207036 |
| San Jose | 0506207037 |
| San Rafael | 0506207038 |
| San Ramon | 0506207039 |
| San Vicente | 0506207040 |
| Santa Cruz | 0506207041 |
| Sevilla | 0506207042 |
| Sibago | 0506207043 |
| Suguian | 0506207044 |
| Tagbac | 0506207045 |
| Tinanogan | 0506207046 |
| Tongdol | 0506207047 |
| Tres Marias | 0506207048 |
| Tuba | 0506207049 |
| Tupas | 0506207050 |
| Vinisitahan | 0506207051 |

## Look up Donsol with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0506207000") or cities.lookup("0506207000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Donsol

```python
from barangay import search_fuzzy

for r in search_fuzzy("Donsol", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
