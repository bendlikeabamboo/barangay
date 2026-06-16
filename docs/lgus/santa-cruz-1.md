---
title: "Barangays in Santa Cruz, Ilocos Sur — PSGC Codes"
description: "Complete list of 49 barangays in Santa Cruz, Ilocos Sur with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Santa Cruz, Ilocos Sur

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Santa Cruz, Ilocos Sur",
  "description": "Municipality in the Philippines with 49 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Ilocos Sur",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Ilocos Sur"
  }
}
</script>

Santa Cruz is a **municipality** in Ilocos Sur (Philippines) with
**49 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Amarao | 0102924001 |
| Babayoan | 0102924002 |
| Bacsayan | 0102924003 |
| Banay | 0102924004 |
| Bayugao Este | 0102924005 |
| Bayugao Oeste | 0102924006 |
| Besalan | 0102924007 |
| Bugbuga | 0102924008 |
| Calaoaan | 0102924009 |
| Camanggaan | 0102924010 |
| Candalican | 0102924011 |
| Capariaan | 0102924012 |
| Casilagan | 0102924013 |
| Coscosnong | 0102924014 |
| Daligan | 0102924015 |
| Dili | 0102924016 |
| Gabor Norte | 0102924017 |
| Gabor Sur | 0102924018 |
| Lalong | 0102924019 |
| Lantag | 0102924020 |
| Las-ud | 0102924021 |
| Mambog | 0102924022 |
| Mantanas | 0102924023 |
| Nagtengnga | 0102924024 |
| Padaoil | 0102924025 |
| Paratong | 0102924026 |
| Pattiqui | 0102924027 |
| Pidpid | 0102924028 |
| Pilar | 0102924029 |
| Pinipin | 0102924030 |
| Poblacion Este | 0102924031 |
| Poblacion Norte | 0102924032 |
| Poblacion Sur | 0102924034 |
| Poblacion Weste | 0102924033 |
| Quinfermin | 0102924035 |
| Quinsoriano | 0102924036 |
| Sagat | 0102924037 |
| San Antonio | 0102924038 |
| San Jose | 0102924039 |
| San Pedro | 0102924040 |
| Saoat | 0102924041 |
| Sevilla | 0102924042 |
| Sidaoen | 0102924043 |
| Suyo | 0102924044 |
| Tampugo | 0102924045 |
| Turod | 0102924046 |
| Villa Garcia | 0102924047 |
| Villa Hermosa | 0102924048 |
| Villa Laurencia | 0102924049 |

## Look up Santa Cruz with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0102924000") or cities.lookup("0102924000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Santa Cruz

```python
from barangay import search_fuzzy

for r in search_fuzzy("Santa Cruz", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
