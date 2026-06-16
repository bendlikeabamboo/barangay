---
title: "Barangays in City of San Jose Del Monte, Bulacan — PSGC Codes"
description: "Complete list of 62 barangays in City of San Jose Del Monte, Bulacan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of San Jose Del Monte, Bulacan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of San Jose Del Monte, Bulacan",
  "description": "City in the Philippines with 62 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Bulacan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Bulacan"
  }
}
</script>

City of San Jose Del Monte is a **city** in Bulacan (Philippines) with
**62 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Assumption | 0301420019 |
| Bagong Buhay I | 0301420001 |
| Bagong Buhay II | 0301420020 |
| Bagong Buhay III | 0301420021 |
| Citrus | 0301420012 |
| Ciudad Real | 0301420022 |
| Dulong Bayan | 0301420002 |
| Fatima I | 0301420015 |
| Fatima II | 0301420023 |
| Fatima III | 0301420024 |
| Fatima IV | 0301420025 |
| Fatima V | 0301420026 |
| Francisco Homes-Guijo | 0301420027 |
| Francisco Homes-Mulawin | 0301420028 |
| Francisco Homes-Narra | 0301420029 |
| Francisco Homes-Yakal | 0301420030 |
| Gaya-gaya | 0301420003 |
| Graceville | 0301420031 |
| Gumaoc Central | 0301420032 |
| Gumaoc East | 0301420033 |
| Gumaoc West | 0301420034 |
| Kaybanban | 0301420005 |
| Kaypian | 0301420004 |
| Lawang Pari | 0301420035 |
| Maharlika | 0301420036 |
| Minuyan I | 0301420006 |
| Minuyan II | 0301420037 |
| Minuyan III | 0301420038 |
| Minuyan IV | 0301420039 |
| Minuyan Proper | 0301420041 |
| Minuyan V | 0301420040 |
| Muzon East | 0301420060 |
| Muzon Proper | 0301420007 |
| Muzon South | 0301420061 |
| Muzon West | 0301420062 |
| Paradise III | 0301420042 |
| Poblacion | 0301420008 |
| Poblacion I | 0301420043 |
| San Isidro | 0301420044 |
| San Manuel | 0301420045 |
| San Martin I | 0301420013 |
| San Martin II | 0301420046 |
| San Martin III | 0301420047 |
| San Martin IV | 0301420048 |
| San Martin de Porres | 0301420059 |
| San Pedro | 0301420016 |
| San Rafael I | 0301420049 |
| San Rafael II | 0301420017 |
| San Rafael III | 0301420050 |
| San Rafael IV | 0301420051 |
| San Rafael V | 0301420052 |
| San Roque | 0301420053 |
| Santa Cruz I | 0301420014 |
| Santa Cruz II | 0301420054 |
| Santa Cruz III | 0301420055 |
| Santa Cruz IV | 0301420056 |
| Santa Cruz V | 0301420057 |
| Santo Cristo | 0301420009 |
| Santo Niño I | 0301420018 |
| Santo Niño II | 0301420058 |
| Sapang Palay | 0301420010 |
| Tungkong Mangga | 0301420011 |

## Look up San Jose Del Monte with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0301420000") or cities.lookup("0301420000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in San Jose Del Monte

```python
from barangay import search_fuzzy

for r in search_fuzzy("San Jose Del Monte", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
