Custom Sanitizers
=================

This section covers the internals of sanitizers and how they work within the barangay package.

Overview
--------

Sanitizers are functions that normalize strings before fuzzy matching. They remove common prefixes, suffixes, and special characters to improve matching accuracy.

The default sanitizer ([`_basic_sanitizer`](../api_reference/utils.rst)) removes:

* "City of " prefix
* " city" suffix
* "(Pob.)" and "(POB)" suffixes
* Periods, commas, hyphens, ampersands
* Parentheses

Sanitization Process
--------------------

How Sanitizers Work
~~~~~~~~~~~~~~~~~~~

The sanitization process follows these steps:

1. **Input normalization**: Convert string to lowercase
2. **Pattern matching**: Identify and remove excluded patterns
3. **Result generation**: Return sanitized string for fuzzy matching

The [`sanitize_input`](../api_reference/utils.rst) function provides the core sanitization logic:

.. code-block:: python

    from barangay import sanitize_input

    # Basic sanitization
    sanitized = sanitize_input(
        "City of Manila",
        exclude=["city of ", " city", "pob.", "(pob)", ".", ",", "-", "&", "(", ")"]
    )
    # Result: "manila"

Sanitization and Fuzzy Matching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sanitization occurs before fuzzy matching to improve accuracy:

.. mermaid::

    graph LR
        A[Input String] --> B[Sanitizer]
        B --> C[Sanitized String]
        C --> D[Fuzzy Matching]
        D --> E[Match Results]

The sanitized string is compared against pre-computed sanitized strings in the FuzzBase, allowing for more accurate matching despite variations in input format.

Performance Considerations
--------------------------

Sanitizer Performance
~~~~~~~~~~~~~~~~~~~~~

The performance of sanitizers depends on:

1. **Number of exclusions**: More exclusions mean more string operations
2. **String length**: Longer strings take more time to process
3. **Exclusion pattern complexity**: Simple patterns are faster than complex ones

Optimization Techniques
~~~~~~~~~~~~~~~~~~~~~~~

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

For practical examples of creating and using custom sanitizers, see :doc:`../how_to/custom_matching`.

See Also
--------

* :ref:`api-utils` - Utility functions API reference
* :ref:`api-search` - Search function API reference
* :ref:`advanced-fuzzy-matching` - Fuzzy matching internals
* :doc:`../how_to/custom_matching` - Custom matching guide