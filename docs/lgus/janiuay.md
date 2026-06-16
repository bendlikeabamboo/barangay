---
title: "Barangays in Janiuay, Iloilo — PSGC Codes"
description: "Complete list of 60 barangays in Janiuay, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Janiuay, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Janiuay, Iloilo",
  "description": "Municipality in the Philippines with 60 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Janiuay is a **municipality** in Iloilo (Philippines) with
**60 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abangay | 0603023001 |
| Agcarope | 0603023002 |
| Aglobong | 0603023003 |
| Aguingay | 0603023004 |
| Anhawan | 0603023005 |
| Aquino Nobleza East | 0603023046 |
| Aquino Nobleza West | 0603023047 |
| Atimonan | 0603023006 |
| Balanac | 0603023007 |
| Barasalon | 0603023008 |
| Bongol | 0603023009 |
| Cabantog | 0603023010 |
| Calmay | 0603023011 |
| Canawili | 0603023012 |
| Canawillian | 0603023013 |
| Capt. A. Tirador | 0603023060 |
| Caranas | 0603023014 |
| Caraudan | 0603023015 |
| Carigangan | 0603023016 |
| Concepcion Pob. | 0603023049 |
| Crispin Salazar North | 0603023055 |
| Crispin Salazar South | 0603023056 |
| Cunsad | 0603023017 |
| Dabong | 0603023018 |
| Damires | 0603023019 |
| Damo-ong | 0603023020 |
| Danao | 0603023021 |
| Don T. Lutero Center | 0603023052 |
| Don T. Lutero East | 0603023053 |
| Don T. Lutero West Pob. | 0603023054 |
| Gines | 0603023022 |
| Golgota | 0603023050 |
| Guadalupe | 0603023023 |
| Jibolo | 0603023025 |
| Kuyot | 0603023026 |
| Locsin | 0603023051 |
| Madong | 0603023027 |
| Manacabac | 0603023028 |
| Mangil | 0603023029 |
| Matag-ub | 0603023030 |
| Monte-Magapa | 0603023031 |
| Pangilihan | 0603023032 |
| Panuran | 0603023033 |
| Pararinga | 0603023034 |
| Patong-patong | 0603023035 |
| Quipot | 0603023036 |
| R. Armada | 0603023048 |
| S. M. Villa | 0603023061 |
| San Julian | 0603023057 |
| San Pedro | 0603023058 |
| Santa Rita | 0603023059 |
| Santo Tomas | 0603023037 |
| Sarawag | 0603023038 |
| Tambal | 0603023039 |
| Tamu-an | 0603023040 |
| Tiringanan | 0603023041 |
| Tolarucan | 0603023042 |
| Tuburan | 0603023043 |
| Ubian | 0603023044 |
| Yabon | 0603023045 |

## Look up Janiuay with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603023000") or cities.lookup("0603023000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Janiuay

```python
from barangay import search_fuzzy

for r in search_fuzzy("Janiuay", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
