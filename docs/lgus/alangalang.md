---
title: "Barangays in Alangalang, Leyte — PSGC Codes"
description: "Complete list of 54 barangays in Alangalang, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Alangalang, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Alangalang, Leyte",
  "description": "Municipality in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Alangalang is a **municipality** in Leyte (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aslum | 0803702001 |
| Astorga | 0803702002 |
| Bato | 0803702004 |
| Binongto-an | 0803702005 |
| Binotong | 0803702006 |
| Blumentritt | 0803702049 |
| Bobonon | 0803702007 |
| Borseth | 0803702008 |
| Buenavista | 0803702009 |
| Bugho | 0803702010 |
| Buri | 0803702011 |
| Cabadsan | 0803702012 |
| Calaasan | 0803702013 |
| Cambahanon | 0803702014 |
| Cambolao | 0803702015 |
| Canvertudes | 0803702016 |
| Capiz | 0803702017 |
| Cavite | 0803702018 |
| Cogon | 0803702019 |
| Dapdap | 0803702020 |
| Divisoria | 0803702021 |
| Ekiran | 0803702022 |
| Hinapolan | 0803702023 |
| Holy Child I | 0803702050 |
| Holy Child II | 0803702051 |
| Hubang | 0803702024 |
| Hupit | 0803702025 |
| Langit | 0803702026 |
| Lingayon | 0803702027 |
| Lourdes | 0803702028 |
| Lukay | 0803702029 |
| Magsaysay | 0803702030 |
| Milagrosa | 0803702052 |
| Mudboron | 0803702031 |
| P. Barrantes | 0803702032 |
| Pepita | 0803702034 |
| Peñalosa | 0803702033 |
| Salvacion | 0803702055 |
| Salvacion Poblacion | 0803702035 |
| San Antonio | 0803702036 |
| San Antonio Pob. | 0803702053 |
| San Diego | 0803702037 |
| San Francisco East | 0803702038 |
| San Francisco West | 0803702039 |
| San Isidro | 0803702040 |
| San Pedro | 0803702041 |
| San Roque | 0803702054 |
| San Vicente | 0803702042 |
| Santiago | 0803702043 |
| Santo Niño | 0803702044 |
| Santol | 0803702045 |
| Tabangohay | 0803702046 |
| Tombo | 0803702047 |
| Veteranos | 0803702048 |

## Look up Alangalang with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803702000") or cities.lookup("0803702000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Alangalang

```python
from barangay import search_fuzzy

for r in search_fuzzy("Alangalang", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
