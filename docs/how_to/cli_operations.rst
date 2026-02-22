CLI Operations
==============

This guide provides practical how-to instructions for using the barangay command-line interface (CLI).

Installation
------------

The CLI is automatically installed when you install the barangay package:

.. code:: bash

   pip install barangay

After installation, the CLI is available as ``barangay``:

.. code:: bash

   # Show help
   barangay --help

   # Show version
   barangay --version

   # Get help for a specific command
   barangay search --help

Basic Commands
--------------

Search Commands
~~~~~~~~~~~~~~~

**Basic Search**

Search for a barangay with default parameters:

.. code:: bash

   barangay search "Tongmageng"

Output:

.. code:: text

   ┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
   ┃ Barangay   ┃ Municipality/City ┃ Province/HUC  ┃ PSGC ID    ┃ Score ┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
   │ Tongmageng │ Sitangkai         │ Tawi-Tawi     │ 1907005010 │ 69.0  │
   │ Bonga      │ Marogong          │ Lanao del Sur │ 1903631006 │ 66.7  │
   │ Bubong     │ Maguing           │ Lanao del Sur │ 1903634051 │ 66.7  │
   │ Cambong    │ Maguing           │ Lanao del Sur │ 1903634016 │ 64.0  │
   │ Kamagong   │ Bongao            │ Tawi-Tawi     │ 1907002006 │ 64.0  │
   └────────────┴───────────────────┴───────────────┴────────────┴───────┘

**Search with Custom Parameters**

Get more results:

.. code:: bash

   barangay search "San Jose" --limit 10

Get only high-confidence matches:

.. code:: bash

   barangay search "San Jose" --threshold 85

Search using data from a specific date:

.. code:: bash

   barangay search "Tongmageng" --as-of 2025-07-08

Get results in JSON format:

.. code:: bash

   barangay search "Tongmageng" --format json

**Historical Search**

Search for barangays in historical data:

.. code:: bash

   barangay history search "Tongmageng" --as-of 2025-07-08

List available historical dates:

.. code:: bash

   barangay history list-dates

Export Commands
~~~~~~~~~~~~~~~

**Export to JSON**

Export data to console:

.. code:: bash

   barangay export --model flat --format json

Save data to a file:

.. code:: bash

   barangay export --model flat --format json --output data.json

**Export to CSV**

Export data in CSV format:

.. code:: bash

   barangay export --model flat --format csv --output data.csv

**Export Historical Data**

Export data from a specific date:

.. code:: bash

   barangay export --as-of 2025-07-08 --model flat --output historical_data.json

**Export Different Data Models**

Export the extended model:

.. code:: bash

   barangay export --model extended --output extended.json

Export the basic model:

.. code:: bash

   barangay export --model basic --output basic.json

**Export Historical Data**

Export historical data to a file:

.. code:: bash

   barangay history export --as-of 2025-07-08 --model flat --output historical.json

Info Commands
~~~~~~~~~~~~~

**Show Current Version**

Check the current data version:

.. code:: bash

   barangay info version

Output:

.. code:: text

   Current version: 2026-01-13
   Available dates: 2025-07-08, 2025-08-29, 2025-10-13

**Show Data Statistics**

Get statistics about the data:

.. code:: bash

   barangay info stats

Output:

.. code:: text

   ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
   ┃ Model          ┃ Count   ┃
   ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
   │ Basic (nested) │ 42,077  │
   │ Flat (list)    │ 42,077  │
   │ Extended       │ 42,077  │
   ┗━━━━━━━━━━━━━━━━┻━━━━━━━━━┛

**List All Regions**

List all available regions:

.. code:: bash

   barangay info list-regions

**List Municipalities in a Region**

List all municipalities in a specific region:

.. code:: bash

   barangay info list-municipalities "National Capital Region (NCR)"

**List Barangays in a Municipality**

List all barangays in a specific municipality:

.. code:: bash

   barangay info list-barangays "Quezon City"

Cache Commands
~~~~~~~~~~~~~~

**Show Cache Information**

View cache directory and contents:

.. code:: bash

   barangay cache info

**Clear Cache**

Remove all cached data:

.. code:: bash

   barangay cache clear

**Download Data to Cache**

Download current data:

.. code:: bash

   barangay cache download

Download specific historical data:

.. code:: bash

   barangay cache download --date 2025-07-08

Batch Commands
~~~~~~~~~~~~~~

**Batch Search from File**

Create a file with one query per line:

.. code:: bash

   cat queries.txt
   Tongmageng
   San Jose
   Quezon City
   Manila

Run batch search:

.. code:: bash

   barangay batch search queries.txt

Save results to file:

.. code:: bash

   barangay batch search queries.txt --output results.json

Batch search with custom parameters:

.. code:: bash

   barangay batch search queries.txt --limit 3 --threshold 70

**Batch Validate Barangay Names**

Create a file with barangay names to validate:

.. code:: bash

   cat barangays.txt
   Tongmageng
   San Jose
   Invalid Barangay Name

Run validation:

.. code:: bash

   barangay batch validate barangays.txt

Output:

.. code:: text

   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃ Barangay    ┃ Status      ┃ Match                    ┃
   ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ Tongmageng  │ Valid       │ Tongmageng               │
   │ San Jose    │ Valid       │ San Jose                 │
   │ Invalid...  │ Not found   │ -                        │
   ┗━━━━━━━━━━━━━━┻━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━┛

Common Workflows
----------------

Address Lookup for Delivery Services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quick lookup of a barangay:

.. code:: bash

   barangay search "Tongmageng"

Lookup with more context for better accuracy:

.. code:: bash

   barangay search "Tongmageng, Tawi-Tawi" --threshold 85

For critical delivery validation, use a high threshold:

.. code:: bash

   barangay search "Tongmageng" --threshold 90

Batch validate multiple addresses:

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

Data Export for Analytics
~~~~~~~~~~~~~~~~~~~~~~~~~

Export flat model to CSV for spreadsheet analysis:

.. code:: bash

   barangay export --model flat --format csv --output barangay_data.csv

Export to JSON for programming:

.. code:: bash

   barangay export --model flat --format json --output barangay_data.json

Export specific historical snapshot:

.. code:: bash

   barangay export --as-of 2025-07-08 --model flat --output snapshot_2025-07-08.json

Export extended model for hierarchical analysis:

.. code:: bash

   barangay export --model extended --format json --output barangay_extended.json

Export multiple historical snapshots for trend analysis:

.. code:: bash

   barangay export --as-of 2025-07-08 --model flat --output snapshot_2025_07_08.json
   barangay export --as-of 2025-08-29 --model flat --output snapshot_2025_08_29.json
   barangay export --as-of 2025-10-13 --model flat --output snapshot_2025_10_13.json

Data Exploration and Research
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the current data version:

.. code:: bash

   barangay info version

View data statistics:

.. code:: bash

   barangay info stats

List all regions to understand the geographic coverage:

.. code:: bash

   barangay info list-regions

List municipalities in a specific region:

.. code:: bash

   # Explore NCR
   barangay info list-municipalities "NCR"

   # Explore a region
   barangay info list-municipalities "Region I - Ilocos Region"

List barangays in a municipality:

.. code:: bash

   # Explore Quezon City
   barangay info list-barangays "Quezon City"

   # Explore a municipality
   barangay info list-barangays "City of Manila"

Search for barangays with specific names:

.. code:: bash

   # Search for barangays with "San" in the name
   barangay search "San" --limit 20

   # Search for barangays with "1" in the name
   barangay search "Barangay 1" --limit 20

Data Cleaning and Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate a single address with high confidence:

.. code:: bash

   barangay search "Tongmageng" --threshold 90 --format json

Batch validate a list of addresses:

.. code:: bash

   cat > addresses_to_validate.txt << EOF
   Tongmageng
   San Jose
   Quezon City
   Invalid Barangay Name
   Typo Barangay
   EOF

   barangay batch validate addresses_to_validate.txt

Search with lower threshold to find potential matches for typos:

.. code:: bash

   barangay search "Tongmagen" --threshold 70 --limit 5

Export validated data for further processing:

.. code:: bash

   barangay batch search addresses_to_validate.txt --output validated_results.json

Integration with Shell Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Cache Management for Offline Use
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the current data for offline use:

.. code:: bash

   barangay cache download

Download specific historical data:

.. code:: bash

   barangay cache download --date 2025-07-08
   barangay cache download --date 2025-08-29
   barangay cache download --date 2025-10-13

Once data is cached, you can use it offline:

.. code:: bash

   # Search using cached data
   barangay search "Tongmageng"

   # Export using cached data
   barangay export --model flat --output offline_data.json

Integration with Other Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Process JSON output with jq:

.. code:: bash

   # Extract specific fields
   barangay search "Tongmageng" --format json | jq '.[] | {barangay, municipality, province: .province_or_huc, psgc_id}'

   # Filter by score
   barangay search "San Jose" --format json | jq '.[] | select([.f_000b_ratio_score, .f_0p0b_ratio_score, .f_00mb_ratio_score, .f_0pmb_ratio_score] | max > 80)'

   # Count results
   barangay search "San Jose" --format json | jq 'length'

Filter table output with grep:

.. code:: bash

   # Search for specific province
   barangay search "San Jose" --format table | grep "Tawi-Tawi"

   # Count matches
   barangay search "San Jose" --format table | grep -c "San Jose"

Export to CSV for database import:

.. code:: bash

   barangay export --model flat --format csv --output barangay_import.csv

Data Migration and Backup
~~~~~~~~~~~~~~~~~~~~~~~~~

Create backup directory and export all models:

.. code:: bash

   mkdir -p barangay_backup

   # Export all models
   barangay export --model basic --format json --output barangay_backup/basic.json
   barangay export --model flat --format json --output barangay_backup/flat.json
   barangay export --model extended --format json --output barangay_backup/extended.json

   # Export historical snapshots
   for date in 2025-07-08 2025-08-29 2025-10-13; do
       barangay export --as-of "$date" --model flat --format json --output "barangay_backup/snapshot_$date.json"
   done

Export data in a format suitable for another system:

.. code:: bash

   # Export to CSV for spreadsheet systems
   barangay export --model flat --format csv --output migration_data.csv

   # Export to JSON for NoSQL databases
   barangay export --model extended --format json --output migration_data.json

Tips and Best Practices
-----------------------

Choosing the Right Threshold

* **High confidence (85-100)**: Use for critical applications where accuracy is paramount
* **Balanced (70-84)**: Good default for most use cases
* **Inclusive (60-69)**: Use when you want more options or are exploring
* **Exploratory (<60)**: Use for debugging or research purposes

Example:

.. code:: bash

   # Critical validation
   barangay search "Tongmageng" --threshold 90

   # General use
   barangay search "Tongmageng" --threshold 70

   # Exploratory
   barangay search "Tongmageng" --threshold 50

Selecting the Right Data Model

* **flat**: Best for data analysis, CSV export, and most use cases
* **extended**: Best when you need the complete hierarchical structure
* **basic**: Simple nested structure for basic use cases

Example:

.. code:: bash

   # For data analysis
   barangay export --model flat --format csv --output data.csv

   # For complete hierarchy
   barangay export --model extended --output data.json

   # For simple use
   barangay export --model basic --output data.json

Optimizing Batch Operations

* Use appropriate thresholds to reduce processing time
* Limit results per query to avoid large outputs
* Save results to files for later analysis

Example:

.. code:: bash

   # Efficient batch search
   barangay batch search queries.txt --limit 3 --threshold 70 --output results.json

Working with Historical Data

* Always check available dates first
* Use specific dates for reproducible results
* Export historical snapshots for offline analysis

Example:

.. code:: bash

   # Check available dates
   barangay history list-dates

   # Use specific date for reproducibility
   barangay history search "Tongmageng" --as-of 2025-07-08

   # Export snapshot
   barangay history export --as-of 2025-07-08 --output snapshot.json

Cache Management for Performance

* Download data once for offline use
* Clear cache periodically to free disk space
* Check cache info to monitor usage

Example:

.. code:: bash

   # Download for offline use
   barangay cache download

   # Monitor cache usage
   barangay cache info

   # Clear when needed
   barangay cache clear

Output Format Selection

* **table**: Best for human-readable output (default)
* **json**: Best for programmatic processing and integration

Example:

.. code:: bash

   # Human-readable
   barangay search "Tongmageng" --format table

   # Programmatic
   barangay search "Tongmageng" --format json | jq '.[].psgc_id'

Troubleshooting
---------------

No Results Found

If you get no results:

.. code:: bash

   # Try lowering the threshold
   barangay search "query" --threshold 50

   # Try partial matches
   barangay search "partial query"

   # Check if the spelling is correct
   barangay info list-regions | grep -i "region name"

Cache Issues

If you encounter cache-related errors:

.. code:: bash

   # Check cache status
   barangay cache info

   # Clear and rebuild cache
   barangay cache clear
   barangay cache download

Historical Data Not Found

If historical data is not available:

.. code:: bash

   # Check available dates
   barangay history list-dates

   # Use a valid date
   barangay history search "query" --as-of 2025-07-08

Batch Processing Errors

If batch processing fails:

.. code:: bash

   # Check file format (one query per line)
   cat queries.txt

   # Try with a smaller file
   head -10 queries.txt > test_queries.txt
   barangay batch search test_queries.txt