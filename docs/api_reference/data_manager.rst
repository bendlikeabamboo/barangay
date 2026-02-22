#####################
 Data Manager Module
####################

The data_manager module provides the DataManager class for handling data
loading, caching, and downloading of Philippine barangay data. The
DataManager supports multiple data formats and can load data from
bundled package files, local cache, or download from GitHub.


 Overview
*********

The DataManager class provides a unified interface for loading barangay
data from multiple sources. It handles data loading from bundled package
files, local cache, and downloading from GitHub repository.

Supported Data Types
====================

The DataManager supports the following data types:

-  **basic**: Basic barangay data (JSON format) - Nested dictionary
   structure
-  **extended**: Extended barangay data with recursive structure (JSON
   format)
-  **flat**: Flat barangay data with parent references (JSON format)
-  **fuzzer_base**: Pre-processed data for fuzzy matching (Parquet
   format)

Data Loading Priority
=====================

The DataManager follows this priority order when loading data:

#. **Bundled package data** - For current date or when as_of is None
#. **Local cache** - For historical dates (if previously downloaded)
#. **Download from GitHub** - If not cached (for historical dates)


 API Reference
**************

.. autoclass:: barangay.data_manager.DataManager
   :members:
   :undoc-members:
   :show-inheritance:


 Module Constants
*****************

.. autodata:: barangay.data_manager.CURRENT_DATE
   :annotation: = "2026-01-13"

.. autodata:: barangay.data_manager.DATA_TYPE_MAPPING
   :annotation: = {"basic": "barangay.json", "extended": "barangay_extended.json", "flat": "barangay_flat.json", "fuzzer_base": "fuzzer_base.parquet"}

.. autodata:: barangay.data_manager.DATA_TYPE_EXTENSIONS
   :annotation: = {"basic": ".json", "extended": ".json", "flat": ".json", "fuzzer_base": ".parquet"}


 Examples
*********

Basic Usage
===========

.. code:: python

   from barangay.data_manager import DataManager

   # Create DataManager instance
   dm = DataManager()

   # Load latest basic data
   data = dm.get_data(data_type="basic")

Loading Historical Data
=======================

.. code:: python

   from barangay.data_manager import DataManager

   # Create DataManager instance
   dm = DataManager()

   # Load historical data
   data = dm.get_data(as_of="2025-07-08", data_type="basic")

Loading Fuzzer Base
===================

.. code:: python

   from barangay.data_manager import DataManager

   # Create DataManager instance
   dm = DataManager()

   # Load fuzzer base (returns DataFrame)
   df = dm.get_data(data_type="fuzzer_base")

Loading Different Data Types
============================

.. code:: python

   from barangay.data_manager import DataManager

   dm = DataManager()

   # Load basic data
   basic = dm.get_data(data_type="basic")

   # Load extended data
   extended = dm.get_data(data_type="extended")

   # Load flat data
   flat = dm.get_data(data_type="flat")

Using with Date Resolution
==========================

.. code:: python

   from barangay.data_manager import DataManager

   dm = DataManager()

   # The DataManager automatically resolves dates
   # If as_of is None, it uses the latest bundled data
   data = dm.get_data(as_of=None, data_type="basic")

   # If as_of is specified, it resolves to the closest available dataset
   data = dm.get_data(as_of="2026-01-01", data_type="basic")

Cache Directory
===============

The DataManager uses a cache directory to store downloaded historical
data. The cache directory location depends on the operating system:

-  **Windows**: ``%LOCALAPPDATA%\\barangay\\cache``
-  **Linux/Mac with XDG_CACHE_HOME**: ``$XDG_CACHE_HOME/barangay``
-  **Linux/Mac fallback**: ``~/.cache/barangay``
-  **Custom**: ``$BARANGAY_CACHE_DIR`` if set


 See Also
*********

-  :mod:`barangay.data` - Data loading module
-  :mod:`barangay.downloader` - Data downloading module
-  :mod:`barangay.date_resolver` - Date resolution module
-  :func:`barangay.data.load_barangay_data` - Load basic barangay data
-  :func:`barangay.data.load_barangay_extended_data` - Load extended
   barangay data
-  :func:`barangay.data.load_barangay_flat_data` - Load flat barangay
   data
-  :func:`barangay.data.load_fuzzer_base` - Load fuzzer base data