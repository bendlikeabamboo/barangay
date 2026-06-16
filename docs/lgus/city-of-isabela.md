---
title: "Barangays in City of Isabela, Region IX (Zamboanga Peninsula) — PSGC Codes"
description: "Complete list of 45 barangays in City of Isabela, Region IX (Zamboanga Peninsula) with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Isabela, Region IX (Zamboanga Peninsula)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Isabela, Region IX (Zamboanga Peninsula)",
  "description": "City in the Philippines with 45 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Region IX (Zamboanga Peninsula)",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Region IX (Zamboanga Peninsula)"
  }
}
</script>

City of Isabela is a **city** in Region IX (Zamboanga Peninsula) (Philippines) with
**45 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aguada | 0990101002 |
| Balatanay | 0990101004 |
| Baluno | 0990101005 |
| Begang | 0990101006 |
| Binuangan | 0990101007 |
| Busay | 0990101008 |
| Cabunbata | 0990101010 |
| Calvario | 0990101011 |
| Carbon | 0990101012 |
| Diki | 0990101013 |
| Dona Ramona T. Alano | 0990101016 |
| Isabela Eastside | 0990101014 |
| Isabela Proper | 0990101015 |
| Kapatagan Grande | 0990101017 |
| Kapayawan | 0990101057 |
| Kaumpurnah Zone I | 0990101018 |
| Kaumpurnah Zone II | 0990101019 |
| Kaumpurnah Zone III | 0990101020 |
| Kumalarang | 0990101021 |
| La Piedad | 0990101022 |
| Lampinigan | 0990101023 |
| Lanote | 0990101024 |
| Lukbuton | 0990101027 |
| Lumbang | 0990101029 |
| Makiri | 0990101030 |
| Maligue | 0990101031 |
| Marang-marang | 0990101033 |
| Marketsite | 0990101034 |
| Masula | 0990101058 |
| Menzi | 0990101036 |
| Panigayan | 0990101038 |
| Panunsulan | 0990101039 |
| Port Area | 0990101040 |
| Riverside | 0990101041 |
| San Rafael | 0990101042 |
| Santa Barbara | 0990101043 |
| Santa Cruz | 0990101044 |
| Seaside | 0990101045 |
| Small Kapatagan | 0990101059 |
| Sumagdang | 0990101047 |
| Sunrise Village | 0990101049 |
| Tabiawan | 0990101050 |
| Tabuk | 0990101051 |
| Tampalan | 0990101060 |
| Timpul | 0990101055 |

## Look up Isabela with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0990101000") or cities.lookup("0990101000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Isabela

```python
from barangay import search_fuzzy

for r in search_fuzzy("Isabela", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
