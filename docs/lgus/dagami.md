---
title: "Barangays in Dagami, Leyte — PSGC Codes"
description: "Complete list of 65 barangays in Dagami, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Dagami, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Dagami, Leyte",
  "description": "Municipality in the Philippines with 65 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Dagami is a **municipality** in Leyte (Philippines) with
**65 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abaca | 0803717001 |
| Abre | 0803717002 |
| Balilit | 0803717003 |
| Balugo | 0803717057 |
| Banayon | 0803717004 |
| Bayabas | 0803717005 |
| Bolirao | 0803717006 |
| Buenavista | 0803717007 |
| Buntay | 0803717008 |
| Caanislagan | 0803717009 |
| Cabariwan | 0803717010 |
| Cabuloran | 0803717011 |
| Cabunga-an | 0803717012 |
| Calipayan | 0803717013 |
| Calsadahay | 0803717014 |
| Caluctogan | 0803717015 |
| Calutan | 0803717016 |
| Camono-an | 0803717017 |
| Candagara | 0803717018 |
| Canlingga | 0803717019 |
| Cansamada East | 0803717020 |
| Cansamada West | 0803717058 |
| Capulhan | 0803717059 |
| Digahungan | 0803717021 |
| Guinarona | 0803717022 |
| Hiabangan | 0803717023 |
| Hilabago | 0803717024 |
| Hinabuyan | 0803717025 |
| Hinologan | 0803717026 |
| Hitomnog | 0803717027 |
| Katipunan | 0803717028 |
| Lapu-Lapu | 0803717040 |
| Lobe-Lobe | 0803717030 |
| Lobe-Lobe East | 0803717060 |
| Los Martires | 0803717029 |
| Lusad Pob. | 0803717041 |
| Macaalang | 0803717031 |
| Maliwaliw | 0803717032 |
| Maragongdong | 0803717033 |
| Ormocay | 0803717034 |
| Palacio | 0803717035 |
| Panda | 0803717036 |
| Paraiso | 0803717061 |
| Patoc | 0803717037 |
| Plaridel | 0803717038 |
| Poponton | 0803717048 |
| Rizal | 0803717049 |
| Salvacion | 0803717050 |
| Sampaguita | 0803717062 |
| Sampao East Pob. | 0803717042 |
| Sampao West Pob. | 0803717039 |
| San Antonio Pob. | 0803717043 |
| San Benito | 0803717051 |
| San Jose Pob. | 0803717044 |
| San Roque Pob. | 0803717047 |
| Sawahon | 0803717063 |
| Sirab | 0803717053 |
| Sta. Mesa Pob. | 0803717045 |
| Sto. Domingo | 0803717052 |
| Tagkip | 0803717054 |
| Talinhugon | 0803717064 |
| Tin-ao | 0803717055 |
| Tunga Pob. | 0803717046 |
| Tuya | 0803717065 |
| Victoria | 0803717056 |

## Look up Dagami with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803717000") or cities.lookup("0803717000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Dagami

```python
from barangay import search_fuzzy

for r in search_fuzzy("Dagami", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
