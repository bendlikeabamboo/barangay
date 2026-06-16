---
title: "Barangays in City of Roxas, Capiz — PSGC Codes"
description: "Complete list of 47 barangays in City of Roxas, Capiz with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Roxas, Capiz

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Roxas, Capiz",
  "description": "City in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Capiz",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Capiz"
  }
}
</script>

City of Roxas is a **city** in Capiz (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adlawan | 0601914001 |
| Bago | 0601914002 |
| Balijuagan | 0601914003 |
| Banica | 0601914004 |
| Barra | 0601914017 |
| Bato | 0601914018 |
| Baybay | 0601914019 |
| Bolo | 0601914020 |
| Cabugao | 0601914021 |
| Cagay | 0601914022 |
| Cogon | 0601914023 |
| Culajao | 0601914024 |
| Culasi | 0601914025 |
| Dayao | 0601914027 |
| Dinginan | 0601914028 |
| Dumolog | 0601914026 |
| Gabu-an | 0601914029 |
| Inzo Arnaldo Village | 0601914030 |
| Jumaguicjic | 0601914031 |
| Lanot | 0601914032 |
| Lawa-an | 0601914033 |
| Libas | 0601914035 |
| Liong | 0601914034 |
| Loctugan | 0601914036 |
| Lonoy | 0601914037 |
| Milibili | 0601914039 |
| Mongpong | 0601914040 |
| Olotayan | 0601914041 |
| Poblacion I | 0601914005 |
| Poblacion II | 0601914009 |
| Poblacion III | 0601914010 |
| Poblacion IV | 0601914011 |
| Poblacion IX | 0601914016 |
| Poblacion V | 0601914012 |
| Poblacion VI | 0601914013 |
| Poblacion VII | 0601914014 |
| Poblacion VIII | 0601914015 |
| Poblacion X | 0601914006 |
| Poblacion XI | 0601914007 |
| Punta Cogon | 0601914042 |
| Punta Tabuc | 0601914043 |
| San Jose | 0601914044 |
| Sibaguan | 0601914045 |
| Talon | 0601914046 |
| Tanque | 0601914047 |
| Tanza | 0601914048 |
| Tiza | 0601914049 |

## Look up Roxas with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0601914000") or cities.lookup("0601914000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Roxas

```python
from barangay import search_fuzzy

for r in search_fuzzy("Roxas", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
