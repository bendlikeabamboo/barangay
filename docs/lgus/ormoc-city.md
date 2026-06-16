---
title: "Barangays in Ormoc City, Leyte — PSGC Codes"
description: "Complete list of 85 barangays in Ormoc City, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Ormoc City, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Ormoc City, Leyte",
  "description": "City in the Philippines with 85 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Leyte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Leyte"
  }
}
</script>

Ormoc City is a **city** in Leyte (Philippines) with
**85 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Airport | 0803738092 |
| Alegria | 0803738001 |
| Alta Vista | 0803738108 |
| Bagong | 0803738002 |
| Bagong Buhay | 0803738109 |
| Bantigue | 0803738004 |
| Barangay East | 0803738115 |
| Barangay North | 0803738091 |
| Barangay South | 0803738116 |
| Barangay West | 0803738117 |
| Batuan | 0803738005 |
| Bayog | 0803738110 |
| Biliboy | 0803738006 |
| Borok | 0803738007 |
| Cabaon-an | 0803738009 |
| Cabintan | 0803738093 |
| Cabulihan | 0803738010 |
| Cagbuhangin | 0803738011 |
| Camp Downes | 0803738094 |
| Can-adieng | 0803738012 |
| Can-untog | 0803738013 |
| Catmon | 0803738015 |
| Cogon Combado | 0803738016 |
| Concepcion | 0803738017 |
| Curva | 0803738018 |
| Danao | 0803738019 |
| Danhug | 0803738107 |
| Dayhagan | 0803738020 |
| Dolores | 0803738049 |
| Domonar | 0803738050 |
| Don Felipe Larrazabal | 0803738051 |
| Don Potenciano Larrazabal | 0803738104 |
| Donghol | 0803738052 |
| Doña Feliza Z. Mejia | 0803738111 |
| Esperanza | 0803738053 |
| Gaas | 0803738095 |
| Green Valley | 0803738096 |
| Guintigui-an | 0803738106 |
| Hibunawon | 0803738054 |
| Hugpa | 0803738055 |
| Ipil | 0803738056 |
| Juaton | 0803738112 |
| Kadaohan | 0803738105 |
| Labrador | 0803738003 |
| Lao | 0803738057 |
| Leondoni | 0803738099 |
| Libertad | 0803738058 |
| Liberty | 0803738098 |
| Licuma | 0803738097 |
| Liloan | 0803738059 |
| Linao | 0803738060 |
| Luna | 0803738113 |
| Mabato | 0803738114 |
| Mabini | 0803738061 |
| Macabug | 0803738062 |
| Magaswi | 0803738063 |
| Mahayag | 0803738064 |
| Mahayahay | 0803738065 |
| Manlilinao | 0803738066 |
| Margen | 0803738067 |
| Mas-in | 0803738068 |
| Matica-a | 0803738069 |
| Milagro | 0803738070 |
| Monterico | 0803738071 |
| Nasunogan | 0803738072 |
| Naungan | 0803738073 |
| Nueva Sociedad | 0803738100 |
| Nueva Vista | 0803738074 |
| Patag | 0803738075 |
| Punta | 0803738076 |
| Quezon, Jr. | 0803738077 |
| Rufina M. Tan | 0803738078 |
| Sabang Bao | 0803738079 |
| Salvacion | 0803738080 |
| San Antonio | 0803738081 |
| San Isidro | 0803738082 |
| San Jose | 0803738083 |
| San Juan | 0803738084 |
| San Pablo | 0803738088 |
| San Vicente | 0803738086 |
| Santo Niño | 0803738087 |
| Sumangga | 0803738089 |
| Tambulilid | 0803738101 |
| Tongonan | 0803738102 |
| Valencia | 0803738090 |

## Look up Ormoc City with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803738000") or cities.lookup("0803738000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Ormoc City

```python
from barangay import search_fuzzy

for r in search_fuzzy("Ormoc City", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
