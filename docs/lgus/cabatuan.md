---
title: "Barangays in Cabatuan, Iloilo — PSGC Codes"
description: "Complete list of 68 barangays in Cabatuan, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Cabatuan, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Cabatuan, Iloilo",
  "description": "Municipality in the Philippines with 68 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Iloilo",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Iloilo"
  }
}
</script>

Cabatuan is a **municipality** in Iloilo (Philippines) with
**68 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Acao | 0603012001 |
| Amerang | 0603012002 |
| Amurao | 0603012003 |
| Anuang | 0603012004 |
| Ayaman | 0603012005 |
| Ayong | 0603012006 |
| Bacan | 0603012007 |
| Balabag | 0603012008 |
| Baluyan | 0603012009 |
| Banguit | 0603012010 |
| Bulay | 0603012011 |
| Cadoldolan | 0603012012 |
| Cagban | 0603012013 |
| Calawagan | 0603012014 |
| Calayo | 0603012015 |
| Duyanduyan | 0603012016 |
| Gaub | 0603012017 |
| Gines Interior | 0603012018 |
| Gines Patag | 0603012019 |
| Guibuangan Tigbauan | 0603012020 |
| Inabasan | 0603012021 |
| Inaca | 0603012022 |
| Inaladan | 0603012023 |
| Ingas | 0603012024 |
| Ito Norte | 0603012025 |
| Ito Sur | 0603012026 |
| Janipaan Central | 0603012027 |
| Janipaan Este | 0603012028 |
| Janipaan Oeste | 0603012029 |
| Janipaan Olo | 0603012030 |
| Jelicuon Lusaya | 0603012031 |
| Jelicuon Montinola | 0603012032 |
| Lag-an | 0603012033 |
| Leong | 0603012034 |
| Lutac | 0603012035 |
| Manguna | 0603012036 |
| Maraguit | 0603012037 |
| Morubuan | 0603012038 |
| Pacatin | 0603012039 |
| Pagotpot | 0603012040 |
| Pamul-Ogan | 0603012041 |
| Pamuringao Garrido | 0603012043 |
| Pamuringao Proper | 0603012042 |
| Pungtod | 0603012055 |
| Puyas | 0603012056 |
| Salacay | 0603012057 |
| Sulanga | 0603012059 |
| Tabucan | 0603012060 |
| Tacdangan | 0603012061 |
| Talanghauan | 0603012062 |
| Tigbauan Road | 0603012063 |
| Tinio-an | 0603012064 |
| Tiring | 0603012065 |
| Tupol Central | 0603012066 |
| Tupol Este | 0603012067 |
| Tupol Oeste | 0603012068 |
| Tuy-an | 0603012069 |
| Zone I Pob. | 0603012044 |
| Zone II Pob. | 0603012047 |
| Zone III Pob. | 0603012048 |
| Zone IV Pob. | 0603012049 |
| Zone IX Pob. | 0603012054 |
| Zone V Pob. | 0603012050 |
| Zone VI Pob. | 0603012051 |
| Zone VII Pob. | 0603012052 |
| Zone VIII Pob. | 0603012053 |
| Zone X Pob. | 0603012045 |
| Zone XI Pob. | 0603012046 |

## Look up Cabatuan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603012000") or cities.lookup("0603012000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Cabatuan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Cabatuan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
