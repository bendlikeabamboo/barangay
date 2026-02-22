Error Handling
==============

This section provides information about the error handling architecture in the barangay package.

Overview
--------

The barangay package may raise various exceptions depending on the operation being performed. Proper error handling ensures your application remains robust and provides helpful feedback to users.

Common Exception Types:

* **ValueError**: Invalid parameters or configuration
* **RuntimeError**: Download failures or data loading errors
* **FileNotFoundError**: Missing data files
* **ConnectionError**: Network-related issues
* **KeyError**: Missing data keys or columns

Exception Hierarchy
-------------------

The package follows Python's standard exception hierarchy:

.. mermaid::

    graph TD
        A[Exception] --> B[ValueError]
        A --> C[RuntimeError]
        A --> D[FileNotFoundError]
        A --> E[ConnectionError]
        A --> F[KeyError]

        B --> B1[Invalid match_hooks]
        B --> B2[Invalid data_type]
        B --> B3[Invalid date format]

        C --> C1[Download failures]
        C --> C2[Data corruption]

        D --> D1[Missing package data]
        D --> D2[Missing cache file]

        E --> E1[Network timeout]
        E --> E2[Rate limiting]

        F --> F1[Missing data keys]
        F --> F2[Missing columns]

Error Sources
-------------

The main sources of errors in the barangay package are:

Data Loading Errors
~~~~~~~~~~~~~~~~~~~

Errors that occur during data loading:

* **Package data missing**: Installation is incomplete
* **Cache file missing**: Expected cache file doesn't exist
* **Download failure**: Cannot download from GitHub
* **Data corruption**: Cached data is corrupted

Search Errors
~~~~~~~~~~~~~

Errors that occur during search operations:

* **Invalid parameters**: Match hooks, thresholds, or other parameters are invalid
* **No matches**: No results found above threshold
* **Data format error**: Search results have unexpected format

Network Errors
~~~~~~~~~~~~~~

Errors that occur during network operations:

* **Connection timeout**: Request takes too long
* **Rate limiting**: GitHub API rate limit exceeded
* **HTTP errors**: Server returns error status

For practical error handling patterns and examples, see :doc:`../how_to/address_validation` and :doc:`../troubleshooting/common_errors`.

See Also
--------

* :doc:`../api_reference/search` - Search function API reference
* :doc:`../api_reference/data_manager` - DataManager class API reference
* :doc:`../troubleshooting/common_errors` - Common errors and solutions
* :doc:`../how_to/address_validation` - Address validation guide