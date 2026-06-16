---
title: "Barangays in City of Oroquieta, Misamis Occidental — PSGC Codes"
description: "Complete list of 47 barangays in City of Oroquieta, Misamis Occidental with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Oroquieta, Misamis Occidental

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Oroquieta, Misamis Occidental",
  "description": "City in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Misamis Occidental",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Misamis Occidental"
  }
}
</script>

City of Oroquieta is a **city** in Misamis Occidental (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Apil | 1004209001 |
| Binuangan | 1004209002 |
| Bolibol | 1004209003 |
| Buenavista | 1004209004 |
| Bunga | 1004209005 |
| Buntawan | 1004209006 |
| Burgos | 1004209007 |
| Canubay | 1004209008 |
| Ciriaco C. Pastrano | 1004209027 |
| Clarin Settlement | 1004209009 |
| Dolipos Alto | 1004209011 |
| Dolipos Bajo | 1004209010 |
| Dulapo | 1004209012 |
| Dullan Norte | 1004209013 |
| Dullan Sur | 1004209014 |
| Lamac Lower | 1004209015 |
| Lamac Upper | 1004209016 |
| Langcangan Lower | 1004209017 |
| Langcangan Proper | 1004209018 |
| Langcangan Upper | 1004209019 |
| Layawan | 1004209020 |
| Loboc Lower | 1004209021 |
| Loboc Upper | 1004209022 |
| Malindang | 1004209024 |
| Mialen | 1004209025 |
| Mobod | 1004209026 |
| Paypayan | 1004209028 |
| Pines | 1004209029 |
| Poblacion I | 1004209030 |
| Poblacion II | 1004209031 |
| Rizal Lower | 1004209023 |
| Rizal Upper | 1004209046 |
| San Vicente Alto | 1004209033 |
| San Vicente Bajo | 1004209034 |
| Sebucal | 1004209035 |
| Senote | 1004209036 |
| Taboc Norte | 1004209037 |
| Taboc Sur | 1004209038 |
| Talairon | 1004209039 |
| Talic | 1004209040 |
| Tipan | 1004209042 |
| Toliyok | 1004209041 |
| Tuyabang Alto | 1004209043 |
| Tuyabang Bajo | 1004209044 |
| Tuyabang Proper | 1004209045 |
| Victoria | 1004209047 |
| Villaflor | 1004209048 |

## Look up Oroquieta with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1004209000") or cities.lookup("1004209000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Oroquieta

```python
from barangay import search_fuzzy

for r in search_fuzzy("Oroquieta", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
