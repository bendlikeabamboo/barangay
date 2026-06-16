---
title: "Barangays in Libmanan, Camarines Sur — PSGC Codes"
description: "Complete list of 75 barangays in Libmanan, Camarines Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Libmanan, Camarines Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Libmanan, Camarines Sur",
  "description": "Municipality in the Philippines with 75 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Libmanan is a **municipality** in Camarines Sur (Philippines) with
**75 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aslong | 0501718001 |
| Awayan | 0501718002 |
| Bagacay | 0501718003 |
| Bagadion | 0501718004 |
| Bagamelon | 0501718005 |
| Bagumbayan | 0501718006 |
| Bahao | 0501718007 |
| Bahay | 0501718008 |
| Begajo Norte | 0501718012 |
| Begajo Sur | 0501718013 |
| Beguito Nuevo | 0501718009 |
| Beguito Viejo | 0501718010 |
| Bikal | 0501718014 |
| Busak | 0501718015 |
| Caima | 0501718016 |
| Calabnigan | 0501718017 |
| Camambugan | 0501718018 |
| Cambalidio | 0501718019 |
| Candami | 0501718020 |
| Candato | 0501718021 |
| Cawayan | 0501718022 |
| Concepcion | 0501718023 |
| Cuyapi | 0501718024 |
| Danawan | 0501718025 |
| Duang Niog | 0501718026 |
| Handong | 0501718027 |
| Ibid | 0501718028 |
| Inalahan | 0501718029 |
| Labao | 0501718030 |
| Libod I | 0501718031 |
| Libod II | 0501718032 |
| Loba-loba | 0501718033 |
| Mabini | 0501718035 |
| Malansad Nuevo | 0501718036 |
| Malansad Viejo | 0501718037 |
| Malbogon | 0501718038 |
| Malinao | 0501718039 |
| Mambalite | 0501718040 |
| Mambayawas | 0501718041 |
| Mambulo Nuevo | 0501718042 |
| Mambulo Viejo | 0501718043 |
| Mancawayan | 0501718044 |
| Mandacanan | 0501718045 |
| Mantalisay | 0501718046 |
| Padlos | 0501718047 |
| Pag-Oring Nuevo | 0501718048 |
| Pag-Oring Viejo | 0501718049 |
| Palangon | 0501718050 |
| Palong | 0501718051 |
| Patag | 0501718052 |
| Planza | 0501718053 |
| Poblacion | 0501718054 |
| Potot | 0501718055 |
| Puro-Batia | 0501718056 |
| Rongos | 0501718057 |
| Salvacion | 0501718058 |
| San Isidro | 0501718060 |
| San Juan | 0501718061 |
| San Pablo | 0501718062 |
| San Vicente | 0501718063 |
| Sibujo | 0501718064 |
| Sigamot | 0501718065 |
| Station-Church Site | 0501718066 |
| Taban-Fundado | 0501718067 |
| Tampuhan | 0501718068 |
| Tanag | 0501718069 |
| Tarum | 0501718070 |
| Tinalmud Nuevo | 0501718071 |
| Tinalmud Viejo | 0501718072 |
| Tinangkihan | 0501718073 |
| Udoc | 0501718074 |
| Umalo | 0501718075 |
| Uson | 0501718076 |
| Villadima | 0501718078 |
| Villasocorro | 0501718077 |

## Look up Libmanan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0501718000") or cities.lookup("0501718000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Libmanan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Libmanan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
