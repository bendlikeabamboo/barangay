---
title: "Barangays in Jaro, Leyte — PSGC Codes"
description: "Complete list of 46 barangays in Jaro, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Jaro, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Jaro, Leyte",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Jaro is a **municipality** in Leyte (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alahag | 0803723001 |
| Anibongan | 0803723002 |
| Atipolo | 0803723044 |
| Badiang | 0803723003 |
| Batug | 0803723004 |
| Bias Zabala | 0803723043 |
| Buenavista | 0803723005 |
| Bukid | 0803723006 |
| Burabod | 0803723007 |
| Buri | 0803723008 |
| Canapuan | 0803723045 |
| Canhandugan | 0803723010 |
| Crossing Rubas | 0803723011 |
| Daro | 0803723012 |
| District I | 0803723027 |
| District II | 0803723028 |
| District III | 0803723029 |
| District IV | 0803723030 |
| Hiagsam | 0803723013 |
| Hibucawan | 0803723015 |
| Hibunawon | 0803723014 |
| Kaglawaan | 0803723009 |
| Kalinawan | 0803723016 |
| La Paz | 0803723046 |
| Likod | 0803723017 |
| Macanip | 0803723018 |
| Macopa | 0803723019 |
| Mag-aso | 0803723020 |
| Malobago | 0803723021 |
| Olotan | 0803723023 |
| Palanog | 0803723047 |
| Pange | 0803723024 |
| Parasan | 0803723025 |
| Pitogo | 0803723026 |
| Sagkahan | 0803723031 |
| San Agustin | 0803723032 |
| San Pedro | 0803723033 |
| San Roque | 0803723034 |
| Santa Cruz | 0803723035 |
| Santo Niño | 0803723036 |
| Sari-sari | 0803723037 |
| Tinambacan | 0803723038 |
| Tuba | 0803723039 |
| Uguiao | 0803723040 |
| Villa Paz | 0803723042 |
| Villagonzoilo | 0803723041 |

## Look up Jaro with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803723000") or cities.lookup("0803723000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Jaro

```python
from barangay import search_fuzzy

for r in search_fuzzy("Jaro", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
