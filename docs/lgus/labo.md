---
title: "Barangays in Labo, Camarines Norte — PSGC Codes"
description: "Complete list of 52 barangays in Labo, Camarines Norte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Labo, Camarines Norte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Labo, Camarines Norte",
  "description": "Municipality in the Philippines with 52 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Camarines Norte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Camarines Norte"
  }
}
</script>

Labo is a **municipality** in Camarines Norte (Philippines) with
**52 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Anahaw | 0501606012 |
| Anameam | 0501606001 |
| Awitan | 0501606002 |
| Baay | 0501606003 |
| Bagacay | 0501606004 |
| Bagong Silang I | 0501606005 |
| Bagong Silang II | 0501606006 |
| Bagong Silang III | 0501606049 |
| Bakiad | 0501606007 |
| Bautista | 0501606008 |
| Bayabas | 0501606009 |
| Bayan-bayan | 0501606010 |
| Benit | 0501606011 |
| Bulhao | 0501606016 |
| Cabatuhan | 0501606017 |
| Cabusay | 0501606018 |
| Calabasa | 0501606019 |
| Canapawan | 0501606020 |
| Daguit | 0501606021 |
| Dalas | 0501606022 |
| Dumagmang | 0501606023 |
| Exciban | 0501606024 |
| Fundado | 0501606025 |
| Guinacutan | 0501606026 |
| Guisican | 0501606027 |
| Gumamela | 0501606013 |
| Iberica | 0501606028 |
| Kalamunding | 0501606015 |
| Lugui | 0501606030 |
| Mabilo I | 0501606031 |
| Mabilo II | 0501606032 |
| Macogon | 0501606033 |
| Mahawan-hawan | 0501606034 |
| Malangcao-Basud | 0501606035 |
| Malasugui | 0501606036 |
| Malatap | 0501606037 |
| Malaya | 0501606038 |
| Malibago | 0501606039 |
| Maot | 0501606040 |
| Masalong | 0501606041 |
| Matanlang | 0501606042 |
| Napaod | 0501606043 |
| Pag-Asa | 0501606044 |
| Pangpang | 0501606045 |
| Pinya | 0501606046 |
| San Antonio | 0501606047 |
| San Francisco | 0501606014 |
| Santa Cruz | 0501606048 |
| Submakin | 0501606050 |
| Talobatib | 0501606051 |
| Tigbinan | 0501606052 |
| Tulay Na Lupa | 0501606053 |

## Look up Labo with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0501606000") or cities.lookup("0501606000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Labo

```python
from barangay import search_fuzzy

for r in search_fuzzy("Labo", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
