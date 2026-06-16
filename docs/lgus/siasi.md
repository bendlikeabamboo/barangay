---
title: "Barangays in Siasi, Sulu — PSGC Codes"
description: "Complete list of 50 barangays in Siasi, Sulu with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Siasi, Sulu

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Siasi, Sulu",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Sulu",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Sulu"
  }
}
</script>

Siasi is a **municipality** in Sulu (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Bakud | 0906612001 |
| Buan | 0906612004 |
| Bulansing Tara | 0906612006 |
| Bulihkullul | 0906612007 |
| Campo Islam | 0906612008 |
| Duggo | 0906612010 |
| Duhol Tara | 0906612011 |
| East Kungtad | 0906612012 |
| East Sisangat | 0906612013 |
| Ipil | 0906612015 |
| Jambangan | 0906612016 |
| Kabubu | 0906612018 |
| Kong-Kong Laminusa | 0906612019 |
| Kud-kud | 0906612020 |
| Kungtad West | 0906612021 |
| Latung | 0906612025 |
| Luuk Laminusa | 0906612023 |
| Luuk Tara | 0906612026 |
| Manta | 0906612030 |
| Minapan | 0906612032 |
| Nipa-nipa | 0906612035 |
| North Laud | 0906612037 |
| North Manta | 0906612038 |
| North Musu Laud | 0906612040 |
| North Silumpak | 0906612041 |
| Pislong | 0906612046 |
| Poblacion | 0906612009 |
| Punungan | 0906612042 |
| Puukan Laminusa | 0906612080 |
| Ratag | 0906612048 |
| Sablay | 0906612049 |
| Sarukot | 0906612050 |
| Siburi | 0906612053 |
| Singko | 0906612056 |
| Siolakan | 0906612057 |
| Siowing | 0906612059 |
| Sipanding | 0906612060 |
| Sisangat | 0906612061 |
| Siundoh | 0906612058 |
| South Musu Laud | 0906612065 |
| South Silumpak | 0906612066 |
| Southwestern Bulikullul | 0906612067 |
| Subah Buaya | 0906612069 |
| Tampakan Laminusa | 0906612070 |
| Tengah Laminusa | 0906612071 |
| Tong Laminusa | 0906612072 |
| Tong-tong | 0906612073 |
| Tonglabah | 0906612074 |
| Tubig Kutah | 0906612075 |
| Tulling | 0906612076 |

## Look up Siasi with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0906612000") or cities.lookup("0906612000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Siasi

```python
from barangay import search_fuzzy

for r in search_fuzzy("Siasi", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
