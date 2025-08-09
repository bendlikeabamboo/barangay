# barangay

A Python package providing a nested dictionary of all Philippine barangays,
cities/municipalities, provinces, and regions, updated as of 2025. This project is
intended for geographic data analysis, lookup, and mapping applications.

## Features

- Comprehensive, up-to-date list of Philippine barangays and their administrative
  hierarchy.
- Data available in both JSON and YAML formats.
- Easy integration with Python projects.

## Project Structure

- **barangay/**: Main package containing the data and access logic.
- **notebooks/parsing_process.ipynb**: Jupyter notebook for parsing and generating the
  data files.
- **resources/psgc_2025-08-07.csv**: Source data from the Philippine Statistics
  Authority.

## Installation

Clone the repository and install the package using [Poetry](https://python-poetry.org/):

```sh
git clone https://github.com/yourusername/barangay.git
cd barangay
poetry install
```

from barangay import barangay_dict  # Example: actual symbol may vary

# Access a specific barangay
region = "Negros Island Region (NIR)"
city = "City of Bacolod"
barangay = "Barangay 38"

print(barangay_dict[region][city][barangay])

import json
import yaml

with open("barangay/barangay.json", encoding="utf8") as f:
    data = json.load(f)

with open("barangay/barangay.yaml", encoding="utf8") as f:
    data = yaml.safe_load(f)