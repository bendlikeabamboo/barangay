---
title: "Barangays in Angadanan, Isabela — PSGC Codes"
description: "Complete list of 59 barangays in Angadanan, Isabela with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Angadanan, Isabela

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Angadanan, Isabela",
  "description": "Municipality in the Philippines with 59 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Isabela",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Isabela"
  }
}
</script>

Angadanan is a **municipality** in Isabela (Philippines) with
**59 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Allangigan | 0203102001 |
| Aniog | 0203102002 |
| Baniket | 0203102003 |
| Bannawag | 0203102004 |
| Bantug | 0203102005 |
| Barangcuag | 0203102006 |
| Baui | 0203102007 |
| Bonifacio | 0203102008 |
| Buenavista | 0203102009 |
| Bunnay | 0203102010 |
| Calabayan-Minanga | 0203102011 |
| Calaccab | 0203102012 |
| Calaocan | 0203102013 |
| Campanario | 0203102015 |
| Canangan | 0203102016 |
| Centro I | 0203102017 |
| Centro II | 0203102018 |
| Centro III | 0203102019 |
| Consular | 0203102020 |
| Cumu | 0203102021 |
| Dalakip | 0203102022 |
| Dalenat | 0203102023 |
| Dipaluda | 0203102024 |
| Duroc | 0203102025 |
| Esperanza | 0203102027 |
| Fugaru | 0203102028 |
| Ingud Norte | 0203102030 |
| Ingud Sur | 0203102031 |
| Kalusutan | 0203102014 |
| La Suerte | 0203102032 |
| Liwliwa | 0203102029 |
| Lomboy | 0203102033 |
| Loria | 0203102034 |
| Lourdes | 0203102026 |
| Mabuhay | 0203102035 |
| Macalauat | 0203102036 |
| Macaniao | 0203102037 |
| Malannao | 0203102038 |
| Malasin | 0203102039 |
| Mangandingay | 0203102040 |
| Minanga Proper | 0203102041 |
| Pappat | 0203102042 |
| Pissay | 0203102043 |
| Ramona | 0203102044 |
| Rancho Bassit | 0203102045 |
| Rang-ayan | 0203102046 |
| Salay | 0203102047 |
| San Ambrocio | 0203102048 |
| San Guillermo | 0203102049 |
| San Isidro | 0203102050 |
| San Marcelo | 0203102051 |
| San Roque | 0203102052 |
| San Vicente | 0203102053 |
| Santo Niño | 0203102054 |
| Saranay | 0203102055 |
| Sinabbaran | 0203102056 |
| Victory | 0203102058 |
| Viga | 0203102059 |
| Villa Domingo | 0203102060 |

## Look up Angadanan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0203102000") or cities.lookup("0203102000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Angadanan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Angadanan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
