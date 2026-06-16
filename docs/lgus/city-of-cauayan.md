---
title: "Barangays in City of Cauayan, Isabela — PSGC Codes"
description: "Complete list of 65 barangays in City of Cauayan, Isabela with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Cauayan, Isabela

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Cauayan, Isabela",
  "description": "City in the Philippines with 65 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Isabela",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Isabela"
  }
}
</script>

City of Cauayan is a **city** in Isabela (Philippines) with
**65 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alicaocao | 0203108001 |
| Alinam | 0203108002 |
| Amobocan | 0203108003 |
| Andarayan | 0203108004 |
| Baculod | 0203108006 |
| Baringin Norte | 0203108007 |
| Baringin Sur | 0203108008 |
| Buena Suerte | 0203108009 |
| Bugallon | 0203108010 |
| Buyon | 0203108011 |
| Cabaruan | 0203108012 |
| Cabugao | 0203108014 |
| Carabatan Bacareno | 0203108018 |
| Carabatan Chica | 0203108015 |
| Carabatan Grande | 0203108016 |
| Carabatan Punta | 0203108017 |
| Casalatan | 0203108019 |
| Cassap Fuera | 0203108022 |
| Catalina | 0203108023 |
| Culalabat | 0203108024 |
| Dabburab | 0203108025 |
| De Vera | 0203108028 |
| Dianao | 0203108029 |
| Disimuray | 0203108030 |
| District I | 0203108031 |
| District II | 0203108032 |
| District III | 0203108033 |
| Duminit | 0203108034 |
| Faustino | 0203108035 |
| Gagabutan | 0203108036 |
| Gappal | 0203108037 |
| Guayabal | 0203108038 |
| Labinab | 0203108039 |
| Linglingay | 0203108040 |
| Mabantad | 0203108041 |
| Maligaya | 0203108043 |
| Manaoag | 0203108044 |
| Marabulig I | 0203108045 |
| Marabulig II | 0203108046 |
| Minante I | 0203108048 |
| Minante II | 0203108049 |
| Naganacan | 0203108051 |
| Nagcampegan | 0203108050 |
| Nagrumbuan | 0203108052 |
| Nungnungan I | 0203108053 |
| Nungnungan II | 0203108054 |
| Pinoma | 0203108055 |
| Rizal | 0203108056 |
| Rogus | 0203108057 |
| San Antonio | 0203108058 |
| San Fermin | 0203108059 |
| San Francisco | 0203108060 |
| San Isidro | 0203108061 |
| San Luis | 0203108062 |
| San Pablo | 0203108020 |
| Santa Luciana | 0203108064 |
| Santa Maria | 0203108065 |
| Sillawit | 0203108066 |
| Sinippil | 0203108067 |
| Tagaran | 0203108069 |
| Turayong | 0203108070 |
| Union | 0203108071 |
| Villa Concepcion | 0203108072 |
| Villa Luna | 0203108073 |
| Villaflor | 0203108074 |

## Look up Cauayan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0203108000") or cities.lookup("0203108000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Cauayan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Cauayan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
