---
title: "Barangays in City of Cabanatuan, Nueva Ecija — PSGC Codes"
description: "Complete list of 89 barangays in City of Cabanatuan, Nueva Ecija with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in City of Cabanatuan, Nueva Ecija

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "City of Cabanatuan, Nueva Ecija",
  "description": "City in the Philippines with 89 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Nueva Ecija",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Nueva Ecija"
  }
}
</script>

City of Cabanatuan is a **city** in Nueva Ecija (Philippines) with
**89 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Aduas Centro | 0304903002 |
| Aduas Norte | 0304903090 |
| Aduas Sur | 0304903091 |
| Bagong Buhay | 0304903005 |
| Bagong Sikat | 0304903003 |
| Bakero | 0304903006 |
| Bakod Bayan | 0304903007 |
| Balite | 0304903008 |
| Bangad | 0304903009 |
| Bantug Bulalo | 0304903010 |
| Bantug Norte | 0304903011 |
| Barlis | 0304903012 |
| Barrera District | 0304903013 |
| Bernardo District | 0304903015 |
| Bitas | 0304903016 |
| Bonifacio District | 0304903017 |
| Buliran | 0304903018 |
| Caalibangbangan | 0304903019 |
| Cabu | 0304903020 |
| Calawagan | 0304903040 |
| Campo Tinio | 0304903022 |
| Caridad | 0304903096 |
| Caudillo | 0304903026 |
| Cinco-Cinco | 0304903024 |
| City Supermarket | 0304903025 |
| Communal | 0304903027 |
| Cruz Roja | 0304903028 |
| Daang Sarile | 0304903029 |
| Dalampang | 0304903030 |
| Dicarma | 0304903031 |
| Dimasalang | 0304903032 |
| Dionisio S. Garcia | 0304903033 |
| Fatima | 0304903035 |
| General Luna | 0304903036 |
| Hermogenes C. Concepcion, Sr. | 0304903092 |
| Ibabao Bana | 0304903037 |
| Imelda District | 0304903038 |
| Isla | 0304903039 |
| Kalikid Norte | 0304903041 |
| Kalikid Sur | 0304903042 |
| Kapitan Pepe | 0304903023 |
| Lagare | 0304903043 |
| Lourdes | 0304903051 |
| M. S. Garcia | 0304903044 |
| Mabini Extension | 0304903046 |
| Mabini Homesite | 0304903047 |
| Macatbong | 0304903048 |
| Magsaysay District | 0304903049 |
| Magsaysay South | 0304903097 |
| Maria Theresa | 0304903098 |
| Matadero | 0304903050 |
| Mayapyap Norte | 0304903052 |
| Mayapyap Sur | 0304903053 |
| Melojavilla | 0304903054 |
| Nabao | 0304903087 |
| Obrero | 0304903055 |
| Padre Burgos | 0304903088 |
| Padre Crisostomo | 0304903056 |
| Pagas | 0304903057 |
| Palagay | 0304903058 |
| Pamaldan | 0304903059 |
| Pangatian | 0304903060 |
| Patalac | 0304903061 |
| Polilio | 0304903063 |
| Pula | 0304903064 |
| Quezon District | 0304903065 |
| Rizdelis | 0304903066 |
| Samon | 0304903067 |
| San Isidro | 0304903068 |
| San Josef Norte | 0304903071 |
| San Josef Sur | 0304903072 |
| San Juan Pob. | 0304903073 |
| San Roque Norte | 0304903074 |
| San Roque Sur | 0304903075 |
| Sanbermicristi | 0304903076 |
| Sangitan | 0304903077 |
| Sangitan East | 0304903099 |
| Santa Arcadia | 0304903078 |
| Santo Niño | 0304903100 |
| Sapang | 0304903093 |
| Sumacab Este | 0304903094 |
| Sumacab Norte | 0304903079 |
| Sumacab South | 0304903095 |
| Talipapa | 0304903089 |
| Valdefuente | 0304903082 |
| Valle Cruz | 0304903083 |
| Vijandre District | 0304903084 |
| Villa Ofelia-Caridad | 0304903085 |
| Zulueta District | 0304903086 |

## Look up Cabanatuan with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0304903000") or cities.lookup("0304903000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Cabanatuan

```python
from barangay import search_fuzzy

for r in search_fuzzy("Cabanatuan", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
