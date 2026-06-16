---
title: "Barangays in Calinog, Iloilo — PSGC Codes"
description: "Complete list of 59 barangays in Calinog, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Calinog, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Calinog, Iloilo",
  "description": "Municipality in the Philippines with 59 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Iloilo",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Iloilo"
  }
}
</script>

Calinog is a **municipality** in Iloilo (Philippines) with
**59 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agcalaga | 0603013002 |
| Aglibacao | 0603013003 |
| Aglonok | 0603013004 |
| Alibunan | 0603013006 |
| Badlan Grande | 0603013007 |
| Badlan Pequeño | 0603013008 |
| Badu | 0603013009 |
| Baje San Julian | 0603013062 |
| Balaticon | 0603013011 |
| Banban Grande | 0603013012 |
| Banban Pequeño | 0603013013 |
| Barrio Calinog | 0603013022 |
| Binolosan Grande | 0603013015 |
| Binolosan Pequeño | 0603013016 |
| Cabagiao | 0603013017 |
| Cabugao | 0603013019 |
| Cahigon | 0603013020 |
| Camalongo | 0603013023 |
| Canabajan | 0603013024 |
| Caratagan | 0603013025 |
| Carvasana | 0603013026 |
| Dalid | 0603013027 |
| Datagan | 0603013028 |
| Gama Grande | 0603013030 |
| Gama Pequeño | 0603013031 |
| Garangan | 0603013032 |
| Guinbonyugan | 0603013034 |
| Guiso | 0603013036 |
| Hilwan | 0603013037 |
| Impalidan | 0603013038 |
| Ipil | 0603013040 |
| Jamin-ay | 0603013041 |
| Lampaya | 0603013042 |
| Libot | 0603013043 |
| Lonoy | 0603013044 |
| Malag-it | 0603013073 |
| Malaguinabot | 0603013045 |
| Malapawe | 0603013046 |
| Malitbog Centro | 0603013047 |
| Mambiranan | 0603013049 |
| Manaripay | 0603013050 |
| Marandig | 0603013051 |
| Masaroy | 0603013052 |
| Maspasan | 0603013053 |
| Nalbugan | 0603013054 |
| Owak | 0603013056 |
| Poblacion Centro | 0603013057 |
| Poblacion Delgado | 0603013058 |
| Poblacion Ilaya | 0603013060 |
| Poblacion Rizal Ilaud | 0603013059 |
| San Nicolas | 0603013063 |
| Simsiman | 0603013064 |
| Supanga | 0603013074 |
| Tabucan | 0603013065 |
| Tahing | 0603013066 |
| Tibiao | 0603013068 |
| Tigbayog | 0603013069 |
| Toyungan | 0603013071 |
| Ulayan | 0603013072 |

## Look up Calinog with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603013000") or cities.lookup("0603013000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Calinog

```python
from barangay import search_fuzzy

for r in search_fuzzy("Calinog", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
