---
title: "Barangays in Abuyog, Leyte — PSGC Codes"
description: "Complete list of 63 barangays in Abuyog, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Abuyog, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Abuyog, Leyte",
  "description": "Municipality in the Philippines with 63 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Leyte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Leyte"
  }
}
</script>

Abuyog is a **municipality** in Leyte (Philippines) with
**63 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alangilan | 0803701001 |
| Anibongon | 0803701002 |
| Bagacay | 0803701004 |
| Bahay | 0803701005 |
| Balinsasayao | 0803701006 |
| Balocawe | 0803701007 |
| Balocawehay | 0803701008 |
| Barayong | 0803701009 |
| Bayabas | 0803701010 |
| Bito | 0803701011 |
| Buaya | 0803701003 |
| Buenavista | 0803701012 |
| Bulak | 0803701013 |
| Bunga | 0803701014 |
| Buntay | 0803701015 |
| Burubud-an | 0803701016 |
| Cadac-an | 0803701022 |
| Cagbolo | 0803701017 |
| Can-aporong | 0803701019 |
| Can-uguib | 0803701018 |
| Canmarating | 0803701020 |
| Capilian | 0803701021 |
| Combis | 0803701023 |
| Dingle | 0803701024 |
| Guintagbucan | 0803701025 |
| Hampipila | 0803701026 |
| Katipunan | 0803701027 |
| Kikilo | 0803701028 |
| Laray | 0803701029 |
| Lawa-an | 0803701030 |
| Libertad | 0803701031 |
| Loyonsawang | 0803701032 |
| Mag-atubang | 0803701034 |
| Mahagna | 0803701033 |
| Mahayahay | 0803701035 |
| Maitum | 0803701036 |
| Malaguicay | 0803701037 |
| Matagnao | 0803701038 |
| Nalibunan | 0803701039 |
| Nebga | 0803701040 |
| New Taligue | 0803701057 |
| Odiongan | 0803701041 |
| Old Taligue | 0803701058 |
| Pagsang-an | 0803701042 |
| Paguite | 0803701043 |
| Parasanon | 0803701044 |
| Picas Sur | 0803701045 |
| Pilar | 0803701046 |
| Pinamanagan | 0803701047 |
| Salvacion | 0803701048 |
| San Francisco | 0803701049 |
| San Isidro | 0803701050 |
| San Roque | 0803701051 |
| Santa Fe | 0803701052 |
| Santa Lucia | 0803701053 |
| Santo Niño | 0803701054 |
| Tabigue | 0803701055 |
| Tadoc | 0803701056 |
| Tib-o | 0803701059 |
| Tinalian | 0803701060 |
| Tinocolan | 0803701061 |
| Tuy-a | 0803701062 |
| Victory | 0803701063 |

## Look up Abuyog with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803701000") or cities.lookup("0803701000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Abuyog

```python
from barangay import search_fuzzy

for r in search_fuzzy("Abuyog", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
