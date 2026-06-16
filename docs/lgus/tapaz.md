---
title: "Barangays in Tapaz, Capiz — PSGC Codes"
description: "Complete list of 58 barangays in Tapaz, Capiz with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tapaz, Capiz

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tapaz, Capiz",
  "description": "Municipality in the Philippines with 58 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Capiz",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Capiz"
  }
}
</script>

Tapaz is a **municipality** in Capiz (Philippines) with
**58 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abangay | 0601917001 |
| Acuña | 0601917002 |
| Agcococ | 0601917003 |
| Aglinab | 0601917004 |
| Aglupacan | 0601917005 |
| Agpalali | 0601917006 |
| Apero | 0601917007 |
| Artuz | 0601917008 |
| Bag-Ong Barrio | 0601917009 |
| Bato-bato | 0601917010 |
| Buri | 0601917011 |
| Camburanan | 0601917012 |
| Candelaria | 0601917013 |
| Carida | 0601917014 |
| Cristina | 0601917015 |
| Da-an Banwa | 0601917016 |
| Da-an Norte | 0601917017 |
| Da-an Sur | 0601917018 |
| Garcia | 0601917019 |
| Gebio-an | 0601917020 |
| Hilwan | 0601917021 |
| Initan | 0601917022 |
| Katipunan | 0601917023 |
| Lagdungan | 0601917024 |
| Lahug | 0601917025 |
| Libertad | 0601917026 |
| Mabini | 0601917027 |
| Maliao | 0601917028 |
| Malitbog | 0601917029 |
| Minan | 0601917030 |
| Nayawan | 0601917031 |
| Poblacion | 0601917032 |
| Rizal Norte | 0601917033 |
| Rizal Sur | 0601917034 |
| Roosevelt | 0601917035 |
| Roxas | 0601917036 |
| Salong | 0601917037 |
| San Antonio | 0601917038 |
| San Francisco | 0601917039 |
| San Jose | 0601917041 |
| San Julian | 0601917042 |
| San Miguel Ilawod | 0601917043 |
| San Miguel Ilaya | 0601917044 |
| San Nicolas | 0601917045 |
| San Pedro | 0601917046 |
| San Roque | 0601917047 |
| San Vicente | 0601917048 |
| Santa Ana | 0601917049 |
| Santa Petronila | 0601917050 |
| Senonod | 0601917051 |
| Siya | 0601917052 |
| Switch | 0601917053 |
| Tabon | 0601917054 |
| Tacayan | 0601917055 |
| Taft | 0601917056 |
| Taganghin | 0601917057 |
| Taslan | 0601917058 |
| Wright | 0601917059 |

## Look up Tapaz with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0601917000") or cities.lookup("0601917000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tapaz

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tapaz", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
