---
title: "Barangays in Leon, Iloilo — PSGC Codes"
description: "Complete list of 85 barangays in Leon, Iloilo with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Leon, Iloilo

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Leon, Iloilo",
  "description": "Municipality in the Philippines with 85 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Iloilo",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Iloilo"
  }
}
</script>

Leon is a **municipality** in Iloilo (Philippines) with
**85 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Agboy Norte | 0603028001 |
| Agboy Sur | 0603028002 |
| Agta | 0603028003 |
| Ambulong | 0603028004 |
| Anonang | 0603028005 |
| Apian | 0603028006 |
| Avanzada | 0603028007 |
| Awis | 0603028008 |
| Ayabang | 0603028009 |
| Ayubo | 0603028010 |
| Bacolod | 0603028011 |
| Baje | 0603028012 |
| Banagan | 0603028013 |
| Barangbang | 0603028014 |
| Barasan | 0603028015 |
| Bayag Norte | 0603028016 |
| Bayag Sur | 0603028017 |
| Binolbog | 0603028018 |
| Biri Norte | 0603028019 |
| Biri Sur | 0603028020 |
| Bobon | 0603028021 |
| Bucari | 0603028022 |
| Buenavista | 0603028023 |
| Buga | 0603028024 |
| Bulad | 0603028025 |
| Bulwang | 0603028026 |
| Cabolo-an | 0603028027 |
| Cabunga-an | 0603028028 |
| Cabutongan | 0603028029 |
| Cagay | 0603028030 |
| Camandag | 0603028031 |
| Camando | 0603028032 |
| Cananaman | 0603028033 |
| Capt. Fernando | 0603028034 |
| Carara-an | 0603028035 |
| Carolina | 0603028036 |
| Cawilihan | 0603028037 |
| Coyugan Norte | 0603028038 |
| Coyugan Sur | 0603028039 |
| Danao | 0603028040 |
| Dorog | 0603028041 |
| Dusacan | 0603028042 |
| Gines | 0603028043 |
| Gumboc | 0603028044 |
| Igcadios | 0603028045 |
| Ingay | 0603028046 |
| Isian Norte | 0603028047 |
| Isian Victoria | 0603028048 |
| Jamog Gines | 0603028049 |
| Lampaya | 0603028054 |
| Lanag | 0603028050 |
| Lang-og | 0603028051 |
| Ligtos | 0603028052 |
| Lonoc | 0603028053 |
| Magcapay | 0603028055 |
| Maliao | 0603028056 |
| Malublub | 0603028057 |
| Manampunay | 0603028058 |
| Marirong | 0603028059 |
| Mina | 0603028060 |
| Mocol | 0603028061 |
| Nagbangi | 0603028062 |
| Nalbang | 0603028063 |
| Odong-odong | 0603028064 |
| Oluangan | 0603028065 |
| Omambong | 0603028066 |
| Paga | 0603028072 |
| Pandan | 0603028068 |
| Panginman | 0603028069 |
| Paoy | 0603028067 |
| Pepe | 0603028070 |
| Poblacion | 0603028071 |
| Salngan | 0603028073 |
| Samlague | 0603028074 |
| Siol Norte | 0603028075 |
| Siol Sur | 0603028076 |
| Tacuyong Norte | 0603028077 |
| Tacuyong Sur | 0603028078 |
| Tagsing | 0603028079 |
| Talacuan | 0603028080 |
| Ticuan | 0603028081 |
| Tina-an Norte | 0603028082 |
| Tina-an Sur | 0603028083 |
| Tu-og | 0603028085 |
| Tunguan | 0603028084 |

## Look up Leon with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0603028000") or cities.lookup("0603028000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Leon

```python
from barangay import search_fuzzy

for r in search_fuzzy("Leon", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
