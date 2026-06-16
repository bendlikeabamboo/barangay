---
title: "Barangays in Tuguegarao City, Cagayan — PSGC Codes"
description: "Complete list of 49 barangays in Tuguegarao City, Cagayan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tuguegarao City, Cagayan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tuguegarao City, Cagayan",
  "description": "City in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cagayan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cagayan"
  }
}
</script>

Tuguegarao City is a **city** in Cagayan (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Annafunan East | 0201529001 |
| Annafunan West | 0201529038 |
| Atulayan Norte | 0201529002 |
| Atulayan Sur | 0201529039 |
| Bagay | 0201529003 |
| Buntun | 0201529015 |
| Caggay | 0201529016 |
| Capatan | 0201529017 |
| Carig | 0201529018 |
| Caritan Centro | 0201529040 |
| Caritan Norte | 0201529019 |
| Caritan Sur | 0201529020 |
| Cataggaman Nuevo | 0201529021 |
| Cataggaman Pardo | 0201529041 |
| Cataggaman Viejo | 0201529022 |
| Centro 1 | 0201529005 |
| Centro 10 | 0201529013 |
| Centro 11 | 0201529014 |
| Centro 12 | 0201529037 |
| Centro 2 | 0201529035 |
| Centro 3 | 0201529036 |
| Centro 4 | 0201529006 |
| Centro 5 | 0201529007 |
| Centro 6 | 0201529008 |
| Centro 7 | 0201529009 |
| Centro 8 | 0201529010 |
| Centro 9 | 0201529011 |
| Dadda | 0201529042 |
| Gosi Norte | 0201529023 |
| Gosi Sur | 0201529043 |
| Larion Alto | 0201529024 |
| Larion Bajo | 0201529025 |
| Leonarda | 0201529044 |
| Libag Norte | 0201529026 |
| Libag Sur | 0201529045 |
| Linao East | 0201529027 |
| Linao Norte | 0201529046 |
| Linao West | 0201529047 |
| Namabbalan Norte | 0201529029 |
| Namabbalan Sur | 0201529048 |
| Pallua Norte | 0201529030 |
| Pallua Sur | 0201529049 |
| Pengue | 0201529031 |
| Reyes | 0201529050 |
| San Gabriel | 0201529051 |
| Tagga | 0201529032 |
| Tanza | 0201529033 |
| Ugac Norte | 0201529034 |
| Ugac Sur | 0201529052 |

## Look up Tuguegarao City with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0201529000") or cities.lookup("0201529000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tuguegarao City

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tuguegarao City", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
