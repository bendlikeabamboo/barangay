---
title: "Barangays in Daram, Samar — PSGC Codes"
description: "Complete list of 58 barangays in Daram, Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Daram, Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Daram, Samar",
  "description": "Municipality in the Philippines with 58 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Samar"
  }
}
</script>

Daram is a **municipality** in Samar (Philippines) with
**58 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Arawane | 0806006001 |
| Astorga | 0806006002 |
| Bachao | 0806006003 |
| Baclayan | 0806006004 |
| Bagacay | 0806006005 |
| Bayog | 0806006006 |
| Betaug | 0806006008 |
| Birawan | 0806006007 |
| Bono-anon | 0806006009 |
| Buenavista | 0806006010 |
| Burgos | 0806006011 |
| Cabac | 0806006012 |
| Cabil-isan | 0806006013 |
| Cabiton-an | 0806006014 |
| Cabugao | 0806006015 |
| Cagboboto | 0806006055 |
| Calawan-an | 0806006016 |
| Cambuhay | 0806006017 |
| Campelipa | 0806006020 |
| Candugue | 0806006018 |
| Canloloy | 0806006019 |
| Cansaganay | 0806006021 |
| Casab-ahan | 0806006023 |
| Guindapunan | 0806006024 |
| Guintampilan | 0806006025 |
| Iquiran | 0806006026 |
| Jacopon | 0806006027 |
| Losa | 0806006028 |
| Lucob-lucob | 0806006056 |
| Mabini | 0806006029 |
| Macalpe | 0806006030 |
| Mandoyucan | 0806006031 |
| Marupangdan | 0806006033 |
| Mayabay | 0806006034 |
| Mongolbongol | 0806006032 |
| Nipa | 0806006035 |
| Parasan | 0806006037 |
| Poblacion 1 | 0806006038 |
| Poblacion 2 | 0806006039 |
| Poblacion 3 | 0806006022 |
| Pondang | 0806006040 |
| Poso | 0806006041 |
| Real | 0806006042 |
| Rizal | 0806006043 |
| San Antonio | 0806006044 |
| San Jose | 0806006045 |
| San Miguel | 0806006046 |
| San Roque | 0806006047 |
| San Vicente | 0806006057 |
| Saugan | 0806006048 |
| So-ong | 0806006049 |
| Sua | 0806006050 |
| Sugod | 0806006058 |
| Talisay | 0806006051 |
| Tugas | 0806006052 |
| Ubo | 0806006053 |
| Valles-Bello | 0806006054 |
| Yangta | 0806006059 |

## Look up Daram with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0806006000") or cities.lookup("0806006000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Daram

```python
from barangay import search_fuzzy

for r in search_fuzzy("Daram", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
