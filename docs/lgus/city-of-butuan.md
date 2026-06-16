---
title: "Barangays in City of Butuan, Region XIII (Caraga) — PSGC Codes"
description: "Complete list of 86 barangays in City of Butuan, Region XIII (Caraga) with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Butuan, Region XIII (Caraga)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Butuan, Region XIII (Caraga)",
  "description": "City in the Philippines with 86 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Region XIII (Caraga)",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Region XIII (Caraga)"
  }
}
</script>

City of Butuan is a **city** in Region XIII (Caraga) (Philippines) with
**86 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agao Pob. | 1630400002 |
| Agusan Pequeño | 1630400003 |
| Ambago | 1630400004 |
| Amparo | 1630400006 |
| Ampayon | 1630400007 |
| Anticala | 1630400008 |
| Antongalon | 1630400009 |
| Aupagan | 1630400010 |
| Baan KM 3 | 1630400012 |
| Baan Riverside Pob. | 1630400033 |
| Babag | 1630400013 |
| Bading Pob. | 1630400014 |
| Bancasi | 1630400016 |
| Banza | 1630400017 |
| Baobaoan | 1630400018 |
| Basag | 1630400019 |
| Bayanihan Pob. | 1630400020 |
| Bilay | 1630400021 |
| Bit-os | 1630400022 |
| Bitan-agan | 1630400023 |
| Bobon | 1630400024 |
| Bonbon | 1630400025 |
| Bugabus | 1630400026 |
| Bugsukan | 1630400092 |
| Buhangin Pob. | 1630400027 |
| Cabcabon | 1630400029 |
| Camayahan | 1630400031 |
| Dagohoy Pob. | 1630400044 |
| Dankias | 1630400036 |
| De Oro | 1630400093 |
| Diego Silang Pob. | 1630400038 |
| Don Francisco | 1630400102 |
| Doongan | 1630400039 |
| Dulag | 1630400094 |
| Dumalagan | 1630400040 |
| Florida | 1630400095 |
| Golden Ribbon Pob. | 1630400043 |
| Holy Redeemer Pob. | 1630400047 |
| Humabon Pob. | 1630400048 |
| Imadejas Pob. | 1630400037 |
| Jose Rizal Pob. | 1630400045 |
| Kinamlutan | 1630400049 |
| Lapu-lapu Pob. | 1630400051 |
| Lemon | 1630400052 |
| Leon Kilat Pob. | 1630400053 |
| Libertad | 1630400054 |
| Limaha Pob. | 1630400055 |
| Los Angeles | 1630400056 |
| Lumbocan | 1630400057 |
| Maguinda | 1630400060 |
| Mahay | 1630400061 |
| Mahogany Pob. | 1630400062 |
| Maibu | 1630400063 |
| Mandamo | 1630400064 |
| Manila de Bugabus | 1630400065 |
| Maon Pob. | 1630400066 |
| Masao | 1630400067 |
| Maug | 1630400068 |
| New Society Village Pob. | 1630400070 |
| Nong-nong | 1630400096 |
| Obrero Pob. | 1630400091 |
| Ong Yiu Pob. | 1630400071 |
| Pagatpatan | 1630400097 |
| Pangabugan | 1630400098 |
| Pianing | 1630400072 |
| Pigdaulan | 1630400103 |
| Pinamanculan | 1630400073 |
| Port Poyohon Pob. | 1630400069 |
| Rajah Soliman Pob. | 1630400074 |
| Salvacion | 1630400099 |
| San Ignacio Pob. | 1630400075 |
| San Mateo | 1630400076 |
| San Vicente | 1630400077 |
| Santo Niño | 1630400100 |
| Sikatuna Pob. | 1630400078 |
| Silongan Pob. | 1630400079 |
| Sumile | 1630400101 |
| Sumilihon | 1630400080 |
| Tagabaca | 1630400082 |
| Taguibo | 1630400083 |
| Taligaman | 1630400084 |
| Tandang Sora Pob. | 1630400085 |
| Tiniwisan | 1630400086 |
| Tungao | 1630400087 |
| Urduja Pob. | 1630400089 |
| Villa Kananga | 1630400090 |

## Look up Butuan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("1630400000") or cities.lookup("1630400000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Butuan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Butuan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
