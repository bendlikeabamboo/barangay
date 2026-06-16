---
title: "Barangays in City of Passi, Iloilo — PSGC Codes"
description: "Complete list of 51 barangays in City of Passi, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Passi, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Passi, Iloilo",
  "description": "City in the Philippines with 51 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of Passi is a **city** in Iloilo (Philippines) with
**51 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agdahon | 0603035001 |
| Agdayao | 0603035002 |
| Aglalana | 0603035003 |
| Agtabo | 0603035004 |
| Agtambo | 0603035005 |
| Alimono | 0603035006 |
| Arac | 0603035007 |
| Ayuyan | 0603035008 |
| Bacuranan | 0603035009 |
| Bagacay | 0603035010 |
| Batu | 0603035011 |
| Bayan | 0603035012 |
| Bitaogan | 0603035013 |
| Buenavista | 0603035014 |
| Buyo | 0603035015 |
| Cabunga | 0603035016 |
| Cadilang | 0603035017 |
| Cairohan | 0603035018 |
| Dalicanan | 0603035019 |
| Gegachac | 0603035022 |
| Gemat-y | 0603035020 |
| Gemumua-agahon | 0603035021 |
| Gines Viejo | 0603035023 |
| Imbang Grande | 0603035024 |
| Jaguimitan | 0603035025 |
| Libo-o | 0603035026 |
| Maasin | 0603035027 |
| Magdungao | 0603035028 |
| Malag-it Grande | 0603035029 |
| Malag-it Pequeño | 0603035030 |
| Mambiranan Grande | 0603035031 |
| Mambiranan Pequeño | 0603035032 |
| Man-it | 0603035033 |
| Mantulang | 0603035034 |
| Mulapula | 0603035035 |
| Nueva Union | 0603035036 |
| Pagaypay | 0603035038 |
| Pangi | 0603035037 |
| Poblacion Ilawod | 0603035039 |
| Poblacion Ilaya | 0603035040 |
| Punong | 0603035041 |
| Quinagaringan Grande | 0603035042 |
| Quinagaringan Pequeño | 0603035043 |
| Sablogon | 0603035044 |
| Salngan | 0603035045 |
| Santo Tomas | 0603035046 |
| Sarapan | 0603035047 |
| Tagubong | 0603035049 |
| Talongonan | 0603035050 |
| Tubod | 0603035051 |
| Tuburan | 0603035052 |

## Look up Passi with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603035000") or cities.lookup("0603035000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Passi

```python
from barangay import search_fuzzy

for r in search_fuzzy("Passi", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
