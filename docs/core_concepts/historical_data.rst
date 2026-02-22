Historical Data
===============

This guide covers accessing and using historical data from previous PSGC (Philippine Standard Geographic Code) releases.

Introduction to Historical Data
-------------------------------

What is Historical Data?
~~~~~~~~~~~~~~~~~~~~~~~~

The Philippine Statistics Authority (PSA) periodically updates the PSGC masterlist to reflect administrative changes such as:

* Creation of new barangays
* Renaming of barangays, cities, or municipalities
* Transfer of barangays between municipalities
* Changes in administrative boundaries

Historical data allows you to:

* Access data as it existed on specific dates
* Track administrative changes over time
* Validate historical addresses
* Perform time-series analysis

Available Dates
~~~~~~~~~~~~~~~

The barangay package provides access to multiple historical datasets. Check available dates:

.. code-block:: python

   from barangay import available_dates

   print("Available dates:")
   for date in sorted(available_dates, reverse=True):
       print(f"  - {date}")

Example output:

.. code-block:: text

   Available dates:
     - 2026-01-13 (current)
     - 2025-10-13
     - 2025-08-29
     - 2025-07-08

.. note:: The current dataset is always bundled with the package. Historical datasets are downloaded on-demand and cached locally.

Why Use Historical Data?
~~~~~~~~~~~~~~~~~~~~~~~~

Common use cases include:

* **Historical Address Validation**: Validate addresses from old records
* **Change Tracking**: Monitor administrative changes over time
* **Data Migration**: Migrate data using historical boundaries
* **Research**: Study administrative evolution
* **Compliance**: Meet regulatory requirements for historical data

Accessing Historical Data
-------------------------

Using the as_of Parameter
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``as_of`` parameter is available in most data loading functions:

.. code-block:: python

   from barangay import search, load_barangay_data, load_barangay_extended_data, load_barangay_flat_data

   # Search with historical data
   results = search("Tongmageng", as_of="2025-07-08")

   # Load basic data from a specific date
   data = load_barangay_data(as_of="2025-07-08")

   # Load extended data from a specific date
   extended_data = load_barangay_extended_data(as_of="2025-07-08")

   # Load flat data from a specific date
   flat_data = load_barangay_flat_data(as_of="2025-07-08")

Module-Level as_of Attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set a default ``as_of`` date for the entire session:

.. code-block:: python

   import barangay

   # Set default date for this session
   barangay.as_of = "2025-07-08"

   # All subsequent operations use this date
   results = barangay.search("Tongmageng")
   data = barangay.load_barangay_data()

   # Reset to latest data
   barangay.as_of = None

Environment Variable Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set a default date using environment variables:

.. code-block:: bash

   # Set environment variable
   export BARANGAY_AS_OF="2025-07-08"

Then in Python:

.. code-block:: python

   from barangay import search

   # Uses BARANGAY_AS_OF environment variable
   results = search("Tongmageng")

Date Resolution
---------------

Exact Date Matching
~~~~~~~~~~~~~~~~~~~

If you specify an exact date that matches an available dataset, that dataset is used:

.. code-block:: python

   from barangay import search

   # Exact match - uses 2025-07-08 dataset
   results = search("Tongmageng", as_of="2025-07-08")

Approximate Date Matching
~~~~~~~~~~~~~~~~~~~~~~~~~

If you specify a date that doesn't match an available dataset, the package automatically resolves to the closest available dataset on or before the requested date:

.. code-block:: python

   from barangay import search, resolve_date

   # Request date between available datasets
   requested_date = "2025-08-15"

   # Resolve to closest available date
   from barangay import get_available_dates
   available = get_available_dates() + [barangay.current]
   resolved_date, message = resolve_date(requested_date, available, barangay.current)

   print(f"Requested: {requested_date}")
   print(f"Resolved: {resolved_date}")
   print(f"Message: {message}")

Output:

.. code-block:: text

   Requested: 2025-08-15
   Resolved: 2025-08-29
   Message: Using 2025-08-29 dataset (closest on or before 2025-08-15)

Resolution Priority Order
~~~~~~~~~~~~~~~~~~~~~~~~~

The package resolves dates in the following priority order:

1. **Exact match**: If the requested date matches an available dataset exactly
2. **Closest before**: If no exact match, use the closest dataset on or before the requested date
3. **Latest**: If the requested date is after all available datasets, use the latest

.. code-block:: python

   from barangay import search, resolve_date, get_available_dates, current

   available = get_available_dates() + [current]

   # Test different dates
   test_dates = [
       "2025-06-01",  # Before first available
       "2025-07-08",  # Exact match
       "2025-08-15",  # Between available dates
       "2025-09-01",  # Between available dates
       "2026-02-01",  # After all available
   ]

   for date in test_dates:
       resolved, message = resolve_date(date, available, current)
       print(f"{date} → {resolved} ({message})")

Available Dates List
~~~~~~~~~~~~~~~~~~~~

Get a list of all available historical dates:

.. code-block:: python

   from barangay import get_available_dates, current

   # Get historical dates (excluding current)
   historical_dates = get_available_dates()
   print(f"Historical dates: {len(historical_dates)}")

   # Get all dates (including current)
   all_dates = historical_dates + [current]
   print(f"All dates: {len(all_dates)}")

   # Display dates
   for date in sorted(all_dates, reverse=True):
       print(f"  - {date}")

Caching Historical Data
-----------------------

How Caching Works
~~~~~~~~~~~~~~~~~

When you request historical data for the first time:

1. The package checks if the data is in the local cache
2. If not cached, it downloads the data from GitHub
3. The downloaded data is saved to the cache directory
4. Subsequent requests use the cached data

Cache Location
~~~~~~~~~~~~~~

The cache directory location depends on your operating system:

* **Windows**: ``%LOCALAPPDATA%\barangay\cache``
* **Linux/Mac with XDG_CACHE_HOME**: ``$XDG_CACHE_HOME/barangay``
* **Linux/Mac fallback**: ``~/.cache/barangay``
* **Custom**: ``$BARANGAY_CACHE_DIR`` if set

Check your cache directory:

.. code-block:: python

   from barangay import get_cache_dir

   cache_dir = get_cache_dir()
   print(f"Cache directory: {cache_dir}")

Cache File Naming
~~~~~~~~~~~~~~~~~

Cached files follow the pattern ``{date}_{filename}``:

* ``2025-07-08_barangay.json``
* ``2025-07-08_barangay_extended.json``
* ``2025-07-08_barangay_flat.json``
* ``2025-07-08_fuzzer_base.parquet``

Cache Management
~~~~~~~~~~~~~~~~

List cached files:

.. code-block:: python

   from pathlib import Path
   from barangay import get_cache_dir

   cache_dir = get_cache_dir()
   cache_files = list(cache_dir.glob("*"))

   print(f"Cached files: {len(cache_files)}")
   for file in sorted(cache_files):
       size_mb = file.stat().st_size / (1024 * 1024)
       print(f"  - {file.name} ({size_mb:.2f} MB)")

Clearing Cache
~~~~~~~~~~~~~~

To clear the cache, delete files from the cache directory:

.. code-block:: python

   from pathlib import Path
   from barangay import get_cache_dir

   cache_dir = get_cache_dir()

   # Delete all cached files
   for file in cache_dir.glob("*"):
       file.unlink()
       print(f"Deleted: {file.name}")

   print("Cache cleared")

.. warning:: Clearing the cache will cause historical data to be re-downloaded on next access, which may take time and bandwidth.

Use Cases
---------

Tracking Administrative Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare data across different dates to track changes:

.. code-block:: python

   from barangay import load_barangay_flat_data
   import pandas as pd

   # Load data from two different dates
   data_july = pd.DataFrame(load_barangay_flat_data(as_of="2025-07-08"))
   data_august = pd.DataFrame(load_barangay_flat_data(as_of="2025-08-29"))

   # Compare total counts
   print(f"Total barangays (July): {len(data_july)}")
   print(f"Total barangays (August): {len(data_august)}")
   print(f"Change: {len(data_august) - len(data_july)}")

   # Find new barangays
   july_set = set(data_july['psgc_id'])
   august_set = set(data_august['psgc_id'])

   new_psgc_ids = august_set - july_set
   new_barangays = data_august[data_august['psgc_id'].isin(new_psgc_ids)]

   print(f"\nNew barangays added: {len(new_barangays)}")
   print(new_barangays[['barangay', 'municipality_or_city', 'province_or_huc']])

Historical Address Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate addresses using historical data:

.. code-block:: python

   from barangay import search

   def validate_historical_address(address, reference_date):
       """Validate an address as it existed on a specific date."""
       results = search(address, as_of=reference_date, threshold=70.0)

       if not results:
           return {
               'valid': False,
               'message': f'No match found for {reference_date}',
               'address': address
           }

       best = results[0]
       return {
           'valid': True,
           'address': address,
           'reference_date': reference_date,
           'matched': {
               'barangay': best['barangay'],
               'municipality_or_city': best['municipality_or_city'],
               'province_or_huc': best['province_or_huc'],
            'psgc_id': best['psgc_id'],
            },
            'score': best['score']
        }

   # Example: Validate an address from 2025
   address = "Tongmageng, Tawi-Tawi"
   result = validate_historical_address(address, "2025-07-08")

   if result['valid']:
       print(f"Address valid as of {result['reference_date']}")
       print(f"Matched: {result['matched']}")
       print(f"Score: {result['score']:.1f}%")
   else:
       print(f"Address not found: {result['message']}")

Data Analysis Over Time
~~~~~~~~~~~~~~~~~~~~~~~

Analyze trends and changes over time:

.. code-block:: python

   from barangay import load_barangay_flat_data, get_available_dates, current
   import pandas as pd

   # Get all available dates
   dates = sorted(get_available_dates() + [current])

   # Load data for each date
   data_by_date = {}
   for date in dates:
       data = pd.DataFrame(load_barangay_flat_data(as_of=date))
       data_by_date[date] = data
       print(f"Loaded data for {date}: {len(data)} barangays")

   # Analyze trends
   print("\n=== Barangay Count Over Time ===")
   for date in dates:
       count = len(data_by_date[date])
       print(f"{date}: {count}")

   # Analyze by region
   print("\n=== Barangay Count by Region Over Time ===")
   for date in dates:
       data = data_by_date[date]
       region_counts = data.groupby('region').size()
       print(f"\n{date}:")
       print(region_counts.head(5))

Downloading Historical Data
---------------------------

On-Demand Download
~~~~~~~~~~~~~~~~~~

Historical data is downloaded on-demand when first accessed:

.. code-block:: python

   from barangay import search

   # First access - downloads data
   print("Downloading data for 2025-07-08...")
   results = search("Tongmageng", as_of="2025-07-08")
   print(f"Found {len(results)} results")

   # Subsequent access - uses cached data
   print("\nUsing cached data for 2025-07-08...")
   results = search("Tongmageng", as_of="2025-07-08")
   print(f"Found {len(results)} results")

Download Progress
~~~~~~~~~~~~~~~~~

When downloading historical data, the package logs information about which dataset is being used:

.. code-block:: python

   from barangay import load_env_config, get_verbose

   # Enable verbose logging
   import os
   os.environ["BARANGAY_VERBOSE"] = "true"

   # Load configuration
   config = load_env_config()
   verbose = get_verbose()

   print(f"Verbose logging: {verbose}")

   # Access historical data
   from barangay import search
   results = search("Tongmageng", as_of="2025-07-08")

Output (with verbose logging):

.. code-block:: text

   Verbose logging: True
   [barangay] Using 2025-07-08 dataset (closest on or before 2025-07-08)

Comparing Data Across Dates
---------------------------

Comparing Two Dates
~~~~~~~~~~~~~~~~~~~

Compare data between two specific dates:

.. code-block:: python

   from barangay import load_barangay_flat_data
   import pandas as pd

   # Load data from two dates
   date1 = "2025-07-08"
   date2 = "2025-08-29"

   data1 = pd.DataFrame(load_barangay_flat_data(as_of=date1))
   data2 = pd.DataFrame(load_barangay_flat_data(as_of=date2))

   # Compare totals
   print(f"=== Comparison: {date1} vs {date2} ===")
   print(f"Total barangays: {len(data1)} → {len(data2)} (change: {len(data2) - len(data1)})")

   # Find differences
   set1 = set(data1['psgc_id'])
   set2 = set(data2['psgc_id'])

   added = set2 - set1
   removed = set1 - set2

   print(f"\nAdded: {len(added)}")
   if added:
       added_data = data2[data2['psgc_id'].isin(added)]
       print(added_data[['barangay', 'municipality_or_city', 'province_or_huc']].head())

   print(f"\nRemoved: {len(removed)}")
   if removed:
       removed_data = data1[data1['psgc_id'].isin(removed)]
       print(removed_data[['barangay', 'municipality_or_city', 'province_or_huc']].head())

Tracking Changes for a Specific Location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Track how a specific location changes over time:

.. code-block:: python

   from barangay import load_barangay_flat_data, get_available_dates, current
   import pandas as pd

   # Get all available dates
   dates = sorted(get_available_dates() + [current])

   # Location to track
   target_barangay = "Tongmageng"

   print(f"=== Tracking '{target_barangay}' over time ===")

   for date in dates:
       data = pd.DataFrame(load_barangay_flat_data(as_of=date))
       matches = data[data['barangay'] == target_barangay]

       if len(matches) > 0:
           match = matches.iloc[0]
           print(f"\n{date}:")
           print(f"  Barangay: {match['barangay']}")
           print(f"  Municipality: {match['municipality_or_city']}")
           print(f"  Province: {match['province_or_huc']}")
           print(f"  PSGC ID: {match['psgc_id']}")
       else:
           print(f"\n{date}: Not found")

Complete Example
----------------

Here's a complete example demonstrating historical data usage:

.. code-block:: python

   from barangay import (
       search,
       load_barangay_flat_data,
       get_available_dates,
       current,
       resolve_date,
   )
   import pandas as pd

   class HistoricalDataManager:
       """Manage and analyze historical barangay data."""

       def __init__(self):
           self.dates = sorted(get_available_dates() + [current])
           self.data_cache = {}

       def load_data(self, date):
           """Load data for a specific date with caching."""
           if date not in self.data_cache:
               print(f"Loading data for {date}...")
               self.data_cache[date] = pd.DataFrame(
                   load_barangay_flat_data(as_of=date)
               )
           return self.data_cache[date]

       def compare_dates(self, date1, date2):
           """Compare data between two dates."""
           data1 = self.load_data(date1)
           data2 = self.load_data(date2)

           set1 = set(data1['psgc_id'])
           set2 = set(data2['psgc_id'])

           added = set2 - set1
           removed = set1 - set2

           return {
               'date1': date1,
               'date2': date2,
               'count1': len(data1),
               'count2': len(data2),
               'change': len(data2) - len(data1),
               'added': len(added),
               'removed': len(removed),
               'added_data': data2[data2['psgc_id'].isin(added)] if added else pd.DataFrame(),
               'removed_data': data1[data1['psgc_id'].isin(removed)] if removed else pd.DataFrame(),
           }

       def track_barangay(self, barangay_name):
           """Track a specific barangay across all dates."""
           print(f"\n=== Tracking '{barangay_name}' ===")

           for date in self.dates:
               data = self.load_data(date)
               matches = data[data['barangay'] == barangay_name]

               if len(matches) > 0:
                   match = matches.iloc[0]
                   print(f"\n{date}:")
                   print(f"  Municipality: {match['municipality_or_city']}")
                   print(f"  Province: {match['province_or_huc']}")
                   print(f"  PSGC ID: {match['psgc_id']}")
               else:
                   print(f"\n{date}: Not found")

       def analyze_trends(self):
           """Analyze trends across all dates."""
           print("\n=== Trends Analysis ===")

           counts = []
           for date in self.dates:
               data = self.load_data(date)
               counts.append({'date': date, 'count': len(data)})

           trends_df = pd.DataFrame(counts)

           print("\nBarangay count over time:")
           print(trends_df)

           if len(trends_df) > 1:
               trends_df['change'] = trends_df['count'].diff()
               trends_df['pct_change'] = trends_df['count'].pct_change() * 100
               print("\nChanges:")
               print(trends_df)

   # Usage
   manager = HistoricalDataManager()

   # Display available dates
   print(f"Available dates: {manager.dates}")

   # Compare two dates
   print("\n=== Comparing 2025-07-08 vs 2025-08-29 ===")
   comparison = manager.compare_dates("2025-07-08", "2025-08-29")
   print(f"Count: {comparison['count1']} → {comparison['count2']} (change: {comparison['change']})")
   print(f"Added: {comparison['added']}")
   print(f"Removed: {comparison['removed']}")

   # Track a specific barangay
   manager.track_barangay("Tongmageng")

   # Analyze trends
   manager.analyze_trends()

Next Steps
----------

Now that you understand historical data, explore these topics:

* :doc:`search_fundamentals` - Learn about fuzzy search features
* :doc:`data_models` - Detailed information about data structures
* :doc:`configuration` - Configure the package for your needs
* :doc:`../how_to/performance` - Performance optimization tips

For API reference, see :doc:`../api_reference/date_resolver` and :doc:`../api_reference/data_manager`.