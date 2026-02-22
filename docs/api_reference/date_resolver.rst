######################
 Date Resolver Module
#####################

The date_resolver module provides functions for resolving approximate
dates to the closest available dataset. It supports fetching available
dates from GitHub API and caching the results locally for improved
performance.


 Overview
*********

The date_resolver module handles date resolution for loading historical
barangay data. When a specific date is requested, the module resolves it
to the closest available dataset from the GitHub repository.

Date Resolution Logic
=====================

The date resolution follows these rules:

#. If as_of is None: Use latest bundled data
#. If exact match exists: Use that date
#. If no exact match: Use the closest date <= requested date
#. If requested date is before all available dates: Use the earliest
   date


 API Reference
**************

.. autofunction:: barangay.date_resolver.resolve_date

.. autofunction:: barangay.date_resolver.get_available_dates

.. autofunction:: barangay.date_resolver.get_cache_dir


 Module Constants
*****************

.. autodata:: barangay.date_resolver.GITHUB_API_URL
   :annotation: = "https://api.github.com/repos/bendlikeabamboo/barangay-data-repository/contents/"

.. autodata:: barangay.date_resolver.AVAILABLE_DATES_CACHE_FILE
   :annotation: = "available_dates.json"


 Examples
*********

Resolving a Date
================

.. code:: python

   from barangay.date_resolver import resolve_date

   # Get available dates
   available_dates = ["2025-07-08", "2025-08-29", "2025-10-13"]
   current_date = "2026-01-13"

   # Exact match
   resolved, message = resolve_date("2025-07-08", available_dates, current_date)
   print(resolved)  # 2025-07-08
   print(message)  # Using 2025-07-08 dataset

   # Closest match
   resolved, message = resolve_date("2026-01-01", available_dates, current_date)
   print(resolved)  # 2025-10-13
   print(message)  # Using 2025-10-13 dataset (closest to 2026-01-01)

   # Latest (None)
   resolved, message = resolve_date(None, available_dates, current_date)
   print(resolved)  # None
   print(message)  # Using latest dataset

Getting Available Dates
=======================

.. code:: python

   from barangay.date_resolver import get_available_dates

   # Fetch available dates from GitHub API
   dates = get_available_dates()
   print(dates[:3])
   # ['2025-07-08', '2025-08-29', '2025-10-13']

   # Check if a specific date is available
   if "2025-07-08" in dates:
       print("2025-07-08 dataset is available")

Using with Data Loading
=======================

.. code:: python

   from barangay.date_resolver import resolve_date, get_available_dates
   from barangay.data_manager import DataManager

   # Get available dates
   available_dates = get_available_dates()
   current_date = "2026-01-13"

   # Resolve requested date
   resolved_date, status_message = resolve_date(
       "2025-12-01", available_dates, current_date
   )

   # Load data using resolved date
   dm = DataManager()
   data = dm.get_data(as_of=resolved_date, data_type="basic")

Cache Behavior
==============

The available dates are cached locally to reduce GitHub API calls:

-  **Cache location**: ``~/.cache/barangay/available_dates.json``
   (Linux/Mac) or
   ``%LOCALAPPDATA%\\barangay\\cache\\available_dates.json`` (Windows)

-  **Cache TTL**: 1 hour

-  **Fallback**: If GitHub API call fails, cached data is returned if
   available

.. code:: python

   from barangay.date_resolver import get_available_dates

   # First call: Fetches from GitHub API and caches the result
   dates = get_available_dates()

   # Second call within 1 hour: Returns cached data (no API call)
   dates = get_available_dates()

   # After 1 hour: Fetches from GitHub API again and updates cache

Date Format Validation
======================

The module validates that date strings match the YYYY-MM-DD format and
represent valid calendar dates.

.. code:: python

   from barangay.date_resolver import _is_valid_date

   # Valid dates
   print(_is_valid_date("2025-07-08"))  # True
   print(_is_valid_date("2026-01-13"))  # True

   # Invalid dates
   print(_is_valid_date("2025-13-01"))  # False (invalid month)
   print(_is_valid_date("2025-02-30"))  # False (invalid day)
   print(_is_valid_date("not-a-date"))  # False (invalid format)


 See Also
*********

-  :mod:`barangay.config` - Configuration module
-  :mod:`barangay.data_manager` - Data management module
-  :func:`barangay.config.resolve_as_of` - Resolve as_of date from
   multiple layers