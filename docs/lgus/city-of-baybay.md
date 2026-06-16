---
title: "Barangays in City of Baybay, Leyte — PSGC Codes"
description: "Complete list of 92 barangays in City of Baybay, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Baybay, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Baybay, Leyte",
  "description": "City in the Philippines with 92 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of Baybay is a **city** in Leyte (Philippines) with
**92 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Altavista | 0803708001 |
| Ambacan | 0803708002 |
| Amguhan | 0803708003 |
| Ampihanon | 0803708004 |
| Balao | 0803708005 |
| Banahao | 0803708006 |
| Biasong | 0803708008 |
| Bidlinan | 0803708009 |
| Bitanhuan | 0803708010 |
| Bubon | 0803708011 |
| Buenavista | 0803708012 |
| Bunga | 0803708013 |
| Butigan | 0803708014 |
| Candadam | 0803708034 |
| Caridad | 0803708016 |
| Ciabo | 0803708089 |
| Cogon | 0803708093 |
| Ga-as | 0803708017 |
| Gabas | 0803708018 |
| Gakat | 0803708019 |
| Guadalupe | 0803708020 |
| Gubang | 0803708021 |
| Hibunawan | 0803708022 |
| Higuloan | 0803708023 |
| Hilapnitan | 0803708024 |
| Hipusngo | 0803708025 |
| Igang | 0803708026 |
| Imelda | 0803708027 |
| Jaena | 0803708028 |
| Kabalasan | 0803708029 |
| Kabatuan | 0803708015 |
| Kabungaan | 0803708030 |
| Kagumay | 0803708031 |
| Kambonggan | 0803708032 |
| Kan-ipa | 0803708035 |
| Kansungka | 0803708036 |
| Kantagnos | 0803708037 |
| Kilim | 0803708038 |
| Lintaon | 0803708039 |
| Maganhan | 0803708041 |
| Mahayahay | 0803708042 |
| Mailhi | 0803708043 |
| Maitum | 0803708044 |
| Makinhas | 0803708045 |
| Mapgap | 0803708046 |
| Marcos | 0803708047 |
| Maslug | 0803708048 |
| Matam-is | 0803708049 |
| Maybog | 0803708050 |
| Maypatag | 0803708051 |
| Monte Verde | 0803708094 |
| Monterico | 0803708052 |
| Palhi | 0803708053 |
| Pangasungan | 0803708054 |
| Pansagan | 0803708055 |
| Patag | 0803708056 |
| Plaridel | 0803708057 |
| Poblacion Zone 1 | 0803708092 |
| Poblacion Zone 10 | 0803708066 |
| Poblacion Zone 11 | 0803708067 |
| Poblacion Zone 12 | 0803708068 |
| Poblacion Zone 13 | 0803708069 |
| Poblacion Zone 14 | 0803708070 |
| Poblacion Zone 15 | 0803708071 |
| Poblacion Zone 16 | 0803708072 |
| Poblacion Zone 17 | 0803708073 |
| Poblacion Zone 18 | 0803708074 |
| Poblacion Zone 19 | 0803708075 |
| Poblacion Zone 2 | 0803708058 |
| Poblacion Zone 20 | 0803708076 |
| Poblacion Zone 21 | 0803708077 |
| Poblacion Zone 22 | 0803708078 |
| Poblacion Zone 23 | 0803708079 |
| Poblacion Zone 3 | 0803708059 |
| Poblacion Zone 4 | 0803708060 |
| Poblacion Zone 5 | 0803708061 |
| Poblacion Zone 6 | 0803708062 |
| Poblacion Zone 7 | 0803708063 |
| Poblacion Zone 8 | 0803708064 |
| Poblacion Zone 9 | 0803708065 |
| Pomponan | 0803708080 |
| Punta | 0803708081 |
| Sabang | 0803708082 |
| San Agustin | 0803708083 |
| San Isidro | 0803708084 |
| San Juan | 0803708085 |
| Santa Cruz | 0803708086 |
| Santo Rosario | 0803708087 |
| Sapa | 0803708088 |
| Villa Mag-aso | 0803708095 |
| Villa Solidaridad | 0803708090 |
| Zacarito | 0803708091 |

## Look up Baybay with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803708000") or cities.lookup("0803708000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Baybay

```python
from barangay import search_fuzzy

for r in search_fuzzy("Baybay", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
