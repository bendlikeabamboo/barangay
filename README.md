# barangay
[![PyPI version](https://img.shields.io/pypi/v/barangay.svg)](https://pypi.org/project/barangay/)

A Python package providing a nested dictionary of all Philippine barangays,
cities/municipalities, provinces, and regions. This project is
intended for geographic data analysis, lookup, and mapping applications.

__UPDATED AS OF__: [July 8, 2025 PSGC Release](https://psa.gov.ph/classification/psgc/node/1684077694)

## Features

- Comprehensive, up-to-date list of Philippine barangays and their administrative
  hierarchy based on Philippine Standard Geographic Code ([PSGC](https://psa.gov.ph/classification/psgc))
- Data also available in both JSON and YAML formats under `barangay/`
- Easy integration with Python projects.

## Installation

```bash
pip install barangay
```

## Usage
```python
from barangay import BARANGAY

# Lookup of all barangays with region, province/huc, and municipality/city provided
brgys_of_binondo = BARANGAY["National Capital Region (NCR)"]["City of Manila"][
    "Binondo"
]
print(brgys_of_binondo)
```
