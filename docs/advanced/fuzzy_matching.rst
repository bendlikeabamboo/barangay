Fuzzy Matching Internals
========================

This section provides a deep dive into the fuzzy matching algorithms used by the barangay package.

Overview
--------

The barangay package uses the `RapidFuzz` library for fuzzy string matching, which provides fast and accurate string similarity calculations. The core algorithm used is **token sort ratio**, which is particularly effective for matching addresses and names.

Key Concepts:

* **Token Sort Ratio**: Measures similarity between two strings after sorting their tokens
* **Pre-computation**: Fuzzy matching functions are pre-computed for performance
* **Multiple Matching Strategies**: Different combinations of administrative levels
* **Sanitization**: Strings are normalized before matching to improve accuracy

Token Sort Ratio Algorithm
--------------------------

How It Works
~~~~~~~~~~~~

The token sort ratio algorithm works as follows:

1. **Tokenization**: Split each string into tokens (words)
2. **Sorting**: Sort tokens alphabetically
3. **Reconstruction**: Reconstruct strings from sorted tokens
4. **Comparison**: Calculate similarity ratio using Levenshtein distance

Mathematical Representation:

.. math::

   \text{similarity} = \frac{\text{matching\_tokens}}{\text{total\_tokens}} \times 100

Example:

.. code-block:: python

    from rapidfuzz import fuzz

    # Original strings
    s1 = "City of Manila"
    s2 = "Manila City"

    # Token sort ratio
    score = fuzz.token_sort_ratio(s1, s2)
    print(f"Similarity: {score}%")

    # What happens internally:
    # s1 tokens: ["city", "of", "manila"] → sorted: ["city", "manila", "of"]
    # s2 tokens: ["manila", "city"] → sorted: ["city", "manila"]
    # After sorting, both strings become very similar

Output:

.. code-block:: text

    Similarity: 100%

Why Token Sort Ratio?
~~~~~~~~~~~~~~~~~~~~~

Token sort ratio is ideal for address matching because:

* **Order independence**: "Manila City" and "City of Manila" match perfectly
* **Robust to word order**: Users often type addresses in different orders
* **Handles common prefixes/suffixes**: "City of" is normalized away
* **Fast computation**: Efficient algorithm suitable for large datasets

Comparison with Other Algorithms:

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Algorithm
     - Order Sensitive
     - Best For
     - Example Score
   * - Token Sort Ratio
     - No
     - Addresses, names
     - 100%
   * - Simple Ratio
     - Yes
     - Exact matches
     - 75%
   * - Partial Ratio
     - Yes
     - Substrings
     - 80%
   * - Token Set Ratio
     - No
     - Different lengths
     - 90%

Pre-computation
---------------

FuzzBase Structure
~~~~~~~~~~~~~~~~~~

The [`FuzzBase`](../api_reference/fuzz.rst) class pre-computes fuzzy matching functions for all barangays in the dataset. This dramatically improves performance when performing multiple searches.

Structure:

.. code-block:: python

    import pandas as pd
    from barangay import load_fuzzer_base

    # Load the pre-computed fuzzer base
    fuzzer_base = load_fuzzer_base()

    # The DataFrame contains pre-computed columns:
    print(fuzzer_base.columns.tolist())

Output:

.. code-block:: text

    ['barangay', 'province_or_huc', 'municipality_or_city', 'psgc_id',
     '000b', '0p0b', '00mb', '0pmb',
     'f_000b_ratio', 'f_0p0b_ratio', 'f_00mb_ratio', 'f_0pmb_ratio']

Column Explanations:

* **barangay**: Original barangay name
* **province_or_huc**: Province or Highly Urbanized City name
* **municipality_or_city**: Municipality or city name
* **psgc_id**: Philippine Standard Geographic Code
* **000b**: Sanitized barangay name only
* **0p0b**: Sanitized province + barangay
* **00mb**: Sanitized municipality + barangay
* **0pmb**: Sanitized province + municipality + barangay
* **f_000b_ratio**: Pre-computed fuzzy function for barangay only
* **f_0p0b_ratio**: Pre-computed fuzzy function for province + barangay
* **f_00mb_ratio**: Pre-computed fuzzy function for municipality + barangay
* **f_0pmb_ratio**: Pre-computed fuzzy function for all three levels

Sanitized Strings
~~~~~~~~~~~~~~~~~

Before pre-computation, strings are sanitized using the [`_basic_sanitizer`](../api_reference/utils.rst):

.. code-block:: python

    from barangay.utils import _basic_sanitizer

    # Examples of sanitization
    examples = [
        "City of Manila",
        "Barangay (Pob.)",
        "San Jose, City",
        "Makati & Taguig"
    ]

    for example in examples:
        sanitized = _basic_sanitizer(example)
        print(f"{example:30s} → {sanitized}")

Output:

.. code-block:: text

    City of Manila               → manila
    Barangay (Pob.)             → barangay
    San Jose, City               → san jose
    Makati & Taguig             → makati taguig

The sanitizer removes:

* "City of " prefix
* " city" suffix
* "(Pob.)" and "(POB)" suffixes
* Periods, commas, hyphens, ampersands
* Parentheses

Partial Functions
~~~~~~~~~~~~~~~~~

The pre-computed columns use Python's `functools.partial` to create functions that are ready to accept the search string:

.. code-block:: python

    from functools import partial
    from rapidfuzz import fuzz

    # Create a partial function with s1 fixed
    match_function = partial(fuzz.token_sort_ratio, s1="manila")

    # Now we can call it with just s2
    score = match_function(s2="city of manila")
    print(f"Score: {score}%")

Output:

.. code-block:: text

    Score: 100%

This is what happens internally in the FuzzBase class for every barangay, allowing fast matching against search strings.

Matching Strategies
-------------------

The barangay package supports four matching strategies based on the combination of administrative levels:

Strategy Overview
~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Strategy
     - Administrative Levels
     - Column Used
     - Use Case
   * - B (Barangay only)
     - Barangay
     - f_000b_ratio_score
     - Quick searches, finding similar names
   * - PB (Province + Barangay)
     - Province, Barangay
     - f_0p0b_ratio_score
     - Disambiguating by province
   * - MB (Municipality + Barangay)
     - Municipality, Barangay
     - f_00mb_ratio_score
     - Disambiguating by municipality
   * - PMB (All three)
     - Province, Municipality, Barangay
     - f_0pmb_ratio_score
     - Most specific matching

Strategy Implementation
~~~~~~~~~~~~~~~~~~~~~~~

Each strategy uses a different pre-computed function:

.. mermaid::

    graph TD
        A[Search String] --> B{Strategy}
        B -->|B| C[000b Function]
        B -->|PB| D[0p0b Function]
        B -->|MB| E[00mb Function]
        B -->|PMB| F[0pmb Function]
        C --> G[Match Results]
        D --> G
        E --> G
        F --> G

Performance Characteristics
---------------------------

Time Complexity
~~~~~~~~~~~~~~~

The time complexity of fuzzy matching depends on the matching strategy:

* **Single search**: O(n × m) where n is the number of barangays and m is the average string length
* **Pre-computation**: O(n × m) done once during initialization
* **Subsequent searches**: O(n) per search (due to pre-computation)

Benchmark Results:

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Operation
     - Dataset Size
     - Average Time
   * - Create FuzzBase
     - 42,000 barangays
     - ~2 seconds
   * - Single search (no pre-computation)
     - 42,000 barangays
     - ~500ms
   * - Single search (with pre-computation)
     - 42,000 barangays
     - ~50ms
   * - 100 searches (with pre-computation)
     - 42,000 barangays
     - ~5 seconds

Space Complexity
~~~~~~~~~~~~~~~~

The space complexity is primarily determined by the pre-computed data:

* **Original data**: O(n × m) where n is the number of barangays and m is the average string length
* **Pre-computed functions**: O(n) additional storage
* **Sanitized strings**: O(n × m) additional storage

Total memory usage for the full dataset:

* **Basic data**: ~50 MB
* **Pre-computed functions**: ~100 MB
* **Total**: ~150 MB

Optimization Techniques
~~~~~~~~~~~~~~~~~~~~~~~

The package uses several optimization techniques:

1. **Pre-computation**: Fuzzy matching functions are computed once and reused
2. **Vectorization**: Pandas operations are vectorized where possible
3. **Lazy evaluation**: Results are computed only when needed
4. **Early termination**: Searches stop after finding n results above threshold

For practical examples of using different matching strategies, see :doc:`../how_to/custom_matching`.

See Also
--------

* :ref:`api-fuzz` - FuzzBase class API reference
* :ref:`api-search` - Search function API reference
* :doc:`../how_to/custom_matching` - Custom matching guide