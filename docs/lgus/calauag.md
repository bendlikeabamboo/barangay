---
title: "Barangays in Calauag, Quezon — PSGC Codes"
description: "Complete list of 81 barangays in Calauag, Quezon with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Calauag, Quezon

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Calauag, Quezon",
  "description": "Municipality in the Philippines with 81 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Quezon",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Quezon"
  }
}
</script>

Calauag is a **municipality** in Quezon (Philippines) with
**81 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agoho | 0405607001 |
| Anahawan | 0405607002 |
| Anas | 0405607003 |
| Apad Lutao | 0405607004 |
| Apad Quezon | 0405607005 |
| Apad Taisan | 0405607006 |
| Atulayan | 0405607007 |
| Baclaran | 0405607008 |
| Bagong Silang | 0405607009 |
| Balibago | 0405607010 |
| Bangkuruhan | 0405607011 |
| Bantolinao | 0405607012 |
| Barangay I | 0405607013 |
| Barangay II | 0405607014 |
| Barangay III | 0405607015 |
| Barangay IV | 0405607016 |
| Barangay V | 0405607017 |
| Bigaan | 0405607018 |
| Binutas | 0405607019 |
| Biyan | 0405607020 |
| Bukal | 0405607021 |
| Buli | 0405607022 |
| Dapdap | 0405607023 |
| Dominlog | 0405607024 |
| Doña Aurora | 0405607026 |
| Guinosayan | 0405607027 |
| Ipil | 0405607029 |
| Kalibo | 0405607032 |
| Kapaluhan | 0405607033 |
| Katangtang | 0405607034 |
| Kigtan | 0405607035 |
| Kinalin Ibaba | 0405607037 |
| Kinalin Ilaya | 0405607038 |
| Kinamaligan | 0405607036 |
| Kumaludkud | 0405607039 |
| Kunalum | 0405607040 |
| Kuyaoyao | 0405607041 |
| Lagay | 0405607042 |
| Lainglaingan | 0405607043 |
| Lungib | 0405607044 |
| Mabini | 0405607045 |
| Madlangdungan | 0405607046 |
| Maglipad | 0405607047 |
| Maligaya | 0405607048 |
| Mambaling | 0405607049 |
| Manhulugin | 0405607050 |
| Marilag | 0405607051 |
| Mulay | 0405607053 |
| Pandanan | 0405607054 |
| Pansol | 0405607055 |
| Patihan | 0405607058 |
| Pinagbayanan | 0405607059 |
| Pinagkamaligan | 0405607060 |
| Pinagsakayan | 0405607061 |
| Pinagtalleran | 0405607062 |
| Rizal Ibaba | 0405607064 |
| Rizal Ilaya | 0405607065 |
| Sabang I | 0405607066 |
| Sabang II | 0405607067 |
| Salvacion | 0405607068 |
| San Quintin | 0405607069 |
| San Roque Ibaba | 0405607070 |
| San Roque Ilaya | 0405607071 |
| Santa Cecilia | 0405607072 |
| Santa Maria | 0405607073 |
| Santa Milagrosa | 0405607074 |
| Santa Rosa | 0405607075 |
| Santo Angel | 0405607076 |
| Santo Domingo | 0405607077 |
| Sinag | 0405607078 |
| Sumilang | 0405607079 |
| Sumulong | 0405607080 |
| Tabansak | 0405607081 |
| Talingting | 0405607083 |
| Tamis | 0405607084 |
| Tikiwan | 0405607085 |
| Tiniguiban | 0405607086 |
| Villa Magsino | 0405607087 |
| Villa San Isidro | 0405607088 |
| Viñas | 0405607089 |
| Yaganak | 0405607090 |

## Look up Calauag with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0405607000") or cities.lookup("0405607000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Calauag

```python
from barangay import search_fuzzy

for r in search_fuzzy("Calauag", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
