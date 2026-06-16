---
title: "Barangays in Carigara, Leyte — PSGC Codes"
description: "Complete list of 49 barangays in Carigara, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Carigara, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Carigara, Leyte",
  "description": "Municipality in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Carigara is a **municipality** in Leyte (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Bagong Lipunan | 0803715046 |
| Balilit | 0803715001 |
| Barayong | 0803715002 |
| Barugohay Central | 0803715003 |
| Barugohay Norte | 0803715004 |
| Barugohay Sur | 0803715005 |
| Baybay | 0803715006 |
| Binibihan | 0803715007 |
| Bislig | 0803715008 |
| Caghalo | 0803715009 |
| Camansi | 0803715010 |
| Canal | 0803715011 |
| Candigahub | 0803715012 |
| Canfabi | 0803715047 |
| Canlampay | 0803715013 |
| Cogon | 0803715014 |
| Cutay | 0803715015 |
| East Visoria | 0803715016 |
| Guindapunan East | 0803715017 |
| Guindapunan West | 0803715018 |
| Hiluctogan | 0803715019 |
| Jugaban | 0803715020 |
| Libo | 0803715021 |
| Lower Hiraan | 0803715022 |
| Lower Sogod | 0803715023 |
| Macalpi | 0803715024 |
| Manloy | 0803715025 |
| Nauguisan | 0803715026 |
| Paglaum | 0803715044 |
| Pangna | 0803715027 |
| Parag-um | 0803715028 |
| Parina | 0803715029 |
| Piloro | 0803715030 |
| Ponong | 0803715031 |
| Rizal | 0803715048 |
| Sagkahan | 0803715032 |
| San Isidro | 0803715049 |
| San Juan | 0803715045 |
| San Mateo | 0803715033 |
| Santa Fe | 0803715034 |
| Sawang | 0803715035 |
| Tagak | 0803715036 |
| Tangnan | 0803715037 |
| Tigbao | 0803715038 |
| Tinaguban | 0803715039 |
| Upper Hiraan | 0803715040 |
| Upper Sogod | 0803715041 |
| Uyawan | 0803715042 |
| West Visoria | 0803715043 |

## Look up Carigara with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803715000") or cities.lookup("0803715000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Carigara

```python
from barangay import search_fuzzy

for r in search_fuzzy("Carigara", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
