---
title: "Barangays in City of Dasmariñas, Cavite — PSGC Codes"
description: "Complete list of 75 barangays in City of Dasmariñas, Cavite with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Dasmariñas, Cavite

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Dasmari\u00f1as, Cavite",
  "description": "City in the Philippines with 75 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cavite",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cavite"
  }
}
</script>

City of Dasmariñas is a **city** in Cavite (Philippines) with
**75 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Burol | 0402106003 |
| Burol I | 0402106047 |
| Burol II | 0402106048 |
| Burol III | 0402106049 |
| Datu Esmael | 0402106020 |
| Emmanuel Bergado I | 0402106021 |
| Emmanuel Bergado II | 0402106050 |
| Fatima I | 0402106022 |
| Fatima II | 0402106051 |
| Fatima III | 0402106052 |
| H-2 | 0402106080 |
| Langkaan I | 0402106005 |
| Langkaan II | 0402106053 |
| Luzviminda I | 0402106023 |
| Luzviminda II | 0402106054 |
| Paliparan I | 0402106008 |
| Paliparan II | 0402106055 |
| Paliparan III | 0402106056 |
| Sabang | 0402106010 |
| Saint Peter I | 0402106024 |
| Saint Peter II | 0402106057 |
| Salawag | 0402106011 |
| Salitran I | 0402106012 |
| Salitran II | 0402106058 |
| Salitran III | 0402106059 |
| Salitran IV | 0402106060 |
| Sampaloc I | 0402106013 |
| Sampaloc II | 0402106061 |
| Sampaloc III | 0402106062 |
| Sampaloc IV | 0402106063 |
| Sampaloc V | 0402106064 |
| San Agustin I | 0402106014 |
| San Agustin II | 0402106065 |
| San Agustin III | 0402106066 |
| San Andres I | 0402106025 |
| San Andres II | 0402106067 |
| San Antonio De Padua I | 0402106026 |
| San Antonio De Padua II | 0402106068 |
| San Dionisio | 0402106027 |
| San Esteban | 0402106028 |
| San Francisco I | 0402106029 |
| San Francisco II | 0402106069 |
| San Isidro Labrador I | 0402106030 |
| San Isidro Labrador II | 0402106070 |
| San Jose | 0402106015 |
| San Juan | 0402106031 |
| San Lorenzo Ruiz I | 0402106032 |
| San Lorenzo Ruiz II | 0402106071 |
| San Luis I | 0402106033 |
| San Luis II | 0402106072 |
| San Manuel I | 0402106034 |
| San Manuel II | 0402106073 |
| San Mateo | 0402106035 |
| San Miguel | 0402106036 |
| San Miguel II | 0402106074 |
| San Nicolas I | 0402106037 |
| San Nicolas II | 0402106075 |
| San Roque | 0402106038 |
| San Simon | 0402106039 |
| Santa Cristina I | 0402106040 |
| Santa Cristina II | 0402106076 |
| Santa Cruz I | 0402106041 |
| Santa Cruz II | 0402106077 |
| Santa Fe | 0402106042 |
| Santa Lucia | 0402106043 |
| Santa Maria | 0402106044 |
| Santo Cristo | 0402106045 |
| Santo Niño I | 0402106046 |
| Santo Niño II | 0402106078 |
| Victoria Reyes | 0402106081 |
| Zone I | 0402106016 |
| Zone I-B | 0402106079 |
| Zone II | 0402106017 |
| Zone III | 0402106018 |
| Zone IV | 0402106019 |

## Look up Dasmariñas with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0402106000") or cities.lookup("0402106000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Dasmariñas

```python
from barangay import search_fuzzy

for r in search_fuzzy("Dasmariñas", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
