---
title: "Barangays in City of Sorsogon, Sorsogon — PSGC Codes"
description: "Complete list of 64 barangays in City of Sorsogon, Sorsogon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Sorsogon, Sorsogon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Sorsogon, Sorsogon",
  "description": "City in the Philippines with 64 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Sorsogon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Sorsogon"
  }
}
</script>

City of Sorsogon is a **city** in Sorsogon (Philippines) with
**64 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abuyog | 0506216001 |
| Almendras-Cogon | 0506216002 |
| Balete | 0506216038 |
| Balogo (Bacon District) | 0506216039 |
| Balogo (Sorsogon East District) | 0506216003 |
| Barayong | 0506216004 |
| Basud | 0506216005 |
| Bato | 0506216040 |
| Bibincahan | 0506216006 |
| Bitan-o/Dalipay | 0506216008 |
| Bogña | 0506216042 |
| Bon-Ot | 0506216041 |
| Bucalbucalan | 0506216009 |
| Buenavista (Bacon District) | 0506216043 |
| Buenavista (Sorsogon West District) | 0506216010 |
| Buhatan | 0506216011 |
| Bulabog | 0506216012 |
| Burabod | 0506216013 |
| Cabarbuhan | 0506216044 |
| Cabid-An | 0506216014 |
| Cambulaga | 0506216015 |
| Capuy | 0506216016 |
| Caricaran | 0506216045 |
| Del Rosario | 0506216046 |
| Gatbo | 0506216047 |
| Gimaloto | 0506216017 |
| Guinlajon | 0506216018 |
| Jamislagan | 0506216048 |
| Macabog | 0506216019 |
| Maricrum | 0506216049 |
| Marinas | 0506216020 |
| Osiao | 0506216050 |
| Pamurayan | 0506216021 |
| Pangpang | 0506216022 |
| Panlayaan | 0506216023 |
| Peñafrancia | 0506216024 |
| Piot | 0506216025 |
| Poblacion | 0506216051 |
| Polvorista | 0506216026 |
| Rawis | 0506216052 |
| Rizal | 0506216027 |
| Salog | 0506216028 |
| Salvacion (Bacon District) | 0506216053 |
| Salvacion (Sorsogon West District) | 0506216029 |
| Sampaloc | 0506216030 |
| San Isidro (Bacon District) | 0506216054 |
| San Isidro (Sorsogon West District) | 0506216031 |
| San Juan | 0506216055 |
| San Juan (Roro) | 0506216032 |
| San Pascual | 0506216056 |
| San Ramon | 0506216057 |
| San Roque | 0506216058 |
| San Vicente | 0506216059 |
| Santa Cruz | 0506216060 |
| Santa Lucia | 0506216061 |
| Santo Domingo | 0506216062 |
| Santo Niño | 0506216063 |
| Sawanga | 0506216064 |
| Sirangan | 0506216033 |
| Sugod | 0506216065 |
| Sulucan | 0506216034 |
| Talisay | 0506216035 |
| Ticol | 0506216036 |
| Tugos | 0506216037 |

## Look up Sorsogon with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0506216000") or cities.lookup("0506216000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Sorsogon

```python
from barangay import search_fuzzy

for r in search_fuzzy("Sorsogon", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
