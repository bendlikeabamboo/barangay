---
title: "Barangays in Talipao, Sulu — PSGC Codes"
description: "Complete list of 52 barangays in Talipao, Sulu with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Talipao, Sulu

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Talipao, Sulu",
  "description": "Municipality in the Philippines with 52 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Talipao is a **municipality** in Sulu (Philippines) with
**52 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Andalan | 0906613001 |
| Bagsak | 0906613002 |
| Bandang | 0906613003 |
| Bilaan | 0906613004 |
| Bud Bunga | 0906613007 |
| Buntod | 0906613008 |
| Buroh | 0906613009 |
| Dalih | 0906613010 |
| Gata | 0906613011 |
| Kabatuhan Bilaan | 0906613059 |
| Kabatuhan Tiis | 0906613014 |
| Kabungkol | 0906613015 |
| Kagay | 0906613016 |
| Kahawa | 0906613017 |
| Kandaga | 0906613018 |
| Kanlibot | 0906613019 |
| Kiutaan | 0906613020 |
| Kuhaw | 0906613021 |
| Kulamboh | 0906613023 |
| Kuttong | 0906613024 |
| Lagtoh | 0906613025 |
| Lambanah | 0906613026 |
| Liban | 0906613027 |
| Liu-Bud Pantao | 0906613028 |
| Lower Binuang | 0906613029 |
| Lower Kamuntayan | 0906613030 |
| Lower Laus | 0906613031 |
| Lower Sinumaan | 0906613032 |
| Lower Talipao | 0906613033 |
| Lumbayao | 0906613035 |
| Lumping Pigih Daho | 0906613036 |
| Lungkiaban | 0906613037 |
| Mabahay | 0906613038 |
| Mahala | 0906613039 |
| Mampallam | 0906613040 |
| Marsada | 0906613041 |
| Mauboh | 0906613042 |
| Mungit-mungit | 0906613043 |
| Niog-Sangahan | 0906613044 |
| Pantao | 0906613045 |
| Samak | 0906613047 |
| Talipao Proper | 0906613048 |
| Tampakan | 0906613049 |
| Tiis | 0906613051 |
| Tinggah | 0906613052 |
| Tubod | 0906613053 |
| Tuyang | 0906613054 |
| Upper Binuang | 0906613060 |
| Upper Kamuntayan | 0906613055 |
| Upper Laus | 0906613056 |
| Upper Sinumaan | 0906613057 |
| Upper Talipao | 0906613058 |

## Look up Talipao with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0906613000") or cities.lookup("0906613000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Talipao

```python
from barangay import search_fuzzy

for r in search_fuzzy("Talipao", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
