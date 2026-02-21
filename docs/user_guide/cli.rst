CLI User Guide
==============

This guide provides comprehensive information about using the barangay command-line interface (CLI). The CLI offers quick and convenient access to all barangay package functionality without writing Python code.

Introduction
------------

The barangay CLI is built using the Click framework and provides 14 commands organized into 6 command groups:

* **Main Commands**: Core search and export functionality
* **Info Group**: Data information and listing commands
* **History Group**: Historical data operations
* **Cache Group**: Cache management commands
* **Batch Group**: Batch processing commands

Installation and Basic Usage
----------------------------

Installation
~~~~~~~~~~~~

The CLI is automatically installed when you install the barangay package:

.. code:: bash

   pip install barangay

Basic Usage
~~~~~~~~~~~

After installation, the CLI is available as ``barangay``:

.. code:: bash

   # Show help
   barangay --help

   # Show version
   barangay --version

   # Get help for a specific command
   barangay search --help

Command Overview
----------------

Main Commands
~~~~~~~~~~~~~

**search** - Fuzzy search for barangays

.. code:: bash

   barangay search QUERY [OPTIONS]

Options:

* ``--limit, -l``: Maximum number of results (default: 5)
* ``--threshold, -t``: Minimum similarity score 0-100 (default: 60.0)
* ``--as-of``: Historical date (YYYY-MM-DD)
* ``--format, -f``: Output format - json or table (default: table)

**export** - Export data to JSON/CSV

.. code:: bash

   barangay export [OPTIONS]

Options:

* ``--model``: Data model - flat, extended, or basic (default: flat)
* ``--format, -f``: Output format - json or csv (default: json)
* ``--output, -o``: Output file (default: stdout)
* ``--as-of``: Historical date (YYYY-MM-DD)

Info Group
~~~~~~~~~~

**info version** - Show current data version

.. code:: bash

   barangay info version

**info stats** - Show data statistics

.. code:: bash

   barangay info stats

**info list-regions** - List all regions

.. code:: bash

   barangay info list-regions

**info list-municipalities** - List municipalities in a region

.. code:: bash

   barangay info list-municipalities REGION

**info list-barangays** - List barangays in a municipality

.. code:: bash

   barangay info list-barangays MUNICIPALITY

History Group
~~~~~~~~~~~~~

**history list-dates** - List available historical dates

.. code:: bash

   barangay history list-dates

**history search** - Search historical data

.. code:: bash

   barangay history search QUERY [OPTIONS]

Options:

* ``--as-of``: Historical date (required, YYYY-MM-DD)
* ``--limit, -l``: Maximum number of results (default: 5)
* ``--threshold, -t``: Minimum similarity score 0-100 (default: 60.0)
* ``--format, -f``: Output format - json or table (default: table)

**history export** - Export historical data

.. code:: bash

   barangay history export [OPTIONS]

Options:

* ``--as-of``: Historical date (required, YYYY-MM-DD)
* ``--model``: Data model - flat, extended, or basic (default: flat)
* ``--format, -f``: Output format - json or csv (default: json)
* ``--output, -o``: Output file (default: stdout)

Cache Group
~~~~~~~~~~~

**cache clear** - Clear cache directory

.. code:: bash

   barangay cache clear

**cache info** - Show cache information

.. code:: bash

   barangay cache info

**cache download** - Download data to cache

.. code:: bash

   barangay cache download [OPTIONS]

Options:

* ``--date``: Date to download (YYYY-MM-DD, optional)

Batch Group
~~~~~~~~~~~

**batch search** - Batch search from file

.. code:: bash

   barangay batch search FILE [OPTIONS]

Options:

* ``--limit, -l``: Maximum number of results per query (default: 5)
* ``--threshold, -t``: Minimum similarity score 0-100 (default: 60.0)
* ``--as-of``: Historical date (YYYY-MM-DD)
* ``--output, -o``: Output JSON file (default: stdout)

**batch validate** - Validate barangay names from file

.. code:: bash

   barangay batch validate FILE

Detailed Command Examples
-------------------------

Search Command
~~~~~~~~~~~~~~

Basic Search

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

Search with Custom Limit

Get more results:

.. code:: bash

   barangay search "San Jose" --limit 10

Search with Higher Threshold

Get only high-confidence matches:

.. code:: bash

   barangay search "San Jose" --threshold 85

Search with Historical Data

Search using data from a specific date:

.. code:: bash

   barangay search "Tongmageng" --as-of 2025-07-08

Search with JSON Output

Get results in JSON format:

.. code:: bash

   barangay search "Tongmageng" --format json

Output:

.. code:: json

   [
      {
         "barangay": "Tongmageng",
         "province_or_huc": "Tawi-Tawi",
         "municipality_or_city": "Sitangkai",
         "psgc_id": "1907005010",
         "f_0p0b_ratio_score": 68.96551724137932,
         "f_00mb_ratio_score": 66.66666666666667,
         "f_0pmb_ratio_score": 51.28205128205128,
         "000b": "tongmageng",
         "0p0b": "tawitawi tongmageng",
         "00mb": "sitangkai tongmageng",
         "0pmb": "tawitawi sitangkai tongmageng"
      },
      {
         "barangay": "Bonga",
         "province_or_huc": "Lanao del Sur",
         "municipality_or_city": "Marogong",
         "psgc_id": "1903631006",
         "f_0p0b_ratio_score": 41.379310344827594,
         "f_00mb_ratio_score": 66.66666666666667,
         "f_0pmb_ratio_score": 42.10526315789473,
         "000b": "bonga",
         "0p0b": "lanao del sur bonga",
         "00mb": "marogong bonga",
         "0pmb": "lanao del sur marogong bonga"
      },
      {
         "barangay": "Bubong",
         "province_or_huc": "Lanao del Sur",
         "municipality_or_city": "Maguing",
         "psgc_id": "1903634051",
         "f_0p0b_ratio_score": 33.333333333333336,
         "f_00mb_ratio_score": 66.66666666666667,
         "f_0pmb_ratio_score": 42.10526315789473,
         "000b": "bubong",
         "0p0b": "lanao del sur bubong",
         "00mb": "maguing bubong",
         "0pmb": "lanao del sur maguing bubong"
      },
      {
         "barangay": "Cambong",
         "province_or_huc": "Lanao del Sur",
         "municipality_or_city": "Maguing",
         "psgc_id": "1903634016",
         "f_0p0b_ratio_score": 32.25806451612904,
         "f_00mb_ratio_score": 64.0,
         "f_0pmb_ratio_score": 41.02564102564102,
         "000b": "cambong",
         "0p0b": "lanao del sur cambong",
         "00mb": "maguing cambong",
         "0pmb": "lanao del sur maguing cambong"
      },
      {
         "barangay": "Kamagong",
         "province_or_huc": "Tawi-Tawi",
         "municipality_or_city": "Bongao",
         "psgc_id": "1907002006",
         "f_0p0b_ratio_score": 37.03703703703704,
         "f_00mb_ratio_score": 64.0,
         "f_0pmb_ratio_score": 47.05882352941176,
         "000b": "kamagong",
         "0p0b": "tawitawi kamagong",
         "00mb": "bongao kamagong",
         "0pmb": "tawitawi bongao kamagong"
      }
   ]

Export Command
~~~~~~~~~~~~~~

Export to JSON (stdout)

Export data to console:

.. code:: bash

   barangay export --model flat --format json

Export to JSON File

Save data to a file:

.. code:: bash

   barangay export --model flat --format json --output data.json

Export to CSV

Export data in CSV format:

.. code:: bash

   barangay export --model flat --format csv --output data.csv

Export Historical Data

Export data from a specific date:

.. code:: bash

   barangay export --as-of 2025-07-08 --model flat --output historical_data.json

Export Different Data Models

Export the extended model:

.. code:: bash

   barangay export --model extended --output extended.json

Export the basic model:

.. code:: bash

   barangay export --model basic --output basic.json

Info Commands
~~~~~~~~~~~~~

Show Current Version

Check the current data version:

.. code:: bash

   barangay info version

Output:

.. code:: text

   Current version: 2026-01-13
   Available dates: 2025-07-08, 2025-08-29, 2025-10-13

Show Data Statistics

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

List All Regions

List all available regions:

.. code:: bash

   barangay info list-regions

Output:

.. code:: text

                          Regions
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Region                                                  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Bangsamoro Autonomous Region In Muslim Mindanao (BARMM) │
│ Cordillera Administrative Region (CAR)                  │
│ MIMAROPA Region                                         │
│ National Capital Region (NCR)                           │
│ Negros Island Region (NIR)                              │
│ Region I (Ilocos Region)                                │
│ Region II (Cagayan Valley)                              │
│ Region III (Central Luzon)                              │
│ Region IV-A (CALABARZON)                                │
│ Region IX (Zamboanga Peninsula)                         │
│ Region V (Bicol Region)                                 │
│ Region VI (Western Visayas)                             │
│ Region VII (Central Visayas)                            │
│ Region VIII (Eastern Visayas)                           │
│ Region X (Northern Mindanao)                            │
│ Region XI (Davao Region)                                │
│ Region XII (SOCCSKSARGEN)                               │
│ Region XIII (Caraga)                                    │
└─────────────────────────────────────────────────────────┘

List Municipalities in a Region

List all municipalities in a specific region:

.. code:: bash

   barangay info list-municipalities "National Capital Region (NCR)"

Output:

.. code:: text

      Municipalities in
   National Capital Region
            (NCR)
   ┏━━━━━━━━━━━━━━━━━━━━━┓
   ┃ Municipality/City   ┃
   ┡━━━━━━━━━━━━━━━━━━━━━┩
   │ City of Caloocan    │
   │ City of Las Piñas   │
   │ City of Makati      │
   │ City of Malabon     │
   │ City of Mandaluyong │
   │ City of Manila      │
   │ City of Marikina    │
   │ City of Muntinlupa  │
   │ City of Navotas     │
   │ City of Parañaque   │
   │ City of Pasig       │
   │ City of San Juan    │
   │ City of Taguig      │
   │ City of Valenzuela  │
   │ Pasay City          │
   │ Pateros             │
   │ Quezon City         │
   └─────────────────────┘

List Barangays in a Municipality

List all barangays in a specific municipality:

.. code:: bash

   barangay info list-barangays "Quezon City"

Output:

.. code:: text

   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃ Barangay                                             ┃
   ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ Barangay 1                                           │
   │ Barangay 2                                           │
   │ Barangay 3                                           │
   │ ...                                                  │
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

History Commands
~~~~~~~~~~~~~~~~

List Available Historical Dates

Show all available historical data dates:

.. code:: bash

   barangay history list-dates

Output:

.. code:: text

   ┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
   ┃ Date          ┃ Type         ┃
   ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
   │ 2025-07-08    │ Historical   │
   │ 2025-08-29    │ Historical   │
   │ 2025-10-13    │ Historical   │
   │ 2026-01-13    │ Current     │
   ┗━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━┛

Search Historical Data

Search for barangays in historical data:

.. code:: bash

   barangay history search "Tongmageng" --as-of 2025-07-08

Export Historical Data

Export historical data to a file:

.. code:: bash

   barangay history export --as-of 2025-07-08 --model flat --output historical.json

Cache Commands
~~~~~~~~~~~~~~

Show Cache Information

View cache directory and contents:

.. code:: bash

   barangay cache info

Output:

.. code:: text

   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃ Property                                             ┃
   ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ Cache directory    │ /home/user/.cache/barangay     │
   │ Files               │ 3                              │
   │ Total size          │ 12.45 MB                       │
   │                     │                                │
   │ Cached files        │                                │
   │                     │ barangay_2025-07-08.json (4.12 MB) │
   │                     │ barangay_2025-08-29.json (4.18 MB) │
   │                     │ barangay_2025-10-13.json (4.15 MB) │
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Clear Cache

Remove all cached data:

.. code:: bash

   barangay cache clear

Output:

.. code:: text

   Cache cleared: /home/user/.cache/barangay

Download Data to Cache

Download current data:

.. code:: bash

   barangay cache download

Download specific historical data:

.. code:: bash

   barangay cache download --date 2025-07-08

Batch Commands
~~~~~~~~~~~~~~

Batch Search from File

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

Batch Validate Barangay Names

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

Common Use Cases
----------------

Quick Address Lookup

Quickly find information about a barangay:

.. code:: bash

   # Simple lookup
   barangay search "Tongmageng"

   # With more context
   barangay search "Tongmageng, Tawi-Tawi"

   # With high confidence
   barangay search "Tongmageng" --threshold 90

Data Export for Analysis

Export data for analysis in other tools:

.. code:: bash

   # Export flat model to CSV for spreadsheet analysis
   barangay export --model flat --format csv --output barangay_data.csv

   # Export to JSON for programming
   barangay export --model flat --format json --output barangay_data.json

   # Export specific historical snapshot
   barangay export --as-of 2025-07-08 --model flat --output snapshot_2025-07-08.json

Batch Processing

Process multiple queries efficiently:

.. code:: bash

   # Create query file
   echo -e "Tongmageng\nSan Jose\nQuezon City" > queries.txt

   # Batch search and save results
   barangay batch search queries.txt --output results.json

   # Validate a list of barangay names
   barangay batch validate barangay_list.txt

Data Exploration

Explore the data structure:

.. code:: bash

   # Check data version
   barangay info version

   # View statistics
   barangay info stats

   # List all regions
   barangay info list-regions

   # Explore a specific region
   barangay info list-municipalities "NCR"
   barangay info list-barangays "Quezon City"

Historical Data Analysis

Access historical data for comparison:

.. code:: bash

   # List available historical dates
   barangay history list-dates

   # Search historical data
   barangay history search "Tongmageng" --as-of 2025-07-08

   # Export historical data
   barangay history export --as-of 2025-07-08 --output historical.json

Cache Management

Manage cached data for offline use:

.. code:: bash

   # Check cache status
   barangay cache info

   # Download data for offline use
   barangay cache download

   # Download specific historical data
   barangay cache download --date 2025-07-08

   # Clear cache to free space
   barangay cache clear

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

Next Steps
----------

Now that you understand the CLI, explore these topics:

* :doc:`search` - Learn about fuzzy search in depth
* :doc:`data_models` - Understand the different data models
* :doc:`historical_data` - Learn about historical data access
* :doc:`configuration` - Configure the package for your needs
* :doc:`../examples/cli` - Real-world CLI usage examples

For API reference, see :doc:`../api_reference/cli`.