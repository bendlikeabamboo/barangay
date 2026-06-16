---
title: "Barangays in City of Zamboanga, Region IX (Zamboanga Peninsula) — PSGC Codes"
description: "Complete list of 98 barangays in City of Zamboanga, Region IX (Zamboanga Peninsula) with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Zamboanga, Region IX (Zamboanga Peninsula)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Zamboanga, Region IX (Zamboanga Peninsula)",
  "description": "City in the Philippines with 98 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of Zamboanga is a **city** in Region IX (Zamboanga Peninsula) (Philippines) with
**98 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Arena Blanco | 0931700001 |
| Ayala | 0931700002 |
| Baliwasan | 0931700004 |
| Baluno | 0931700005 |
| Barangay Zone I | 0931700061 |
| Barangay Zone II | 0931700062 |
| Barangay Zone III | 0931700063 |
| Barangay Zone IV | 0931700064 |
| Boalan | 0931700010 |
| Bolong | 0931700011 |
| Buenavista | 0931700012 |
| Bunguiao | 0931700013 |
| Busay | 0931700014 |
| Cabaluay | 0931700015 |
| Cabatangan | 0931700016 |
| Cacao | 0931700017 |
| Calabasa | 0931700018 |
| Calarian | 0931700019 |
| Camino Nuevo | 0931700099 |
| Campo Islam | 0931700020 |
| Canelar | 0931700021 |
| Capisan | 0931700098 |
| Cawit | 0931700022 |
| Culianan | 0931700023 |
| Curuan | 0931700024 |
| Dita | 0931700025 |
| Divisoria | 0931700026 |
| Dulian (Upper Bunguiao) | 0931700027 |
| Dulian (Upper Pasonanca) | 0931700028 |
| Guisao | 0931700030 |
| Guiwan | 0931700031 |
| Kasanyangan | 0931700101 |
| La Paz | 0931700032 |
| Labuan | 0931700033 |
| Lamisahan | 0931700034 |
| Landang Gua | 0931700035 |
| Landang Laum | 0931700036 |
| Lanzones | 0931700037 |
| Lapakan | 0931700038 |
| Latuan | 0931700039 |
| Licomo | 0931700100 |
| Limaong | 0931700040 |
| Limpapa | 0931700041 |
| Lubigan | 0931700042 |
| Lumayang | 0931700043 |
| Lumbangan | 0931700044 |
| Lunzuran | 0931700045 |
| Maasin | 0931700046 |
| Malagutay | 0931700047 |
| Mampang | 0931700048 |
| Manalipa | 0931700049 |
| Mangusu | 0931700050 |
| Manicahan | 0931700051 |
| Mariki | 0931700052 |
| Mercedes | 0931700053 |
| Muti | 0931700054 |
| Pamucutan | 0931700055 |
| Pangapuyan | 0931700056 |
| Panubigan | 0931700057 |
| Pasilmanta | 0931700058 |
| Pasobolong | 0931700102 |
| Pasonanca | 0931700059 |
| Patalon | 0931700060 |
| Putik | 0931700065 |
| Quiniput | 0931700066 |
| Recodo | 0931700067 |
| Rio Hondo | 0931700068 |
| Salaan | 0931700069 |
| San Jose Cawa-cawa | 0931700070 |
| San Jose Gusu | 0931700071 |
| San Roque | 0931700072 |
| Sangali | 0931700073 |
| Santa Barbara | 0931700074 |
| Santa Catalina | 0931700075 |
| Santa Maria | 0931700076 |
| Santo Niño | 0931700077 |
| Sibulao | 0931700078 |
| Sinubung | 0931700079 |
| Sinunoc | 0931700080 |
| Tagasilay | 0931700081 |
| Taguiti | 0931700082 |
| Talabaan | 0931700083 |
| Talisayan | 0931700084 |
| Talon-talon | 0931700085 |
| Taluksangay | 0931700086 |
| Tetuan | 0931700087 |
| Tictapul | 0931700088 |
| Tigbalabag | 0931700089 |
| Tigtabon | 0931700090 |
| Tolosa | 0931700091 |
| Tugbungan | 0931700092 |
| Tulungatung | 0931700093 |
| Tumaga | 0931700094 |
| Tumalutab | 0931700095 |
| Tumitus | 0931700096 |
| Victoria | 0931700103 |
| Vitali | 0931700097 |
| Zambowood | 0931700104 |

## Look up Zamboanga with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0931700000") or cities.lookup("0931700000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Zamboanga

```python
from barangay import search_fuzzy

for r in search_fuzzy("Zamboanga", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
