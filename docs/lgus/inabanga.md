---
title: "Barangays in Inabanga, Bohol — PSGC Codes"
description: "Complete list of 50 barangays in Inabanga, Bohol with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Inabanga, Bohol

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Inabanga, Bohol",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Bohol",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Bohol"
  }
}
</script>

Inabanga is a **municipality** in Bohol (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Anonang | 0701224001 |
| Badiang | 0701224003 |
| Baguhan | 0701224005 |
| Bahan | 0701224002 |
| Banahao | 0701224007 |
| Baogo | 0701224008 |
| Bugang | 0701224009 |
| Cagawasan | 0701224010 |
| Cagayan | 0701224011 |
| Cambitoon | 0701224012 |
| Canlinte | 0701224013 |
| Cawayan | 0701224014 |
| Cogon | 0701224015 |
| Cuaming | 0701224016 |
| Dagnawan | 0701224017 |
| Dagohoy | 0701224018 |
| Dait Sur | 0701224019 |
| Datag | 0701224020 |
| Fatima | 0701224021 |
| Hambongan | 0701224022 |
| Ilaud | 0701224023 |
| Ilaya | 0701224024 |
| Ilihan | 0701224025 |
| Lapacan Norte | 0701224027 |
| Lapacan Sur | 0701224028 |
| Lawis | 0701224029 |
| Liloan Norte | 0701224030 |
| Liloan Sur | 0701224031 |
| Lomboy | 0701224032 |
| Lonoy Cainsican | 0701224033 |
| Lonoy Roma | 0701224034 |
| Lutao | 0701224035 |
| Luyo | 0701224036 |
| Mabuhay | 0701224037 |
| Maria Rosario | 0701224038 |
| Nabuad | 0701224039 |
| Napo | 0701224040 |
| Ondol | 0701224041 |
| Poblacion | 0701224042 |
| Riverside | 0701224043 |
| Saa | 0701224044 |
| San Isidro | 0701224045 |
| San Jose | 0701224046 |
| Santo Niño | 0701224047 |
| Santo Rosario | 0701224048 |
| Sua | 0701224049 |
| Tambook | 0701224050 |
| Tungod | 0701224051 |
| U-og | 0701224052 |
| Ubujan | 0701224053 |

## Look up Inabanga with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0701224000") or cities.lookup("0701224000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Inabanga

```python
from barangay import search_fuzzy

for r in search_fuzzy("Inabanga", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
