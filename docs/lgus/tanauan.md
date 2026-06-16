---
title: "Barangays in Tanauan, Leyte — PSGC Codes"
description: "Complete list of 54 barangays in Tanauan, Leyte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tanauan, Leyte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tanauan, Leyte",
  "description": "Municipality in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Tanauan is a **municipality** in Leyte (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Ada | 0803748001 |
| Amanluran | 0803748002 |
| Arado | 0803748003 |
| Atipolo | 0803748004 |
| Balud | 0803748005 |
| Bangon | 0803748006 |
| Bantagan | 0803748007 |
| Baras | 0803748008 |
| Binolo | 0803748009 |
| Binongto-an | 0803748010 |
| Bislig | 0803748011 |
| Buntay | 0803748040 |
| Cabalagnan | 0803748012 |
| Cabarasan Guti | 0803748013 |
| Cabonga-an | 0803748014 |
| Cabuynan | 0803748015 |
| Cahumayhumayan | 0803748016 |
| Calogcog | 0803748017 |
| Calsadahay | 0803748018 |
| Camire | 0803748019 |
| Canbalisara | 0803748020 |
| Canramos | 0803748041 |
| Catigbian | 0803748021 |
| Catmon | 0803748022 |
| Cogon | 0803748023 |
| Guindag-an | 0803748024 |
| Guingawan | 0803748025 |
| Hilagpad | 0803748026 |
| Kiling | 0803748054 |
| Lapay | 0803748028 |
| Licod | 0803748042 |
| Limbuhan Daku | 0803748029 |
| Limbuhan Guti | 0803748030 |
| Linao | 0803748031 |
| Magay | 0803748032 |
| Maghulod | 0803748033 |
| Malaguicay | 0803748034 |
| Maribi | 0803748035 |
| Mohon | 0803748036 |
| Pago | 0803748037 |
| Pasil | 0803748038 |
| Pikas | 0803748039 |
| Sacme | 0803748055 |
| Salvador | 0803748044 |
| San Isidro | 0803748045 |
| San Miguel | 0803748043 |
| San Roque | 0803748046 |
| San Victor | 0803748047 |
| Santa Cruz | 0803748048 |
| Santa Elena | 0803748049 |
| Santo Niño Pob. | 0803748050 |
| Solano | 0803748051 |
| Talolora | 0803748052 |
| Tugop | 0803748053 |

## Look up Tanauan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0803748000") or cities.lookup("0803748000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tanauan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tanauan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
