#############
 Fuzz Module
############

The fuzz module provides the FuzzBase class and related functions for
performing fuzzy string matching on Philippine barangay data. The module
uses the RapidFuzz library for fast and accurate fuzzy matching based on
token sort ratio.


 Overview
*********

The FuzzBase class prepares a DataFrame with pre-computed partial
functions for efficient searching across different administrative
levels. This pre-computation significantly improves performance when
performing multiple searches.

Matching Strategies
===================

The FuzzBase class creates four different matching strategies:

-  **000b**: Barangay name only
-  **0p0b**: Province + Barangay names
-  **00mb**: Municipality + Barangay names
-  **0pmb**: Province + Municipality + Barangay names

Each strategy has both a sanitized string version (e.g., "000b") and a
pre-computed partial function (e.g., "f_000b_ratio") for fast matching.


 API Reference
**************

.. autoclass:: barangay.fuzz.FuzzBase
   :members:
   :undoc-members:
   :show-inheritance:

.. autofunction:: barangay.fuzz.create_fuzz_base


 Examples
*********

Creating a FuzzBase Instance
============================

.. code:: python

   from barangay import FuzzBase
   import pandas as pd

   # Create a FuzzBase instance with custom data
   data = pd.DataFrame(
       {
           "barangay": ["Barangay 1", "Barangay 2"],
           "province_or_huc": ["Province A", "Province B"],
           "municipality_or_city": ["City 1", "City 2"],
       }
   )
   fuzz_base = FuzzBase(fuzzer_base=data)

Using create_fuzz_base Factory
==============================

.. code:: python

   from barangay import create_fuzz_base

   # Create FuzzBase with latest data
   fuzz_base = create_fuzz_base()

   # Create FuzzBase with historical data
   fuzz_base = create_fuzz_base(as_of="2025-07-08")

Using FuzzBase with Search
==========================

.. code:: python

   from barangay import search, create_fuzz_base

   # Create a FuzzBase instance for multiple searches
   fuzz_base = create_fuzz_base()

   # Perform multiple searches efficiently
   results1 = search("Tongmageng", fuzz_base=fuzz_base)
   results2 = search("San Jose", fuzz_base=fuzz_base)

With Custom Sanitizer
=====================

.. code:: python

   from barangay import FuzzBase, sanitize_input

   # Create a custom sanitizer
   custom_sanitizer = lambda x: sanitize_input(x, exclude=["city of "])

   # Create FuzzBase with custom sanitizer
   fuzz_base = FuzzBase(fuzzer_base=your_dataframe, sanitizer=custom_sanitizer)

Accessing Pre-computed Functions
================================

.. code:: python

   from barangay import create_fuzz_base

   # Create FuzzBase instance
   fuzz_base = create_fuzz_base()

   # Access the pre-computed DataFrame
   df = fuzz_base.fuzzer_base

   # The DataFrame contains:
   # - Sanitized strings: 000b, 0p0b, 00mb, 0pmb
   # - Pre-computed functions: f_000b_ratio, f_0p0b_ratio, f_00mb_ratio, f_0pmb_ratio
   print(df.columns.tolist())


 See Also
*********

-  :mod:`barangay.search` - Search functionality module
-  :mod:`barangay.data` - Data loading module
-  :func:`barangay.search.search` - Search function using FuzzBase
-  :func:`barangay.data.load_fuzzer_base` - Load fuzzer base data
-  :func:`barangay.utils.sanitize_input` - String sanitization utility