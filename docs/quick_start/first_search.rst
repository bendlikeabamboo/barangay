First Search
============

This guide will walk you through your first search using the barangay package. You'll learn how to perform basic searches, understand the results, and use common search patterns.

Basic Search Example
--------------------

Let's start with a simple search for a barangay:

.. code-block:: python

   from barangay import search

   results = search("Tongmageng, Tawi-Tawi")
   print(results[0])

Output:

.. code-block:: python

   {
       'barangay': 'Tongmageng',
       'province_or_huc': 'Tawi-Tawi',
       'municipality_or_city': 'Sitangkai',
       'psgc_id': '157501001',
       'max_score': 95.5,
       'f_000b_ratio_score': 95.5,
       'f_0p0b_ratio_score': 95.5,
       'f_00mb_ratio_score': 95.5,
       'f_0pmb_ratio_score': 95.5,
       '000b': 'tongmageng',
       '0p0b': 'tawi-tawi tongmageng',
       '00mb': 'sitangkai tongmageng',
       '0pmb': 'tawi-tawi sitangkai tongmageng'
   }

Understanding Search Results
----------------------------

The search function returns a list of dictionaries, each containing the following fields:

Core Information
~~~~~~~~~~~~~~~~

* **barangay** - The barangay name
* **province_or_huc** - The province or Highly Urbanized City name
* **municipality_or_city** - The municipality or city name
* **psgc_id** - The Philippine Standard Geographic Code

Scoring Information
~~~~~~~~~~~~~~~~~~~

* **max_score** - The maximum similarity score across all match types (0-100)
* **f_000b_ratio_score** - Score for barangay-only matching
* **f_0p0b_ratio_score** - Score for province + barangay matching
* **f_00mb_ratio_score** - Score for municipality + barangay matching
* **f_0pmb_ratio_score** - Score for province + municipality + barangay matching

Sanitized Strings
~~~~~~~~~~~~~~~~~

* **000b** - Sanitized barangay name
* **0p0b** - Sanitized province + barangay string
* **00mb** - Sanitized municipality + barangay string
* **0pmb** - Sanitized province + municipality + barangay string

.. note:: The score represents the similarity between your search string and the matched data, with 100 being a perfect match. The default threshold is 60.0, meaning only matches with a score of 60 or higher are returned.

Common Search Patterns
----------------------

Search with Partial Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can search with partial addresses or incomplete information:

.. code-block:: python

   from barangay import search

   # Search with just a barangay name
   results = search("San Jose")
   for result in results[:3]:
       print(f"{result['barangay']}, {result['municipality_or_city']}, {result['province_or_huc']}")

Output:

.. code-block:: text

   San Jose, City of Manila, National Capital Region (NCR)
   San Jose, City of Antipolo, Rizal
   San Jose, City of Davao, Davao del Sur

Search with Typos
~~~~~~~~~~~~~~~~~

The fuzzy search handles typos and variations:

.. code-block:: python

   from barangay import search

   # Search with a typo
   results = search("Tongmagen, Tawi-Tawi")
   print(f"Best match: {results[0]['barangay']} (score: {results[0]['max_score']})")

Output:

.. code-block:: text

   Best match: Tongmageng (score: 95.5)

Search with City/Municipality Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can search for municipalities or cities:

.. code-block:: python

   from barangay import search

   # Search for a city
   results = search("Quezon City")
   for result in results[:5]:
       print(f"{result['barangay']} (score: {result['max_score']})")

Output:

.. code-block:: text

   Quezon City (score: 100.0)
   Quezon City Hill (score: 85.0)
   Quezon City Proper (score: 85.0)
   ...

Customizing Search Parameters
-----------------------------

Limit Number of Results
~~~~~~~~~~~~~~~~~~~~~~~

Use the ``n`` parameter to limit the number of results:

.. code-block:: python

   from barangay import search

   # Get only top 3 results
   results = search("San Jose", n=3)
   for i, result in enumerate(results, 1):
       print(f"{i}. {result['barangay']}, {result['municipality_or_city']}")

Set Minimum Threshold
~~~~~~~~~~~~~~~~~~~~~

Use the ``threshold`` parameter to set the minimum similarity score:

.. code-block:: python

   from barangay import search

   # Only return matches with 80% similarity or higher
   results = search("San Jose", threshold=80.0)
   print(f"Found {len(results)} matches above 80% similarity")

Match Specific Administrative Levels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``match_hooks`` parameter to specify which administrative levels to match:

.. code-block:: python

   from barangay import search

   # Match only against barangay names
   results = search("San Jose", match_hooks=["barangay"])

   # Match against municipality and barangay
   results = search("San Jose", match_hooks=["municipality", "barangay"])

   # Match against all levels (default)
   results = search("San Jose", match_hooks=["province", "municipality", "barangay"])

Tips for Better Results
-----------------------

Use More Context
~~~~~~~~~~~~~~~~

Including more context (like province or municipality) improves accuracy:

.. code-block:: python

   from barangay import search

   # Less specific - may return many results
   results = search("San Jose")

   # More specific - returns more accurate results
   results = search("San Jose, City of Manila")

Handle Common Variations
~~~~~~~~~~~~~~~~~~~~~~~~

The search handles common variations, but being explicit helps:

.. code-block:: python

   from barangay import search

   # These will all work
   results = search("City of Manila")
   results = search("Manila City")
   results = search("Manila")

Check the Score
~~~~~~~~~~~~~~~

Always check the ``max_score`` to gauge confidence in the match:

.. code-block:: python

   from barangay import search

   results = search("Tongmagen, Tawi-Tawi")
   for result in results:
       print(f"{result['barangay']} - Score: {result['max_score']:.1f}")
       if result['max_score'] >= 90:
           print("  → High confidence match")
       elif result['max_score'] >= 70:
           print("  → Moderate confidence match")
       else:
           print("  → Low confidence match")

Use Multiple Results
~~~~~~~~~~~~~~~~~~~~

For ambiguous queries, consider multiple results:

.. code-block:: python

   from barangay import search

   results = search("San Jose", n=5)
   print(f"Found {len(results)} potential matches:")
   for i, result in enumerate(results, 1):
       print(f"{i}. {result['barangay']}, {result['municipality_or_city']}, {result['province_or_huc']}")

Complete Example
----------------

Here's a complete example that demonstrates several features:

.. code-block:: python

   from barangay import search

   def find_barangay(query, n=5, threshold=60.0):
       """Find barangays matching the query."""
       results = search(query, n=n, threshold=threshold)

       if not results:
           print(f"No matches found for '{query}' with threshold {threshold}")
           return

       print(f"Top {len(results)} matches for '{query}':\n")

       for i, result in enumerate(results, 1):
           print(f"{i}. {result['barangay']}")
           print(f"   Municipality/City: {result['municipality_or_city']}")
           print(f"   Province/HUC: {result['province_or_huc']}")
           print(f"   PSGC ID: {result['psgc_id']}")
           print(f"   Score: {result['max_score']:.1f}%")

           # Add confidence indicator
           if result['max_score'] >= 90:
               confidence = "High"
           elif result['max_score'] >= 70:
               confidence = "Medium"
           else:
               confidence = "Low"
           print(f"   Confidence: {confidence}\n")

   # Example searches
   find_barangay("Tongmageng, Tawi-Tawi")
   find_barangay("San Jose, City of Manila", n=3)
   find_barangay("Tongmagen, Tawi-Tawi", threshold=85.0)

Output:

.. code-block:: text

   Top 5 matches for 'Tongmageng, Tawi-Tawi':

   1. Tongmageng
      Municipality/City: Sitangkai
      Province/HUC: Tawi-Tawi
      PSGC ID: 157501001
      Score: 95.5%
      Confidence: High

   ...

Next Steps
----------

Now that you've performed your first search, explore these topics:

* :doc:`data_models_overview` - Learn about the different data models available
* :doc:`../user_guide/search` - Comprehensive guide to fuzzy search features
* :doc:`../user_guide/data_models` - Detailed information about data structures
* :doc:`../user_guide/historical_data` - How to access historical data

For more advanced search features and customization options, see the :doc:`../user_guide/search` guide.