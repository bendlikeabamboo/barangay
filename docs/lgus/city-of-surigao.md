---
title: "Barangays in City of Surigao, Surigao del Norte — PSGC Codes"
description: "Complete list of 54 barangays in City of Surigao, Surigao del Norte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Surigao, Surigao del Norte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Surigao, Surigao del Norte",
  "description": "City in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Surigao del Norte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Surigao del Norte"
  }
}
</script>

City of Surigao is a **city** in Surigao del Norte (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alang-alang | 1606724001 |
| Alegria | 1606724002 |
| Anomar | 1606724003 |
| Aurora | 1606724004 |
| Balibayon | 1606724006 |
| Baybay | 1606724007 |
| Bilabid | 1606724008 |
| Bitaugan | 1606724010 |
| Bonifacio | 1606724011 |
| Buenavista | 1606724012 |
| Cabongbongan | 1606724013 |
| Cagniog | 1606724014 |
| Cagutsan | 1606724015 |
| Canlanipa | 1606724096 |
| Cantiasay | 1606724016 |
| Capalayan | 1606724017 |
| Catadman | 1606724018 |
| Danao | 1606724019 |
| Danawan | 1606724020 |
| Day-asan | 1606724021 |
| Ipil | 1606724022 |
| Libuac | 1606724023 |
| Lipata | 1606724024 |
| Lisondra | 1606724025 |
| Luna | 1606724026 |
| Mabini | 1606724027 |
| Mabua | 1606724028 |
| Manyagao | 1606724029 |
| Mapawa | 1606724030 |
| Mat-i | 1606724031 |
| Nabago | 1606724032 |
| Nonoc | 1606724033 |
| Orok | 1606724067 |
| Poctoy | 1606724034 |
| Punta Bilar | 1606724035 |
| Quezon | 1606724036 |
| Rizal | 1606724037 |
| Sabang | 1606724038 |
| San Isidro | 1606724039 |
| San Jose | 1606724040 |
| San Juan | 1606724041 |
| San Pedro | 1606724042 |
| San Roque | 1606724043 |
| Serna | 1606724005 |
| Sidlakan | 1606724044 |
| Silop | 1606724045 |
| Sugbay | 1606724046 |
| Sukailang | 1606724047 |
| Taft | 1606724048 |
| Talisay | 1606724064 |
| Togbongon | 1606724065 |
| Trinidad | 1606724066 |
| Washington | 1606724068 |
| Zaragoza | 1606724095 |

## Look up Surigao with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1606724000") or cities.lookup("1606724000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Surigao

```python
from barangay import search_fuzzy

for r in search_fuzzy("Surigao", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
