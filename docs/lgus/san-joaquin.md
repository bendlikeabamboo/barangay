---
title: "Barangays in San Joaquin, Iloilo — PSGC Codes"
description: "Complete list of 85 barangays in San Joaquin, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in San Joaquin, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "San Joaquin, Iloilo",
  "description": "Municipality in the Philippines with 85 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

San Joaquin is a **municipality** in Iloilo (Philippines) with
**85 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Amboyu-an | 0603040001 |
| Andres Bonifacio | 0603040002 |
| Antalon | 0603040003 |
| Bad-as | 0603040004 |
| Bagumbayan | 0603040005 |
| Balabago | 0603040006 |
| Baybay | 0603040007 |
| Bayunan | 0603040008 |
| Bolbogan | 0603040010 |
| Bonga | 0603040088 |
| Bucaya | 0603040012 |
| Bulho | 0603040011 |
| Cadluman | 0603040013 |
| Cadoldolan | 0603040014 |
| Camaba-an | 0603040016 |
| Camia | 0603040015 |
| Cata-an | 0603040017 |
| Crossing Dapuyan | 0603040018 |
| Cubay | 0603040019 |
| Cumarascas | 0603040020 |
| Dacdacanan | 0603040021 |
| Danawan | 0603040022 |
| Doldol | 0603040024 |
| Dongoc | 0603040025 |
| Escalantera | 0603040026 |
| Ginot-an | 0603040027 |
| Guibongan Bayunan | 0603040089 |
| Huna | 0603040029 |
| Igbaje | 0603040030 |
| Igbangcal | 0603040031 |
| Igbinangon | 0603040032 |
| Igburi | 0603040033 |
| Igcabutong | 0603040034 |
| Igcadlum | 0603040035 |
| Igcaphang | 0603040036 |
| Igcaratong | 0603040037 |
| Igcondao | 0603040038 |
| Igcores | 0603040039 |
| Igdagmay | 0603040040 |
| Igdomingding | 0603040041 |
| Iglilico | 0603040042 |
| Igpayong | 0603040043 |
| Jawod | 0603040044 |
| Langca | 0603040045 |
| Languanan | 0603040046 |
| Lawigan | 0603040047 |
| Lomboy | 0603040048 |
| Lomboyan | 0603040078 |
| Lopez Vito | 0603040049 |
| Mabini Norte | 0603040050 |
| Mabini Sur | 0603040051 |
| Manhara | 0603040053 |
| Maninila | 0603040054 |
| Masagud | 0603040055 |
| Matambog | 0603040056 |
| Mayunoc | 0603040057 |
| Montinola | 0603040058 |
| Nadsadan | 0603040060 |
| Nagquirisan | 0603040059 |
| Nagsipit | 0603040061 |
| New Gumawan | 0603040062 |
| Panatan | 0603040063 |
| Pitogo | 0603040064 |
| Purok 1 | 0603040065 |
| Purok 2 | 0603040066 |
| Purok 3 | 0603040067 |
| Purok 4 | 0603040068 |
| Purok 5 | 0603040069 |
| Qui-anan | 0603040070 |
| Roma | 0603040071 |
| San Luis | 0603040072 |
| San Mateo Norte | 0603040073 |
| San Mateo Sur | 0603040074 |
| Santa Rita | 0603040079 |
| Santiago | 0603040075 |
| Sinogbuhan | 0603040076 |
| Siwaragan | 0603040077 |
| Talagutac | 0603040080 |
| Tapikan | 0603040081 |
| Taslan | 0603040082 |
| Tiglawa | 0603040083 |
| Tiolas | 0603040084 |
| To-og | 0603040085 |
| Torocadan | 0603040086 |
| Ulay | 0603040087 |

## Look up San Joaquin with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603040000") or cities.lookup("0603040000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in San Joaquin

```python
from barangay import search_fuzzy

for r in search_fuzzy("San Joaquin", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
