Search Guide
============

This guide provides comprehensive information about the fuzzy search functionality in the barangay package. You'll learn about search strategies, parameters, customization options, and performance tips.

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

Advanced Patterns
-----------------

Searching with Partial Addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Handle incomplete or partial addresses:

.. code-block:: python

   from barangay import search

   # Only barangay name
   results = search("Tongmageng")

   # Barangay + province
   results = search("Tongmageng, Tawi-Tawi")

   # Barangay + city + province
   results = search("Tongmageng, Sitangkai, Tawi-Tawi")

   # Only city
   results = search("Quezon City")

Handling Typos and Variations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fuzzy search handles common variations:

.. code-block:: python

   from barangay import search

   # Typos
   results = search("Tongmagen")  # Should match "Tongmageng"

   # Abbreviations
   results = search("Brgy. 1")  # Should match "Barangay 1"

   # Different word order
   results = search("Manila City")  # Should match "City of Manila"

   # Missing words
   results = search("San Jose")  # Should match "Barangay San Jose"

Multi-level Matching
~~~~~~~~~~~~~~~~~~~~

Use multiple match hooks for comprehensive matching:

.. code-block:: python

   from barangay import search

   # Match against all levels
   results = search(
       "San Jose",
       match_hooks=["province", "municipality", "barangay"],
       n=10
   )

    # Group results by administrative level
    # Get the maximum score from active matching strategies for each result
    for r in results:
        scores = [
            r.get('f_000b_ratio_score', 0),
            r.get('f_0p0b_ratio_score', 0),
            r.get('f_00mb_ratio_score', 0),
            r.get('f_0pmb_ratio_score', 0)
        ]
        r['max_score'] = max(scores)
    
    province_matches = [r for r in results if r['f_0p0b_ratio_score'] == r['max_score']]
    municipality_matches = [r for r in results if r['f_00mb_ratio_score'] == r['max_score']]
    barangay_matches = [r for r in results if r['f_000b_ratio_score'] == r['max_score']]

    print(f"Province matches: {len(province_matches)}")
    print(f"Municipality matches: {len(municipality_matches)}")
    print(f"Barangay matches: {len(barangay_matches)}")

Custom Sanitizers
~~~~~~~~~~~~~~~~~

Create custom sanitizers for specific use cases:

.. code-block:: python

   from barangay import search, sanitize_input

   # Remove common prefixes
   def custom_sanitizer(text):
       return sanitize_input(text, exclude=["city of ", "brgy. ", "barangay "])

   results = search("City of San Jose", search_sanitizer=custom_sanitizer)

   # Handle Filipino abbreviations
   def filipino_sanitizer(text):
       text = text.lower()
       text = text.replace("brgy", "barangay")
       text = text.replace("city", "")
       return sanitize_input(text)

   results = search("Brgy 1, City of Manila", search_sanitizer=filipino_sanitizer)

Using Custom Sanitizers
-----------------------

Creating Custom Sanitizers
~~~~~~~~~~~~~~~~~~~~~~~~~~

A sanitizer function should:

1. Take a string as input
2. Return a sanitized string
3. Handle edge cases (empty strings, None, etc.)

.. code-block:: python

   from barangay import search

   def my_custom_sanitizer(text):
       """Custom sanitizer for my specific use case."""
       if not text:
           return ""

       # Convert to lowercase
       text = text.lower()

       # Remove specific words
       words_to_remove = ["city of", "municipality of", "brgy", "barangay"]
       for word in words_to_remove:
           text = text.replace(word, "")

       # Remove special characters
       import re
       text = re.sub(r'[^a-z0-9\s]', '', text)

       # Strip whitespace
       text = text.strip()

       return text

   results = search("City of San Jose", search_sanitizer=my_custom_sanitizer)

Common Customizations
~~~~~~~~~~~~~~~~~~~~~

Remove specific words:

.. code-block:: python

   from barangay import sanitize_input

   # Remove "City of" prefix
   def remove_city_of(text):
       return sanitize_input(text, exclude=["city of "])

Handle special characters:

.. code-block:: python

   import re

   def handle_special_chars(text):
       text = text.lower()
       text = re.sub(r'[^\w\s]', '', text)  # Remove non-alphanumeric
       return text.strip()

Normalize Filipino abbreviations:

.. code-block:: python

   def normalize_filipino(text):
       text = text.lower()
       replacements = {
           "brgy": "barangay",
           "mun": "municipality",
           "city": "",
           "st": "santo",
           "san": "santo",
       }
       for old, new in replacements.items():
           text = text.replace(old, new)
       return text

Reusing FuzzBase Instances
--------------------------

Why Reuse FuzzBase?
~~~~~~~~~~~~~~~~~~~

Creating a FuzzBase instance involves:

1. Loading the data
2. Sanitizing all strings
3. Pre-computing fuzzy matching functions

This is computationally expensive. Reusing a FuzzBase instance for multiple searches significantly improves performance.

Creating a Reusable FuzzBase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import create_fuzz_base, search

   # Create FuzzBase once (expensive)
   fuzz_base = create_fuzz_base()

   # Reuse for multiple searches (fast)
   search_strings = [
       "San Jose",
       "Quezon City",
       "Manila",
       "Tongmageng",
       "Makati",
   ]

   for search_string in search_strings:
       results = search(search_string, fuzz_base=fuzz_base)
       print(f"{search_string}: {len(results)} results")

Performance Comparison
~~~~~~~~~~~~~~~~~~~~~~

Without reusing FuzzBase:

.. code-block:: python

   import time
   from barangay import search

   start = time.time()
   for i in range(100):
       results = search("San Jose")
   end = time.time()
   print(f"Without reuse: {end - start:.2f} seconds")

With reusing FuzzBase:

.. code-block:: python

   import time
   from barangay import create_fuzz_base, search

   fuzz_base = create_fuzz_base()
   start = time.time()
   for i in range(100):
       results = search("San Jose", fuzz_base=fuzz_base)
   end = time.time()
   print(f"With reuse: {end - start:.2f} seconds")

Best Practices
--------------

Choosing the Right Threshold
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **High confidence (90+)**: Use when accuracy is critical
* **Balanced (70-89)**: Good default for most use cases
* **Inclusive (60-69)**: Use when you want more options
* **Exploratory (<60)**: Use for debugging or research

.. code-block:: python

   from barangay import search

   # Critical applications (e.g., legal documents)
   results = search("Tongmageng", threshold=95.0)

   # General use (default)
   results = search("Tongmageng", threshold=60.0)

   # Exploratory (find all possible matches)
   results = search("Tongmageng", threshold=40.0)

Optimizing for Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Reuse FuzzBase instances** for multiple searches
2. **Use appropriate match_hooks** - don't match more levels than needed
3. **Set reasonable thresholds** - avoid processing low-score matches
4. **Limit result count** - use ``n`` parameter to avoid unnecessary processing

.. code-block:: python

   from barangay import create_fuzz_base, search

   # Optimize for batch processing
   fuzz_base = create_fuzz_base()

   def batch_search(search_strings, threshold=70.0, n=5):
       """Optimized batch search."""
       results = {}
       for search_string in search_strings:
           matches = search(
               search_string,
               fuzz_base=fuzz_base,
               threshold=threshold,
               n=n
           )
           results[search_string] = matches
       return results

   search_strings = ["San Jose", "Quezon City", "Manila"]
   results = batch_search(search_strings)

Handling Edge Cases
~~~~~~~~~~~~~~~~~~~

No Results Found:

.. code-block:: python

   from barangay import search

   results = search("Invalid Barangay Name")
   if not results:
       print("No matches found. Try:")
       print("1. Lowering the threshold")
       print("2. Checking for typos")
       print("3. Using a partial match")

Multiple Equally Good Matches:

.. code-block:: python

   from barangay import search

   results = search("San Jose", n=10)
   if len(results) > 1:
       # Get the maximum score from active matching strategies for each result
       for r in results:
           scores = [
               r.get('f_000b_ratio_score', 0),
               r.get('f_0p0b_ratio_score', 0),
               r.get('f_00mb_ratio_score', 0),
               r.get('f_0pmb_ratio_score', 0)
           ]
           r['max_score'] = max(scores)
       
       top_score = results[0]['max_score']
       top_matches = [r for r in results if r['max_score'] == top_score]
       if len(top_matches) > 1:
           print(f"Multiple top matches with score {top_score}:")
           for match in top_matches:
               print(f"  - {match['barangay']}, {match['municipality_or_city']}, {match['province_or_huc']}")

Low Confidence Matches:

.. code-block:: python

   from barangay import search

    results = search("Tongmagen")
    for result in results:
        # Get the maximum score from active matching strategies
        scores = [
            result.get('f_000b_ratio_score', 0),
            result.get('f_0p0b_ratio_score', 0),
            result.get('f_00mb_ratio_score', 0),
            result.get('f_0pmb_ratio_score', 0)
        ]
        score = max(scores)
        if score < 70:
            print(f"Low confidence: {result['barangay']} ({score:.1f}%)")
            print("  Consider manual verification")

Complete Example
----------------

Here's a complete example demonstrating advanced search features:

.. code-block:: python

   from barangay import create_fuzz_base, search, sanitize_input

   class AddressValidator:
       """Validate and standardize Philippine addresses."""

       def __init__(self, threshold=70.0):
           self.threshold = threshold
           self.fuzz_base = create_fuzz_base()

       def validate(self, address):
           """Validate an address and return standardized information."""
           # Search for matches
           results = search(
               address,
               fuzz_base=self.fuzz_base,
               threshold=self.threshold,
               n=5
           )

           if not results:
               return {
                   'valid': False,
                   'message': 'No matches found',
                   'original': address
               }

            # Get best match
            best = results[0]

            # Get the maximum score from active matching strategies
            scores = [
                best.get('f_000b_ratio_score', 0),
                best.get('f_0p0b_ratio_score', 0),
                best.get('f_00mb_ratio_score', 0),
                best.get('f_0pmb_ratio_score', 0)
            ]
            # Get the maximum score from active matching strategies
            scores = [
                best.get('f_000b_ratio_score', 0),
                best.get('f_0p0b_ratio_score', 0),
                best.get('f_00mb_ratio_score', 0),
                best.get('f_0pmb_ratio_score', 0)
            ]
            best['max_score'] = max(scores)

            # Determine confidence
            if best['max_score'] >= 90:
                confidence = 'high'
            elif best['max_score'] >= 70:
                confidence = 'medium'
            else:
                confidence = 'low'

            return {
                'valid': True,
                'confidence': confidence,
                'original': address,
                'standardized': {
                    'barangay': best['barangay'],
                    'municipality_or_city': best['municipality_or_city'],
                    'province_or_huc': best['province_or_huc'],
                    'psgc_id': best['psgc_id'],
                },
                'score': best['max_score'],
                'alternatives': results[1:] if len(results) > 1 else []
            }

   # Usage
   validator = AddressValidator(threshold=70.0)

   # Test addresses
   test_addresses = [
       "Tongmageng, Tawi-Tawi",
       "San Jose, City of Manila",
       "Quezon City",
       "Tongmagen, Tawi-Tawi",  # Typo
   ]

   for address in test_addresses:
       result = validator.validate(address)
       print(f"\nOriginal: {result['original']}")
       if result['valid']:
           std = result['standardized']
           print(f"Standardized: {std['barangay']}, {std['municipality_or_city']}, {std['province_or_huc']}")
           print(f"PSGC ID: {std['psgc_id']}")
           print(f"Score: {result['score']:.1f}% ({result['confidence']})")
       else:
           print(f"Message: {result['message']}")

Next Steps
----------

Now that you understand fuzzy search, explore these topics:

* :doc:`data_models` - Learn about the different data models
* :doc:`historical_data` - How to access historical data
* :doc:`configuration` - Configure the package for your needs
* :doc:`performance` - Performance optimization tips

For API reference, see :doc:`../api_reference/search`.