---
title: "Barangays in Cuyapo, Nueva Ecija — PSGC Codes"
description: "Complete list of 51 barangays in Cuyapo, Nueva Ecija with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Cuyapo, Nueva Ecija

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Cuyapo, Nueva Ecija",
  "description": "Municipality in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Nueva Ecija",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Nueva Ecija"
  }
}
</script>

Cuyapo is a **municipality** in Nueva Ecija (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Baloy | 0304906001 |
| Bambanaba | 0304906002 |
| Bantug | 0304906003 |
| Bentigan | 0304906004 |
| Bibiclat | 0304906005 |
| Bonifacio | 0304906006 |
| Bued | 0304906007 |
| Bulala | 0304906008 |
| Burgos | 0304906009 |
| Cabatuan | 0304906011 |
| Cabileo | 0304906010 |
| Cacapasan | 0304906012 |
| Calancuasan Norte | 0304906013 |
| Calancuasan Sur | 0304906014 |
| Colosboa | 0304906015 |
| Columbitin | 0304906016 |
| Curva | 0304906017 |
| District I | 0304906018 |
| District II | 0304906019 |
| District IV | 0304906021 |
| District V | 0304906022 |
| District VI | 0304906023 |
| District VII | 0304906024 |
| District VIII | 0304906025 |
| Landig | 0304906026 |
| Latap | 0304906027 |
| Loob | 0304906028 |
| Luna | 0304906029 |
| Malbeg-Patalan | 0304906030 |
| Malineng | 0304906031 |
| Matindeg | 0304906032 |
| Maycaban | 0304906033 |
| Nagcuralan | 0304906034 |
| Nagmisahan | 0304906035 |
| Paitan Norte | 0304906036 |
| Paitan Sur | 0304906037 |
| Piglisan | 0304906038 |
| Pugo | 0304906039 |
| Rizal | 0304906040 |
| Sabit | 0304906041 |
| Salagusog | 0304906042 |
| San Antonio | 0304906043 |
| San Jose | 0304906044 |
| San Juan | 0304906045 |
| Santa Clara | 0304906046 |
| Santa Cruz | 0304906047 |
| Simimbaan | 0304906048 |
| Tagtagumbao | 0304906049 |
| Tutuloy | 0304906050 |
| Ungab | 0304906051 |
| Villaflores | 0304906052 |

## Look up Cuyapo with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0304906000") or cities.lookup("0304906000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Cuyapo

```python
from barangay import search_fuzzy

for r in search_fuzzy("Cuyapo", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
