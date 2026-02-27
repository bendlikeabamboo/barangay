# API Reference

## Main Search Function

### `search()`

Search for barangays using fuzzy string matching.

```python
from barangay import search

results = search("Tongmageng, Tawi-Tawi")
```

**Parameters:**

- `search_string` (str): The string to search for
- `match_hooks` (List[str]): Administrative levels to match against. Valid options: `"province"`, `"municipality"`, `"barangay"`. Default: all three
- `threshold` (float): Minimum similarity score (0-100). Default: 60.0
- `n` (int): Maximum number of results. Default: 5
- `search_sanitizer` (Callable): Function to sanitize search string
- `fuzz_base` (FuzzBase | None): Pre-computed fuzzy matching instance for performance
- `as_of` (str | None): Historical date (YYYY-MM-DD) or None for latest

**Returns:** List[dict] with matching results

**Example:**

```python
results = search(
    "Tongmagen, Tawi-Tawi",
    n=4,
    match_hooks=["municipality", "barangay"],
    threshold=70.0,
    as_of="2025-07-08"
)

for result in results:
    print(f"{result['barangay']} (score: {result['max_score']})")
```

## Data Access

### Direct Data Access

```python
from barangay import barangay, barangay_extended, barangay_flat

# Access nested data
ncr_cities = list(barangay["National Capital Region (NCR)"].keys())
manila_brgys = barangay["National Capital Region (NCR)"]["City of Manila"]

# Access flat data
brgy = [loc for loc in barangay_flat if loc["name"] == "Marayos"][0]
```

### DataManager

Manage data loading, caching, and downloading.

```python
from barangay.data_manager import DataManager

dm = DataManager()
data = dm.get_data(as_of="2025-07-08", data_type="basic")
```

**Parameters:**

- `as_of` (str | None): Historical date (YYYY-MM-DD) or None for latest
- `data_type` (str): Data model - `"basic"`, `"flat"`, or `"extended"`

## Fuzzy Matching

### `create_fuzz_base()`

Factory function to create FuzzBase instances for performance optimization.

```python
from barangay import create_fuzz_base, search

fuzz_base = create_fuzz_base(as_of="2025-08-29")
results = search("Tongmageng", fuzz_base=fuzz_base)
```

**Parameters:**

- `as_of` (str | None): Historical date (YYYY-MM-DD) or None for latest

**Returns:** FuzzBase instance

### FuzzBase

Class for fuzzy matching operations with pre-computed matching functions.

## Utilities

### `sanitize_input()`

Utility function for string sanitization.

```python
from barangay import sanitize_input

cleaned = sanitize_input("City of San Jose", exclude=["city of "])
```

### `resolve_date()`

Resolve approximate dates to closest available dataset.

```python
from barangay import resolve_date

date = resolve_date("2025-07-01")
```

### `get_available_dates()`

Get list of available historical dates.

```python
from barangay import get_available_dates

dates = get_available_dates()
print(dates)
# ['2025-07-08', '2025-08-29', '2025-10-13']
```

## Configuration

### `resolve_as_of()`

Resolve as_of date from multiple layers with priority.

```python
from barangay import resolve_as_of

date = resolve_as_of(as_of_param="2025-08-29")
```

**Priority order:**

1. Function parameter (if provided)
2. Module attribute (`barangay.as_of`)
3. Environment variable (`BARANGAY_AS_OF`)
4. Default: None (use latest bundled data)

### `get_verbose()`

Get verbose logging setting from environment.

```python
from barangay import get_verbose

verbose = get_verbose()
```

### `get_cache_dir()`

Get cache directory path.

```python
from barangay import get_cache_dir

cache_dir = get_cache_dir()
print(cache_dir)
# /home/user/.cache/barangay
```

### `load_env_config()`

Load configuration from environment variables.

```python
from barangay import load_env_config

config = load_env_config()
print(config["BARANGAY_VERBOSE"])
```

## Module-Level Attributes

```python
import barangay

# Current dataset date
print(barangay.current)           # '2026-01-13'

# Available dataset dates
print(barangay.available_dates)    # List of available dates

# Set default date for session
barangay.as_of = "2025-07-08"
```

## Data Models

### BarangayModel

Pydantic model for barangay data validation.

```python
from barangay import BarangayModel

model = BarangayModel(
    barangay="Tongmageng",
    municipality_or_city="Tongmagen",
    province_or_huc="Tawi-Tawi",
    psgc_id="123456789"
)
```
