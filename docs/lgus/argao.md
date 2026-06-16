---
title: "Barangays in Argao, Cebu — PSGC Codes"
description: "Complete list of 45 barangays in Argao, Cebu with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Argao, Cebu

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Argao, Cebu",
  "description": "Municipality in the Philippines with 45 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Cebu",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Cebu"
  }
}
</script>

Argao is a **municipality** in Cebu (Philippines) with
**45 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alambijud | 0702205001 |
| Anajao | 0702205002 |
| Apo | 0702205003 |
| Balaas | 0702205004 |
| Balisong | 0702205005 |
| Binlod | 0702205006 |
| Bogo | 0702205007 |
| Bug-ot | 0702205009 |
| Bulasa | 0702205010 |
| Butong | 0702205008 |
| Calagasan | 0702205012 |
| Canbantug | 0702205013 |
| Canbanua | 0702205014 |
| Cansuje | 0702205015 |
| Capio-an | 0702205016 |
| Casay | 0702205017 |
| Catang | 0702205018 |
| Colawin | 0702205019 |
| Conalum | 0702205020 |
| Guiwanon | 0702205021 |
| Gutlang | 0702205022 |
| Jampang | 0702205023 |
| Jomgao | 0702205024 |
| Lamacan | 0702205025 |
| Langtad | 0702205026 |
| Langub | 0702205027 |
| Lapay | 0702205028 |
| Lengigon | 0702205029 |
| Linut-od | 0702205030 |
| Mabasa | 0702205031 |
| Mandilikit | 0702205032 |
| Mompeller | 0702205033 |
| Panadtaran | 0702205034 |
| Poblacion | 0702205035 |
| Sua | 0702205036 |
| Sumaguan | 0702205037 |
| Tabayag | 0702205038 |
| Talaga | 0702205039 |
| Talaytay | 0702205040 |
| Talo-ot | 0702205041 |
| Tiguib | 0702205042 |
| Tulang | 0702205043 |
| Tulic | 0702205044 |
| Ubaub | 0702205045 |
| Usmad | 0702205046 |

## Look up Argao with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0702205000") or cities.lookup("0702205000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Argao

```python
from barangay import search_fuzzy

for r in search_fuzzy("Argao", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
