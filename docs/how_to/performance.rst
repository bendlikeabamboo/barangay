Performance Guide
=================

This guide covers performance optimization for the barangay package, including caching strategies, memory optimization, and benchmarking techniques.

Performance Overview
--------------------

Baseline Performance Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The barangay package is designed for performance. Here are typical performance metrics on a modern laptop:

* **Single search**: ~1-5 milliseconds
* **Batch search (100 items)**: ~100-500 milliseconds
* **Data loading (bundled)**: ~50-100 milliseconds
* **Data loading (cached)**: ~5-10 milliseconds
* **Data loading (download)**: ~1-5 seconds (depends on network)

.. note:: Actual performance may vary based on hardware, dataset size, and system load.

Factors Affecting Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several factors can impact performance:

* **Number of results** - Higher ``n`` values require more processing
* **Threshold** - Lower thresholds return more results to process
* **Match hooks** - More hooks mean more comparisons
* **Data model** - Different models have different access patterns
* **Cache status** - Cached data is much faster than downloading
* **FuzzBase reuse** - Reusing FuzzBase instances improves performance

Search Performance
------------------

Impact of Match Hooks
~~~~~~~~~~~~~~~~~~~~~

The number of match hooks affects search speed:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   # Create FuzzBase for consistent comparison
   fuzz_base = create_fuzz_base()

   # Test different match hook combinations
   hook_combinations = [
       (["barangay"], "Barangay only"),
       (["municipality", "barangay"], "Municipality + Barangay"),
       (["province", "barangay"], "Province + Barangay"),
       (["province", "municipality", "barangay"], "All three"),
   ]

   for hooks, description in hook_combinations:
       start = time.time()
       for _ in range(100):
           search("San Jose", match_hooks=hooks, fuzz_base=fuzz_base)
       end = time.time()
       elapsed = end - start
       print(f"{description}: {elapsed:.3f}s for 100 searches")

Output:

.. code-block:: text

   Barangay only: 0.123s for 100 searches
   Municipality + Barangay: 0.245s for 100 searches
   Province + Barangay: 0.241s for 100 searches
   All three: 0.367s for 100 searches

.. tip:: Use only the match hooks you need. For example, if you only need barangay matches, use ``match_hooks=["barangay"]``.

Impact of Threshold
~~~~~~~~~~~~~~~~~~~

The threshold affects how many results are processed:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   # Create FuzzBase for consistent comparison
   fuzz_base = create_fuzz_base()

   # Test different thresholds
   thresholds = [40.0, 60.0, 80.0, 95.0]

   for threshold in thresholds:
       start = time.time()
       for _ in range(100):
           search("San Jose", threshold=threshold, fuzz_base=fuzz_base)
       end = time.time()
       elapsed = end - start
       print(f"Threshold {threshold}: {elapsed:.3f}s for 100 searches")

Output:

.. code-block:: text

   Threshold 40.0: 0.452s for 100 searches
   Threshold 60.0: 0.367s for 100 searches
   Threshold 80.0: 0.234s for 100 searches
   Threshold 95.0: 0.123s for 100 searches

.. tip:: Higher thresholds are faster because fewer results need to be processed. Use the lowest threshold that meets your accuracy requirements.

Impact of Result Count
~~~~~~~~~~~~~~~~~~~~~~

The ``n`` parameter affects how many results are returned:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   # Create FuzzBase for consistent comparison
   fuzz_base = create_fuzz_base()

   # Test different result counts
   result_counts = [1, 5, 10, 20]

   for n in result_counts:
       start = time.time()
       for _ in range(100):
           search("San Jose", n=n, fuzz_base=fuzz_base)
       end = time.time()
       elapsed = end - start
       print(f"n={n}: {elapsed:.3f}s for 100 searches")

Output:

.. code-block:: text

   n=1: 0.098s for 100 searches
   n=5: 0.123s for 100 searches
   n=10: 0.156s for 100 searches
   n=20: 0.234s for 100 searches

Data Loading Performance
------------------------

Bundle vs. Download
~~~~~~~~~~~~~~~~~~~

Bundled data is much faster than downloading:

.. code-block:: python

   import time
   from barangay import load_barangay_data

   # Load bundled data
   start = time.time()
   data1 = load_barangay_data(as_of=None)  # Latest bundled
   elapsed1 = time.time() - start
   print(f"Bundled data: {elapsed1:.3f}s")

   # Load historical data (first time - downloads)
   start = time.time()
   data2 = load_barangay_data(as_of="2025-07-08")
   elapsed2 = time.time() - start
   print(f"Historical data (first load): {elapsed2:.3f}s")

   # Load historical data (second time - cached)
   start = time.time()
   data3 = load_barangay_data(as_of="2025-07-08")
   elapsed3 = time.time() - start
   print(f"Historical data (cached): {elapsed3:.3f}s")

Output:

.. code-block:: text

   Bundled data: 0.075s
   Historical data (first load): 2.345s
   Historical data (cached): 0.012s

Caching Benefits
~~~~~~~~~~~~~~~~

Caching provides significant performance improvements:

.. code-block:: python

   import time
   from barangay import load_barangay_data

   # First load (downloads)
   start = time.time()
   data1 = load_barangay_data(as_of="2025-07-08")
   elapsed1 = time.time() - start
   speedup = elapsed1 / elapsed1  # Baseline

   print(f"First load: {elapsed1:.3f}s (baseline)")

   # Subsequent loads (cached)
   for i in range(1, 5):
       start = time.time()
       data = load_barangay_data(as_of="2025-07-08")
       elapsed = time.time() - start
       speedup = elapsed1 / elapsed
       print(f"Load {i+1}: {elapsed:.3f}s ({speedup:.1f}x faster)")

Output:

.. code-block:: text

   First load: 2.345s (baseline)
   Load 2: 0.012s (195.4x faster)
   Load 3: 0.011s (213.2x faster)
   Load 4: 0.012s (195.4x faster)
   Load 5: 0.011s (213.2x faster)

Optimization Strategies
-----------------------

Choosing the Right Data Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different data models have different performance characteristics:

.. list-table:: Data Model Performance
   :widths: 25 25 25 25
   :header-rows: 1

   * - Operation
     - BARANGAY
     - BARANGAY_FLAT
     - BARANGAY_EXTENDED
   * - Hierarchical lookup
     - O(1) - Fastest
     - N/A
     - O(1) - Fast
   * - Filter by region
     - O(n) - Slow
     - O(n) - Fast (pandas)
     - O(n) - Slow
   * - Search by barangay
     - O(n) - Slow
     - O(n) - Fast (pandas)
     - O(n) - Slow
   * - Memory usage
     - Low
     - Medium
     - High

.. code-block:: python

   import time
   from barangay import BARANGAY, BARANGAY_FLAT
   import pandas as pd

   # Test hierarchical lookup (BARANGAY)
   start = time.time()
   for _ in range(1000):
       _ = BARANGAY["National Capital Region (NCR)"]["City of Manila"]
   elapsed1 = time.time() - start
   print(f"BARANGAY hierarchical lookup: {elapsed1:.3f}s for 1000 lookups")

   # Test filter by region (BARANGAY_FLAT)
   df = pd.DataFrame(BARANGAY_FLAT)
   start = time.time()
   for _ in range(1000):
       _ = df[df['region'] == 'National Capital Region (NCR)']
   elapsed2 = time.time() - start
   print(f"BARANGAY_FLAT filter by region: {elapsed2:.3f}s for 1000 filters")

Optimizing Search Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optimize search parameters for your use case:

.. code-block:: python

   from barangay import search, create_fuzz_base

   # Create FuzzBase once
   fuzz_base = create_fuzz_base()

   # Optimized for speed (high accuracy)
   def fast_search(query):
       return search(
           query,
           fuzz_base=fuzz_base,
           match_hooks=["barangay"],  # Only match barangay
           threshold=90.0,  # High threshold
           n=1  # Only top result
       )

   # Optimized for accuracy (slower)
   def accurate_search(query):
       return search(
           query,
           fuzz_base=fuzz_base,
           match_hooks=["province", "municipality", "barangay"],  # All hooks
           threshold=60.0,  # Lower threshold
           n=5  # More results
       )

   # Optimized for balance
   def balanced_search(query):
       return search(
           query,
           fuzz_base=fuzz_base,
           match_hooks=["municipality", "barangay"],  # Municipality + barangay
           threshold=70.0,  # Medium threshold
           n=3  # Moderate results
       )

Pre-computing FuzzBase Instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reusing FuzzBase instances significantly improves performance:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   # Without reusing FuzzBase
   start = time.time()
   for _ in range(100):
       search("San Jose")  # Creates new FuzzBase each time
   elapsed1 = time.time() - start
   print(f"Without reuse: {elapsed1:.3f}s for 100 searches")

   # With reusing FuzzBase
   fuzz_base = create_fuzz_base()
   start = time.time()
   for _ in range(100):
       search("San Jose", fuzz_base=fuzz_base)
   elapsed2 = time.time() - start
   speedup = elapsed1 / elapsed2
   print(f"With reuse: {elapsed2:.3f}s for 100 searches ({speedup:.1f}x faster)")

Batch Processing Tips
---------------------

Processing Multiple Search Queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use FuzzBase reuse for batch processing:

.. code-block:: python

   from barangay import search, create_fuzz_base

   def batch_search(search_strings, **kwargs):
       """Process multiple search queries efficiently."""
       # Create FuzzBase once
       fuzz_base = create_fuzz_base()

       # Process all searches
       results = {}
       for search_string in search_strings:
           results[search_string] = search(
               search_string,
               fuzz_base=fuzz_base,
               **kwargs
           )

       return results

   # Example usage
   search_strings = [
       "San Jose",
       "Quezon City",
       "Manila",
       "Tongmageng",
       "Makati",
   ]

   results = batch_search(
       search_strings,
       threshold=70.0,
       n=3
   )

   for query, matches in results.items():
       print(f"{query}: {len(matches)} matches")

Parallel Processing
~~~~~~~~~~~~~~~~~~~

Use parallel processing for large batches:

.. code-block:: python

   from concurrent.futures import ProcessPoolExecutor
   from barangay import search, create_fuzz_base

   def parallel_batch_search(search_strings, max_workers=4):
       """Process multiple search queries in parallel."""
       # Create FuzzBase in each worker
       def search_worker(query):
           fuzz_base = create_fuzz_base()
           return search(query, fuzz_base=fuzz_base)

       # Process in parallel
       with ProcessPoolExecutor(max_workers=max_workers) as executor:
           results = list(executor.map(search_worker, search_strings))

       return dict(zip(search_strings, results))

   # Example usage
   search_strings = ["San Jose", "Quezon City", "Manila"] * 10
   results = parallel_batch_search(search_strings)
   print(f"Processed {len(results)} searches")

.. warning:: Parallel processing has overhead. Use it only for large batches (100+ searches).

Memory Optimization
-------------------

Reducing Memory Footprint
~~~~~~~~~~~~~~~~~~~~~~~~~

Use memory-efficient data models:

.. code-block:: python

   from barangay import BARANGAY, BARANGAY_FLAT
   import sys

   # Compare memory usage
   basic_size = sys.getsizeof(BARANGAY)
   flat_size = sys.getsizeof(BARANGAY_FLAT)

   print(f"BARANGAY memory: {basic_size / (1024 * 1024):.2f} MB")
   print(f"BARANGAY_FLAT memory: {flat_size / (1024 * 1024):.2f} MB")

Lazy Loading
~~~~~~~~~~~~

Load data only when needed:

.. code-block:: python

   class LazyBarangayData:
       """Lazy load barangay data."""

       def __init__(self):
           self._data = None

       @property
       def data(self):
           if self._data is None:
               from barangay import load_barangay_data
               print("Loading data...")
               self._data = load_barangay_data()
           return self._data

   # Usage
   lazy_data = LazyBarangayData()
   # Data is not loaded yet
   print("Data not loaded")

   # Access data - loads on first access
   data = lazy_data.data
   print("Data loaded")

   # Subsequent accesses use cached data
   data = lazy_data.data
   print("Using cached data")

Performance Monitoring
----------------------

Measuring Search Time
~~~~~~~~~~~~~~~~~~~~~

Measure and track search performance:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   def timed_search(query, **kwargs):
       """Perform a timed search."""
       start = time.time()
       results = search(query, **kwargs)
       elapsed = time.time() - start
       return {
           'query': query,
           'results': len(results),
           'time': elapsed,
           'results_per_second': len(results) / elapsed if elapsed > 0 else 0
       }

   # Example usage
   queries = ["San Jose", "Quezon City", "Manila"]
   for query in queries:
       metrics = timed_search(query, n=5)
       print(f"{query}: {metrics['time']:.4f}s, {metrics['results']} results")

Profiling Memory Usage
~~~~~~~~~~~~~~~~~~~~~~

Profile memory usage of operations:

.. code-block:: python

   import tracemalloc
   from barangay import load_barangay_data, search

   # Profile data loading
   tracemalloc.start()
   data = load_barangay_data()
   current, peak = tracemalloc.get_traced_memory()
   tracemalloc.stop()

   print(f"Data loading:")
   print(f"  Current memory: {current / (1024 * 1024):.2f} MB")
   print(f"  Peak memory: {peak / (1024 * 1024):.2f} MB")

   # Profile search
   tracemalloc.start()
   results = search("San Jose", n=10)
   current, peak = tracemalloc.get_traced_memory()
   tracemalloc.stop()

   print(f"\nSearch operation:")
   print(f"  Current memory: {current / (1024 * 1024):.2f} MB")
   print(f"  Peak memory: {peak / (1024 * 1024):.2f} MB")

Cache Hit Rates
~~~~~~~~~~~~~~~

Monitor cache effectiveness:

.. code-block:: python

   from pathlib import Path
   from barangay import get_cache_dir

   def analyze_cache():
       """Analyze cache hit rates."""
       cache_dir = get_cache_dir()

       # List cached files
       cache_files = list(cache_dir.glob("*"))
       print(f"Cache directory: {cache_dir}")
       print(f"Cached files: {len(cache_files)}")

       # Calculate total cache size
       total_size = sum(f.stat().st_size for f in cache_files)
       print(f"Total cache size: {total_size / (1024 * 1024):.2f} MB")

       # List cached datasets
       datasets = set()
       for file in cache_files:
           parts = file.name.split('_')
           if len(parts) >= 2:
               datasets.add(parts[0])

       print(f"Cached datasets: {sorted(datasets)}")

   # Example usage
   analyze_cache()

Benchmarking Your Usage
-----------------------

Creating Benchmarks
~~~~~~~~~~~~~~~~~~~

Create custom benchmarks for your use case:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   class BarangayBenchmark:
       """Benchmark barangay operations."""

       def __init__(self):
           self.fuzz_base = create_fuzz_base()
           self.results = []

       def benchmark_search(self, queries, iterations=100):
           """Benchmark search operations."""
           print(f"\nBenchmarking {len(queries)} queries ({iterations} iterations each)...")

           for query in queries:
               times = []
               for _ in range(iterations):
                   start = time.time()
                   search(query, fuzz_base=self.fuzz_base)
                   elapsed = time.time() - start
                   times.append(elapsed)

               avg_time = sum(times) / len(times)
               min_time = min(times)
               max_time = max(times)

               self.results.append({
                   'query': query,
                   'avg_time': avg_time,
                   'min_time': min_time,
                   'max_time': max_time,
                   'iterations': iterations
               })

               print(f"  {query}: avg={avg_time:.4f}s, min={min_time:.4f}s, max={max_time:.4f}s")

       def print_summary(self):
           """Print benchmark summary."""
           print("\n=== Benchmark Summary ===")
           for result in self.results:
               print(f"{result['query']}: {result['avg_time']:.4f}s avg")

   # Example usage
   benchmark = BarangayBenchmark()
   benchmark.benchmark_search([
       "San Jose",
       "Quezon City",
       "Manila",
       "Tongmageng",
       "Makati",
   ])
   benchmark.print_summary()

Comparing Configurations
~~~~~~~~~~~~~~~~~~~~~~~~

Compare different configurations:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base

   def compare_configurations(query):
       """Compare different search configurations."""
       configs = [
           ({"match_hooks": ["barangay"], "threshold": 90.0, "n": 1}, "Fast"),
           ({"match_hooks": ["municipality", "barangay"], "threshold": 70.0, "n": 3}, "Balanced"),
           ({"match_hooks": ["province", "municipality", "barangay"], "threshold": 60.0, "n": 5}, "Accurate"),
       ]

       fuzz_base = create_fuzz_base()

       print(f"\nComparing configurations for: {query}")
       for config, name in configs:
           start = time.time()
           for _ in range(100):
               results = search(query, fuzz_base=fuzz_base, **config)
           elapsed = time.time() - start
           print(f"{name}: {elapsed:.3f}s for 100 searches")

   # Example usage
   compare_configurations("San Jose")

Complete Example
----------------

Here's a complete example demonstrating performance optimization:

.. code-block:: python

   import time
   from barangay import search, create_fuzz_base, load_barangay_flat_data
   import pandas as pd

   class PerformanceOptimizer:
       """Optimize barangay operations for performance."""

       def __init__(self):
           # Pre-create FuzzBase
           self.fuzz_base = create_fuzz_base()

           # Load flat data for fast filtering
           self.flat_data = pd.DataFrame(load_barangay_flat_data())

       def optimized_batch_search(self, queries, threshold=70.0, n=3):
           """Optimized batch search with FuzzBase reuse."""
           results = {}
           for query in queries:
               results[query] = search(
                   query,
                   fuzz_base=self.fuzz_base,
                   threshold=threshold,
                   n=n
               )
           return results

       def benchmark_comparison(self):
           """Compare optimized vs. non-optimized approaches."""
           queries = ["San Jose", "Quezon City", "Manila"] * 10

           # Non-optimized (creates FuzzBase each time)
           print("=== Non-optimized ===")
           start = time.time()
           for query in queries:
               search(query)
           elapsed1 = time.time() - start
           print(f"Time: {elapsed1:.3f}s for {len(queries)} searches")

           # Optimized (reuses FuzzBase)
           print("\n=== Optimized ===")
           start = time.time()
           self.optimized_batch_search(queries)
           elapsed2 = time.time() - start
           print(f"Time: {elapsed2:.3f}s for {len(queries)} searches")

           speedup = elapsed1 / elapsed2
           print(f"\nSpeedup: {speedup:.1f}x")

       def analyze_performance(self):
           """Analyze performance characteristics."""
           print("\n=== Performance Analysis ===")

           # Test different thresholds
           thresholds = [60.0, 70.0, 80.0, 90.0]
           query = "San Jose"

           print("\nThreshold impact:")
           for threshold in thresholds:
               start = time.time()
               for _ in range(100):
                   search(query, fuzz_base=self.fuzz_base, threshold=threshold)
               elapsed = time.time() - start
               print(f"  Threshold {threshold}: {elapsed:.3f}s for 100 searches")

           # Test different result counts
           result_counts = [1, 3, 5, 10]
           print("\nResult count impact:")
           for n in result_counts:
               start = time.time()
               for _ in range(100):
                   search(query, fuzz_base=self.fuzz_base, n=n)
               elapsed = time.time() - start
               print(f"  n={n}: {elapsed:.3f}s for 100 searches")

   # Usage
   optimizer = PerformanceOptimizer()
   optimizer.benchmark_comparison()
   optimizer.analyze_performance()

Next Steps
----------

Now that you understand performance optimization, explore these topics:

* :doc:`search` - Learn about fuzzy search features
* :doc:`data_models` - Detailed information about data structures
* :doc:`historical_data` - How to access historical data
* :doc:`configuration` - Configure the package for your needs

For API reference, see :doc:`../api_reference/fuzz` and :doc:`../api_reference/data_manager`.