---
title: "Barangays in Catanauan, Quezon — PSGC Codes"
description: "Complete list of 46 barangays in Catanauan, Quezon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Catanauan, Quezon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Catanauan, Quezon",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Quezon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Quezon"
  }
}
</script>

Catanauan is a **municipality** in Quezon (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Ajos | 0405610001 |
| Anusan | 0405610002 |
| Barangay 1 | 0405610003 |
| Barangay 10 | 0405610046 |
| Barangay 2 | 0405610004 |
| Barangay 3 | 0405610005 |
| Barangay 4 | 0405610006 |
| Barangay 5 | 0405610007 |
| Barangay 6 | 0405610008 |
| Barangay 7 | 0405610009 |
| Barangay 8 | 0405610010 |
| Barangay 9 | 0405610011 |
| Bolo | 0405610012 |
| Bulagsong | 0405610013 |
| Camandiison | 0405610014 |
| Canculajao | 0405610015 |
| Catumbo | 0405610016 |
| Cawayanin Ibaba | 0405610017 |
| Cawayanin Ilaya | 0405610018 |
| Cutcutan | 0405610019 |
| Dahican | 0405610020 |
| Doongan Ibaba | 0405610021 |
| Doongan Ilaya | 0405610022 |
| Gatasan | 0405610023 |
| Macpac | 0405610024 |
| Madulao | 0405610025 |
| Matandang Sabang Kanluran | 0405610026 |
| Matandang Sabang Silangan | 0405610027 |
| Milagrosa | 0405610028 |
| Navitas | 0405610029 |
| Pacabit | 0405610030 |
| San Antonio Magkupa | 0405610031 |
| San Antonio Pala | 0405610032 |
| San Isidro | 0405610033 |
| San Jose | 0405610034 |
| San Pablo | 0405610035 |
| San Roque | 0405610036 |
| San Vicente Kanluran | 0405610037 |
| San Vicente Silangan | 0405610038 |
| Santa Maria | 0405610039 |
| Tagabas Ibaba | 0405610040 |
| Tagabas Ilaya | 0405610041 |
| Tagbacan Ibaba | 0405610042 |
| Tagbacan Ilaya | 0405610043 |
| Tagbacan Silangan | 0405610044 |
| Tuhian | 0405610045 |

## Look up Catanauan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0405610000") or cities.lookup("0405610000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Catanauan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Catanauan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
