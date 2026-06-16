---
title: "Barangays in Daraga, Albay — PSGC Codes"
description: "Complete list of 54 barangays in Daraga, Albay with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Daraga, Albay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Daraga, Albay",
  "description": "Municipality in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Daraga is a **municipality** in Albay (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alcala | 0500503001 |
| Alobo | 0500503002 |
| Anislag | 0500503003 |
| Bagumbayan | 0500503004 |
| Balinad | 0500503005 |
| Bascaran | 0500503008 |
| Bañadero | 0500503006 |
| Bañag | 0500503007 |
| Bigao | 0500503009 |
| Binitayan | 0500503010 |
| Bongalon | 0500503011 |
| Budiao | 0500503012 |
| Burgos | 0500503013 |
| Busay | 0500503014 |
| Canarom | 0500503016 |
| Cullat | 0500503015 |
| Dela Paz | 0500503017 |
| Dinoronan | 0500503018 |
| Gabawan | 0500503019 |
| Gapo | 0500503020 |
| Ibaugan | 0500503021 |
| Ilawod Area Pob. | 0500503022 |
| Inarado | 0500503023 |
| Kidaco | 0500503024 |
| Kilicao | 0500503025 |
| Kimantong | 0500503026 |
| Kinawitan | 0500503027 |
| Kiwalo | 0500503028 |
| Lacag | 0500503029 |
| Mabini | 0500503030 |
| Malabog | 0500503031 |
| Malobago | 0500503032 |
| Maopi | 0500503033 |
| Market Area Pob. | 0500503034 |
| Maroroy | 0500503035 |
| Matnog | 0500503036 |
| Mayon | 0500503037 |
| Mi-isi | 0500503038 |
| Nabasan | 0500503039 |
| Namantao | 0500503040 |
| Pandan | 0500503041 |
| Peñafrancia | 0500503042 |
| Sagpon | 0500503044 |
| Salvacion | 0500503045 |
| San Rafael | 0500503046 |
| San Ramon | 0500503047 |
| San Roque | 0500503048 |
| San Vicente Grande | 0500503049 |
| San Vicente Pequeño | 0500503050 |
| Sipi | 0500503051 |
| Tabon-tabon | 0500503052 |
| Tagas | 0500503053 |
| Talahib | 0500503054 |
| Villahermosa | 0500503055 |

## Look up Daraga with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0500503000") or cities.lookup("0500503000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Daraga

```python
from barangay import search_fuzzy

for r in search_fuzzy("Daraga", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
