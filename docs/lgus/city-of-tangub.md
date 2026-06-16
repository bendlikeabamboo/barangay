---
title: "Barangays in City of Tangub, Misamis Occidental — PSGC Codes"
description: "Complete list of 55 barangays in City of Tangub, Misamis Occidental with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Tangub, Misamis Occidental

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Tangub, Misamis Occidental",
  "description": "City in the Philippines with 55 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Misamis Occidental",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Misamis Occidental"
  }
}
</script>

City of Tangub is a **city** in Misamis Occidental (Philippines) with
**55 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aquino | 1004215050 |
| Balatacan | 1004215002 |
| Baluk | 1004215051 |
| Banglay | 1004215003 |
| Barangay I - City Hall | 1004215012 |
| Barangay II - Marilou Annex | 1004215013 |
| Barangay III- Market Kalubian | 1004215029 |
| Barangay IV - St. Michael | 1004215014 |
| Barangay V - Malubog | 1004215026 |
| Barangay VI - Lower Polao | 1004215023 |
| Barangay VII - Upper Polao | 1004215047 |
| Bintana | 1004215006 |
| Bocator | 1004215007 |
| Bongabong | 1004215008 |
| Caniangan | 1004215009 |
| Capalaran | 1004215010 |
| Catagan | 1004215011 |
| Garang | 1004215016 |
| Guinabot | 1004215017 |
| Guinalaban | 1004215018 |
| Huyohoy | 1004215052 |
| Isidro D. Tan | 1004215015 |
| Kauswagan | 1004215019 |
| Kimat | 1004215020 |
| Labuyo | 1004215021 |
| Lorenzo Tan | 1004215022 |
| Lumban | 1004215024 |
| Maloro | 1004215025 |
| Manga | 1004215027 |
| Mantic | 1004215004 |
| Maquilao | 1004215028 |
| Matugnaw | 1004215053 |
| Migcanaway | 1004215005 |
| Minsubong | 1004215030 |
| Owayan | 1004215031 |
| Paiton | 1004215032 |
| Panalsalan | 1004215033 |
| Pangabuan | 1004215034 |
| Prenza | 1004215035 |
| Salimpuno | 1004215036 |
| San Antonio | 1004215037 |
| San Apolinario | 1004215038 |
| San Vicente | 1004215039 |
| Santa Cruz | 1004215040 |
| Santa Maria | 1004215001 |
| Santo Niño | 1004215041 |
| Sicot | 1004215054 |
| Silanga | 1004215049 |
| Silangit | 1004215042 |
| Simasay | 1004215043 |
| Sumirap | 1004215044 |
| Taguite | 1004215045 |
| Tituron | 1004215046 |
| Tugas | 1004215055 |
| Villaba | 1004215048 |

## Look up Tangub with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1004215000") or cities.lookup("1004215000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tangub

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tangub", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
