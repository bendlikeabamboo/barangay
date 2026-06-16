---
title: "Barangays in Sipocot, Camarines Sur — PSGC Codes"
description: "Complete list of 46 barangays in Sipocot, Camarines Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Sipocot, Camarines Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Sipocot, Camarines Sur",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Camarines Sur",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Camarines Sur"
  }
}
</script>

Sipocot is a **municipality** in Camarines Sur (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aldezar | 0501734001 |
| Alteza | 0501734002 |
| Anib | 0501734003 |
| Awayan | 0501734004 |
| Azucena | 0501734005 |
| Bagong Sirang | 0501734006 |
| Binahian | 0501734007 |
| Bolo Norte | 0501734009 |
| Bolo Sur | 0501734008 |
| Bulan | 0501734010 |
| Bulawan | 0501734011 |
| Cabuyao | 0501734012 |
| Caima | 0501734013 |
| Calagbangan | 0501734014 |
| Calampinay | 0501734015 |
| Carayrayan | 0501734016 |
| Cotmo | 0501734017 |
| Gabi | 0501734018 |
| Gaongan | 0501734019 |
| Impig | 0501734020 |
| Lipilip | 0501734021 |
| Lubigan Jr. | 0501734022 |
| Lubigan Sr. | 0501734023 |
| Malaguico | 0501734024 |
| Malubago | 0501734025 |
| Manangle | 0501734026 |
| Mangapo | 0501734028 |
| Mangga | 0501734027 |
| Manlubang | 0501734029 |
| Mantila | 0501734030 |
| North Centro | 0501734031 |
| North Villazar | 0501734032 |
| Sagrada Familia | 0501734034 |
| Salanda | 0501734035 |
| Salvacion | 0501734036 |
| San Isidro | 0501734037 |
| San Vicente | 0501734038 |
| Serranzana | 0501734039 |
| South Centro | 0501734040 |
| South Villazar | 0501734041 |
| Taisan | 0501734042 |
| Tara | 0501734043 |
| Tible | 0501734044 |
| Tula-tula | 0501734045 |
| Vigaan | 0501734046 |
| Yabo | 0501734048 |

## Look up Sipocot with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0501734000") or cities.lookup("0501734000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Sipocot

```python
from barangay import search_fuzzy

for r in search_fuzzy("Sipocot", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
