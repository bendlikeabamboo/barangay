---
title: "Barangays in Tuburan, Cebu — PSGC Codes"
description: "Complete list of 54 barangays in Tuburan, Cebu with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tuburan, Cebu

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tuburan, Cebu",
  "description": "Municipality in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cebu",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cebu"
  }
}
</script>

Tuburan is a **municipality** in Cebu (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alegria | 0702252001 |
| Amatugan | 0702252002 |
| Antipolo | 0702252003 |
| Apalan | 0702252004 |
| Bagasawe | 0702252005 |
| Bakyawan | 0702252006 |
| Bangkito | 0702252007 |
| Barangay I | 0702252048 |
| Barangay II | 0702252049 |
| Barangay III | 0702252050 |
| Barangay IV | 0702252051 |
| Barangay V | 0702252052 |
| Barangay VI | 0702252053 |
| Barangay VII | 0702252054 |
| Barangay VIII | 0702252055 |
| Bulwang | 0702252008 |
| Caridad | 0702252015 |
| Carmelo | 0702252016 |
| Cogon | 0702252017 |
| Colonia | 0702252018 |
| Daan Lungsod | 0702252019 |
| Fortaliza | 0702252020 |
| Ga-ang | 0702252021 |
| Gimama-a | 0702252022 |
| Jagbuaya | 0702252023 |
| Kabangkalan | 0702252009 |
| Kabkaban | 0702252024 |
| Kagba-o | 0702252025 |
| Kalangahan | 0702252010 |
| Kamansi | 0702252011 |
| Kampoot | 0702252026 |
| Kan-an | 0702252012 |
| Kanlunsing | 0702252013 |
| Kansi | 0702252014 |
| Kaorasan | 0702252027 |
| Libo | 0702252028 |
| Lusong | 0702252029 |
| Macupa | 0702252030 |
| Mag-alwa | 0702252031 |
| Mag-antoy | 0702252032 |
| Mag-atubang | 0702252033 |
| Maghan-ay | 0702252034 |
| Mangga | 0702252035 |
| Marmol | 0702252036 |
| Molobolo | 0702252037 |
| Montealegre | 0702252038 |
| Putat | 0702252040 |
| San Juan | 0702252041 |
| Sandayong | 0702252042 |
| Santo Niño | 0702252043 |
| Siotes | 0702252044 |
| Sumon | 0702252045 |
| Tominjao | 0702252046 |
| Tomugpa | 0702252047 |

## Look up Tuburan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0702252000") or cities.lookup("0702252000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tuburan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tuburan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
