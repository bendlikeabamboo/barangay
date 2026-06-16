---
title: "Barangays in Esperanza, Agusan del Sur — PSGC Codes"
description: "Complete list of 47 barangays in Esperanza, Agusan del Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Esperanza, Agusan del Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Esperanza, Agusan del Sur",
  "description": "Municipality in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Agusan del Sur",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Agusan del Sur"
  }
}
</script>

Esperanza is a **municipality** in Agusan del Sur (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agsabu | 1600303031 |
| Aguinaldo | 1600303032 |
| Anolingan | 1600303001 |
| Bakingking | 1600303002 |
| Balubo | 1600303033 |
| Bentahon | 1600303003 |
| Bunaguit | 1600303004 |
| Catmonon | 1600303006 |
| Cebulan | 1600303034 |
| Concordia | 1600303007 |
| Crossing Luna | 1600303035 |
| Cubo | 1600303036 |
| Dakutan | 1600303008 |
| Duangan | 1600303009 |
| Guadalupe | 1600303011 |
| Guibonon | 1600303037 |
| Hawilian | 1600303012 |
| Kalabuan | 1600303038 |
| Kinamaybay | 1600303039 |
| Labao | 1600303013 |
| Langag | 1600303040 |
| Maasin | 1600303014 |
| Mac-Arthur | 1600303010 |
| Mahagcot | 1600303015 |
| Maliwanag | 1600303041 |
| Milagros | 1600303016 |
| Nato | 1600303017 |
| New Gingoog | 1600303042 |
| Odiong | 1600303043 |
| Oro | 1600303018 |
| Piglawigan | 1600303044 |
| Poblacion | 1600303019 |
| Remedios | 1600303020 |
| Salug | 1600303021 |
| San Isidro | 1600303045 |
| San Jose | 1600303046 |
| San Toribio | 1600303022 |
| San Vicente | 1600303047 |
| Santa Fe | 1600303023 |
| Segunda | 1600303024 |
| Sinakungan | 1600303048 |
| Tagabase | 1600303026 |
| Taganahaw | 1600303027 |
| Tagbalili | 1600303028 |
| Tahina | 1600303029 |
| Tandang Sora | 1600303030 |
| Valentina | 1600303049 |

## Look up Esperanza with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1600303000") or cities.lookup("1600303000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Esperanza

```python
from barangay import search_fuzzy

for r in search_fuzzy("Esperanza", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
