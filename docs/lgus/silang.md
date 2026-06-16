---
title: "Barangays in Silang, Cavite — PSGC Codes"
description: "Complete list of 64 barangays in Silang, Cavite with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Silang, Cavite

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Silang, Cavite",
  "description": "Municipality in the Philippines with 64 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cavite",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cavite"
  }
}
</script>

Silang is a **municipality** in Cavite (Philippines) with
**64 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Acacia | 0402118049 |
| Adlas | 0402118001 |
| Anahaw I | 0402118050 |
| Anahaw II | 0402118054 |
| Balite I | 0402118003 |
| Balite II | 0402118004 |
| Balubad | 0402118005 |
| Banaba | 0402118055 |
| Barangay I | 0402118032 |
| Barangay II | 0402118033 |
| Barangay III | 0402118034 |
| Barangay IV | 0402118035 |
| Barangay V | 0402118036 |
| Batas | 0402118006 |
| Biga I | 0402118007 |
| Biga II | 0402118056 |
| Biluso | 0402118008 |
| Bucal | 0402118010 |
| Buho | 0402118009 |
| Bulihan | 0402118011 |
| Cabangaan | 0402118012 |
| Carmen | 0402118013 |
| Hoyo | 0402118057 |
| Hukay | 0402118014 |
| Iba | 0402118015 |
| Inchican | 0402118016 |
| Ipil I | 0402118051 |
| Ipil II | 0402118058 |
| Kalubkob | 0402118017 |
| Kaong | 0402118018 |
| Lalaan I | 0402118019 |
| Lalaan II | 0402118020 |
| Litlit | 0402118021 |
| Lucsuhin | 0402118022 |
| Lumil | 0402118023 |
| Maguyam | 0402118026 |
| Malabag | 0402118027 |
| Malaking Tatyao | 0402118059 |
| Mataas Na Burol | 0402118028 |
| Munting Ilog | 0402118029 |
| Narra I | 0402118052 |
| Narra II | 0402118060 |
| Narra III | 0402118061 |
| Paligawan | 0402118030 |
| Pasong Langka | 0402118031 |
| Pooc I | 0402118037 |
| Pooc II | 0402118062 |
| Pulong Bunga | 0402118038 |
| Pulong Saging | 0402118039 |
| Puting Kahoy | 0402118040 |
| Sabutan | 0402118041 |
| San Miguel I | 0402118042 |
| San Miguel II | 0402118063 |
| San Vicente I | 0402118043 |
| San Vicente II | 0402118064 |
| Santol | 0402118044 |
| Tartaria | 0402118045 |
| Tibig | 0402118046 |
| Toledo | 0402118065 |
| Tubuan I | 0402118047 |
| Tubuan II | 0402118066 |
| Tubuan III | 0402118067 |
| Ulat | 0402118048 |
| Yakal | 0402118053 |

## Look up Silang with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0402118000") or cities.lookup("0402118000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Silang

```python
from barangay import search_fuzzy

for r in search_fuzzy("Silang", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
