---
title: "Barangays in Tobias Fornier, Antique — PSGC Codes"
description: "Complete list of 50 barangays in Tobias Fornier, Antique with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Tobias Fornier, Antique

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Tobias Fornier, Antique",
  "description": "Municipality in the Philippines with 50 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Antique",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Antique"
  }
}
</script>

Tobias Fornier is a **municipality** in Antique (Philippines) with
**50 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abaca | 0600607001 |
| Aras-Asan | 0600607002 |
| Arobo | 0600607003 |
| Atabay | 0600607004 |
| Atiotes | 0600607005 |
| Bagumbayan | 0600607006 |
| Ballescas | 0600607007 |
| Balud | 0600607008 |
| Barasanan A | 0600607009 |
| Barasanan B | 0600607010 |
| Barasanan C | 0600607011 |
| Bariri | 0600607012 |
| Camandagan | 0600607013 |
| Cato-ogan | 0600607014 |
| Danawan | 0600607015 |
| Diclum | 0600607016 |
| Fatima | 0600607017 |
| Gamad | 0600607018 |
| Igbalogo | 0600607019 |
| Igbangcal-A | 0600607020 |
| Igbangcal-B | 0600607021 |
| Igbangcal-C | 0600607022 |
| Igcabuad | 0600607023 |
| Igcadac | 0600607049 |
| Igcado | 0600607024 |
| Igcalawagan | 0600607025 |
| Igcapuyas | 0600607026 |
| Igcasicad | 0600607027 |
| Igdalaguit | 0600607028 |
| Igdanlog | 0600607029 |
| Igdurarog | 0600607030 |
| Igtugas | 0600607031 |
| Lawigan | 0600607032 |
| Lindero | 0600607050 |
| Manaling | 0600607033 |
| Masayo | 0600607034 |
| Nagsubuan | 0600607035 |
| Nasuli-A | 0600607042 |
| Opsan | 0600607041 |
| Paciencia | 0600607036 |
| Poblacion Norte | 0600607037 |
| Poblacion Sur | 0600607038 |
| Portillo | 0600607039 |
| Quezon | 0600607040 |
| Samalague | 0600607043 |
| Sto. Tomas | 0600607044 |
| Tacbuyan | 0600607045 |
| Tene | 0600607046 |
| Villaflor | 0600607047 |
| Ysulat | 0600607048 |

## Look up Tobias Fornier with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0600607000") or cities.lookup("0600607000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Tobias Fornier

```python
from barangay import search_fuzzy

for r in search_fuzzy("Tobias Fornier", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
