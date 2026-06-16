---
title: "Barangays in Boac, Marinduque — PSGC Codes"
description: "Complete list of 61 barangays in Boac, Marinduque with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Boac, Marinduque

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Boac, Marinduque",
  "description": "Municipality in the Philippines with 61 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Marinduque",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Marinduque"
  }
}
</script>

Boac is a **municipality** in Marinduque (Philippines) with
**61 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agot | 1704001001 |
| Agumaymayan | 1704001002 |
| Amoingon | 1704001003 |
| Apitong | 1704001004 |
| Balagasan | 1704001005 |
| Balaring | 1704001006 |
| Balimbing | 1704001007 |
| Balogo | 1704001008 |
| Bamban | 1704001010 |
| Bangbangalon | 1704001009 |
| Bantad | 1704001011 |
| Bantay | 1704001012 |
| Bayuti | 1704001013 |
| Binunga | 1704001014 |
| Boi | 1704001015 |
| Boton | 1704001016 |
| Buliasnin | 1704001017 |
| Bunganay | 1704001018 |
| Caganhao | 1704001020 |
| Canat | 1704001021 |
| Catubugan | 1704001022 |
| Cawit | 1704001023 |
| Daig | 1704001024 |
| Daypay | 1704001025 |
| Duyay | 1704001026 |
| Hinapulan | 1704001029 |
| Ihatub | 1704001027 |
| Isok I | 1704001061 |
| Isok II Pob. | 1704001028 |
| Laylay | 1704001030 |
| Lupac | 1704001031 |
| Mahinhin | 1704001032 |
| Mainit | 1704001033 |
| Malbog | 1704001034 |
| Maligaya | 1704001019 |
| Malusak | 1704001035 |
| Mansiwat | 1704001036 |
| Mataas Na Bayan | 1704001037 |
| Maybo | 1704001038 |
| Mercado | 1704001039 |
| Murallon | 1704001040 |
| Ogbac | 1704001041 |
| Pawa | 1704001042 |
| Pili | 1704001043 |
| Poctoy | 1704001044 |
| Poras | 1704001045 |
| Puting Buhangin | 1704001046 |
| Puyog | 1704001047 |
| Sabong | 1704001048 |
| San Miguel | 1704001049 |
| Santol | 1704001050 |
| Sawi | 1704001051 |
| Tabi | 1704001052 |
| Tabigue | 1704001053 |
| Tagwak | 1704001054 |
| Tambunan | 1704001055 |
| Tampus | 1704001056 |
| Tanza | 1704001057 |
| Tugos | 1704001058 |
| Tumagabok | 1704001059 |
| Tumapon | 1704001060 |

## Look up Boac with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1704001000") or cities.lookup("1704001000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Boac

```python
from barangay import search_fuzzy

for r in search_fuzzy("Boac", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
