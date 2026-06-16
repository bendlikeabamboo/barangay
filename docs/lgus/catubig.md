---
title: "Barangays in Catubig, Northern Samar — PSGC Codes"
description: "Complete list of 47 barangays in Catubig, Northern Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Catubig, Northern Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Catubig, Northern Samar",
  "description": "Municipality in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Northern Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Northern Samar"
  }
}
</script>

Catubig is a **municipality** in Northern Samar (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Anongo | 0804806001 |
| Barangay 1 | 0804806045 |
| Barangay 2 | 0804806046 |
| Barangay 3 | 0804806047 |
| Barangay 4 | 0804806048 |
| Barangay 5 | 0804806049 |
| Barangay 6 | 0804806050 |
| Barangay 7 | 0804806051 |
| Barangay 8 | 0804806052 |
| Bonifacio | 0804806003 |
| Boring | 0804806004 |
| Cagbugna | 0804806005 |
| Cagmanaba | 0804806006 |
| Cagogobngan | 0804806008 |
| Calingnan | 0804806009 |
| Canuctan | 0804806010 |
| Claro M. Recto | 0804806020 |
| D. Mercader | 0804806002 |
| Guibwangan | 0804806011 |
| Hinagonoyan | 0804806013 |
| Hiparayan | 0804806014 |
| Hitapi-an | 0804806015 |
| Inoburan | 0804806016 |
| Irawahan | 0804806017 |
| Lenoyahan | 0804806021 |
| Libon | 0804806018 |
| Magongon | 0804806023 |
| Magtuad | 0804806024 |
| Manering | 0804806025 |
| Nabulo | 0804806026 |
| Nagoocan | 0804806027 |
| Nahulid | 0804806028 |
| Opong | 0804806029 |
| Osang | 0804806030 |
| Osmeña | 0804806031 |
| P. Rebadulla | 0804806032 |
| Roxas | 0804806033 |
| Sagudsuron | 0804806034 |
| San Antonio | 0804806035 |
| San Francisco | 0804806036 |
| San Jose | 0804806037 |
| San Vicente | 0804806038 |
| Santa Fe | 0804806039 |
| Sulitan | 0804806040 |
| Tangbo | 0804806042 |
| Tungodnon | 0804806043 |
| Vienna Maria | 0804806044 |

## Look up Catubig with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0804806000") or cities.lookup("0804806000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Catubig

```python
from barangay import search_fuzzy

for r in search_fuzzy("Catubig", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
