Caching Mechanisms
==================

This section provides detailed information about the caching architecture and behavior of the barangay package.

Overview
--------

The barangay package implements a multi-layered caching system to optimize performance and reduce redundant data loading. Caching occurs at two levels:

1. **Data Caching**: Historical data downloaded from GitHub is cached locally
2. **FuzzBase Caching**: Pre-computed fuzzy matching functions can be reused across searches

Benefits of Caching:

* **Faster subsequent loads**: Cached data loads instantly
* **Reduced network usage**: Download data only once per version
* **Lower API costs**: Avoid repeated GitHub API calls
* **Improved performance**: Pre-computed functions speed up searches

Caching Architecture
--------------------

Cache Layers
~~~~~~~~~~~~

The caching system has three layers:

.. mermaid::

    graph TD
        A[Request Data] --> B{Is Current Date?}
        B -->|Yes| C[Load from Package]
        B -->|No| D{In Local Cache?}
        D -->|Yes| E[Load from Cache]
        D -->|No| F[Download from GitHub]
        F --> G[Save to Cache]
        G --> E

Layer 1: Package Data
~~~~~~~~~~~~~~~~~~~~~

The current version of barangay data is bundled with the package installation. This data is always available and doesn't require caching.

Characteristics:

* **Always available**: No network access required
* **Fastest access**: Loaded directly from package files
* **Version-specific**: Matches the package version
* **Read-only**: Cannot be modified

Accessed when:

* `as_of` parameter is `None`
* `as_of` parameter matches the current package date

Layer 2: Local Cache
~~~~~~~~~~~~~~~~~~~~

Historical data is cached locally after the first download. Subsequent requests for the same date load from cache instead of downloading.

Characteristics:

* **Persistent**: Survives across sessions
* **Fast**: Loads from local filesystem
* **Version-specific**: Each date has its own cache file
* **Automatic**: Managed by the DataManager class

Cache Location:

* **Windows**: `%LOCALAPPDATA%\barangay\cache`
* **Linux/Mac (XDG)**: `$XDG_CACHE_HOME/barangay`
* **Linux/Mac (fallback)**: `~/.cache/barangay`
* **Custom**: `$BARANGAY_CACHE_DIR` if set

Layer 3: GitHub Download
~~~~~~~~~~~~~~~~~~~~~~~~

If data is not in the package or local cache, it's downloaded from the GitHub repository.

Characteristics:

* **Network required**: Requires internet connection
* **Slower**: Depends on network speed
* **Rate limited**: Subject to GitHub API limits
* **One-time**: Downloaded data is cached for future use

Cache Directory Structure
-------------------------

Directory Layout
~~~~~~~~~~~~~~~~

The cache directory is organized as follows:

.. code-block:: text

    ~/.cache/barangay/
    ├── 2025-07-08_barangay.json
    ├── 2025-07-08_barangay_extended.json
    ├── 2025-07-08_barangay_flat.json
    ├── 2025-07-08_fuzzer_base.parquet
    ├── 2025-08-29_barangay.json
    ├── 2025-08-29_barangay_extended.json
    ├── 2025-08-29_barangay_flat.json
    ├── 2025-08-29_fuzzer_base.parquet
    └── ...

File Naming Convention
~~~~~~~~~~~~~~~~~~~~~~

Cache files follow the pattern: `{date}_{filename}`

Components:

* **date**: YYYY-MM-DD format (e.g., "2025-07-08")
* **filename**: Original data filename (e.g., "barangay.json")

Examples:

* `2025-07-08_barangay.json` - Basic data for July 8, 2025
* `2025-08-29_fuzzer_base.parquet` - FuzzBase data for August 29, 2025

Cache Invalidation
------------------

Automatic Invalidation
~~~~~~~~~~~~~~~~~~~~~~

Cache files are automatically invalidated when:

* **Data version changes**: New PSGC releases have different dates
* **Manual deletion**: User deletes cache files
* **Corruption detected**: Cache files fail to load

The package does **not** automatically delete old cache files. They remain available for historical analysis.

For practical cache management and performance optimization, see :doc:`../how_to/performance`.

See Also
--------

* :ref:`api-data-manager` - DataManager class API reference
* :ref:`api-downloader` - Downloader functions API reference
* :doc:`../how_to/performance` - Performance optimization guide