---
title: "Barangays in Igbaras, Iloilo — PSGC Codes"
description: "Complete list of 46 barangays in Igbaras, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Igbaras, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Igbaras, Iloilo",
  "description": "Municipality in the Philippines with 46 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

Igbaras is a **municipality** in Iloilo (Philippines) with
**46 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alameda | 0603021001 |
| Amorogtong | 0603021002 |
| Anilawan | 0603021003 |
| Bagacay | 0603021004 |
| Bagacayan | 0603021005 |
| Bagay | 0603021006 |
| Balibagan | 0603021007 |
| Barangay 1 Poblacion | 0603021033 |
| Barangay 2 Poblacion | 0603021034 |
| Barangay 3 Poblacion | 0603021035 |
| Barangay 4 Poblacion | 0603021036 |
| Barangay 5 Poblacion | 0603021037 |
| Barangay 6 Poblacion | 0603021038 |
| Barasan | 0603021008 |
| Binanua-an | 0603021009 |
| Boclod | 0603021010 |
| Buenavista | 0603021011 |
| Buga | 0603021012 |
| Bugnay | 0603021013 |
| Calampitao | 0603021014 |
| Cale | 0603021015 |
| Catiringan | 0603021017 |
| Corucuan | 0603021016 |
| Igcabugao | 0603021018 |
| Igpigus | 0603021019 |
| Igtalongon | 0603021020 |
| Indaluyon | 0603021021 |
| Jovellar | 0603021022 |
| Kinagdan | 0603021023 |
| Lab-on | 0603021024 |
| Lacay Dol-Dol | 0603021025 |
| Lumangan | 0603021026 |
| Lutungan | 0603021027 |
| Mantangon | 0603021028 |
| Mulangan | 0603021029 |
| Pasong | 0603021030 |
| Passi | 0603021031 |
| Pinaopawan | 0603021032 |
| Riro-an | 0603021039 |
| San Ambrosio | 0603021040 |
| Santa Barbara | 0603021041 |
| Signe | 0603021042 |
| Tabiac | 0603021043 |
| Talayatay | 0603021044 |
| Taytay | 0603021045 |
| Tigbanaba | 0603021046 |

## Look up Igbaras with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603021000") or cities.lookup("0603021000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Igbaras

```python
from barangay import search_fuzzy

for r in search_fuzzy("Igbaras", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
