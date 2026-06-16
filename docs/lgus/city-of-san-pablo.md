---
title: "Barangays in City of San Pablo, Laguna — PSGC Codes"
description: "Complete list of 80 barangays in City of San Pablo, Laguna with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of San Pablo, Laguna

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of San Pablo, Laguna",
  "description": "City in the Philippines with 80 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Laguna",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Laguna"
  }
}
</script>

City of San Pablo is a **city** in Laguna (Philippines) with
**80 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Atisan | 0403424080 |
| Bagong Bayan II-A | 0403424001 |
| Bagong Pook VI-C | 0403424002 |
| Barangay I-A | 0403424003 |
| Barangay I-B | 0403424004 |
| Barangay II-A | 0403424005 |
| Barangay II-B | 0403424006 |
| Barangay II-C | 0403424007 |
| Barangay II-D | 0403424008 |
| Barangay II-E | 0403424009 |
| Barangay II-F | 0403424010 |
| Barangay III-A | 0403424011 |
| Barangay III-B | 0403424012 |
| Barangay III-C | 0403424013 |
| Barangay III-D | 0403424014 |
| Barangay III-E | 0403424015 |
| Barangay III-F | 0403424016 |
| Barangay IV-A | 0403424017 |
| Barangay IV-B | 0403424018 |
| Barangay IV-C | 0403424019 |
| Barangay V-A | 0403424020 |
| Barangay V-B | 0403424021 |
| Barangay V-C | 0403424022 |
| Barangay V-D | 0403424023 |
| Barangay VI-A | 0403424024 |
| Barangay VI-B | 0403424025 |
| Barangay VI-D | 0403424027 |
| Barangay VI-E | 0403424028 |
| Barangay VII-A | 0403424029 |
| Barangay VII-B | 0403424030 |
| Barangay VII-C | 0403424031 |
| Barangay VII-D | 0403424032 |
| Barangay VII-E | 0403424033 |
| Bautista | 0403424034 |
| Concepcion | 0403424035 |
| Del Remedio | 0403424036 |
| Dolores | 0403424037 |
| San Antonio 1 | 0403424040 |
| San Antonio 2 | 0403424041 |
| San Bartolome | 0403424042 |
| San Buenaventura | 0403424043 |
| San Crispin | 0403424044 |
| San Cristobal | 0403424045 |
| San Diego | 0403424046 |
| San Francisco | 0403424047 |
| San Gabriel | 0403424048 |
| San Gregorio | 0403424049 |
| San Ignacio | 0403424050 |
| San Isidro | 0403424051 |
| San Joaquin | 0403424052 |
| San Jose | 0403424053 |
| San Juan | 0403424054 |
| San Lorenzo | 0403424055 |
| San Lucas 1 | 0403424056 |
| San Lucas 2 | 0403424057 |
| San Marcos | 0403424058 |
| San Mateo | 0403424059 |
| San Miguel | 0403424060 |
| San Nicolas | 0403424061 |
| San Pedro | 0403424062 |
| San Rafael | 0403424063 |
| San Roque | 0403424064 |
| San Vicente | 0403424065 |
| Santa Ana | 0403424066 |
| Santa Catalina | 0403424067 |
| Santa Cruz | 0403424068 |
| Santa Elena | 0403424081 |
| Santa Felomina | 0403424069 |
| Santa Isabel | 0403424070 |
| Santa Maria | 0403424082 |
| Santa Maria Magdalena | 0403424071 |
| Santa Monica | 0403424083 |
| Santa Veronica | 0403424072 |
| Santiago I | 0403424073 |
| Santiago II | 0403424074 |
| Santisimo Rosario | 0403424075 |
| Santo Angel | 0403424076 |
| Santo Cristo | 0403424077 |
| Santo Niño | 0403424078 |
| Soledad | 0403424079 |

## Look up San Pablo with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0403424000") or cities.lookup("0403424000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in San Pablo

```python
from barangay import search_fuzzy

for r in search_fuzzy("San Pablo", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
