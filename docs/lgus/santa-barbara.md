---
title: "Barangays in Santa Barbara, Iloilo — PSGC Codes"
description: "Complete list of 60 barangays in Santa Barbara, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Santa Barbara, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Santa Barbara, Iloilo",
  "description": "Municipality in the Philippines with 60 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Iloilo",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Iloilo"
  }
}
</script>

Santa Barbara is a **municipality** in Iloilo (Philippines) with
**60 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agusipan | 0603043001 |
| Agutayan | 0603043002 |
| Bagumbayan | 0603043003 |
| Balabag | 0603043004 |
| Balibagan Este | 0603043005 |
| Balibagan Oeste | 0603043006 |
| Ban-ag | 0603043007 |
| Bantay | 0603043008 |
| Barangay Zone I | 0603043009 |
| Barangay Zone II | 0603043010 |
| Barangay Zone III | 0603043011 |
| Barangay Zone IV | 0603043012 |
| Barangay Zone V | 0603043013 |
| Barangay Zone VI | 0603043061 |
| Barasan Este | 0603043014 |
| Barasan Oeste | 0603043015 |
| Binangkilan | 0603043016 |
| Bitaog-Taytay | 0603043017 |
| Bolong Este | 0603043018 |
| Bolong Oeste | 0603043019 |
| Buayahon | 0603043020 |
| Buyo | 0603043021 |
| Cabugao Norte | 0603043022 |
| Cabugao Sur | 0603043023 |
| Cadagmayan Norte | 0603043024 |
| Cadagmayan Sur | 0603043025 |
| Cafe | 0603043026 |
| Calaboa Este | 0603043027 |
| Calaboa Oeste | 0603043028 |
| Camambugan | 0603043029 |
| Canipayan | 0603043030 |
| Conaynay | 0603043032 |
| Daga | 0603043033 |
| Dalid | 0603043034 |
| Duyanduyan | 0603043035 |
| Gen. Martin T. Delgado | 0603043036 |
| Guno | 0603043037 |
| Inangayan | 0603043038 |
| Jibao-an | 0603043039 |
| Lacadon | 0603043040 |
| Lanag | 0603043041 |
| Lupa | 0603043042 |
| Magancina | 0603043043 |
| Malawog | 0603043044 |
| Mambuyo | 0603043045 |
| Manhayang | 0603043046 |
| Miraga-Guibuangan | 0603043047 |
| Nasugban | 0603043048 |
| Omambog | 0603043049 |
| Pal-Agon | 0603043050 |
| Pungsod | 0603043051 |
| San Sebastian | 0603043052 |
| Sangcate | 0603043053 |
| Tagsing | 0603043054 |
| Talanghauan | 0603043055 |
| Talongadian | 0603043056 |
| Tigtig | 0603043057 |
| Tuburan | 0603043059 |
| Tugas | 0603043060 |
| Tungay | 0603043058 |

## Look up Santa Barbara with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603043000") or cities.lookup("0603043000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Santa Barbara

```python
from barangay import search_fuzzy

for r in search_fuzzy("Santa Barbara", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
