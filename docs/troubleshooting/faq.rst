Frequently Asked Questions
==========================

This section covers frequently asked questions about the barangay package.

General Questions
-----------------

What is the barangay package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The barangay package is a Python library that provides Philippine geographic and administrative data with fuzzy search capabilities. It's based on the Philippine Standard Geographic Code (PSGC) masterlist from the Philippine Statistics Authority (PSA).

Key features:

* **Fuzzy search**: Find barangays even with typos or variations
* **Multiple data models**: Choose the structure that fits your use case
* **Historical data**: Access previous PSGC releases by date
* **Smart caching**: Automatic caching for faster subsequent loads
* **Multiple formats**: JSON, YAML, and Python dictionary formats

What data does the package include?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package includes comprehensive Philippine administrative data:

* **Regions**: 17 administrative regions including NCR, CAR, and ARMM
* **Provinces**: 81 provinces
* **Cities/Municipalities**: Highly Urbanized Cities (HUCs), Independent Component Cities (ICCs), Component Cities, and Municipalities
* **Barangays**: Over 42,000 barangays nationwide
* **PSGC Codes**: Philippine Standard Geographic Codes for all administrative units
* **Metadata**: Administrative types, hierarchy information, and geographic classifications

What is the data source?
~~~~~~~~~~~~~~~~~~~~~~~~

The data is sourced from the `Philippine Statistics Authority (PSA) <https://psa.gov.ph/classification/psgc>`_ PSGC masterlist. The package uses the January 2026 masterlist as the current version.

Historical data is also available from previous PSGC releases:
* 2025-07-08
* 2025-08-29
* 2025-10-13
* 2026-01-13 (current)

How often is the data updated?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package is updated when new PSGC masterlists are released by the PSA. The current version (2026-01-13) was released in January 2026.

Historical data is preserved to allow analysis of administrative changes over time.

Is the data free to use?
~~~~~~~~~~~~~~~~~~~~~~~~

Yes, the PSGC data is public domain and free to use. The barangay package is licensed under the MIT License.

What Python version is required?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package requires **Python 3.10 or higher**.

Check your Python version:

.. code-block:: bash

   python --version

If you have an older version, upgrade to Python 3.10+.

Usage Questions
---------------

How do I perform a basic search?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest search uses all default parameters:

.. code-block:: python

   from barangay import search

   results = search("Tongmageng, Tawi-Tawi")
   print(results[0]['barangay'])  # Tongmageng

See :doc:`../quick_start/first_search` for more details.

How do I search for a specific barangay?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search by barangay name:

.. code-block:: python

   from barangay import search

   results = search("Tongmageng")
   for result in results:
       print(f"{result['barangay']}, {result['province_or_huc']}")

How do I search by city or municipality?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search by city or municipality name:

.. code-block:: python

   from barangay import search

   results = search("Quezon City")
   for result in results:
       print(f"{result['barangay']}, {result['municipality_or_city']}")

How do I search by province?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search by province name:

.. code-block:: python

   from barangay import search

   results = search("Tawi-Tawi")
   for result in results:
       print(f"{result['barangay']}, {result['municipality_or_city']}")

How do I handle typos in search?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fuzzy search automatically handles typos:

.. code-block:: python

   from barangay import search

   # Typo: "Tongmagen" instead of "Tongmageng"
   results = search("Tongmagen, Tawi-Tawi")
   print(results[0]['barangay'])  # Tongmageng

The fuzzy matching uses the token sort ratio algorithm, which is robust to:
* Typos and misspellings
* Word order variations
* Partial matches
* Common abbreviations

How do I get more search results?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``n`` parameter to get more results:

.. code-block:: python

   from barangay import search

    # Get top 10 results
    results = search("San Jose", n=10)
    for i, result in enumerate(results, 1):
        # Get the maximum score from active matching strategies
        scores = [
            result.get('f_000b_ratio_score', 0),
            result.get('f_0p0b_ratio_score', 0),
            result.get('f_00mb_ratio_score', 0),
            result.get('f_0pmb_ratio_score', 0)
        ]
        score = max(scores)
        print(f"{i}. {result['barangay']} ({score:.1f}%)")

How do I filter results by similarity score?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``threshold`` parameter:

.. code-block:: python

   from barangay import search

   # Only high-confidence matches (90%+)
   results = search("San Jose", threshold=90.0)

   # Medium confidence (70%+)
   results = search("San Jose", threshold=70.0)

   # Low confidence (60%+, default)
   results = search("San Jose", threshold=60.0)

How do I use historical data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``as_of`` parameter with a date:

.. code-block:: python

   from barangay import search

   # Search with data from July 8, 2025
   results = search("Tongmageng", as_of="2025-07-08")

Available dates:

.. code-block:: python

   from barangay import get_available_dates

   dates = get_available_dates()
   print(dates)  # ['2025-07-08', '2025-08-29', '2025-10-13']

See :doc:`../user_guide/historical_data` for more details.

How do I access the full dataset?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load the complete dataset:

.. code-block:: python

   from barangay import BARANGAY, BARANGAY_EXTENDED, BARANGAY_FLAT

   # Basic nested structure
   ncr_cities = list(BARANGAY["National Capital Region (NCR)"].keys())

   # Extended recursive structure
   ncr = [item for item in BARANGAY_EXTENDED["components"]
          if item["name"] == "National Capital Region (NCR)"][0]

   # Flat list
   brgys = [b for b in BARANGAY_FLAT if b['province_or_huc'] == "NCR"]

See :doc:`../user_guide/data_models` for more details.

Technical Questions
-------------------

What is fuzzy search?
~~~~~~~~~~~~~~~~~~~~~

Fuzzy search is a technique that finds matches even when the search string doesn't exactly match the target data. The barangay package uses the `RapidFuzz <https://github.com/maxbachmann/RapidFuzz>`_ library, which implements the **token sort ratio** algorithm.

The algorithm:

1. Splits strings into tokens (words)
2. Sorts the tokens alphabetically
3. Compares the sorted token sequences
4. Returns a similarity score from 0-100

This is ideal for Philippine addresses which often have variations like:
* "San Jose" vs "Sanjose"
* "City of Manila" vs "Manila City"
* "Barangay 1" vs "Brgy. 1"

What are match hooks?
~~~~~~~~~~~~~~~~~~~~~

Match hooks determine which administrative levels to match against:

* ``"barangay"`` - Match barangay names only
* ``"municipality"`` - Match municipality/city names
* ``"province"`` - Match province/HUC names

Default: ``["province", "municipality", "barangay"]``

.. code-block:: python

   from barangay import search

   # Match only barangay names (fastest)
   results = search("San Jose", match_hooks=["barangay"])

   # Match municipality and barangay
   results = search("San Jose", match_hooks=["municipality", "barangay"])

   # Match all levels (default, most comprehensive)
   results = search("San Jose", match_hooks=["province", "municipality", "barangay"])

What is a FuzzBase?
~~~~~~~~~~~~~~~~~~~

A FuzzBase is a pre-computed data structure that contains sanitized strings and pre-computed fuzzy matching functions. Creating a FuzzBase is computationally expensive, but reusing it for multiple searches significantly improves performance.

.. code-block:: python

   from barangay import search, create_fuzz_base

   # Create FuzzBase once (expensive)
   fuzz_base = create_fuzz_base()

   # Reuse for multiple searches (fast)
   results1 = search("San Jose", fuzz_base=fuzz_base)
   results2 = search("Quezon City", fuzz_base=fuzz_base)
   results3 = search("Manila", fuzz_base=fuzz_base)

What is the difference between the data models?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package provides three data models:

**BARANGAY (Basic)**
* Nested dictionary structure
* Best for simple lookups
* Format: ``region → city → barangay``
* Size: ~50 MB

**BARANGAY_EXTENDED**
* Recursive structure with rich metadata
* Handles complex hierarchies (HUCs, municipalities directly under regions)
* Best for complex administrative queries
* Size: ~200 MB

**BARANGAY_FLAT**
* Flat list with parent references
* Best for search, filtering, and DataFrame operations
* Each entry has ``parent_psgc_id`` to trace hierarchy
* Size: ~100 MB

See :doc:`../user_guide/data_models` for more details.

How does caching work?
~~~~~~~~~~~~~~~~~~~~~~

The package automatically caches downloaded data:

* **Location**: ``~/.cache/barangay`` (Linux/macOS) or ``%USERPROFILE%\.cache\barangay`` (Windows)
* **Behavior**: First download is cached, subsequent loads use cache
* **Expiration**: No automatic expiration
* **Management**: Use ``DataManager.clear_cache()`` to clear cache

.. code-block:: python

   from barangay.data_manager import DataManager

   dm = DataManager()

   # First load (downloads and caches)
   data = dm.get_data(as_of="2025-07-08")

   # Second load (uses cache, much faster)
   data = dm.get_data(as_of="2025-07-08")

   # Clear cache if needed
   dm.clear_cache()

See :doc:`../advanced/caching` for more details.

Best Practices
--------------

How do I optimize search performance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Reuse FuzzBase** for multiple searches:

   .. code-block:: python

      from barangay import search, create_fuzz_base

      fuzz_base = create_fuzz_base()
      results = [search(addr, fuzz_base=fuzz_base) for addr in addresses]

2. **Use appropriate match hooks**:

   .. code-block:: python

      # Faster (only barangay)
      results = search("San Jose", match_hooks=["barangay"])

3. **Increase threshold** for high-confidence searches:

   .. code-block:: python

      results = search("San Jose", threshold=80.0)

4. **Limit results** to what you need:

   .. code-block:: python

      results = search("San Jose", n=3)

See :doc:`performance` for more optimization tips.

How do I validate search results?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the similarity score:

.. code-block:: python

   from barangay import search

   results = search("Tongmagen, Tawi-Tawi")

    if results:
        best = results[0]
        # Get the maximum score from active matching strategies
        scores = [
            best.get('f_000b_ratio_score', 0),
            best.get('f_0p0b_ratio_score', 0),
            best.get('f_00mb_ratio_score', 0),
            best.get('f_0pmb_ratio_score', 0)
        ]
        score = max(scores)

        if score >= 90:
            confidence = "High"
        elif score >= 70:
            confidence = "Medium"
        else:
            confidence = "Low"

        print(f"Match: {best['barangay']}")
        print(f"Score: {score:.1f}% ({confidence})")
   else:
       print("No matches found")

How do I handle no results?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check if results list is empty:

.. code-block:: python

   from barangay import search

   results = search("Invalid Barangay Name")

   if not results:
       print("No matches found. Try:")
       print("1. Lowering the threshold")
       print("2. Checking for typos")
       print("3. Using a partial match")
   else:
       print(f"Found {len(results)} matches")

How do I batch process addresses?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use FuzzBase reuse for efficiency:

.. code-block:: python

   from barangay import search, create_fuzz_base

   def batch_search(addresses, threshold=70.0, n=5):
       """Search multiple addresses efficiently."""
       fuzz_base = create_fuzz_base()

       results = {}
       for address in addresses:
           matches = search(
               address,
               fuzz_base=fuzz_base,
               threshold=threshold,
               n=n
           )
           results[address] = matches

       return results

   addresses = [
       "Tongmageng, Tawi-Tawi",
       "San Jose, City of Manila",
       "Quezon City",
   ]

   results = batch_search(addresses)

Version Compatibility
---------------------

Can I use this with Python 2?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, the package requires Python 3.10 or higher. Python 2 is no longer supported.

Can I use this with Django/Flask?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, the package works with any Python web framework:

.. code-block:: python

   # Flask example
   from flask import Flask
   from barangay import search

   app = Flask(__name__)

   @app.route('/search')
   def search_address():
       query = request.args.get('q')
       results = search(query)
       return jsonify(results)

Can I use this with pandas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, the package integrates well with pandas:

.. code-block:: python

   import pandas as pd
   from barangay import BARANGAY_FLAT

   # Convert to DataFrame
   df = pd.DataFrame(BARANGAY_FLAT)

   # Filter
   ncr_brgys = df[df['province_or_huc'] == 'National Capital Region (NCR)']

   # Search
   from barangay import search
   results = search("San Jose")
   result_df = pd.DataFrame(results)

Can I use this in production?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, the package is production-ready. For production use:

1. **Use caching**: Data is automatically cached
2. **Reuse FuzzBase**: Create once, reuse for multiple searches
3. **Handle errors**: Use try-except blocks
4. **Monitor performance**: Track search times

.. code-block:: python

   from barangay import search, create_fuzz_base

   # Initialize once (e.g., at startup)
   fuzz_base = create_fuzz_base()

   def search_production(address):
       try:
           results = search(address, fuzz_base=fuzz_base, threshold=70.0, n=5)
           return {'success': True, 'results': results}
       except Exception as e:
           return {'success': False, 'error': str(e)}

Data Update Questions
---------------------

How do I update to the latest data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package includes the latest data by default. To update:

.. code-block:: bash

   pip install --upgrade barangay

This will install the latest version with the most recent PSGC data.

How do I access data from a specific date?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``as_of`` parameter:

.. code-block:: python

   from barangay import search, get_available_dates

   # Check available dates
   dates = get_available_dates()
   print(dates)

   # Search with specific date
   results = search("Tongmageng", as_of="2025-07-08")

How do I compare data across dates?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search with different dates:

.. code-block:: python

   from barangay import search

   date1 = "2025-07-08"
   date2 = "2025-10-13"

   results1 = search("Tongmageng", as_of=date1)
   results2 = search("Tongmageng", as_of=date2)

   print(f"Results from {date1}: {len(results1)}")
   print(f"Results from {date2}: {len(results2)}")

Integration Questions
---------------------

Can I use this with geocoding services?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, combine with geocoding services:

.. code-block:: python

   from barangay import search

   # First, validate and standardize address
   results = search("Tongmageng, Tawi-Tawi")

   if results:
       best = results[0]
       standardized = f"{best['barangay']}, {best['municipality_or_city']}, {best['province_or_huc']}"

       # Then use with geocoding service
       # coordinates = geocode(standardized)

Can I use this with address validation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, use for address validation:

.. code-block:: python

   from barangay import search

    def validate_address(address):
        results = search(address, threshold=80.0, n=1)

        if not results:
            return {'valid': False, 'reason': 'No matches found'}

        best = results[0]
        # Get the maximum score from active matching strategies
        scores = [
            best.get('f_000b_ratio_score', 0),
            best.get('f_0p0b_ratio_score', 0),
            best.get('f_00mb_ratio_score', 0),
            best.get('f_0pmb_ratio_score', 0)
        ]
        score = max(scores)
        if score < 80:
            return {'valid': False, 'reason': 'Low confidence match'}

        return {
            'valid': True,
            'standardized': {
                'barangay': best['barangay'],
                'municipality_or_city': best['municipality_or_city'],
                'province_or_huc': best['province_or_huc'],
                'psgc_id': best['psgc_id'],
            },
            'score': score
        }

Can I use this with data cleaning?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, use for cleaning messy address data:

.. code-block:: python

   from barangay import search

    def clean_addresses(addresses):
        cleaned = []
        for address in addresses:
            results = search(address, threshold=70.0, n=1)

            if results:
                best = results[0]
                # Get the maximum score from active matching strategies
                scores = [
                    best.get('f_000b_ratio_score', 0),
                    best.get('f_0p0b_ratio_score', 0),
                    best.get('f_00mb_ratio_score', 0),
                    best.get('f_0pmb_ratio_score', 0)
                ]
                score = max(scores)
                cleaned.append({
                    'original': address,
                    'barangay': best['barangay'],
                    'municipality_or_city': best['municipality_or_city'],
                    'province_or_huc': best['province_or_huc'],
                    'psgc_id': best['psgc_id'],
                    'score': score
                })
            else:
                cleaned.append({
                    'original': address,
                    'error': 'No match found'
                })

        return cleaned

Can I use this with data analysis?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, combine with analysis libraries:

.. code-block:: python

   import pandas as pd
   from barangay import BARANGAY_FLAT, search

   # Load data
   df = pd.DataFrame(BARANGAY_FLAT)

   # Analyze by province
   province_counts = df['province_or_huc'].value_counts()

   # Search and analyze
   results = search("San Jose", n=100)
   result_df = pd.DataFrame(results)

   # Group by province
   province_distribution = result_df['province_or_huc'].value_counts()

Troubleshooting
---------------

What should I do if search is slow?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Reuse FuzzBase** for multiple searches
2. **Reduce match hooks** to only what you need
3. **Increase threshold** to filter early
4. **Limit results** with the ``n`` parameter

See :doc:`performance` for more tips.

What should I do if I get no results?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Lower the threshold** to include more matches
2. **Check for typos** in the search string
3. **Try partial matches** with fewer words
4. **Verify the barangay exists** in the dataset

.. code-block:: python

   from barangay import search, BARANGAY_FLAT

   # Try lower threshold
   results = search("Invalid Barangay Name", threshold=40.0)

   # Check if similar names exist
   matches = [b for b in BARANGAY_FLAT if "Tong" in b['name'].lower()]
   print(matches)

What should I do if I get an import error?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Verify installation**:

   .. code-block:: bash

      pip list | grep barangay

2. **Reinstall the package**:

   .. code-block:: bash

      pip uninstall barangay
      pip install barangay

3. **Check Python version** (must be 3.10+):

   .. code-block:: bash

      python --version

4. **Ensure correct environment** is activated

See :doc:`common_errors` for more solutions.

What should I do if I get a download error?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Check internet connection**
2. **Use bundled data** instead of downloading
3. **Retry with exponential backoff**
4. **Check for rate limiting** from GitHub API

.. code-block:: python

   from barangay import load_barangay_data

   # Use bundled data (no download needed)
   data = load_barangay_data()

See :doc:`common_errors` for more solutions.

Additional Resources
--------------------

Where can I find more examples?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :doc:`../examples/address_validation` - Address validation examples
* :doc:`../examples/geocoding` - Geocoding integration examples
* :doc:`../examples/data_analysis` - Data analysis examples
* :doc:`../examples/batch_processing` - Batch processing examples
* `Sample Usage Notebook <https://github.com/bendlikeabamboo/barangay/blob/main/notebooks/sample_usage.ipynb>`_

Where can I report issues?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Report issues on `GitHub <https://github.com/bendlikeabamboo/barangay/issues>`_.

When reporting, include:

* Python version
* Package version
* Error message
* Minimal reproducible example
* System information

Where can I contribute?
~~~~~~~~~~~~~~~~~~~~~~~

Contributions are welcome! See :doc:`../contributing/index` for details.

See Also
--------

* :doc:`common_errors` - Common errors and solutions
* :doc:`performance` - Performance troubleshooting
* :doc:`../quick_start/installation` - Installation guide
* :doc:`../user_guide/search` - Comprehensive search guide