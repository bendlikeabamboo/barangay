###################
 Downloader Module
##################

The downloader module provides functions for downloading Philippine
barangay data from the GitHub repository. It supports downloading
different data types and saving them to a local cache directory.


 Overview
*********

The downloader module handles downloading barangay data from the GitHub
repository. It supports downloading different data types and saves them
to a local cache directory for faster subsequent access.

Supported Data Types
====================

The module supports downloading the following data types:

-  **basic**: Basic barangay data (barangay.json)
-  **extended**: Extended barangay data (barangay_extended.json)
-  **flat**: Flat barangay data (barangay_flat.json)
-  **fuzzer_base**: Pre-processed data for fuzzy matching
   (fuzzer_base.parquet)


 API Reference
**************

.. autofunction:: barangay.downloader.get_github_url

.. autofunction:: barangay.downloader.download_data

.. autofunction:: barangay.downloader.fetch_available_dates


 Module Constants
*****************

.. autodata:: barangay.downloader.GITHUB_REPO
   :annotation: = "bendlikeabamboo/barangay-data-repository"

.. autodata:: barangay.downloader.GITHUB_RAW_URL
   :annotation: = "https://raw.githubusercontent.com/{repo}/main/{date}/{filename}"

.. autodata:: barangay.downloader.GITHUB_API_URL
   :annotation: = "https://api.github.com/repos/{repo}/contents/"

.. autodata:: barangay.downloader.DATA_TYPE_MAPPING
   :annotation: = {"basic": "barangay.json", "extended": "barangay_extended.json", "flat": "barangay_flat.json", "fuzzer_base": "fuzzer_base.parquet"}


 Examples
*********

Downloading Data
================

.. code:: python

   from barangay.downloader import download_data
   from pathlib import Path

   # Set cache directory
   cache_dir = Path.home() / ".cache" / "barangay"

   # Download basic data
   file_path = download_data("2025-07-08", "basic", cache_dir)
   print(file_path)
   # /home/user/.cache/barangay/2025-07-08_barangay.json

   # Download fuzzer base
   file_path = download_data("2025-08-29", "fuzzer_base", cache_dir)
   print(file_path)
   # /home/user/.cache/barangay/2025-08-29_fuzzer_base.parquet

Getting GitHub URL
==================

.. code:: python

   from barangay.downloader import get_github_url

   # Get URL for basic data
   url = get_github_url("2025-07-08", "barangay.json")
   print(url)
   # https://raw.githubusercontent.com/bendlikeabamboo/barangay-data-repository/main/2025-07-08/barangay.json

   # Get URL for fuzzer base
   url = get_github_url("2025-08-29", "fuzzer_base.parquet")
   print(url)
   # https://raw.githubusercontent.com/bendlikeabamboo/barangay-data-repository/main/2025-08-29/fuzzer_base.parquet

Fetching Available Dates
========================

.. code:: python

   from barangay.downloader import fetch_available_dates

   # Fetch available dates from GitHub API
   dates = fetch_available_dates()
   print(dates[:3])
   # ['2025-07-08', '2025-08-29', '2025-10-13']

   # Check if a specific date is available
   if "2025-07-08" in dates:
       print("2025-07-08 dataset is available")

Downloading Multiple Data Types
===============================

.. code:: python

   from barangay.downloader import download_data
   from pathlib import Path

   cache_dir = Path.home() / ".cache" / "barangay"
   date = "2025-07-08"

   # Download all data types for a specific date
   data_types = ["basic", "extended", "flat", "fuzzer_base"]
   for data_type in data_types:
       file_path = download_data(date, data_type, cache_dir)
       print(f"Downloaded {data_type}: {file_path}")

Error Handling
==============

.. code:: python

   from barangay.downloader import download_data
   from pathlib import Path

   cache_dir = Path.home() / ".cache" / "barangay"

   try:
       # Download data
       file_path = download_data("2025-07-08", "basic", cache_dir)
       print(f"Successfully downloaded: {file_path}")
   except ValueError as e:
       print(f"Invalid data type: {e}")
   except RuntimeError as e:
       print(f"Download failed: {e}")

Using with DataManager
======================

.. code:: python

   from barangay.data_manager import DataManager
   from barangay.downloader import download_data
   from pathlib import Path

   # Set cache directory
   cache_dir = Path.home() / ".cache" / "barangay"

   # Download data manually
   file_path = download_data("2025-07-08", "basic", cache_dir)

   # Or let DataManager handle downloading automatically
   dm = DataManager()
   data = dm.get_data(as_of="2025-07-08", data_type="basic")

GitHub Repository
=================

The downloader module fetches data from the following GitHub repository:

-  **Repository**: ``bendlikeabamboo/barangay-data-repository``
-  **Base URL**:
   ``https://raw.githubusercontent.com/bendlikeabamboo/barangay-data-repository/main/``
-  **API URL**:
   ``https://api.github.com/repos/bendlikeabamboo/barangay-data-repository/contents/``

Data files are organized by date in the repository:

.. code:: text

   barangay-data-repository/
   ├── 2025-07-08/
   │   ├── barangay.json
   │   ├── barangay_extended.json
   │   ├── barangay_flat.json
   │   └── fuzzer_base.parquet
   ├── 2025-08-29/
   │   ├── barangay.json
   │   ├── barangay_extended.json
   │   ├── barangay_flat.json
   │   └── fuzzer_base.parquet
   └── ...


 See Also
*********

-  :mod:`barangay.data_manager` - Data management module
-  :mod:`barangay.date_resolver` - Date resolution module
-  :func:`barangay.date_resolver.get_available_dates` - Fetch available
   dates with caching