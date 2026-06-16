---
title: "Barangays in Mangatarem, Pangasinan — PSGC Codes"
description: "Complete list of 82 barangays in Mangatarem, Pangasinan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Mangatarem, Pangasinan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Mangatarem, Pangasinan",
  "description": "Municipality in the Philippines with 82 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Pangasinan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Pangasinan"
  }
}
</script>

Mangatarem is a **municipality** in Pangasinan (Philippines) with
**82 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Andangin | 0105527001 |
| Arellano Street | 0105527002 |
| Bantay | 0105527003 |
| Bantocaling | 0105527004 |
| Baracbac | 0105527005 |
| Bogtong Bolo | 0105527007 |
| Bogtong Bunao | 0105527008 |
| Bogtong Centro | 0105527009 |
| Bogtong Niog | 0105527010 |
| Bogtong Silag | 0105527011 |
| Buaya | 0105527012 |
| Buenlag | 0105527013 |
| Bueno | 0105527014 |
| Bunagan | 0105527015 |
| Bunlalacao | 0105527017 |
| Burgos Street | 0105527018 |
| Cabaluyan 1st | 0105527019 |
| Cabaluyan 2nd | 0105527020 |
| Cabarabuan | 0105527021 |
| Cabaruan | 0105527022 |
| Cabayaoasan | 0105527023 |
| Cabayugan | 0105527024 |
| Cacaoiten | 0105527025 |
| Calomboyan Norte | 0105527026 |
| Calomboyan Sur | 0105527027 |
| Calvo | 0105527028 |
| Casilagan | 0105527029 |
| Catarataraan | 0105527030 |
| Caturay Norte | 0105527031 |
| Caturay Sur | 0105527032 |
| Caviernesan | 0105527033 |
| Dorongan Ketaket | 0105527034 |
| Dorongan Linmansangan | 0105527035 |
| Dorongan Punta | 0105527036 |
| Dorongan Sawat | 0105527037 |
| Dorongan Valerio | 0105527038 |
| General Luna | 0105527039 |
| Historia | 0105527040 |
| Lawak Langka | 0105527041 |
| Linmansangan | 0105527042 |
| Lopez | 0105527043 |
| Mabini | 0105527044 |
| Macarang | 0105527045 |
| Malabobo | 0105527046 |
| Malibong | 0105527047 |
| Malunec | 0105527048 |
| Maravilla | 0105527049 |
| Maravilla-Arellano Ext. | 0105527050 |
| Muelang | 0105527051 |
| Naguilayan East | 0105527052 |
| Naguilayan West | 0105527053 |
| Nancasalan | 0105527054 |
| Niog-Cabison-Bulaney | 0105527055 |
| Olegario-Caoile | 0105527056 |
| Olo Cacamposan | 0105527057 |
| Olo Cafabrosan | 0105527058 |
| Olo Cagarlitan | 0105527059 |
| Osmeña | 0105527060 |
| Pacalat | 0105527061 |
| Pampano | 0105527062 |
| Parian | 0105527063 |
| Paul | 0105527064 |
| Peania Pedania | 0105527006 |
| Pogon-Aniat | 0105527065 |
| Pogon-Lomboy | 0105527066 |
| Ponglo-Baleg | 0105527067 |
| Ponglo-Muelag | 0105527068 |
| Quetegan | 0105527069 |
| Quezon | 0105527070 |
| Salavante | 0105527071 |
| Sapang | 0105527072 |
| Sonson Ongkit | 0105527073 |
| Suaco | 0105527074 |
| Tagac | 0105527075 |
| Takipan | 0105527076 |
| Talogtog | 0105527077 |
| Tococ Barikir | 0105527078 |
| Torre 1st | 0105527079 |
| Torre 2nd | 0105527080 |
| Torres Bugallon | 0105527081 |
| Umangan | 0105527082 |
| Zamora | 0105527083 |

## Look up Mangatarem with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0105527000") or cities.lookup("0105527000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Mangatarem

```python
from barangay import search_fuzzy

for r in search_fuzzy("Mangatarem", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
