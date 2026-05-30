# CLI Reference

## Search

### `barangay search`

Fuzzy search for barangays.

```bash
barangay search "Tongmageng, Tawi-Tawi"
```

**Options:**

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `--limit`, `-l` | `int` | `5` | No | Maximum number of results |
| `--threshold`, `-t` | `float` | `60.0` | No | Minimum similarity score 0-100 |
| `--as-of` | `str` | - | No | Historical date (YYYY-MM-DD) |
| `--format`, `-f` | `str` | `table` | No | Output format - `json` or `table` |
| `--plugin` | `str` | - | No | Enable a plugin for enrichment (repeatable) |

**Examples:**

```bash
# Basic search
barangay search "Tongmageng, Tawi-Tawi"

# With custom limit and threshold
barangay search "Tongmageng" --limit 5 --threshold 70.0

# JSON output
barangay search "Tongmageng" --format json

# Historical data search
barangay search "Tongmageng" --as-of "2025-07-08" --format table

# With plugin enrichment
barangay search "Tongmageng" --plugin psgc-aux-data --format json
```

**Note:** Results include scores for each matching level (barangay only, province+barangay, municipality+barangay, province+municipality+barangay). Use `--format json` to see individual score fields.

## Export

### `barangay export`

Export data to JSON or CSV.

```bash
barangay export --model flat --format json --output data.json
```

**Options:**

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `--model` | `str` | `flat` | No | Data model - `flat`, `extended`, or `basic` |
| `--format`, `-f` | `str` | `json` | No | Output format - `json` or `csv` |
| `--output`, `-o` | `str` | `stdout` | No | Output file |
| `--as-of` | `str` | - | No | Historical date (YYYY-MM-DD) |
| `--plugin` | `str` | - | No | Enable a plugin for enrichment (repeatable; only with `--model flat`) |

**Examples:**

```bash
# Export flat data to JSON
barangay export --model flat --format json --output data.json

# Export basic data to CSV
barangay export --model basic --format csv --output data.csv

# Export historical data
barangay export --model flat --format json --as-of "2025-07-08" --output historical.json

# Export with plugin enrichment
barangay export --model flat --plugin psgc-aux-data --format json --output enriched.json
```

## Info

### `barangay info version`

Show current data version.

```bash
barangay info version
```

### `barangay info stats`

Show data statistics.

```bash
barangay info stats
```

### `barangay info list-regions`

List all regions.

```bash
barangay info list-regions
```

### `barangay info list-municipalities`

List municipalities in a region.

```bash
barangay info list-municipalities "National Capital Region (NCR)"
```

**Note:** Region name must match exactly as shown in the data (e.g., "National Capital Region (NCR)", not just "NCR").

### `barangay info list-barangays`

List barangays in a municipality.

```bash
barangay info list-barangays "City of Manila"
```

## History

### `barangay history list-dates`

List available historical dates.

```bash
barangay history list-dates
```

### `barangay history search-history`

Search historical data.

```bash
barangay history search-history "Tongmageng" --as-of "2025-07-08"
```

**Options:**

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `--as-of` | `str` | - | Yes | Historical date (YYYY-MM-DD) |
| `--limit`, `-l` | `int` | `5` | No | Maximum number of results |
| `--threshold`, `-t` | `float` | `60.0` | No | Minimum similarity score 0-100 |
| `--format`, `-f` | `str` | `table` | No | Output format - `json` or `table` |

**Example:**

```bash
barangay history search-history "Tongmageng" --as-of "2025-07-08" --limit 5 --format table
```

### `barangay history export-history`

Export historical data.

```bash
barangay history export-history --as-of "2025-07-08" --model flat
```

**Options:**

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `--as-of` | `str` | - | Yes | Historical date (YYYY-MM-DD) |
| `--model` | `str` | `flat` | No | Data model - `flat`, `extended`, or `basic` |
| `--format`, `-f` | `str` | `json` | No | Output format - `json` or `csv` |
| `--output`, `-o` | `str` | `stdout` | No | Output file |

**Example:**

```bash
barangay history export-history --as-of "2025-07-08" --model flat --format json --output 2025-07-08.json
```

## Cache

### `barangay cache info`

Show cache information.

```bash
barangay cache info
```

### `barangay cache clear`

Clear cache directory.

```bash
barangay cache clear
```

### `barangay cache download`

Download data to cache.

```bash
barangay cache download
```

**Options:**

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `--date` | `str` | - | No | Date to download (YYYY-MM-DD) |

**Examples:**

```bash
# Download current data
barangay cache download

# Download specific historical date
barangay cache download --date "2025-07-08"
```

## Batch

### `barangay batch batch-search`

Batch search from file (one query per line).

```bash
barangay batch batch-search queries.txt --limit 5 --output results.json
```

**Options:**

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `--limit`, `-l` | `int` | `5` | No | Maximum number of results per query |
| `--threshold`, `-t` | `float` | `60.0` | No | Minimum similarity score 0-100 |
| `--as-of` | `str` | - | No | Historical date (YYYY-MM-DD) |
| `--output`, `-o` | `str` | `stdout` | No | Output JSON file |

**Example:**

```bash
# queries.txt contains one query per line
barangay batch batch-search queries.txt --limit 5 --output results.json
```

### `barangay batch validate`

Validate barangay names from file (one per line).

```bash
barangay batch validate barangay_names.txt
```

**Note:** This command uses a high threshold (95.0) to validate exact matches. It displays whether each barangay name is valid or not found.

**Example:**

```bash
# barangay_names.txt contains one barangay name per line
barangay batch validate barangay_names.txt
```

## Help

```bash
barangay --help
barangay search --help
barangay export --help
barangay info --help
barangay history --help
barangay cache --help
barangay batch --help
```
