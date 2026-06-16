---
title: "Barangays in City of Gingoog, Misamis Oriental — PSGC Codes"
description: "Complete list of 79 barangays in City of Gingoog, Misamis Oriental with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Gingoog, Misamis Oriental

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Gingoog, Misamis Oriental",
  "description": "City in the Philippines with 79 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Misamis Oriental",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Misamis Oriental"
  }
}
</script>

City of Gingoog is a **city** in Misamis Oriental (Philippines) with
**79 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agay-ayan | 1004308001 |
| Alagatan | 1004308002 |
| Anakan | 1004308003 |
| Bagubad | 1004308004 |
| Bakidbakid | 1004308005 |
| Bal-ason | 1004308006 |
| Bantaawan | 1004308007 |
| Barangay 1 | 1004308033 |
| Barangay 10 | 1004308034 |
| Barangay 11 | 1004308035 |
| Barangay 12 | 1004308036 |
| Barangay 13 | 1004308037 |
| Barangay 14 | 1004308038 |
| Barangay 15 | 1004308039 |
| Barangay 16 | 1004308040 |
| Barangay 17 | 1004308041 |
| Barangay 18 | 1004308073 |
| Barangay 18-A | 1004308042 |
| Barangay 19 | 1004308043 |
| Barangay 2 | 1004308044 |
| Barangay 20 | 1004308045 |
| Barangay 21 | 1004308046 |
| Barangay 22 | 1004308074 |
| Barangay 22-A | 1004308047 |
| Barangay 23 | 1004308048 |
| Barangay 24 | 1004308049 |
| Barangay 24-A | 1004308075 |
| Barangay 25 | 1004308050 |
| Barangay 26 | 1004308051 |
| Barangay 3 | 1004308055 |
| Barangay 4 | 1004308056 |
| Barangay 5 | 1004308057 |
| Barangay 6 | 1004308058 |
| Barangay 7 | 1004308059 |
| Barangay 8 | 1004308060 |
| Barangay 9 | 1004308061 |
| Binakalan | 1004308008 |
| Capitulangan | 1004308010 |
| Daan-Lungsod | 1004308011 |
| Dinawehan | 1004308076 |
| Eureka | 1004308077 |
| Hindangon | 1004308012 |
| Kalagonoy | 1004308013 |
| Kalipay | 1004308078 |
| Kamanikan | 1004308079 |
| Kianlagan | 1004308080 |
| Kibuging | 1004308014 |
| Kipuntos | 1004308015 |
| Lawaan | 1004308016 |
| Lawit | 1004308017 |
| Libertad | 1004308018 |
| Libon | 1004308019 |
| Lunao | 1004308020 |
| Lunotan | 1004308021 |
| Malibud | 1004308022 |
| Malinao | 1004308023 |
| Maribucao | 1004308024 |
| Mimbalagon | 1004308026 |
| Mimbunga | 1004308027 |
| Mimbuntong | 1004308025 |
| Minsapinit | 1004308028 |
| Murallon | 1004308029 |
| Odiongan | 1004308030 |
| Pangasihan | 1004308031 |
| Pigsaluhan | 1004308032 |
| Punong | 1004308062 |
| Ricoro | 1004308063 |
| Samay | 1004308064 |
| San Jose | 1004308081 |
| San Juan | 1004308065 |
| San Luis | 1004308066 |
| San Miguel | 1004308067 |
| Sangalan | 1004308082 |
| Santiago | 1004308068 |
| Tagpako | 1004308083 |
| Talisay | 1004308069 |
| Talon | 1004308070 |
| Tinabalan | 1004308071 |
| Tinulongan | 1004308072 |

## Look up Gingoog with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1004308000") or cities.lookup("1004308000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Gingoog

```python
from barangay import search_fuzzy

for r in search_fuzzy("Gingoog", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
