---
title: "Barangays in City of Tarlac, Tarlac — PSGC Codes"
description: "Complete list of 76 barangays in City of Tarlac, Tarlac with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Tarlac, Tarlac

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Tarlac, Tarlac",
  "description": "City in the Philippines with 76 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Tarlac",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Tarlac"
  }
}
</script>

City of Tarlac is a **city** in Tarlac (Philippines) with
**76 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aguso | 0306916001 |
| Alvindia Segundo | 0306916003 |
| Amucao | 0306916004 |
| Armenia | 0306916005 |
| Asturias | 0306916006 |
| Atioc | 0306916007 |
| Balanti | 0306916008 |
| Balete | 0306916009 |
| Balibago I | 0306916010 |
| Balibago II | 0306916011 |
| Balingcanaway | 0306916012 |
| Banaba | 0306916013 |
| Bantog | 0306916014 |
| Baras-baras | 0306916015 |
| Batang-batang | 0306916016 |
| Binauganan | 0306916018 |
| Bora | 0306916019 |
| Buenavista | 0306916020 |
| Buhilit | 0306916021 |
| Burot | 0306916023 |
| Calingcuan | 0306916024 |
| Capehan | 0306916025 |
| Carangian | 0306916026 |
| Care | 0306916099 |
| Central | 0306916027 |
| Culipat | 0306916028 |
| Cut-cut I | 0306916029 |
| Cut-cut II | 0306916030 |
| Dalayap | 0306916031 |
| Dela Paz | 0306916034 |
| Dolores | 0306916035 |
| Laoang | 0306916039 |
| Ligtasan | 0306916041 |
| Lourdes | 0306916042 |
| Mabini | 0306916046 |
| Maligaya | 0306916047 |
| Maliwalo | 0306916048 |
| Mapalacsiao | 0306916050 |
| Mapalad | 0306916051 |
| Matadero | 0306916096 |
| Matatalaib | 0306916052 |
| Paraiso | 0306916056 |
| Poblacion | 0306916057 |
| Salapungan | 0306916097 |
| San Carlos | 0306916058 |
| San Francisco | 0306916059 |
| San Isidro | 0306916060 |
| San Jose | 0306916061 |
| San Jose de Urquico | 0306916062 |
| San Juan de Mata | 0306916064 |
| San Luis | 0306916066 |
| San Manuel | 0306916067 |
| San Miguel | 0306916068 |
| San Nicolas | 0306916069 |
| San Pablo | 0306916070 |
| San Pascual | 0306916071 |
| San Rafael | 0306916072 |
| San Roque | 0306916073 |
| San Sebastian | 0306916074 |
| San Vicente | 0306916075 |
| Santa Cruz | 0306916076 |
| Santa Maria | 0306916077 |
| Santo Cristo | 0306916078 |
| Santo Domingo | 0306916079 |
| Santo Niño | 0306916080 |
| Sapang Maragul | 0306916081 |
| Sapang Tagalog | 0306916082 |
| Sepung Calzada | 0306916083 |
| Sinait | 0306916084 |
| Suizo | 0306916085 |
| Tariji | 0306916087 |
| Tibag | 0306916088 |
| Tibagan | 0306916089 |
| Trinidad | 0306916091 |
| Ungot | 0306916093 |
| Villa Bacolor | 0306916098 |

## Look up Tarlac with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0306916000") or cities.lookup("0306916000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tarlac

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tarlac", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
