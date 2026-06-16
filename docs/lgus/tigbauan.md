---
title: "Barangays in Tigbauan, Iloilo — PSGC Codes"
description: "Complete list of 52 barangays in Tigbauan, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tigbauan, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tigbauan, Iloilo",
  "description": "Municipality in the Philippines with 52 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Tigbauan is a **municipality** in Iloilo (Philippines) with
**52 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alupidian | 0603045001 |
| Atabayan | 0603045002 |
| Bagacay | 0603045003 |
| Baguingin | 0603045004 |
| Bagumbayan | 0603045005 |
| Bangkal | 0603045006 |
| Bantud | 0603045007 |
| Barangay 1 | 0603045008 |
| Barangay 2 | 0603045009 |
| Barangay 3 | 0603045010 |
| Barangay 4 | 0603045011 |
| Barangay 5 | 0603045012 |
| Barangay 6 | 0603045013 |
| Barangay 7 | 0603045014 |
| Barangay 8 | 0603045015 |
| Barangay 9 | 0603045016 |
| Barosong | 0603045017 |
| Barroc | 0603045018 |
| Bayuco | 0603045019 |
| Binaliuan Mayor | 0603045020 |
| Binaliuan Menor | 0603045021 |
| Bitas | 0603045022 |
| Buenavista | 0603045023 |
| Bugasongan | 0603045024 |
| Buyu-an | 0603045025 |
| Canabuan | 0603045026 |
| Cansilayan | 0603045027 |
| Cordova Norte | 0603045028 |
| Cordova Sur | 0603045029 |
| Danao | 0603045030 |
| Dapdap | 0603045031 |
| Dorong-an | 0603045032 |
| Guisian | 0603045033 |
| Isauan | 0603045034 |
| Isian | 0603045035 |
| Jamog | 0603045036 |
| Lanag | 0603045037 |
| Linobayan | 0603045038 |
| Lubog | 0603045039 |
| Nagba | 0603045040 |
| Namocon | 0603045041 |
| Napnapan Norte | 0603045042 |
| Napnapan Sur | 0603045043 |
| Olo Barroc | 0603045044 |
| Parara Norte | 0603045045 |
| Parara Sur | 0603045046 |
| San Rafael | 0603045047 |
| Sermon | 0603045048 |
| Sipitan | 0603045049 |
| Supa | 0603045050 |
| Tan Pael | 0603045051 |
| Taro | 0603045052 |

## Look up Tigbauan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603045000") or cities.lookup("0603045000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tigbauan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tigbauan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
