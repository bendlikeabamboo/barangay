---
title: "Barangays in Caramoan, Camarines Sur — PSGC Codes"
description: "Complete list of 49 barangays in Caramoan, Camarines Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Caramoan, Camarines Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Caramoan, Camarines Sur",
  "description": "Municipality in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Camarines Sur",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Camarines Sur"
  }
}
</script>

Caramoan is a **municipality** in Camarines Sur (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agaas | 0501711001 |
| Antolon | 0501711002 |
| Bacgong | 0501711003 |
| Bahay | 0501711004 |
| Bikal | 0501711005 |
| Binanuahan | 0501711006 |
| Cabacongan | 0501711007 |
| Cadong | 0501711008 |
| Canatuan | 0501711010 |
| Caputatan | 0501711011 |
| Colongcogong | 0501711009 |
| Daraga | 0501711013 |
| Gata | 0501711014 |
| Gibgos | 0501711015 |
| Gogon | 0501711012 |
| Guijalo | 0501711016 |
| Hanopol | 0501711017 |
| Hanoy | 0501711018 |
| Haponan | 0501711019 |
| Ilawod | 0501711020 |
| Ili-Centro | 0501711022 |
| Lidong | 0501711023 |
| Lubas | 0501711024 |
| Malabog | 0501711025 |
| Maligaya | 0501711026 |
| Mampirao | 0501711027 |
| Mandiclum | 0501711028 |
| Maqueda | 0501711029 |
| Minalaba | 0501711030 |
| Oring | 0501711031 |
| Oroc-Osoc | 0501711032 |
| Pagolinan | 0501711033 |
| Pandanan | 0501711034 |
| Paniman | 0501711035 |
| Patag-Belen | 0501711036 |
| Pili-Centro | 0501711037 |
| Pili-Tabiguian | 0501711038 |
| Poloan | 0501711039 |
| Salvacion | 0501711040 |
| San Roque | 0501711041 |
| San Vicente | 0501711042 |
| Santa Cruz | 0501711043 |
| Solnopan | 0501711044 |
| Tabgon | 0501711045 |
| Tabiguian | 0501711046 |
| Tabog | 0501711047 |
| Tawog | 0501711048 |
| Terogo | 0501711050 |
| Toboan | 0501711049 |

## Look up Caramoan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0501711000") or cities.lookup("0501711000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Caramoan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Caramoan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
