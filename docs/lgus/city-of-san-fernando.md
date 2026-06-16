---
title: "Barangays in City of San Fernando, La Union — PSGC Codes"
description: "Complete list of 59 barangays in City of San Fernando, La Union with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of San Fernando, La Union

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of San Fernando, La Union",
  "description": "City in the Philippines with 59 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of San Fernando is a **city** in La Union (Philippines) with
**59 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abut | 0103314001 |
| Apaleng | 0103314002 |
| Bacsil | 0103314003 |
| Bangbangolan | 0103314004 |
| Bangcusay | 0103314005 |
| Barangay I | 0103314006 |
| Barangay II | 0103314007 |
| Barangay III | 0103314008 |
| Barangay IV | 0103314009 |
| Baraoas | 0103314010 |
| Bato | 0103314011 |
| Biday | 0103314012 |
| Birunget | 0103314013 |
| Bungro | 0103314014 |
| Cabaroan | 0103314015 |
| Cabarsican | 0103314016 |
| Cadaclan | 0103314017 |
| Calabugao | 0103314018 |
| Camansi | 0103314019 |
| Canaoay | 0103314020 |
| Carlatan | 0103314021 |
| Catbangen | 0103314022 |
| Dallangayan Este | 0103314023 |
| Dallangayan Oeste | 0103314024 |
| Dalumpinas Este | 0103314025 |
| Dalumpinas Oeste | 0103314026 |
| Ilocanos Norte | 0103314027 |
| Ilocanos Sur | 0103314028 |
| Langcuas | 0103314029 |
| Lingsat | 0103314030 |
| Madayegdeg | 0103314031 |
| Mameltac | 0103314032 |
| Masicong | 0103314033 |
| Nagyubuyuban | 0103314034 |
| Namtutan | 0103314035 |
| Narra Este | 0103314036 |
| Narra Oeste | 0103314037 |
| Pacpaco | 0103314039 |
| Pagdalagan | 0103314040 |
| Pagdaraoan | 0103314041 |
| Pagudpud | 0103314042 |
| Pao Norte | 0103314043 |
| Pao Sur | 0103314044 |
| Parian | 0103314045 |
| Pias | 0103314046 |
| Poro | 0103314047 |
| Puspus | 0103314048 |
| Sacyud | 0103314049 |
| Sagayad | 0103314050 |
| San Agustin | 0103314051 |
| San Francisco | 0103314052 |
| San Vicente | 0103314053 |
| Santiago Norte | 0103314054 |
| Santiago Sur | 0103314055 |
| Saoay | 0103314056 |
| Sevilla | 0103314057 |
| Siboan-Otong | 0103314058 |
| Tanqui | 0103314059 |
| Tanquigan | 0103314060 |

## Look up San Fernando with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0103314000") or cities.lookup("0103314000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in San Fernando

```python
from barangay import search_fuzzy

for r in search_fuzzy("San Fernando", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
