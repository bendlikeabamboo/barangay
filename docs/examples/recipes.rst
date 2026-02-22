Recipes
=======

This section contains short, reusable code snippets for common tasks with the barangay package. Each recipe is copy-paste ready and focuses on practical, frequently-used patterns.

Basic Search
------------

**Problem**: Perform a simple fuzzy search for a barangay.

**Solution**:

.. code-block:: python

    from barangay import search

    results = search("Tongmageng, Tawi-Tawi")
    print(results[0])

Search with Custom Threshold
----------------------------

**Problem**: Control the minimum similarity score required for matches.

**Solution**:

.. code-block:: python

    from barangay import search

    # Only return matches with 80% similarity or higher
    results = search("San Jose", threshold=80.0)
    print(f"Found {len(results)} matches above 80% similarity")

Search with Result Limit
------------------------

**Problem**: Limit the number of results returned.

**Solution**:

.. code-block:: python

    from barangay import search

    # Get only top 3 results
    results = search("San Jose", n=3)
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['barangay']}, {result['municipality_or_city']}")

Calculate Maximum Score
-----------------------

**Problem**: Get the maximum score from active matching strategies for confidence assessment.

**Solution**:

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

Load Data into DataFrame
------------------------

**Problem**: Convert barangay data to a pandas DataFrame for analysis.

**Solution**:

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    df = pd.DataFrame(BARANGAY_FLAT)
    print(f"Total barangays: {len(df)}")
    print(df.head())

Search with Historical Data
---------------------------

**Problem**: Search using data from a specific historical date.

**Solution**:

.. code-block:: python

    from barangay import search

    # Search with historical data
    results = search("Tongmageng", as_of="2025-07-08")

Check Available Dates
---------------------

**Problem**: List all available historical dataset dates.

**Solution**:

.. code-block:: python

    from barangay import available_dates

    print("Available dates:")
    for date in sorted(available_dates, reverse=True):
        print(f"  - {date}")

Batch Validate Addresses
------------------------

**Problem**: Validate multiple addresses efficiently.

**Solution**:

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

Create FuzzBase for Performance
-------------------------------

**Problem**: Reuse FuzzBase instance for faster multiple searches.

**Solution**:

.. code-block:: python

    from barangay import search, create_fuzz_base

    # Create FuzzBase once
    fuzz_base = create_fuzz_base()

    # Reuse for multiple searches (faster)
    results1 = search("San Jose", fuzz_base=fuzz_base)
    results2 = search("Quezon City", fuzz_base=fuzz_base)
    results3 = search("Manila", fuzz_base=fuzz_base)

Filter Data by Region
---------------------

**Problem**: Filter barangay data by region using pandas.

**Solution**:

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    df = pd.DataFrame(BARANGAY_FLAT)

    # Filter by region
    ncr_df = df[df['region'] == 'National Capital Region (NCR)']
    print(f"NCR barangays: {len(ncr_df)}")

    # Filter by city
    manila_df = df[df['municipality_or_city'] == 'City of Manila']
    print(f"Manila barangays: {len(manila_df)}")

Export Data to CSV
------------------

**Problem**: Export barangay data to CSV file.

**Solution**:

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    df = pd.DataFrame(BARANGAY_FLAT)

    # Export to CSV
    df.to_csv('philippine_barangays.csv', index=False)
    print("Exported to philippine_barangays.csv")

Search with Match Hooks
-----------------------

**Problem**: Match against specific administrative levels.

**Solution**:

.. code-block:: python

    from barangay import search

    # Match only barangay names
    results = search("San Jose", match_hooks=["barangay"])

    # Match against municipality and barangay
    results = search("San Jose", match_hooks=["municipality", "barangay"])

    # Match against all levels (default)
    results = search("San Jose", match_hooks=["province", "municipality", "barangay"])