---
title: "Barangays in City of Cagayan De Oro, Region X (Northern Mindanao) — PSGC Codes"
description: "Complete list of 80 barangays in City of Cagayan De Oro, Region X (Northern Mindanao) with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Cagayan De Oro, Region X (Northern Mindanao)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Cagayan De Oro, Region X (Northern Mindanao)",
  "description": "City in the Philippines with 80 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Region X (Northern Mindanao)",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Region X (Northern Mindanao)"
  }
}
</script>

City of Cagayan De Oro is a **city** in Region X (Northern Mindanao) (Philippines) with
**80 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agusan | 1030500001 |
| Baikingon | 1030500002 |
| Balubal | 1030500004 |
| Balulang | 1030500005 |
| Barangay 1 | 1030500073 |
| Barangay 10 | 1030500006 |
| Barangay 11 | 1030500007 |
| Barangay 12 | 1030500008 |
| Barangay 13 | 1030500009 |
| Barangay 14 | 1030500010 |
| Barangay 15 | 1030500011 |
| Barangay 16 | 1030500012 |
| Barangay 17 | 1030500013 |
| Barangay 18 | 1030500014 |
| Barangay 19 | 1030500015 |
| Barangay 2 | 1030500016 |
| Barangay 20 | 1030500075 |
| Barangay 21 | 1030500017 |
| Barangay 22 | 1030500018 |
| Barangay 23 | 1030500019 |
| Barangay 24 | 1030500020 |
| Barangay 25 | 1030500076 |
| Barangay 26 | 1030500021 |
| Barangay 27 | 1030500022 |
| Barangay 28 | 1030500023 |
| Barangay 29 | 1030500077 |
| Barangay 3 | 1030500024 |
| Barangay 30 | 1030500025 |
| Barangay 31 | 1030500078 |
| Barangay 32 | 1030500026 |
| Barangay 33 | 1030500027 |
| Barangay 34 | 1030500028 |
| Barangay 35 | 1030500079 |
| Barangay 36 | 1030500080 |
| Barangay 37 | 1030500081 |
| Barangay 38 | 1030500029 |
| Barangay 39 | 1030500030 |
| Barangay 4 | 1030500031 |
| Barangay 40 | 1030500032 |
| Barangay 5 | 1030500036 |
| Barangay 6 | 1030500033 |
| Barangay 7 | 1030500074 |
| Barangay 8 | 1030500034 |
| Barangay 9 | 1030500035 |
| Bayabas | 1030500037 |
| Bayanga | 1030500038 |
| Besigan | 1030500039 |
| Bonbon | 1030500040 |
| Bugo | 1030500041 |
| Bulua | 1030500003 |
| Camaman-an | 1030500042 |
| Canito-an | 1030500043 |
| Carmen | 1030500044 |
| Consolacion | 1030500045 |
| Cugman | 1030500046 |
| Dansolihon | 1030500047 |
| F. S. Catanico | 1030500048 |
| Gusa | 1030500049 |
| Indahag | 1030500050 |
| Iponan | 1030500051 |
| Kauswagan | 1030500052 |
| Lapasan | 1030500053 |
| Lumbia | 1030500054 |
| Macabalan | 1030500055 |
| Macasandig | 1030500056 |
| Mambuaya | 1030500057 |
| Nazareth | 1030500058 |
| Pagalungan | 1030500059 |
| Pagatpat | 1030500060 |
| Patag | 1030500061 |
| Pigsag-an | 1030500062 |
| Puerto | 1030500063 |
| Puntod | 1030500064 |
| San Simon | 1030500065 |
| Tablon | 1030500067 |
| Taglimao | 1030500068 |
| Tagpangi | 1030500069 |
| Tignapoloan | 1030500070 |
| Tuburan | 1030500071 |
| Tumpagon | 1030500072 |

## Look up Cagayan De Oro with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1030500000") or cities.lookup("1030500000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Cagayan De Oro

```python
from barangay import search_fuzzy

for r in search_fuzzy("Cagayan De Oro", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
