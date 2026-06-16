---
title: "Barangays in Lambunao, Iloilo — PSGC Codes"
description: "Complete list of 73 barangays in Lambunao, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Lambunao, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Lambunao, Iloilo",
  "description": "Municipality in the Philippines with 73 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Iloilo",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Iloilo"
  }
}
</script>

Lambunao is a **municipality** in Iloilo (Philippines) with
**73 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agsirab | 0603025001 |
| Agtuman | 0603025002 |
| Alugmawa | 0603025003 |
| Badiangan | 0603025004 |
| Bagongbong | 0603025005 |
| Balagiao | 0603025006 |
| Banban | 0603025007 |
| Bansag | 0603025008 |
| Bayuco | 0603025009 |
| Binaba-an Armada | 0603025010 |
| Binaba-an Labayno | 0603025011 |
| Binaba-an Limoso | 0603025012 |
| Binaba-an Portigo | 0603025013 |
| Binaba-an Tirador | 0603025014 |
| Bonbon | 0603025015 |
| Bontoc | 0603025016 |
| Buri | 0603025017 |
| Burirao | 0603025018 |
| Buwang | 0603025019 |
| Cabatangan | 0603025020 |
| Cabugao | 0603025021 |
| Cabunlawan | 0603025022 |
| Caguisanan | 0603025023 |
| Caloy-Ahan | 0603025024 |
| Caninguan | 0603025025 |
| Capangyan | 0603025026 |
| Cayan Este | 0603025027 |
| Cayan Oeste | 0603025028 |
| Corot-on | 0603025029 |
| Coto | 0603025030 |
| Cubay | 0603025031 |
| Cunarum | 0603025032 |
| Daanbanwa | 0603025033 |
| Gines | 0603025034 |
| Hipgos | 0603025035 |
| Jayubo | 0603025036 |
| Jorog | 0603025037 |
| Lanot Grande | 0603025038 |
| Lanot Pequeño | 0603025039 |
| Legayada | 0603025040 |
| Lumanay | 0603025041 |
| Madarag | 0603025042 |
| Magbato | 0603025043 |
| Maite Grande | 0603025044 |
| Maite Pequeño | 0603025045 |
| Malag-it | 0603025046 |
| Manaulan | 0603025047 |
| Maribong | 0603025048 |
| Marong | 0603025049 |
| Misi | 0603025050 |
| Natividad | 0603025051 |
| Pajo | 0603025052 |
| Pandan | 0603025053 |
| Panuran | 0603025054 |
| Pasig | 0603025055 |
| Patag | 0603025056 |
| Poblacion Ilawod | 0603025057 |
| Poblacion Ilaya | 0603025058 |
| Poong | 0603025059 |
| Pughanan | 0603025060 |
| Pungsod | 0603025061 |
| Quiling | 0603025062 |
| Sagcup | 0603025063 |
| San Gregorio | 0603025064 |
| Sibacungan | 0603025065 |
| Sibaguan | 0603025066 |
| Simsiman | 0603025067 |
| Supoc | 0603025068 |
| Tampucao | 0603025069 |
| Tranghawan | 0603025070 |
| Tubungan | 0603025071 |
| Tuburan | 0603025072 |
| Walang | 0603025073 |

## Look up Lambunao with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603025000") or cities.lookup("0603025000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Lambunao

```python
from barangay import search_fuzzy

for r in search_fuzzy("Lambunao", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
