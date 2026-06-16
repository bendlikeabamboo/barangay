---
title: "Barangays in Malasiqui, Pangasinan — PSGC Codes"
description: "Complete list of 73 barangays in Malasiqui, Pangasinan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Malasiqui, Pangasinan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Malasiqui, Pangasinan",
  "description": "Municipality in the Philippines with 73 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Malasiqui is a **municipality** in Pangasinan (Philippines) with
**73 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abonagan | 0105524001 |
| Agdao | 0105524002 |
| Alacan | 0105524003 |
| Aliaga | 0105524004 |
| Amacalan | 0105524005 |
| Anolid | 0105524006 |
| Apaya | 0105524007 |
| Asin Este | 0105524008 |
| Asin Weste | 0105524009 |
| Bacundao Este | 0105524010 |
| Bacundao Weste | 0105524011 |
| Bakitiw | 0105524012 |
| Balite | 0105524013 |
| Banawang | 0105524014 |
| Barang | 0105524015 |
| Bawer | 0105524016 |
| Binalay | 0105524017 |
| Bobon | 0105524018 |
| Bolaoit | 0105524019 |
| Bongar | 0105524020 |
| Butao | 0105524021 |
| Cabatling | 0105524022 |
| Cabueldatan | 0105524023 |
| Calbueg | 0105524026 |
| Canan Norte | 0105524027 |
| Canan Sur | 0105524028 |
| Cawayan Bogtong | 0105524029 |
| Don Pedro | 0105524031 |
| Gatang | 0105524032 |
| Goliman | 0105524033 |
| Gomez | 0105524034 |
| Guilig | 0105524035 |
| Ican | 0105524036 |
| Ingalagala | 0105524037 |
| Lareg-lareg | 0105524038 |
| Lasip | 0105524039 |
| Lepa | 0105524040 |
| Loqueb Este | 0105524041 |
| Loqueb Norte | 0105524042 |
| Loqueb Sur | 0105524043 |
| Lunec | 0105524044 |
| Mabulitec | 0105524045 |
| Malimpec | 0105524047 |
| Manggan-Dampay | 0105524048 |
| Nalsian Norte | 0105524050 |
| Nalsian Sur | 0105524051 |
| Nancapian | 0105524049 |
| Nansangaan | 0105524053 |
| Olea | 0105524054 |
| Pacuan | 0105524055 |
| Palapar Norte | 0105524056 |
| Palapar Sur | 0105524057 |
| Palong | 0105524058 |
| Pamaranum | 0105524059 |
| Pasima | 0105524060 |
| Payar | 0105524061 |
| Poblacion | 0105524062 |
| Polong Norte | 0105524063 |
| Polong Sur | 0105524064 |
| Potiocan | 0105524065 |
| San Julian | 0105524066 |
| Tabo-Sili | 0105524067 |
| Talospatang | 0105524069 |
| Taloy | 0105524070 |
| Taloyan | 0105524071 |
| Tambac | 0105524072 |
| Tobor | 0105524068 |
| Tolonguat | 0105524073 |
| Tomling | 0105524074 |
| Umando | 0105524075 |
| Viado | 0105524076 |
| Waig | 0105524077 |
| Warey | 0105524078 |

## Look up Malasiqui with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0105524000") or cities.lookup("0105524000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Malasiqui

```python
from barangay import search_fuzzy

for r in search_fuzzy("Malasiqui", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
