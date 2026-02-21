Installation
============

This guide will help you install the barangay package and verify that it's working correctly.

.. note:: If you're using a virtual environment (recommended), make sure it's activated before installing.

Install from PyPI
-----------------

The easiest way to install barangay is from PyPI using pip:

.. code-block:: bash

   pip install barangay

This will install the latest version of barangay along with all its dependencies.

Install a Specific Version
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need a specific version, specify it with:

.. code-block:: bash

   pip install barangay==2026.1.13.1

.. tip::

   Starting with v2026.1.13.1, all versions now have access to historical data using the
   "as_of" configuration.

Install from Source
-------------------

If you want to install from source, you can clone the repository and install:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/bendlikeabamboo/barangay.git
   cd barangay

   # Install in development mode
   pip install -e .

Or using uv (recommended for development):

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/bendlikeabamboo/barangay.git
   cd barangay

   # Install with uv
   uv pip install -e .

Verify Installation
-------------------

After installation, verify that barangay is installed correctly:

.. code-block:: bash

   barangay --version

You should see the current version (e.g., ``2026-01-13``).

You can also check the package version:

.. code-block:: bash

   pip show barangay

Output:

.. code-block:: txt

   Name: barangay
   Version: 2026.1.13.1
   Summary: Philippines Standard Geographic Code (PSGC) 2026 Python package, Fuzzy Search, JSON, and YAML.
   ...

Test a Basic Search
~~~~~~~~~~~~~~~~~~~

To verify that everything is working, try a basic search in Python:

.. code-block:: python

   from barangay import search

   results = search("Tongmageng, Tawi-Tawi")

Expected output:

.. code-block:: text

   [
      {
         'barangay': 'Tongmageng',
         'province_or_huc': 'Tawi-Tawi',
         'municipality_or_city': 'Sitangkai',
         'psgc_id': '1907005010',
         'f_0p0b_ratio_score': 100.0,
         'f_00mb_ratio_score': 76.92307692307692,
         'f_0pmb_ratio_score': 79.16666666666666,
         '000b': 'tongmageng',
         '0p0b': 'tawitawi tongmageng',
         '00mb': 'sitangkai tongmageng',
         '0pmb': 'tawitawi sitangkai tongmageng'
      }
   ]

Dependencies
------------

These packages are required before installing the package:

* **Python 3.13 or higher** - The package requires Python 3.13 or newer
* **pip** - Python's package installer (usually included with Python)

The package automatically installs the following dependencies:

* **pandas** (>=2.3.2, <3.0.0) - For data manipulation and analysis
* **fastparquet** (>=2024.11.0, <2025.0.0) - For reading Parquet files
* **rapidfuzz** (>=3.14.0, <4.0.0) - For fuzzy string matching
* **pydantic** (>=2.11.7, <3.0.0) - For data validation
* **requests** (>=2.32.0) - For downloading data from GitHub
* **python-dotenv** (>=1.0.0) - For loading environment variables


Troubleshooting
---------------

Python Version Incompatible
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you see an error like:

.. code-block:: text

   ERROR: Package 'barangay' requires a different Python: 3.9.x not in '>=3.13'

You need to upgrade Python to version 3.13 or higher. Check your Python version:

.. code-block:: bash

   python --version

Permission Denied
~~~~~~~~~~~~~~~~~

If you get a permission error during installation, try:

.. code-block:: bash

   pip install --user barangay

Or use a virtual environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install barangay

Import Error
~~~~~~~~~~~~

If you get an ``ImportError`` when trying to import barangay:

.. code-block:: text

   ModuleNotFoundError: No module named 'barangay'

Try reinstalling the package:

.. code-block:: bash

   pip uninstall barangay
   pip install barangay

Or if you're in a virtual environment, make sure it's activated.

Dependency Conflicts
~~~~~~~~~~~~~~~~~~~~

If you encounter dependency conflicts, try installing in a fresh virtual environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install --upgrade pip
   pip install barangay

Slow Download
~~~~~~~~~~~~~

If the download is slow, try using a different PyPI mirror:

.. code-block:: bash

   pip install -i https://pypi.org/simple barangay

Or download the wheel file and install it directly:

.. code-block:: bash

   pip download barangay
   pip install barangay-*.whl

Development Installation
------------------------

For development, it's recommended to install the package in editable mode along with development dependencies:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/bendlikeabamboo/barangay.git
   cd barangay

   # Install with development dependencies using uv
   uv pip install -e ".[dev]"

   # Or using pip
   pip install -e ".[dev]"

This will install:

* The package in editable mode (changes to source code are immediately reflected)
* Development tools (pytest, ruff, mypy, etc.)
* Documentation tools (sphinx, furo, etc.)

.. tip:: Using ``uv`` is recommended for faster dependency resolution and installation.

Next Steps
----------

Now that you have barangay installed, check out these guides:

* :doc:`first_search` - Learn how to perform your first search
* :doc:`data_models_overview` - Understand the different data models available
* :doc:`../user_guide/search` - Comprehensive guide to fuzzy search
* :doc:`../user_guide/configuration` - Configure the package for your needs

If you encounter any issues not covered here, please check the :doc:`../troubleshooting/common_errors` guide or `report an issue <https://github.com/bendlikeabamboo/barangay/issues>`_.