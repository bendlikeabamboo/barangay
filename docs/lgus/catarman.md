---
title: "Barangays in Catarman, Northern Samar — PSGC Codes"
description: "Complete list of 55 barangays in Catarman, Northern Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Catarman, Northern Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Catarman, Northern Samar",
  "description": "Municipality in the Philippines with 55 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Northern Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Northern Samar"
  }
}
</script>

Catarman is a **municipality** in Northern Samar (Philippines) with
**55 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Acacia | 0804805062 |
| Aguinaldo | 0804805001 |
| Airport Village | 0804805002 |
| Bangkerohan | 0804805076 |
| Baybay | 0804805003 |
| Bocsol | 0804805005 |
| Cabayhan | 0804805007 |
| Cag-abaca | 0804805008 |
| Cal-igang | 0804805010 |
| Calachuchi | 0804805072 |
| Cawayan | 0804805011 |
| Cervantes | 0804805012 |
| Cularima | 0804805013 |
| Daganas | 0804805015 |
| Dalakit | 0804805077 |
| Doña Pulqueria | 0804805025 |
| Galutan | 0804805016 |
| Gebalagnan | 0804805021 |
| Gebulwangan | 0804805022 |
| General Malvar | 0804805018 |
| Guba | 0804805020 |
| Hinatad | 0804805026 |
| Imelda | 0804805027 |
| Ipil-ipil | 0804805066 |
| Jose Abad Santos | 0804805067 |
| Jose P. Rizal | 0804805075 |
| Kasoy | 0804805068 |
| Lapu-lapu | 0804805069 |
| Liberty | 0804805028 |
| Libjo | 0804805029 |
| Mabini | 0804805032 |
| Mabolo | 0804805074 |
| Macagtas | 0804805033 |
| Mckinley | 0804805034 |
| Molave | 0804805064 |
| Narra | 0804805071 |
| New Rizal | 0804805037 |
| Old Rizal | 0804805038 |
| Paticua | 0804805041 |
| Polangi | 0804805042 |
| Quezon | 0804805043 |
| Salvacion | 0804805045 |
| Sampaguita | 0804805073 |
| San Julian | 0804805049 |
| San Pascual | 0804805078 |
| Santol | 0804805070 |
| Somoge | 0804805051 |
| Talisay | 0804805063 |
| Tinowaran | 0804805053 |
| Trangue | 0804805054 |
| UEP I | 0804805059 |
| UEP II | 0804805060 |
| UEP III | 0804805061 |
| Washington | 0804805056 |
| Yakal | 0804805065 |

## Look up Catarman with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0804805000") or cities.lookup("0804805000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Catarman

```python
from barangay import search_fuzzy

for r in search_fuzzy("Catarman", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
