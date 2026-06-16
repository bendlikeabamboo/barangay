---
title: "Barangays in Dueñas, Iloilo — PSGC Codes"
description: "Complete list of 47 barangays in Dueñas, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Dueñas, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Due\u00f1as, Iloilo",
  "description": "Municipality in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Dueñas is a **municipality** in Iloilo (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agutayan | 0603017001 |
| Angare | 0603017002 |
| Anjawan | 0603017003 |
| Baac | 0603017004 |
| Bagongbong | 0603017005 |
| Balangigan | 0603017006 |
| Balingasag | 0603017007 |
| Banugan | 0603017008 |
| Batuan | 0603017009 |
| Bita | 0603017010 |
| Buenavista | 0603017011 |
| Bugtongan | 0603017012 |
| Cabudian | 0603017013 |
| Calaca-an | 0603017014 |
| Calang | 0603017015 |
| Calawinan | 0603017016 |
| Capaycapay | 0603017017 |
| Capuling | 0603017018 |
| Catig | 0603017019 |
| Dila-an | 0603017020 |
| Fundacion | 0603017021 |
| Inadlawan | 0603017022 |
| Jagdong | 0603017023 |
| Jaguimit | 0603017024 |
| Lacadon | 0603017025 |
| Luag | 0603017026 |
| Malusgod | 0603017027 |
| Maribuyong | 0603017028 |
| Minanga | 0603017029 |
| Monpon | 0603017030 |
| Navalas | 0603017031 |
| Pader | 0603017032 |
| Pandan | 0603017033 |
| Poblacion A | 0603017048 |
| Poblacion B | 0603017049 |
| Poblacion C | 0603017050 |
| Poblacion D | 0603017051 |
| Ponong Grande | 0603017038 |
| Ponong Pequeño | 0603017039 |
| Purog | 0603017040 |
| Romblon | 0603017041 |
| San Isidro | 0603017042 |
| Santo Niño | 0603017043 |
| Sawe | 0603017044 |
| Taminla | 0603017045 |
| Tinocuan | 0603017046 |
| Tipolo | 0603017047 |

## Look up Dueñas with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603017000") or cities.lookup("0603017000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Dueñas

```python
from barangay import search_fuzzy

for r in search_fuzzy("Dueñas", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
