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

Manual Cache Management
~~~~~~~~~~~~~~~~~~~~~~~

You can manually manage the cache using the following approaches:

Checking Cache Contents
~~~~~~~~~~~~~~~~~~~~~~~

List all cached files:

.. code-block:: python

    import os
    from pathlib import Path
    from barangay import get_cache_dir

    def list_cached_files() -> dict:
        """List all cached data files.

        Returns:
            Dictionary with cache information
        """
        cache_dir = Path(get_cache_dir())

        if not cache_dir.exists():
            return {
                'cache_dir': str(cache_dir),
                'exists': False,
                'files': []
            }

        files = list(cache_dir.glob('*'))
        file_info = []

        for file in files:
            stat = file.stat()
            file_info.append({
                'filename': file.name,
                'size_mb': stat.st_size / (1024 * 1024),
                'modified': stat.st_mtime
            })

        return {
            'cache_dir': str(cache_dir),
            'exists': True,
            'total_files': len(files),
            'total_size_mb': sum(f['size_mb'] for f in file_info),
            'files': file_info
        }

    # Example usage
    cache_info = list_cached_files()
    print(f"Cache directory: {cache_info['cache_dir']}")
    print(f"Total files: {cache_info['total_files']}")
    print(f"Total size: {cache_info['total_size_mb']:.2f} MB")

    for file in cache_info['files']:
        print(f"  {file['filename']} ({file['size_mb']:.2f} MB)")

Clearing Cache
~~~~~~~~~~~~~~

Clear all cached files:

.. code-block:: python

    import shutil
    from pathlib import Path
    from barangay import get_cache_dir

    def clear_cache() -> dict:
        """Clear all cached data files.

        Returns:
            Dictionary with operation results
        """
        cache_dir = Path(get_cache_dir())

        if not cache_dir.exists():
            return {
                'success': False,
                'message': 'Cache directory does not exist',
                'cache_dir': str(cache_dir)
            }

        # Count files before deletion
        files = list(cache_dir.glob('*'))
        file_count = len(files)

        # Delete all files
        shutil.rmtree(cache_dir)

        return {
            'success': True,
            'message': f'Deleted {file_count} cached files',
            'cache_dir': str(cache_dir),
            'files_deleted': file_count
        }

    # Example usage
    result = clear_cache()
    print(result['message'])

Clearing Cache for Specific Date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clear cache files for a specific date:

.. code-block:: python

    import os
    from pathlib import Path
    from barangay import get_cache_dir

    def clear_cache_for_date(date: str) -> dict:
        """Clear cache files for a specific date.

        Args:
            date: Date string (YYYY-MM-DD)

        Returns:
            Dictionary with operation results
        """
        cache_dir = Path(get_cache_dir())

        if not cache_dir.exists():
            return {
                'success': False,
                'message': 'Cache directory does not exist',
                'cache_dir': str(cache_dir)
            }

        # Find files matching the date
        pattern = f"{date}_*"
        files = list(cache_dir.glob(pattern))
        file_count = len(files)

        # Delete matching files
        for file in files:
            file.unlink()

        return {
            'success': True,
            'message': f'Deleted {file_count} cached files for {date}',
            'cache_dir': str(cache_dir),
            'files_deleted': file_count
        }

    # Example usage
    result = clear_cache_for_date("2025-07-08")
    print(result['message'])

Cache Performance
-----------------

Hit Rate Analysis
~~~~~~~~~~~~~~~~~

Monitor cache hit rates to understand caching effectiveness:

.. code-block:: python

    from barangay import DataManager
    from collections import defaultdict

    class CacheMonitor:
        """Monitor cache performance."""

        def __init__(self):
            self.stats = defaultdict(int)

        def get_data(self, data_type: str, as_of: str = None) -> dict:
            """Get data with cache monitoring.

            Args:
                data_type: Type of data to load
                as_of: Optional date string

            Returns:
                Loaded data
            """
            dm = DataManager()

            # Determine source
            if as_of is None or as_of == dm._get_current_date():
                self.stats['package_hits'] += 1
                return dm._load_from_package(data_type)
            else:
                # Try cache first
                cached = dm._load_from_cache(as_of, data_type)
                if cached is not None:
                    self.stats['cache_hits'] += 1
                    return cached
                else:
                    self.stats['cache_misses'] += 1
                    return dm._download_from_github(as_of, data_type)

        def get_statistics(self) -> dict:
            """Get cache statistics.

            Returns:
                Dictionary with cache statistics
            """
            total = sum(self.stats.values())
            if total == 0:
                return {'total_requests': 0}

            cache_hit_rate = (self.stats['cache_hits'] / total) * 100
            package_hit_rate = (self.stats['package_hits'] / total) * 100
            miss_rate = (self.stats['cache_misses'] / total) * 100

            return {
                'total_requests': total,
                'package_hits': self.stats['package_hits'],
                'cache_hits': self.stats['cache_hits'],
                'cache_misses': self.stats['cache_misses'],
                'package_hit_rate': f'{package_hit_rate:.1f}%',
                'cache_hit_rate': f'{cache_hit_rate:.1f}%',
                'miss_rate': f'{miss_rate:.1f}%'
            }

    # Example usage
    monitor = CacheMonitor()

    # Simulate multiple data requests
    monitor.get_data('basic', as_of='2025-07-08')  # Cache miss (first time)
    monitor.get_data('basic', as_of='2025-07-08')  # Cache hit
    monitor.get_data('basic', as_of='2025-08-29')  # Cache miss (first time)
    monitor.get_data('basic', as_of='2025-08-29')  # Cache hit
    monitor.get_data('basic')  # Package hit

    stats = monitor.get_statistics()
    print("Cache Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

Cache Warming
~~~~~~~~~~~~~

Pre-load cache by downloading all available historical data:

.. code-block:: python

    from barangay import DataManager, get_available_dates

    def warm_cache() -> dict:
        """Warm cache by downloading all available historical data.

        Returns:
            Dictionary with warming results
        """
        dm = DataManager()
        available_dates = get_available_dates()

        results = {
            'total_dates': len(available_dates),
            'downloaded': 0,
            'already_cached': 0,
            'errors': []
        }

        for date in available_dates:
            try:
                # Try to load from cache first
                cached = dm._load_from_cache(date, 'basic')

                if cached is not None:
                    results['already_cached'] += 1
                else:
                    # Download and cache
                    dm._download_from_github(date, 'basic')
                    results['downloaded'] += 1

            except Exception as e:
                results['errors'].append({
                    'date': date,
                    'error': str(e)
                })

        return results

    # Example usage
    results = warm_cache()
    print(f"Cache warming complete!")
    print(f"  Downloaded: {results['downloaded']} datasets")
    print(f"  Already cached: {results['already_cached']} datasets")
    print(f"  Errors: {len(results['errors'])}")

Troubleshooting Cache Issues
----------------------------

Common Cache Problems
~~~~~~~~~~~~~~~~~~~~~

Cache Not Being Used
~~~~~~~~~~~~~~~~~~~~

**Symptom**: Data is downloaded every time even though it should be cached.

**Possible Causes**:

1. **Incorrect cache directory**: Cache directory path is wrong
2. **Permission issues**: Cannot write to cache directory
3. **Date mismatch**: Requested date doesn't match cached file names

**Solutions**:

.. code-block:: python

    from barangay import get_cache_dir
    from pathlib import Path

    # Check cache directory
    cache_dir = Path(get_cache_dir())
    print(f"Cache directory: {cache_dir}")
    print(f"Exists: {cache_dir.exists()}")
    print(f"Writable: {os.access(cache_dir, os.W_OK)}")

    # List cached files
    if cache_dir.exists():
        files = list(cache_dir.glob('*'))
        print(f"Cached files: {len(files)}")
        for file in files:
            print(f"  {file.name}")

Cache Corruption
~~~~~~~~~~~~~~~~

**Symptom**: Errors when loading cached data.

**Possible Causes**:

1. **Incomplete download**: Download was interrupted
2. **File system error**: Disk corruption or I/O error
3. **Version mismatch**: Cached file format is incompatible

**Solutions**:

.. code-block:: python

    from barangay import DataManager

    def repair_cache() -> dict:
        """Attempt to repair corrupted cache files.

        Returns:
            Dictionary with repair results
        """
        dm = DataManager()
        results = {
            'checked': 0,
            'repaired': 0,
            'failed': [],
            'deleted': []
        }

        # Get all cached files
        cache_dir = Path(get_cache_dir())
        if not cache_dir.exists():
            return results

        files = list(cache_dir.glob('*.json')) + list(cache_dir.glob('*.parquet'))

        for file in files:
            results['checked'] += 1

            # Try to load the file
            try:
                if file.suffix == '.json':
                    import json
                    with open(file) as f:
                        json.load(f)
                elif file.suffix == '.parquet':
                    import pandas as pd
                    pd.read_parquet(file)

                results['repaired'] += 1

            except Exception as e:
                # File is corrupted, delete it
                file.unlink()
                results['deleted'].append(file.name)
                results['failed'].append({
                    'file': file.name,
                    'error': str(e)
                })

        return results

    # Example usage
    repair_results = repair_cache()
    print(f"Checked {repair_results['checked']} files")
    print(f"Repaired: {repair_results['repaired']}")
    print(f"Deleted corrupted: {len(repair_results['deleted'])}")

    if repair_results['deleted']:
        print("Deleted files:")
        for filename in repair_results['deleted']:
            print(f"  {filename}")

Cache Size Issues
~~~~~~~~~~~~~~~~~

**Symptom**: Cache directory is using too much disk space.

**Solutions**:

.. code-block:: python

    from pathlib import Path
    from barangay import get_cache_dir

    def manage_cache_size(max_size_mb: float = 500) -> dict:
        """Manage cache size by deleting oldest files.

        Args:
            max_size_mb: Maximum cache size in MB

        Returns:
            Dictionary with management results
        """
        cache_dir = Path(get_cache_dir())
        if not cache_dir.exists():
            return {'success': False, 'message': 'Cache directory does not exist'}

        # Get all cache files with modification times
        files = []
        for file in cache_dir.glob('*'):
            stat = file.stat()
            files.append({
                'path': file,
                'size_mb': stat.st_size / (1024 * 1024),
                'modified': stat.st_mtime
            })

        # Calculate total size
        total_size = sum(f['size_mb'] for f in files)

        if total_size <= max_size_mb:
            return {
                'success': True,
                'message': f'Cache size ({total_size:.2f} MB) is within limit ({max_size_mb} MB)',
                'total_size_mb': total_size,
                'files_deleted': 0
            }

        # Sort by modification time (oldest first)
        files.sort(key=lambda x: x['modified'])

        # Delete oldest files until under limit
        deleted = 0
        while total_size > max_size_mb and files:
            file = files.pop(0)
            file['path'].unlink()
            total_size -= file['size_mb']
            deleted += 1

        return {
            'success': True,
            'message': f'Deleted {deleted} files to reduce cache size',
            'total_size_mb': total_size,
            'files_deleted': deleted
        }

    # Example usage
    result = manage_cache_size(max_size_mb=500)
    print(result['message'])

Custom Cache Configuration
--------------------------

Setting Custom Cache Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set a custom cache directory using the `BARANGAY_CACHE_DIR` environment variable:

.. code-block:: bash

    # Linux/Mac
    export BARANGAY_CACHE_DIR=/path/to/custom/cache

    # Windows
    set BARANGAY_CACHE_DIR=C:\path\to\custom\cache

Or set it programmatically:

.. code-block:: python

    import os
    from barangay import get_cache_dir

    # Set custom cache directory
    os.environ['BARANGAY_CACHE_DIR'] = '/path/to/custom/cache'

    # Verify the new cache directory
    cache_dir = get_cache_dir()
    print(f"Cache directory: {cache_dir}")

Disabling Caching
~~~~~~~~~~~~~~~~~

To disable caching (not recommended for production), you can implement a custom DataManager:

.. code-block:: python

    from barangay.data_manager import DataManager

    class NoCacheDataManager(DataManager):
        """DataManager that bypasses cache."""

        def get_data(self, as_of=None, data_type="basic"):
            """Get data without using cache.

            Args:
                as_of: Optional date string
                data_type: Type of data to load

            Returns:
                Loaded data
            """
            # Always load from package or download, never from cache
            from .config import resolve_as_of, get_verbose
            from .date_resolver import resolve_date, get_available_dates

            as_of = resolve_as_of(as_of)
            available_dates = get_available_dates()
            resolved_date, _ = resolve_date(as_of, available_dates, self._get_current_date())

            if resolved_date is None or resolved_date == self._get_current_date():
                return self._load_from_package(data_type)
            else:
                # Always download, never use cache
                return self._download_from_github(resolved_date, data_type)

Code Examples for Cache Operations
----------------------------------

Cache Inspection Utility
~~~~~~~~~~~~~~~~~~~~~~~~

A comprehensive utility for inspecting and managing cache:

.. code-block:: python

    import os
    import json
    from pathlib import Path
    from datetime import datetime
    from barangay import get_cache_dir

    class CacheInspector:
        """Utility for inspecting and managing cache."""

        def __init__(self):
            self.cache_dir = Path(get_cache_dir())

        def get_info(self) -> dict:
            """Get comprehensive cache information.

            Returns:
                Dictionary with cache information
            """
            if not self.cache_dir.exists():
                return {
                    'exists': False,
                    'path': str(self.cache_dir)
                }

            files = list(self.cache_dir.glob('*'))
            total_size = sum(f.stat().st_size for f in files)

            # Group by date
            by_date = {}
            for file in files:
                date = file.name.split('_')[0]
                if date not in by_date:
                    by_date[date] = []
                by_date[date].append(file.name)

            return {
                'exists': True,
                'path': str(self.cache_dir),
                'total_files': len(files),
                'total_size_mb': total_size / (1024 * 1024),
                'total_size_gb': total_size / (1024 * 1024 * 1024),
                'dates_cached': len(by_date),
                'files_by_date': by_date,
                'oldest_file': min(files, key=lambda f: f.stat().st_mtime).name if files else None,
                'newest_file': max(files, key=lambda f: f.stat().st_mtime).name if files else None
            }

        def print_info(self) -> None:
            """Print cache information in a readable format."""
            info = self.get_info()

            if not info['exists']:
                print(f"Cache directory does not exist: {info['path']}")
                return

            print("=" * 60)
            print("Cache Information")
            print("=" * 60)
            print(f"Path: {info['path']}")
            print(f"Total files: {info['total_files']}")
            print(f"Total size: {info['total_size_mb']:.2f} MB ({info['total_size_gb']:.3f} GB)")
            print(f"Dates cached: {info['dates_cached']}")
            print(f"Oldest file: {info['oldest_file']}")
            print(f"Newest file: {info['newest_file']}")

            print("\nFiles by date:")
            for date, files in sorted(info['files_by_date'].items()):
                print(f"  {date}: {len(files)} files")

            print("=" * 60)

        def export_info(self, output_path: str) -> None:
            """Export cache information to JSON file.

            Args:
                output_path: Path to output JSON file
            """
            info = self.get_info()

            # Convert Path objects to strings for JSON serialization
            if 'files_by_date' in info:
                info['files_by_date'] = {
                    date: files
                    for date, files in info['files_by_date'].items()
                }

            with open(output_path, 'w') as f:
                json.dump(info, f, indent=2)

            print(f"Cache information exported to {output_path}")

    # Example usage
    inspector = CacheInspector()
    inspector.print_info()

    # Export to JSON
    inspector.export_info('cache_info.json')

See Also
--------

* :ref:`api-data-manager` - DataManager class API reference
* :ref:`api-downloader` - Downloader functions API reference
* :ref:`userguide-configuration` - Configuration guide
* :ref:`advanced-error-handling` - Error handling patterns