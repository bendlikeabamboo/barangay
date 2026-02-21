Custom Sanitizers
=================

This section covers creating and using custom sanitizers for specialized use cases.

Overview
--------

Sanitizers are functions that normalize strings before fuzzy matching. They remove common prefixes, suffixes, and special characters to improve matching accuracy.

The default sanitizer ([`_basic_sanitizer`](../api_reference/utils.rst)) removes:

* "City of " prefix
* " city" suffix
* "(Pob.)" and "(POB)" suffixes
* Periods, commas, hyphens, ampersands
* Parentheses

When to Customize
-----------------

Consider creating custom sanitizers when:

* **Domain-specific terminology**: Your data uses special terms
* **Regional variations**: Different regions use different naming conventions
* **Legacy data**: Historical data uses obsolete terms
* **Special characters**: Your data contains unique character patterns
* **Language variations**: Mixed English and Filipino terms

Creating Custom Sanitizers
--------------------------

Basic Custom Sanitizer
~~~~~~~~~~~~~~~~~~~~~~

Create a simple custom sanitizer:

.. code-block:: python

    from barangay import sanitize_input

    # Create a custom sanitizer
    def custom_sanitizer(input_str: str) -> str:
        """Custom sanitizer for specific use case.

        Args:
            input_str: Input string to sanitize

        Returns:
            Sanitized string
        """
        # Use the base sanitizer function
        sanitized = sanitize_input(
            input_str,
            exclude=[
                "city of ",
                " city",
                "pob.",
                "(pob)",
                ".",
                ",",
                "-",
                "&",
                "(",
                ")",
                # Add custom exclusions
                "barangay",
                "bgy.",
                "brgy."
            ]
        )

        return sanitized

    # Test the custom sanitizer
    examples = [
        "Barangay San Jose",
        "City of Manila",
        "Bgy. Poblacion",
        "Makati City"
    ]

    for example in examples:
        sanitized = custom_sanitizer(example)
        print(f"{example:30s} → {sanitized}")

Output:

.. code-block:: text

    Barangay San Jose             → san jose
    City of Manila                → manila
    Bgy. Poblacion                → poblacion
    Makati City                   → makati

Using Custom Sanitizers with Search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply custom sanitizers to search operations:

.. code-block:: python

    from barangay import search

    # Define custom sanitizer
    def address_sanitizer(input_str: str) -> str:
        """Sanitizer for address strings."""
        from barangay import sanitize_input

        return sanitize_input(
            input_str,
            exclude=[
                "city of ",
                " city",
                "pob.",
                "(pob)",
                "municipality of ",
                " municipality",
                ".",
                ",",
                "-",
                "&",
                "(",
                ")"
            ]
        )

    # Use custom sanitizer in search
    results = search(
        "Municipality of San Jose, Batangas",
        search_sanitizer=address_sanitizer,
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

Advanced Custom Sanitizers
--------------------------

Domain-Specific Sanitizers
~~~~~~~~~~~~~~~~~~~~~~~~~~

E-commerce Address Sanitizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a sanitizer for e-commerce addresses:

.. code-block:: python

    from barangay import sanitize_input

    def ecommerce_sanitizer(input_str: str) -> str:
        """Sanitizer for e-commerce addresses.

        Handles common e-commerce address formats and abbreviations.

        Args:
            input_str: Input string to sanitize

        Returns:
            Sanitized string
        """
        # Define e-commerce specific exclusions
        ecommerce_exclusions = [
            # Common prefixes
            "city of ",
            "municipality of ",
            "town of ",

            # Common suffixes
            " city",
            " municipality",
            " town",
            " poblacion",
            " poblacion",

            # Abbreviations
            "bgy.",
            "brgy.",
            "brg.",
            "pob.",
            "(pob)",
            "(pob.)",

            # Street indicators
            "street",
            "st.",
            "st ",
            "road",
            "rd.",
            "rd ",
            "avenue",
            "ave.",
            "ave ",
            "boulevard",
            "blvd.",
            "blvd ",

            # Building indicators
            "building",
            "bldg.",
            "bldg ",
            "unit",
            "floor",
            "flr.",

            # Punctuation
            ".",
            ",",
            "-",
            "&",
            "(",
            ")",
            "[",
            "]"
        ]

        sanitized = sanitize_input(input_str, exclude=ecommerce_exclusions)

        # Additional processing
        # Remove numbers (house numbers, postal codes)
        sanitized = ''.join(c for c in sanitized if not c.isdigit())

        return sanitized

    # Test the e-commerce sanitizer
    examples = [
        "Unit 123, Building A, San Jose Street, City of Manila",
        "Brgy. Poblacion, Municipality of Batangas",
        "123 Main St., Makati City",
        "Floor 5, Tower 2, Bgy. San Isidro"
    ]

    for example in examples:
        sanitized = ecommerce_sanitizer(example)
        print(f"{example:60s} → {sanitized}")

Government Form Sanitizer
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a sanitizer for government form addresses:

.. code-block:: python

    from barangay import sanitize_input

    def government_form_sanitizer(input_str: str) -> str:
        """Sanitizer for government form addresses.

        Handles formal government address formats.

        Args:
            input_str: Input string to sanitize

        Returns:
            Sanitized string
        """
        # Define government form specific exclusions
        gov_exclusions = [
            # Formal prefixes
            "city of ",
            "municipality of ",
            "province of ",

            # Formal suffixes
            " city",
            " municipality",
            " province",

            # Administrative terms
            "barangay",
            "bgy.",
            "brgy.",
            "sitio",
            "purok",
            "zone",

            # Formal designations
            "poblacion",
            " poblacion",
            "(pob)",
            "(pob.)",

            # Punctuation
            ".",
            ",",
            ";",
            "-",
            "&",
            "(",
            ")"
        ]

        sanitized = sanitize_input(input_str, exclude=gov_exclusions)

        # Remove Roman numerals (often used for zones)
        import re
        sanitized = re.sub(r'\b[IVXLCDM]+\b', '', sanitized)

        return sanitized

    # Test the government form sanitizer
    examples = [
        "Barangay Poblacion, Municipality of Batangas",
        "Zone IV, City of Manila",
        "Sitio Maligaya, Bgy. San Isidro",
        "Purok 3, Barangay San Jose"
    ]

    for example in examples:
        sanitized = government_form_sanitizer(example)
        print(f"{example:50s} → {sanitized}")

Combining Multiple Sanitizers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chain multiple sanitizers for comprehensive processing:

.. code-block:: python

    from barangay import sanitize_input

    def create_combined_sanitizer(exclusions_list: list) -> callable:
        """Create a combined sanitizer from multiple exclusion lists.

        Args:
            exclusions_list: List of exclusion lists to combine

        Returns:
            Combined sanitizer function
        """
        # Combine all exclusions
        combined_exclusions = []
        for exclusions in exclusions_list:
            combined_exclusions.extend(exclusions)

        # Remove duplicates while preserving order
        seen = set()
        unique_exclusions = []
        for item in combined_exclusions:
            if item not in seen:
                seen.add(item)
                unique_exclusions.append(item)

        # Create sanitizer function
        def combined_sanitizer(input_str: str) -> str:
            return sanitize_input(input_str, exclude=unique_exclusions)

        return combined_sanitizer

    # Define different exclusion sets
    basic_exclusions = ["city of ", " city", "pob.", "(pob)", ".", ",", "-"]
    ecommerce_exclusions = ["bgy.", "brgy.", "street", "st.", "st ", "road", "rd.", "rd "]
    government_exclusions = ["barangay", "bgy.", "brgy.", "sitio", "purok", "zone"]

    # Create combined sanitizer
    combined = create_combined_sanitizer([
        basic_exclusions,
        ecommerce_exclusions,
        government_exclusions
    ])

    # Test the combined sanitizer
    examples = [
        "Bgy. San Jose Street, City of Manila",
        "Barangay Poblacion, Municipality of Batangas",
        "Zone IV, St. Main, Makati City"
    ]

    for example in examples:
        sanitized = combined(example)
        print(f"{example:50s} → {sanitized}")

Sanitizer Testing
-----------------

Testing Sanitizer Effectiveness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create test cases to validate sanitizer behavior:

.. code-block:: python

    from barangay import search

    def test_sanitizer(
        sanitizer: callable,
        test_cases: list[dict],
        threshold: float = 80.0
    ) -> dict:
        """Test a sanitizer against test cases.

        Args:
            sanitizer: Sanitizer function to test
            test_cases: List of test case dictionaries with 'input' and 'expected' keys
            threshold: Minimum similarity score for passing

        Returns:
            Dictionary with test results
        """
        results = {
            'total': len(test_cases),
            'passed': 0,
            'failed': 0,
            'details': []
        }

        for i, test_case in enumerate(test_cases):
            input_str = test_case['input']
            expected = test_case.get('expected', None)

            # Apply sanitizer
            sanitized = sanitizer(input_str)

            # Search with sanitized string
            matches = search(sanitized, n=1, threshold=threshold)

            # Check result
            if matches:
                # Get the maximum score from active matching strategies
                scores = [
                    matches[0].get('f_000b_ratio_score', 0),
                    matches[0].get('f_0p0b_ratio_score', 0),
                    matches[0].get('f_00mb_ratio_score', 0),
                    matches[0].get('f_0pmb_ratio_score', 0)
                ]
                score = max(scores)
                if score >= threshold:
                    passed = True
                    matched = matches[0]['barangay']
                else:
                    passed = False
                    matched = None
            else:
                passed = False
                matched = None

            # Compare with expected if provided
            if expected and passed:
                passed = (matched == expected)

            # Record result
            result_detail = {
                'test_case': i + 1,
                'input': input_str,
                'sanitized': sanitized,
                'matched': matched,
                'expected': expected,
                'passed': passed
            }

            results['details'].append(result_detail)

            if passed:
                results['passed'] += 1
            else:
                results['failed'] += 1

        return results

    # Define test cases
    test_cases = [
        {
            'input': 'City of Manila',
            'expected': 'Manila'
        },
        {
            'input': 'Bgy. San Jose, Batangas',
            'expected': 'San Jose'
        },
        {
            'input': 'Poblacion, Tawi-Tawi',
            'expected': 'Poblacion'
        }
    ]

    # Test the default sanitizer
    from barangay.utils import _basic_sanitizer
    test_results = test_sanitizer(_basic_sanitizer, test_cases)

    print(f"Test Results: {test_results['passed']}/{test_results['total']} passed")

    for detail in test_results['details']:
        status = "✓" if detail['passed'] else "✗"
        print(f"{status} {detail['input']:40s} → {detail['sanitized']:30s} "
              f"(matched: {detail['matched']})")

Benchmarking Sanitizers
~~~~~~~~~~~~~~~~~~~~~~~

Compare different sanitizers:

.. code-block:: python

    from barangay import search
    import time

    def benchmark_sanitizer(
        sanitizer: callable,
        test_addresses: list[str],
        iterations: int = 10
    ) -> dict:
        """Benchmark a sanitizer's performance.

        Args:
            sanitizer: Sanitizer function to benchmark
            test_addresses: List of test addresses
            iterations: Number of iterations

        Returns:
            Dictionary with benchmark results
        """
        results = {
            'total_addresses': len(test_addresses),
            'iterations': iterations,
            'total_time': 0.0,
            'avg_time_per_address': 0.0,
            'avg_time_per_iteration': 0.0
        }

        # Warm up
        for address in test_addresses[:5]:
            sanitizer(address)

        # Benchmark
        start_time = time.time()
        for _ in range(iterations):
            for address in test_addresses:
                sanitized = sanitizer(address)
                # Simulate search
                search(sanitized, n=1, threshold=70.0)
        end_time = time.time()

        results['total_time'] = end_time - start_time
        results['avg_time_per_address'] = (
            results['total_time'] / (len(test_addresses) * iterations)
        )
        results['avg_time_per_iteration'] = (
            results['total_time'] / iterations
        )

        return results

    # Test addresses
    test_addresses = [
        "City of Manila",
        "Bgy. San Jose, Batangas",
        "Poblacion, Tawi-Tawi",
        "Makati City",
        "Municipality of Quezon"
    ]

    # Benchmark default sanitizer
    from barangay.utils import _basic_sanitizer
    default_results = benchmark_sanitizer(_basic_sanitizer, test_addresses)

    # Benchmark custom sanitizer
    def custom_sanitizer(input_str: str) -> str:
        from barangay import sanitize_input
        return sanitize_input(input_str, exclude=["city of ", " city", "bgy.", "brgy."])

    custom_results = benchmark_sanitizer(custom_sanitizer, test_addresses)

    # Compare results
    print("Benchmark Results:")
    print(f"\nDefault Sanitizer:")
    print(f"  Total time: {default_results['total_time']:.2f}s")
    print(f"  Avg per address: {default_results['avg_time_per_address']*1000:.2f}ms")
    print(f"  Avg per iteration: {default_results['avg_time_per_iteration']:.2f}s")

    print(f"\nCustom Sanitizer:")
    print(f"  Total time: {custom_results['total_time']:.2f}s")
    print(f"  Avg per address: {custom_results['avg_time_per_address']*1000:.2f}ms")
    print(f"  Avg per iteration: {custom_results['avg_time_per_iteration']:.2f}s")

Performance Considerations
--------------------------

Optimizing Sanitizer Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tips for creating efficient sanitizers:

1. **Use string methods**: Prefer built-in string methods over regex

.. code-block:: python

    # Good - string methods
    def efficient_sanitizer(input_str: str) -> str:
        sanitized = input_str.lower()
        for exclusion in exclusions:
            sanitized = sanitized.replace(exclusion, '')
        return sanitized

    # Less efficient - regex
    import re
    def less_efficient_sanitizer(input_str: str) -> str:
        pattern = '|'.join(re.escape(ex) for ex in exclusions)
        return re.sub(pattern, '', input_str.lower())

2. **Pre-compile patterns**: If using regex, pre-compile patterns

.. code-block:: python

    import re

    # Pre-compile pattern
    EXCLUSION_PATTERN = re.compile(
        '|'.join(re.escape(ex) for ex in exclusions),
        re.IGNORECASE
    )

    def regex_sanitizer(input_str: str) -> str:
        return EXCLUSION_PATTERN.sub('', input_str.lower())

3. **Cache results**: For frequently used inputs, cache sanitized results

.. code-block:: python

    from functools import lru_cache

    @lru_cache(maxsize=1000)
    def cached_sanitizer(input_str: str) -> str:
        from barangay import sanitize_input
        return sanitize_input(input_str, exclude=exclusions)

4. **Minimize operations**: Reduce the number of string operations

.. code-block:: python

    # Good - single pass
    def single_pass_sanitizer(input_str: str) -> str:
        # Combine all replacements in one pass
        result = input_str.lower()
        for exclusion in exclusions:
            result = result.replace(exclusion, '')
        return result

    # Less efficient - multiple passes
    def multi_pass_sanitizer(input_str: str) -> str:
        result = input_str
        for exclusion in exclusions:
            result = result.lower().replace(exclusion, '')
        return result

Code Examples for Various Use Cases
-----------------------------------

Real-World Sanitizer Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Logistics/Shipping Address Sanitizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from barangay import sanitize_input

    def logistics_sanitizer(input_str: str) -> str:
        """Sanitizer for logistics and shipping addresses.

        Handles common logistics address formats.

        Args:
            input_str: Input string to sanitize

        Returns:
            Sanitized string
        """
        logistics_exclusions = [
            # Location types
            "city of ",
            " municipality of ",
            " town of ",

            # Common suffixes
            " city",
            " municipality",
            " town",
            " district",
            " subdistrict",

            # Barangay variations
            "barangay",
            "bgy.",
            "brgy.",
            "brg.",
            "pob.",
            "(pob)",
            "(pob.)",

            # Street types
            "street",
            "st.",
            "st ",
            "road",
            "rd.",
            "rd ",
            "avenue",
            "ave.",
            "ave ",
            "boulevard",
            "blvd.",
            "blvd ",
            "lane",
            "ln.",
            "ln ",
            "drive",
            "dr.",
            "dr ",

            # Building types
            "building",
            "bldg.",
            "bldg ",
            "warehouse",
            "facility",
            "terminal",

            # Logistics terms
            "port",
            "pier",
            "dock",
            "depot",
            "hub",

            # Punctuation
            ".",
            ",",
            ";",
            "-",
            "&",
            "(",
            ")",
            "#"
        ]

        sanitized = sanitize_input(input_str, exclude=logistics_exclusions)

        # Remove numbers (tracking numbers, etc.)
        sanitized = ''.join(c for c in sanitized if not c.isdigit())

        return sanitized

Real Estate Address Sanitizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from barangay import sanitize_input

    def real_estate_sanitizer(input_str: str) -> str:
        """Sanitizer for real estate addresses.

        Handles common real estate address formats.

        Args:
            input_str: Input string to sanitize

        Returns:
            Sanitized string
        """
        real_estate_exclusions = [
            # Property types
            "subdivision",
            "subd.",
            "village",
            "vlg.",
            "estate",
            "residential",
            "commercial",

            # Location indicators
            "city of ",
            " municipality of ",
            " barangay",
            "bgy.",
            "brgy.",
            "pob.",
            "(pob)",

            # Street types
            "street",
            "st.",
            "st ",
            "road",
            "rd.",
            "rd ",
            "avenue",
            "ave.",
            "ave ",
            "boulevard",
            "blvd.",
            "blvd ",
            "lane",
            "drive",
            "circle",
            "crescent",

            # Building types
            "building",
            "bldg.",
            "bldg ",
            "condominium",
            "condo.",
            "condo ",
            "apartment",
            "apt.",
            "apt ",
            "house",
            "lot",
            "block",
            "bl.",

            # Punctuation
            ".",
            ",",
            "-",
            "&",
            "(",
            ")",
            "#"
        ]

        sanitized = sanitize_input(input_str, exclude=real_estate_exclusions)

        # Remove lot and block numbers
        import re
        sanitized = re.sub(r'\b(lot|block|bl)\s*\d*', '', sanitized, flags=re.IGNORECASE)

        return sanitized

Emergency Services Address Sanitizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from barangay import sanitize_input

    def emergency_sanitizer(input_str: str) -> str:
        """Sanitizer for emergency services addresses.

        Prioritizes accuracy for critical services.

        Args:
            input_str: Input string to sanitize

        Returns:
            Sanitized string
        """
        emergency_exclusions = [
            # Critical location indicators
            "city of ",
            " municipality of ",
            " barangay",
            "bgy.",
            "brgy.",
            "pob.",
            "(pob)",

            # Emergency facility types
            "hospital",
            "clinic",
            "health center",
            "fire station",
            "police station",
            "emergency",
            "ambulance",

            # Street types (keep for accuracy)
            # Minimal exclusions for emergency services
            ".",
            ",",
            "-",
            "&",
            "(",
            ")"
        ]

        sanitized = sanitize_input(input_str, exclude=emergency_exclusions)

        return sanitized

See Also
--------

* :ref:`api-utils` - Utility functions API reference
* :ref:`api-search` - Search function API reference
* :ref:`advanced-fuzzy-matching` - Fuzzy matching internals
* :ref:`examples-address-validation` - Address validation examples