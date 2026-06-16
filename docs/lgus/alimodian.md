---
title: "Barangays in Alimodian, Iloilo — PSGC Codes"
description: "Complete list of 51 barangays in Alimodian, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Alimodian, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Alimodian, Iloilo",
  "description": "Municipality in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Alimodian is a **municipality** in Iloilo (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abang-abang | 0603002001 |
| Agsing | 0603002002 |
| Atabay | 0603002003 |
| Ba-ong | 0603002004 |
| Bagsakan | 0603002006 |
| Baguingin-Lanot | 0603002005 |
| Bagumbayan-Ilajas | 0603002007 |
| Balabago | 0603002008 |
| Ban-ag | 0603002009 |
| Bancal | 0603002010 |
| Binalud | 0603002011 |
| Bugang | 0603002012 |
| Buhay | 0603002014 |
| Bulod | 0603002015 |
| Cabacanan Proper | 0603002017 |
| Cabacanan Rizal | 0603002018 |
| Cagay | 0603002019 |
| Coline | 0603002020 |
| Coline-Dalag | 0603002021 |
| Cunsad | 0603002022 |
| Cuyad | 0603002023 |
| Dalid | 0603002024 |
| Dao | 0603002025 |
| Gines | 0603002026 |
| Ginomoy | 0603002027 |
| Ingwan | 0603002028 |
| Laylayan | 0603002029 |
| Lico | 0603002030 |
| Luan-luan | 0603002031 |
| Malamboy-Bondolan | 0603002033 |
| Malamhay | 0603002032 |
| Mambawi | 0603002034 |
| Manasa | 0603002035 |
| Manduyog | 0603002036 |
| Pajo | 0603002037 |
| Pianda-an Norte | 0603002038 |
| Pianda-an Sur | 0603002039 |
| Poblacion | 0603002054 |
| Punong | 0603002041 |
| Quinaspan | 0603002042 |
| Sinamay | 0603002043 |
| Sulong | 0603002044 |
| Taban-Manguining | 0603002045 |
| Tabug | 0603002046 |
| Tarug | 0603002047 |
| Tugaslon | 0603002048 |
| Ubodan | 0603002049 |
| Ugbo | 0603002050 |
| Ulay-Bugang | 0603002051 |
| Ulay-Hinablan | 0603002052 |
| Umingan | 0603002053 |

## Look up Alimodian with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603002000") or cities.lookup("0603002000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Alimodian

```python
from barangay import search_fuzzy

for r in search_fuzzy("Alimodian", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
