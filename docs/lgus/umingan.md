---
title: "Barangays in Umingan, Pangasinan — PSGC Codes"
description: "Complete list of 58 barangays in Umingan, Pangasinan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Umingan, Pangasinan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Umingan, Pangasinan",
  "description": "Municipality in the Philippines with 58 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Pangasinan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Pangasinan"
  }
}
</script>

Umingan is a **municipality** in Pangasinan (Philippines) with
**58 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abot Molina | 0105544001 |
| Alo-o | 0105544002 |
| Amaronan | 0105544003 |
| Annam | 0105544004 |
| Bantug | 0105544005 |
| Baracbac | 0105544006 |
| Barat | 0105544007 |
| Buenavista | 0105544008 |
| Cabalitian | 0105544010 |
| Cabangaran | 0105544060 |
| Cabaruan | 0105544011 |
| Cabatuan | 0105544012 |
| Cadiz | 0105544013 |
| Calitlitan | 0105544014 |
| Capas | 0105544015 |
| Carayungan Sur | 0105544061 |
| Carosalesan | 0105544017 |
| Casilan | 0105544018 |
| Caurdanetaan | 0105544019 |
| Concepcion | 0105544020 |
| Decreto | 0105544021 |
| Del Rosario | 0105544062 |
| Diaz | 0105544022 |
| Diket | 0105544023 |
| Don Justo Abalos | 0105544024 |
| Don Montano | 0105544025 |
| Esperanza | 0105544026 |
| Evangelista | 0105544027 |
| Flores | 0105544028 |
| Fulgosino | 0105544029 |
| Gonzales | 0105544030 |
| La Paz | 0105544031 |
| Labuan | 0105544032 |
| Lauren | 0105544033 |
| Lubong | 0105544034 |
| Luna Este | 0105544036 |
| Luna Weste | 0105544035 |
| Mantacdang | 0105544037 |
| Maseil-seil | 0105544038 |
| Nampalcan | 0105544039 |
| Nancalabasaan | 0105544040 |
| Pangangaan | 0105544041 |
| Papallasen | 0105544042 |
| Pemienta | 0105544044 |
| Poblacion East | 0105544046 |
| Poblacion West | 0105544047 |
| Prado | 0105544048 |
| Resurreccion | 0105544049 |
| Ricos | 0105544050 |
| San Andres | 0105544051 |
| San Juan | 0105544052 |
| San Leon | 0105544053 |
| San Pablo | 0105544054 |
| San Vicente | 0105544055 |
| Santa Maria | 0105544056 |
| Santa Rosa | 0105544057 |
| Sinabaan | 0105544058 |
| Tanggal Sawang | 0105544059 |

## Look up Umingan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0105544000") or cities.lookup("0105544000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Umingan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Umingan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
