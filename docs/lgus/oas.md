---
title: "Barangays in Oas, Albay — PSGC Codes"
description: "Complete list of 53 barangays in Oas, Albay with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Oas, Albay

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Oas, Albay",
  "description": "Municipality in the Philippines with 53 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Oas is a **municipality** in Albay (Philippines) with
**53 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Badbad | 0500512001 |
| Badian | 0500512002 |
| Bagsa | 0500512003 |
| Bagumbayan | 0500512004 |
| Balogo | 0500512005 |
| Banao | 0500512008 |
| Bangiawon | 0500512009 |
| Bogtong | 0500512011 |
| Bongoran | 0500512010 |
| Busac | 0500512012 |
| Cadawag | 0500512013 |
| Cagmanaba | 0500512014 |
| Calaguimit | 0500512015 |
| Calpi | 0500512016 |
| Calzada | 0500512017 |
| Camagong | 0500512018 |
| Casinagan | 0500512019 |
| Centro Poblacion | 0500512020 |
| Coliat | 0500512021 |
| Del Rosario | 0500512022 |
| Gumabao | 0500512023 |
| Ilaor Norte | 0500512024 |
| Ilaor Sur | 0500512025 |
| Iraya Norte | 0500512026 |
| Iraya Sur | 0500512027 |
| Manga | 0500512028 |
| Maporong | 0500512029 |
| Maramba | 0500512030 |
| Matambo | 0500512032 |
| Mayag | 0500512033 |
| Mayao | 0500512034 |
| Moroponros | 0500512031 |
| Nagas | 0500512035 |
| Obaliw-Rinas | 0500512037 |
| Pistola | 0500512038 |
| Ramay | 0500512039 |
| Rizal | 0500512040 |
| Saban | 0500512041 |
| San Agustin | 0500512042 |
| San Antonio | 0500512043 |
| San Isidro | 0500512044 |
| San Jose | 0500512045 |
| San Juan | 0500512046 |
| San Miguel | 0500512047 |
| San Pascual | 0500512036 |
| San Ramon | 0500512049 |
| San Vicente | 0500512050 |
| Tablon | 0500512056 |
| Talisay | 0500512051 |
| Talongog | 0500512052 |
| Tapel | 0500512053 |
| Tobgon | 0500512054 |
| Tobog | 0500512055 |

## Look up Oas with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0500512000") or cities.lookup("0500512000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Oas

```python
from barangay import search_fuzzy

for r in search_fuzzy("Oas", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
