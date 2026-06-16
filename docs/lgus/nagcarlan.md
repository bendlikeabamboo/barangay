---
title: "Barangays in Nagcarlan, Laguna — PSGC Codes"
description: "Complete list of 52 barangays in Nagcarlan, Laguna with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Nagcarlan, Laguna

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Nagcarlan, Laguna",
  "description": "Municipality in the Philippines with 52 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Laguna",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Laguna"
  }
}
</script>

Nagcarlan is a **municipality** in Laguna (Philippines) with
**52 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abo | 0403417001 |
| Alibungbungan | 0403417002 |
| Alumbrado | 0403417003 |
| Balayong | 0403417004 |
| Balimbing | 0403417005 |
| Balinacon | 0403417006 |
| Bambang | 0403417007 |
| Banago | 0403417008 |
| Banca-banca | 0403417009 |
| Bangcuro | 0403417010 |
| Banilad | 0403417011 |
| Bayaquitos | 0403417012 |
| Buboy | 0403417013 |
| Buenavista | 0403417014 |
| Buhanginan | 0403417015 |
| Bukal | 0403417016 |
| Bunga | 0403417017 |
| Cabuyew | 0403417018 |
| Calumpang | 0403417019 |
| Kanluran Kabubuhayan | 0403417020 |
| Kanluran Lazaan | 0403417024 |
| Labangan | 0403417022 |
| Lagulo | 0403417026 |
| Lawaguin | 0403417023 |
| Maiit | 0403417027 |
| Malaya | 0403417028 |
| Malinao | 0403417029 |
| Manaol | 0403417030 |
| Maravilla | 0403417031 |
| Nagcalbang | 0403417032 |
| Oples | 0403417036 |
| Palayan | 0403417037 |
| Palina | 0403417038 |
| Poblacion I | 0403417033 |
| Poblacion II | 0403417034 |
| Poblacion III | 0403417035 |
| Sabang | 0403417039 |
| San Francisco | 0403417040 |
| Santa Lucia | 0403417045 |
| Sibulan | 0403417041 |
| Silangan Ilaya | 0403417043 |
| Silangan Kabubuhayan | 0403417021 |
| Silangan Lazaan | 0403417025 |
| Silangan Napapatid | 0403417042 |
| Sinipian | 0403417044 |
| Sulsuguin | 0403417046 |
| Talahib | 0403417047 |
| Talangan | 0403417048 |
| Taytay | 0403417049 |
| Tipacan | 0403417050 |
| Wakat | 0403417052 |
| Yukos | 0403417053 |

## Look up Nagcarlan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0403417000") or cities.lookup("0403417000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Nagcarlan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Nagcarlan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
