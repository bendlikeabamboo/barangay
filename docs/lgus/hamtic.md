---
title: "Barangays in Hamtic, Antique — PSGC Codes"
description: "Complete list of 47 barangays in Hamtic, Antique with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Hamtic, Antique

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Hamtic, Antique",
  "description": "Municipality in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Hamtic is a **municipality** in Antique (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Apdo | 0600608001 |
| Asluman | 0600608002 |
| Banawon | 0600608003 |
| Bia-an | 0600608005 |
| Bongbongan I-II | 0600608006 |
| Bongbongan III | 0600608008 |
| Botbot | 0600608009 |
| Budbudan | 0600608010 |
| Buhang | 0600608011 |
| Calacja I | 0600608012 |
| Calacja II | 0600608013 |
| Calala | 0600608014 |
| Cantulan | 0600608015 |
| Caridad | 0600608016 |
| Caromangay | 0600608017 |
| Casalngan | 0600608018 |
| Dangcalan | 0600608019 |
| Del Pilar | 0600608020 |
| Fabrica | 0600608021 |
| Funda | 0600608022 |
| General Fullon | 0600608023 |
| Gov. Evelio B. Javier | 0600608030 |
| Guintas | 0600608024 |
| Igbical | 0600608025 |
| Igbucagay | 0600608026 |
| Inabasan | 0600608027 |
| Ingwan-Batangan | 0600608028 |
| La Paz | 0600608029 |
| Linaban | 0600608031 |
| Malandog | 0600608033 |
| Mapatag | 0600608034 |
| Masanag | 0600608035 |
| Nalihawan | 0600608036 |
| Pamandayan | 0600608037 |
| Pasu-Jungao | 0600608038 |
| Piapi I | 0600608039 |
| Piapi II | 0600608040 |
| Piapi III | 0600608041 |
| Pili 1, 2, 3 | 0600608042 |
| Poblacion 1 | 0600608045 |
| Poblacion 2 | 0600608046 |
| Poblacion 3 | 0600608047 |
| Poblacion 4 | 0600608048 |
| Poblacion 5 | 0600608049 |
| Pu-ao | 0600608050 |
| Suloc | 0600608051 |
| Villavert-Jimenez | 0600608053 |

## Look up Hamtic with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0600608000") or cities.lookup("0600608000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Hamtic

```python
from barangay import search_fuzzy

for r in search_fuzzy("Hamtic", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
