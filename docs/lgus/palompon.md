---
title: "Barangays in Palompon, Leyte — PSGC Codes"
description: "Complete list of 50 barangays in Palompon, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Palompon, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Palompon, Leyte",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Palompon is a **municipality** in Leyte (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Baguinbin | 0803740001 |
| Belen | 0803740002 |
| Bitaog Pob. | 0803740052 |
| Buenavista | 0803740003 |
| Caduhaan | 0803740004 |
| Cambakbak | 0803740005 |
| Cambinoy | 0803740006 |
| Cangcosme | 0803740007 |
| Cangmuya | 0803740008 |
| Canipaan | 0803740009 |
| Cantandoy | 0803740010 |
| Cantuhaon | 0803740011 |
| Catigahan | 0803740012 |
| Central 1 | 0803740030 |
| Central 2 | 0803740031 |
| Cruz | 0803740013 |
| Duljugan | 0803740014 |
| Guiwan 1 | 0803740016 |
| Guiwan 2 | 0803740017 |
| Himarco | 0803740018 |
| Hinablayan Pob. | 0803740032 |
| Hinagbuan | 0803740019 |
| Lat-osan | 0803740020 |
| Liberty | 0803740021 |
| Lomonon | 0803740023 |
| Mabini | 0803740024 |
| Magsaysay | 0803740025 |
| Masaba | 0803740026 |
| Mazawalo Pob. | 0803740022 |
| Parilla | 0803740027 |
| Pinagdait Pob. | 0803740050 |
| Pinaghi-usa Pob. | 0803740051 |
| Plaridel | 0803740029 |
| Rizal | 0803740033 |
| Sabang | 0803740034 |
| San Guillermo | 0803740035 |
| San Isidro | 0803740036 |
| San Joaquin | 0803740037 |
| San Juan | 0803740038 |
| San Miguel | 0803740039 |
| San Pablo | 0803740040 |
| San Pedro | 0803740041 |
| San Roque | 0803740042 |
| Santiago | 0803740043 |
| Taberna | 0803740044 |
| Tabunok | 0803740045 |
| Tambis | 0803740046 |
| Tinabilan | 0803740047 |
| Tinago | 0803740048 |
| Tinubdan | 0803740049 |

## Look up Palompon with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803740000") or cities.lookup("0803740000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Palompon

```python
from barangay import search_fuzzy

for r in search_fuzzy("Palompon", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
