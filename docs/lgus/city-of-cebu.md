---
title: "Barangays in City of Cebu, Region VII (Central Visayas) — PSGC Codes"
description: "Complete list of 80 barangays in City of Cebu, Region VII (Central Visayas) with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Cebu, Region VII (Central Visayas)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Cebu, Region VII (Central Visayas)",
  "description": "City in the Philippines with 80 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Region VII (Central Visayas)",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Region VII (Central Visayas)"
  }
}
</script>

City of Cebu is a **city** in Region VII (Central Visayas) (Philippines) with
**80 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adlaon | 0730600001 |
| Agsungot | 0730600002 |
| Apas | 0730600003 |
| Babag | 0730600004 |
| Bacayan | 0730600006 |
| Banilad | 0730600007 |
| Basak Pardo | 0730600005 |
| Basak San Nicolas | 0730600008 |
| Binaliw | 0730600010 |
| Bonbon | 0730600011 |
| Budla-an | 0730600013 |
| Buhisan | 0730600014 |
| Bulacao | 0730600015 |
| Buot-Taup Pardo | 0730600016 |
| Busay | 0730600017 |
| Calamba | 0730600018 |
| Cambinocot | 0730600019 |
| Camputhaw | 0730600036 |
| Capitol Site | 0730600020 |
| Carreta | 0730600021 |
| Central | 0730600022 |
| Cogon Pardo | 0730600024 |
| Cogon Ramos | 0730600023 |
| Day-as | 0730600025 |
| Duljo | 0730600027 |
| Ermita | 0730600028 |
| Guadalupe | 0730600029 |
| Guba | 0730600030 |
| Hippodromo | 0730600031 |
| Inayawan | 0730600032 |
| Kalubihan | 0730600033 |
| Kalunasan | 0730600034 |
| Kamagayan | 0730600035 |
| Kasambagan | 0730600037 |
| Kinasang-an Pardo | 0730600038 |
| Labangon | 0730600040 |
| Lahug | 0730600041 |
| Lorega | 0730600042 |
| Lusaran | 0730600043 |
| Luz | 0730600044 |
| Mabini | 0730600045 |
| Mabolo | 0730600046 |
| Malubog | 0730600048 |
| Mambaling | 0730600049 |
| Pahina Central | 0730600050 |
| Pahina San Nicolas | 0730600051 |
| Pamutan | 0730600052 |
| Pardo | 0730600053 |
| Pari-an | 0730600054 |
| Paril | 0730600055 |
| Pasil | 0730600056 |
| Pit-os | 0730600057 |
| Pulangbato | 0730600059 |
| Pung-ol-Sibugay | 0730600060 |
| Punta Princesa | 0730600062 |
| Quiot Pardo | 0730600063 |
| Sambag I | 0730600064 |
| Sambag II | 0730600065 |
| San Antonio | 0730600066 |
| San Jose | 0730600067 |
| San Nicolas Central | 0730600068 |
| San Roque | 0730600069 |
| Santa Cruz | 0730600070 |
| Sapangdaku | 0730600077 |
| Sawang Calero | 0730600071 |
| Sinsin | 0730600073 |
| Sirao | 0730600074 |
| Suba Pob. | 0730600075 |
| Sudlon I | 0730600076 |
| Sudlon II | 0730600088 |
| T. Padilla | 0730600078 |
| Tabunan | 0730600079 |
| Tagbao | 0730600080 |
| Talamban | 0730600081 |
| Taptap | 0730600082 |
| Tejero | 0730600083 |
| Tinago | 0730600084 |
| Tisa | 0730600085 |
| To-ong Pardo | 0730600086 |
| Zapatera | 0730600087 |

## Look up Cebu with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0730600000") or cities.lookup("0730600000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Cebu

```python
from barangay import search_fuzzy

for r in search_fuzzy("Cebu", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
