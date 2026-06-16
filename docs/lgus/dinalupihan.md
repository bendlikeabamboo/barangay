---
title: "Barangays in Dinalupihan, Bataan — PSGC Codes"
description: "Complete list of 46 barangays in Dinalupihan, Bataan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Dinalupihan, Bataan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Dinalupihan, Bataan",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Bataan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Bataan"
  }
}
</script>

Dinalupihan is a **municipality** in Bataan (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aquino | 0300804044 |
| Bangal | 0300804002 |
| Bayan-bayanan | 0300804045 |
| Bonifacio | 0300804003 |
| Burgos | 0300804006 |
| Colo | 0300804007 |
| Daang Bago | 0300804008 |
| Dalao | 0300804009 |
| Del Pilar | 0300804010 |
| Gen. Luna | 0300804011 |
| Gomez | 0300804012 |
| Happy Valley | 0300804013 |
| Jose C. Payumo, Jr. | 0300804050 |
| Kataasan | 0300804014 |
| Layac | 0300804015 |
| Luacan | 0300804016 |
| Mabini Ext. | 0300804018 |
| Mabini Proper | 0300804017 |
| Magsaysay | 0300804019 |
| Maligaya | 0300804046 |
| Naparing | 0300804020 |
| New San Jose | 0300804021 |
| Old San Jose | 0300804022 |
| Padre Dandan | 0300804023 |
| Pag-asa | 0300804024 |
| Pagalanggang | 0300804025 |
| Payangan | 0300804047 |
| Pentor | 0300804048 |
| Pinulot | 0300804026 |
| Pita | 0300804027 |
| Rizal | 0300804029 |
| Roosevelt | 0300804030 |
| Roxas | 0300804031 |
| Saguing | 0300804032 |
| San Benito | 0300804033 |
| San Isidro | 0300804034 |
| San Pablo | 0300804035 |
| San Ramon | 0300804036 |
| San Simon | 0300804037 |
| Santa Isabel | 0300804040 |
| Santo Niño | 0300804038 |
| Sapang Balas | 0300804039 |
| Torres Bugauen | 0300804041 |
| Tubo-tubo | 0300804049 |
| Tucop | 0300804042 |
| Zamora | 0300804043 |

## Look up Dinalupihan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0300804000") or cities.lookup("0300804000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Dinalupihan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Dinalupihan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
