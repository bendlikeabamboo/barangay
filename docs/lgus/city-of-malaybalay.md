---
title: "Barangays in City of Malaybalay, Bukidnon — PSGC Codes"
description: "Complete list of 46 barangays in City of Malaybalay, Bukidnon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Malaybalay, Bukidnon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Malaybalay, Bukidnon",
  "description": "City in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Bukidnon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Bukidnon"
  }
}
</script>

City of Malaybalay is a **city** in Bukidnon (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aglayan | 1001312001 |
| Apo Macote | 1001312027 |
| Bangcud | 1001312002 |
| Barangay 1 | 1001312038 |
| Barangay 10 | 1001312053 |
| Barangay 11 | 1001312054 |
| Barangay 2 | 1001312045 |
| Barangay 3 | 1001312046 |
| Barangay 4 | 1001312047 |
| Barangay 5 | 1001312048 |
| Barangay 6 | 1001312049 |
| Barangay 7 | 1001312050 |
| Barangay 8 | 1001312051 |
| Barangay 9 | 1001312052 |
| Busdi | 1001312003 |
| Cabangahan | 1001312004 |
| Caburacanan | 1001312007 |
| Canayan | 1001312009 |
| Capitan Angel | 1001312010 |
| Casisang | 1001312012 |
| Dalwangan | 1001312014 |
| Imbayao | 1001312017 |
| Indalaza | 1001312018 |
| Kabalabag | 1001312021 |
| Kalasungay | 1001312019 |
| Kulaman | 1001312022 |
| Laguitas | 1001312023 |
| Linabo | 1001312026 |
| Magsaysay | 1001312029 |
| Maligaya | 1001312030 |
| Managok | 1001312031 |
| Manalog | 1001312032 |
| Mapayag | 1001312034 |
| Mapulo | 1001312035 |
| Miglamin | 1001312028 |
| Patpat | 1001312025 |
| San Jose | 1001312059 |
| San Martin | 1001312060 |
| Silae | 1001312062 |
| Simaya | 1001312063 |
| Sinanglanan | 1001312064 |
| St. Peter | 1001312058 |
| Sto. Niño | 1001312061 |
| Sumpong | 1001312065 |
| Violeta | 1001312066 |
| Zamboanguita | 1001312067 |

## Look up Malaybalay with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1001312000") or cities.lookup("1001312000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Malaybalay

```python
from barangay import search_fuzzy

for r in search_fuzzy("Malaybalay", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
