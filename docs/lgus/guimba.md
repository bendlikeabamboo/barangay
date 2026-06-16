---
title: "Barangays in Guimba, Nueva Ecija — PSGC Codes"
description: "Complete list of 64 barangays in Guimba, Nueva Ecija with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Guimba, Nueva Ecija

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Guimba, Nueva Ecija",
  "description": "Municipality in the Philippines with 64 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Nueva Ecija",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Nueva Ecija"
  }
}
</script>

Guimba is a **municipality** in Nueva Ecija (Philippines) with
**64 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agcano | 0304911001 |
| Ayos Lomboy | 0304911002 |
| Bacayao | 0304911003 |
| Bagong Barrio | 0304911004 |
| Balbalino | 0304911005 |
| Balingog East | 0304911006 |
| Balingog West | 0304911007 |
| Banitan | 0304911008 |
| Bantug | 0304911009 |
| Bulakid | 0304911011 |
| Bunol | 0304911070 |
| Caballero | 0304911014 |
| Cabaruan | 0304911015 |
| Caingin Tabing Ilog | 0304911016 |
| Calem | 0304911017 |
| Camiing | 0304911018 |
| Cardinal | 0304911019 |
| Casongsong | 0304911020 |
| Catimon | 0304911021 |
| Cavite | 0304911022 |
| Cawayan Bugtong | 0304911023 |
| Consuelo | 0304911024 |
| Culong | 0304911025 |
| Escano | 0304911026 |
| Faigal | 0304911027 |
| Galvan | 0304911028 |
| Guiset | 0304911029 |
| Lamorito | 0304911030 |
| Lennec | 0304911031 |
| Macamias | 0304911032 |
| Macapabellag | 0304911033 |
| Macatcatuit | 0304911034 |
| Manacsac | 0304911035 |
| Manggang Marikit | 0304911036 |
| Maturanoc | 0304911038 |
| Maybubon | 0304911039 |
| Naglabrahan | 0304911041 |
| Nagpandayan | 0304911042 |
| Narvacan I | 0304911043 |
| Narvacan II | 0304911044 |
| Pacac | 0304911045 |
| Partida I | 0304911046 |
| Partida II | 0304911047 |
| Pasong Inchic | 0304911048 |
| Saint John District | 0304911049 |
| San Agustin | 0304911050 |
| San Andres | 0304911051 |
| San Bernardino | 0304911052 |
| San Marcelino | 0304911053 |
| San Miguel | 0304911054 |
| San Rafael | 0304911055 |
| San Roque | 0304911056 |
| Santa Ana | 0304911057 |
| Santa Cruz | 0304911058 |
| Santa Lucia | 0304911059 |
| Santa Veronica District | 0304911060 |
| Santo Cristo District | 0304911061 |
| Saranay District | 0304911062 |
| Sinulatan | 0304911063 |
| Subol | 0304911064 |
| Tampac I | 0304911065 |
| Tampac II &amp; III | 0304911066 |
| Triala | 0304911068 |
| Yuson | 0304911069 |

## Look up Guimba with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0304911000") or cities.lookup("0304911000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Guimba

```python
from barangay import search_fuzzy

for r in search_fuzzy("Guimba", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
