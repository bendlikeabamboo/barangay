CLI Usage Examples
==================

This document provides real-world examples of using the barangay CLI for various
tasks. Each example demonstrates practical use cases with detailed explanations
and expected outputs.

Use Cases
---------

Address Lookup for Delivery Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: A delivery service needs to quickly validate and look up address
information for barangays across the Philippines.

Basic Address Lookup

Quick lookup of a barangay:

.. code:: bash

   barangay search "Tongmageng"

Output:

.. code:: text

   ┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┓
   ┃ Barangay   ┃ Municipality/City  ┃ Province/HUC    ┃ PSGC ID  ┃ Score  ┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━┩
   │ Tongmageng │ Sitangkai           │ Tawi-Tawi       │ 157501001 │  95.2  │
   └────────────┴─────────────────────┴─────────────────┴───────────┴────────┘

Address Lookup with Context

Lookup with more context for better accuracy:

.. code:: bash

   barangay search "Tongmageng, Tawi-Tawi" --threshold 85

High-Confidence Validation

For critical delivery validation, use a high threshold:

.. code:: bash

   barangay search "Tongmageng" --threshold 90

Batch Address Validation

Validate multiple addresses at once:

.. code:: bash

   # Create input file
   cat > delivery_addresses.txt << EOF
   Tongmageng
   San Jose
   Quezon City
   Manila
   EOF

   # Batch validate
   barangay batch search delivery_addresses.txt --output delivery_results.json

Check the results:

.. code:: bash

   cat delivery_results.json

Data Export for Analytics
~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Export barangay data for analysis in spreadsheets, databases, or
data visualization tools.

Export to CSV for Spreadsheet Analysis

Export flat model data to CSV:

.. code:: bash

   barangay export --model flat --format csv --output barangay_data.csv

The CSV file can be opened in Excel, Google Sheets, or imported into databases:

.. code:: bash

   # View first few lines
   head -20 barangay_data.csv

Export to JSON for Programming

Export to JSON for use in applications:

.. code:: bash

   barangay export --model flat --format json --output barangay_data.json

Export Extended Model for Hierarchical Analysis

Export the extended model for hierarchical data analysis:

.. code:: bash

   barangay export --model extended --format json --output barangay_extended.json

Export Historical Data for Trend Analysis

Export historical data for comparing changes over time:

.. code:: bash

   # Export multiple historical snapshots
   barangay export --as-of 2025-07-08 --model flat --output snapshot_2025_07_08.json
   barangay export --as-of 2025-08-29 --model flat --output snapshot_2025_08_29.json
   barangay export --as-of 2025-10-13 --model flat --output snapshot_2025_10_13.json

Regional Data Export

Export data for a specific region by filtering the exported data:

.. code:: bash

   # Export all data
   barangay export --model flat --format json --output all_data.json

   # Filter for NCR using jq
   jq '[.[] | select(.province_or_huc == "NCR")]' all_data.json > ncr_data.json

Data Exploration and Research
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Researchers exploring Philippine geographic data for analysis or
visualization.

Explore Data Structure

Check the current data version:

.. code:: bash

   barangay info version

View data statistics:

.. code:: bash

   barangay info stats

Explore Regions

List all regions to understand the geographic coverage:

.. code:: bash

   barangay info list-regions

Explore Municipalities

List municipalities in a specific region:

.. code:: bash

   # Explore NCR
   barangay info list-municipalities "NCR"

   # Explore a region
   barangay info list-municipalities "Region I - Ilocos Region"

Explore Barangays

List barangays in a municipality:

.. code:: bash

   # Explore Quezon City
   barangay info list-barangays "Quezon City"

   # Explore a municipality
   barangay info list-barangays "City of Manila"

Search Patterns

Search for barangays with specific names:

.. code:: bash

   # Search for barangays with "San" in the name
   barangay search "San" --limit 20

   # Search for barangays with "1" in the name
   barangay search "Barangay 1" --limit 20

Historical Data Analysis

List available historical dates:

.. code:: bash

   barangay history list-dates

Compare data across different dates:

.. code:: bash

   # Search in different historical snapshots
   barangay history search "Tongmageng" --as-of 2025-07-08
   barangay history search "Tongmageng" --as-of 2025-08-29
   barangay history search "Tongmageng" --as-of 2025-10-13

Data Cleaning and Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Clean and validate a database of Philippine addresses.

Single Address Validation

Validate a single address:

.. code:: bash

   # High confidence validation
   barangay search "Tongmageng" --threshold 90 --format json

Batch Validation of Address Database

Create a file with addresses to validate:

.. code:: bash

   cat > addresses_to_validate.txt << EOF
   Tongmageng
   San Jose
   Quezon City
   Invalid Barangay Name
   Typo Barangay
   EOF

Batch validate the addresses:

.. code:: bash

   barangay batch validate addresses_to_validate.txt

Output:

.. code:: text

   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃ Barangay              ┃ Status      ┃ Match            ┃
   ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
   │ Tongmageng           │ Valid       │ Tongmageng       │
   │ San Jose             │ Valid       │ San Jose         │
   │ Quezon City          │ Valid       │ Quezon City      │
   │ Invalid Barangay...  │ Not found   │ -                │
   │ Typo Barangay        │ Not found   │ -                │
   └──────────────────────┴─────────────┴──────────────────┘

Fuzzy Matching for Typos

Search with lower threshold to find potential matches for typos:

.. code:: bash

   # Search for potential typo matches
   barangay search "Tongmagen" --threshold 70 --limit 5

Export Validated Data

Export validated data for further processing:

.. code:: bash

   # Batch search and export
   barangay batch search addresses_to_validate.txt --output validated_results.json

Integration with Shell Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Integrate barangay CLI into shell scripts for automation.

Simple Lookup Script

Create a script to look up barangay information:

.. code:: bash

   #!/bin/bash

   # lookup_barangay.sh - Look up barangay information
   if [ -z "$1" ]; then
       echo "Usage: $0 <barangay_name>"
       exit 1
   fi

   echo "Looking up: $1"
   barangay search "$1" --format json | jq '.[0]'

Usage:

.. code:: bash

   chmod +x lookup_barangay.sh
   ./lookup_barangay.sh "Tongmageng"

Batch Processing Script

Create a script to process multiple queries:

.. code:: bash

   #!/bin/bash

   # batch_lookup.sh - Batch lookup barangay information
   INPUT_FILE="$1"
   OUTPUT_FILE="$2"

   if [ -z "$INPUT_FILE" ] || [ -z "$OUTPUT_FILE" ]; then
       echo "Usage: $0 <input_file> <output_file>"
       exit 1
   fi

   echo "Processing queries from $INPUT_FILE..."
   barangay batch search "$INPUT_FILE" --output "$OUTPUT_FILE"
   echo "Results saved to $OUTPUT_FILE"

Usage:

.. code:: bash

   chmod +x batch_lookup.sh
   ./batch_lookup.sh queries.txt results.json

Validation Script

Create a script to validate barangay names:

.. code:: bash

   #!/bin/bash

   # validate_barangays.sh - Validate barangay names
   INPUT_FILE="$1"

   if [ -z "$INPUT_FILE" ]; then
       echo "Usage: $0 <input_file>"
       exit 1
   fi

   echo "Validating barangay names from $INPUT_FILE..."
   barangay batch validate "$INPUT_FILE"

Usage:

.. code:: bash

   chmod +x validate_barangays.sh
   ./validate_barangays.sh barangays.txt

Cache Management for Offline Use
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Download data for offline use in environments without internet access.

Download Current Data

Download the current data for offline use:

.. code:: bash

   # Download current data
   barangay cache download

Download Historical Data

Download specific historical data:

.. code:: bash

   # Download all available historical data
   barangay cache download --date 2025-07-08
   barangay cache download --date 2025-08-29
   barangay cache download --date 2025-10-13

Check Cache Status

Verify the cached data:

.. code:: bash

   barangay cache info

Output:

.. code:: text

   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃ Property                                             ┃
   ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ Cache directory    │ /home/user/.cache/barangay     │
   │ Files               │ 4                              │
   │ Total size          │ 16.57 MB                       │
   │                     │                                │
   │ Cached files        │                                │
   │                     │ barangay_2025-07-08.json (4.12 MB) │
   │                     │ barangay_2025-08-29.json (4.18 MB) │
   │                     │ barangay_2025-10-13.json (4.15 MB) │
   │                     │ barangay_current.json (4.12 MB)    │
   └──────────────────────────────────────────────────────┘

Clear Cache

Clear the cache to free disk space:

.. code:: bash

   barangay cache clear

Offline Usage

Once data is cached, you can use it offline:

.. code:: bash

   # Search using cached data
   barangay search "Tongmageng"

   # Export using cached data
   barangay export --model flat --output offline_data.json

Integration with Other Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Integrate barangay CLI with other command-line tools and utilities.

Pipe to jq for JSON Processing

Process JSON output with jq:

.. code:: bash

   # Extract specific fields
   barangay search "Tongmageng" --format json | jq '.[] | {barangay, municipality, province: .province_or_huc, psgc_id}'

    # Filter by score (calculate max from individual score fields)
    barangay search "San Jose" --format json | jq '.[] | select([.f_000b_ratio_score, .f_0p0b_ratio_score, .f_00mb_ratio_score, .f_0pmb_ratio_score] | max > 80)'

   # Count results
   barangay search "San Jose" --format json | jq 'length'

Pipe to grep for Text Processing

Filter table output with grep:

.. code:: bash

   # Search for specific province
   barangay search "San Jose" --format table | grep "Tawi-Tawi"

   # Count matches
   barangay search "San Jose" --format table | grep -c "San Jose"

Combine with awk for Custom Formatting

Format output with awk:

.. code:: bash

   # Extract PSGC IDs
   barangay search "Tongmageng" --format json | jq -r '.[].psgc_id'

   # Create custom CSV
   barangay search "San Jose" --limit 10 --format json | jq -r '.[] | "\(.barangay),\(.municipality_or_city),\(.province_or_huc),\(.psgc_id)"'

Integration with Databases

Export data for database import:

.. code:: bash

   # Export to CSV for database import
   barangay export --model flat --format csv --output barangay_import.csv

   # Import into SQLite
   sqlite3 barangay.db << EOF
   CREATE TABLE barangays (
       barangay TEXT,
       municipality_or_city TEXT,
       province_or_huc TEXT,
       psgc_id TEXT PRIMARY KEY
   );
   .import --csv barangay_import.csv barangays
   EOF

   # Query the database
   sqlite3 barangay.db "SELECT * FROM barangays WHERE barangay LIKE '%San%' LIMIT 10;"

Web Application Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Use the CLI as a backend for web applications or APIs.

Create a Simple API Endpoint

Create a simple shell script API:

.. code:: bash

   #!/bin/bash

   # api_search.sh - Simple API for barangay search
   QUERY="$1"
   FORMAT="${2:-json}"

   if [ -z "$QUERY" ]; then
       echo '{"error": "Query parameter required"}'
       exit 1
   fi

   barangay search "$QUERY" --format "$FORMAT"

Usage:

.. code:: bash

   chmod +x api_search.sh
   ./api_search.sh "Tongmageng" json

Create a Validation API

Create a validation endpoint:

.. code:: bash

   #!/bin/bash

   # api_validate.sh - Validate barangay names
   BARANGAY="$1"
   THRESHOLD="${2:-80}"

   if [ -z "$BARANGAY" ]; then
       echo '{"error": "Barangay name required"}'
       exit 1
   fi

    RESULT=$(barangay search "$BARANGAY" --threshold "$THRESHOLD" --format json | jq '.[0]')

    if [ "$(echo "$RESULT" | jq -r '.f_000b_ratio_score')" != "null" ]; then
        SCORE=$(echo "$RESULT" | jq -r '[.f_000b_ratio_score, .f_0p0b_ratio_score, .f_00mb_ratio_score, .f_0pmb_ratio_score] | max')
        if (( $(echo "$SCORE >= $THRESHOLD" | bc -l) )); then
           echo '{"valid": true, "data": '"$RESULT"'}'
       else
           echo '{"valid": false, "message": "Score below threshold"}'
       fi
   else
       echo '{"valid": false, "message": "No match found"}'
   fi

Usage:

.. code:: bash

   chmod +x api_validate.sh
   ./api_validate.sh "Tongmageng" 80

Data Migration and Backup
~~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Migrate data between systems or create backups.

Create Data Backup

Export all data models for backup:

.. code:: bash

   # Create backup directory
   mkdir -p barangay_backup

   # Export all models
   barangay export --model basic --format json --output barangay_backup/basic.json
   barangay export --model flat --format json --output barangay_backup/flat.json
   barangay export --model extended --format json --output barangay_backup/extended.json

   # Export historical snapshots
   for date in 2025-07-08 2025-08-29 2025-10-13; do
       barangay export --as-of "$date" --model flat --format json --output "barangay_backup/snapshot_$date.json"
   done

Migrate to Another System

Export data in a format suitable for another system:

.. code:: bash

   # Export to CSV for spreadsheet systems
   barangay export --model flat --format csv --output migration_data.csv

   # Export to JSON for NoSQL databases
   barangay export --model extended --format json --output migration_data.json

Incremental Backups

Create incremental backups of historical data:

.. code:: bash

   #!/bin/bash

   # incremental_backup.sh - Create incremental backups
   BACKUP_DIR="backups/$(date +%Y%m%d)"
   mkdir -p "$BACKUP_DIR"

   # Export current data
   barangay export --model flat --format json --output "$BACKUP_DIR/current.json"

   # Export historical data
   for date in $(barangay history list-dates --format json | jq -r '.[].Date' | grep -v "Current"); do
       barangay export --as-of "$date" --model flat --format json --output "$BACKUP_DIR/snapshot_$date.json"
   done

   echo "Backup created in $BACKUP_DIR"

Performance Monitoring
~~~~~~~~~~~~~~~~~~~~~~

Scenario: Monitor and optimize CLI performance.

Benchmark Search Performance

Measure search performance:

.. code:: bash

   # Time a single search
   time barangay search "Tongmageng"

   # Benchmark multiple searches
   for i in {1..10}; do
       time barangay search "San Jose" > /dev/null
   done

Monitor Cache Performance

Check cache size and performance:

.. code:: bash

   # Check cache status
   barangay cache info

   # Measure cache hit performance
   time barangay search "Tongmageng"  # First run (cache miss)
   time barangay search "Tongmageng"  # Second run (cache hit)

Optimize Batch Operations

Optimize batch processing with appropriate parameters:

.. code:: bash

   # Test different thresholds
   time barangay batch search queries.txt --threshold 90
   time barangay batch search queries.txt --threshold 70
   time barangay batch search queries.txt --threshold 50

   # Test different limits
   time barangay batch search queries.txt --limit 3
   time barangay batch search queries.txt --limit 5
   time barangay batch search queries.txt --limit 10

Troubleshooting Examples
~~~~~~~~~~~~~~~~~~~~~~~~

Scenario: Diagnose and resolve common issues.

Debug Search Results

Debug search results with different parameters:

.. code:: bash

   # Try different thresholds
   barangay search "query" --threshold 90
   barangay search "query" --threshold 70
   barangay search "query" --threshold 50

   # Try different limits
   barangay search "query" --limit 10
   barangay search "query" --limit 20

   # Try JSON output for detailed information
   barangay search "query" --format json

Debug Cache Issues

Diagnose cache-related problems:

.. code:: bash

   # Check cache status
   barangay cache info

   # Clear cache
   barangay cache clear

   # Redownload data
   barangay cache download

Debug Historical Data

Verify historical data availability:

.. code:: bash

   # List available dates
   barangay history list-dates

   # Try searching with different dates
   barangay history search "query" --as-of 2025-07-08
   barangay history search "query" --as-of 2025-08-29

Debug Batch Processing

Debug batch processing issues:

.. code:: bash

   # Check input file format
   cat queries.txt

   # Try with a smaller file
   head -5 queries.txt > test_queries.txt
   barangay batch search test_queries.txt

   # Check output format
   barangay batch search queries.txt --format json | jq '.'

Advanced Workflows
~~~~~~~~~~~~~~~~~~

Scenario: Complex workflows combining multiple CLI commands.

Complete Data Pipeline

Create a complete data pipeline:

.. code:: bash

   #!/bin/bash

   # data_pipeline.sh - Complete data processing pipeline
   set -e

   echo "=== Barangay Data Pipeline ==="

   # Step 1: Check cache
   echo "Step 1: Checking cache..."
   barangay cache info

   # Step 2: Download data if needed
   echo "Step 2: Ensuring data is available..."
   barangay cache download

   # Step 3: Export current data
   echo "Step 3: Exporting current data..."
   OUTPUT_DIR="output/$(date +%Y%m%d)"
   mkdir -p "$OUTPUT_DIR"

   barangay export --model flat --format json --output "$OUTPUT_DIR/current.json"
   barangay export --model flat --format csv --output "$OUTPUT_DIR/current.csv"

   # Step 4: Export historical snapshots
   echo "Step 4: Exporting historical snapshots..."
   for date in 2025-07-08 2025-08-29 2025-10-13; do
       barangay export --as-of "$date" --model flat --format json --output "$OUTPUT_DIR/snapshot_$date.json"
   done

   # Step 5: Validate sample data
   echo "Step 5: Validating sample data..."
   echo -e "Tongmageng\nSan Jose\nQuezon City" > "$OUTPUT_DIR/sample_queries.txt"
   barangay batch search "$OUTPUT_DIR/sample_queries.txt" --output "$OUTPUT_DIR/validation_results.json"

   # Step 6: Generate report
   echo "Step 6: Generating report..."
   cat > "$OUTPUT_DIR/report.txt" << EOF
   Barangay Data Pipeline Report
   ==============================
   Date: $(date)

   Files Generated:
   - current.json
   - current.csv
   - snapshot_2025-07-08.json
   - snapshot_2025-08-29.json
   - snapshot_2025-10-13.json
   - validation_results.json

   Data Statistics:
   EOF

   barangay info stats >> "$OUTPUT_DIR/report.txt"

   echo "=== Pipeline Complete ==="
   echo "Output directory: $OUTPUT_DIR"

Usage:

.. code:: bash

   chmod +x data_pipeline.sh
   ./data_pipeline.sh

Multi-Region Analysis

Analyze data across multiple regions:

.. code:: bash

   #!/bin/bash

   # regional_analysis.sh - Analyze data across regions
   OUTPUT_DIR="regional_analysis/$(date +%Y%m%d)"
   mkdir -p "$OUTPUT_DIR"

   # Get list of regions
   barangay info list-regions > "$OUTPUT_DIR/regions.txt"

   # Export data for each region
   while read -r region; do
       echo "Processing: $region"
       barangay export --model flat --format json --output "$OUTPUT_DIR/${region// /_}.json"
   done < "$OUTPUT_DIR/regions.txt"

   # Generate summary
   echo "Regional Analysis Summary" > "$OUTPUT_DIR/summary.txt"
   echo "Date: $(date)" >> "$OUTPUT_DIR/summary.txt"
   echo "" >> "$OUTPUT_DIR/summary.txt"
   echo "Regions processed:" >> "$OUTPUT_DIR/summary.txt"
   wc -l "$OUTPUT_DIR/regions.txt" >> "$OUTPUT_DIR/summary.txt"

   echo "Analysis complete: $OUTPUT_DIR"

Usage:

.. code:: bash

   chmod +x regional_analysis.sh
   ./regional_analysis.sh

See Also
--------

* :doc:`../how_to/cli_operations` - CLI user guide
* :doc:`../api_reference/cli` - CLI API reference
* :doc:`address_validation` - Address validation examples
* :doc:`batch_processing` - Batch processing examples
* :doc:`data_analysis` - Data analysis examples