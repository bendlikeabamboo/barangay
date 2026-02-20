Configuration Guide
===================

This guide covers configuration options for the barangay package, including environment variables, module-level attributes, and configuration best practices.

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

Advanced Configuration
----------------------

Custom Cache Directory Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up a custom cache directory:

.. code-block:: python

   import os
   from barangay import get_cache_dir

   # Set custom cache directory
   custom_cache = "/custom/cache/path"
   os.environ["BARANGAY_CACHE_DIR"] = custom_cache

   # Verify cache directory
   cache_dir = get_cache_dir()
   print(f"Cache directory: {cache_dir}")

   # Import and use barangay
   from barangay import search
   results = search("Tongmageng", as_of="2025-07-08")

.. note:: The cache directory will be created automatically if it doesn't exist.

Logging Configuration
~~~~~~~~~~~~~~~~~~~~~

Configure verbose logging:

.. code-block:: python

   import os
   import logging

   # Enable verbose logging
   os.environ["BARANGAY_VERBOSE"] = "true"

   # Configure logging level
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   )

   # Import and use barangay
   from barangay import search
   results = search("Tongmageng", as_of="2025-07-08")

Output with verbose logging:

.. code-block:: text

   2025-02-19 12:00:00 - barangay - INFO - Using 2025-07-08 dataset (closest on or before 2025-07-08)

Proxy Settings (for Downloads)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure proxy for downloading historical data:

.. code-block:: python

   import os

   # Set proxy environment variables
   os.environ["HTTP_PROXY"] = "http://proxy.example.com:8080"
   os.environ["HTTPS_PROXY"] = "http://proxy.example.com:8080"

   # Import and use barangay
   from barangay import search
   results = search("Tongmageng", as_of="2025-07-08")

Configuration Priority Examples
-------------------------------

Example 1: Environment Variable Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os

   # Set environment variable
   os.environ["BARANGAY_AS_OF"] = "2025-07-08"

   # Import and use barangay
   from barangay import search
   results = search("Tongmageng")

   # Uses BARANGAY_AS_OF environment variable

Example 2: Module Attribute Override
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   import barangay

   # Set environment variable
   os.environ["BARANGAY_AS_OF"] = "2025-07-08"

   # Override with module attribute
   barangay.as_of = "2025-08-29"

   # Import and use barangay
   from barangay import search
   results = search("Tongmageng")

   # Uses barangay.as_of (module attribute takes priority)

Example 3: Function Parameter Override
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   import barangay

   # Set environment variable
   os.environ["BARANGAY_AS_OF"] = "2025-07-08"

   # Override with module attribute
   barangay.as_of = "2025-08-29"

   # Override with function parameter
   from barangay import search
   results = search("Tongmageng", as_of="2025-10-13")

   # Uses function parameter (highest priority)

Configuration Helper Functions
------------------------------

resolve_as_of()
~~~~~~~~~~~~~~~

Resolve the ``as_of`` date from multiple configuration layers:

.. code-block:: python

   from barangay.config import resolve_as_of

   # Resolve from function parameter
   date1 = resolve_as_of(as_of_param="2025-08-29")
   print(f"Function parameter: {date1}")

   # Resolve from module attribute
   import barangay
   barangay.as_of = "2025-07-08"
   date2 = resolve_as_of()
   print(f"Module attribute: {date2}")

   # Resolve from environment variable
   import os
   os.environ["BARANGAY_AS_OF"] = "2025-10-13"
   date3 = resolve_as_of()
   print(f"Environment variable: {date3}")

   # Resolve default (None)
   date4 = resolve_as_of()
   print(f"Default: {date4}")

get_verbose()
~~~~~~~~~~~~~

Get the verbose logging setting:

.. code-block:: python

   from barangay.config import get_verbose
   import os

   # Default (true)
   verbose = get_verbose()
   print(f"Verbose (default): {verbose}")

   # Set to false
   os.environ["BARANGAY_VERBOSE"] = "false"
   verbose = get_verbose()
   print(f"Verbose (false): {verbose}")

get_cache_dir()
~~~~~~~~~~~~~~~

Get the cache directory path:

.. code-block:: python

   from barangay.config import get_cache_dir
   import os

   # Default cache directory
   cache_dir = get_cache_dir()
   print(f"Cache directory (default): {cache_dir}")

   # Custom cache directory
   os.environ["BARANGAY_CACHE_DIR"] = "/custom/cache"
   cache_dir = get_cache_dir()
   print(f"Cache directory (custom): {cache_dir}")

load_env_config()
~~~~~~~~~~~~~~~~~

Load all configuration from environment variables:

.. code-block:: python

   from barangay.config import load_env_config
   import os

   # Set environment variables
   os.environ["BARANGAY_AS_OF"] = "2025-07-08"
   os.environ["BARANGAY_VERBOSE"] = "true"
   os.environ["BARANGAY_CACHE_DIR"] = "/custom/cache"

   # Load configuration
   config = load_env_config()
   print("Configuration:")
   for key, value in config.items():
       print(f"  {key}: {value}")

Complete Example
----------------

Here's a complete example demonstrating various configuration options:

.. code-block:: python

   import os
   import logging
   from barangay import search, current, available_dates, as_of
   from barangay.config import (
       load_env_config,
       resolve_as_of,
       get_verbose,
       get_cache_dir,
   )

   class BarangayConfigDemo:
       """Demonstrate configuration options."""

       def __init__(self):
           # Configure logging
           logging.basicConfig(
               level=logging.INFO,
               format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
           )

       def demo_environment_variables(self):
           """Demonstrate environment variable configuration."""
           print("\n=== Environment Variables ===")

           # Set environment variables
           os.environ["BARANGAY_AS_OF"] = "2025-07-08"
           os.environ["BARANGAY_VERBOSE"] = "true"

           # Load configuration
           config = load_env_config()
           print("Configuration from environment:")
           for key, value in config.items():
               print(f"  {key}: {value}")

           # Use configuration
           results = search("Tongmageng")
           print(f"Results: {len(results)}")

       def demo_module_attributes(self):
           """Demonstrate module attribute configuration."""
           print("\n=== Module Attributes ===")

           # Display module attributes
           print(f"Current dataset: {current}")
           print(f"Available dates: {available_dates}")
           print(f"Default as_of: {as_of}")

           # Set module attribute
           import barangay
           barangay.as_of = "2025-08-29"
           print(f"Updated as_of: {barangay.as_of}")

           # Use configuration
           results = search("Tongmageng")
           print(f"Results: {len(results)}")

       def demo_function_parameters(self):
           """Demonstrate function parameter configuration."""
           print("\n=== Function Parameters ===")

           # Use different dates
           dates = ["2025-07-08", "2025-08-29", "2025-10-13"]
           for date in dates:
               results = search("Tongmageng", as_of=date)
               print(f"Date {date}: {len(results)} results")

       def demo_configuration_priority(self):
           """Demonstrate configuration priority."""
           print("\n=== Configuration Priority ===")

           # Set environment variable
           os.environ["BARANGAY_AS_OF"] = "2025-07-08"
           print(f"Environment variable: {os.environ['BARANGAY_AS_OF']}")

           # Set module attribute
           import barangay
           barangay.as_of = "2025-08-29"
           print(f"Module attribute: {barangay.as_of}")

           # Use function parameter
           results = search("Tongmageng", as_of="2025-10-13")
           print(f"Function parameter: 2025-10-13")
           print(f"Actual date used: 2025-10-13 (highest priority)")

       def demo_cache_configuration(self):
           """Demonstrate cache configuration."""
           print("\n=== Cache Configuration ===")

           # Default cache directory
           cache_dir = get_cache_dir()
           print(f"Default cache directory: {cache_dir}")

           # Custom cache directory
           os.environ["BARANGAY_CACHE_DIR"] = "/tmp/barangay_cache"
           cache_dir = get_cache_dir()
           print(f"Custom cache directory: {cache_dir}")

       def demo_verbose_configuration(self):
           """Demonstrate verbose configuration."""
           print("\n=== Verbose Configuration ===")

           # Check verbose setting
           verbose = get_verbose()
           print(f"Verbose logging: {verbose}")

           # Toggle verbose
           os.environ["BARANGAY_VERBOSE"] = "false"
           verbose = get_verbose()
           print(f"Verbose logging (disabled): {verbose}")

   # Run demo
   demo = BarangayConfigDemo()
   demo.demo_environment_variables()
   demo.demo_module_attributes()
   demo.demo_function_parameters()
   demo.demo_configuration_priority()
   demo.demo_cache_configuration()
   demo.demo_verbose_configuration()

Next Steps
----------

Now that you understand configuration, explore these topics:

* :doc:`search` - Learn about fuzzy search features
* :doc:`data_models` - Detailed information about data structures
* :doc:`historical_data` - How to access historical data
* :doc:`performance` - Performance optimization tips

For API reference, see :doc:`../api_reference/config`.