---
title: "Barangays in City of Bacoor, Cavite — PSGC Codes"
description: "Complete list of 47 barangays in City of Bacoor, Cavite with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Bacoor, Cavite

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Bacoor, Cavite",
  "description": "City in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of Bacoor is a **city** in Cavite (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aniban 1 | 0402103076 |
| Aniban 2 | 0402103077 |
| Bayanan | 0402103004 |
| Dulong Bayan | 0402103007 |
| Habay I | 0402103008 |
| Habay II | 0402103034 |
| Kaingin Digman | 0402103078 |
| Ligas 1 | 0402103079 |
| Ligas 2 | 0402103036 |
| Mabolo | 0402103080 |
| Maliksi 1 | 0402103012 |
| Maliksi 2 | 0402103081 |
| Mambog 1 | 0402103013 |
| Mambog 2 | 0402103082 |
| Mambog 3 | 0402103042 |
| Mambog 4 | 0402103043 |
| Molino I | 0402103014 |
| Molino II | 0402103045 |
| Molino III | 0402103046 |
| Molino IV | 0402103047 |
| Molino V | 0402103048 |
| Molino VI | 0402103049 |
| Molino VII | 0402103050 |
| Niog | 0402103083 |
| P.F. Espiritu 1 | 0402103018 |
| P.F. Espiritu 2 | 0402103084 |
| P.F. Espiritu 3 | 0402103055 |
| P.F. Espiritu 4 | 0402103085 |
| P.F. Espiritu 5 | 0402103058 |
| P.F. Espiritu 6 | 0402103059 |
| Poblacion | 0402103086 |
| Queens Row Central | 0402103026 |
| Queens Row East | 0402103027 |
| Queens Row West | 0402103028 |
| Real | 0402103087 |
| Salinas 2 | 0402103088 |
| Salinas I | 0402103020 |
| San Nicolas 1 | 0402103021 |
| San Nicolas II | 0402103064 |
| San Nicolas III | 0402103065 |
| Sinbanali | 0402103089 |
| Talaba 1 | 0402103090 |
| Talaba 2 | 0402103066 |
| Talaba 3 | 0402103091 |
| Zapote 1 | 0402103092 |
| Zapote 2 | 0402103093 |
| Zapote 3 | 0402103075 |

## Look up Bacoor with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0402103000") or cities.lookup("0402103000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Bacoor

```python
from barangay import search_fuzzy

for r in search_fuzzy("Bacoor", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
