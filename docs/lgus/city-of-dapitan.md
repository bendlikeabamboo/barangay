---
title: "Barangays in City of Dapitan, Zamboanga del Norte — PSGC Codes"
description: "Complete list of 50 barangays in City of Dapitan, Zamboanga del Norte with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Dapitan, Zamboanga del Norte

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Dapitan, Zamboanga del Norte",
  "description": "City in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Zamboanga del Norte",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Zamboanga del Norte"
  }
}
</script>

City of Dapitan is a **city** in Zamboanga del Norte (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aliguay | 0907201001 |
| Antipolo | 0907201002 |
| Aseniero | 0907201003 |
| Ba-ao | 0907201004 |
| Bagting | 0907201048 |
| Banbanan | 0907201005 |
| Banonong | 0907201049 |
| Barcelona | 0907201006 |
| Baylimango | 0907201007 |
| Burgos | 0907201009 |
| Canlucani | 0907201010 |
| Carang | 0907201011 |
| Cawa-cawa | 0907201050 |
| Dampalan | 0907201012 |
| Daro | 0907201013 |
| Dawo | 0907201051 |
| Diwa-an | 0907201014 |
| Guimputlan | 0907201016 |
| Hilltop | 0907201017 |
| Ilaya | 0907201018 |
| Kauswagan | 0907201046 |
| Larayan | 0907201019 |
| Linabo | 0907201053 |
| Liyang | 0907201020 |
| Maria Cristina | 0907201021 |
| Maria Uray | 0907201022 |
| Masidlakon | 0907201023 |
| Matagobtob Pob. | 0907201052 |
| Napo | 0907201024 |
| Opao | 0907201025 |
| Oro | 0907201026 |
| Owaon | 0907201027 |
| Oyan | 0907201028 |
| Polo | 0907201031 |
| Potol | 0907201054 |
| Potungan | 0907201032 |
| San Francisco | 0907201033 |
| San Nicolas | 0907201034 |
| San Pedro | 0907201035 |
| San Vicente | 0907201036 |
| Santa Cruz | 0907201055 |
| Santo Niño | 0907201042 |
| Selinog | 0907201040 |
| Sicayab-Bucana | 0907201038 |
| Sigayan | 0907201039 |
| Sinonoc | 0907201041 |
| Sulangon | 0907201043 |
| Tag-ulo | 0907201044 |
| Taguilon | 0907201045 |
| Tamion | 0907201047 |

## Look up Dapitan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0907201000") or cities.lookup("0907201000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Dapitan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Dapitan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
