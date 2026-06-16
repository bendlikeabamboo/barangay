---
title: "Barangays in Echague, Isabela — PSGC Codes"
description: "Complete list of 64 barangays in Echague, Isabela with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Echague, Isabela

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Echague, Isabela",
  "description": "Municipality in the Philippines with 64 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Isabela",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Isabela"
  }
}
</script>

Echague is a **municipality** in Isabela (Philippines) with
**64 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Angoluan | 0203112001 |
| Annafunan | 0203112002 |
| Arabiat | 0203112003 |
| Aromin | 0203112004 |
| Babaran | 0203112005 |
| Bacradal | 0203112006 |
| Benguet | 0203112007 |
| Buneg | 0203112008 |
| Busilelao | 0203112009 |
| Cabugao | 0203112066 |
| Caniguing | 0203112010 |
| Carulay | 0203112011 |
| Castillo | 0203112012 |
| Dammang East | 0203112013 |
| Dammang West | 0203112014 |
| Diasan | 0203112067 |
| Dicaraoyan | 0203112015 |
| Dugayong | 0203112016 |
| Fugu | 0203112017 |
| Garit Norte | 0203112018 |
| Garit Sur | 0203112019 |
| Gucab | 0203112020 |
| Gumbauan | 0203112021 |
| Ipil | 0203112023 |
| Libertad | 0203112024 |
| Mabbayad | 0203112025 |
| Mabuhay | 0203112026 |
| Madadamian | 0203112027 |
| Magleticia | 0203112028 |
| Malibago | 0203112029 |
| Maligaya | 0203112030 |
| Malitao | 0203112031 |
| Narra | 0203112032 |
| Nilumisu | 0203112033 |
| Pag-asa | 0203112034 |
| Pangal Norte | 0203112036 |
| Pangal Sur | 0203112037 |
| Rumang-ay | 0203112039 |
| Salay | 0203112040 |
| Salvacion | 0203112041 |
| San Antonio Minit | 0203112043 |
| San Antonio Ugad | 0203112042 |
| San Carlos | 0203112044 |
| San Fabian | 0203112045 |
| San Felipe | 0203112046 |
| San Juan | 0203112047 |
| San Manuel | 0203112048 |
| San Miguel | 0203112049 |
| San Salvador | 0203112050 |
| Santa Ana | 0203112051 |
| Santa Cruz | 0203112052 |
| Santa Maria | 0203112053 |
| Santa Monica | 0203112054 |
| Santo Domingo | 0203112055 |
| Silauan Norte | 0203112057 |
| Silauan Sur | 0203112056 |
| Sinabbaran | 0203112058 |
| Soyung | 0203112059 |
| Taggappan | 0203112060 |
| Tuguegarao | 0203112061 |
| Villa Campo | 0203112062 |
| Villa Fermin | 0203112063 |
| Villa Rey | 0203112064 |
| Villa Victoria | 0203112065 |

## Look up Echague with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0203112000") or cities.lookup("0203112000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Echague

```python
from barangay import search_fuzzy

for r in search_fuzzy("Echague", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
