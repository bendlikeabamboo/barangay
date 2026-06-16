---
title: "Barangays in Amulung, Cagayan — PSGC Codes"
description: "Complete list of 47 barangays in Amulung, Cagayan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Amulung, Cagayan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Amulung, Cagayan",
  "description": "Municipality in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cagayan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cagayan"
  }
}
</script>

Amulung is a **municipality** in Cagayan (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abolo | 0201504001 |
| Agguirit | 0201504002 |
| Alituntung | 0201504003 |
| Annabuculan | 0201504004 |
| Annafatan | 0201504005 |
| Anquiray | 0201504006 |
| Babayuan | 0201504007 |
| Baccuit | 0201504008 |
| Bacring | 0201504009 |
| Baculud | 0201504010 |
| Balauini | 0201504011 |
| Bauan | 0201504012 |
| Bayabat | 0201504013 |
| Calamagui | 0201504014 |
| Calintaan | 0201504015 |
| Caratacat | 0201504016 |
| Casingsingan Norte | 0201504017 |
| Casingsingan Sur | 0201504018 |
| Catarauan | 0201504019 |
| Centro | 0201504020 |
| Concepcion | 0201504021 |
| Cordova | 0201504022 |
| Dadda | 0201504023 |
| Dafunganay | 0201504024 |
| Dugayung | 0201504025 |
| Estefania | 0201504026 |
| Gabut | 0201504027 |
| Gangauan | 0201504028 |
| Goran | 0201504029 |
| Jurisdiccion | 0201504030 |
| La Suerte | 0201504031 |
| Logung | 0201504032 |
| Magogod | 0201504033 |
| Manalo | 0201504034 |
| Marobbob | 0201504035 |
| Masical | 0201504036 |
| Monte Alegre | 0201504037 |
| Nabbialan | 0201504038 |
| Nagsabaran | 0201504039 |
| Nangalasauan | 0201504040 |
| Nanuccauan | 0201504041 |
| Pacac-Grande | 0201504042 |
| Pacac-Pequeño | 0201504043 |
| Palacu | 0201504044 |
| Palayag | 0201504045 |
| Tana | 0201504046 |
| Unag | 0201504047 |

## Look up Amulung with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0201504000") or cities.lookup("0201504000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Amulung

```python
from barangay import search_fuzzy

for r in search_fuzzy("Amulung", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
