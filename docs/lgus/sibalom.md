---
title: "Barangays in Sibalom, Antique — PSGC Codes"
description: "Complete list of 76 barangays in Sibalom, Antique with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Sibalom, Antique

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Sibalom, Antique",
  "description": "Municipality in the Philippines with 76 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Antique",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Antique"
  }
}
</script>

Sibalom is a **municipality** in Antique (Philippines) with
**76 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alangan | 0600616002 |
| Bari | 0600616004 |
| Biga-a | 0600616005 |
| Bongbongan I | 0600616006 |
| Bongbongan II | 0600616007 |
| Bongsod | 0600616008 |
| Bontol | 0600616009 |
| Bugnay | 0600616010 |
| Bululacao | 0600616011 |
| Cabanbanan | 0600616012 |
| Cabariuan | 0600616013 |
| Cabladan | 0600616014 |
| Cadoldolan | 0600616015 |
| Calo-oy | 0600616016 |
| Calog | 0600616017 |
| Catmon | 0600616018 |
| Catungan I | 0600616019 |
| Catungan II | 0600616020 |
| Catungan III | 0600616021 |
| Catungan IV | 0600616022 |
| Cubay-Napultan | 0600616051 |
| Cubay-Sermon | 0600616023 |
| District I | 0600616061 |
| District II | 0600616062 |
| District III | 0600616063 |
| District IV | 0600616064 |
| Egaña | 0600616024 |
| Esperanza I | 0600616025 |
| Esperanza II | 0600616026 |
| Esperanza III | 0600616027 |
| Igcococ | 0600616028 |
| Igdagmay | 0600616030 |
| Igdalaquit | 0600616029 |
| Iglanot | 0600616031 |
| Igpanolong | 0600616032 |
| Igparas | 0600616033 |
| Igsuming | 0600616034 |
| Ilabas | 0600616035 |
| Imparayan | 0600616036 |
| Inabasan | 0600616037 |
| Indag-an | 0600616038 |
| Initan | 0600616039 |
| Insarayan | 0600616040 |
| Lacaron | 0600616041 |
| Lagdo | 0600616042 |
| Lambayagan | 0600616043 |
| Luna | 0600616044 |
| Luyang | 0600616045 |
| Maasin | 0600616046 |
| Mabini | 0600616047 |
| Millamena | 0600616048 |
| Mojon | 0600616049 |
| Nagdayao | 0600616050 |
| Nazareth | 0600616053 |
| Odiong | 0600616054 |
| Olaga | 0600616055 |
| Pangpang | 0600616056 |
| Panlagangan | 0600616057 |
| Pantao | 0600616058 |
| Pasong | 0600616059 |
| Pis-anan | 0600616060 |
| Rombang | 0600616065 |
| Salvacion | 0600616066 |
| San Juan | 0600616067 |
| Sido | 0600616068 |
| Solong | 0600616069 |
| Tabongtabong | 0600616070 |
| Tig-ohot | 0600616071 |
| Tigbalua I | 0600616073 |
| Tigbalua II | 0600616079 |
| Tordesillas | 0600616074 |
| Tulatula | 0600616075 |
| Valentin Grasparil | 0600616003 |
| Villafont | 0600616076 |
| Villahermosa | 0600616077 |
| Villar | 0600616078 |

## Look up Sibalom with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0600616000") or cities.lookup("0600616000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Sibalom

```python
from barangay import search_fuzzy

for r in search_fuzzy("Sibalom", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
