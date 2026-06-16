---
title: "Barangays in City of Ligao, Albay — PSGC Codes"
description: "Complete list of 55 barangays in City of Ligao, Albay with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Ligao, Albay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Ligao, Albay",
  "description": "City in the Philippines with 55 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Albay",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Albay"
  }
}
</script>

City of Ligao is a **city** in Albay (Philippines) with
**55 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abella | 0500508001 |
| Allang | 0500508002 |
| Amtic | 0500508003 |
| Bacong | 0500508004 |
| Bagumbayan | 0500508005 |
| Balanac | 0500508006 |
| Baligang | 0500508007 |
| Barayong | 0500508008 |
| Basag | 0500508009 |
| Batang | 0500508010 |
| Bay | 0500508011 |
| Binanowan | 0500508012 |
| Binatagan | 0500508013 |
| Bobonsuran | 0500508014 |
| Bonga | 0500508015 |
| Busac | 0500508016 |
| Busay | 0500508017 |
| Cabarian | 0500508018 |
| Calzada | 0500508019 |
| Catburawan | 0500508020 |
| Cavasi | 0500508021 |
| Culliat | 0500508022 |
| Dunao | 0500508023 |
| Francia | 0500508024 |
| Guilid | 0500508025 |
| Herrera | 0500508026 |
| Layon | 0500508027 |
| Macalidong | 0500508028 |
| Mahaba | 0500508029 |
| Malama | 0500508030 |
| Maonon | 0500508031 |
| Nabonton | 0500508033 |
| Nasisi | 0500508032 |
| Oma-oma | 0500508034 |
| Palapas | 0500508035 |
| Pandan | 0500508036 |
| Paulba | 0500508037 |
| Paulog | 0500508038 |
| Pinamaniquian | 0500508039 |
| Pinit | 0500508040 |
| Ranao-ranao | 0500508042 |
| San Vicente | 0500508043 |
| Santa Cruz | 0500508044 |
| Tagpo | 0500508045 |
| Tambo | 0500508046 |
| Tandarura | 0500508047 |
| Tastas | 0500508048 |
| Tinago | 0500508049 |
| Tinampo | 0500508050 |
| Tiongson | 0500508051 |
| Tomolin | 0500508052 |
| Tuburan | 0500508053 |
| Tula-tula Grande | 0500508054 |
| Tula-tula Pequeño | 0500508055 |
| Tupas | 0500508056 |

## Look up Ligao with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0500508000") or cities.lookup("0500508000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Ligao

```python
from barangay import search_fuzzy

for r in search_fuzzy("Ligao", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
