---
title: "Barangays in Dolores, Eastern Samar — PSGC Codes"
description: "Complete list of 46 barangays in Dolores, Eastern Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Dolores, Eastern Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Dolores, Eastern Samar",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Eastern Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Eastern Samar"
  }
}
</script>

Dolores is a **municipality** in Eastern Samar (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aroganga | 0802606001 |
| Barangay 1 | 0802606022 |
| Barangay 10 | 0802606023 |
| Barangay 11 | 0802606024 |
| Barangay 12 | 0802606025 |
| Barangay 13 | 0802606026 |
| Barangay 14 | 0802606027 |
| Barangay 15 | 0802606028 |
| Barangay 2 | 0802606029 |
| Barangay 3 | 0802606030 |
| Barangay 4 | 0802606031 |
| Barangay 5 | 0802606032 |
| Barangay 6 | 0802606033 |
| Barangay 7 | 0802606034 |
| Barangay 8 | 0802606035 |
| Barangay 9 | 0802606036 |
| Bonghon | 0802606047 |
| Buenavista | 0802606003 |
| Cabago-an | 0802606004 |
| Caglao-an | 0802606005 |
| Cagtabon | 0802606006 |
| Dampigan | 0802606007 |
| Dapdap | 0802606008 |
| Del Pilar | 0802606009 |
| Denigpian | 0802606010 |
| Gap-ang | 0802606011 |
| Hilabaan | 0802606014 |
| Hinolaso | 0802606015 |
| Japitan | 0802606012 |
| Jicontol | 0802606013 |
| Libertad | 0802606016 |
| Magongbong | 0802606002 |
| Magsaysay | 0802606018 |
| Malaintos | 0802606048 |
| Malobago | 0802606019 |
| Osmeña | 0802606020 |
| Rizal | 0802606037 |
| San Isidro | 0802606038 |
| San Pascual | 0802606039 |
| San Roque | 0802606040 |
| San Vicente | 0802606041 |
| Santa Cruz | 0802606042 |
| Santo Niño | 0802606043 |
| Tanauan | 0802606044 |
| Tikling | 0802606049 |
| Villahermosa | 0802606046 |

## Look up Dolores with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0802606000") or cities.lookup("0802606000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Dolores

```python
from barangay import search_fuzzy

for r in search_fuzzy("Dolores", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
