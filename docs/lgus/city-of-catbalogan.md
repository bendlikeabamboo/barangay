---
title: "Barangays in City of Catbalogan, Samar — PSGC Codes"
description: "Complete list of 57 barangays in City of Catbalogan, Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Catbalogan, Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Catbalogan, Samar",
  "description": "City in the Philippines with 57 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Samar"
  }
}
</script>

City of Catbalogan is a **city** in Samar (Philippines) with
**57 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Albalate | 0806005001 |
| Bagongon | 0806005002 |
| Bangon | 0806005003 |
| Basiao | 0806005004 |
| Buluan | 0806005005 |
| Bunuanan | 0806005006 |
| Cabugawan | 0806005007 |
| Cagudalo | 0806005008 |
| Cagusipan | 0806005009 |
| Cagutian | 0806005011 |
| Cagutsan | 0806005012 |
| Canhawan Gote | 0806005013 |
| Canlapwas | 0806005014 |
| Cawayan | 0806005015 |
| Cinco | 0806005016 |
| Darahuway Daco | 0806005017 |
| Darahuway Gote | 0806005018 |
| Estaka | 0806005019 |
| Guindaponan | 0806005049 |
| Guinsorongan | 0806005020 |
| Ibol | 0806005057 |
| Iguid | 0806005021 |
| Lagundi | 0806005022 |
| Libas | 0806005023 |
| Lobo | 0806005024 |
| Manguehay | 0806005025 |
| Maulong | 0806005026 |
| Mercedes | 0806005027 |
| Mombon | 0806005028 |
| Muñoz | 0806005047 |
| New Mahayag | 0806005029 |
| Old Mahayag | 0806005030 |
| Palanyogon | 0806005031 |
| Pangdan | 0806005032 |
| Payao | 0806005033 |
| Poblacion 1 | 0806005034 |
| Poblacion 10 | 0806005043 |
| Poblacion 11 | 0806005044 |
| Poblacion 12 | 0806005045 |
| Poblacion 13 | 0806005046 |
| Poblacion 2 | 0806005035 |
| Poblacion 3 | 0806005036 |
| Poblacion 4 | 0806005037 |
| Poblacion 5 | 0806005038 |
| Poblacion 6 | 0806005039 |
| Poblacion 7 | 0806005040 |
| Poblacion 8 | 0806005041 |
| Poblacion 9 | 0806005042 |
| Pupua | 0806005048 |
| Rama | 0806005050 |
| San Andres | 0806005051 |
| San Pablo | 0806005052 |
| San Roque | 0806005053 |
| San Vicente | 0806005054 |
| Silanga | 0806005055 |
| Socorro | 0806005059 |
| Totoringon | 0806005056 |

## Look up Catbalogan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0806005000") or cities.lookup("0806005000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Catbalogan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Catbalogan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
