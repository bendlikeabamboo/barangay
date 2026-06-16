---
title: "Barangays in Agoo, La Union — PSGC Codes"
description: "Complete list of 49 barangays in Agoo, La Union with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Agoo, La Union

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Agoo, La Union",
  "description": "Municipality in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "La Union",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "La Union"
  }
}
</script>

Agoo is a **municipality** in La Union (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Ambitacay | 0103301001 |
| Balawarte | 0103301002 |
| Capas | 0103301003 |
| Consolacion | 0103301004 |
| Macalva Central | 0103301005 |
| Macalva Norte | 0103301006 |
| Macalva Sur | 0103301007 |
| Nazareno | 0103301008 |
| Purok | 0103301009 |
| San Agustin East | 0103301010 |
| San Agustin Norte | 0103301011 |
| San Agustin Sur | 0103301012 |
| San Antonino | 0103301013 |
| San Antonio | 0103301014 |
| San Francisco | 0103301015 |
| San Isidro | 0103301016 |
| San Joaquin Norte | 0103301017 |
| San Joaquin Sur | 0103301018 |
| San Jose Norte | 0103301019 |
| San Jose Sur | 0103301020 |
| San Juan | 0103301021 |
| San Julian Central | 0103301022 |
| San Julian East | 0103301023 |
| San Julian Norte | 0103301024 |
| San Julian West | 0103301025 |
| San Manuel Norte | 0103301026 |
| San Manuel Sur | 0103301027 |
| San Marcos | 0103301028 |
| San Miguel | 0103301029 |
| San Nicolas Central | 0103301030 |
| San Nicolas East | 0103301031 |
| San Nicolas Norte | 0103301032 |
| San Nicolas Sur | 0103301034 |
| San Nicolas West | 0103301033 |
| San Pedro | 0103301035 |
| San Roque East | 0103301037 |
| San Roque West | 0103301036 |
| San Vicente Norte | 0103301038 |
| San Vicente Sur | 0103301039 |
| Santa Ana | 0103301040 |
| Santa Barbara | 0103301041 |
| Santa Fe | 0103301042 |
| Santa Maria | 0103301043 |
| Santa Monica | 0103301044 |
| Santa Rita | 0103301045 |
| Santa Rita East | 0103301046 |
| Santa Rita Norte | 0103301047 |
| Santa Rita Sur | 0103301048 |
| Santa Rita West | 0103301049 |

## Look up Agoo with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0103301000") or cities.lookup("0103301000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Agoo

```python
from barangay import search_fuzzy

for r in search_fuzzy("Agoo", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
