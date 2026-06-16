---
title: "Barangays in City of San Carlos, Pangasinan — PSGC Codes"
description: "Complete list of 86 barangays in City of San Carlos, Pangasinan with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of San Carlos, Pangasinan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of San Carlos, Pangasinan",
  "description": "City in the Philippines with 86 barangays listed under the Philippine Standard Geographic Code (PSGC).",
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

City of San Carlos is a **city** in Pangasinan (Philippines) with
**86 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abanon | 0105532001 |
| Agdao | 0105532002 |
| Anando | 0105532003 |
| Ano | 0105532004 |
| Antipangol | 0105532005 |
| Aponit | 0105532006 |
| Bacnar | 0105532007 |
| Balaya | 0105532008 |
| Balayong | 0105532009 |
| Baldog | 0105532010 |
| Balite Sur | 0105532011 |
| Balococ | 0105532012 |
| Bani | 0105532013 |
| Bega | 0105532014 |
| Bocboc | 0105532015 |
| Bogaoan | 0105532017 |
| Bolingit | 0105532018 |
| Bolosan | 0105532019 |
| Bonifacio | 0105532020 |
| Buenglat | 0105532021 |
| Bugallon-Posadas Street | 0105532016 |
| Burgos Padlan | 0105532022 |
| Cacaritan | 0105532023 |
| Caingal | 0105532024 |
| Calobaoan | 0105532025 |
| Calomboyan | 0105532026 |
| Caoayan-Kiling | 0105532028 |
| Capataan | 0105532027 |
| Cobol | 0105532029 |
| Coliling | 0105532030 |
| Cruz | 0105532031 |
| Doyong | 0105532032 |
| Gamata | 0105532035 |
| Guelew | 0105532036 |
| Ilang | 0105532037 |
| Inerangan | 0105532038 |
| Isla | 0105532039 |
| Libas | 0105532040 |
| Lilimasan | 0105532041 |
| Longos | 0105532043 |
| Lucban | 0105532044 |
| M. Soriano | 0105532091 |
| Mabalbalino | 0105532045 |
| Mabini | 0105532046 |
| Magtaking | 0105532047 |
| Malacañang | 0105532048 |
| Maliwara | 0105532050 |
| Mamarlao | 0105532051 |
| Manzon | 0105532052 |
| Matagdem | 0105532053 |
| Mestizo Norte | 0105532054 |
| Naguilayan | 0105532055 |
| Nilentap | 0105532056 |
| PNR Station Site | 0105532081 |
| Padilla-Gomez | 0105532057 |
| Pagal | 0105532058 |
| Paitan-Panoypoy | 0105532066 |
| Palaming | 0105532060 |
| Palaris | 0105532061 |
| Palospos | 0105532062 |
| Pangalangan | 0105532063 |
| Pangoloan | 0105532064 |
| Pangpang | 0105532065 |
| Parayao | 0105532067 |
| Payapa | 0105532069 |
| Payar | 0105532070 |
| Perez Boulevard | 0105532071 |
| Polo | 0105532072 |
| Quezon Boulevard | 0105532073 |
| Quintong | 0105532074 |
| Rizal | 0105532075 |
| Roxas Boulevard | 0105532076 |
| Salinap | 0105532077 |
| San Juan | 0105532078 |
| San Pedro-Taloy | 0105532079 |
| Sapinit | 0105532080 |
| Supo | 0105532082 |
| Talang | 0105532083 |
| Tamayo | 0105532084 |
| Tandang Sora | 0105532092 |
| Tandoc | 0105532085 |
| Tarece | 0105532086 |
| Tarectec | 0105532087 |
| Tayambani | 0105532088 |
| Tebag | 0105532089 |
| Turac | 0105532090 |

## Look up San Carlos with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0105532000") or cities.lookup("0105532000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in San Carlos

```python
from barangay import search_fuzzy

for r in search_fuzzy("San Carlos", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
