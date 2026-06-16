---
title: "Barangays in Guiuan, Eastern Samar — PSGC Codes"
description: "Complete list of 60 barangays in Guiuan, Eastern Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Guiuan, Eastern Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Guiuan, Eastern Samar",
  "description": "Municipality in the Philippines with 60 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Eastern Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Eastern Samar"
  }
}
</script>

Guiuan is a **municipality** in Eastern Samar (Philippines) with
**60 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alingarog | 0802609001 |
| Bagua | 0802609002 |
| Banaag | 0802609003 |
| Banahao | 0802609004 |
| Baras | 0802609005 |
| Barbo | 0802609006 |
| Bitaugan | 0802609007 |
| Bucao | 0802609009 |
| Buenavista | 0802609010 |
| Bungtod | 0802609008 |
| Cagdara-o | 0802609011 |
| Cagusu-an | 0802609012 |
| Camparang | 0802609013 |
| Campoyong | 0802609014 |
| Canawayon | 0802609058 |
| Cantahay | 0802609015 |
| Casuguran | 0802609017 |
| Cogon | 0802609018 |
| Culasi | 0802609019 |
| Dalaragan | 0802609059 |
| Gahoy | 0802609022 |
| Habag | 0802609024 |
| Hagna | 0802609060 |
| Hamorawon | 0802609025 |
| Hollywood | 0802609061 |
| Inapulangan | 0802609026 |
| Lupok | 0802609028 |
| Mayana | 0802609029 |
| Ngolos | 0802609030 |
| Pagbabangnan | 0802609031 |
| Pagnamitan | 0802609032 |
| Poblacion Ward 1 | 0802609033 |
| Poblacion Ward 10 | 0802609020 |
| Poblacion Ward 11 | 0802609035 |
| Poblacion Ward 12 | 0802609036 |
| Poblacion Ward 2 | 0802609034 |
| Poblacion Ward 3 | 0802609037 |
| Poblacion Ward 4 | 0802609038 |
| Poblacion Ward 4-A | 0802609027 |
| Poblacion Ward 5 | 0802609039 |
| Poblacion Ward 6 | 0802609040 |
| Poblacion Ward 7 | 0802609041 |
| Poblacion Ward 8 | 0802609042 |
| Poblacion Ward 9 | 0802609043 |
| Poblacion Ward 9-A | 0802609021 |
| Salug | 0802609044 |
| San Antonio | 0802609045 |
| San Jose | 0802609046 |
| San Juan | 0802609062 |
| San Pedro | 0802609047 |
| Santo Niño | 0802609063 |
| Sapao | 0802609048 |
| Sulangan | 0802609050 |
| Suluan | 0802609051 |
| Surok | 0802609052 |
| Tagporo | 0802609064 |
| Taytay | 0802609054 |
| Timala | 0802609055 |
| Trinidad | 0802609056 |
| Victory Island | 0802609057 |

## Look up Guiuan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0802609000") or cities.lookup("0802609000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Guiuan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Guiuan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
