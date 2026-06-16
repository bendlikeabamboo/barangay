---
title: "Barangays in City of Pagadian, Zamboanga del Sur — PSGC Codes"
description: "Complete list of 54 barangays in City of Pagadian, Zamboanga del Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Pagadian, Zamboanga del Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Pagadian, Zamboanga del Sur",
  "description": "City in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Zamboanga del Sur",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Zamboanga del Sur"
  }
}
</script>

City of Pagadian is a **city** in Zamboanga del Sur (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alegria | 0907322001 |
| Balangasan | 0907322002 |
| Balintawak | 0907322003 |
| Baloyboan | 0907322004 |
| Banale | 0907322005 |
| Bogo | 0907322006 |
| Bomba | 0907322007 |
| Buenavista | 0907322010 |
| Bulatok | 0907322011 |
| Bulawan | 0907322012 |
| Dampalan | 0907322056 |
| Danlugan | 0907322013 |
| Dao | 0907322014 |
| Datagan | 0907322015 |
| Deborok | 0907322016 |
| Ditoray | 0907322017 |
| Dumagoc | 0907322057 |
| Gatas | 0907322018 |
| Gubac | 0907322019 |
| Gubang | 0907322020 |
| Kagawasan | 0907322021 |
| Kahayagan | 0907322022 |
| Kalasan | 0907322023 |
| Kawit | 0907322052 |
| La Suerte | 0907322024 |
| Lala | 0907322025 |
| Lapidian | 0907322026 |
| Lenienza | 0907322027 |
| Lizon Valley | 0907322028 |
| Lourdes | 0907322029 |
| Lower Sibatang | 0907322030 |
| Lumad | 0907322031 |
| Lumbia | 0907322053 |
| Macasing | 0907322032 |
| Manga | 0907322033 |
| Muricay | 0907322034 |
| Napolan | 0907322035 |
| Palpalan | 0907322036 |
| Pedulonan | 0907322037 |
| Poloyagan | 0907322038 |
| San Francisco | 0907322039 |
| San Jose | 0907322040 |
| San Pedro | 0907322041 |
| Santa Lucia | 0907322042 |
| Santa Maria | 0907322054 |
| Santiago | 0907322043 |
| Santo Niño | 0907322055 |
| Tawagan Sur | 0907322044 |
| Tiguma | 0907322045 |
| Tuburan | 0907322046 |
| Tulangan | 0907322048 |
| Tulawas | 0907322047 |
| Upper Sibatang | 0907322050 |
| White Beach | 0907322051 |

## Look up Pagadian with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0907322000") or cities.lookup("0907322000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Pagadian

```python
from barangay import search_fuzzy

for r in search_fuzzy("Pagadian", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
