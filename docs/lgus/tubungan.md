---
title: "Barangays in Tubungan, Iloilo — PSGC Codes"
description: "Complete list of 48 barangays in Tubungan, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tubungan, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tubungan, Iloilo",
  "description": "Municipality in the Philippines with 48 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Iloilo",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Iloilo"
  }
}
</script>

Tubungan is a **municipality** in Iloilo (Philippines) with
**48 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adgao | 0603046001 |
| Ago | 0603046002 |
| Ambarihon | 0603046003 |
| Ayubo | 0603046004 |
| Bacan | 0603046005 |
| Badiang | 0603046007 |
| Bagunanay | 0603046006 |
| Balicua | 0603046008 |
| Bantayanan | 0603046009 |
| Batga | 0603046013 |
| Bato | 0603046014 |
| Bikil | 0603046015 |
| Boloc | 0603046016 |
| Bondoc | 0603046017 |
| Borong | 0603046018 |
| Buenavista | 0603046019 |
| Cadabdab | 0603046020 |
| Daga-ay | 0603046021 |
| Desposorio | 0603046022 |
| Igdampog Norte | 0603046023 |
| Igdampog Sur | 0603046024 |
| Igpaho | 0603046025 |
| Igtuble | 0603046026 |
| Ingay | 0603046027 |
| Isauan | 0603046028 |
| Jolason | 0603046029 |
| Jona | 0603046030 |
| La-ag | 0603046031 |
| Lanag Norte | 0603046032 |
| Lanag Sur | 0603046033 |
| Male | 0603046034 |
| Mayang | 0603046035 |
| Molina | 0603046036 |
| Morcillas | 0603046037 |
| Nagba | 0603046038 |
| Navillan | 0603046039 |
| Pinamacalan | 0603046040 |
| San Jose | 0603046041 |
| Sibucauan | 0603046042 |
| Singon | 0603046043 |
| Tabat | 0603046044 |
| Tagpu-an | 0603046045 |
| Talento | 0603046046 |
| Teniente Benito | 0603046047 |
| Victoria | 0603046048 |
| Zone I | 0603046010 |
| Zone II | 0603046011 |
| Zone III | 0603046012 |

## Look up Tubungan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603046000") or cities.lookup("0603046000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tubungan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tubungan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
