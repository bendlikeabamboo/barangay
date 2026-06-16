---
title: "Barangays in Bacacay, Albay — PSGC Codes"
description: "Complete list of 56 barangays in Bacacay, Albay with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Bacacay, Albay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Bacacay, Albay",
  "description": "Municipality in the Philippines with 56 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Albay",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Albay"
  }
}
</script>

Bacacay is a **municipality** in Albay (Philippines) with
**56 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Baclayon | 0500501001 |
| Banao | 0500501002 |
| Barangay 1 | 0500501032 |
| Barangay 10 | 0500501033 |
| Barangay 11 | 0500501034 |
| Barangay 12 | 0500501035 |
| Barangay 13 | 0500501036 |
| Barangay 14 | 0500501037 |
| Barangay 2 | 0500501038 |
| Barangay 3 | 0500501039 |
| Barangay 4 | 0500501040 |
| Barangay 5 | 0500501041 |
| Barangay 6 | 0500501042 |
| Barangay 7 | 0500501043 |
| Barangay 8 | 0500501044 |
| Barangay 9 | 0500501045 |
| Bariw | 0500501003 |
| Basud | 0500501004 |
| Bayandong | 0500501005 |
| Bonga | 0500501006 |
| Buang | 0500501008 |
| Busdac | 0500501048 |
| Cabasan | 0500501009 |
| Cagbulacao | 0500501010 |
| Cagraray | 0500501011 |
| Cajogutan | 0500501012 |
| Cawayan | 0500501013 |
| Damacan | 0500501014 |
| Gubat Ilawod | 0500501015 |
| Gubat Iraya | 0500501016 |
| Hindi | 0500501017 |
| Igang | 0500501018 |
| Langaton | 0500501019 |
| Manaet | 0500501020 |
| Mapulang Daga | 0500501021 |
| Mataas | 0500501022 |
| Misibis | 0500501023 |
| Nahapunan | 0500501024 |
| Namanday | 0500501025 |
| Namantao | 0500501026 |
| Napao | 0500501027 |
| Panarayon | 0500501028 |
| Pigcobohan | 0500501029 |
| Pili Ilawod | 0500501030 |
| Pili Iraya | 0500501031 |
| Pongco | 0500501046 |
| San Pablo | 0500501049 |
| San Pedro | 0500501050 |
| Sogod | 0500501051 |
| Sula | 0500501052 |
| Tambilagao | 0500501053 |
| Tambongon | 0500501054 |
| Tanagan | 0500501055 |
| Uson | 0500501056 |
| Vinisitahan-Basud | 0500501057 |
| Vinisitahan-Napao | 0500501058 |

## Look up Bacacay with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0500501000") or cities.lookup("0500501000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Bacacay

```python
from barangay import search_fuzzy

for r in search_fuzzy("Bacacay", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
