---
title: "Barangays in City of Ozamiz, Misamis Occidental — PSGC Codes"
description: "Complete list of 51 barangays in City of Ozamiz, Misamis Occidental with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Ozamiz, Misamis Occidental

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Ozamiz, Misamis Occidental",
  "description": "City in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Misamis Occidental",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Misamis Occidental"
  }
}
</script>

City of Ozamiz is a **city** in Misamis Occidental (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| 50th District | 1004210051 |
| Aguada | 1004210001 |
| Bacolod | 1004210003 |
| Bagakay | 1004210004 |
| Balintawak | 1004210005 |
| Banadero | 1004210002 |
| Baybay San Roque | 1004210043 |
| Baybay Santa Cruz | 1004210006 |
| Baybay Triunfo | 1004210007 |
| Bongbong | 1004210008 |
| Calabayan | 1004210009 |
| Capucao C. | 1004210010 |
| Capucao P. | 1004210011 |
| Carangan | 1004210012 |
| Carmen | 1004210037 |
| Catadman-Manabay | 1004210013 |
| Cavinte | 1004210014 |
| Cogon | 1004210015 |
| Dalapang | 1004210016 |
| Diguan | 1004210017 |
| Dimaluna | 1004210018 |
| Doña Consuelo | 1004210052 |
| Embargo | 1004210019 |
| Gala | 1004210020 |
| Gango | 1004210021 |
| Gotokan Daku | 1004210022 |
| Gotokan Diot | 1004210023 |
| Guimad | 1004210024 |
| Guingona | 1004210025 |
| Kinuman Norte | 1004210026 |
| Kinuman Sur | 1004210027 |
| Labinay | 1004210028 |
| Labo | 1004210029 |
| Lam-an | 1004210030 |
| Liposong | 1004210031 |
| Litapan | 1004210032 |
| Malaubang | 1004210033 |
| Manaka | 1004210034 |
| Maningcol | 1004210035 |
| Mentering | 1004210036 |
| Molicay | 1004210038 |
| Pantaon | 1004210040 |
| Pulot | 1004210041 |
| San Antonio | 1004210042 |
| Sangay Daku | 1004210044 |
| Sangay Diot | 1004210045 |
| Sinuza | 1004210046 |
| Stimson Abordo | 1004210039 |
| Tabid | 1004210047 |
| Tinago | 1004210048 |
| Trigos | 1004210049 |

## Look up Ozamiz with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1004210000") or cities.lookup("1004210000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Ozamiz

```python
from barangay import search_fuzzy

for r in search_fuzzy("Ozamiz", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
