---
title: "Barangays in City of Tabaco, Albay — PSGC Codes"
description: "Complete list of 47 barangays in City of Tabaco, Albay with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Tabaco, Albay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Tabaco, Albay",
  "description": "City in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of Tabaco is a **city** in Albay (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agnas | 0500517001 |
| Bacolod | 0500517002 |
| Bangkilingan | 0500517003 |
| Bantayan | 0500517004 |
| Baranghawon | 0500517005 |
| Basagan | 0500517006 |
| Basud | 0500517007 |
| Bogñabong | 0500517008 |
| Bombon | 0500517009 |
| Bonot | 0500517010 |
| Buang | 0500517012 |
| Buhian | 0500517013 |
| Cabagñan | 0500517014 |
| Cobo | 0500517015 |
| Comon | 0500517016 |
| Cormidal | 0500517017 |
| Divino Rostro | 0500517018 |
| Fatima | 0500517019 |
| Guinobat | 0500517020 |
| Hacienda | 0500517021 |
| Magapo | 0500517022 |
| Mariroc | 0500517023 |
| Matagbac | 0500517024 |
| Oras | 0500517025 |
| Oson | 0500517026 |
| Panal | 0500517027 |
| Pawa | 0500517029 |
| Pinagbobong | 0500517030 |
| Quinale Cabasan | 0500517031 |
| Quinastillojan | 0500517032 |
| Rawis | 0500517033 |
| Sagurong | 0500517034 |
| Salvacion | 0500517035 |
| San Antonio | 0500517036 |
| San Carlos | 0500517037 |
| San Isidro | 0500517011 |
| San Juan | 0500517038 |
| San Lorenzo | 0500517039 |
| San Ramon | 0500517040 |
| San Roque | 0500517041 |
| San Vicente | 0500517042 |
| Santo Cristo | 0500517044 |
| Sua-Igot | 0500517045 |
| Tabiguian | 0500517046 |
| Tagas | 0500517048 |
| Tayhi | 0500517049 |
| Visita | 0500517050 |

## Look up Tabaco with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0500517000") or cities.lookup("0500517000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tabaco

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tabaco", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
