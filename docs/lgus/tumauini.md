---
title: "Barangays in Tumauini, Isabela — PSGC Codes"
description: "Complete list of 46 barangays in Tumauini, Isabela with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tumauini, Isabela

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tumauini, Isabela",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Tumauini is a **municipality** in Isabela (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Annafunan | 0203137001 |
| Antagan I | 0203137002 |
| Antagan II | 0203137003 |
| Arcon | 0203137005 |
| Balug | 0203137007 |
| Banig | 0203137008 |
| Bantug | 0203137009 |
| Barangay District 1 | 0203137037 |
| Barangay District 2 | 0203137038 |
| Barangay District 3 | 0203137039 |
| Barangay District 4 | 0203137040 |
| Bayabo East | 0203137010 |
| Caligayan | 0203137012 |
| Camasi | 0203137013 |
| Carpentero | 0203137014 |
| Compania | 0203137015 |
| Cumabao | 0203137016 |
| Fermeldy | 0203137021 |
| Fugu Abajo | 0203137018 |
| Fugu Norte | 0203137019 |
| Fugu Sur | 0203137020 |
| Lalauanan | 0203137022 |
| Lanna | 0203137023 |
| Lapogan | 0203137024 |
| Lingaling | 0203137025 |
| Liwanag | 0203137026 |
| Malamag East | 0203137029 |
| Malamag West | 0203137030 |
| Maligaya | 0203137031 |
| Minanga | 0203137032 |
| Moldero | 0203137055 |
| Namnama | 0203137033 |
| Paragu | 0203137035 |
| Pilitan | 0203137036 |
| San Mateo | 0203137041 |
| San Pedro | 0203137042 |
| San Vicente | 0203137044 |
| Santa | 0203137045 |
| Sinippil | 0203137048 |
| Sisim Abajo | 0203137050 |
| Sisim Alto | 0203137051 |
| Sta. Catalina | 0203137046 |
| Sta. Visitacion | 0203137027 |
| Sto. Niño | 0203137047 |
| Tunggui | 0203137053 |
| Ugad | 0203137054 |

## Look up Tumauini with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0203137000") or cities.lookup("0203137000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tumauini

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tumauini", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
