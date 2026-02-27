# CLI Reference

## Search

### `barangay search`

Fuzzy search for barangays.

```bash
barangay search "Tongmageng, Tawi-Tawi"
```

**Options:**

- `--limit`, `-l`: Maximum number of results (default: 5)
- `--threshold`, `-t`: Minimum similarity score 0-100 (default: 60.0)
- `--as-of`: Historical date (YYYY-MM-DD)
- `--format`, `-f`: Output format - `json` or `table` (default: table)

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
```

## Export

### `barangay export`

Export data to JSON or CSV.

```bash
barangay export --model flat --format json --output data.json
```

**Options:**

- `--model`: Data model - `flat`, `extended`, or `basic` (default: flat)
- `--format`, `-f`: Output format - `json` or `csv` (default: json)
- `--output`, `-o`: Output file (default: stdout)
- `--as-of`: Historical date (YYYY-MM-DD)

**Examples:**

```bash
# Export flat data to JSON
barangay export --model flat --format json --output data.json

# Export basic data to CSV
barangay export --model basic --format csv --output data.csv

# Export historical data
barangay export --model flat --format json --as-of "2025-07-08" --output historical.json
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

### `barangay history search`

Search historical data.

```bash
barangay history search "Tongmageng" --as-of "2025-07-08"
```

**Options:**

- `--as-of`: Historical date (YYYY-MM-DD) - **required**
- `--limit`, `-l`: Maximum number of results (default: 5)
- `--threshold`, `-t`: Minimum similarity score 0-100 (default: 60.0)
- `--format`, `-f`: Output format - `json` or `table` (default: table)

**Example:**

```bash
barangay history search "Tongmageng" --as-of "2025-07-08" --limit 5 --format table
```

### `barangay history export`

Export historical data.

```bash
barangay history export --as-of "2025-07-08" --model flat
```

**Options:**

- `--as-of`: Historical date (YYYY-MM-DD) - **required**
- `--model`: Data model - `flat`, `extended`, or `basic` (default: flat)
- `--format`, `-f`: Output format - `json` or `csv` (default: json)
- `--output`, `-o`: Output file (default: stdout)

**Example:**

```bash
barangay history export --as-of "2025-07-08" --model flat --format json --output 2025-07-08.json
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

- `--date`: Date to download (YYYY-MM-DD)

**Examples:**

```bash
# Download current data
barangay cache download

# Download specific historical date
barangay cache download --date "2025-07-08"
```

## Batch

### `barangay batch search`

Batch search from file (one query per line).

```bash
barangay batch search queries.txt --limit 5 --output results.json
```

**Options:**

- `--limit`, `-l`: Maximum number of results per query (default: 5)
- `--threshold`, `-t`: Minimum similarity score 0-100 (default: 60.0)
- `--as-of`: Historical date (YYYY-MM-DD)
- `--output`, `-o`: Output JSON file (default: stdout)

**Example:**

```bash
# queries.txt contains one query per line
barangay batch search queries.txt --limit 5 --output results.json
```

### `barangay batch validate`

Validate barangay names from file (one per line).

```bash
barangay batch validate barangay_names.txt
```

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
