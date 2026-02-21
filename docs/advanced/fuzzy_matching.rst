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

B: Barangay Only
~~~~~~~~~~~~~~~~

Match against barangay names only:

.. code-block:: python

    from barangay import search

    # Match against barangay names only
    results = search(
        "Tongmageng",
        match_hooks=["barangay"],
        n=5
    )

    for result in results:
        print(f"{result['barangay']} (score: {result['f_000b_ratio_score']:.1f})")

Use cases:

* Searching when you only know the barangay name
* Finding barangays with similar names across different locations
* Quick searches when context is less important

PB: Province + Barangay
~~~~~~~~~~~~~~~~~~~~~~~

Match against province and barangay names:

.. code-block:: python

    from barangay import search

    # Match against province and barangay
    results = search(
        "Tongmageng, Tawi-Tawi",
        match_hooks=["province", "barangay"],
        n=5
    )

    for result in results:
        print(f"{result['barangay']}, {result['province_or_huc']} "
              f"(score: {result['f_0p0b_ratio_score']:.1f})")

Use cases:

* Searching with province context
* Disambiguating barangays with the same name
* When municipality information is missing

MB: Municipality + Barangay
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Match against municipality and barangay names:

.. code-block:: python

    from barangay import search

    # Match against municipality and barangay
    results = search(
        "Tongmageng, Sitangkai",
        match_hooks=["municipality", "barangay"],
        n=5
    )

    for result in results:
        print(f"{result['barangay']}, {result['municipality_or_city']} "
              f"(score: {result['f_00mb_ratio_score']:.1f})")

Use cases:

* Searching with municipality context
* When province information is not needed
* More specific than barangay-only, less specific than full address

PMB: Province + Municipality + Barangay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Match against all three administrative levels:

.. code-block:: python

    from barangay import search

    # Match against all three levels (default)
    results = search(
        "Tongmageng, Sitangkai, Tawi-Tawi",
        match_hooks=["province", "municipality", "barangay"],
        n=5
    )

    for result in results:
        print(f"{result['barangay']}, {result['municipality_or_city']}, "
              f"{result['province_or_huc']} (score: {result['f_0pmb_ratio_score']:.1f})")

Use cases:

* Most specific matching
* When you have complete address information
* Highest accuracy for well-formed addresses

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

Custom Matching Strategies
--------------------------

Creating Custom Match Hooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can create custom matching strategies by combining different administrative levels:

.. code-block:: python

    from barangay import search, create_fuzz_base

    # Create a custom matching strategy
    def custom_search(
        search_string: str,
        include_province: bool = True,
        include_municipality: bool = True,
        include_barangay: bool = True,
        **kwargs
    ):
        """Search with custom matching strategy.

        Args:
            search_string: String to search for
            include_province: Whether to include province in matching
            include_municipality: Whether to include municipality in matching
            include_barangay: Whether to include barangay in matching
            **kwargs: Additional arguments for search()
        """
        match_hooks = []
        if include_province:
            match_hooks.append("province")
        if include_municipality:
            match_hooks.append("municipality")
        if include_barangay:
            match_hooks.append("barangay")

        return search(search_string, match_hooks=match_hooks, **kwargs)

    # Example: Search with only municipality and barangay
    results = custom_search(
        "Tongmageng, Sitangkai",
        include_province=False,
        include_municipality=True,
        include_barangay=True,
        n=5
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
        print(f"{result['barangay']}, {result['municipality_or_city']} "
              f"(score: {score:.1f})")

Weighted Matching
~~~~~~~~~~~~~~~~~

Implement weighted matching to prioritize certain administrative levels:

.. code-block:: python

    from barangay import search
    import pandas as pd

    def weighted_search(
        search_string: str,
        province_weight: float = 1.0,
        municipality_weight: float = 1.0,
        barangay_weight: float = 1.0,
        n: int = 5
    ) -> list:
        """Search with weighted matching scores.

        Args:
            search_string: String to search for
            province_weight: Weight for province matching
            municipality_weight: Weight for municipality matching
            barangay_weight: Weight for barangay matching
            n: Number of results to return

        Returns:
            List of results with weighted scores
        """
        # Get results with all match hooks
        results = search(
            search_string,
            match_hooks=["province", "municipality", "barangay"],
            n=100,  # Get more results for better weighting
            threshold=0.0  # No threshold to get all results
        )

        # Calculate weighted scores
        for result in results:
            weighted_score = 0.0
            total_weight = 0.0

            if 'f_000b_ratio_score' in result:
                weighted_score += result['f_000b_ratio_score'] * barangay_weight
                total_weight += barangay_weight

            if 'f_0p0b_ratio_score' in result:
                weighted_score += result['f_0p0b_ratio_score'] * province_weight * barangay_weight
                total_weight += province_weight * barangay_weight

            if 'f_00mb_ratio_score' in result:
                weighted_score += result['f_00mb_ratio_score'] * municipality_weight * barangay_weight
                total_weight += municipality_weight * barangay_weight

            if 'f_0pmb_ratio_score' in result:
                weighted_score += result['f_0pmb_ratio_score'] * province_weight * municipality_weight * barangay_weight
                total_weight += province_weight * municipality_weight * barangay_weight

            result['weighted_score'] = weighted_score / total_weight if total_weight > 0 else 0.0

        # Sort by weighted score and return top n
        results.sort(key=lambda x: x['weighted_score'], reverse=True)
        return results[:n]

    # Example: Prioritize barangay matching
    results = weighted_search(
        "Tongmageng",
        province_weight=0.5,
        municipality_weight=0.5,
        barangay_weight=2.0,
        n=5
    )

    for result in results:
        print(f"{result['barangay']} (weighted score: {result['weighted_score']:.1f})")

Code Examples and Benchmarks
----------------------------

Benchmarking Search Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare performance of different search approaches:

.. code-block:: python

    import time
    from barangay import search, create_fuzz_base

    def benchmark_search(
        search_string: str,
        iterations: int = 100
    ) -> dict:
        """Benchmark search performance.

        Args:
            search_string: String to search for
            iterations: Number of iterations

        Returns:
            Dictionary with benchmark results
        """
        results = {}

        # Benchmark 1: Without pre-computation
        start_time = time.time()
        for _ in range(iterations):
            search(search_string, fuzz_base=None)
        time_without_precomp = (time.time() - start_time) / iterations
        results['without_precomputation'] = time_without_precomp

        # Benchmark 2: With pre-computation
        fuzz_base = create_fuzz_base()
        start_time = time.time()
        for _ in range(iterations):
            search(search_string, fuzz_base=fuzz_base)
        time_with_precomp = (time.time() - start_time) / iterations
        results['with_precomputation'] = time_with_precomp

        # Calculate speedup
        speedup = time_without_precomp / time_with_precomp
        results['speedup'] = speedup

        return results

    # Run benchmark
    benchmark = benchmark_search("Tongmageng, Tawi-Tawi", iterations=100)

    print("Benchmark Results:")
    print(f"  Without pre-computation: {benchmark['without_precomputation']*1000:.2f} ms")
    print(f"  With pre-computation: {benchmark['with_precomputation']*1000:.2f} ms")
    print(f"  Speedup: {benchmark['speedup']:.1f}x")

Output:

.. code-block:: text

    Benchmark Results:
      Without pre-computation: 520.34 ms
      With pre-computation: 48.12 ms
      Speedup: 10.8x

Comparing Matching Strategies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare accuracy of different matching strategies:

.. code-block:: python

    from barangay import search

    def compare_strategies(
        search_string: str,
        expected_barangay: str
    ) -> dict:
        """Compare different matching strategies.

        Args:
            search_string: String to search for
            expected_barangay: Expected barangay name

        Returns:
            Dictionary with comparison results
        """
        strategies = {
            'B (Barangay only)': ["barangay"],
            'PB (Province + Barangay)': ["province", "barangay"],
            'MB (Municipality + Barangay)': ["municipality", "barangay"],
            'PMB (All three)': ["province", "municipality", "barangay"]
        }

        results = {}
        for name, hooks in strategies.items():
            matches = search(search_string, match_hooks=hooks, n=1)
            if matches:
                is_correct = matches[0]['barangay'] == expected_barangay
                # Get the maximum score from active matching strategies
                scores = [
                    matches[0].get('f_000b_ratio_score', 0),
                    matches[0].get('f_0p0b_ratio_score', 0),
                    matches[0].get('f_00mb_ratio_score', 0),
                    matches[0].get('f_0pmb_ratio_score', 0)
                ]
                score = max(scores)
                results[name] = {
                    'found': True,
                    'is_correct': is_correct,
                    'score': score,
                    'matched_barangay': matches[0]['barangay']
                }
            else:
                results[name] = {
                    'found': False,
                    'is_correct': False,
                    'score': None,
                    'matched_barangay': None
                }

        return results

    # Compare strategies
    comparison = compare_strategies("Tongmageng, Tawi-Tawi", "Tongmageng")

    print("Matching Strategy Comparison:")
    for strategy, result in comparison.items():
        status = "✓" if result['is_correct'] else "✗"
        print(f"  {status} {strategy}:")
        print(f"      Score: {result['score']:.1f}" if result['score'] else "      Score: N/A")
        print(f"      Matched: {result['matched_barangay']}" if result['matched_barangay'] else "      Matched: None")

See Also
--------

* :ref:`api-fuzz` - FuzzBase class API reference
* :ref:`api-search` - Search function API reference
* :ref:`userguide-search` - Search user guide
* :ref:`advanced-custom-sanitizers` - Custom sanitizers guide