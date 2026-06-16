---
title: "Barangays in City of Malolos, Bulacan — PSGC Codes"
description: "Complete list of 51 barangays in City of Malolos, Bulacan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Malolos, Bulacan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Malolos, Bulacan",
  "description": "City in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of Malolos is a **city** in Bulacan (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Anilao | 0301410001 |
| Atlag | 0301410002 |
| Babatnin | 0301410003 |
| Bagna | 0301410004 |
| Bagong Bayan | 0301410005 |
| Balayong | 0301410006 |
| Balite | 0301410007 |
| Bangkal | 0301410008 |
| Barihan | 0301410010 |
| Bulihan | 0301410012 |
| Bungahan | 0301410013 |
| Caingin | 0301410016 |
| Calero | 0301410017 |
| Caliligawan | 0301410018 |
| Canalate | 0301410019 |
| Caniogan | 0301410020 |
| Catmon | 0301410021 |
| Cofradia | 0301410056 |
| Dakila | 0301410014 |
| Guinhawa | 0301410015 |
| Liang | 0301410023 |
| Ligas | 0301410022 |
| Longos | 0301410025 |
| Look 1st | 0301410026 |
| Look 2nd | 0301410027 |
| Lugam | 0301410028 |
| Mabolo | 0301410029 |
| Mambog | 0301410031 |
| Masile | 0301410032 |
| Matimbo | 0301410033 |
| Mojon | 0301410034 |
| Namayan | 0301410035 |
| Niugan | 0301410036 |
| Pamarawan | 0301410037 |
| Panasahan | 0301410038 |
| Pinagbakahan | 0301410039 |
| San Agustin | 0301410041 |
| San Gabriel | 0301410042 |
| San Juan | 0301410043 |
| San Pablo | 0301410044 |
| San Vicente | 0301410045 |
| Santiago | 0301410046 |
| Santisima Trinidad | 0301410047 |
| Santo Cristo | 0301410048 |
| Santo Niño | 0301410049 |
| Santo Rosario | 0301410050 |
| Santor | 0301410051 |
| Sumapang Bata | 0301410052 |
| Sumapang Matanda | 0301410053 |
| Taal | 0301410054 |
| Tikay | 0301410055 |

## Look up Malolos with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0301410000") or cities.lookup("0301410000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Malolos

```python
from barangay import search_fuzzy

for r in search_fuzzy("Malolos", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
