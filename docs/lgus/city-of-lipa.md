---
title: "Barangays in City of Lipa, Batangas — PSGC Codes"
description: "Complete list of 72 barangays in City of Lipa, Batangas with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Lipa, Batangas

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Lipa, Batangas",
  "description": "City in the Philippines with 72 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of Lipa is a **city** in Batangas (Philippines) with
**72 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adya | 0401014001 |
| Anilao | 0401014003 |
| Anilao-Labac | 0401014004 |
| Antipolo Del Norte | 0401014005 |
| Antipolo Del Sur | 0401014006 |
| Bagong Pook | 0401014007 |
| Balintawak | 0401014009 |
| Banaybanay | 0401014010 |
| Barangay 12 | 0401014077 |
| Bolbok | 0401014011 |
| Bugtong na Pulo | 0401014012 |
| Bulacnin | 0401014013 |
| Bulaklakan | 0401014014 |
| Calamias | 0401014015 |
| Cumba | 0401014016 |
| Dagatan | 0401014017 |
| Duhatan | 0401014018 |
| Halang | 0401014020 |
| Inosloban | 0401014021 |
| Kayumanggi | 0401014022 |
| Latag | 0401014024 |
| Lodlod | 0401014025 |
| Lumbang | 0401014026 |
| Mabini | 0401014027 |
| Malagonlong | 0401014028 |
| Malitlit | 0401014029 |
| Marauoy | 0401014030 |
| Mataas Na Lupa | 0401014031 |
| Munting Pulo | 0401014032 |
| Pagolingin Bata | 0401014033 |
| Pagolingin East | 0401014034 |
| Pagolingin West | 0401014035 |
| Pangao | 0401014036 |
| Pinagkawitan | 0401014037 |
| Pinagtongulan | 0401014038 |
| Plaridel | 0401014039 |
| Poblacion Barangay 1 | 0401014040 |
| Poblacion Barangay 10 | 0401014041 |
| Poblacion Barangay 11 | 0401014042 |
| Poblacion Barangay 2 | 0401014043 |
| Poblacion Barangay 3 | 0401014044 |
| Poblacion Barangay 4 | 0401014045 |
| Poblacion Barangay 5 | 0401014046 |
| Poblacion Barangay 6 | 0401014047 |
| Poblacion Barangay 7 | 0401014048 |
| Poblacion Barangay 8 | 0401014049 |
| Poblacion Barangay 9 | 0401014050 |
| Poblacion Barangay 9-A | 0401014076 |
| Pusil | 0401014051 |
| Quezon | 0401014052 |
| Rizal | 0401014053 |
| Sabang | 0401014054 |
| Sampaguita | 0401014055 |
| San Benito | 0401014056 |
| San Carlos | 0401014057 |
| San Celestino | 0401014058 |
| San Francisco | 0401014059 |
| San Guillermo | 0401014060 |
| San Jose | 0401014061 |
| San Lucas | 0401014062 |
| San Salvador | 0401014063 |
| San Sebastian | 0401014008 |
| Santo Niño | 0401014068 |
| Santo Toribio | 0401014069 |
| Sapac | 0401014064 |
| Sico | 0401014066 |
| Talisay | 0401014070 |
| Tambo | 0401014071 |
| Tangob | 0401014072 |
| Tanguay | 0401014073 |
| Tibig | 0401014074 |
| Tipacan | 0401014075 |

## Look up Lipa with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0401014000") or cities.lookup("0401014000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Lipa

```python
from barangay import search_fuzzy

for r in search_fuzzy("Lipa", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
