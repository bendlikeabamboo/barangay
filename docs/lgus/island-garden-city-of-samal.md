---
title: "Barangays in Island Garden City of Samal, Davao del Norte — PSGC Codes"
description: "Complete list of 46 barangays in Island Garden City of Samal, Davao del Norte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Island Garden City of Samal, Davao del Norte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Island Garden City of Samal, Davao del Norte",
  "description": "City in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Davao del Norte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Davao del Norte"
  }
}
</script>

Island Garden City of Samal is a **city** in Davao del Norte (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adecor | 1102317001 |
| Anonang | 1102317002 |
| Aumbay | 1102317003 |
| Aundanao | 1102317004 |
| Balet | 1102317005 |
| Bandera | 1102317006 |
| Caliclic | 1102317007 |
| Camudmud | 1102317008 |
| Catagman | 1102317009 |
| Cawag | 1102317010 |
| Cogon | 1102317011 |
| Cogon (Talicod) | 1102317012 |
| Dadatan | 1102317013 |
| Del Monte | 1102317014 |
| Guilon | 1102317015 |
| Kanaan | 1102317016 |
| Kinawitnon | 1102317017 |
| Libertad | 1102317018 |
| Libuak | 1102317019 |
| Licup | 1102317020 |
| Limao | 1102317021 |
| Linosutan | 1102317022 |
| Mambago-A | 1102317023 |
| Mambago-B | 1102317024 |
| Miranda | 1102317025 |
| Moncado | 1102317026 |
| Pangubatan | 1102317027 |
| Peñaplata | 1102317028 |
| Poblacion | 1102317029 |
| San Agustin | 1102317030 |
| San Antonio | 1102317031 |
| San Isidro (Babak) | 1102317032 |
| San Isidro (Kaputian) | 1102317033 |
| San Jose | 1102317034 |
| San Miguel | 1102317035 |
| San Remigio | 1102317036 |
| Santa Cruz | 1102317037 |
| Santo Niño | 1102317038 |
| Sion | 1102317039 |
| Tagbaobo | 1102317040 |
| Tagbay | 1102317041 |
| Tagbitan-ag | 1102317042 |
| Tagdaliao | 1102317043 |
| Tagpopongan | 1102317044 |
| Tambo | 1102317045 |
| Toril | 1102317046 |

## Look up Island Garden Samal with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1102317000") or cities.lookup("1102317000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Island Garden Samal

```python
from barangay import search_fuzzy

for r in search_fuzzy("Island Garden Samal", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
