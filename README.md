# barangay
[<p style="text-align:center;">![PyPI version](https://img.shields.io/pypi/v/barangay.svg)](https://pypi.org/project/barangay/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI Downloads](https://static.pepy.tech/badge/barangay)](https://pepy.tech/projects/barangay) [![Release](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml/badge.svg)](https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml)<p>
<p>

Philippines Standard Geographic Code (PSGC) 2025 Python masterlist data package for
Philippine regions, provinces, cities, municipalities, and barangay. Available in JSON,
YAML, and Python dictionary formats and with fuzzy search. Latest and updated as of July
2025.

__SOURCE FILE__: [2025-07-08 PSGC Release](https://psa.gov.ph/classification/psgc/node/1684077694) <br>
__PyPI__: https://pypi.org/project/barangay/ <br>
__GitHub__: [bendlikeabamboo/barangay](https://github.com/bendlikeabamboo/barangay) <br>
__Installation__: `pip install barangay`

## Features

### Fuzzy Search
- Performant, customizable, and easy to use fuzzy search function
- Works for unstandardized strings like addresses and text entries

### Data dictionaries
- Comprehensive, up-to-date list of Philippine barangays and their administrative
  hierarchy based on Philippine Standard Geographic Code ([PSGC](https://psa.gov.ph/classification/psgc))
- Data also available in both JSON and YAML formats under [`data/`](https://github.com/bendlikeabamboo/barangay/tree/main/data/)
- Available in different dictionary data models
  - Direct Nested Hierarchical Model
  - Metadata-rich Recursive Hierarchical Model
  - Metadata-rich Flat Model
- Easy integration with Python projects

## Installation

```bash
pip install barangay
```

## Usage
Sample usage in [`notebooks/sample_usage.ipynb`](https://github.com/bendlikeabamboo/barangay/blob/main/notebooks/sample_usage.ipynb)

### Fuzzy Search

Simple string search

#### Example

```python
from barangay import search

search("Tongmageng, Tawi-Tawi")
```

Custom search also possible using the following configuration: 
- match_hooks (argument: `match_hooks`, default: all matchers)
  - allowed matchers:
    - barangay (required)
    - municipality
    - province
  - any combination of allowed matchers
- threshold (argument: `threshold`, default: 60.0)
  - 0.00 to 100.00
  - 100.00 means strict match
- number of matches returned (argument: `n`)
  
#### Example
```python
from barangay import search

search(
  "Tongmagen, Tawi-Tawi",
  n = 4,
  match_hooks=["municipality","barangay"],
  threshold=70.0,
)
```

### Data Dictionaries
#### barangay.BARANGAY: Direct Nested Hierarchical Model
Traversing `barangay.BARANGAY` is straightforward since it’s a purely nested dictionary
composed of names, with no additional metadata.

```python
from barangay import BARANGAY
  
# Example lookup process and dictionary traversal
all_regions = BARANGAY.keys()

# Looking for NCR Cities & Municipalities
ncr_cities_and_municipalities =  list(BARANGAY["National Capital Region (NCR)"].keys())
print(f"NCR Cities & Municipalities: {ncr_cities_and_municipalities}")

# Looking for Municipalities of Cities of Manila
municipalities_of_manila = list(BARANGAY["National Capital Region (NCR)"][
  "City of Manila"
].keys())
print(f"Municipalities of Manila: {municipalities_of_manila}")

# Looking for Barangays in Binondo
brgy_of_binondo = BARANGAY["National Capital Region (NCR)"]["City of Manila"][
  "Binondo"
]
print(f"Brgys of Binondo: {brgy_of_binondo}")
```

The provided code demonstrates a simple traversal of the `BARANGAY` nested dictionary.
This dictionary, however, has only simple parent-child structure that doesn't fully
represent the complex geographical hierarchy of the Philippines. For example, some
municipalities like __Pateros__ are directly under a region, and certain highly
urbanized cities (__HUCs__) such as __Tacloban City__ and __Davao City__ are not part of
a province.

This simplified structure can make it challenging to implement accurate address
selectors with labeled forms where distinctions between municipalities and cities and
provinces are important. To address this, I developed `barangay.BARANGAY_EXTENDED`, a
more complex fractal dictionary that accurately mirrors the intricate geographical
divisions of the Philippines.

#### barangay.BARANGAY_EXTENDED: Metadata-rich Recursive Hierarchical Model
Traversing `barangay.BARANGAY_EXTENDED` is slightly more involved, as each location
includes rich metadata stored in dictionary fields. Instead of simple key-value pairs,
traversal involves navigating lists of dictionaries—adding a bit of complexity, but also
unlocking far greater flexibility and precision. This structure enables more accurate
modeling of the Philippines' administrative divisions, making it ideal for applications
that require detailed address handling or contextual geographic data.

```python
from barangay import BARANGAY_EXTENDED
from pprint import pprint

# Listing all component locations under Philippines
philippine_components = [item["name"] for item in BARANGAY_EXTENDED["components"]]
print("philippine_components: ")
pprint(philippine_components)
print("\n\n")

# retrieving National Capital Region (NCR) location data
ncr = [
    item
    for item in BARANGAY_EXTENDED["components"]
    if item["name"] == "National Capital Region (NCR)"
][0]

# Listing all component locations under NCR. In the output, notice tha Pateros is a
# municipality directly under a region, which is unusual but possible, nonetheless.
ncr_components = [(item["name"], item["type"]) for item in ncr["components"]]
print("ncr_components")
pprint(ncr_components)
print("\n\n")

# Retrieving City of Manila location data
city_of_manila = [
    item for item in ncr["components"] if item["name"] == "City of Manila"
][0]

# Listing all component locations under City of Manila
city_of_manila_components = [
    (item["name"], item["type"]) for item in city_of_manila["components"]
]
print("city_of_manila_components")
pprint(city_of_manila_components)
print("\n\n")

# Retrieving Sta Ana location data
sta_ana = [
    item for item in city_of_manila["components"] if item["name"] == "Santa Ana"
][0]

# Listing all component locations under Santa Ana (which are now the Barangay)
santa_ana_components = [
    (item["name"], item["type"]) for item in sta_ana["components"]
]
print("santa_ana_components")
pprint(santa_ana_components)
print("\n\n")
```

#### barangay.BARANGAY_FLAT: Metadata-rich Flat Model

The barangay.BARANGAY_FLAT structure offers a fully flattened list of all Philippine
administrative units—regions, provinces, cities, municipalities, and barangays—with rich
metadata for each entry. This format is ideal for search, filtering, and integration
with tabular data workflows such as pandas DataFrames or database imports.

```python
from barangay import BARANGAY_FLAT


# Looking for Brgy. Marayos in Mindoro
brgy_marayos = [loc for loc in BARANGAY_FLAT if loc["name"]=="Marayos"]
print(brgy_marayos)

# From here we can now trace its hierarchy by following parent_psgc_id
brgy_marayos_parent = [loc for loc in BARANGAY_FLAT if loc["psgc_id"]=="1705209000"]
print(brgy_marayos_parent)

pinamalayan_parent = [loc for loc in BARANGAY_FLAT if loc["psgc_id"]=="1705200000"]
print(pinamalayan_parent)

oriental_mindoro_parent = [loc for loc in BARANGAY_FLAT if loc["psgc_id"]=="1700000000"]
print(oriental_mindoro_parent)
```
