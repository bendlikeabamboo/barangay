---
title: "Barangays in Rosario, Batangas — PSGC Codes"
description: "Complete list of 48 barangays in Rosario, Batangas with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Rosario, Batangas

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Rosario, Batangas",
  "description": "Municipality in the Philippines with 48 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Batangas",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Batangas"
  }
}
</script>

Rosario is a **municipality** in Batangas (Philippines) with
**48 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alupay | 0401021001 |
| Antipolo | 0401021002 |
| Bagong Pook | 0401021003 |
| Balibago | 0401021004 |
| Barangay A | 0401021031 |
| Barangay B | 0401021032 |
| Barangay C | 0401021033 |
| Barangay D | 0401021034 |
| Barangay E | 0401021035 |
| Bayawang | 0401021005 |
| Baybayin | 0401021006 |
| Bulihan | 0401021007 |
| Cahigam | 0401021008 |
| Calantas | 0401021009 |
| Colongan | 0401021010 |
| Itlugan | 0401021011 |
| Leviste | 0401021047 |
| Lumbangan | 0401021012 |
| Maalas-As | 0401021013 |
| Mabato | 0401021014 |
| Mabunga | 0401021015 |
| Macalamcam A | 0401021016 |
| Macalamcam B | 0401021017 |
| Malaya | 0401021018 |
| Maligaya | 0401021019 |
| Marilag | 0401021020 |
| Masaya | 0401021021 |
| Matamis | 0401021022 |
| Mavalor | 0401021023 |
| Mayuro | 0401021024 |
| Namuco | 0401021025 |
| Namunga | 0401021026 |
| Nasi | 0401021028 |
| Natu | 0401021027 |
| Palakpak | 0401021029 |
| Pinagsibaan | 0401021030 |
| Putingkahoy | 0401021036 |
| Quilib | 0401021037 |
| Salao | 0401021038 |
| San Carlos | 0401021039 |
| San Ignacio | 0401021040 |
| San Isidro | 0401021041 |
| San Jose | 0401021042 |
| San Roque | 0401021043 |
| Santa Cruz | 0401021044 |
| Timbugan | 0401021045 |
| Tiquiwan | 0401021046 |
| Tulos | 0401021048 |

## Look up Rosario with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0401021000") or cities.lookup("0401021000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Rosario

```python
from barangay import search_fuzzy

for r in search_fuzzy("Rosario", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
