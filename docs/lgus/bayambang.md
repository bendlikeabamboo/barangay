---
title: "Barangays in Bayambang, Pangasinan — PSGC Codes"
description: "Complete list of 77 barangays in Bayambang, Pangasinan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Bayambang, Pangasinan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Bayambang, Pangasinan",
  "description": "Municipality in the Philippines with 77 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Pangasinan",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Pangasinan"
  }
}
</script>

Bayambang is a **municipality** in Pangasinan (Philippines) with
**77 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Alinggan | 0105511001 |
| Amancosiling Norte | 0105511003 |
| Amancosiling Sur | 0105511004 |
| Amanperez | 0105511002 |
| Ambayat I | 0105511005 |
| Ambayat II | 0105511006 |
| Apalen | 0105511007 |
| Asin | 0105511008 |
| Ataynan | 0105511009 |
| Bacnono | 0105511010 |
| Balaybuaya | 0105511011 |
| Banaban | 0105511012 |
| Bani | 0105511013 |
| Batangcaoa | 0105511014 |
| Beleng | 0105511015 |
| Bical Norte | 0105511016 |
| Bical Sur | 0105511017 |
| Bongato East | 0105511018 |
| Bongato West | 0105511019 |
| Buayaen | 0105511020 |
| Buenlag 1st | 0105511021 |
| Buenlag 2nd | 0105511022 |
| Cadre Site | 0105511023 |
| Carungay | 0105511024 |
| Caturay | 0105511025 |
| Darawey | 0105511065 |
| Duera | 0105511027 |
| Dusoc | 0105511028 |
| Hermoza | 0105511029 |
| Idong | 0105511030 |
| Inanlorenza | 0105511031 |
| Inirangan | 0105511032 |
| Iton | 0105511033 |
| Langiran | 0105511034 |
| Ligue | 0105511035 |
| M. H. del Pilar | 0105511036 |
| Macayocayo | 0105511037 |
| Magsaysay | 0105511038 |
| Maigpa | 0105511039 |
| Malimpec | 0105511040 |
| Malioer | 0105511041 |
| Managos | 0105511042 |
| Manambong Norte | 0105511043 |
| Manambong Parte | 0105511044 |
| Manambong Sur | 0105511045 |
| Mangayao | 0105511046 |
| Nalsian Norte | 0105511047 |
| Nalsian Sur | 0105511048 |
| Pangdel | 0105511049 |
| Pantol | 0105511050 |
| Paragos | 0105511051 |
| Poblacion Sur | 0105511053 |
| Pugo | 0105511054 |
| Reynado | 0105511055 |
| San Gabriel 1st | 0105511056 |
| San Gabriel 2nd | 0105511057 |
| San Vicente | 0105511058 |
| Sancagulis | 0105511059 |
| Sanlibo | 0105511060 |
| Sapang | 0105511061 |
| Tamaro | 0105511062 |
| Tambac | 0105511063 |
| Tampog | 0105511064 |
| Tanolong | 0105511066 |
| Tatarac | 0105511067 |
| Telbang | 0105511068 |
| Tococ East | 0105511069 |
| Tococ West | 0105511070 |
| Warding | 0105511071 |
| Wawa | 0105511072 |
| Zone I | 0105511073 |
| Zone II | 0105511074 |
| Zone III | 0105511075 |
| Zone IV | 0105511076 |
| Zone V | 0105511077 |
| Zone VI | 0105511078 |
| Zone VII | 0105511079 |

## Look up Bayambang with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0105511000") or cities.lookup("0105511000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Bayambang

```python
from barangay import search_fuzzy

for r in search_fuzzy("Bayambang", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
