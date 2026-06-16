---
title: "Barangays in City of Tayabas, Quezon — PSGC Codes"
description: "Complete list of 66 barangays in City of Tayabas, Quezon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Tayabas, Quezon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Tayabas, Quezon",
  "description": "City in the Philippines with 66 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Quezon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Quezon"
  }
}
</script>

City of Tayabas is a **city** in Quezon (Philippines) with
**66 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alitao | 0405647001 |
| Alsam Ibaba | 0405647019 |
| Alsam Ilaya | 0405647025 |
| Alupay | 0405647002 |
| Angeles Zone I | 0405647003 |
| Angeles Zone II | 0405647004 |
| Angeles Zone III | 0405647005 |
| Angeles Zone IV | 0405647006 |
| Angustias Zone I | 0405647007 |
| Angustias Zone II | 0405647008 |
| Angustias Zone III | 0405647009 |
| Angustias Zone IV | 0405647010 |
| Anos | 0405647011 |
| Ayaas | 0405647012 |
| Baguio | 0405647013 |
| Banilad | 0405647014 |
| Bukal Ibaba | 0405647020 |
| Bukal Ilaya | 0405647026 |
| Calantas | 0405647015 |
| Calumpang | 0405647032 |
| Camaysa | 0405647016 |
| Dapdap | 0405647017 |
| Domoit Kanluran | 0405647033 |
| Domoit Silangan | 0405647059 |
| Gibanga | 0405647018 |
| Ibas | 0405647024 |
| Ilasan Ibaba | 0405647021 |
| Ilasan Ilaya | 0405647027 |
| Ipilan | 0405647030 |
| Isabang | 0405647031 |
| Katigan Kanluran | 0405647034 |
| Katigan Silangan | 0405647060 |
| Lakawan | 0405647036 |
| Lalo | 0405647037 |
| Lawigue | 0405647038 |
| Lita | 0405647039 |
| Malaoa | 0405647040 |
| Masin | 0405647041 |
| Mate | 0405647042 |
| Mateuna | 0405647043 |
| Mayowe | 0405647044 |
| Nangka Ibaba | 0405647022 |
| Nangka Ilaya | 0405647028 |
| Opias | 0405647045 |
| Palale Ibaba | 0405647023 |
| Palale Ilaya | 0405647029 |
| Palale Kanluran | 0405647035 |
| Palale Silangan | 0405647061 |
| Pandakaki | 0405647046 |
| Pook | 0405647047 |
| Potol | 0405647048 |
| San Diego Zone I | 0405647049 |
| San Diego Zone II | 0405647050 |
| San Diego Zone III | 0405647051 |
| San Diego Zone IV | 0405647052 |
| San Isidro Zone I | 0405647053 |
| San Isidro Zone II | 0405647054 |
| San Isidro Zone III | 0405647055 |
| San Isidro Zone IV | 0405647056 |
| San Roque Zone I | 0405647057 |
| San Roque Zone II | 0405647058 |
| Talolong | 0405647062 |
| Tamlong | 0405647063 |
| Tongko | 0405647064 |
| Valencia | 0405647065 |
| Wakas | 0405647066 |

## Look up Tayabas with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0405647000") or cities.lookup("0405647000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tayabas

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tayabas", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
