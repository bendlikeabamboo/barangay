Performance Issues
==================

This section covers performance troubleshooting and optimization tips for the barangay package.

Slow Search Performance
-----------------------

Understanding Search Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search performance depends on several factors:

* **Match hooks**: More hooks = slower search
* **Dataset size**: Larger datasets take longer to search
* **Threshold**: Lower thresholds require more comparisons
* **Number of results**: More results = more processing
* **FuzzBase reuse**: Creating FuzzBase is expensive, reusing is fast

Performance Benchmarks
~~~~~~~~~~~~~~~~~~~~~~

Typical search times on a modern laptop:

.. list-table:: Search Performance Benchmarks
   :widths: 25 25 25 25
   :header-rows: 1

   * - Match Hooks
     - Threshold
     - Results (n)
     - Time (ms)
   * - barangay
     - 60
     - 5
     - ~15-25
   * - municipality + barangay
     - 60
     - 5
     - ~25-40
   * - province + barangay
     - 60
     - 5
     - ~30-45
   * - All three
     - 60
     - 5
     - ~70-90

.. note:: These benchmarks are approximate and depend on your system configuration.

Optimization Strategies
~~~~~~~~~~~~~~~~~~~~~~~

1. **Reduce Match Hooks**

   Use only the match hooks you need:

   .. code-block:: python

      from barangay import search

      # Slower (all hooks)
      results = search("San Jose", match_hooks=["province", "municipality", "barangay"])

      # Faster (only barangay)
      results = search("San Jose", match_hooks=["barangay"])

   .. tip:: If you only need barangay names, use ``match_hooks=["barangay"]`` for 3-4x speedup.

2. **Increase Threshold**

   Higher thresholds filter out low-score matches early:

   .. code-block:: python

      from barangay import search

      # Slower (processes more matches)
      results = search("San Jose", threshold=40.0)

      # Faster (filters early)
      results = search("San Jose", threshold=80.0)

3. **Limit Results**

   Request only the results you need:

   .. code-block:: python

      from barangay import search

      # Slower (returns more results)
      results = search("San Jose", n=20)

      # Faster (returns fewer results)
      results = search("San Jose", n=3)

4. **Reuse FuzzBase**

   Create FuzzBase once and reuse for multiple searches:

   .. code-block:: python

      from barangay import search, create_fuzz_base

      # Slow (creates FuzzBase for each search)
      for address in addresses:
          results = search(address)

      # Fast (creates FuzzBase once)
      fuzz_base = create_fuzz_base()
      for address in addresses:
          results = search(address, fuzz_base=fuzz_base)

   .. tip:: Reusing FuzzBase can provide 5-10x speedup for batch operations.

5. **Use Appropriate Data Type**

   Choose the right data model for your use case:

   .. code-block:: python

      from barangay import BARANGAY, BARANGAY_FLAT

      # For simple lookups (fast)
      city = BARANGAY["National Capital Region (NCR)"]["City of Manila"]

      # For search/filtering (fast with indexing)
      from barangay import BARANGAY_FLAT
      brgys = [b for b in BARANGAY_FLAT if b['name'] == "Tongmageng"]

Batch Processing Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For processing multiple addresses, use these patterns:

.. code-block:: python

   from barangay import search, create_fuzz_base
   from concurrent.futures import ThreadPoolExecutor
   import time

   # Optimize batch search
   def batch_search_optimized(addresses, threshold=70.0, n=5, workers=4):
       """Optimized batch search with FuzzBase reuse and parallel processing."""

       # Create FuzzBase once (expensive)
       fuzz_base = create_fuzz_base()

       def search_single(address):
           return search(
               address,
               fuzz_base=fuzz_base,
               threshold=threshold,
               n=n
           )

       # Use parallel processing
       with ThreadPoolExecutor(max_workers=workers) as executor:
           results = list(executor.map(search_single, addresses))

       return results

   # Example usage
   addresses = [
       "Tongmageng, Tawi-Tawi",
       "San Jose, City of Manila",
       "Quezon City",
       "Makati",
   ]

   start = time.time()
   results = batch_search_optimized(addresses)
   elapsed = time.time() - start

   print(f"Processed {len(addresses)} addresses in {elapsed:.2f} seconds")
   print(f"Average: {elapsed/len(addresses)*1000:.1f}ms per address")

High Memory Usage
-----------------

Understanding Memory Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~

Memory is primarily used by:

* **Data structures**: Loaded datasets (basic, extended, flat)
* **FuzzBase**: Pre-computed fuzzy matching functions
* **Search results**: Returned result lists
* **Cache**: Downloaded historical data

Typical memory usage:

.. list-table:: Memory Usage
   :widths: 40 30 30
   :header-rows: 1

   * - Component
     - Memory
     - Notes
   * - BARANGAY (basic)
     - ~50 MB
     - Nested dictionary
   * - BARANGAY_EXTENDED
     - ~200 MB
     - Recursive with metadata
   * - BARANGAY_FLAT
     - ~100 MB
     - Flat list
   * - FuzzBase
     - ~300 MB
     - Pre-computed functions
   * - Total (all loaded)
     - ~650 MB
     - All components

.. warning:: Loading all data types simultaneously can use significant memory.

Optimization Strategies
~~~~~~~~~~~~~~~~~~~~~~~

1. **Load Only Needed Data**

   Load only the data type you need:

   .. code-block:: python

      from barangay import load_barangay_data, load_barangay_flat_data

      # Load only what you need
      flat_data = load_barangay_flat_data()

      # Don't load multiple types unless necessary
      # basic_data = load_barangay_data()  # Avoid if not needed
      # extended_data = load_barangay_extended_data()  # Avoid if not needed

2. **Use Generators for Large Datasets**

   Process data in chunks instead of loading everything:

   .. code-block:: python

      from barangay import BARANGAY_FLAT

      # Bad: Load all into memory
      all_brgys = [b for b in BARANGAY_FLAT if b['province_or_huc'] == "NCR"]

      # Good: Use generator for memory efficiency
      def get_brgys_by_province(province):
          for brgy in BARANGAY_FLAT:
              if brgy['province_or_huc'] == province:
                  yield brgy

      # Process one at a time
      for brgy in get_brgys_by_province("NCR"):
          process(brgy)

3. **Clear Unused Objects**

   Explicitly clear objects when done:

   .. code-block:: python

      from barangay import search, create_fuzz_base

      # Use FuzzBase
      fuzz_base = create_fuzz_base()
      results = search("San Jose", fuzz_base=fuzz_base)

      # Clear when done
      del fuzz_base

      # Force garbage collection
      import gc
      gc.collect()

4. **Process Results in Batches**

   Don't keep all results in memory:

   .. code-block:: python

      from barangay import search

      # Bad: Keep all results
      all_results = []
      for address in addresses:
          results = search(address)
          all_results.extend(results)  # Can use lots of memory

      # Good: Process and discard
      for address in addresses:
          results = search(address)
          for result in results:
              process(result)  # Process immediately
          # results discarded after each iteration

5. **Use Efficient Data Structures**

   Choose appropriate data structures:

   .. code-block:: python

      from barangay import BARANGAY_FLAT

      # Bad: List for frequent lookups (O(n))
      def find_brgy_by_psgc(psgc_id):
          for brgy in BARANGAY_FLAT:
              if brgy['psgc_id'] == psgc_id:
                  return brgy
          return None

      # Good: Dictionary for lookups (O(1))
      brgy_dict = {b['psgc_id']: b for b in BARANGAY_FLAT}
      def find_brgy_by_psgc(psgc_id):
          return brgy_dict.get(psgc_id)

6. **Limit Cache Size**

   Configure cache to prevent unlimited growth:

   .. code-block:: python

      from barangay.data_manager import DataManager

      # Use default cache (reasonable size)
      dm = DataManager()

      # Or disable cache if memory is constrained
      dm = DataManager(cache_enabled=False)

   .. warning:: Disabling cache will cause data to be re-downloaded on each load.

Monitoring Memory Usage
~~~~~~~~~~~~~~~~~~~~~~~

Use these tools to monitor memory:

.. code-block:: python

   import psutil
   import os

   def get_memory_usage():
       """Get current process memory usage."""
       process = psutil.Process(os.getpid())
       return process.memory_info().rss / 1024 / 1024  # MB

   # Monitor before and after
   print(f"Memory before: {get_memory_usage():.1f} MB")

   from barangay import create_fuzz_base
   fuzz_base = create_fuzz_base()

   print(f"Memory after: {get_memory_usage():.1f} MB")
   print(f"Memory used: {get_memory_usage() - get_memory_usage():.1f} MB")

Slow Data Loading
-----------------

Understanding Data Loading
~~~~~~~~~~~~~~~~~~~~~~~~~~

Data loading time depends on:

* **Data type**: Extended data takes longer to load
* **Source**: Bundled data (fast) vs downloaded (slow)
* **Cache**: Cached data (fast) vs first download (slow)
* **Format**: JSON vs YAML (similar performance)

Typical load times:

.. list-table:: Data Loading Times
   :widths: 30 35 35
   :header-rows: 1

   * - Data Type
     - First Load
     - Cached Load
   * - BARANGAY (basic)
     - ~100-200ms
     - ~50-100ms
   * - BARANGAY_EXTENDED
     - ~300-500ms
     - ~150-250ms
   * - BARANGAY_FLAT
     - ~200-300ms
     - ~100-150ms

.. note:: First load times include parsing. Cached loads are faster.

Optimization Strategies
~~~~~~~~~~~~~~~~~~~~~~~

1. **Use Cached Data**

   Data is automatically cached after first load:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()

      # First load (slower, downloads if needed)
      data = dm.get_data(data_type="basic")

      # Subsequent loads (faster, uses cache)
      data = dm.get_data(data_type="basic")

2. **Load Only Needed Data Types**

   Don't load all data types:

   .. code-block:: python

      from barangay import load_barangay_data

      # Load only what you need
      basic_data = load_barangay_data()

      # Don't load extended unless needed
      # extended_data = load_barangay_extended_data()

3. **Use Bundled Data**

   Bundled data loads faster than downloaded data:

   .. code-block:: python

      from barangay import search

      # Fast (uses bundled data)
      results = search("Tongmageng")

      # Slower (downloads if not cached)
      results = search("Tongmageng", as_of="2025-07-08")

4. **Pre-load Data**

   Load data during application startup:

   .. code-block:: python

      from barangay import create_fuzz_base, search

      # Load during startup
      fuzz_base = create_fuzz_base()

      # Fast searches later
      def handle_request(address):
          return search(address, fuzz_base=fuzz_base)

5. **Use Appropriate Format**

   JSON and YAML have similar performance. Choose based on preference:

   .. code-block:: python

      from barangay import load_barangay_data

      # JSON (slightly faster)
      import json
      with open('barangay/data/barangay.json', 'r') as f:
          data = json.load(f)

      # YAML (slightly slower but more readable)
      import yaml
      with open('barangay/data/barangay.yaml', 'r') as f:
          data = yaml.safe_load(f)

Cache Miss Issues
-----------------

Understanding Cache
~~~~~~~~~~~~~~~~~~~

The package caches downloaded data to avoid repeated downloads. Cache behavior:

* **Location**: ``~/.cache/barangay`` (Linux/macOS) or ``%USERPROFILE%\.cache\barangay`` (Windows)
* **Content**: Downloaded historical data files
* **Expiration**: No automatic expiration
* **Size**: ~10-50 MB per cached dataset

Identifying Cache Misses
~~~~~~~~~~~~~~~~~~~~~~~~

Cache misses occur when:

* Data is requested for the first time
* Cache was cleared
* Cache directory doesn't exist
* Data is corrupted

Detect cache misses:

.. code-block:: python

   import logging

   # Enable verbose logging
   import os
   os.environ['BARANGAY_VERBOSE'] = '1'
   logging.basicConfig(level=logging.INFO)

   from barangay.data_manager import DataManager

   dm = DataManager()

   # Cache miss (will download)
   print("Loading data (cache miss):")
   data = dm.get_data(as_of="2025-07-08")

   # Cache hit (uses cache)
   print("\nLoading data (cache hit):")
   data = dm.get_data(as_of="2025-07-08")

Optimization Strategies
~~~~~~~~~~~~~~~~~~~~~~~

1. **Pre-warm Cache**

   Load all needed data during application startup:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()

      # Pre-warm cache with all needed dates
      dates = ["2025-07-08", "2025-08-29", "2025-10-13"]

      for date in dates:
          print(f"Pre-warming cache for {date}...")
          data = dm.get_data(as_of=date, data_type="basic")

      print("Cache pre-warmed. Subsequent loads will be fast.")

2. **Check Cache Before Loading**

   Verify data is cached before loading:

   .. code-block:: python

      from barangay.data_manager import DataManager

      dm = DataManager()

      # Check if data is cached
      if dm.is_cached(as_of="2025-07-08"):
          print("Data is cached, loading will be fast")
      else:
          print("Data not cached, first load will download")

      data = dm.get_data(as_of="2025-07-08")

3. **Use Persistent Cache**

   Cache persists across application runs by default:

   .. code-block:: python

      from barangay.data_manager import DataManager

      # Cache is persistent by default
      dm = DataManager()

      # First run (downloads and caches)
      data = dm.get_data(as_of="2025-07-08")

      # Second run (uses cache)
      data = dm.get_data(as_of="2025-07-08")

4. **Configure Cache Directory**

   Use a fast disk for cache:

   .. code-block:: python

      from barangay.data_manager import DataManager
      import os

      # Use SSD or fast disk for cache
      cache_dir = "/fast/ssd/cache/barangay"
      os.makedirs(cache_dir, exist_ok=True)

      dm = DataManager(cache_dir=cache_dir)
      data = dm.get_data(as_of="2025-07-08")

5. **Monitor Cache Performance**

   Measure cache hit rate:

   .. code-block:: python

      from barangay.data_manager import DataManager
      import time

      class CacheMonitor:
          def __init__(self):
              self.hits = 0
              self.misses = 0

          def load_with_monitor(self, dm, as_of, data_type="basic"):
              start = time.time()
              was_cached = dm.is_cached(as_of=as_of)

              data = dm.get_data(as_of=as_of, data_type=data_type)

              elapsed = time.time() - start

              if was_cached:
                  self.hits += 1
                  cache_status = "HIT"
              else:
                  self.misses += 1
                  cache_status = "MISS"

              print(f"{cache_status}: {elapsed*1000:.1f}ms")
              return data

      # Usage
      dm = DataManager()
      monitor = CacheMonitor()

      # First load (miss)
      monitor.load_with_monitor(dm, "2025-07-08")

      # Second load (hit)
      monitor.load_with_monitor(dm, "2025-07-08")

      # Statistics
      total = monitor.hits + monitor.misses
      hit_rate = (monitor.hits / total * 100) if total > 0 else 0
      print(f"Cache hit rate: {hit_rate:.1f}%")

Optimization Tips
-----------------

General Best Practices
~~~~~~~~~~~~~~~~~~~~~~

1. **Profile Before Optimizing**

   Measure before making changes:

   .. code-block:: python

      import time
      from barangay import search

      # Profile search
      start = time.time()
      results = search("San Jose")
      elapsed = time.time() - start

      print(f"Search took {elapsed*1000:.1f}ms")

2. **Use Appropriate Abstractions**

   Choose the right tool for the job:

   .. code-block:: python

      from barangay import search, BARANGAY, BARANGAY_FLAT

      # For fuzzy search
      results = search("San Jose")

      # For exact lookups (faster)
      city = BARANGAY["National Capital Region (NCR)"]["City of Manila"]

      # For filtering (fast with dict)
      brgy_dict = {b['psgc_id']: b for b in BARANGAY_FLAT}
      brgy = brgy_dict.get("010010001")

3. **Batch Operations**

   Process multiple items together:

   .. code-block:: python

      from barangay import search, create_fuzz_base

      # Bad: Create FuzzBase for each search
      for address in addresses:
          results = search(address)

      # Good: Create FuzzBase once
      fuzz_base = create_fuzz_base()
      for address in addresses:
          results = search(address, fuzz_base=fuzz_base)

4. **Use Parallel Processing**

   For CPU-bound tasks, use parallel processing:

   .. code-block:: python

      from barangay import search, create_fuzz_base
      from concurrent.futures import ThreadPoolExecutor

      fuzz_base = create_fuzz_base()

      def search_address(address):
          return search(address, fuzz_base=fuzz_base)

      with ThreadPoolExecutor(max_workers=4) as executor:
          results = list(executor.map(search_address, addresses))

5. **Lazy Loading**

   Load data only when needed:

   .. code-block:: python

      from barangay import load_barangay_data

      # Bad: Load all data upfront
      data = load_barangay_data()
      # ... use data later

      # Good: Load only when needed
      def get_data():
          if not hasattr(get_data, '_cached'):
              get_data._cached = load_barangay_data()
          return get_data._cached

      # ... use data when needed
      data = get_data()

Performance Patterns
~~~~~~~~~~~~~~~~~~~~

Pattern 1: Single Search
^^^^^^^^^^^^^^^^^^^^^^^^

For one-off searches, use default settings:

.. code-block:: python

   from barangay import search

   results = search("Tongmageng, Tawi-Tawi")

Pattern 2: Batch Search
^^^^^^^^^^^^^^^^^^^^^^^

For multiple searches, reuse FuzzBase:

.. code-block:: python

   from barangay import search, create_fuzz_base

   fuzz_base = create_fuzz_base()
   results = [search(addr, fuzz_base=fuzz_base) for addr in addresses]

Pattern 3: High-Throughput Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For maximum throughput, use parallel processing:

.. code-block:: python

   from barangay import search, create_fuzz_base
   from concurrent.futures import ThreadPoolExecutor

   fuzz_base = create_fuzz_base()

   def search_batch(addresses, workers=4):
       def search_single(addr):
           return search(addr, fuzz_base=fuzz_base)

       with ThreadPoolExecutor(max_workers=workers) as executor:
           return list(executor.map(search_single, addresses))

   results = search_batch(addresses, workers=4)

Pattern 4: Memory-Constrained Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For memory-constrained environments, process in chunks:

.. code-block:: python

   from barangay import search, create_fuzz_base

   fuzz_base = create_fuzz_base()

   def search_in_chunks(addresses, chunk_size=100):
       results = []
       for i in range(0, len(addresses), chunk_size):
           chunk = addresses[i:i + chunk_size]
           chunk_results = [search(addr, fuzz_base=fuzz_base) for addr in chunk]
           results.extend(chunk_results)
           # Process or save results
           save_results(chunk_results)
       return results

Benchmarking Guidance
---------------------

Setting Up Benchmarks
~~~~~~~~~~~~~~~~~~~~~

Create reproducible benchmarks:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   def benchmark_search(addresses, **kwargs):
       """Benchmark search performance."""

       # Warm-up
       for addr in addresses[:5]:
           search(addr, **kwargs)

       # Benchmark
       times = []
       for addr in addresses:
           start = time.time()
           results = search(addr, **kwargs)
           elapsed = time.time() - start
           times.append(elapsed)

       # Statistics
       avg_time = sum(times) / len(times)
       min_time = min(times)
       max_time = max(times)
       median_time = sorted(times)[len(times) // 2]

       return {
           'avg': avg_time * 1000,  # ms
           'min': min_time * 1000,
           'max': max_time * 1000,
           'median': median_time * 1000,
           'total': sum(times),
           'count': len(times)
       }

   # Usage
   test_addresses = ["San Jose", "Quezon City", "Manila"] * 10

   # Benchmark default settings
   results = benchmark_search(test_addresses)
   print(f"Average: {results['avg']:.1f}ms")

   # Benchmark with FuzzBase
   fuzz_base = create_fuzz_base()
   results = benchmark_search(test_addresses, fuzz_base=fuzz_base)
   print(f"With FuzzBase: {results['avg']:.1f}ms")

Comparing Configurations
~~~~~~~~~~~~~~~~~~~~~~~~

Compare different configurations:

.. code-block:: python

   from barangay import search, create_fuzz_base

   test_addresses = ["San Jose", "Quezon City", "Manila"] * 10

   configurations = [
       {"name": "Default", "kwargs": {}},
       {"name": "High threshold", "kwargs": {"threshold": 80.0}},
       {"name": "Fewer hooks", "kwargs": {"match_hooks": ["barangay"]}},
       {"name": "With FuzzBase", "kwargs": {"fuzz_base": create_fuzz_base()}},
   ]

   for config in configurations:
       results = benchmark_search(test_addresses, **config["kwargs"])
       print(f"{config['name']}: {results['avg']:.1f}ms avg")

Profiling Tools
~~~~~~~~~~~~~~~

Use Python's profiling tools:

.. code-block:: python

   import cProfile
   import pstats
   from io import StringIO
   from barangay import search

   # Profile search
   pr = cProfile.Profile()
   pr.enable()

   for _ in range(100):
       search("San Jose")

   pr.disable()

   # Print statistics
   s = StringIO()
   ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
   ps.print_stats(20)
   print(s.getvalue())

Memory Profiling
~~~~~~~~~~~~~~~~

Profile memory usage:

.. code-block:: python

   from memory_profiler import profile
   from barangay import create_fuzz_base

   @profile
   def test_memory():
       fuzz_base = create_fuzz_base()
       return fuzz_base

   if __name__ == '__main__':
       test_memory()

.. note:: Install memory_profiler with ``pip install memory-profiler``.

See Also
--------

* :doc:`common_errors` - Common errors and solutions
* :doc:`faq` - Frequently asked questions
* :doc:`../user_guide/performance` - Performance optimization guide
* :doc:`../advanced/caching` - Caching mechanisms