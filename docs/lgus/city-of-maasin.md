---
title: "Barangays in City of Maasin, Southern Leyte — PSGC Codes"
description: "Complete list of 70 barangays in City of Maasin, Southern Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Maasin, Southern Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Maasin, Southern Leyte",
  "description": "City in the Philippines with 70 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Southern Leyte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Southern Leyte"
  }
}
</script>

City of Maasin is a **city** in Southern Leyte (Philippines) with
**70 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abgao | 0806407001 |
| Acasia | 0806407065 |
| Asuncion | 0806407002 |
| Bactul I | 0806407004 |
| Bactul II | 0806407003 |
| Badiang | 0806407005 |
| Bagtican | 0806407006 |
| Basak | 0806407007 |
| Bato I | 0806407009 |
| Bato II | 0806407008 |
| Batuan | 0806407010 |
| Baugo | 0806407011 |
| Bilibol | 0806407012 |
| Bogo | 0806407013 |
| Cabadiangan | 0806407014 |
| Cabulihan | 0806407015 |
| Cagnituan | 0806407016 |
| Cambooc | 0806407017 |
| Cansirong | 0806407018 |
| Canturing | 0806407019 |
| Canyuom | 0806407020 |
| Combado | 0806407066 |
| Dongon | 0806407021 |
| Gawisan | 0806407022 |
| Guadalupe | 0806407023 |
| Hanginan | 0806407024 |
| Hantag | 0806407025 |
| Hinapu Daku | 0806407026 |
| Hinapu Gamay | 0806407027 |
| Ibarra | 0806407028 |
| Isagani | 0806407029 |
| Laboon | 0806407030 |
| Lanao | 0806407031 |
| Lib-og | 0806407068 |
| Libertad | 0806407067 |
| Libhu | 0806407032 |
| Lonoy | 0806407033 |
| Lunas | 0806407034 |
| Mahayahay | 0806407035 |
| Malapoc Norte | 0806407036 |
| Malapoc Sur | 0806407037 |
| Mambajao | 0806407038 |
| Manhilo | 0806407039 |
| Mantahan | 0806407040 |
| Maria Clara | 0806407041 |
| Matin-ao | 0806407042 |
| Nasaug | 0806407043 |
| Nati | 0806407044 |
| Nonok Norte | 0806407045 |
| Nonok Sur | 0806407046 |
| Panan-awan | 0806407047 |
| Pansaan | 0806407048 |
| Pasay | 0806407069 |
| Pinascohan | 0806407049 |
| Rizal | 0806407050 |
| San Agustin | 0806407070 |
| San Isidro | 0806407051 |
| San Jose | 0806407052 |
| San Rafael | 0806407053 |
| Santa Cruz | 0806407054 |
| Santa Rosa | 0806407055 |
| Santo Niño | 0806407056 |
| Santo Rosario | 0806407057 |
| Soro-soro | 0806407058 |
| Tagnipa | 0806407059 |
| Tam-is | 0806407060 |
| Tawid | 0806407061 |
| Tigbawan | 0806407062 |
| Tomoy-tomoy | 0806407063 |
| Tunga-tunga | 0806407064 |

## Look up Maasin with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0806407000") or cities.lookup("0806407000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Maasin

```python
from barangay import search_fuzzy

for r in search_fuzzy("Maasin", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
