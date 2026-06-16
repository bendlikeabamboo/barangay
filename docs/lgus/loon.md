---
title: "Barangays in Loon, Bohol — PSGC Codes"
description: "Complete list of 67 barangays in Loon, Bohol with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Loon, Bohol

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Loon, Bohol",
  "description": "Municipality in the Philippines with 67 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Bohol",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Bohol"
  }
}
</script>

Loon is a **municipality** in Bohol (Philippines) with
**67 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agsoso | 0701230001 |
| Badbad Occidental | 0701230002 |
| Badbad Oriental | 0701230003 |
| Bagacay Katipunan | 0701230004 |
| Bagacay Kawayan | 0701230005 |
| Bagacay Saong | 0701230006 |
| Bahi | 0701230007 |
| Basac | 0701230008 |
| Basdacu | 0701230009 |
| Basdio | 0701230010 |
| Biasong | 0701230011 |
| Bongco | 0701230012 |
| Bugho | 0701230013 |
| Cabacongan | 0701230014 |
| Cabadug | 0701230015 |
| Cabug | 0701230016 |
| Calayugan Norte | 0701230017 |
| Calayugan Sur | 0701230018 |
| Cambaquiz | 0701230020 |
| Campatud | 0701230021 |
| Candaigan | 0701230022 |
| Canhangdon Occidental | 0701230023 |
| Canhangdon Oriental | 0701230024 |
| Canigaan | 0701230025 |
| Canmaag | 0701230019 |
| Canmanoc | 0701230026 |
| Cansuagwit | 0701230027 |
| Cansubayon | 0701230028 |
| Cantam-is Bago | 0701230032 |
| Cantam-is Baslay | 0701230035 |
| Cantaongon | 0701230033 |
| Cantumocad | 0701230034 |
| Catagbacan Handig | 0701230029 |
| Catagbacan Norte | 0701230030 |
| Catagbacan Sur | 0701230031 |
| Cogon Norte | 0701230036 |
| Cogon Sur | 0701230037 |
| Cuasi | 0701230038 |
| Genomoan | 0701230039 |
| Lintuan | 0701230040 |
| Looc | 0701230041 |
| Mocpoc Norte | 0701230042 |
| Mocpoc Sur | 0701230043 |
| Moto Norte | 0701230050 |
| Moto Sur | 0701230051 |
| Nagtuang | 0701230044 |
| Napo | 0701230045 |
| Nueva Vida | 0701230046 |
| Panangquilon | 0701230047 |
| Pantudlan | 0701230048 |
| Pig-ot | 0701230049 |
| Pondol | 0701230052 |
| Quinobcoban | 0701230053 |
| Sondol | 0701230054 |
| Song-on | 0701230055 |
| Talisay | 0701230056 |
| Tan-awan | 0701230057 |
| Tangnan | 0701230058 |
| Taytay | 0701230059 |
| Ticugan | 0701230060 |
| Tiwi | 0701230061 |
| Tontonan | 0701230062 |
| Tubodacu | 0701230063 |
| Tubodio | 0701230064 |
| Tubuan | 0701230065 |
| Ubayon | 0701230066 |
| Ubojan | 0701230067 |

## Look up Loon with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0701230000") or cities.lookup("0701230000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Loon

```python
from barangay import search_fuzzy

for r in search_fuzzy("Loon", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
