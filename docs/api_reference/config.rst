###############
 Config Module
##############

The config module provides functions for resolving configuration
settings from multiple sources, including environment variables, module
attributes, and function parameters. The configuration follows a
priority-based resolution system.


 Overview
*********

The config module handles configuration resolution for the barangay
package, allowing users to configure behavior through environment
variables, module attributes, or function parameters.

Environment Variables
=====================

The following environment variables are supported:

-  **BARANGAY_AS_OF**: Default dataset date (YYYY-MM-DD format). If set,
   this date will be used for all searches unless overridden by function
   parameters or module attributes.

-  **BARANGAY_VERBOSE**: Enable verbose logging. Valid values are
   "true", "1", "yes", "on" (case-insensitive). Default is "true".

-  **BARANGAY_CACHE_DIR**: Custom cache directory path. If set,
   downloaded data will be stored in this directory instead of the
   system default.

Configuration Priority
======================

The as_of date is resolved in the following priority order (highest to
lowest):

#. **Function parameter** (if provided)
#. **Module attribute** (barangay.as_of)
#. **Environment variable** (BARANGAY_AS_OF)
#. **Default**: None (use latest bundled data)


 API Reference
**************

.. autofunction:: barangay.config.load_env_config

.. autofunction:: barangay.config.resolve_as_of

.. autofunction:: barangay.config.get_verbose

.. autofunction:: barangay.config.get_cache_dir


 Module Constants
*****************

.. autodata:: barangay.config.DEFAULT_VERBOSE
   :annotation: = "true"

.. autodata:: barangay.config.DEFAULT_CACHE_DIR
   :annotation: = None


 Examples
*********

Setting Configuration via Environment Variables
===============================================

.. code:: python

   import os

   # Set environment variables
   os.environ["BARANGAY_AS_OF"] = "2025-07-08"
   os.environ["BARANGAY_VERBOSE"] = "true"
   os.environ["BARANGAY_CACHE_DIR"] = "/custom/cache/path"

   # The configuration will be used automatically
   from barangay import search

   results = search("Tongmageng")  # Uses 2025-07-08 dataset

Using resolve_as_of
===================

.. code:: python

   from barangay.config import resolve_as_of

   # Using function parameter (highest priority)
   date = resolve_as_of(as_of_param="2025-08-29")
   print(date)  # 2025-08-29

   # Using default (None)
   date = resolve_as_of()
   print(date)  # None (uses latest bundled data)

Getting Verbose Setting
=======================

.. code:: python

   from barangay.config import get_verbose

   # Get verbose setting
   verbose = get_verbose()
   print(verbose)  # True (default)

   # With custom environment variable
   import os

   os.environ["BARANGAY_VERBOSE"] = "false"
   verbose = get_verbose()
   print(verbose)  # False

Getting Cache Directory
=======================

.. code:: python

   from barangay.config import get_cache_dir
   from pathlib import Path

   # Get default cache directory
   cache_dir = get_cache_dir()
   print(cache_dir)
   # /home/user/.cache/barangay (Linux/Mac)
   # C:\Users\user\AppData\Local\barangay\cache (Windows)

   # With custom environment variable
   import os

   os.environ["BARANGAY_CACHE_DIR"] = "/custom/cache/path"
   cache_dir = get_cache_dir()
   print(cache_dir)  # /custom/cache/path

Using Module Attribute
======================

.. code:: python

   import barangay

   # Set module attribute (second priority)
   barangay.as_of = "2025-07-08"

   # The attribute will be used by resolve_as_of
   from barangay.config import resolve_as_of

   date = resolve_as_of()
   print(date)  # 2025-07-08

Combining Configuration Sources
===============================

.. code:: python

   import os
   import barangay

   # Set environment variable (third priority)
   os.environ["BARANGAY_AS_OF"] = "2025-10-13"

   # Set module attribute (second priority)
   barangay.as_of = "2025-08-29"

   # Function parameter (highest priority)
   from barangay.config import resolve_as_of

   date = resolve_as_of(as_of_param="2025-07-08")
   print(date)  # 2025-07-08 (function parameter wins)

Cache Directory Locations
=========================

The cache directory location depends on the operating system:

-  **Windows**: ``%LOCALAPPDATA%\\barangay\\cache``
-  **Linux/Mac with XDG_CACHE_HOME**: ``$XDG_CACHE_HOME/barangay``
-  **Linux/Mac fallback**: ``~/.cache/barangay``
-  **Custom**: ``$BARANGAY_CACHE_DIR`` if set


 See Also
*********

-  :mod:`barangay.date_resolver` - Date resolution module
-  :mod:`barangay.data_manager` - Data management module
-  :func:`barangay.date_resolver.resolve_date` - Resolve approximate
   dates to closest available dataset