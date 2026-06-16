---
title: "Barangays in City of Puerto Princesa, MIMAROPA Region — PSGC Codes"
description: "Complete list of 66 barangays in City of Puerto Princesa, MIMAROPA Region with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Puerto Princesa, MIMAROPA Region

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Puerto Princesa, MIMAROPA Region",
  "description": "City in the Philippines with 66 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "MIMAROPA Region",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "MIMAROPA Region"
  }
}
</script>

City of Puerto Princesa is a **city** in MIMAROPA Region (Philippines) with
**66 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Babuyan | 1731500001 |
| Bacungan | 1731500002 |
| Bagong Bayan | 1731500003 |
| Bagong Pag-Asa | 1731500004 |
| Bagong Sikat | 1731500005 |
| Bagong Silang | 1731500006 |
| Bahile | 1731500008 |
| Bancao-bancao | 1731500009 |
| Binduyan | 1731500010 |
| Buenavista | 1731500011 |
| Cabayugan | 1731500012 |
| Concepcion | 1731500013 |
| Inagawan | 1731500014 |
| Inagawan Sub-Colony | 1731500063 |
| Irawan | 1731500015 |
| Iwahig | 1731500016 |
| Kalipay | 1731500017 |
| Kamuning | 1731500018 |
| Langogan | 1731500019 |
| Liwanag | 1731500020 |
| Lucbuan | 1731500021 |
| Luzviminda | 1731500064 |
| Mabuhay | 1731500022 |
| Macarascas | 1731500023 |
| Magkakaibigan | 1731500024 |
| Maligaya | 1731500025 |
| Manalo | 1731500026 |
| Mandaragat | 1731500065 |
| Manggahan | 1731500027 |
| Mangingisda | 1731500062 |
| Maningning | 1731500028 |
| Maoyon | 1731500029 |
| Marufinas | 1731500030 |
| Maruyogon | 1731500031 |
| Masigla | 1731500032 |
| Masikap | 1731500033 |
| Masipag | 1731500034 |
| Matahimik | 1731500035 |
| Matiyaga | 1731500036 |
| Maunlad | 1731500037 |
| Milagrosa | 1731500038 |
| Model | 1731500039 |
| Montible | 1731500040 |
| Napsan | 1731500041 |
| New Panggangan | 1731500042 |
| Pagkakaisa | 1731500043 |
| Princesa | 1731500044 |
| Salvacion | 1731500045 |
| San Jose | 1731500046 |
| San Manuel | 1731500066 |
| San Miguel | 1731500047 |
| San Pedro | 1731500048 |
| San Rafael | 1731500049 |
| Santa Cruz | 1731500050 |
| Santa Lourdes | 1731500051 |
| Santa Lucia | 1731500052 |
| Santa Monica | 1731500053 |
| Seaside | 1731500054 |
| Sicsican | 1731500055 |
| Simpocan | 1731500056 |
| Tagabinit | 1731500057 |
| Tagburos | 1731500058 |
| Tagumpay | 1731500059 |
| Tanabag | 1731500060 |
| Tanglaw | 1731500061 |
| Tiniguiban | 1731500067 |

## Look up Puerto Princesa with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1731500000") or cities.lookup("1731500000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Puerto Princesa

```python
from barangay import search_fuzzy

for r in search_fuzzy("Puerto Princesa", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
