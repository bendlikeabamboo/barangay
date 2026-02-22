Troubleshooting Guide
=====================

This guide provides solutions to common issues when using the barangay package, organized by error type for quick lookup.

.. contents::
   :local:
   :depth: 2

Installation Issues
-------------------

Python Version Incompatible
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ERROR: Package 'barangay' requires a different Python: 3.9.x not in '>=3.10'

**Cause:** The barangay package requires Python 3.10 or higher.

**Solution:**

1. Check your Python version:

   .. code-block:: bash

      python --version

2. Upgrade to Python 3.10 or higher:

   * **Linux/macOS:** Use pyenv or your package manager
   * **Windows:** Download from `python.org <https://www.python.org/downloads/>`_

3. Verify the new version:

   .. code-block:: bash

      python3.10 --version

.. tip:: Using a virtual environment is recommended to manage Python versions.

Permission Denied
~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied

**Cause:** Insufficient permissions to install packages globally.

**Solution:**

Option 1 - Use ``--user`` flag:

.. code-block:: bash

   pip install --user barangay

Option 2 - Use a virtual environment (recommended):

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install barangay

Option 3 - Use ``sudo`` (Linux/macOS, not recommended):

.. code-block:: bash

   sudo pip install barangay

.. warning:: Using ``sudo`` can cause permission issues with system packages. Virtual environments are safer.

Dependency Conflicts
~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ERROR: pip's dependency resolver does not currently take into account all the packages that are installed.

**Cause:** Conflicts with existing packages in your environment.

**Solution:**

1. Create a fresh virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Upgrade pip:

   .. code-block:: bash

      pip install --upgrade pip

3. Install barangay:

   .. code-block:: bash

      pip install barangay

4. If using ``uv``, it handles dependencies more efficiently:

   .. code-block:: bash

      uv pip install barangay

Slow Download
~~~~~~~~~~~~~

**Error:** Download is very slow or times out.

**Cause:** Network issues or slow PyPI mirror.

**Solution:**

Option 1 - Use a different PyPI mirror:

.. code-block:: bash

   pip install -i https://pypi.org/simple barangay

Option 2 - Download and install manually:

.. code-block:: bash

   pip download barangay
   pip install barangay-*.whl

Option 3 - Use a faster mirror:

.. code-block:: bash

   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple barangay

Import Errors
-------------

ModuleNotFoundError
~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ModuleNotFoundError: No module named 'barangay'

**Cause:** The package is not installed or not in the current Python environment.

**Solution:**

1. Verify installation:

   .. code-block:: bash

      pip list | grep barangay

2. If not installed, install it:

   .. code-block:: bash

      pip install barangay

3. If installed but not found, check your Python path:

   .. code-block:: python

      import sys
      print(sys.path)

4. Ensure you're using the correct Python environment:

   .. code-block:: bash

      which python  # Linux/macOS
      where python  # Windows

5. If using a virtual environment, make sure it's activated:

   .. code-block:: bash

      source venv/bin/activate  # On Windows: venv\Scripts\activate

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ModuleNotFoundError: No module named 'pandas'
   ModuleNotFoundError: No module named 'rapidfuzz'
   ModuleNotFoundError: No module named 'pydantic'

**Cause:** Dependencies not installed properly.

**Solution:**

1. Reinstall barangay with dependencies:

   .. code-block:: bash

      pip uninstall barangay
      pip install barangay

2. Or install missing dependencies manually:

   .. code-block:: bash

      pip install pandas rapidfuzz pydantic requests python-dotenv fastparquet

3. Verify all dependencies are installed:

   .. code-block:: bash

      pip list | grep -E "(pandas|rapidfuzz|pydantic|requests|fastparquet)"

ImportError: DLL Load Failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ImportError: DLL load failed while importing _fuzzy

**Cause:** Incompatible binary dependencies, especially on Windows.

**Solution:**

1. Uninstall and reinstall:

   .. code-block:: bash

      pip uninstall rapidfuzz
      pip install rapidfuzz

2. Use pre-built wheels:

   .. code-block:: bash

      pip install --only-binary :all: rapidfuzz

3. If on Windows, ensure you have the latest Visual C++ Redistributable

Search Issues
-------------

No Results Found
~~~~~~~~~~~~~~~~

**Error:** Search returns empty list.

.. code-block:: python

   results = search("Invalid Barangay Name")
   print(results)  # []

**Cause:** Search string doesn't match any barangays above the threshold.

**Solution:**

1. Lower the threshold:

   .. code-block:: python

      from barangay import search

      results = search("Invalid Barangay Name", threshold=40.0)

2. Check for typos:

   .. code-block:: python

      # Try variations
      results = search("Tongmagen")  # Typo
      results = search("Tongmageng")  # Correct

3. Use partial matches:

   .. code-block:: python

      results = search("Tong")  # Partial match

4. Verify the barangay exists:

   .. code-block:: python

      from barangay import BARANGAY_FLAT

      # Search in flat data
      matches = [b for b in BARANGAY_FLAT if "Tong" in b['name'].lower()]
      print(matches)

5. Check available data:

   .. code-block:: python

      from barangay import current

      print(f"Using data from: {current}")

Search Performance Issues
~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:** Search takes too long or times out.

**Cause:** Large dataset, inefficient search parameters, or system resource constraints.

**Solution:**

1. Reuse FuzzBase for multiple searches:

   .. code-block:: python

      from barangay import search, create_fuzz_base

      # Create once (expensive)
      fuzz_base = create_fuzz_base()

      # Reuse for multiple searches (fast)
      results1 = search("San Jose", fuzz_base=fuzz_base)
      results2 = search("Quezon City", fuzz_base=fuzz_base)

2. Reduce match hooks:

   .. code-block:: python

      from barangay import search

      # Slower (all hooks)
      results = search("San Jose", match_hooks=["province", "municipality", "barangay"])

      # Faster (fewer hooks)
      results = search("San Jose", match_hooks=["barangay"])

3. Limit results:

   .. code-block:: python

      results = search("San Jose", n=3)

4. Increase threshold:

   .. code-block:: python

      results = search("San Jose", threshold=80.0)

5. Use system monitoring to identify bottlenecks:

   .. code-block:: python

      import time

      start = time.time()
      results = search("San Jose")
      elapsed = time.time() - start
      print(f"Search took {elapsed:.3f} seconds")

Invalid Match Hooks
~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ValueError: Invalid match_hooks: ['invalid_level']. Valid options: ['province', 'municipality', 'barangay']

**Cause:** Using invalid administrative level in ``match_hooks`` parameter.

**Solution:**

Use only valid match hooks:

.. code-block:: python

   from barangay import search

   # Valid match hooks
   valid_hooks = ["province", "municipality", "barangay"]

   # Correct usage
   results = search("San Jose", match_hooks=["barangay"])
   results = search("San Jose", match_hooks=["municipality", "barangay"])
   results = search("San Jose", match_hooks=["province", "municipality", "barangay"])

   # Invalid (will raise ValueError)
   # results = search("San Jose", match_hooks=["invalid_level"])

Data Issues
-----------

FileNotFoundError
~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   FileNotFoundError: [Errno 2] No such file or directory: 'barangay/data/barangay.json'

**Cause:** Package data files are missing or corrupted.

**Solution:**

1. Reinstall the package:

   .. code-block:: bash

      pip uninstall barangay
      pip install barangay

2. Verify installation:

   .. code-block:: python

      import os
      import barangay

      package_path = os.path.dirname(barangay.__file__)
      print(f"Package path: {package_path}")

      data_path = os.path.join(package_path, "data", "barangay.json")
      print(f"Data file exists: {os.path.exists(data_path)}")

3. If data file is missing, try using DataManager to download:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()
      data = dm.get_data(data_type="basic")

4. Check for corrupted installation:

   .. code-block:: bash

      pip show barangay
      pip check

JSONDecodeError
~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

**Cause:** JSON data file is corrupted or empty.

**Solution:**

1. Reinstall the package:

   .. code-block:: bash

      pip uninstall barangay
      pip install barangay

2. Clear cache and reload:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()
      dm.clear_cache()
      data = dm.get_data(data_type="basic")

3. Use alternative data format (YAML):

   .. code-block:: python

      from barangay import load_barangay_data

      # Try loading YAML instead
      import yaml
      with open('barangay/data/barangay.yaml', 'r') as f:
          data = yaml.safe_load(f)

Data Type Not Found
~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ValueError: Invalid data_type: 'invalid_type'. Valid options: ['basic', 'extended', 'flat']

**Cause:** Using invalid data type parameter.

**Solution:**

Use only valid data types:

.. code-block:: python

   from barangay.data_manager import DataManager

   dm = DataManager()

   # Valid data types
   data = dm.get_data(data_type="basic")
   data = dm.get_data(data_type="extended")
   data = dm.get_data(data_type="flat")

   # Invalid (will raise ValueError)
   # data = dm.get_data(data_type="invalid_type")

Network Issues
--------------

ConnectionError
~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   requests.exceptions.ConnectionError: Failed to establish a new connection

**Cause:** No internet connection or network issues.

**Solution:**

1. Check internet connection:

   .. code-block:: bash

      ping github.com

2. Use bundled data instead of downloading:

   .. code-block:: python

      from barangay import load_barangay_data

      # Use bundled data (no download required)
      data = load_barangay_data()

3. Configure proxy if needed:

   .. code-block:: python

      import os

      os.environ['HTTP_PROXY'] = 'http://proxy.example.com:8080'
      os.environ['HTTPS_PROXY'] = 'http://proxy.example.com:8080'

4. Retry with exponential backoff:

   .. code-block:: python

      from barangay.data_manager import DataManager
      import time

      dm = DataManager()

      for attempt in range(3):
          try:
              data = dm.get_data(as_of="2025-07-08")
              break
          except Exception as e:
              if attempt < 2:
                  wait_time = 2 ** attempt
                  print(f"Attempt {attempt + 1} failed. Retrying in {wait_time}s...")
                  time.sleep(wait_time)
              else:
                  raise

HTTPError / 404 Not Found
~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   requests.exceptions.HTTPError: 404 Client Error: Not Found

**Cause:** Invalid date or data not available for the specified date.

**Solution:**

1. Check available dates:

   .. code-block:: python

      from barangay import get_available_dates

      dates = get_available_dates()
      print(f"Available dates: {dates}")

2. Use a valid date:

   .. code-block:: python

      from barangay import search

      # Valid date
      results = search("Tongmageng", as_of="2025-07-08")

      # Invalid date (will raise error)
      # results = search("Tongmageng", as_of="2020-01-01")

3. Use latest bundled data:

   .. code-block:: python

      from barangay import search

      # Use latest data (no date specified)
      results = search("Tongmageng")

TimeoutError
~~~~~~~~~~~~

**Error:**

.. code-block:: text

   requests.exceptions.Timeout: Request timed out

**Cause:** Slow network or large file download.

**Solution:**

1. Use bundled data:

   .. code-block:: python

      from barangay import load_barangay_data

      data = load_barangay_data()

2. Download during off-peak hours

3. Use a faster network connection

Rate Limiting
~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   requests.exceptions.HTTPError: 429 Client Error: Too Many Requests

**Cause:** GitHub API rate limit exceeded.

**Solution:**

1. Wait and retry:

   .. code-block:: python

      from barangay.data_manager import DataManager
      import time

      dm = DataManager()

      for attempt in range(5):
          try:
              data = dm.get_data(as_of="2025-07-08")
              break
          except Exception as e:
              if '429' in str(e) and attempt < 4:
                  wait_time = 60 * (attempt + 1)  # Wait 1, 2, 3, 4 minutes
                  print(f"Rate limited. Waiting {wait_time}s...")
                  time.sleep(wait_time)
              else:
                  raise

2. Use bundled data to avoid downloads:

   .. code-block:: python

      from barangay import load_barangay_data

      data = load_barangay_data()

3. Cache data locally to avoid repeated downloads:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()
      # First download will cache the data
      data = dm.get_data(as_of="2025-07-08")
      # Subsequent calls use cache (no rate limit)
      data = dm.get_data(as_of="2025-07-08")

Cache Issues
------------

Cache Corruption
~~~~~~~~~~~~~~~~

**Error:** Unexpected errors when loading cached data.

**Cause:** Cache files are corrupted or incompatible.

**Solution:**

1. Clear cache:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()
      dm.clear_cache()

2. Manually delete cache directory:

   .. code-block:: bash

      # Find cache location
      python -c "from barangay.data_manager import DataManager; dm = DataManager(); print(dm.cache_dir)"

      # Delete cache directory
      rm -rf ~/.cache/barangay  # Linux/macOS
      # or
      del %USERPROFILE%\.cache\barangay  # Windows

3. Reload data:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()
      data = dm.get_data(data_type="basic")

Cache Permission Denied
~~~~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   PermissionError: [Errno 13] Permission denied: '/path/to/cache'

**Cause:** Insufficient permissions to write to cache directory.

**Solution:**

1. Check cache directory permissions:

   .. code-block:: bash

      ls -la ~/.cache/barangay  # Linux/macOS

2. Fix permissions:

   .. code-block:: bash

      chmod -R 755 ~/.cache/barangay  # Linux/macOS

3. Set custom cache directory with write permissions:

   .. code-block:: python

      from barangay.data_manager import DataManager
      import os

      # Use a directory you have write access to
      cache_dir = os.path.expanduser("~/my_cache")
      os.makedirs(cache_dir, exist_ok=True)

      dm = DataManager(cache_dir=cache_dir)
      data = dm.get_data(data_type="basic")

4. Run with appropriate permissions:

   .. code-block:: bash

      # Avoid running as root/sudo if possible
      # Instead, fix directory ownership
      sudo chown -R $USER:$USER ~/.cache/barangay

Cache Disk Full
~~~~~~~~~~~~~~~

**Error:** Cannot write to cache due to insufficient disk space.

**Cause:** Disk is full or cache directory quota exceeded.

**Solution:**

1. Check disk space:

   .. code-block:: bash

      df -h  # Linux/macOS
      # or
      dir  # Windows

2. Clear old cache files:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()
      dm.clear_cache()

3. Use a different cache location with more space:

   .. code-block:: python

      from barangay.data_manager import DataManager
      import os

      cache_dir = "/path/to/larger/disk/cache"
      os.makedirs(cache_dir, exist_ok=True)

      dm = DataManager(cache_dir=cache_dir)
      data = dm.get_data(data_type="basic")

4. Disable caching (not recommended):

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager(cache_enabled=False)
      data = dm.get_data(data_type="basic")

.. warning:: Disabling caching will cause data to be downloaded on every load, which is slow and may hit rate limits.

Configuration Issues
--------------------

Invalid Date Format
~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   ValueError: Invalid date format. Expected YYYY-MM-DD, got '2025/07/08'

**Cause:** Using incorrect date format.

**Solution:**

Use YYYY-MM-DD format:

.. code-block:: python

   from barangay import search

   # Correct format
   results = search("Tongmageng", as_of="2025-07-08")

   # Incorrect format (will raise ValueError)
   # results = search("Tongmageng", as_of="2025/07/08")
   # results = search("Tongmageng", as_of="July 8, 2025")
   # results = search("Tongmageng", as_of="08-07-2025")

Environment Variable Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:** Unexpected behavior due to environment variables.

**Cause:** Conflicting or incorrect environment variable settings.

**Solution:**

1. Check environment variables:

   .. code-block:: python

      import os

      print(f"BARANGAY_CACHE_DIR: {os.environ.get('BARANGAY_CACHE_DIR')}")
      print(f"BARANGAY_VERBOSE: {os.environ.get('BARANGAY_VERBOSE')}")

2. Unset conflicting variables:

   .. code-block:: bash

      unset BARANGAY_CACHE_DIR
      unset BARANGAY_VERBOSE

3. Set correct variables:

   .. code-block:: bash

      export BARANGAY_CACHE_DIR="/path/to/cache"
      export BARANGAY_VERBOSE="1"

4. Or set in Python:

   .. code-block:: python

      import os

      os.environ['BARANGAY_CACHE_DIR'] = '/path/to/cache'
      os.environ['BARANGAY_VERBOSE'] = '1'

Best Practices for Troubleshooting
----------------------------------

1. **Enable verbose logging:**

   .. code-block:: python

      import os
      import logging

      os.environ['BARANGAY_VERBOSE'] = '1'
      logging.basicConfig(level=logging.DEBUG)

2. **Use try-except blocks:**

   .. code-block:: python

      from barangay import search

      try:
          results = search("Tongmageng")
      except Exception as e:
          print(f"Error: {e}")
          # Handle error appropriately

3. **Validate inputs:**

   .. code-block:: python

      from barangay import get_available_dates

      dates = get_available_dates()
      if "2025-07-08" in dates:
          results = search("Tongmageng", as_of="2025-07-08")
      else:
          print("Date not available")

4. **Check package version:**

   .. code-block:: python

      import barangay

      print(f"Package version: {barangay.__version__ if hasattr(barangay, '__version__') else 'unknown'}")
      print(f"Data version: {barangay.current}")

5. **Test with simple examples:**

   .. code-block:: python

      from barangay import search

      # Test with known good data
      results = search("Tongmageng, Tawi-Tawi")
      print(f"Found {len(results)} results")

6. **Report issues with details:**

   * Python version
   * Package version
   * Error message
   * Minimal reproducible example
   * System information

See Also
--------

* :doc:`performance` - Performance troubleshooting
* :doc:`../advanced/error_handling` - Comprehensive error handling guide
* :doc:`../quick_start/installation` - Installation guide