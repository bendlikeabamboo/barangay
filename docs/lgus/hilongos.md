---
title: "Barangays in Hilongos, Leyte — PSGC Codes"
description: "Complete list of 51 barangays in Hilongos, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Hilongos, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Hilongos, Leyte",
  "description": "Municipality in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Leyte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Leyte"
  }
}
</script>

Hilongos is a **municipality** in Leyte (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agutayan | 0803719001 |
| Atabay | 0803719002 |
| Baas | 0803719003 |
| Bagong Lipunan | 0803719049 |
| Bagumbayan | 0803719004 |
| Baliw | 0803719005 |
| Bantigue | 0803719006 |
| Bon-ot | 0803719050 |
| Bung-aw | 0803719007 |
| Cacao | 0803719008 |
| Campina | 0803719009 |
| Catandog 1 | 0803719010 |
| Catandog 2 | 0803719011 |
| Central Barangay | 0803719028 |
| Concepcion | 0803719012 |
| Eastern Barangay | 0803719029 |
| Hampangan | 0803719051 |
| Himo-aw | 0803719014 |
| Hitudpan | 0803719015 |
| Imelda Marcos | 0803719016 |
| Kang-iras | 0803719017 |
| Kangha-as | 0803719052 |
| Lamak | 0803719018 |
| Libertad | 0803719019 |
| Liberty | 0803719020 |
| Lunang | 0803719021 |
| Magnangoy | 0803719022 |
| Manaul | 0803719053 |
| Marangog | 0803719023 |
| Matapay | 0803719024 |
| Naval | 0803719025 |
| Owak | 0803719026 |
| Pa-a | 0803719027 |
| Pontod | 0803719031 |
| Proteccion | 0803719032 |
| San Agustin | 0803719033 |
| San Antonio | 0803719034 |
| San Isidro | 0803719035 |
| San Juan | 0803719036 |
| San Roque | 0803719037 |
| Santa Cruz | 0803719038 |
| Santa Margarita | 0803719039 |
| Santo Niño | 0803719041 |
| Tabunok | 0803719042 |
| Tagnate | 0803719043 |
| Talisay | 0803719044 |
| Tambis | 0803719045 |
| Tejero | 0803719046 |
| Tuguipa | 0803719047 |
| Utanan | 0803719048 |
| Western Barangay | 0803719030 |

## Look up Hilongos with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803719000") or cities.lookup("0803719000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Hilongos

```python
from barangay import search_fuzzy

for r in search_fuzzy("Hilongos", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
