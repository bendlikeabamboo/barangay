---
title: "Barangays in Gandara, Samar — PSGC Codes"
description: "Complete list of 69 barangays in Gandara, Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Gandara, Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Gandara, Samar",
  "description": "Municipality in the Philippines with 69 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Samar"
  }
}
</script>

Gandara is a **municipality** in Samar (Philippines) with
**69 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Adela Heights | 0806007094 |
| Arong | 0806007095 |
| Balocawe | 0806007002 |
| Bangahon | 0806007093 |
| Beslig | 0806007006 |
| Buao | 0806007010 |
| Bunyagan | 0806007014 |
| Burabod I | 0806007008 |
| Burabod II | 0806007009 |
| Calirocan | 0806007018 |
| Canhumawid | 0806007020 |
| Caparangasan | 0806007023 |
| Caranas | 0806007024 |
| Carmona | 0806007025 |
| Casab-ahan | 0806007026 |
| Casandig | 0806007027 |
| Catorse De Agosto | 0806007096 |
| Caugbusan | 0806007028 |
| Concepcion | 0806007029 |
| Diaz | 0806007097 |
| Dumalo-ong | 0806007031 |
| Elcano | 0806007032 |
| Gerali | 0806007034 |
| Gereganan | 0806007098 |
| Giaboc | 0806007035 |
| Hampton | 0806007039 |
| Hetebac | 0806007099 |
| Himamaloto | 0806007100 |
| Hinayagan | 0806007041 |
| Hinugacan | 0806007042 |
| Hiparayan | 0806007101 |
| Jasminez | 0806007044 |
| Lungib | 0806007048 |
| Mabuhay | 0806007049 |
| Macugo | 0806007050 |
| Malayog | 0806007102 |
| Marcos | 0806007092 |
| Minda | 0806007052 |
| Nacube | 0806007054 |
| Nalihugan | 0806007055 |
| Napalisan | 0806007056 |
| Natimonan | 0806007057 |
| Ngoso | 0806007058 |
| Palambrag | 0806007059 |
| Palanas | 0806007060 |
| Pizarro | 0806007062 |
| Piñaplata | 0806007061 |
| Pologon | 0806007063 |
| Purog | 0806007064 |
| Rawis | 0806007067 |
| Rizal | 0806007068 |
| Samoyao | 0806007070 |
| San Agustin | 0806007071 |
| San Antonio | 0806007072 |
| San Enrique | 0806007073 |
| San Francisco | 0806007074 |
| San Isidro | 0806007076 |
| San Jose | 0806007078 |
| San Miguel | 0806007079 |
| San Pelayo | 0806007080 |
| San Ramon | 0806007081 |
| Santa Elena | 0806007082 |
| Santo Niño | 0806007083 |
| Senibaran | 0806007085 |
| Sidmon | 0806007103 |
| Tagnao | 0806007087 |
| Tambongan | 0806007088 |
| Tawiran | 0806007090 |
| Tigbawon | 0806007091 |

## Look up Gandara with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0806007000") or cities.lookup("0806007000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Gandara

```python
from barangay import search_fuzzy

for r in search_fuzzy("Gandara", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
