---
title: "Barangays in Basey, Samar — PSGC Codes"
description: "Complete list of 51 barangays in Basey, Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Basey, Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Basey, Samar",
  "description": "Municipality in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Samar"
  }
}
</script>

Basey is a **municipality** in Samar (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Amandayehan | 0806002001 |
| Anglit | 0806002002 |
| Bacubac | 0806002003 |
| Balante | 0806002017 |
| Baloog | 0806002004 |
| Basiao | 0806002005 |
| Baybay | 0806002034 |
| Binongtu-an | 0806002051 |
| Buenavista | 0806002006 |
| Bulao | 0806002052 |
| Burgos | 0806002007 |
| Buscada | 0806002035 |
| Cambayan | 0806002008 |
| Can-abay | 0806002009 |
| Cancaiyas | 0806002010 |
| Canmanila | 0806002011 |
| Catadman | 0806002012 |
| Cogon | 0806002013 |
| Del Pilar | 0806002025 |
| Dolongan | 0806002014 |
| Guintigui-an | 0806002015 |
| Guirang | 0806002016 |
| Iba | 0806002018 |
| Inuntan | 0806002019 |
| Lawa-an | 0806002036 |
| Loog | 0806002021 |
| Loyo | 0806002037 |
| Mabini | 0806002022 |
| Magallanes | 0806002023 |
| Manlilinab | 0806002024 |
| May-it | 0806002026 |
| Mercado | 0806002038 |
| Mongabong | 0806002027 |
| New San Agustin | 0806002028 |
| Nouvelas Occidental | 0806002029 |
| Old San Agustin | 0806002031 |
| Palaypay | 0806002039 |
| Panugmonon | 0806002032 |
| Pelit | 0806002033 |
| Roxas | 0806002041 |
| Salvacion | 0806002042 |
| San Antonio | 0806002043 |
| San Fernando | 0806002030 |
| Sawa | 0806002044 |
| Serum | 0806002045 |
| Sugca | 0806002046 |
| Sugponon | 0806002047 |
| Sulod | 0806002040 |
| Tinaogan | 0806002048 |
| Tingib | 0806002049 |
| Villa Aurora | 0806002050 |

## Look up Basey with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0806002000") or cities.lookup("0806002000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Basey

```python
from barangay import search_fuzzy

for r in search_fuzzy("Basey", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
