---
title: "Barangays in Santa Cruz, Marinduque — PSGC Codes"
description: "Complete list of 55 barangays in Santa Cruz, Marinduque with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Santa Cruz, Marinduque

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Santa Cruz, Marinduque",
  "description": "Municipality in the Philippines with 55 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Marinduque",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Marinduque"
  }
}
</script>

Santa Cruz is a **municipality** in Marinduque (Philippines) with
**55 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alobo | 1704005001 |
| Angas | 1704005002 |
| Aturan | 1704005003 |
| Bagong Silang Pob. | 1704005004 |
| Baguidbirin | 1704005005 |
| Baliis | 1704005006 |
| Balogo | 1704005007 |
| Banahaw Pob. | 1704005008 |
| Bangcuangan | 1704005009 |
| Banogbog | 1704005010 |
| Biga | 1704005011 |
| Botilao | 1704005012 |
| Buyabod | 1704005013 |
| Dating Bayan | 1704005014 |
| Devilla | 1704005015 |
| Dolores | 1704005016 |
| Haguimit | 1704005017 |
| Hupi | 1704005018 |
| Ipil | 1704005019 |
| Jolo | 1704005020 |
| Kaganhao | 1704005021 |
| Kalangkang | 1704005022 |
| Kamandugan | 1704005023 |
| Kasily | 1704005024 |
| Kilo-kilo | 1704005025 |
| Kinyaman | 1704005026 |
| Labo | 1704005027 |
| Lamesa | 1704005028 |
| Landy | 1704005029 |
| Lapu-lapu Pob. | 1704005030 |
| Libjo | 1704005031 |
| Lipa | 1704005032 |
| Lusok | 1704005033 |
| Maharlika Pob. | 1704005034 |
| Makulapnit | 1704005035 |
| Maniwaya | 1704005036 |
| Manlibunan | 1704005037 |
| Masaguisi | 1704005038 |
| Masalukot | 1704005039 |
| Matalaba | 1704005040 |
| Mongpong | 1704005041 |
| Morales | 1704005042 |
| Napo | 1704005043 |
| Pag-Asa Pob. | 1704005044 |
| Pantayin | 1704005045 |
| Polo | 1704005047 |
| Pulong-Parang | 1704005048 |
| Punong | 1704005049 |
| San Antonio | 1704005050 |
| San Isidro | 1704005051 |
| Tagum | 1704005052 |
| Tamayo | 1704005053 |
| Tambangan | 1704005054 |
| Tawiran | 1704005055 |
| Taytay | 1704005056 |

## Look up Santa Cruz with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1704005000") or cities.lookup("1704005000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Santa Cruz

```python
from barangay import search_fuzzy

for r in search_fuzzy("Santa Cruz", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
