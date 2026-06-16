---
title: "Barangays in Maasin, Iloilo — PSGC Codes"
description: "Complete list of 50 barangays in Maasin, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Maasin, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Maasin, Iloilo",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Maasin is a **municipality** in Iloilo (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| AGROCEL Pob. | 0603029004 |
| Abay | 0603029001 |
| Abilay | 0603029002 |
| Amerang | 0603029005 |
| Bagacay East | 0603029006 |
| Bagacay West | 0603029007 |
| Bolo | 0603029009 |
| Bug-ot | 0603029008 |
| Bulay | 0603029010 |
| Buntalan | 0603029011 |
| Burak | 0603029012 |
| Cabangcalan | 0603029013 |
| Cabatac | 0603029014 |
| Caigon | 0603029015 |
| Cananghan | 0603029016 |
| Canawili | 0603029017 |
| DELCAR Pob. | 0603029023 |
| Dagami | 0603029020 |
| Daja | 0603029021 |
| Dalusan | 0603029022 |
| Inabasan | 0603029025 |
| Layog | 0603029026 |
| Linab | 0603029029 |
| Liñagan Calsada | 0603029027 |
| Liñagan Tacas | 0603029028 |
| MARI Pob. | 0603029030 |
| Magsaysay | 0603029031 |
| Mandog | 0603029032 |
| Miapa | 0603029033 |
| Nagba | 0603029034 |
| Nasaka | 0603029035 |
| Naslo-Bucao | 0603029036 |
| Nasuli | 0603029037 |
| Panalian | 0603029038 |
| Piandaan East | 0603029039 |
| Piandaan West | 0603029040 |
| Pispis | 0603029041 |
| Punong | 0603029042 |
| Santa Rita | 0603029046 |
| Sinubsuban | 0603029044 |
| Siwalo | 0603029045 |
| Subog | 0603029047 |
| THTP Pob. | 0603029048 |
| Tigbauan | 0603029050 |
| Trangka | 0603029051 |
| Tubang | 0603029052 |
| Tulahong | 0603029053 |
| Tuy-an East | 0603029054 |
| Tuy-an West | 0603029055 |
| Ubian | 0603029056 |

## Look up Maasin with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603029000") or cities.lookup("0603029000")
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
