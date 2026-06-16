---
title: "Barangays in Lopez, Quezon — PSGC Codes"
description: "Complete list of 95 barangays in Lopez, Quezon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Lopez, Quezon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Lopez, Quezon",
  "description": "Municipality in the Philippines with 95 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Quezon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Quezon"
  }
}
</script>

Lopez is a **municipality** in Quezon (Philippines) with
**95 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Bacungan | 0405622001 |
| Bagacay | 0405622002 |
| Banabahin Ibaba | 0405622003 |
| Banabahin Ilaya | 0405622004 |
| Bayabas | 0405622009 |
| Bebito | 0405622010 |
| Bigajo | 0405622011 |
| Binahian A | 0405622012 |
| Binahian B | 0405622013 |
| Binahian C | 0405622014 |
| Bocboc | 0405622015 |
| Buenavista | 0405622016 |
| Burgos | 0405622005 |
| Buyacanin | 0405622017 |
| Cagacag | 0405622018 |
| Calantipayan | 0405622019 |
| Canda Ibaba | 0405622020 |
| Canda Ilaya | 0405622021 |
| Cawayan | 0405622022 |
| Cawayanin | 0405622023 |
| Cogorin Ibaba | 0405622024 |
| Cogorin Ilaya | 0405622025 |
| Concepcion | 0405622026 |
| Danlagan | 0405622027 |
| De La Paz | 0405622028 |
| Del Pilar | 0405622029 |
| Del Rosario | 0405622030 |
| Esperanza Ibaba | 0405622031 |
| Esperanza Ilaya | 0405622032 |
| Gomez | 0405622006 |
| Guihay | 0405622033 |
| Guinuangan | 0405622034 |
| Guites | 0405622035 |
| Hondagua | 0405622037 |
| Ilayang Ilog A | 0405622038 |
| Ilayang Ilog B | 0405622039 |
| Inalusan | 0405622040 |
| Jongo | 0405622041 |
| Lalaguna | 0405622042 |
| Lourdes | 0405622043 |
| Mabanban | 0405622044 |
| Mabini | 0405622045 |
| Magallanes | 0405622046 |
| Magsaysay | 0405622007 |
| Maguilayan | 0405622047 |
| Mahayod-Hayod | 0405622048 |
| Mal-ay | 0405622049 |
| Mandoog | 0405622050 |
| Manguisian | 0405622051 |
| Matinik | 0405622052 |
| Monteclaro | 0405622053 |
| Pamampangin | 0405622054 |
| Pansol | 0405622055 |
| Peñafrancia | 0405622056 |
| Pisipis | 0405622057 |
| Rizal (Poblacion) | 0405622095 |
| Rizal (Rural) | 0405622058 |
| Roma | 0405622059 |
| Rosario | 0405622060 |
| Samat | 0405622061 |
| San Andres | 0405622062 |
| San Antonio | 0405622063 |
| San Francisco A | 0405622064 |
| San Francisco B | 0405622065 |
| San Isidro | 0405622066 |
| San Jose | 0405622067 |
| San Miguel | 0405622068 |
| San Pedro | 0405622069 |
| San Rafael | 0405622070 |
| San Roque | 0405622071 |
| Santa Catalina | 0405622072 |
| Santa Elena | 0405622073 |
| Santa Jacobe | 0405622074 |
| Santa Lucia | 0405622075 |
| Santa Maria | 0405622076 |
| Santa Rosa | 0405622077 |
| Santa Teresa | 0405622096 |
| Santo Niño Ibaba | 0405622078 |
| Santo Niño Ilaya | 0405622079 |
| Silang | 0405622080 |
| Sugod | 0405622081 |
| Sumalang | 0405622082 |
| Talolong | 0405622008 |
| Tan-ag Ibaba | 0405622083 |
| Tan-ag Ilaya | 0405622084 |
| Tocalin | 0405622085 |
| Vegaflor | 0405622086 |
| Vergaña | 0405622087 |
| Veronica | 0405622088 |
| Villa Aurora | 0405622089 |
| Villa Espina | 0405622090 |
| Villa Geda | 0405622092 |
| Villa Hermosa | 0405622091 |
| Villamonte | 0405622093 |
| Villanacaob | 0405622094 |

## Look up Lopez with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0405622000") or cities.lookup("0405622000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Lopez

```python
from barangay import search_fuzzy

for r in search_fuzzy("Lopez", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
