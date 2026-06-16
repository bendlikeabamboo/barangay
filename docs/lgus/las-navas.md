---
title: "Barangays in Las Navas, Northern Samar — PSGC Codes"
description: "Complete list of 53 barangays in Las Navas, Northern Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Las Navas, Northern Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Las Navas, Northern Samar",
  "description": "Municipality in the Philippines with 53 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Northern Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Northern Samar"
  }
}
</script>

Las Navas is a **municipality** in Northern Samar (Philippines) with
**53 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Balugo | 0804810001 |
| Bugay | 0804810002 |
| Bugtosan | 0804810003 |
| Bukid | 0804810004 |
| Bulao | 0804810005 |
| Caputoan | 0804810006 |
| Catoto-ogan | 0804810007 |
| Cuenco | 0804810008 |
| Dapdap | 0804810009 |
| Del Pilar | 0804810010 |
| Dolores | 0804810011 |
| Epaw | 0804810012 |
| Geguinta | 0804810013 |
| Geracdo | 0804810014 |
| Guyo | 0804810015 |
| H. Jolejole | 0804810054 |
| H. Jolejole District | 0804810016 |
| Hangi | 0804810017 |
| Imelda | 0804810018 |
| L. Empon | 0804810019 |
| Lakandula | 0804810020 |
| Lourdes | 0804810022 |
| Lumala-og | 0804810021 |
| Mabini | 0804810023 |
| Macarthur | 0804810024 |
| Magsaysay | 0804810025 |
| Matelarag | 0804810026 |
| Osmeña | 0804810027 |
| Paco | 0804810028 |
| Palanas | 0804810029 |
| Perez | 0804810030 |
| Poponton | 0804810031 |
| Quezon | 0804810032 |
| Quirino | 0804810033 |
| Quirino District | 0804810034 |
| Rebong | 0804810035 |
| Rizal | 0804810036 |
| Roxas | 0804810037 |
| Rufino | 0804810038 |
| Sag-od | 0804810039 |
| San Andres | 0804810040 |
| San Antonio | 0804810041 |
| San Fernando | 0804810042 |
| San Francisco | 0804810043 |
| San Isidro | 0804810045 |
| San Jorge | 0804810046 |
| San Jose | 0804810047 |
| San Miguel | 0804810048 |
| Santo Tomas | 0804810049 |
| Tagab-iran | 0804810050 |
| Tagan-ayan | 0804810051 |
| Taylor | 0804810052 |
| Victory | 0804810053 |

## Look up Las Navas with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0804810000") or cities.lookup("0804810000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Las Navas

```python
from barangay import search_fuzzy

for r in search_fuzzy("Las Navas", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
