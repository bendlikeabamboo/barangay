Common Usage Patterns
=====================

This section consolidates the most frequently used patterns from the documentation. Each pattern includes a brief description and copy-paste ready code.

Basic Search
------------

Perform a simple fuzzy search for a barangay.

.. code-block:: python

    from barangay import search

    results = search("Tongmageng, Tawi-Tawi")
    print(results[0])

Search with Custom Threshold
----------------------------

Control the minimum similarity score required for matches.

.. code-block:: python

    from barangay import search

    # Only return matches with 80% similarity or higher
    results = search("San Jose", threshold=80.0)
    print(f"Found {len(results)} matches above 80% similarity")

Search with Result Limit
------------------------

Limit the number of results returned.

.. code-block:: python

    from barangay import search

    # Get only top 3 results
    results = search("San Jose", n=3)
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['barangay']}, {result['municipality_or_city']}")

Calculate Maximum Score
-----------------------

Get the maximum score from active matching strategies for confidence assessment.

.. code-block:: python

    from barangay import search

    results = search("Tongmagen, Tawi-Tawi")
    for result in results:
        scores = [
            result.get('f_000b_ratio_score', 0),
            result.get('f_0p0b_ratio_score', 0),
            result.get('f_00mb_ratio_score', 0),
            result.get('f_0pmb_ratio_score', 0)
        ]
        score = max(scores)
        print(f"{result['barangay']} - Score: {score:.1f}%")

Batch Validate Addresses
------------------------

Validate multiple addresses efficiently.

.. code-block:: python

    import pandas as pd
    from barangay import search

    def batch_validate(addresses, threshold=80.0):
        results = []
        for address in addresses:
            matches = search(address, n=1, threshold=threshold)
            if matches:
                scores = [
                    matches[0].get('f_000b_ratio_score', 0),
                    matches[0].get('f_0p0b_ratio_score', 0),
                    matches[0].get('f_00mb_ratio_score', 0),
                    matches[0].get('f_0pmb_ratio_score', 0)
                ]
                score = max(scores)
                if score >= threshold:
                    results.append({'address': address, 'valid': True, 'score': score})
        return pd.DataFrame(results)

    addresses = ["Tongmageng, Tawi-Tawi", "San Jose, Manila"]
    df = batch_validate(addresses)
    print(df)

Load Data into pandas DataFrame
-------------------------------

Convert barangay data to a pandas DataFrame for analysis.

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    df = pd.DataFrame(BARANGAY_FLAT)
    print(f"Total barangays: {len(df)}")
    print(df.head())