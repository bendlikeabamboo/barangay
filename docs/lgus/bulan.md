---
title: "Barangays in Bulan, Sorsogon — PSGC Codes"
description: "Complete list of 63 barangays in Bulan, Sorsogon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Bulan, Sorsogon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Bulan, Sorsogon",
  "description": "Municipality in the Philippines with 63 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Sorsogon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Sorsogon"
  }
}
</script>

Bulan is a **municipality** in Sorsogon (Philippines) with
**63 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| A. Bonifacio | 0506203001 |
| Abad Santos | 0506203002 |
| Aguinaldo | 0506203003 |
| Antipolo | 0506203004 |
| Beguin | 0506203012 |
| Benigno S. Aquino | 0506203025 |
| Bical | 0506203011 |
| Bonga | 0506203013 |
| Butag | 0506203014 |
| Cadandanan | 0506203015 |
| Calomagon | 0506203016 |
| Calpi | 0506203017 |
| Cocok-Cabitan | 0506203018 |
| Daganas | 0506203019 |
| Danao | 0506203020 |
| Dolos | 0506203021 |
| E. Quirino | 0506203022 |
| Fabrica | 0506203023 |
| G. Del Pilar | 0506203062 |
| Gate | 0506203024 |
| Inararan | 0506203026 |
| J. Gerona | 0506203027 |
| J.P. Laurel | 0506203045 |
| Jamorawon | 0506203028 |
| Lajong | 0506203030 |
| Libertad | 0506203029 |
| M. Roxas | 0506203049 |
| Magsaysay | 0506203031 |
| Managanaga | 0506203032 |
| Marinab | 0506203033 |
| Montecalvario | 0506203035 |
| N. Roque | 0506203036 |
| Namo | 0506203037 |
| Nasuje | 0506203034 |
| Obrero | 0506203038 |
| Osmeña | 0506203039 |
| Otavi | 0506203040 |
| Padre Diaz | 0506203041 |
| Palale | 0506203042 |
| Quezon | 0506203046 |
| R. Gerona | 0506203047 |
| Recto | 0506203048 |
| Sagrada | 0506203050 |
| San Francisco | 0506203051 |
| San Isidro | 0506203052 |
| San Juan Bag-o | 0506203053 |
| San Juan Daan | 0506203054 |
| San Rafael | 0506203055 |
| San Ramon | 0506203056 |
| San Vicente | 0506203057 |
| Santa Remedios | 0506203058 |
| Santa Teresita | 0506203059 |
| Sigad | 0506203060 |
| Somagongsong | 0506203061 |
| Taromata | 0506203063 |
| Zone I Pob. | 0506203005 |
| Zone II Pob. | 0506203006 |
| Zone III Pob. | 0506203007 |
| Zone IV Pob. | 0506203008 |
| Zone V Pob. | 0506203009 |
| Zone VI Pob. | 0506203010 |
| Zone VII Pob. | 0506203064 |
| Zone VIII Pob. | 0506203065 |

## Look up Bulan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0506203000") or cities.lookup("0506203000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Bulan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Bulan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
