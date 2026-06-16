---
title: "Barangays in Camalig, Albay — PSGC Codes"
description: "Complete list of 50 barangays in Camalig, Albay with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Camalig, Albay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Camalig, Albay",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Albay",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Albay"
  }
}
</script>

Camalig is a **municipality** in Albay (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Anoling | 0500502001 |
| Baligang | 0500502002 |
| Bantonan | 0500502003 |
| Barangay 1 | 0500502046 |
| Barangay 2 | 0500502047 |
| Barangay 3 | 0500502048 |
| Barangay 4 | 0500502049 |
| Barangay 5 | 0500502050 |
| Barangay 6 | 0500502051 |
| Barangay 7 | 0500502052 |
| Bariw | 0500502004 |
| Binanderahan | 0500502006 |
| Binitayan | 0500502007 |
| Bongabong | 0500502009 |
| Cabagñan | 0500502010 |
| Cabraran Pequeño | 0500502011 |
| Caguiba | 0500502053 |
| Calabidongan | 0500502012 |
| Comun | 0500502013 |
| Cotmon | 0500502014 |
| Del Rosario | 0500502015 |
| Gapo | 0500502016 |
| Gotob | 0500502017 |
| Ilawod | 0500502018 |
| Iluluan | 0500502019 |
| Libod | 0500502021 |
| Ligban | 0500502022 |
| Mabunga | 0500502023 |
| Magogon | 0500502024 |
| Manawan | 0500502025 |
| Maninila | 0500502026 |
| Mina | 0500502027 |
| Miti | 0500502028 |
| Palanog | 0500502029 |
| Panoypoy | 0500502030 |
| Pariaan | 0500502031 |
| Quinartilan | 0500502032 |
| Quirangay | 0500502033 |
| Quitinday | 0500502034 |
| Salugan | 0500502035 |
| Solong | 0500502036 |
| Sua | 0500502037 |
| Sumlang | 0500502038 |
| Tagaytay | 0500502039 |
| Tagoytoy | 0500502040 |
| Taladong | 0500502041 |
| Taloto | 0500502042 |
| Taplacon | 0500502043 |
| Tinago | 0500502044 |
| Tumpa | 0500502045 |

## Look up Camalig with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0500502000") or cities.lookup("0500502000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Camalig

```python
from barangay import search_fuzzy

for r in search_fuzzy("Camalig", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
