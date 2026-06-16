---
title: "Barangays in Naujan, Oriental Mindoro — PSGC Codes"
description: "Complete list of 70 barangays in Naujan, Oriental Mindoro with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Naujan, Oriental Mindoro

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Naujan, Oriental Mindoro",
  "description": "Municipality in the Philippines with 70 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Oriental Mindoro",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Oriental Mindoro"
  }
}
</script>

Naujan is a **municipality** in Oriental Mindoro (Philippines) with
**70 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adrialuna | 1705208001 |
| Andres Ilagan | 1705208025 |
| Antipolo | 1705208002 |
| Apitong | 1705208003 |
| Arangin | 1705208004 |
| Aurora | 1705208005 |
| Bacungan | 1705208006 |
| Bagong Buhay | 1705208007 |
| Balite | 1705208068 |
| Bancuro | 1705208008 |
| Banuton | 1705208069 |
| Barcenaga | 1705208010 |
| Bayani | 1705208011 |
| Buhangin | 1705208012 |
| Caburo | 1705208070 |
| Concepcion | 1705208013 |
| Dao | 1705208014 |
| Del Pilar | 1705208015 |
| Estrella | 1705208016 |
| Evangelista | 1705208017 |
| Gamao | 1705208018 |
| General Esco | 1705208019 |
| Herrera | 1705208020 |
| Inarawan | 1705208021 |
| Kalinisan | 1705208022 |
| Laguna | 1705208023 |
| Mabini | 1705208024 |
| Magtibay | 1705208071 |
| Mahabang Parang | 1705208026 |
| Malaya | 1705208027 |
| Malinao | 1705208028 |
| Malvar | 1705208029 |
| Masagana | 1705208030 |
| Masaguing | 1705208031 |
| Melgar A | 1705208032 |
| Melgar B | 1705208066 |
| Metolza | 1705208033 |
| Montelago | 1705208034 |
| Montemayor | 1705208035 |
| Motoderazo | 1705208036 |
| Mulawin | 1705208037 |
| Nag-Iba I | 1705208038 |
| Nag-Iba II | 1705208039 |
| Pagkakaisa | 1705208040 |
| Paitan | 1705208072 |
| Paniquian | 1705208042 |
| Pinagsabangan I | 1705208043 |
| Pinagsabangan II | 1705208044 |
| Piñahan | 1705208045 |
| Poblacion I | 1705208046 |
| Poblacion II | 1705208047 |
| Poblacion III | 1705208048 |
| Sampaguita | 1705208049 |
| San Agustin I | 1705208050 |
| San Agustin II | 1705208051 |
| San Andres | 1705208052 |
| San Antonio | 1705208053 |
| San Carlos | 1705208054 |
| San Isidro | 1705208055 |
| San Jose | 1705208056 |
| San Luis | 1705208057 |
| San Nicolas | 1705208058 |
| San Pedro | 1705208059 |
| Santa Cruz | 1705208067 |
| Santa Isabel | 1705208060 |
| Santa Maria | 1705208061 |
| Santiago | 1705208062 |
| Santo Niño | 1705208063 |
| Tagumpay | 1705208064 |
| Tigkan | 1705208065 |

## Look up Naujan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1705208000") or cities.lookup("1705208000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Naujan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Naujan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
