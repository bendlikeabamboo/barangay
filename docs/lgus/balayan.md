---
title: "Barangays in Balayan, Batangas — PSGC Codes"
description: "Complete list of 48 barangays in Balayan, Batangas with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Balayan, Batangas

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Balayan, Batangas",
  "description": "Municipality in the Philippines with 48 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Balayan is a **municipality** in Batangas (Philippines) with
**48 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Baclaran | 0401003001 |
| Barangay 1 | 0401003003 |
| Barangay 10 | 0401003004 |
| Barangay 11 | 0401003005 |
| Barangay 12 | 0401003006 |
| Barangay 2 | 0401003007 |
| Barangay 3 | 0401003008 |
| Barangay 4 | 0401003009 |
| Barangay 5 | 0401003010 |
| Barangay 6 | 0401003011 |
| Barangay 7 | 0401003012 |
| Barangay 8 | 0401003013 |
| Barangay 9 | 0401003014 |
| Calan | 0401003016 |
| Caloocan | 0401003017 |
| Calzada | 0401003018 |
| Canda | 0401003019 |
| Carenahan | 0401003020 |
| Caybunga | 0401003021 |
| Cayponce | 0401003022 |
| Dalig | 0401003023 |
| Dao | 0401003024 |
| Dilao | 0401003025 |
| Duhatan | 0401003026 |
| Durungao | 0401003027 |
| Gimalas | 0401003028 |
| Gumamela | 0401003029 |
| Lagnas | 0401003030 |
| Lanatan | 0401003031 |
| Langgangan | 0401003032 |
| Lucban Pook | 0401003034 |
| Lucban Putol | 0401003033 |
| Magabe | 0401003035 |
| Malalay | 0401003036 |
| Munting Tubig | 0401003037 |
| Navotas | 0401003038 |
| Palikpikan | 0401003040 |
| Patugo | 0401003039 |
| Pooc | 0401003042 |
| Sambat | 0401003043 |
| Sampaga | 0401003044 |
| San Juan | 0401003045 |
| San Piro | 0401003046 |
| Santol | 0401003048 |
| Sukol | 0401003049 |
| Tactac | 0401003050 |
| Taludtud | 0401003051 |
| Tanggoy | 0401003052 |

## Look up Balayan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0401003000") or cities.lookup("0401003000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Balayan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Balayan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
