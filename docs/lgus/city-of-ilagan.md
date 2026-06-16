---
title: "Barangays in City of Ilagan, Isabela — PSGC Codes"
description: "Complete list of 91 barangays in City of Ilagan, Isabela with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Ilagan, Isabela

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Ilagan, Isabela",
  "description": "City in the Philippines with 91 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Isabela",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Isabela"
  }
}
</script>

City of Ilagan is a **city** in Isabela (Philippines) with
**91 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aggasian | 0203114002 |
| Alibagu | 0203114003 |
| Allinguigan 1st | 0203114004 |
| Allinguigan 2nd | 0203114005 |
| Allinguigan 3rd | 0203114006 |
| Arusip | 0203114008 |
| Baculod | 0203114009 |
| Bagong Silang | 0203114101 |
| Bagumbayan | 0203114011 |
| Baligatan | 0203114013 |
| Ballacong | 0203114014 |
| Bangag | 0203114015 |
| Batong-Labang | 0203114017 |
| Bigao | 0203114018 |
| Cabannungan 1st | 0203114023 |
| Cabannungan 2nd | 0203114024 |
| Cabeseria 10 | 0203114051 |
| Cabeseria 14 and 16 | 0203114042 |
| Cabeseria 17 and 21 | 0203114086 |
| Cabeseria 19 | 0203114027 |
| Cabeseria 2 | 0203114044 |
| Cabeseria 22 | 0203114075 |
| Cabeseria 23 | 0203114031 |
| Cabeseria 25 | 0203114029 |
| Cabeseria 27 | 0203114001 |
| Cabeseria 3 | 0203114030 |
| Cabeseria 4 | 0203114020 |
| Cabeseria 5 | 0203114016 |
| Cabeseria 6 &amp; 24 | 0203114025 |
| Cabeseria 7 | 0203114066 |
| Cabeseria 9 and 11 | 0203114039 |
| Cadu | 0203114032 |
| Calamagui 1st | 0203114033 |
| Calamagui 2nd | 0203114034 |
| Camunatan | 0203114035 |
| Capellan | 0203114037 |
| Capo | 0203114038 |
| Carikkikan Norte | 0203114040 |
| Carikkikan Sur | 0203114041 |
| Centro - San Antonio | 0203114079 |
| Centro Poblacion | 0203114100 |
| Fugu | 0203114045 |
| Fuyo | 0203114046 |
| Gayong-Gayong Norte | 0203114047 |
| Gayong-Gayong Sur | 0203114048 |
| Guinatan | 0203114049 |
| Imelda Bliss Village | 0203114102 |
| Lullutan | 0203114050 |
| Malalam | 0203114052 |
| Malasin | 0203114053 |
| Manaring | 0203114054 |
| Mangcuram | 0203114055 |
| Marana I | 0203114057 |
| Marana II | 0203114058 |
| Marana III | 0203114059 |
| Minabang | 0203114060 |
| Morado | 0203114061 |
| Naguilian Norte | 0203114062 |
| Naguilian Sur | 0203114063 |
| Namnama | 0203114064 |
| Nanaguan | 0203114065 |
| Osmeña | 0203114067 |
| Paliueg | 0203114068 |
| Pasa | 0203114070 |
| Pilar | 0203114071 |
| Quimalabasa | 0203114072 |
| Rang-ayan | 0203114073 |
| Rugao | 0203114074 |
| Salindingan | 0203114076 |
| San Andres | 0203114077 |
| San Felipe | 0203114080 |
| San Ignacio | 0203114081 |
| San Isidro | 0203114082 |
| San Juan | 0203114083 |
| San Lorenzo | 0203114084 |
| San Pablo | 0203114085 |
| San Rodrigo | 0203114103 |
| San Vicente | 0203114087 |
| Santa Barbara | 0203114088 |
| Santa Catalina | 0203114089 |
| Santa Isabel Norte | 0203114091 |
| Santa Isabel Sur | 0203114092 |
| Santa Maria | 0203114104 |
| Santa Victoria | 0203114093 |
| Santo Tomas | 0203114094 |
| Siffu | 0203114095 |
| Sindon Bayabo | 0203114096 |
| Sindon Maride | 0203114097 |
| Sipay | 0203114098 |
| Tangcul | 0203114099 |
| Villa Imelda | 0203114056 |

## Look up Ilagan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0203114000") or cities.lookup("0203114000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Ilagan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Ilagan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
