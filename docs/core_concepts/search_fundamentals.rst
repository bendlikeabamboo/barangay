Search Fundamentals
===================

This guide explains the core concepts of fuzzy search in the barangay package.

Introduction to Fuzzy Search
----------------------------

What is Fuzzy Search?
~~~~~~~~~~~~~~~~~~~~~

Fuzzy search is a technique that finds matches even when the search string doesn't exactly match the target data. It handles:

* Typos and misspellings
* Word order variations
* Partial matches
* Common abbreviations

The barangay package uses the `RapidFuzz <https://github.com/maxbachmann/RapidFuzz>`_ library, which implements the **token sort ratio** algorithm. This algorithm:

1. Splits strings into tokens (words)
2. Sorts the tokens alphabetically
3. Compares the sorted token sequences
4. Returns a similarity score from 0-100

Why Use Fuzzy Search for Addresses?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Philippine addresses often have variations:

* "San Jose" vs "Sanjose"
* "City of Manila" vs "Manila City"
* "Barangay 1" vs "Brgy. 1"
* "Tongmagen" vs "Tongmageng" (typo)

Fuzzy search handles these variations automatically, making it ideal for:

* Validating user input
* Cleaning messy data
* Finding approximate matches
* Handling real-world address variations

How It Works (High-Level)
~~~~~~~~~~~~~~~~~~~~~~~~~

The search function:

1. **Sanitizes** the search string (removes common prefixes/suffixes, normalizes case)
2. **Matches** against different administrative levels (province, municipality, barangay)
3. **Scores** each match using token sort ratio
4. **Filters** results by threshold
5. **Returns** top results sorted by score

Basic Usage
-----------

Simple Search
~~~~~~~~~~~~~

The simplest search uses all default parameters:

.. code-block:: python

   from barangay import search

   results = search("Tongmageng, Tawi-Tawi")
   print(results[0])

Understanding Match Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each result contains:

.. list-table:: Search Result Fields
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description
   * - barangay
     - Barangay name
   * - province_or_huc
     - Province or Highly Urbanized City name
   * - municipality_or_city
     - Municipality or city name
   * - psgc_id
     - Philippine Standard Geographic Code
   * - f_000b_ratio_score
     - Score for barangay-only matching
   * - f_0p0b_ratio_score
     - Score for province + barangay matching
   * - f_00mb_ratio_score
     - Score for municipality + barangay matching
   * - f_0pmb_ratio_score
     - Score for province + municipality + barangay matching

Score Interpretation
~~~~~~~~~~~~~~~~~~~~

* **90-100**: Very high confidence, likely correct
* **70-89**: Good match, probably correct
* **60-69**: Moderate match, may need verification
* **Below 60**: Low confidence, consider increasing threshold

.. code-block:: python

   from barangay import search

   results = search("Tongmagen, Tawi-Tawi")
   for result in results:
       # Get the maximum score from active matching strategies
       scores = [
           result.get('f_000b_ratio_score', 0),
           result.get('f_0p0b_ratio_score', 0),
           result.get('f_00mb_ratio_score', 0),
           result.get('f_0pmb_ratio_score', 0)
       ]
       score = max(scores)
       if score >= 90:
           confidence = "High"
       elif score >= 70:
           confidence = "Medium"
       else:
           confidence = "Low"
       print(f"{result['barangay']}: {score:.1f}% ({confidence})")

Search Parameters
-----------------

search_string
~~~~~~~~~~~~~

The string to search for. Can be:

* A barangay name: ``"Tongmageng"``
* A city/municipality: ``"Quezon City"``
* A province: ``"Tawi-Tawi"``
* A partial address: ``"Tongmageng, Tawi-Tawi"``
* Any combination: ``"San Jose, City of Manila, NCR"``

.. code-block:: python

   from barangay import search

   # Search by barangay
   results = search("Tongmageng")

   # Search by city
   results = search("Quezon City")

   # Search by province
   results = search("Tawi-Tawi")

   # Search with partial address
   results = search("Tongmageng, Tawi-Tawi")

match_hooks
~~~~~~~~~~~

Administrative levels to match against. Valid values:

* ``"barangay"`` - Match barangay names only
* ``"municipality"`` - Match municipality/city names
* ``"province"`` - Match province/HUC names

Default: ``["province", "municipality", "barangay"]``

.. code-block:: python

   from barangay import search

   # Match only barangay names
   results = search("San Jose", match_hooks=["barangay"])

   # Match municipality and barangay
   results = search("San Jose", match_hooks=["municipality", "barangay"])

   # Match all levels (default)
   results = search("San Jose", match_hooks=["province", "municipality", "barangay"])

threshold
~~~~~~~~~

Minimum similarity score (0-100) for a match to be included.

* Lower values return more results but with lower confidence
* Higher values return fewer results but with higher confidence
* Default: 60.0

.. code-block:: python

   from barangay import search

   # High threshold - only very close matches
   results = search("San Jose", threshold=90.0)
   print(f"High threshold (90): {len(results)} results")

   # Medium threshold (default)
   results = search("San Jose", threshold=60.0)
   print(f"Medium threshold (60): {len(results)} results")

   # Low threshold - more results, lower confidence
   results = search("San Jose", threshold=40.0)
   print(f"Low threshold (40): {len(results)} results")

n
~

Maximum number of results to return. Results are sorted by similarity score.

* Default: 5
* If fewer results meet the threshold, all are returned

.. code-block:: python

   from barangay import search

   # Get top 3 results
   results = search("San Jose", n=3)
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

as_of
~~~~~

Date string (YYYY-MM-DD) for historical data. Only used if ``fuzz_base`` is None.

* ``None`` (default): Use latest bundled data
* ``"2025-07-08"``: Use data from that date

.. code-block:: python

   from barangay import search

   # Search with latest data
   results = search("Tongmageng")

   # Search with historical data
   results = search("Tongmageng", as_of="2025-07-08")

search_sanitizer
~~~~~~~~~~~~~~~~

Function to sanitize the search string before matching. The default sanitizer removes common prefixes/suffixes and normalizes the string.

.. code-block:: python

   from barangay import search, sanitize_input

   # Use default sanitizer
   results = search("City of San Jose")

   # Use custom sanitizer to remove "City of"
   results = search(
       "City of San Jose",
       search_sanitizer=lambda x: sanitize_input(x, exclude=["city of "])
   )

fuzz_base
~~~~~~~~~

Pre-computed FuzzBase instance for fuzzy matching. Reusing a FuzzBase instance improves performance for multiple searches.

.. code-block:: python

   from barangay import search, create_fuzz_base

   # Create FuzzBase once
   fuzz_base = create_fuzz_base()

   # Reuse for multiple searches (faster)
   results1 = search("San Jose", fuzz_base=fuzz_base)
   results2 = search("Quezon City", fuzz_base=fuzz_base)
   results3 = search("Manila", fuzz_base=fuzz_base)

Match Hooks Explained
---------------------

Barangay Only (B)
~~~~~~~~~~~~~~~~~

Match against barangay names only. Fastest option.

.. code-block:: python

   from barangay import search

   results = search("San Jose", match_hooks=["barangay"])
   print(f"Results: {len(results)}")

Province + Barangay (PB)
~~~~~~~~~~~~~~~~~~~~~~~~

Match against province and barangay names. Good for disambiguating barangays with the same name.

.. code-block:: python

   from barangay import search

   results = search("San Jose, Tawi-Tawi", match_hooks=["province", "barangay"])
   for result in results:
       print(f"{result['barangay']}, {result['province_or_huc']}")

Municipality + Barangay (MB)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Match against municipality and barangay names. Good for city-specific searches.

.. code-block:: python

   from barangay import search

   results = search("San Jose, City of Manila", match_hooks=["municipality", "barangay"])
   for result in results:
       print(f"{result['barangay']}, {result['municipality_or_city']}")

Province + Municipality + Barangay (PMB)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Match against all three levels. Most comprehensive but slower.

.. code-block:: python

   from barangay import search

   results = search("San Jose, City of Manila, NCR", match_hooks=["province", "municipality", "barangay"])
   for result in results:
       print(f"{result['barangay']}, {result['municipality_or_city']}, {result['province_or_huc']}")

Performance Implications
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Match Hook Performance
   :widths: 25 25 25 25
   :header-rows: 1

   * - Strategy
     - Speed
     - Accuracy
     - Best For
   * - B (barangay only)
     - Fastest
     - Lower
     - Unique barangay names
   * - PB (province + barangay)
     - Fast
     - Medium
     - Disambiguating by province
   * - MB (municipality + barangay)
     - Fast
     - Medium
     - City-specific searches
   * - PMB (all three)
     - Slowest
     - Highest
     - Most comprehensive matching

Next Steps
----------

For advanced topics, see:

* :doc:`../how_to/custom_matching` - Custom sanitizers and advanced matching strategies
* :doc:`../advanced/fuzzy_matching` - Performance tuning and optimization

For API reference, see :doc:`../api_reference/search`.