---
title: "Barangays in Laoang, Northern Samar — PSGC Codes"
description: "Complete list of 56 barangays in Laoang, Northern Samar with their PSGC codes. Lookup, fuzzy search, and Python examples for the Philippine Standard Geographic Code."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# PSGC Barangays in Laoang, Northern Samar

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Place",
  "name": "Laoang, Northern Samar",
  "description": "Municipality in the Philippines with 56 barangays listed under the Philippine Standard Geographic Code (PSGC).",
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "Northern Samar",
    "addressCountry": "PH"
  },
  "containedInPlace": {
    "@type": "AdministrativeArea",
    "name": "Northern Samar"
  }
}
</script>

Laoang is a **municipality** in Northern Samar (Philippines) with
**56 barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of 2026-04-13. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

| Barangay | PSGC Code |
|----------|-----------|
| Abaton | 0804808001 |
| Aguadahan | 0804808002 |
| Aroganga | 0804808003 |
| Atipolo | 0804808004 |
| Bawang | 0804808005 |
| Baybay | 0804808006 |
| Binatiklan | 0804808007 |
| Bobolosan | 0804808008 |
| Bongliw | 0804808009 |
| Burabud | 0804808010 |
| Cabadiangan | 0804808011 |
| Cabagngan | 0804808012 |
| Cabago-an | 0804808013 |
| Cabulaloan | 0804808014 |
| Cagaasan | 0804808015 |
| Cagdara-o | 0804808016 |
| Cahayagan | 0804808017 |
| Calintaan Pob. | 0804808018 |
| Calomotan | 0804808019 |
| Candawid | 0804808020 |
| Cangcahipos | 0804808021 |
| Canyomanao | 0804808022 |
| Catigbian | 0804808023 |
| E. J. Dulay | 0804808026 |
| G. B. Tan | 0804808027 |
| Gibatangan | 0804808028 |
| Guilaoangi | 0804808029 |
| Inamlan | 0804808030 |
| La Perla | 0804808031 |
| Langob | 0804808032 |
| Lawaan | 0804808033 |
| Little Venice | 0804808034 |
| Magsaysay | 0804808035 |
| Marubay | 0804808036 |
| Mualbual | 0804808037 |
| Napotiocan | 0804808038 |
| Oleras | 0804808039 |
| Onay | 0804808040 |
| Palmera | 0804808041 |
| Pangdan | 0804808042 |
| Rawis | 0804808043 |
| Rombang | 0804808044 |
| San Antonio | 0804808045 |
| San Miguel Heights | 0804808046 |
| Sangcol | 0804808048 |
| Sibunot | 0804808049 |
| Simora | 0804808050 |
| Suba | 0804808052 |
| Talisay | 0804808061 |
| Tan-awan | 0804808054 |
| Tarusan | 0804808055 |
| Tinoblan | 0804808056 |
| Tumaguingting | 0804808057 |
| Vigo | 0804808058 |
| Yabyaban | 0804808059 |
| Yapas | 0804808060 |

## Look up Laoang with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("0804808000") or cities.lookup("0804808000")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in Laoang

```python
from barangay import search_fuzzy

for r in search_fuzzy("Laoang", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist (2026-04-13)](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.md) for fuzzy search, validation, and bulk export.
