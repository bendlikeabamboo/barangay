###################
  CLI Module
############

The CLI module provides a command-line interface for the barangay package,
built using the Click framework. It offers convenient access to all package
functionality including search, export, data information, historical data
access, cache management, and batch processing.


 Overview
 *********

The CLI module is organized into several command groups:

* **Main Commands**: ``search`` and ``export`` for core functionality
* **Info Group**: Commands for displaying data information and listings
* **History Group**: Commands for accessing historical data
* **Cache Group**: Commands for managing cached data
* **Batch Group**: Commands for batch processing operations

The CLI uses the Click framework for command parsing and the Rich library
for formatted console output.


 API Reference
 **************

Main Commands
=============

.. autofunction:: barangay.cli.search_cmd
.. autofunction:: barangay.cli.export

Info Group
==========

.. autofunction:: barangay.cli.version
.. autofunction:: barangay.cli.stats
.. autofunction:: barangay.cli.list_regions
.. autofunction:: barangay.cli.list_municipalities
.. autofunction:: barangay.cli.list_barangays

History Group
=============

.. autofunction:: barangay.cli.list_dates
.. autofunction:: barangay.cli.search_history
.. autofunction:: barangay.cli.export_history

Cache Group
===========

.. autofunction:: barangay.cli.clear
.. autofunction:: barangay.cli.info
.. autofunction:: barangay.cli.download

Batch Group
===========

.. autofunction:: barangay.cli.batch_search
.. autofunction:: barangay.cli.validate


 Internal Functions
 ==================

These functions are used internally by the CLI module:

.. autofunction:: barangay.cli._dict_to_csv
.. autofunction:: barangay.cli._nested_to_csv


 Command Groups
 ==============

The following Click command groups organize related commands:

.. autofunction:: barangay.cli.app
.. autofunction:: barangay.cli.info
.. autofunction:: barangay.cli.history
.. autofunction:: barangay.cli.cache
.. autofunction:: barangay.cli.batch


 Examples
 *********

Basic Search
============

Search for a barangay:

.. code:: bash

   barangay search "Tongmageng"

Search with custom parameters:

.. code:: bash

   barangay search "San Jose" --limit 10 --threshold 70

Search with JSON output:

.. code:: bash

   barangay search "Tongmageng" --format json

Data Export
===========

Export to JSON file:

.. code:: bash

   barangay export --model flat --format json --output data.json

Export to CSV:

.. code:: bash

   barangay export --model flat --format csv --output data.csv

Export historical data:

.. code:: bash

   barangay export --as-of 2025-07-08 --model flat --output historical.json

Data Information
================

Show current version:

.. code:: bash

   barangay info version

Show data statistics:

.. code:: bash

   barangay info stats

List all regions:

.. code:: bash

   barangay info list-regions

List municipalities in a region:

.. code:: bash

   barangay info list-municipalities "NCR"

List barangays in a municipality:

.. code:: bash

   barangay info list-barangays "Quezon City"

Historical Data
===============

List available historical dates:

.. code:: bash

   barangay history list-dates

Search historical data:

.. code:: bash

   barangay history search "Tongmageng" --as-of 2025-07-08

Export historical data:

.. code:: bash

   barangay history export --as-of 2025-07-08 --model flat --output historical.json

Cache Management
================

Show cache information:

.. code:: bash

   barangay cache info

Clear cache:

.. code:: bash

   barangay cache clear

Download data to cache:

.. code:: bash

   barangay cache download

Download specific historical data:

.. code:: bash

   barangay cache download --date 2025-07-08

Batch Processing
================

Batch search from file:

.. code:: bash

   barangay batch search queries.txt

Batch search with output file:

.. code:: bash

   barangay batch search queries.txt --output results.json

Batch validate barangay names:

.. code:: bash

   barangay batch validate barangays.txt


 Command Reference
 *****************

Search Command
==============

**Usage**:

.. code:: bash

   barangay search QUERY [OPTIONS]

**Arguments**:

* ``QUERY``: Search string (required)

**Options**:

* ``--limit, -l INTEGER``: Maximum number of results (default: 5)
* ``--threshold, -t FLOAT``: Minimum similarity score 0-100 (default: 60.0)
* ``--as-of TEXT``: Historical date (YYYY-MM-DD)
* ``--format, -f [json|table]``: Output format (default: table)

**Description**:

Performs fuzzy search for barangays using the search function. Results are
displayed in a formatted table or JSON format depending on the ``--format``
option.

**Examples**:

.. code:: bash

   # Basic search
   barangay search "Tongmageng"

   # Search with custom limit
   barangay search "San Jose" --limit 10

   # Search with high threshold
   barangay search "Tongmageng" --threshold 85

   # Search historical data
   barangay search "Tongmageng" --as-of 2025-07-08

   # JSON output
   barangay search "Tongmageng" --format json


 Export Command
 ==============

 **Usage**:

 .. code:: bash

    barangay export [OPTIONS]

 **Options**:

 * ``--model [flat|extended|basic]``: Data model (default: flat)
 * ``--format, -f [json|csv]``: Output format (default: json)
 * ``--output, -o TEXT``: Output file (default: stdout)
 * ``--as-of TEXT``: Historical date (YYYY-MM-DD)

 **Description**:

 Exports barangay data to JSON or CSV format. The ``--model`` option selects
 the data structure to export. Use ``--output`` to save to a file, or omit
 to print to stdout.

 **Examples**:

 .. code:: bash

    # Export to JSON (stdout)
    barangay export --model flat --format json

    # Export to JSON file
    barangay export --model flat --format json --output data.json

    # Export to CSV
    barangay export --model flat --format csv --output data.csv

    # Export historical data
    barangay export --as-of 2025-07-08 --model flat --output historical.json

    # Export extended model
    barangay export --model extended --output extended.json


 Info Version Command
 ====================

 **Usage**:

 .. code:: bash

    barangay info version

 **Description**:

 Displays the current data version and a list of all available historical
 dates.

 **Examples**:

 .. code:: bash

    barangay info version

 **Output**:

 .. code:: text

    Current version: 2026-01-13
    Available dates: 2025-07-08, 2025-08-29, 2025-10-13


 Info Stats Command
 ===================

 **Usage**:

 .. code:: bash

    barangay info stats

 **Description**:

 Shows statistics about the data, including the count of records in each
 data model (basic, flat, extended).

 **Examples**:

 .. code:: bash

    barangay info stats

 **Output**:

 .. code:: text

    ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
    ┃ Model          ┃ Count   ┃
    ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
    │ Basic (nested) │ 42,077  │
    │ Flat (list)    │ 42,077  │
    │ Extended       │ 42,077  │
    └────────────────┴─────────┘


 Info List-Regions Command
 =========================

 **Usage**:

 .. code:: bash

    barangay info list-regions

 **Description**:

 Lists all available regions in the dataset.

 **Examples**:

 .. code:: bash

    barangay info list-regions


 Info List-Municipalities Command
 ================================

 **Usage**:

 .. code:: bash

    barangay info list-municipalities REGION

 **Arguments**:

 * ``REGION``: Region name (required)

 **Description**:

 Lists all municipalities/cities within a specified region.

 **Examples**:

 .. code:: bash

    # List municipalities in NCR
    barangay info list-municipalities "NCR"

    # List municipalities in a region
    barangay info list-municipalities "Region I - Ilocos Region"


 Info List-Barangays Command
 ============================

 **Usage**:

 .. code:: bash

    barangay info list-barangays MUNICIPALITY

 **Arguments**:

 * ``MUNICIPALITY``: Municipality/city name (required)

 **Description**:

 Lists all barangays within a specified municipality. The municipality
 name must be unique across all regions.

 **Examples**:

 .. code:: bash

    # List barangays in Quezon City
    barangay info list-barangays "Quezon City"

    # List barangays in a municipality
    barangay info list-barangays "City of Manila"


 History List-Dates Command
 ==========================

 **Usage**:

 .. code:: bash

    barangay history list-dates

 **Description**:

 Lists all available historical data dates, including the current version.

 **Examples**:

 .. code:: bash

    barangay history list-dates

 **Output**:

 .. code:: text

    ┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
    ┃ Date          ┃ Type         ┃
    ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
    │ 2025-07-08    │ Historical   │
    │ 2025-08-29    │ Historical   │
    │ 2025-10-13    │ Historical   │
    │ 2026-01-13    │ Current     │
    └───────────────┴──────────────┘


 History Search Command
 =======================

 **Usage**:

 .. code:: bash

    barangay history search QUERY [OPTIONS]

 **Arguments**:

 * ``QUERY``: Search string (required)

 **Options**:

 * ``--as-of TEXT``: Historical date (required, YYYY-MM-DD)
 * ``--limit, -l INTEGER``: Maximum number of results (default: 5)
 * ``--threshold, -t FLOAT``: Minimum similarity score 0-100 (default: 60.0)
 * ``--format, -f [json|table]``: Output format (default: table)

 **Description**:

 Performs fuzzy search on historical data from a specific date. The
 ``--as-of`` option is required and must be a valid historical date.

 **Examples**:

 .. code:: bash

    # Search historical data
    barangay history search "Tongmageng" --as-of 2025-07-08

    # Search with custom parameters
    barangay history search "San Jose" --as-of 2025-07-08 --limit 10 --threshold 70

    # JSON output
    barangay history search "Tongmageng" --as-of 2025-07-08 --format json


 History Export Command
 ======================

 **Usage**:

 .. code:: bash

    barangay history export [OPTIONS]

 **Options**:

 * ``--as-of TEXT``: Historical date (required, YYYY-MM-DD)
 * ``--model [flat|extended|basic]``: Data model (default: flat)
 * ``--format, -f [json|csv]``: Output format (default: json)
 * ``--output, -o TEXT``: Output file (default: stdout)

 **Description**:

 Exports historical data from a specific date. The ``--as-of`` option is
 required and must be a valid historical date.

 **Examples**:

 .. code:: bash

    # Export historical data
    barangay history export --as-of 2025-07-08 --model flat --output historical.json

    # Export historical data to CSV
    barangay history export --as-of 2025-07-08 --model flat --format csv --output historical.csv


 Cache Clear Command
 ====================

 **Usage**:

 .. code:: bash

    barangay cache clear

 **Description**:

 Clears the cache directory, removing all cached data files.

 **Examples**:

 .. code:: bash

    barangay cache clear


 Cache Info Command
 ==================

 **Usage**:

 .. code:: bash

    barangay cache info

 **Description**:

 Displays information about the cache directory, including its location,
 number of files, total size, and a list of cached files.

 **Examples**:

 .. code:: bash

    barangay cache info

 **Output**:

 .. code:: text

    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ Property                                                ┃
    ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
    │ Cache directory    │ /home/user/.cache/barangay         │
    │ Files              │ 3                                  │
    │ Total size         │ 12.45 MB                           │
    │                    │                                    │
    │ Cached files       │                                    │
    │                    │ barangay_2025-07-08.json (4.12 MB) │
    │                    │ barangay_2025-08-29.json (4.18 MB) │
    │                    │ barangay_2025-10-13.json (4.15 MB) │
    └─────────────────────────────────────────────────────────┘


 Cache Download Command
 ======================

 **Usage**:

 .. code:: bash

    barangay cache download [OPTIONS]

 **Options**:

 * ``--date TEXT``: Date to download (YYYY-MM-DD, optional)

 **Description**:

 Downloads data to the cache directory. If ``--date`` is specified, downloads
 historical data from that date. Otherwise, downloads the current data.

 **Examples**:

 .. code:: bash

    # Download current data
    barangay cache download

    # Download specific historical data
    barangay cache download --date 2025-07-08


 Batch Search Command
 ====================

 **Usage**:

 .. code:: bash

    barangay batch search FILE [OPTIONS]

 **Arguments**:

 * ``FILE``: Input file path (required, must exist)

 **Options**:

 * ``--limit, -l INTEGER``: Maximum number of results per query (default: 5)
 * ``--threshold, -t FLOAT``: Minimum similarity score 0-100 (default: 60.0)
 * ``--as-of TEXT``: Historical date (YYYY-MM-DD)
 * ``--output, -o TEXT``: Output JSON file (default: stdout)

 **Description**:

 Performs batch search from a file containing one query per line. Results
 are returned as a JSON object mapping each query to its search results.

 **Examples**:

 .. code:: bash

    # Batch search from file
    barangay batch search queries.txt

    # Save results to file
    barangay batch search queries.txt --output results.json

    # Batch search with custom parameters
    barangay batch search queries.txt --limit 3 --threshold 70

 **Input File Format**:

 The input file should contain one query per line:

 .. code:: text

    Tongmageng
    San Jose
    Quezon City
    Manila

 **Output Format**:

 Results are returned as a JSON object:

 .. code:: json

    {
      "Tongmageng": [
        {
          "barangay": "Tongmageng",
          "municipality_or_city": "Sitangkai",
          "province_or_huc": "Tawi-Tawi",
          "psgc_id": "157501001",
          "f_000b_ratio_score": 95.2,
          "f_0p0b_ratio_score": 0.0,
          "f_00mb_ratio_score": 95.2,
          "f_0pmb_ratio_score": 95.2
        }
      ],
      "San Jose": [...]
    }


 Batch Validate Command
 ======================

 **Usage**:

 .. code:: bash

    barangay batch validate FILE

 **Arguments**:

 * ``FILE``: Input file path (required, must exist)

 **Description**:

 Validates barangay names from a file containing one name per line. Each
 name is searched with a high threshold (95.0) to determine if it's valid.

 **Examples**:

 .. code:: bash

    # Validate barangay names
    barangay batch validate barangays.txt

 **Input File Format**:

 The input file should contain one barangay name per line:

 .. code:: text

    Tongmageng
    San Jose
    Invalid Barangay Name

 **Output**:

 Results are displayed in a table showing the status of each barangay name:

 .. code:: text

    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ Barangay    ┃ Status      ┃ Match                    ┃
    ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩
    │ Tongmageng  │ Valid       │ Tongmageng               │
    │ San Jose    │ Valid       │ San Jose                 │
    │ Invalid...  │ Not found   │ -                        │
    └──────────────┴─────────────┴───────────────────────────┘


 See Also
 *********

 * :mod:`barangay.search` - Search functionality
 * :mod:`barangay.data_manager` - Data management
 * :mod:`barangay.fuzz` - Fuzzy matching
 * :doc:`../user_guide/cli` - CLI user guide
 * :doc:`../examples/cli` - CLI usage examples