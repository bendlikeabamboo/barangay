# Barangay CLI Skill

Interact with the Philippines barangay data package via CLI for searching, exporting, and managing administrative unit data.

## Invocation

```bash
# Direct CLI invocation
python -m barangay <command> [options]

# Or if installed
barangay <command> [options]
```

## Commands

### Search
`search <query>` - Fuzzy search barangays by name
- `--limit N` - Max results (default: 5)
- `--threshold 0-100` - Match sensitivity (default: 60.0)
- `--as-of YYYY-MM-DD` - Search historical data
- `--format {json,table}` - Output format (default: table)

### Info
`info version` - Show package version
`info stats` - Display data statistics
`info list-regions` - List all regions
`info list-municipalities <region>` - List municipalities in region
`info list-barangays <municipality>` - List barangays in municipality

### Export
`export` - Export all data to file
- `--model {basic,flat,extended}` - Data structure model
- `--format {json,csv}` - Output format (default: json)
- `--output PATH` - Output file path
- `--as-of YYYY-MM-DD` - Export historical data

### History
`history list-dates` - List available historical dates
`history search-history <query> --as-of <date>` - Search historical records (--as-of is required)
`history export-history --as-of <date>` - Export historical snapshot (--as-of is required)

### Cache
`cache info` - Display cache status
`cache clear` - Clear local cache
`cache download [--date]` - Download/update data (latest or specific date)

### Batch
`batch batch-search <file>` - Search multiple queries from file
`batch validate <file>` - Validate barangay codes/identifiers in file

## Examples

```bash
# Search barangays
python -m barangay search "Santo Nino" --limit 5 --format json

# List municipalities in NCR
python -m barangay info list-municipalities NCR

# Export to CSV with extended model
python -m barangay export --model extended --format csv --output data.csv

# Search historical data
python -m barangay search "Manila" --as-of 2025-01-13 --format table

# Download latest data
python -m barangay cache download

# Batch process
python -m barangay batch batch-search queries.txt
```

## Important Notes

- **Date Format**: Use `YYYY-MM-DD` for `--as-of` parameter
- **Models**:
  - `basic` - Nested structure (regions → municipalities → barangays)
  - `flat` - Flattened list with all fields
  - `extended` - Recursive structure with parent references
- **Output Formats**: Default varies by command (search=table, export=json)
- **Cache**: Data is cached locally; use `cache clear` to reset
- **Fuzzy Search**: Threshold is 0-100 (lower = more results, higher = stricter matches)
- **History Commands**: `--as-of` is required for `search-history` and `export-history`
