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

Get more results and only high-confidence matches:

.. code:: bash

   barangay search "San Jose" --limit 10 --threshold 85

Output:

.. code:: txt

                        Search Results for 'San Jose'
   ┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
   ┃ Barangay      ┃ Municipality/City ┃ Province/HUC   ┃ PSGC ID    ┃ Score ┃
   ┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
   │ Iba           │ San Jose          │ Tarlac         │ 0306918003 │ 80.0  │
   │ Da-o          │ San Jose          │ Northern Samar │ 0804819007 │ 80.0  │
   │ Aya           │ San Jose          │ Batangas       │ 0401022003 │ 80.0  │
   │ San Jose      │ Oas               │ Albay          │ 0500512045 │ 80.0  │
   │ San Jose      │ Tuy               │ Batangas       │ 0401034019 │ 80.0  │
   │ Pao           │ San Jose          │ Tarlac         │ 0306918010 │ 80.0  │
   │ San Jose      │ Goa               │ Camarines Sur  │ 0501715027 │ 80.0  │
   │ San Jose      │                   │ City of Cebu   │ 0730600067 │ 76.2  │
   │ San Jose Pob. │ Catmon            │ Cebu           │ 0702216018 │ 76.2  │
   │ San Jose      │ Borbon            │ Cebu           │ 0702213017 │ 76.2  │
   └───────────────┴───────────────────┴────────────────┴────────────┴───────┘

Search using data from a specific date:

.. code:: bash

   barangay search "Villa Floresta, San Jose City" --as-of 2025-08-22

Output:

.. code:: txt

            Search Results for 'Villa Floresta, San Jose City'
   ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
   ┃ Barangay       ┃ Municipality/City ┃ Province/HUC  ┃ PSGC ID    ┃ Score ┃
   ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
   │ Villa Floresca │ San Jose City     │ Nueva Ecija   │ 0304926040 │ 95.7  │
   │ San Jose       │ Flora             │ Apayao        │ 1408103015 │ 75.7  │
   │ Villa Aglipay  │ San Jose          │ Tarlac        │ 0306918013 │ 75.6  │
   │ Villa Joson    │ San Jose City     │ Nueva Ecija   │ 0304926016 │ 74.4  │
   │ Villa Flores   │ Santa Fe          │ Nueva Vizcaya │ 0205012012 │ 72.7  │
   └────────────────┴───────────────────┴───────────────┴────────────┴───────┘

Get results in JSON format:

.. code:: bash

   barangay search "Tongmageng" --limit 1 --format json

Output:

.. code:: txt

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
      }
   ]

**Historical Search**

Search for barangays in historical data:

.. code:: bash

   barangay history search-history "Villa Floresta, San Jose City" --as-of 2025-08-22

Output:

.. code:: txt

      Search Results for 'Villa Floresta, San Jose City' (as of 2025-08-22)
   ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
   ┃ Barangay       ┃ Municipality/City ┃ Province/HUC  ┃ PSGC ID    ┃ Score ┃
   ┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
   │ Villa Floresca │ San Jose City     │ Nueva Ecija   │ 0304926040 │ 95.7  │
   │ San Jose       │ Flora             │ Apayao        │ 1408103015 │ 75.7  │
   │ Villa Aglipay  │ San Jose          │ Tarlac        │ 0306918013 │ 75.6  │
   │ Villa Joson    │ San Jose City     │ Nueva Ecija   │ 0304926016 │ 74.4  │
   │ Villa Flores   │ Santa Fe          │ Nueva Vizcaya │ 0205012012 │ 72.7  │
   └────────────────┴───────────────────┴───────────────┴────────────┴───────┘

List available historical dates:

.. code:: bash

   barangay history list-dates

Output:

.. code:: txt

   Available Historical Dates
   ┏━━━━━━━━━━━━┳━━━━━━━━━━━━┓
   ┃ Date       ┃ Type       ┃
   ┡━━━━━━━━━━━━╇━━━━━━━━━━━━┩
   │ 2025-07-08 │ Historical │
   │ 2025-08-29 │ Historical │
   │ 2025-10-13 │ Historical │
   │ 2026-01-13 │ Historical │
   │ 2026-01-13 │ Current    │
   └────────────┴────────────┘


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

   barangay export --as-of 2025-07-08 --model flat --output historical.json

Info Commands
~~~~~~~~~~~~~

**Show Current Version**

Check the current data version:

.. code:: bash

   barangay info version

Output:

.. code:: text

   Current version: 2026-01-13
   Available dates: 2025-08-29, 2025-07-08, 2025-10-13, 2026-01-13

**Show Data Statistics**

Get statistics about the data:

.. code:: bash

   barangay info stats

Output:

.. code:: text

        Data Statistics
   ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
   ┃ Model                ┃ Count ┃
   ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
   │ Basic (nested)       │ 1655  │
   │ Flat (list)          │ 43769 │
   │ Extended (recursive) │ 6     │
   └──────────────────────┴───────┘

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

   cat <<EOF > queries.txt
   Tongmageng
   San Jose
   Makati
   Rosario
   EOF

Run batch search:

.. code:: bash

   barangay batch batch-search queries.txt

Save results to file:

.. code:: bash

   barangay batch batch-search queries.txt --output results.json

Batch search with custom parameters:

.. code:: bash

   barangay batch batch-search queries.txt --limit 3 --threshold 70


Data Export
~~~~~~~~~~~

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
