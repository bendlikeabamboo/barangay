---
title: "Barangays in Calabanga, Camarines Sur — PSGC Codes"
description: "Complete list of 48 barangays in Calabanga, Camarines Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Calabanga, Camarines Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Calabanga, Camarines Sur",
  "description": "Municipality in the Philippines with 48 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Camarines Sur",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Camarines Sur"
  }
}
</script>

Calabanga is a **municipality** in Camarines Sur (Philippines) with
**48 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Balatasan | 0501708001 |
| Balombon | 0501708002 |
| Balongay | 0501708003 |
| Belen | 0501708004 |
| Bigaas | 0501708005 |
| Binaliw | 0501708008 |
| Binanuaanan Grande | 0501708006 |
| Binanuaanan Pequeño | 0501708007 |
| Bonot-Santa Rosa | 0501708009 |
| Burabod | 0501708010 |
| Cabanbanan | 0501708011 |
| Cagsao | 0501708012 |
| Camuning | 0501708013 |
| Comaguingking | 0501708014 |
| Del Carmen | 0501708015 |
| Dominorog | 0501708016 |
| Fabrica | 0501708017 |
| Harobay | 0501708018 |
| La Purisima | 0501708019 |
| Lugsad | 0501708021 |
| Manguiring | 0501708022 |
| Pagatpat | 0501708023 |
| Paolbo | 0501708024 |
| Pinada | 0501708025 |
| Punta Tarawal | 0501708026 |
| Quinale | 0501708027 |
| Sabang | 0501708028 |
| Salvacion-Baybay | 0501708029 |
| San Antonio | 0501708031 |
| San Antonio Poblacion | 0501708030 |
| San Bernardino | 0501708032 |
| San Francisco | 0501708033 |
| San Isidro | 0501708034 |
| San Lucas | 0501708036 |
| San Miguel | 0501708037 |
| San Pablo | 0501708038 |
| San Roque | 0501708039 |
| San Vicente | 0501708040 |
| Santa Cruz Poblacion | 0501708042 |
| Santa Cruz Ratay | 0501708041 |
| Santa Isabel | 0501708043 |
| Santa Salud | 0501708044 |
| Santo Domingo | 0501708045 |
| Santo Niño | 0501708046 |
| Siba-o | 0501708047 |
| Sibobo | 0501708048 |
| Sogod | 0501708049 |
| Tomagodtod | 0501708050 |

## Look up Calabanga with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0501708000") or cities.lookup("0501708000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Calabanga

```python
from barangay import search_fuzzy

for r in search_fuzzy("Calabanga", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
