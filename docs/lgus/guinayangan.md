---
title: "Barangays in Guinayangan, Quezon — PSGC Codes"
description: "Complete list of 54 barangays in Guinayangan, Quezon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Guinayangan, Quezon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Guinayangan, Quezon",
  "description": "Municipality in the Philippines with 54 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Guinayangan is a **municipality** in Quezon (Philippines) with
**54 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| A. Mabini | 0405618001 |
| Aloneros | 0405618002 |
| Arbismen | 0405618003 |
| Bagong Silang | 0405618004 |
| Balinarin | 0405618005 |
| Bukal Maligaya | 0405618006 |
| Cabibihan | 0405618007 |
| Cabong Norte | 0405618008 |
| Cabong Sur | 0405618009 |
| Calimpak | 0405618010 |
| Capuluan Central | 0405618011 |
| Capuluan Tulon | 0405618012 |
| Dancalan Caimawan | 0405618013 |
| Dancalan Central | 0405618014 |
| Danlagan Batis | 0405618015 |
| Danlagan Cabayao | 0405618016 |
| Danlagan Central | 0405618017 |
| Danlagan Reserva | 0405618018 |
| Del Rosario | 0405618019 |
| Dungawan Central | 0405618020 |
| Dungawan Paalyunan | 0405618021 |
| Dungawan Pantay | 0405618022 |
| Ermita | 0405618023 |
| Gapas | 0405618024 |
| Himbubulo Este | 0405618025 |
| Himbubulo Weste | 0405618026 |
| Hinabaan | 0405618027 |
| Ligpit Bantayan | 0405618028 |
| Lubigan | 0405618029 |
| Magallanes | 0405618030 |
| Magsaysay | 0405618031 |
| Manggagawa | 0405618032 |
| Manggalang | 0405618033 |
| Manlayo | 0405618034 |
| Poblacion | 0405618035 |
| Salakan | 0405618036 |
| San Antonio | 0405618037 |
| San Isidro | 0405618038 |
| San Jose | 0405618039 |
| San Lorenzo | 0405618040 |
| San Luis I | 0405618041 |
| San Luis II | 0405618042 |
| San Miguel | 0405618043 |
| San Pedro I | 0405618044 |
| San Pedro II | 0405618045 |
| San Roque | 0405618046 |
| Santa Cruz | 0405618047 |
| Santa Maria | 0405618048 |
| Santa Teresita | 0405618049 |
| Sintones | 0405618050 |
| Sisi | 0405618051 |
| Tikay | 0405618052 |
| Triumpo | 0405618053 |
| Villa Hiwasayan | 0405618054 |

## Look up Guinayangan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0405618000") or cities.lookup("0405618000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Guinayangan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Guinayangan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
