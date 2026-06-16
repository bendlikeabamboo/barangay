---
title: "Barangays in Lemery, Batangas — PSGC Codes"
description: "Complete list of 46 barangays in Lemery, Batangas with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Lemery, Batangas

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Lemery, Batangas",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Batangas",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Batangas"
  }
}
</script>

Lemery is a **municipality** in Batangas (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Anak-Dagat | 0401012001 |
| Arumahan | 0401012002 |
| Ayao-iyao | 0401012003 |
| Bagong Pook | 0401012004 |
| Bagong Sikat | 0401012005 |
| Balanga | 0401012006 |
| Bukal | 0401012007 |
| Cahilan I | 0401012009 |
| Cahilan II | 0401012010 |
| Dayapan | 0401012011 |
| District I | 0401012032 |
| District II | 0401012033 |
| District III | 0401012034 |
| District IV | 0401012035 |
| Dita | 0401012012 |
| Gulod | 0401012013 |
| Lucky | 0401012014 |
| Maguihan | 0401012015 |
| Mahabang Dahilig | 0401012016 |
| Mahayahay | 0401012017 |
| Maigsing Dahilig | 0401012018 |
| Maligaya | 0401012020 |
| Malinis | 0401012021 |
| Masalisi | 0401012022 |
| Mataas Na Bayan | 0401012023 |
| Matingain I | 0401012024 |
| Matingain II | 0401012025 |
| Mayasang | 0401012026 |
| Niugan | 0401012027 |
| Nonong Casto | 0401012028 |
| Palanas | 0401012029 |
| Payapa Ibaba | 0401012030 |
| Payapa Ilaya | 0401012031 |
| Rizal | 0401012036 |
| Sambal Ibaba | 0401012037 |
| Sambal Ilaya | 0401012038 |
| San Isidro Ibaba | 0401012039 |
| San Isidro Itaas | 0401012040 |
| Sangalang | 0401012041 |
| Sinisian East | 0401012048 |
| Sinisian West | 0401012049 |
| Talaga | 0401012043 |
| Tubigan | 0401012044 |
| Tubuan | 0401012045 |
| Wawa Ibaba | 0401012046 |
| Wawa Ilaya | 0401012047 |

## Look up Lemery with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0401012000") or cities.lookup("0401012000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Lemery

```python
from barangay import search_fuzzy

for r in search_fuzzy("Lemery", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
