---
title: "Barangays in City of Calapan, Oriental Mindoro — PSGC Codes"
description: "Complete list of 62 barangays in City of Calapan, Oriental Mindoro with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Calapan, Oriental Mindoro

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Calapan, Oriental Mindoro",
  "description": "City in the Philippines with 62 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Oriental Mindoro",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Oriental Mindoro"
  }
}
</script>

City of Calapan is a **city** in Oriental Mindoro (Philippines) with
**62 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Balingayan | 1705205001 |
| Balite | 1705205002 |
| Baruyan | 1705205003 |
| Batino | 1705205004 |
| Bayanan I | 1705205005 |
| Bayanan II | 1705205006 |
| Biga | 1705205007 |
| Bondoc | 1705205008 |
| Bucayao | 1705205009 |
| Buhuan | 1705205010 |
| Bulusan | 1705205011 |
| Calero | 1705205013 |
| Camansihan | 1705205015 |
| Camilmil | 1705205016 |
| Canubing I | 1705205017 |
| Canubing II | 1705205018 |
| Comunal | 1705205019 |
| Guinobatan | 1705205021 |
| Gulod | 1705205022 |
| Gutad | 1705205023 |
| Ibaba East | 1705205025 |
| Ibaba West | 1705205026 |
| Ilaya | 1705205027 |
| Lalud | 1705205028 |
| Lazareto | 1705205029 |
| Libis | 1705205030 |
| Lumangbayan | 1705205031 |
| Mahal Na Pangalan | 1705205032 |
| Maidlang | 1705205033 |
| Malad | 1705205034 |
| Malamig | 1705205035 |
| Managpi | 1705205036 |
| Masipit | 1705205037 |
| Nag-Iba I | 1705205038 |
| Nag-Iba II | 1705205068 |
| Navotas | 1705205039 |
| Pachoca | 1705205041 |
| Palhi | 1705205042 |
| Panggalaan | 1705205043 |
| Parang | 1705205044 |
| Patas | 1705205045 |
| Personas | 1705205046 |
| Puting Tubig | 1705205047 |
| Salong | 1705205048 |
| San Antonio | 1705205049 |
| San Vicente Central | 1705205050 |
| San Vicente East | 1705205051 |
| San Vicente North | 1705205052 |
| San Vicente South | 1705205053 |
| San Vicente West | 1705205054 |
| Sapul | 1705205058 |
| Silonay | 1705205059 |
| Sta. Cruz | 1705205055 |
| Sta. Isabel | 1705205056 |
| Sta. Maria Village | 1705205061 |
| Sta. Rita | 1705205012 |
| Sto. Niño | 1705205057 |
| Suqui | 1705205062 |
| Tawagan | 1705205063 |
| Tawiran | 1705205064 |
| Tibag | 1705205065 |
| Wawa | 1705205066 |

## Look up Calapan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1705205000") or cities.lookup("1705205000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Calapan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Calapan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
