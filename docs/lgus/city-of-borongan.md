---
title: "Barangays in City of Borongan, Eastern Samar — PSGC Codes"
description: "Complete list of 61 barangays in City of Borongan, Eastern Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Borongan, Eastern Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Borongan, Eastern Samar",
  "description": "City in the Philippines with 61 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Eastern Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Eastern Samar"
  }
}
</script>

City of Borongan is a **city** in Eastern Samar (Philippines) with
**61 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alang-alang | 0802604001 |
| Amantacop | 0802604002 |
| Ando | 0802604003 |
| Balacdas | 0802604004 |
| Balud | 0802604005 |
| Banuyo | 0802604006 |
| Baras | 0802604007 |
| Bato | 0802604008 |
| Bayobay | 0802604009 |
| Benowangan | 0802604010 |
| Bugas | 0802604011 |
| Cabalagnan | 0802604012 |
| Cabong | 0802604013 |
| Cagbonga | 0802604014 |
| Calico-an | 0802604015 |
| Calingatngan | 0802604016 |
| Camada | 0802604020 |
| Campesao | 0802604017 |
| Can-abong | 0802604018 |
| Can-aga | 0802604019 |
| Canjaway | 0802604021 |
| Canlaray | 0802604022 |
| Canyopay | 0802604023 |
| Divinubo | 0802604024 |
| Hebacong | 0802604025 |
| Hindang | 0802604026 |
| Lalawigan | 0802604027 |
| Libuton | 0802604028 |
| Locso-on | 0802604029 |
| Maybacong | 0802604030 |
| Maypangdan | 0802604031 |
| Pepelitan | 0802604032 |
| Pinanag-an | 0802604033 |
| Punta Maria | 0802604043 |
| Purok A | 0802604035 |
| Purok B | 0802604036 |
| Purok C | 0802604037 |
| Purok D1 | 0802604034 |
| Purok D2 | 0802604038 |
| Purok E | 0802604039 |
| Purok F | 0802604040 |
| Purok G | 0802604041 |
| Purok H | 0802604042 |
| Sabang North | 0802604044 |
| Sabang South | 0802604045 |
| San Andres | 0802604046 |
| San Gabriel | 0802604047 |
| San Gregorio | 0802604048 |
| San Jose | 0802604049 |
| San Mateo | 0802604050 |
| San Pablo | 0802604051 |
| San Saturnino | 0802604052 |
| Santa Fe | 0802604053 |
| Siha | 0802604054 |
| Sohutan | 0802604056 |
| Songco | 0802604055 |
| Suribao | 0802604057 |
| Surok | 0802604058 |
| Taboc | 0802604059 |
| Tabunan | 0802604060 |
| Tamoso | 0802604061 |

## Look up Borongan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0802604000") or cities.lookup("0802604000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Borongan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Borongan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
