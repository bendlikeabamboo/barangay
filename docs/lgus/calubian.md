---
title: "Barangays in Calubian, Leyte — PSGC Codes"
description: "Complete list of 53 barangays in Calubian, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Calubian, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Calubian, Leyte",
  "description": "Municipality in the Philippines with 53 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Calubian is a **municipality** in Leyte (Philippines) with
**53 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abanilla | 0803713001 |
| Agas | 0803713002 |
| Anislagan | 0803713003 |
| Bunacan | 0803713005 |
| Cabalhin | 0803713007 |
| Cabalquinto | 0803713006 |
| Cabradilla | 0803713008 |
| Caneja | 0803713009 |
| Cantonghao | 0803713010 |
| Caroyocan | 0803713011 |
| Casiongan | 0803713012 |
| Cristina | 0803713014 |
| Dalumpines | 0803713015 |
| Don Luis | 0803713016 |
| Dulao | 0803713017 |
| Efe | 0803713018 |
| Enage | 0803713019 |
| Espinosa | 0803713020 |
| Ferdinand E. Marcos | 0803713022 |
| Garganera | 0803713021 |
| Garrido | 0803713023 |
| Guadalupe | 0803713024 |
| Gutosan | 0803713025 |
| Igang | 0803713027 |
| Inalad | 0803713028 |
| Jubay | 0803713029 |
| Juson | 0803713030 |
| Kawayan Bogtong | 0803713031 |
| Kawayanan | 0803713032 |
| Kokoy Romualdez | 0803713033 |
| Labtic | 0803713034 |
| Laray | 0803713035 |
| M. Veloso | 0803713036 |
| Mahait | 0803713037 |
| Malobago | 0803713038 |
| Matagok | 0803713039 |
| Nipa | 0803713040 |
| Obispo | 0803713041 |
| Padoga | 0803713048 |
| Pagatpat | 0803713042 |
| Pangpang | 0803713043 |
| Patag | 0803713045 |
| Pates | 0803713046 |
| Paula | 0803713047 |
| Petrolio | 0803713049 |
| Poblacion | 0803713050 |
| Railes | 0803713051 |
| Tabla | 0803713052 |
| Tagharigue | 0803713053 |
| Tuburan | 0803713054 |
| Villahermosa | 0803713056 |
| Villalon | 0803713057 |
| Villanueva | 0803713058 |

## Look up Calubian with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803713000") or cities.lookup("0803713000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Calubian

```python
from barangay import search_fuzzy

for r in search_fuzzy("Calubian", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
