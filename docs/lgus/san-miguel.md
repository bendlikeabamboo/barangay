---
title: "Barangays in San Miguel, Bulacan — PSGC Codes"
description: "Complete list of 49 barangays in San Miguel, Bulacan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in San Miguel, Bulacan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "San Miguel, Bulacan",
  "description": "Municipality in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Bulacan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Bulacan"
  }
}
</script>

San Miguel is a **municipality** in Bulacan (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Bagong Pag-asa | 0301421056 |
| Bagong Silang | 0301421001 |
| Balaong | 0301421002 |
| Balite | 0301421003 |
| Bantog | 0301421004 |
| Bardias | 0301421006 |
| Baritan | 0301421007 |
| Batasan Bata | 0301421008 |
| Batasan Matanda | 0301421009 |
| Biak-na-Bato | 0301421011 |
| Biclat | 0301421012 |
| Buga | 0301421013 |
| Buliran | 0301421014 |
| Bulualto | 0301421015 |
| Calumpang | 0301421016 |
| Cambio | 0301421019 |
| Camias | 0301421020 |
| Ilog-Bulo | 0301421021 |
| King Kabayo | 0301421023 |
| Labne | 0301421024 |
| Lambakin | 0301421025 |
| Magmarale | 0301421027 |
| Malibay | 0301421028 |
| Maligaya | 0301421058 |
| Mandile | 0301421030 |
| Masalipit | 0301421031 |
| Pacalag | 0301421032 |
| Paliwasan | 0301421033 |
| Partida | 0301421035 |
| Pinambaran | 0301421036 |
| Poblacion | 0301421037 |
| Pulong Bayabas | 0301421038 |
| Pulong Duhat | 0301421057 |
| Sacdalan | 0301421039 |
| Salacot | 0301421040 |
| Salangan | 0301421041 |
| San Agustin | 0301421043 |
| San Jose | 0301421044 |
| San Juan | 0301421045 |
| San Vicente | 0301421046 |
| Santa Ines | 0301421047 |
| Santa Lucia | 0301421048 |
| Santa Rita Bata | 0301421049 |
| Santa Rita Matanda | 0301421050 |
| Sapang | 0301421051 |
| Sibul | 0301421052 |
| Tartaro | 0301421054 |
| Tibagan | 0301421055 |
| Tigpalas | 0301421059 |

## Look up San Miguel with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0301421000") or cities.lookup("0301421000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in San Miguel

```python
from barangay import search_fuzzy

for r in search_fuzzy("San Miguel", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
