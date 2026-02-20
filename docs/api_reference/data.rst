#############
 Data Module
############

The data module provides functions for loading Philippine barangay data
in different formats. It supports loading data from bundled package
files, local cache, or downloading from GitHub repository.


 Overview
*********

The data module provides convenient functions for loading barangay data
in three different formats, each optimized for different use cases. The
data can be loaded from bundled package files, local cache, or
downloaded from GitHub repository.


 Data Structures
****************

The module provides three main data structures:

**BARANGAY** - Basic barangay data
   Nested dictionary structure: region -> city/municipality -> barangay
   Best for: Simple lookups and hierarchical access

**BARANGAY_EXTENDED** - Extended barangay data
   Recursive structure with rich metadata Best for: Complex hierarchies
   and detailed information

**BARANGAY_FLAT** - Flat barangay data
   Flat list with parent references Best for: Search, filtering, and
   DataFrame operations


 API Reference
**************

Data Structures
===============

.. autodata:: barangay.data.BARANGAY
   :annotation: = {...}

.. autodata:: barangay.data.BARANGAY_EXTENDED
   :annotation: = {...}

.. autodata:: barangay.data.BARANGAY_FLAT
   :annotation: = {...}

Loading Functions
=================

.. autofunction:: barangay.data.load_barangay_data

.. autofunction:: barangay.data.load_barangay_extended_data

.. autofunction:: barangay.data.load_barangay_flat_data

.. autofunction:: barangay.data.load_fuzzer_base


 Examples
*********

Loading Basic Data
==================

.. code:: python

   from barangay import load_barangay_data

   # Load latest basic data
   data = load_barangay_data()

   # Access regions
   print(list(data.keys())[:3])
   # ['National Capital Region (NCR)', 'Region I (Ilocos Region)', 'Region II (Cagayan Valley)']

   # Access cities/municipalities
   ncr = data["National Capital Region (NCR)"]
   print(list(ncr.keys())[:3])
   # ['City of Manila', 'Quezon City', 'Caloocan City']

   # Access barangays
   manila = ncr["City of Manila"]
   print(list(manila.keys())[:3])
   # ['Barangay 1', 'Barangay 2', 'Barangay 3']

Loading Historical Data
=======================

.. code:: python

   from barangay import load_barangay_data

   # Load historical data
   data = load_barangay_data(as_of="2025-07-08")

   # The data structure is the same as latest data
   print(list(data.keys())[:3])

Loading Extended Data
=====================

.. code:: python

   from barangay import load_barangay_extended_data

   # Load extended data
   data = load_barangay_extended_data()

   # Extended data includes rich metadata
   print(list(data.keys())[:3])

Loading Flat Data
=================

.. code:: python

   from barangay import load_barangay_flat_data

   # Load flat data
   data = load_barangay_flat_data()

   # Access the list of barangays
   barangays = data.get("barangays", [])
   print(barangays[0])
   # {'barangay': 'Barangay 1', 'province_or_huc': 'Province A', ...}

   # Convert to DataFrame
   import pandas as pd

   df = pd.DataFrame(barangays)
   print(df.head())

Loading Fuzzer Base
===================

.. code:: python

   from barangay import load_fuzzer_base

   # Load fuzzer base
   df = load_fuzzer_base()

   # View columns
   print(df.columns.tolist())
   # ['barangay', 'province_or_huc', 'municipality_or_city', 'psgc_id', ...]

   # View sanitized strings
   print(df[["barangay", "000b", "0p0b", "00mb", "0pmb"]].head())

Using Pre-loaded Data
=====================

.. code:: python

   from barangay import BARANGAY, BARANGAY_EXTENDED, BARANGAY_FLAT

   # Access pre-loaded data (loaded at module import)
   print(list(BARANGAY.keys())[:3])
   print(list(BARANGAY_EXTENDED.keys())[:3])
   print(list(BARANGAY_FLAT.keys())[:3])

Converting Between Formats
==========================

.. code:: python

   from barangay import load_barangay_data, load_barangay_flat_data
   import pandas as pd

   # Load basic data
   basic = load_barangay_data()

   # Convert to flat format manually
   barangays = []
   for region, cities in basic.items():
       for city, barangays_dict in cities.items():
           for barangay, psgc_id in barangays_dict.items():
               barangays.append(
                   {
                       "barangay": barangay,
                       "province_or_huc": region,
                       "municipality_or_city": city,
                       "psgc_id": psgc_id,
                   }
               )

   # Or use the flat data directly
   flat = load_barangay_flat_data()
   df = pd.DataFrame(flat["barangays"])

Data Format Comparison
======================

.. list-table:: Data Format Comparison
   :widths: 25 25 25 25
   :header-rows: 1

   -  -  Format
      -  Structure
      -  Best For
      -  Example Use

   -  -  Basic
      -  Nested dict
      -  Simple lookups
      -  ``data["NCR"]["Manila"]["Barangay 1"]``

   -  -  Extended
      -  Recursive
      -  Complex hierarchies
      -  Detailed admin info

   -  -  Flat
      -  List of dicts
      -  Search, filtering
      -  ``df[df["barangay"] == "Barangay 1"]``

   -  -  Fuzzer Base
      -  DataFrame
      -  Fuzzy matching
      -  Pre-computed functions


 See Also
*********

-  :mod:`barangay.data_manager` - Data management module
-  :mod:`barangay.fuzz` - Fuzzy matching module
-  :class:`barangay.fuzz.FuzzBase` - Fuzzy matching class
-  :func:`barangay.fuzz.create_fuzz_base` - Factory function to create
   FuzzBase instances