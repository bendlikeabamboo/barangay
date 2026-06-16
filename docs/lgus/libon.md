---
title: "Barangays in Libon, Albay — PSGC Codes"
description: "Complete list of 47 barangays in Libon, Albay with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Libon, Albay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Libon, Albay",
  "description": "Municipality in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Libon is a **municipality** in Albay (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alongong | 0500507001 |
| Apud | 0500507002 |
| Bacolod | 0500507003 |
| Bariw | 0500507011 |
| Bonbon | 0500507012 |
| Buga | 0500507013 |
| Bulusan | 0500507014 |
| Burabod | 0500507015 |
| Caguscos | 0500507016 |
| East Carisac | 0500507017 |
| Harigue | 0500507019 |
| Libtong | 0500507020 |
| Linao | 0500507021 |
| Mabayawas | 0500507022 |
| Macabugos | 0500507023 |
| Magallang | 0500507024 |
| Malabiga | 0500507025 |
| Marayag | 0500507026 |
| Matara | 0500507027 |
| Molosbolos | 0500507028 |
| Natasan | 0500507029 |
| Niño Jesus | 0500507045 |
| Nogpo | 0500507030 |
| Pantao | 0500507031 |
| Rawis | 0500507033 |
| Sagrada Familia | 0500507034 |
| Salvacion | 0500507035 |
| Sampongan | 0500507036 |
| San Agustin | 0500507037 |
| San Antonio | 0500507038 |
| San Isidro | 0500507039 |
| San Jose | 0500507040 |
| San Pascual | 0500507041 |
| San Ramon | 0500507042 |
| San Vicente | 0500507043 |
| Santa Cruz | 0500507044 |
| Talin-talin | 0500507046 |
| Tambo | 0500507047 |
| Villa Petrona | 0500507049 |
| West Carisac | 0500507018 |
| Zone I | 0500507004 |
| Zone II | 0500507005 |
| Zone III | 0500507006 |
| Zone IV | 0500507007 |
| Zone V | 0500507008 |
| Zone VI | 0500507009 |
| Zone VII | 0500507010 |

## Look up Libon with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0500507000") or cities.lookup("0500507000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Libon

```python
from barangay import search_fuzzy

for r in search_fuzzy("Libon", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
