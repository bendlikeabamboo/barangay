Configuration
=============

This guide explains the core configuration options for the barangay package.

Configuration Overview
----------------------

The barangay package supports multiple configuration layers that work together to provide flexible customization:

.. list-table:: Configuration Layers
   :widths: 30 35 35
   :header-rows: 1

   * - Layer
     - Priority
     - Description
   * - Function parameter
     - Highest
     - Overrides all other settings
   * - Module attribute
     - High
     - Set programmatically at runtime
   * - Environment variable
     - Medium
     - Set before importing the package
   * - Default
     - Lowest
     - Built-in default values

Priority Order
~~~~~~~~~~~~~~

Configuration is resolved in the following priority order (highest to lowest):

1. **Function parameter** - If provided, takes precedence
2. **Module attribute** - ``barangay.as_of``
3. **Environment variable** - ``BARANGAY_*`` variables
4. **Default** - Built-in default values

Best Practices
~~~~~~~~~~~~~~

* Use **environment variables** for global settings (e.g., in production)
* Use **module attributes** for session-specific settings
* Use **function parameters** for per-call overrides
* **Document** your configuration for reproducibility

Environment Variables
---------------------

BARANGAY_AS_OF
~~~~~~~~~~~~~~

Sets the default dataset date for all operations.

**Format**: YYYY-MM-DD (e.g., "2025-07-08")

**Purpose**: Use historical data by default without specifying ``as_of`` in each function call

**Example**:

.. code-block:: bash

   # Set environment variable
   export BARANGAY_AS_OF="2025-07-08"

Then in Python:

.. code-block:: python

   from barangay import search

   # Uses BARANGAY_AS_OF environment variable
   results = search("Tongmageng")

**Use Cases**:

* Analyzing historical data consistently
* Testing with a specific dataset version
* Ensuring reproducibility across runs

.. note:: If ``BARANGAY_AS_OF`` is set, all operations will use that dataset unless explicitly overridden.

BARANGAY_VERBOSE
~~~~~~~~~~~~~~~~

Enables or disables verbose logging.

**Valid Values** (case-insensitive):

* ``"true"``, ``"1"``, ``"yes"``, ``"on"`` - Enable verbose logging
* Any other value (including unset) - Disable verbose logging

**Default**: ``"true"``

**Example**:

.. code-block:: bash

   # Enable verbose logging
   export BARANGAY_VERBOSE="true"

   # Disable verbose logging
   export BARANGAY_VERBOSE="false"

Then in Python:

.. code-block:: python

   from barangay import search, get_verbose

   # Check verbose setting
   verbose = get_verbose()
   print(f"Verbose logging: {verbose}")

   # Perform search (logs will be shown if verbose is True)
   results = search("Tongmageng")

**Use Cases**:

* Debugging data loading issues
* Monitoring which dataset is being used
* Troubleshooting download problems

BARANGAY_CACHE_DIR
~~~~~~~~~~~~~~~~~~

Sets a custom cache directory for downloaded historical data.

**Format**: Absolute or relative path (e.g., "/custom/cache/path")

**Default**: System-dependent (see :ref:`cache-location`)

**Example**:

.. code-block:: bash

   # Set custom cache directory
   export BARANGAY_CACHE_DIR="/custom/cache/path"

Then in Python:

.. code-block:: python

   from barangay import get_cache_dir

   # Check cache directory
   cache_dir = get_cache_dir()
   print(f"Cache directory: {cache_dir}")

**Use Cases**:

* Storing cache in a specific location (e.g., network drive)
* Controlling disk usage
* Sharing cache across environments

.. warning:: The cache directory must be writable. If the directory doesn't exist, it will be created automatically.

Module-Level Attributes
-----------------------

current
~~~~~~~

The current dataset date bundled with the package.

**Type**: ``str``

**Format**: YYYY-MM-DD

**Read-only**: Yes

**Example**:

.. code-block:: python

   import barangay

   print(f"Current dataset date: {barangay.current}")

Output:

.. code-block:: text

   Current dataset date: 2026-01-13

as_of
~~~~~

The default dataset date for the current session.

**Type**: ``str | None``

**Format**: YYYY-MM-DD or None

**Read-only**: No (can be set)

**Default**: None (use latest bundled data)

**Example**:

.. code-block:: python

   import barangay

   # Set default date for this session
   barangay.as_of = "2025-07-08"

   # All operations use this date
   from barangay import search
   results = search("Tongmageng")

   # Reset to latest data
   barangay.as_of = None

**Use Cases**:

* Session-specific historical data analysis
* Testing with different dataset versions
* Temporary override of environment variables

available_dates
~~~~~~~~~~~~~~~

List of all available dataset dates (including current).

**Type**: ``list[str]``

**Format**: List of YYYY-MM-DD strings

**Read-only**: Yes

**Example**:

.. code-block:: python

   import barangay

   print("Available dates:")
   for date in sorted(barangay.available_dates, reverse=True):
       print(f"  - {date}")

Output:

.. code-block:: text

   Available dates:
     - 2026-01-13 (current)
     - 2025-10-13
     - 2025-08-29
     - 2025-07-08

Configuration Examples
----------------------

Setting via Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux/Mac:

.. code-block:: bash

   # Set environment variables
   export BARANGAY_AS_OF="2025-07-08"
   export BARANGAY_VERBOSE="true"
   export BARANGAY_CACHE_DIR="/custom/cache"

   # Run your Python script
   python my_script.py

Windows (Command Prompt):

.. code-block:: bat

   REM Set environment variables
   set BARANGAY_AS_OF=2025-07-08
   set BARANGAY_VERBOSE=true
   set BARANGAY_CACHE_DIR=C:\custom\cache

   REM Run your Python script
   python my_script.py

Windows (PowerShell):

.. code-block:: powershell

   # Set environment variables
   $env:BARANGAY_AS_OF="2025-07-08"
   $env:BARANGAY_VERBOSE="true"
   $env:BARANGAY_CACHE_DIR="C:\custom\cache"

   # Run your Python script
   python my_script.py

Using .env File
~~~~~~~~~~~~~~~

Create a ``.env`` file in your project directory:

.. code-block:: ini

   BARANGAY_AS_OF=2025-07-08
   BARANGAY_VERBOSE=true
   BARANGAY_CACHE_DIR=/custom/cache

Then load it in Python:

.. code-block:: python

   from dotenv import load_dotenv
   load_dotenv()  # Load .env file

   import barangay
   from barangay import search

   # Environment variables are now loaded
   results = search("Tongmageng")

Setting via Module Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set module attributes programmatically:

.. code-block:: python

   import barangay

   # Set default date for this session
   barangay.as_of = "2025-07-08"

   # All operations use this date
   from barangay import search
   results = search("Tongmageng")

   # Reset to latest data
   barangay.as_of = None

Setting via Function Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Override configuration for specific function calls:

.. code-block:: python

   from barangay import search

   # Use latest data (default)
   results1 = search("Tongmageng")

   # Use specific date (overrides all other settings)
   results2 = search("Tongmageng", as_of="2025-07-08")

   # Use another date
   results3 = search("Tongmageng", as_of="2025-08-29")

Combining Configuration Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can combine multiple configuration methods:

.. code-block:: python

   import os
   import barangay

   # Set environment variable (global default)
   os.environ["BARANGAY_AS_OF"] = "2025-07-08"

   # Set module attribute (session override)
   barangay.as_of = "2025-08-29"

   # Use function parameter (per-call override)
   from barangay import search
   results = search("Tongmageng", as_of="2025-10-13")

   # Priority: function parameter > module attribute > environment variable > default

Next Steps
----------

For advanced topics, see:

* :doc:`../advanced/caching` - Advanced cache configuration and management
* :doc:`../how_to/performance` - Performance optimization settings

For API reference, see :doc:`../api_reference/config`.