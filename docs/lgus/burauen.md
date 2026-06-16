---
title: "Barangays in Burauen, Leyte — PSGC Codes"
description: "Complete list of 77 barangays in Burauen, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Burauen, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Burauen, Leyte",
  "description": "Municipality in the Philippines with 77 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Burauen is a **municipality** in Leyte (Philippines) with
**77 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abuyogon | 0803710001 |
| Anonang | 0803710002 |
| Arado | 0803710003 |
| Balao | 0803710004 |
| Balatson | 0803710005 |
| Balorinay | 0803710006 |
| Bobon | 0803710007 |
| Buenavista | 0803710008 |
| Buri | 0803710009 |
| Caanislagan | 0803710010 |
| Cadahunan | 0803710011 |
| Cagangon | 0803710012 |
| Cali | 0803710013 |
| Calsadahay | 0803710014 |
| Candag-on | 0803710015 |
| Cansiboy | 0803710016 |
| Catagbacan | 0803710017 |
| Damulo-an | 0803710076 |
| Dina-ayan | 0803710077 |
| Dumalag | 0803710027 |
| Esperanza | 0803710029 |
| Gamay | 0803710078 |
| Gitabla | 0803710030 |
| Hapunan | 0803710031 |
| Hibunawan | 0803710032 |
| Hugpa East | 0803710033 |
| Hugpa West | 0803710034 |
| Ilihan | 0803710028 |
| Kagbana | 0803710075 |
| Kalao | 0803710035 |
| Kalipayan | 0803710079 |
| Kaparasanan | 0803710036 |
| Laguiwan | 0803710037 |
| Libas | 0803710038 |
| Limburan | 0803710039 |
| Logsongan | 0803710040 |
| Maabab | 0803710041 |
| Maghubas | 0803710042 |
| Mahagnao | 0803710043 |
| Malabca | 0803710044 |
| Malaguinabot | 0803710045 |
| Malaihao | 0803710046 |
| Matin-ao | 0803710047 |
| Moguing | 0803710048 |
| Paghudlan | 0803710049 |
| Paitan | 0803710050 |
| Pangdan | 0803710051 |
| Patag | 0803710052 |
| Patong | 0803710053 |
| Pawa | 0803710054 |
| Poblacion District I | 0803710018 |
| Poblacion District II | 0803710019 |
| Poblacion District III | 0803710020 |
| Poblacion District IV | 0803710021 |
| Poblacion District IX | 0803710026 |
| Poblacion District V | 0803710022 |
| Poblacion District VI | 0803710023 |
| Poblacion District VII | 0803710024 |
| Poblacion District VIII | 0803710025 |
| Roxas | 0803710056 |
| Sambel | 0803710057 |
| San Esteban | 0803710058 |
| San Fernando | 0803710059 |
| San Jose East | 0803710061 |
| San Jose West | 0803710062 |
| San Pablo | 0803710063 |
| Tabuanon | 0803710064 |
| Tagadtaran | 0803710065 |
| Taghuyan | 0803710066 |
| Takin | 0803710067 |
| Tambis | 0803710068 |
| Tambuko | 0803710080 |
| Toloyao | 0803710070 |
| Villa Aurora | 0803710071 |
| Villa Corazon | 0803710072 |
| Villa Patria | 0803710073 |
| Villa Rosas | 0803710074 |

## Look up Burauen with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803710000") or cities.lookup("0803710000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Burauen

```python
from barangay import search_fuzzy

for r in search_fuzzy("Burauen", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
