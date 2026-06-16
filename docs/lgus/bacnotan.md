---
title: "Barangays in Bacnotan, La Union — PSGC Codes"
description: "Complete list of 47 barangays in Bacnotan, La Union with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Bacnotan, La Union

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Bacnotan, La Union",
  "description": "Municipality in the Philippines with 47 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "La Union",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "La Union"
  }
}
</script>

Bacnotan is a **municipality** in La Union (Philippines) with
**47 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agtipal | 0103303001 |
| Arosip | 0103303002 |
| Bacqui | 0103303003 |
| Bacsil | 0103303004 |
| Bagutot | 0103303005 |
| Ballogo | 0103303006 |
| Baroro | 0103303007 |
| Bitalag | 0103303008 |
| Bulala | 0103303009 |
| Burayoc | 0103303010 |
| Bussaoit | 0103303011 |
| Cabaroan | 0103303012 |
| Cabarsican | 0103303013 |
| Cabugao | 0103303014 |
| Calautit | 0103303015 |
| Carcarmay | 0103303016 |
| Casiaman | 0103303017 |
| Galongen | 0103303018 |
| Guinabang | 0103303019 |
| Legleg | 0103303020 |
| Lisqueb | 0103303021 |
| Mabanengbeng 1st | 0103303022 |
| Mabanengbeng 2nd | 0103303023 |
| Maragayap | 0103303024 |
| Nagatiran | 0103303026 |
| Nagsaraboan | 0103303027 |
| Nagsimbaanan | 0103303028 |
| Nangalisan | 0103303025 |
| Narra | 0103303029 |
| Ortega | 0103303030 |
| Oya-oy | 0103303046 |
| Paagan | 0103303031 |
| Pandan | 0103303032 |
| Pang-pang | 0103303033 |
| Poblacion | 0103303034 |
| Quirino | 0103303035 |
| Raois | 0103303036 |
| Salincob | 0103303037 |
| San Martin | 0103303038 |
| Santa Cruz | 0103303039 |
| Santa Rita | 0103303040 |
| Sapilang | 0103303041 |
| Sayoan | 0103303042 |
| Sipulo | 0103303043 |
| Tammocalao | 0103303044 |
| Ubbog | 0103303045 |
| Zaragosa | 0103303047 |

## Look up Bacnotan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0103303000") or cities.lookup("0103303000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Bacnotan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Bacnotan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
