# API Reference

## Main Search Function

### `search()`

Search for barangays using fuzzy string matching.

```python
from barangay import search

results = search("Tongmageng, Tawi-Tawi")
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `search_string` | `str` | - | The string to search for |
| `match_hooks` | `List[Literal["province", "municipality", "barangay"]]` | `["province", "municipality", "barangay"]` | Administrative levels to match against. Valid options: `"province"`, `"municipality"`, `"barangay"` |
| `threshold` | `float` | `60.0` | Minimum similarity score (0-100) |
| `n` | `int` | `5` | Maximum number of results |
| `search_sanitizer` | `Callable` | - | Function to sanitize search string |
| `fuzz_base` | `FuzzBase | None` | - | Pre-computed fuzzy matching instance for performance |
| `as_of` | `str | None` | - | Historical date (YYYY-MM-DD) or None for latest |

**Returns:** List[dict] with matching results

**Note:** The function supports multiple matching patterns:

- `B` (barangay only): Matches against barangay name only
- `PB` (province + barangay): Matches against province and barangay combined
- `MB` (municipality + barangay): Matches against municipality and barangay combined
- `PMB` (province + municipality + barangay): Matches against all three levels combined

Each result includes the following score fields:
- `f_000b_ratio_score`: Score for barangay-only match
- `f_0p0b_ratio_score`: Score for province + barangay match
- `f_00mb_ratio_score`: Score for municipality + barangay match
- `f_0pmb_ratio_score`: Score for province + municipality + barangay match

Each result also includes base fields (`000b`, `0p0b`, `00mb`, `0pmb`) for the corresponding match patterns.

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
    print(f"{result['barangay']} (score: {result['f_00mb_ratio_score']})")
```

## Data Access

### Pydantic Data Models

The package provides three main data models as Pydantic models:

#### `barangay` (AdminDiv)

Nested administrative division data model. Organizes data hierarchically by region → municipality/city → barangay.

```python
from barangay import barangay

# Access nested data using dict-like access
ncr_cities = list(barangay["National Capital Region (NCR)"].keys())
manila_brgys = barangay["National Capital Region (NCR)"]["City of Manila"]

# Iterate over regions
for region, municipalities in barangay.items():
    print(f"Region: {region}")
```

**Type:** `AdminDiv` (RootModel[dict[str, AdminDiv] | List[str]])

**Note:** This is a Pydantic model, not a plain dict. Use `.model_dump()` to convert to dict if needed.

#### `barangay_extended` (AdminDivExtended)

Extended recursive model with complete administrative hierarchy. Each division includes its PSGC ID, parent PSGC ID, type, and nested components.

```python
from barangay import barangay_extended

# Access extended hierarchical data
country = barangay_extended
for region in country.components:
    print(f"Region: {region.name} (PSGC: {region.psgc_id})")
    for province in region.components:
        print(f"  Province: {province.name}")
```

**Type:** `AdminDivExtended`

**Fields:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | - | Name of the administrative division |
| `type` | `str` | - | Type of division (country, region, province, city, municipality, barangay, special_geographic_area, submunicipality) |
| `psgc_id` | `str` | - | PSGC identifier or "n/a" |
| `parent_psgc_id` | `str` | - | Parent PSGC identifier or "n/a" |
| `nicknames` | `Optional[List[str]]` | - | Optional list of alternative names |
| `components` | `List[AdminDivExtended]` | - | List of nested administrative divisions |

#### `barangay_flat` (List[AdminDivFlat])

Flat list of all administrative divisions without nesting. Each entry is a standalone record.

```python
from barangay import barangay_flat

# Access flat data
all_barangays = [item for item in barangay_flat if item.type == "barangay"]
municipalities = [item for item in barangay_flat if item.type == "municipality"]

# Example: Find a specific barangay
brgy = [loc for loc in barangay_flat if loc.name == "Marayos"]
if brgy:
    print(f"Found: {brgy[0].name} in {brgy[0].type}")
```

**Type:** `List[AdminDivFlat]`

**Fields (AdminDivFlat):**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | - | Name of the administrative division |
| `type` | `str` | - | Type of division (country, region, province, city, municipality, barangay, special_geographic_area, submunicipality) |
| `psgc_id` | `str` | - | PSGC identifier or "n/a" |
| `parent_psgc_id` | `str` | - | Parent PSGC identifier or "n/a" |
| `nicknames` | `Optional[List[str]]` | - | Optional list of alternative names |

### Backward Compatibility Dictionaries

For backward compatibility, dict versions of the data are also available:

```python
from barangay import BARANGAY, BARANGAY_EXTENDED, BARANGAY_FLAT

# Dict versions (converted from Pydantic models at import time)
# Use these for legacy code or when you need plain dicts
BARANGAY  # dict: nested structure like barangay
BARANGAY_EXTENDED  # dict: extended nested structure
BARANGAY_FLAT  # List[dict]: list of dicts like barangay_flat
```

**Note:** These are converted from Pydantic models at module import time. For better performance, use the Pydantic models (`barangay`, `barangay_extended`, `barangay_flat`) directly when possible.

### Example: Data Model Comparison

```python
from barangay import barangay, barangay_extended, barangay_flat, BARANGAY_FLAT

# Using Pydantic models (recommended)
for item in barangay_flat:
    print(f"{item.name} - {item.type}")

# Using dict for compatibility
for item in BARANGAY_FLAT:
    print(f"{item['name']} - {item['type']}")
```

### DataManager

Manage data loading, caching, and downloading. Provides access to data from bundled package, local cache, or GitHub.

```python
from barangay import DataManager

dm = DataManager()

# Load latest data
data = dm.get_data(data_type="basic")

# Load historical data
data = dm.get_data(as_of="2025-07-08", data_type="flat")
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `as_of` | `str | None` | - | Historical date (YYYY-MM-DD) or None for latest bundled data |
| `data_type` | `str` | - | Data model type. Valid options: `"basic"` (nested structure), `"flat"` (flat list), `"extended"` (extended recursive structure) |

**Returns:** Depending on `data_type`:

- `"basic"`: dict
- `"flat"`: dict
- `"extended"`: dict

**Data Loading Priority:**

1. Bundled package data (for current version or latest)
2. Local cache (for historical dates)
3. Download from GitHub (if not cached)

**Note:** The DataManager automatically handles date resolution, caching, and downloads based on the `as_of` parameter and configuration.

## Fuzzy Matching

### `create_fuzz_base()`

Factory function to create FuzzBase instances for performance optimization. Reusing a FuzzBase instance across multiple searches improves performance by avoiding redundant data loading and preprocessing.

```python
from barangay import create_fuzz_base, search

# Create FuzzBase instance (can be reused for multiple searches)
fuzz_base = create_fuzz_base(as_of="2025-08-29")

# Use the same fuzz_base for multiple queries
results1 = search("Tongmageng", fuzz_base=fuzz_base)
results2 = search("Marayos", fuzz_base=fuzz_base)
results3 = search("San Jose", fuzz_base=fuzz_base)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `as_of` | `str | None` | - | Historical date (YYYY-MM-DD) or None for latest bundled data |

**Returns:** `FuzzBase` instance

### FuzzBase

Class for fuzzy matching operations with pre-computed matching functions.

```python
from barangay import FuzzBase, create_fuzz_base

# Create FuzzBase instance using factory function
fuzz_base = create_fuzz_base(as_of="2025-08-29")
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `fuzzer_base` | `pd.DataFrame` | - | DataFrame with preprocessed barangay data |
| `sanitizer` | `Callable` | `_basic_sanitizer` | Function to clean strings (optional) |

**Note:** FuzzBase internally creates four matching patterns:

- `000b`: Barangay name only
- `0p0b`: Province + Barangay
- `00mb`: Municipality + Barangay
- `0pmb`: Province + Municipality + Barangay

Each pattern has a pre-computed fuzzy matching function using `rapidfuzz.token_sort_ratio`.

## Utilities

### `sanitize_input()`

Utility function for string sanitization. Converts strings to lowercase and removes specified items.

```python
from barangay import sanitize_input

# Basic sanitization (lowercase only)
cleaned = sanitize_input("City of San Jose")
# Result: "city of san jose"

# Sanitize with exclusions
cleaned = sanitize_input("City of San Jose", exclude=["city of ", " city"])
# Result: "san jose"

# Using a list of exclusions
cleaned = sanitize_input("(pob.) San Jose City", exclude=["(pob.)", " city"])
# Result: "san jose"

# Using a single exclusion string
cleaned = sanitize_input("San Jose & vicinity", exclude="&")
# Result: "san jose  vicinity"
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_str` | `str | None` | - | String to sanitize. None becomes empty string |
| `exclude` | `List[str] | str | None` | - | Items to remove. Can be a list, string, or None |

**Returns:** Sanitized lowercase string with excluded items removed

**Note:** The function handles None input gracefully by converting it to an empty string.</think></tool_call>

### `resolve_date()`

Resolve approximate dates to the closest available dataset. This is useful when working with historical data that may not have exact date matches.

```python
from barangay import resolve_date

# Resolve to closest available date
resolved_date, status = resolve_date("2025-07-01", get_available_dates(), "2026-04-13")
print(resolved_date)  # '2025-07-08' (closest available)
print(status)  # Message describing the resolution
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `target_date` | `str` | - | Target date string (YYYY-MM-DD) |
| `available_dates` | `List[str]` | - | List of available dataset dates |
| `current_date` | `str` | - | Current dataset date (for reference) |

**Returns:** Tuple of (resolved_date: str | None, status_message: str)

### `get_available_dates()`

Get list of available historical dataset dates. This typically includes all historical releases available on GitHub.

```python
from barangay import get_available_dates

dates = get_available_dates()
print(dates)
# ['2023-01-25', '2023-04-18', '2023-08-15', '2023-10-24', '2024-01-23', '2024-04-23', '2024-05-08', '2024-07-12', '2024-10-18', '2025-01-30', '2025-04-23', '2025-07-08', '2025-08-29', '2025-10-13', '2026-01-13', '2026-04-13']
```

**Returns:** List[str] of available dates in YYYY-MM-DD format

**Note:** The current bundled version is also included in this list via the `barangay.available_dates` attribute.

## Configuration

### `resolve_as_of()`

Resolve the "as of" date for data queries from multiple layers with priority.

```python
from barangay import resolve_as_of

# Resolve with parameter
date = resolve_as_of(as_of_param="2025-08-29")
print(date)  # '2025-08-29'

# Resolve without parameter (uses module attribute or env var)
date = resolve_as_of()
print(date)  # None (if not set) or value from barangay.as_of or BARANGAY_AS_OF
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `as_of_param` | `str | None` | - | Optional date string from function parameter |

**Returns:** str | None - The resolved date string, or None for latest data

**Priority order:**

1. Function parameter (if provided)
2. Module attribute (`barangay.as_of`)
3. Environment variable (`BARANGAY_AS_OF`)
4. Default: None (use latest bundled data)

### `get_verbose()`

Get verbose logging setting from environment variable.

```python
from barangay import get_verbose

verbose = get_verbose()
print(verbose)  # True or False
```

**Returns:** bool - True if verbose logging is enabled

**Environment Variable:** `BARANGAY_VERBOSE`

- Valid values (case-insensitive): `"true"`, `"1"`, `"yes"`, `"on"`
- Default: `"true"`

### `get_cache_dir()`

Get the cache directory path for the application.

```python
from barangay import get_cache_dir

cache_dir = get_cache_dir()
print(cache_dir)
# /home/user/.cache/barangay (or custom path)
```

**Returns:** Path - The cache directory path

**Priority order:**

1. Environment variable `BARANGAY_CACHE_DIR` (if set)
2. Windows: `%LOCALAPPDATA%\barangay\cache`
3. Linux/Mac with XDG_CACHE_HOME: `$XDG_CACHE_HOME/barangay`
4. Linux/Mac fallback: `~/.cache/barangay`

### `load_env_config()`

Load configuration from environment variables.

```python
from barangay import load_env_config

config = load_env_config()
print(config)
# {
#     'BARANGAY_AS_OF': '2025-07-08' (or None),
#     'BARANGAY_VERBOSE': 'true',
#     'BARANGAY_CACHE_DIR': None (or custom path)
# }
```

**Returns:** dict with keys:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `BARANGAY_AS_OF` | `str | None` | - | Target dataset date or None |
| `BARANGAY_VERBOSE` | `str` | `"true"` | Verbose setting string |
| `BARANGAY_CACHE_DIR` | `str | None` | - | Custom cache directory path or None |

## Module-Level Attributes

```python
import barangay

# Current dataset date (from bundled package)
print(barangay.current)           # '2026-04-13'

# Available dataset dates (historical + current)
print(barangay.available_dates)    # List of available dates

# Set default date for session (affects search() if no as_of parameter)
barangay.as_of = "2025-07-08"
```

**Attributes:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `current` | `str` | - | Current bundled dataset date (YYYY-MM-DD format). Read from `barangay/data/CURRENT_VERSION` |
| `as_of` | `str | None` | - | Default historical date to use for data queries. Can be set at runtime. Defaults to None (use latest data) |
| `available_dates` | `List[str]` | - | List of all available dataset dates including historical releases and current version. Populated at module import |

## Data Models

### BarangayModel

Pydantic model for barangay data validation and serialization.

```python
from barangay import BarangayModel

# Create a new instance
model = BarangayModel(
    barangay="Tongmageng",
    municipality_or_city="Tongmagen",
    province_or_huc="Tawi-Tawi",
    psgc_id="123456789"
)

# Access fields
print(model.barangay)              # 'Tongmageng'
print(model.municipality_or_city)  # 'Tongmagen'
print(model.province_or_huc)       # 'Tawi-Tawi'
print(model.psgc_id)               # '123456789'

# Convert to dict
model_dict = model.model_dump()
# {'barangay': 'Tongmageng', 'municipality_or_city': 'Tongmagen', ...}

# Convert to JSON
model_json = model.model_dump_json()
```

**Fields:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `barangay` | `str` | - | Name of the barangay |
| `province_or_huc` | `str` | - | Province or highly urbanized city name |
| `municipality_or_city` | `str` | - | Municipality or city name |
| `psgc_id` | `str` | - | Philippine Standard Geographic Code identifier |

**Note:** This is a simple model used for single barangay records, distinct from the hierarchical AdminDiv models.

### AdminDiv

Root model for administrative division mapping. Can be either a nested dict structure or a flat list of identifiers.

```python
from barangay import AdminDiv, barangay

# Used by the barangay module-level attribute
# Acts as a dict-like container
for region, municipalities in barangay.items():
    print(f"Region: {region}")
    for municipality, brgys in municipalities.items():
        print(f"  Municipality: {municipality}")
```

**Type:** RootModel[dict[str, AdminDiv] | List[str]]

**Methods:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `keys()` | `Callable` | - | Get keys if root is a dict |
| `values()` | `Callable` | - | Get values if root is a dict |
| `items()` | `Callable` | - | Get items if root is a dict |
| `__contains__()` | `Callable` | - | Check membership |
| `__iter__()` | `Callable` | - | Iterate over the root structure |

### AdminDivExtended

Extended model for administrative division data with complete hierarchical structure. Each division can have nested components.

```python
from barangay import AdminDivExtended

# Example structure
region = AdminDivExtended(
    name="National Capital Region (NCR)",
    type="region",
    psgc_id="130000000",
    parent_psgc_id="n/a",
    nicknames=["NCR", "Metro Manila"],
    components=[...]
)

# Access nested components
for component in region.components:
    print(f"{component.type}: {component.name}")
```

**Fields:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | - | Name of the administrative division |
| `type` | `Literal` | - | Type of division. Valid values: `"country"`, `"region"`, `"province"`, `"city"`, `"municipality"`, `"barangay"`, `"special_geographic_area"`, `"submunicipality"` |
| `psgc_id` | `str | Literal["n/a"]` | - | PSGC identifier |
| `parent_psgc_id` | `str | Literal["n/a"]` | - | Parent PSGC identifier |
| `nicknames` | `Optional[List[str]]` | - | List of alternative names |
| `components` | `List[AdminDivExtended]` | - | List of nested administrative divisions |

**Note:** This is a recursive model where each division can contain nested child divisions, allowing for complete hierarchical representation of the Philippine administrative structure.

### AdminDivFlat

Flat model for administrative division data without nesting. Each record is self-contained with all necessary information.

```python
from barangay import AdminDivFlat, barangay_flat

# Find barangays by type
barangays = [item for item in barangay_flat if item.type == "barangay"]

# Find by name
for item in barangay_flat:
    if item.name == "Marayos":
        print(f"Found: {item.name}")
        print(f"Type: {item.type}")
        print(f"PSGC ID: {item.psgc_id}")
        print(f"Parent: {item.parent_psgc_id}")
        break
```

**Fields:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | - | Name of the administrative division |
| `type` | `Literal` | - | Type of division (same as AdminDivExtended) |
| `psgc_id` | `str | Literal["n/a"]` | - | PSGC identifier |
| `parent_psgc_id` | `str | Literal["n/a"]` | - | Parent PSGC identifier |
| `nicknames` | `Optional[List[str]]` | - | List of alternative names |

**Note:** Unlike AdminDivExtended, this model has no nested components, making it ideal for flat list representations and simple lookups.
