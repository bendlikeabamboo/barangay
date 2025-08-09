# barangay

A Python package providing a nested dictionary of all Philippine barangays,
cities/municipalities, provinces, and regions, updated as of 2025. This project is
intended for geographic data analysis, lookup, and mapping applications.

## Features

- Comprehensive, up-to-date list of Philippine barangays and their administrative
  hierarchy.
- Data available in both JSON and YAML formats.
- Easy integration with Python projects.

## Installation

Clone the repository and install the package using [Poetry](https://python-poetry.org/):

```sh
git clone https://github.com/yourusername/barangay.git
cd barangay
poetry install
```

## Usage
```python
from barangay import BARANGAY

brgys_of_binondo = BARANGAY["National Capital Region (NCR)"]["City of Manila"][
    "Binondo"
]
print(brgys_of_binondo)
```