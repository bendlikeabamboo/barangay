###############
 Search Module
##############

The search module provides fuzzy string matching capabilities for
searching Philippine barangay data across different administrative
levels (province, municipality, barangay). The search function uses the
RapidFuzz library for fast and accurate fuzzy matching.


 Overview
*********

The main function in this module is :func:`search`, which performs fuzzy
matching on barangay names across different administrative levels using
the RapidFuzz library's token_sort_ratio algorithm.

Matching Strategies
===================

The search function supports multiple matching strategies based on the
combination of match_hooks:

-  **B (Barangay only)**: Match against barangay names only
-  **PB (Province + Barangay)**: Match against province and barangay
   names
-  **MB (Municipality + Barangay)**: Match against municipality and
   barangay names
-  **PMB (Province + Municipality + Barangay)**: Match against all three
   levels


 API Reference
**************

.. autofunction:: barangay.search.search


 Examples
*********

Basic Search
============

.. code:: python

   from barangay import search

   # Search for a barangay
   results = search("Tongmageng, Tawi-Tawi")
   for result in results:
       print(f"{result['barangay']}, {result['municipality_or_city']}")

Search with Custom Parameters
=============================

.. code:: python

   from barangay import search

    # Search with custom parameters
    results = search(
        "Tongmagen, Tawi-Tawi",
        n=4,
        match_hooks=["municipality", "barangay"],
        threshold=70.0,
    )
    for result in results:
        # Get the maximum score from active matching strategies
        scores = [
            result.get('f_000b_ratio_score', 0),
            result.get('f_0p0b_ratio_score', 0),
            result.get('f_00mb_ratio_score', 0),
            result.get('f_0pmb_ratio_score', 0)
        ]
        score = max(scores)
        print(f"{result['barangay']} (score: {score})")

Historical Data Search
======================

.. code:: python

   from barangay import search

   # Search using historical data
   results = search("Tongmageng", as_of="2025-07-08")

Using a Custom Sanitizer
========================

.. code:: python

   from barangay import search, sanitize_input

   # Search with custom sanitizer
   results = search(
       "City of San Jose",
       search_sanitizer=lambda x: sanitize_input(x, exclude=["city of "]),
   )

Reusing a FuzzBase Instance
===========================

.. code:: python

   from barangay import search, create_fuzz_base

   # Create a FuzzBase instance for multiple searches
   fuzz_base = create_fuzz_base()

   # Perform multiple searches efficiently
   results1 = search("Tongmageng", fuzz_base=fuzz_base)
   results2 = search("San Jose", fuzz_base=fuzz_base)


 See Also
*********

-  :mod:`barangay.fuzz` - Fuzzy matching module
-  :mod:`barangay.data` - Data loading module
-  :class:`barangay.fuzz.FuzzBase` - Class for pre-computing fuzzy
   matching functions
-  :func:`barangay.fuzz.create_fuzz_base` - Factory function to create
   FuzzBase instances
-  :func:`barangay.utils.sanitize_input` - String sanitization utility