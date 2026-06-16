---
title: "Barangays in Baggao, Cagayan — PSGC Codes"
description: "Complete list of 48 barangays in Baggao, Cagayan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Baggao, Cagayan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Baggao, Cagayan",
  "description": "Municipality in the Philippines with 48 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cagayan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cagayan"
  }
}
</script>

Baggao is a **municipality** in Cagayan (Philippines) with
**48 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adaoag | 0201506001 |
| Agaman | 0201506002 |
| Agaman Norte | 0201506047 |
| Agaman Sur | 0201506048 |
| Alba | 0201506003 |
| Annayatan | 0201506004 |
| Asassi | 0201506005 |
| Asinga-Via | 0201506006 |
| Awallan | 0201506007 |
| Bacagan | 0201506008 |
| Bagunot | 0201506009 |
| Barsat East | 0201506011 |
| Barsat West | 0201506012 |
| Bitag Grande | 0201506013 |
| Bitag Pequeño | 0201506014 |
| Bunugan | 0201506015 |
| C. Verzosa | 0201506049 |
| Canagatan | 0201506016 |
| Carupian | 0201506017 |
| Catugay | 0201506018 |
| Dabbac Grande | 0201506020 |
| Dalin | 0201506021 |
| Dalla | 0201506022 |
| Hacienda Intal | 0201506023 |
| Ibulo | 0201506024 |
| Imurung | 0201506025 |
| J. Pallagao | 0201506026 |
| Lasilat | 0201506027 |
| Mabini | 0201506046 |
| Masical | 0201506028 |
| Mocag | 0201506029 |
| Nangalinan | 0201506030 |
| Poblacion | 0201506019 |
| Remus | 0201506031 |
| San Antonio | 0201506032 |
| San Francisco | 0201506033 |
| San Isidro | 0201506034 |
| San Jose | 0201506035 |
| San Miguel | 0201506036 |
| San Vicente | 0201506037 |
| Santa Margarita | 0201506038 |
| Santor | 0201506039 |
| Taguing | 0201506040 |
| Taguntungan | 0201506041 |
| Tallang | 0201506042 |
| Taytay | 0201506044 |
| Temblique | 0201506043 |
| Tungel | 0201506045 |

## Look up Baggao with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0201506000") or cities.lookup("0201506000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Baggao

```python
from barangay import search_fuzzy

for r in search_fuzzy("Baggao", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
