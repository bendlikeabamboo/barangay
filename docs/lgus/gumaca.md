---
title: "Barangays in Gumaca, Quezon — PSGC Codes"
description: "Complete list of 59 barangays in Gumaca, Quezon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Gumaca, Quezon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Gumaca, Quezon",
  "description": "Municipality in the Philippines with 59 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Gumaca is a **municipality** in Quezon (Philippines) with
**59 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adia Bitaog | 0405619001 |
| Anonangin | 0405619002 |
| Bagong Buhay | 0405619003 |
| Bamban | 0405619004 |
| Bantad | 0405619006 |
| Batong Dalig | 0405619007 |
| Biga | 0405619008 |
| Binambang | 0405619009 |
| Buensuceso | 0405619010 |
| Bungahan | 0405619011 |
| Butaguin | 0405619012 |
| Calumangin | 0405619013 |
| Camohaguin | 0405619014 |
| Casasahan Ibaba | 0405619015 |
| Casasahan Ilaya | 0405619016 |
| Cawayan | 0405619017 |
| Gayagayaan | 0405619018 |
| Gitnang Barrio | 0405619019 |
| Hagakhakin | 0405619023 |
| Hardinan | 0405619020 |
| Inaclagan | 0405619021 |
| Inagbuhan Ilaya | 0405619022 |
| Labnig | 0405619024 |
| Laguna | 0405619025 |
| Lagyo | 0405619060 |
| Mabini | 0405619026 |
| Mabunga | 0405619027 |
| Malabtog | 0405619028 |
| Manlayaan | 0405619029 |
| Marcelo H. Del Pilar | 0405619030 |
| Mataas Na Bundok | 0405619031 |
| Maunlad | 0405619032 |
| Pagsabangan | 0405619033 |
| Panikihan | 0405619034 |
| Peñafrancia | 0405619035 |
| Pipisik | 0405619036 |
| Progreso | 0405619037 |
| Rizal | 0405619038 |
| Rosario | 0405619039 |
| San Agustin | 0405619040 |
| San Diego | 0405619058 |
| San Diego Poblacion | 0405619041 |
| San Isidro Kanluran | 0405619042 |
| San Isidro Silangan | 0405619043 |
| San Juan De Jesus | 0405619044 |
| San Vicente | 0405619045 |
| Sastre | 0405619046 |
| Tabing Dagat | 0405619047 |
| Tumayan | 0405619048 |
| Villa Arcaya | 0405619049 |
| Villa Bota | 0405619050 |
| Villa Fuerte | 0405619051 |
| Villa M. Principe | 0405619055 |
| Villa Mendoza | 0405619052 |
| Villa Nava | 0405619059 |
| Villa Padua | 0405619053 |
| Villa Perez | 0405619054 |
| Villa Tañada | 0405619056 |
| Villa Victoria | 0405619057 |

## Look up Gumaca with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0405619000") or cities.lookup("0405619000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Gumaca

```python
from barangay import search_fuzzy

for r in search_fuzzy("Gumaca", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
