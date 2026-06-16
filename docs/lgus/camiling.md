---
title: "Barangays in Camiling, Tarlac — PSGC Codes"
description: "Complete list of 61 barangays in Camiling, Tarlac with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Camiling, Tarlac

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Camiling, Tarlac",
  "description": "Municipality in the Philippines with 61 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Tarlac",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Tarlac"
  }
}
</script>

Camiling is a **municipality** in Tarlac (Philippines) with
**61 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Anoling 1st | 0306903001 |
| Anoling 2nd | 0306903002 |
| Anoling 3rd | 0306903003 |
| Bacabac | 0306903004 |
| Bacsay | 0306903005 |
| Bancay 1st | 0306903006 |
| Bilad | 0306903008 |
| Birbira | 0306903009 |
| Bobon 1st | 0306903012 |
| Bobon 2nd | 0306903013 |
| Bobon Caarosipan | 0306903011 |
| Cabanabaan | 0306903016 |
| Cacamilingan Norte | 0306903017 |
| Cacamilingan Sur | 0306903018 |
| Caniag | 0306903019 |
| Carael | 0306903020 |
| Cayaoan | 0306903021 |
| Cayasan | 0306903022 |
| Florida | 0306903023 |
| Lasong | 0306903024 |
| Libueg | 0306903025 |
| Malacampa | 0306903027 |
| Manaquem | 0306903028 |
| Manupeg | 0306903029 |
| Marawi | 0306903030 |
| Matubog | 0306903031 |
| Nagrambacan | 0306903033 |
| Nagserialan | 0306903034 |
| Palimbo Caarosipan | 0306903036 |
| Palimbo Proper | 0306903035 |
| Pao 1st | 0306903037 |
| Pao 2nd | 0306903038 |
| Pao 3rd | 0306903039 |
| Papaac | 0306903040 |
| Pindangan 1st | 0306903041 |
| Pindangan 2nd | 0306903042 |
| Poblacion A | 0306903043 |
| Poblacion B | 0306903044 |
| Poblacion C | 0306903045 |
| Poblacion D | 0306903046 |
| Poblacion E | 0306903047 |
| Poblacion F | 0306903048 |
| Poblacion G | 0306903049 |
| Poblacion H | 0306903050 |
| Poblacion I | 0306903051 |
| Poblacion J | 0306903052 |
| San Isidro | 0306903007 |
| Sawat | 0306903055 |
| Sinilian 1st | 0306903057 |
| Sinilian 2nd | 0306903058 |
| Sinilian 3rd | 0306903059 |
| Sinilian Cacalibosoan | 0306903060 |
| Sinulatan 1st | 0306903061 |
| Sinulatan 2nd | 0306903062 |
| Sta. Maria | 0306903053 |
| Surgui 1st | 0306903063 |
| Surgui 2nd | 0306903064 |
| Surgui 3rd | 0306903065 |
| Tambugan | 0306903066 |
| Telbang | 0306903067 |
| Tuec | 0306903068 |

## Look up Camiling with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0306903000") or cities.lookup("0306903000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Camiling

```python
from barangay import search_fuzzy

for r in search_fuzzy("Camiling", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
