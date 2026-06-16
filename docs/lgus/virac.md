---
title: "Barangays in Virac, Catanduanes — PSGC Codes"
description: "Complete list of 63 barangays in Virac, Catanduanes with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Virac, Catanduanes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Virac, Catanduanes",
  "description": "Municipality in the Philippines with 63 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Catanduanes",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Catanduanes"
  }
}
</script>

Virac is a **municipality** in Catanduanes (Philippines) with
**63 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Antipolo Del Norte | 0502011001 |
| Antipolo Del Sur | 0502011002 |
| Balite | 0502011003 |
| Batag | 0502011004 |
| Bigaa | 0502011005 |
| Buenavista | 0502011006 |
| Buyo | 0502011007 |
| Cabihian | 0502011008 |
| Calabnigan | 0502011009 |
| Calampong | 0502011010 |
| Calatagan Proper | 0502011011 |
| Calatagan Tibang | 0502011012 |
| Capilihan | 0502011013 |
| Casoocan | 0502011014 |
| Cavinitan | 0502011015 |
| Concepcion | 0502011017 |
| Constantino | 0502011018 |
| Danicop | 0502011019 |
| Dugui San Isidro | 0502011021 |
| Dugui San Vicente | 0502011020 |
| Dugui Too | 0502011023 |
| F. Tacorda Village | 0502011024 |
| Francia | 0502011025 |
| Gogon Centro | 0502011026 |
| Gogon Sirangan | 0502011016 |
| Hawan Grande | 0502011027 |
| Hawan Ilaya | 0502011028 |
| Hicming | 0502011029 |
| Ibong Sapa | 0502011053 |
| Igang | 0502011030 |
| Juan M. Alberto | 0502011031 |
| Lanao | 0502011032 |
| Magnesia Del Norte | 0502011033 |
| Magnesia Del Sur | 0502011034 |
| Marcelo Alberto | 0502011035 |
| Marilima | 0502011036 |
| Pajo Baguio | 0502011037 |
| Pajo San Isidro | 0502011038 |
| Palnab Del Norte | 0502011039 |
| Palnab Del Sur | 0502011040 |
| Palta Big | 0502011041 |
| Palta Salvacion | 0502011042 |
| Palta Small | 0502011043 |
| Rawis | 0502011044 |
| Salvacion | 0502011045 |
| San Isidro Village | 0502011046 |
| San Jose | 0502011047 |
| San Juan | 0502011048 |
| San Pablo | 0502011049 |
| San Pedro | 0502011050 |
| San Roque | 0502011051 |
| San Vicente | 0502011052 |
| Santa Cruz | 0502011054 |
| Santa Elena | 0502011055 |
| Santo Cristo | 0502011056 |
| Santo Domingo | 0502011057 |
| Santo Niño | 0502011058 |
| Simamla | 0502011059 |
| Sogod-Simamla | 0502011061 |
| Sogod-Tibgao | 0502011063 |
| Talisoy | 0502011062 |
| Tubaon | 0502011064 |
| Valencia | 0502011065 |

## Look up Virac with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0502011000") or cities.lookup("0502011000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Virac

```python
from barangay import search_fuzzy

for r in search_fuzzy("Virac", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
