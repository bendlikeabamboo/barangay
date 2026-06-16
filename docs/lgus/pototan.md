---
title: "Barangays in Pototan, Iloilo — PSGC Codes"
description: "Complete list of 50 barangays in Pototan, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Pototan, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Pototan, Iloilo",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Pototan is a **municipality** in Iloilo (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abangay | 0603037001 |
| Amamaros | 0603037002 |
| Bagacay | 0603037003 |
| Barasan | 0603037004 |
| Batuan | 0603037005 |
| Bongco | 0603037006 |
| Cahaguichican | 0603037007 |
| Callan | 0603037008 |
| Cansilayan | 0603037009 |
| Casalsagan | 0603037010 |
| Cato-ogan | 0603037011 |
| Cau-ayan | 0603037012 |
| Culob | 0603037013 |
| Danao | 0603037014 |
| Dapitan | 0603037015 |
| Dawis | 0603037016 |
| Dongsol | 0603037019 |
| Fernando Parcon Ward | 0603037042 |
| Fundacion | 0603037020 |
| Guibuangan | 0603037022 |
| Guinacas | 0603037021 |
| Igang | 0603037023 |
| Intaluan | 0603037024 |
| Iwa Ilaud | 0603037025 |
| Iwa Ilaya | 0603037026 |
| Jamabalud | 0603037027 |
| Jebioc | 0603037028 |
| Lay-Ahan | 0603037030 |
| Lopez Jaena Ward | 0603037032 |
| Lumbo | 0603037033 |
| Macatol | 0603037034 |
| Malusgod | 0603037035 |
| Nabitasan | 0603037037 |
| Naga | 0603037038 |
| Nanga | 0603037039 |
| Naslo | 0603037036 |
| Pajo | 0603037040 |
| Palanguia | 0603037041 |
| Pitogo | 0603037044 |
| Polot-an | 0603037045 |
| Primitivo Ledesma Ward | 0603037031 |
| Purog | 0603037046 |
| Rumbang | 0603037047 |
| San Jose Ward | 0603037048 |
| Sinuagan | 0603037049 |
| Tuburan | 0603037050 |
| Tumcon Ilaud | 0603037052 |
| Tumcon Ilaya | 0603037051 |
| Ubang | 0603037053 |
| Zarrague | 0603037054 |

## Look up Pototan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603037000") or cities.lookup("0603037000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Pototan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Pototan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
