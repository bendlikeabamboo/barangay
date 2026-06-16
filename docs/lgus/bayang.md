---
title: "Barangays in Bayang, Lanao del Sur — PSGC Codes"
description: "Complete list of 49 barangays in Bayang, Lanao del Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Bayang, Lanao del Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Bayang, Lanao del Sur",
  "description": "Municipality in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Lanao del Sur",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Lanao del Sur"
  }
}
</script>

Bayang is a **municipality** in Lanao del Sur (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Bagoaingud | 1903604003 |
| Bairan | 1903604004 |
| Bandingun | 1903604005 |
| Biabi | 1903604006 |
| Bialaan | 1903604007 |
| Bubong Lilod | 1903604017 |
| Bubong Raya | 1903604055 |
| Cadayonan | 1903604009 |
| Cadingilan Occidental | 1903604027 |
| Cadingilan Oriental | 1903604028 |
| Condaraan Pob. | 1903604012 |
| Cormatan | 1903604013 |
| Gandamato | 1903604054 |
| Ilian | 1903604014 |
| Lalapung Central | 1903604011 |
| Lalapung Proper | 1903604015 |
| Lalapung Upper | 1903604053 |
| Linao | 1903604018 |
| Linuk | 1903604019 |
| Liong | 1903604020 |
| Lumbac | 1903604021 |
| Lumbac Cadayonan | 1903604010 |
| Maliwanag | 1903604024 |
| Mapantao | 1903604025 |
| Mimbalawag | 1903604022 |
| Palao | 1903604030 |
| Pama-an | 1903604031 |
| Pamacotan | 1903604032 |
| Pantar | 1903604033 |
| Parao | 1903604034 |
| Patong | 1903604035 |
| Poblacion | 1903604056 |
| Porotan | 1903604036 |
| Rantian | 1903604037 |
| Raya Cadayonan | 1903604038 |
| Rinabor | 1903604039 |
| Samporna | 1903604041 |
| Sapa | 1903604040 |
| Silid | 1903604042 |
| Sugod | 1903604043 |
| Sultan Pandapatan | 1903604044 |
| Sumbag | 1903604045 |
| Tagoranao | 1903604046 |
| Tangcal | 1903604047 |
| Tangcal Proper | 1903604048 |
| Tomarompong | 1903604050 |
| Tomongcal Ligi | 1903604051 |
| Torogan | 1903604052 |
| Tuca | 1903604049 |

## Look up Bayang with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1903604000") or cities.lookup("1903604000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Bayang

```python
from barangay import search_fuzzy

for r in search_fuzzy("Bayang", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
