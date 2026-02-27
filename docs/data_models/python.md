# Python Data Models

This package provides three data models for accessing Philippine barangay information, each optimized for different use cases.

## BARANGAY

Dictionary structure has three paths:

- region -> province -> municipality -> barangay
- region -> highly urbanized city (HUC) -> barangay
- region -> municipality -> barangay

The basic `BARANGAY` data model follows the `parent -> child` relationship directly with the terminal  nodes as list of strings.

```python
from barangay import BARANGAY

ncr: dict = BARANGAY["National Capital Region (NCR)"]
print(f"NCR Components: \n\t{'\n\t'.join(list(ncr.keys()))}")

city_of_manila_municipalities: dict = ncr["City of Manila"]
print(
    "City of Manila Municipalities: \n\t"
    f"{'\n\t'.join(list(city_of_manila_municipalities.keys()))}"
)

binondo_barangays: list = city_of_manila_municipalities["Binondo"]
print(f"Binondo Barangays: \n\t{'\n\t'.join(binondo_barangays)}")
```

```txt
NCR Components: 
	City of Manila
	City of Caloocan
	City of Las Piñas
	City of Makati
	City of Malabon
	City of Mandaluyong
	City of Marikina
	City of Muntinlupa
	City of Navotas
	City of Parañaque
	City of Pasig
	City of San Juan
	City of Taguig
	City of Valenzuela
	Pasay City
	Quezon City
	Pateros
City of Manila Municipalities: 
	Binondo
	Ermita
	Intramuros
	Malate
	Paco
	Pandacan
	Port Area
	Quiapo
	Sampaloc
	San Miguel
	San Nicolas
	Santa Ana
	Santa Cruz
	Tondo I/II
Binondo Barangays: 
	Barangay 291
	Barangay 290
	Barangay 293
	Barangay 294
	Barangay 292
	Barangay 289
	Barangay 296
	Barangay 287
	Barangay 288
	Barangay 295
```

## BARANGAY_EXTENDED

`BARANGAY_EXTENDED` also follows the relationship directly but with a recursive `parent -> component` structure, allowing a richer metadata (name, code, level).

To demonstrate, let's try traversing the structure.
```python
from barangay import BARANGAY_EXTENDED
import random
```

### Region Hierarchy Tree (Philippines → region)

Let's first examine the data structure:
```python
regions = [x for x in BARANGAY_EXTENDED["components"]]
```
```python
[{'name': 'Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)',
  'type': 'region',
  'psgc_id': '1900000000',
  'parent_psgc_id': '0000000000',
  'nicknames': None,
  'components': [{'name': 'Basilan',
                  'type': 'province',
                  'psgc_id': '1900700000',
                  'parent_psgc_id': '1900000000',
                  'nicknames': None,
                  'components': [{'name': 'City of Lamitan',
...
```

Creating container for the names of entities in the children components for easier browsing.

```python
region_names = [x["name"] for x in BARANGAY_EXTENDED["components"]]
```
```python
['Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)',
 'Cordillera Administrative Region (CAR)',
 'MIMAROPA Region',
 'National Capital Region (NCR)',
 'Negros Island Region (NIR)',
 'Region I (Ilocos Region)',
 'Region II (Cagayan Valley)',
 'Region III (Central Luzon)',
...
```

Then let's print 3 random components from the pool.
```python
sampled_regions = random.sample(region_names, k=3)
print(f"Sample regions in the Philippines: \n\t{'\n\t'.join(sampled_regions)}")
```
```
Sample regions in the Philippines: 
	Region XI (Davao Region)
	Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)
	MIMAROPA Region
```

### Repeating the Process (Region → province/HUC)

Let's now repeat the process for subsequent levels in the hierarchy by creating using Davao Region as reference.

```python
davao_region = [x for x in regions if x["name"] == "Region XI (Davao Region)"][0]
```
```python
{'name': 'Region XI (Davao Region)',
 'type': 'region',
 'psgc_id': '1100000000',
 'parent_psgc_id': '0000000000',
 'nicknames': None,
 'components': [{'name': 'Davao del Norte',
   'type': 'province',
   'psgc_id': '1102300000',
   'parent_psgc_id': '1100000000',
   'nicknames': None,
   'components': [{'name': 'Asuncion',
...
```

and then performing the steps done above:

```python
davao_provinces_and_hucs = [x for x in davao_region["components"]]
davao_provinces_and_hucs_names = [x["name"] for x in davao_region["components"]]
print(
    "Sample provinces and HUCs in Davao Region: "
    f"{random.sample(davao_provinces_and_hucs_names, k=3)}"
)
```
```txt
Sample provinces and HUCs in Davao Region: ['Davao Occidental', 'Davao del Norte', 'Davao de Oro']
```

### HUC → barangay
```python
# Get HUC hierarchical tree
print("\nSample hierarchy for highly urbanized cities (HUCs):")
davao_city = [x for x in davao_provinces_and_hucs if x["name"] == "City of Davao"][0]
# Get barangays in a city
davao_city_barangays = [x for x in davao_city["components"]]
davao_city_barangay_names = [x["name"] for x in davao_city["components"]]
print(f"Sample Davao City barangays: {random.sample(davao_city_barangay_names, k=3)}")
```

```txt
Sample hierarchy for highly urbanized cities (HUCs):
Sample Davao City barangays: ['Barangay 26-C', 'Manambulan', 'Tagluno']
```

### province → municipality → barangay

```python
# Get provincial hierarchical tree
print("\nSample for provinces:")
davao_oriental_province = [
    x for x in davao_provinces_and_hucs if x["name"] == "Davao Occidental"
][0]
davao_oriental_municipalities = [x for x in davao_oriental_province["components"]]
davao_oriental_municipalities_names = [
    x["name"] for x in davao_oriental_province["components"]
]
print(
    f"Sample Davao Oriental municipalities: {random.sample(davao_oriental_municipalities_names, k=3)}"
)

sarangani_municipality = [
    x for x in davao_oriental_municipalities if x["name"] == "Sarangani"
][0]
sarangani_barangays = [x for x in sarangani_municipality["components"]]
sarangani_barangay_names = [x["name"] for x in sarangani_municipality["components"]]
print(f"Sample Sarangani barangays: {random.sample(sarangani_barangay_names, k=3)}")
```
```
Sample for provinces:
Sample Davao Oriental municipalities: ['Don Marcelino', 'Santa Maria', 'Malita']
Sample Sarangani barangays: ['Patuco', 'Tinina', 'Tucal']
```

## BARANGAY_FLAT

Flat list with parent references. Best for search, filtering, and DataFrame operations.

```python
from barangay import BARANGAY_FLAT

# Filter by type
barangays = [item for item in BARANGAY_FLAT if item["type"] == "barangay"]
print(f"Total barangays: {len(barangays)}")

# Find by PSGC ID
target = next((b for b in barangays if b["psgc_id"] == "1900702001"), None)
print(f"Found: {target['name']} (PSGC: {target['psgc_id']})")
```
