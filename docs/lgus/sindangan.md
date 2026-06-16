---
title: "Barangays in Sindangan, Zamboanga del Norte — PSGC Codes"
description: "Complete list of 52 barangays in Sindangan, Zamboanga del Norte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Sindangan, Zamboanga del Norte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Sindangan, Zamboanga del Norte",
  "description": "Municipality in the Philippines with 52 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Zamboanga del Norte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Zamboanga del Norte"
  }
}
</script>

Sindangan is a **municipality** in Zamboanga del Norte (Philippines) with
**52 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Bago | 0907218003 |
| Balok | 0907218057 |
| Bantayan | 0907218058 |
| Bato | 0907218032 |
| Benigno Aquino Jr. | 0907218055 |
| Binuangan | 0907218004 |
| Bitoon | 0907218005 |
| Bucana | 0907218033 |
| Calatunan | 0907218036 |
| Caluan | 0907218034 |
| Calubian | 0907218035 |
| Dagohoy | 0907218037 |
| Dapaon | 0907218059 |
| Datagan | 0907218038 |
| Datu Tangkilan | 0907218060 |
| Dicoyong | 0907218007 |
| Disud | 0907218039 |
| Don Ricardo Macias | 0907218009 |
| Doña Josefa | 0907218040 |
| Dumalogdog | 0907218010 |
| Fatima | 0907218056 |
| Gampis | 0907218041 |
| Goleo | 0907218042 |
| Imelda | 0907218043 |
| Inuman | 0907218011 |
| Joaquin Macias | 0907218044 |
| La Concepcion | 0907218012 |
| La Roche San Miguel | 0907218061 |
| Labakid | 0907218045 |
| Lagag | 0907218013 |
| Lapero | 0907218014 |
| Lawis | 0907218062 |
| Magsaysay | 0907218063 |
| Mandih | 0907218015 |
| Maras | 0907218018 |
| Mawal | 0907218019 |
| Misok | 0907218020 |
| Motibot | 0907218021 |
| Nato | 0907218022 |
| Nipaan | 0907218064 |
| Pangalalan | 0907218023 |
| Piao | 0907218024 |
| Poblacion | 0907218025 |
| Santo Niño | 0907218050 |
| Santo Rosario | 0907218051 |
| Siare | 0907218026 |
| Talinga | 0907218028 |
| Tigbao | 0907218030 |
| Tinaplan | 0907218029 |
| Titik | 0907218031 |
| Upper Inuman | 0907218065 |
| Upper Nipaan | 0907218054 |

## Look up Sindangan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0907218000") or cities.lookup("0907218000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Sindangan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Sindangan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
