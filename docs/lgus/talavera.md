---
title: "Barangays in Talavera, Nueva Ecija — PSGC Codes"
description: "Complete list of 53 barangays in Talavera, Nueva Ecija with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Talavera, Nueva Ecija

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Talavera, Nueva Ecija",
  "description": "Municipality in the Philippines with 53 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Talavera is a **municipality** in Nueva Ecija (Philippines) with
**53 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Andal Alino | 0304930001 |
| Bagong Sikat | 0304930002 |
| Bagong Silang | 0304930003 |
| Bakal I | 0304930004 |
| Bakal II | 0304930005 |
| Bakal III | 0304930006 |
| Baluga | 0304930008 |
| Bantug | 0304930009 |
| Bantug Hacienda | 0304930010 |
| Bantug Hamog | 0304930011 |
| Bugtong na Buli | 0304930012 |
| Bulac | 0304930013 |
| Burnay | 0304930014 |
| Caaniplahan | 0304930029 |
| Cabubulaonan | 0304930028 |
| Calipahan | 0304930015 |
| Campos | 0304930016 |
| Caputican | 0304930030 |
| Casulucan Este | 0304930018 |
| Collado | 0304930019 |
| Dimasalang Norte | 0304930020 |
| Dimasalang Sur | 0304930021 |
| Dinarayat | 0304930022 |
| Esguerra District | 0304930024 |
| Gulod | 0304930025 |
| Homestead I | 0304930026 |
| Homestead II | 0304930027 |
| Kinalanguyan | 0304930031 |
| La Torre | 0304930032 |
| Lomboy | 0304930033 |
| Mabuhay | 0304930034 |
| Maestrang Kikay | 0304930035 |
| Mamandil | 0304930036 |
| Marcos District | 0304930037 |
| Matingkis | 0304930039 |
| Minabuyoc | 0304930041 |
| Pag-asa | 0304930042 |
| Paludpod | 0304930043 |
| Pantoc Bulac | 0304930044 |
| Pinagpanaan | 0304930045 |
| Poblacion Sur | 0304930046 |
| Pula | 0304930047 |
| Pulong San Miguel | 0304930048 |
| Purok Matias | 0304930038 |
| Sampaloc | 0304930049 |
| San Miguel na Munti | 0304930050 |
| San Pascual | 0304930051 |
| San Ricardo | 0304930052 |
| Sibul | 0304930053 |
| Sicsican Matanda | 0304930054 |
| Tabacao | 0304930055 |
| Tagaytay | 0304930056 |
| Valle | 0304930057 |

## Look up Talavera with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0304930000") or cities.lookup("0304930000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Talavera

```python
from barangay import search_fuzzy

for r in search_fuzzy("Talavera", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
