# barangay

Python Package for Philippine regions, provinces, municipalities, cities, and barangays. Based on Philippine Standard Geographic Code (PSGC) official masterlist.

<div style="display: flex; flex-direction: row; align-items: center; gap: 8px;">
<a href="https://pypi.org/project/barangay/">
    <img src="https://img.shields.io/pypi/v/barangay.svg" alt="PyPI version">
</a>
<a href="https://pepy.tech/projects/barangay">
    <img src="https://static.pepy.tech/badge/barangay" alt="PyPI Downloads">
</a>
<a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</a>
<a href="https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml">
    <img src="https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml/badge.svg" alt="Release Badge">
</a>
</div>

## Features

- **Bundled PSGC Dataset**: Native access to PSGC data, no database or API calls needed
- **Historical PSGC Data**: On-demand access to previous PSGC releases by date
- **Fuzzy Search**: Fast, customizable fuzzy matching
- **Multiple Data Models**: Basic (nested), Extended (recursive), and Flat (list)

## Installation

```bash
pip install barangay
```

## Quick Start

### Basic Search

```python
from barangay import search

results = search("Tongmageng, Tawi-Tawi")
top_result = results[0]
print(f"Barangay Name: {top_result["barangay"]}")
print(f"PSGC ID: {top_result["psgc_id"]}")
```

Ouput:
```txt
Barangay Name: Tongmageng
PSGC ID: 1907005010
```
### Access Data Directly

```python
from barangay import barangay

ncr: dict = barangay["National Capital Region (NCR)"]
print(f"NCR Components: \n\t{'\n\t'.join(list(ncr.keys()))}")

city_of_manila_municipalities: dict = ncr["City of Manila"]
print(
    "City of Manila Municipalities: \n\t"
    f"{'\n\t'.join(list(city_of_manila_municipalities.keys()))}"
)

binondo_barangays: list = city_of_manila_municipalities["Binondo"]
print(f"Binondo Barangays: \n\t{'\n\t'.join(binondo_barangays)}")
```

Output:
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

### CLI Usage

#### Search
```sh
# Search
barangay search "Tongmageng, Tawi-Tawi"
```
Output:

| Barangay | Municipality/City | Province/HUC | PSGC ID | Score |
|----------|-------------------|--------------|---------|-------|
| Tongmageng | Sitangkai | Tawi-Tawi | 1907005010 | 100.0 |
| Tonggosong | Simunul | Tawi-Tawi | 1907004005 | 84.2 |
| Tongbangkaw | Tandubas | Tawi-Tawi | 1907007042 | 82.1 |
| Tongusong | Sitangkai | Tawi-Tawi | 1907005012 | 81.1 |
| Tongehat | Sibutu | Tawi-Tawi | 1907011014 | 77.8 |


#### Export data
```sh
barangay export --model flat --format json --output data.json
```
#### Show info
```sh
barangay info version
```

Ouput:
```txt
Current version: 2026-01-13
Available dates: 2026-01-13, 2025-08-29, 2025-10-13, 2025-07-08
```

```sh
barangay info stats
```
Output:

| Model | Barangay Count |
|-------|----------------|
| Basic (nested) | 42011 |
| Flat (list) | 42011 |
| Extended (recursive) | 42011 |

## Data Version

Current data version: [**2026-01-13** (January 13 2026 PSGC masterlist)](https://psa.gov.ph/classification/psgc/node/1684082306)

## Documentation

- [API Reference](api.md)
- [CLI Reference](cli.md)
- [Configuration](configuration.md)
