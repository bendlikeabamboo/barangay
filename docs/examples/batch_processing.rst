Batch Processing
================

Use Case
--------
Process large datasets of Philippine addresses efficiently. This is essential for:

* **Data migration**: Migrate address databases between systems
* **Data cleaning**: Clean and standardize large address datasets
* **ETL pipelines**: Extract, transform, load address data
* **Bulk validation**: Validate thousands of addresses at once
* **Data enrichment**: Add barangay information to existing datasets

Basic Batch Processing
----------------------

Processing CSV Files
~~~~~~~~~~~~~~~~~~~~

Read addresses from CSV and validate them in batch:

.. code-block:: python

    import pandas as pd
    from barangay import search, create_fuzz_base

    def batch_validate_csv(
        input_path: str,
        output_path: str,
        address_column: str = 'address',
        threshold: float = 80.0
    ) -> None:
        """Validate addresses from a CSV file.

        Args:
            input_path: Path to input CSV file
            output_path: Path to output CSV file
            address_column: Name of column containing addresses
            threshold: Minimum similarity score for validation
        """
        # Read CSV
        df = pd.read_csv(input_path)

        # Create FuzzBase once for efficiency
        fuzz_base = create_fuzz_base()

        # Validate addresses
        results = []
        for idx, row in df.iterrows():
            address = row[address_column]
            matches = search(address, n=1, threshold=threshold, fuzz_base=fuzz_base)

            if matches and matches[0]['max_score'] >= threshold:
                results.append({
                    **row.to_dict(),
                    'is_valid': True,
                    'barangay': matches[0]['barangay'],
                    'municipality': matches[0]['municipality_or_city'],
                    'province': matches[0]['province_or_huc'],
                    'psgc_id': matches[0]['psgc_id'],
                    'score': matches[0]['max_score']
                })
            else:
                results.append({
                    **row.to_dict(),
                    'is_valid': False,
                    'barangay': None,
                    'municipality': None,
                    'province': None,
                    'psgc_id': None,
                    'score': None
                })

        # Save results
        result_df = pd.DataFrame(results)
        result_df.to_csv(output_path, index=False)

        # Print summary
        valid_count = result_df['is_valid'].sum()
        total_count = len(result_df)
        print(f"Processed {total_count} addresses")
        print(f"Valid: {valid_count} ({valid_count/total_count*100:.1f}%)")
        print(f"Invalid: {total_count - valid_count} ({(total_count-valid_count)/total_count*100:.1f}%)")

    # Example usage
    batch_validate_csv(
        input_path='addresses.csv',
        output_path='validated_addresses.csv',
        address_column='address',
        threshold=80.0
    )

Processing Databases
~~~~~~~~~~~~~~~~~~~~

Validate addresses stored in a database:

.. code-block:: python

    import sqlite3
    import pandas as pd
    from barangay import search, create_fuzz_base

    def batch_validate_database(
        db_path: str,
        table_name: str,
        address_column: str = 'address',
        id_column: str = 'id',
        threshold: float = 80.0,
        batch_size: int = 1000
    ) -> None:
        """Validate addresses from a database table.

        Args:
            db_path: Path to SQLite database
            table_name: Name of table containing addresses
            address_column: Name of column containing addresses
            id_column: Name of primary key column
            threshold: Minimum similarity score for validation
            batch_size: Number of records to process at once
        """
        # Connect to database
        conn = sqlite3.connect(db_path)

        # Create FuzzBase once for efficiency
        fuzz_base = create_fuzz_base()

        # Get total count
        total_count = pd.read_sql(f"SELECT COUNT(*) FROM {table_name}", conn).iloc[0, 0]
        print(f"Total addresses to process: {total_count}")

        # Process in batches
        offset = 0
        processed = 0

        while offset < total_count:
            # Read batch
            query = f"""
                SELECT {id_column}, {address_column}
                FROM {table_name}
                LIMIT {batch_size} OFFSET {offset}
            """
            batch_df = pd.read_sql(query, conn)

            # Validate batch
            results = []
            for idx, row in batch_df.iterrows():
                address = row[address_column]
                matches = search(address, n=1, threshold=threshold, fuzz_base=fuzz_base)

                if matches and matches[0]['max_score'] >= threshold:
                    results.append({
                        id_column: row[id_column],
                        'is_valid': 1,
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    })
                else:
                    results.append({
                        id_column: row[id_column],
                        'is_valid': 0,
                        'barangay': None,
                        'municipality': None,
                        'province': None,
                        'psgc_id': None,
                        'score': None
                    })

            # Update database
            result_df = pd.DataFrame(results)
            result_df.to_sql('validation_results', conn, if_exists='append', index=False)

            processed += len(batch_df)
            print(f"Processed {processed}/{total_count} ({processed/total_count*100:.1f}%)")

            offset += batch_size

        conn.close()
        print("Batch processing complete!")

Processing APIs
~~~~~~~~~~~~~~~

Validate addresses from API responses:

.. code-block:: python

    import requests
    import pandas as pd
    from barangay import search, create_fuzz_base

    def batch_validate_api_addresses(
        api_url: str,
        output_path: str,
        address_field: str = 'address',
        threshold: float = 80.0,
        page_size: int = 100
    ) -> None:
        """Validate addresses from a paginated API.

        Args:
            api_url: Base URL of the API
            output_path: Path to output CSV file
            address_field: Field name containing addresses
            threshold: Minimum similarity score for validation
            page_size: Number of records per page
        """
        # Create FuzzBase once for efficiency
        fuzz_base = create_fuzz_base()

        all_results = []
        page = 1

        while True:
            # Fetch page
            params = {'page': page, 'per_page': page_size}
            response = requests.get(api_url, params=params)

            if response.status_code != 200:
                print(f"Error fetching page {page}: {response.status_code}")
                break

            data = response.json()

            if not data or len(data) == 0:
                break

            # Validate addresses
            for item in data:
                address = item.get(address_field, '')
                matches = search(address, n=1, threshold=threshold, fuzz_base=fuzz_base)

                if matches and matches[0]['max_score'] >= threshold:
                    all_results.append({
                        **item,
                        'is_valid': True,
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    })
                else:
                    all_results.append({
                        **item,
                        'is_valid': False,
                        'barangay': None,
                        'municipality': None,
                        'province': None,
                        'psgc_id': None,
                        'score': None
                    })

            print(f"Processed page {page} ({len(data)} addresses)")
            page += 1

            # Check if there are more pages
            if len(data) < page_size:
                break

        # Save results
        result_df = pd.DataFrame(all_results)
        result_df.to_csv(output_path, index=False)
        print(f"Saved {len(result_df)} results to {output_path}")

Performance Optimization
------------------------

Optimizing for Large Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use efficient data structures and algorithms for large datasets:

.. code-block:: python

    import pandas as pd
    from barangay import search, create_fuzz_base
    from tqdm import tqdm

    def optimized_batch_validate(
        addresses: list[str],
        threshold: float = 80.0,
        show_progress: bool = True
    ) -> pd.DataFrame:
        """Optimized batch validation for large datasets.

        Args:
            addresses: List of address strings to validate
            threshold: Minimum similarity score for validation
            show_progress: Whether to show progress bar

        Returns:
            DataFrame with validation results
        """
        # Create FuzzBase once for efficiency
        fuzz_base = create_fuzz_base()

        # Pre-allocate list for results
        results = []

        # Use iterator for memory efficiency
        iterator = tqdm(addresses, desc="Validating") if show_progress else addresses

        for address in iterator:
            matches = search(address, n=1, threshold=threshold, fuzz_base=fuzz_base)

            if matches and matches[0]['max_score'] >= threshold:
                results.append({
                    'address': address,
                    'is_valid': True,
                    'barangay': matches[0]['barangay'],
                    'municipality': matches[0]['municipality_or_city'],
                    'province': matches[0]['province_or_huc'],
                    'psgc_id': matches[0]['psgc_id'],
                    'score': matches[0]['max_score']
                })
            else:
                results.append({
                    'address': address,
                    'is_valid': False,
                    'barangay': None,
                    'municipality': None,
                    'province': None,
                    'psgc_id': None,
                    'score': None
                })

        return pd.DataFrame(results)

Parallel Processing
~~~~~~~~~~~~~~~~~~~

Use multiprocessing for CPU-bound operations:

.. code-block:: python

    import pandas as pd
    from multiprocessing import Pool, cpu_count
    from barangay import search, create_fuzz_base

    def validate_single_address(args: tuple) -> dict:
        """Validate a single address (for multiprocessing).

        Args:
            args: Tuple of (address, fuzz_base, threshold)

        Returns:
            Dictionary with validation result
        """
        address, fuzz_base, threshold = args

        # Note: fuzz_base can't be pickled, so we recreate it in each process
        from barangay import create_fuzz_base
        fuzz_base = create_fuzz_base()

        matches = search(address, n=1, threshold=threshold, fuzz_base=fuzz_base)

        if matches and matches[0]['max_score'] >= threshold:
            return {
                'address': address,
                'is_valid': True,
                'barangay': matches[0]['barangay'],
                'municipality': matches[0]['municipality_or_city'],
                'province': matches[0]['province_or_huc'],
                'psgc_id': matches[0]['psgc_id'],
                'score': matches[0]['max_score']
            }
        else:
            return {
                'address': address,
                'is_valid': False,
                'barangay': None,
                'municipality': None,
                'province': None,
                'psgc_id': None,
                'score': None
            }

    def parallel_batch_validate(
        addresses: list[str],
        threshold: float = 80.0,
        num_workers: int = None
    ) -> pd.DataFrame:
        """Validate addresses in parallel.

        Args:
            addresses: List of address strings to validate
            threshold: Minimum similarity score for validation
            num_workers: Number of worker processes (default: CPU count)

        Returns:
            DataFrame with validation results
        """
        if num_workers is None:
            num_workers = cpu_count()

        # Prepare arguments for each process
        args_list = [(address, None, threshold) for address in addresses]

        # Process in parallel
        with Pool(processes=num_workers) as pool:
            results = pool.map(validate_single_address, args_list)

        return pd.DataFrame(results)

    # Example usage
    addresses = ["Tongmageng, Tawi-Tawi", "Rosario, Batangas", "San Jose, Manila"]
    df = parallel_batch_validate(addresses, threshold=80.0)
    print(df)

Progress Tracking and Logging
-----------------------------

Detailed Progress Tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~

Track progress with detailed statistics:

.. code-block:: python

    import pandas as pd
    from barangay import search, create_fuzz_base
    from datetime import datetime
    from tqdm import tqdm

    class BatchProcessor:
        """Batch processor with progress tracking and logging."""

        def __init__(
            self,
            threshold: float = 80.0,
            log_file: str = None
        ):
            """Initialize the BatchProcessor.

            Args:
                threshold: Minimum similarity score for validation
                log_file: Optional path to log file
            """
            self.threshold = threshold
            self.fuzz_base = create_fuzz_base()
            self.log_file = log_file
            self.stats = {
                'total': 0,
                'valid': 0,
                'invalid': 0,
                'start_time': None,
                'end_time': None
            }

        def _log(self, message: str) -> None:
            """Log a message to console and file.

            Args:
                message: Message to log
            """
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"[{timestamp}] {message}"
            print(log_message)

            if self.log_file:
                with open(self.log_file, 'a') as f:
                    f.write(log_message + '\n')

        def process(
            self,
            addresses: list[str],
            show_progress: bool = True
        ) -> pd.DataFrame:
            """Process a batch of addresses.

            Args:
                addresses: List of address strings to process
                show_progress: Whether to show progress bar

            Returns:
                DataFrame with processing results
            """
            self.stats['start_time'] = datetime.now()
            self.stats['total'] = len(addresses)
            self._log(f"Starting batch processing of {len(addresses)} addresses")

            results = []
            iterator = tqdm(addresses, desc="Processing") if show_progress else addresses

            for address in iterator:
                matches = search(
                    address,
                    n=1,
                    threshold=self.threshold,
                    fuzz_base=self.fuzz_base
                )

                if matches and matches[0]['max_score'] >= self.threshold:
                    results.append({
                        'address': address,
                        'is_valid': True,
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    })
                    self.stats['valid'] += 1
                else:
                    results.append({
                        'address': address,
                        'is_valid': False,
                        'barangay': None,
                        'municipality': None,
                        'province': None,
                        'psgc_id': None,
                        'score': None
                    })
                    self.stats['invalid'] += 1

                # Log progress every 1000 addresses
                if len(results) % 1000 == 0:
                    valid_rate = self.stats['valid'] / len(results) * 100
                    self._log(f"Processed {len(results)} addresses (valid: {valid_rate:.1f}%)")

            self.stats['end_time'] = datetime.now()
            duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds()

            # Log final statistics
            valid_rate = self.stats['valid'] / self.stats['total'] * 100
            self._log(f"Batch processing complete!")
            self._log(f"  Total: {self.stats['total']}")
            self._log(f"  Valid: {self.stats['valid']} ({valid_rate:.1f}%)")
            self._log(f"  Invalid: {self.stats['invalid']} ({100-valid_rate:.1f}%)")
            self._log(f"  Duration: {duration:.2f} seconds")
            self._log(f"  Rate: {self.stats['total']/duration:.2f} addresses/second")

            return pd.DataFrame(results)

        def get_statistics(self) -> dict:
            """Get processing statistics.

            Returns:
                Dictionary with processing statistics
            """
            if self.stats['start_time'] and self.stats['end_time']:
                duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds()
                self.stats['duration_seconds'] = duration
                self.stats['rate_per_second'] = self.stats['total'] / duration

            return self.stats.copy()

    # Example usage
    processor = BatchProcessor(threshold=80.0, log_file='batch_processing.log')
    addresses = ["Tongmageng, Tawi-Tawi", "Rosario, Batangas", "San Jose, Manila"]
    df = processor.process(addresses, show_progress=True)
    print(df)

    stats = processor.get_statistics()
    print(f"Processing rate: {stats['rate_per_second']:.2f} addresses/second")

Memory Management
-----------------

Processing Large Files with Chunking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Process large files in chunks to avoid memory issues:

.. code-block:: python

    import pandas as pd
    from barangay import search, create_fuzz_base

    def process_large_csv_in_chunks(
        input_path: str,
        output_path: str,
        address_column: str = 'address',
        threshold: float = 80.0,
        chunk_size: int = 10000
    ) -> None:
        """Process a large CSV file in chunks.

        Args:
            input_path: Path to input CSV file
            output_path: Path to output CSV file
            address_column: Name of column containing addresses
            threshold: Minimum similarity score for validation
            chunk_size: Number of rows to process at once
        """
        # Create FuzzBase once for efficiency
        fuzz_base = create_fuzz_base()

        # Process in chunks
        chunk_number = 0
        first_chunk = True

        for chunk in pd.read_csv(input_path, chunksize=chunk_size):
            chunk_number += 1
            print(f"Processing chunk {chunk_number} ({len(chunk)} rows)")

            # Validate addresses in chunk
            results = []
            for idx, row in chunk.iterrows():
                address = row[address_column]
                matches = search(address, n=1, threshold=threshold, fuzz_base=fuzz_base)

                if matches and matches[0]['max_score'] >= threshold:
                    results.append({
                        **row.to_dict(),
                        'is_valid': True,
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    })
                else:
                    results.append({
                        **row.to_dict(),
                        'is_valid': False,
                        'barangay': None,
                        'municipality': None,
                        'province': None,
                        'psgc_id': None,
                        'score': None
                    })

            # Save chunk to file
            result_df = pd.DataFrame(results)
            result_df.to_csv(
                output_path,
                mode='w' if first_chunk else 'a',
                header=first_chunk,
                index=False
            )
            first_chunk = False

        print(f"Processing complete! Results saved to {output_path}")

Complete BatchProcessor Class
-----------------------------

Here's a comprehensive BatchProcessor class with all features:

.. code-block:: python

    import pandas as pd
    from typing import Optional, List, Dict, Any, Callable
    from datetime import datetime
    from barangay import search, create_fuzz_base
    from tqdm import tqdm

    class BatchProcessor:
        """Comprehensive batch processor for Philippine addresses.

        This class provides methods for processing large datasets of addresses
        with progress tracking, logging, memory management, and error handling.

        Attributes:
            threshold: Minimum similarity score for validation
            fuzz_base: Pre-computed fuzzy base for efficient searches
            log_file: Optional path to log file
            stats: Processing statistics
        """

        def __init__(
            self,
            threshold: float = 80.0,
            log_file: Optional[str] = None,
            cache_results: bool = False
        ):
            """Initialize the BatchProcessor.

            Args:
                threshold: Minimum similarity score for validation
                log_file: Optional path to log file
                cache_results: Whether to cache validation results
            """
            self.threshold = threshold
            self.fuzz_base = create_fuzz_base()
            self.log_file = log_file
            self.cache_results = cache_results
            self._cache = {}
            self.stats = {
                'total': 0,
                'valid': 0,
                'invalid': 0,
                'errors': 0,
                'start_time': None,
                'end_time': None
            }

        def _log(self, message: str) -> None:
            """Log a message to console and file.

            Args:
                message: Message to log
            """
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_message = f"[{timestamp}] {message}"
            print(log_message)

            if self.log_file:
                with open(self.log_file, 'a') as f:
                    f.write(log_message + '\n')

        def _get_cache_key(self, address: str) -> str:
            """Generate cache key for address.

            Args:
                address: Address string

            Returns:
                Cache key (hash of address)
            """
            return hash(address)

        def process(
            self,
            addresses: List[str],
            show_progress: bool = True,
            progress_desc: str = "Processing"
        ) -> pd.DataFrame:
            """Process a batch of addresses.

            Args:
                addresses: List of address strings to process
                show_progress: Whether to show progress bar
                progress_desc: Description for progress bar

            Returns:
                DataFrame with processing results
            """
            self.stats['start_time'] = datetime.now()
            self.stats['total'] = len(addresses)
            self._log(f"Starting batch processing of {len(addresses)} addresses")

            results = []
            iterator = tqdm(addresses, desc=progress_desc) if show_progress else addresses

            for address in iterator:
                try:
                    # Check cache first
                    if self.cache_results:
                        cache_key = self._get_cache_key(address)
                        if cache_key in self._cache:
                            results.append(self._cache[cache_key])
                            self.stats['valid'] += 1
                            continue

                    # Validate address
                    matches = search(
                        address,
                        n=1,
                        threshold=self.threshold,
                        fuzz_base=self.fuzz_base
                    )

                    if matches and matches[0]['max_score'] >= self.threshold:
                        result = {
                            'address': address,
                            'is_valid': True,
                            'barangay': matches[0]['barangay'],
                            'municipality': matches[0]['municipality_or_city'],
                            'province': matches[0]['province_or_huc'],
                            'psgc_id': matches[0]['psgc_id'],
                            'score': matches[0]['max_score']
                        }
                        self.stats['valid'] += 1
                    else:
                        result = {
                            'address': address,
                            'is_valid': False,
                            'barangay': None,
                            'municipality': None,
                            'province': None,
                            'psgc_id': None,
                            'score': None
                        }
                        self.stats['invalid'] += 1

                    # Cache result
                    if self.cache_results:
                        self._cache[cache_key] = result

                    results.append(result)

                except Exception as e:
                    self._log(f"Error processing address '{address}': {str(e)}")
                    results.append({
                        'address': address,
                        'is_valid': None,
                        'barangay': None,
                        'municipality': None,
                        'province': None,
                        'psgc_id': None,
                        'score': None,
                        'error': str(e)
                    })
                    self.stats['errors'] += 1

                # Log progress periodically
                if len(results) % 1000 == 0:
                    valid_rate = self.stats['valid'] / len(results) * 100
                    self._log(f"Processed {len(results)} addresses (valid: {valid_rate:.1f}%)")

            self.stats['end_time'] = datetime.now()
            self._log_final_statistics()

            return pd.DataFrame(results)

        def process_dataframe(
            self,
            df: pd.DataFrame,
            address_column: str,
            show_progress: bool = True
        ) -> pd.DataFrame:
            """Process addresses from a DataFrame.

            Args:
                df: DataFrame containing addresses
                address_column: Name of column containing addresses
                show_progress: Whether to show progress bar

            Returns:
                DataFrame with processing results added
            """
            addresses = df[address_column].tolist()
            results_df = self.process(addresses, show_progress=show_progress)

            # Merge results with original DataFrame
            result_df = pd.concat(
                [df.reset_index(drop=True), results_df],
                axis=1
            )

            return result_df

        def process_csv(
            self,
            input_path: str,
            output_path: str,
            address_column: str = 'address',
            chunk_size: Optional[int] = None
        ) -> None:
            """Process addresses from a CSV file.

            Args:
                input_path: Path to input CSV file
                output_path: Path to output CSV file
                address_column: Name of column containing addresses
                chunk_size: Optional chunk size for large files
            """
            if chunk_size:
                self._process_csv_in_chunks(
                    input_path,
                    output_path,
                    address_column,
                    chunk_size
                )
            else:
                df = pd.read_csv(input_path)
                result_df = self.process_dataframe(df, address_column)
                result_df.to_csv(output_path, index=False)
                self._log(f"Results saved to {output_path}")

        def _process_csv_in_chunks(
            self,
            input_path: str,
            output_path: str,
            address_column: str,
            chunk_size: int
        ) -> None:
            """Process a large CSV file in chunks.

            Args:
                input_path: Path to input CSV file
                output_path: Path to output CSV file
                address_column: Name of column containing addresses
                chunk_size: Number of rows to process at once
            """
            chunk_number = 0
            first_chunk = True

            for chunk in pd.read_csv(input_path, chunksize=chunk_size):
                chunk_number += 1
                self._log(f"Processing chunk {chunk_number} ({len(chunk)} rows)")

                result_df = self.process_dataframe(chunk, address_column)

                result_df.to_csv(
                    output_path,
                    mode='w' if first_chunk else 'a',
                    header=first_chunk,
                    index=False
                )
                first_chunk = False

            self._log(f"Results saved to {output_path}")

        def _log_final_statistics(self) -> None:
            """Log final processing statistics."""
            duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds()
            valid_rate = self.stats['valid'] / self.stats['total'] * 100 if self.stats['total'] > 0 else 0

            self._log("Batch processing complete!")
            self._log(f"  Total: {self.stats['total']}")
            self._log(f"  Valid: {self.stats['valid']} ({valid_rate:.1f}%)")
            self._log(f"  Invalid: {self.stats['invalid']} ({100-valid_rate:.1f}%)")
            self._log(f"  Errors: {self.stats['errors']}")
            self._log(f"  Duration: {duration:.2f} seconds")
            self._log(f"  Rate: {self.stats['total']/duration:.2f} addresses/second")

        def get_statistics(self) -> Dict[str, Any]:
            """Get processing statistics.

            Returns:
                Dictionary with processing statistics
            """
            stats = self.stats.copy()
            if stats['start_time'] and stats['end_time']:
                duration = (stats['end_time'] - stats['start_time']).total_seconds()
                stats['duration_seconds'] = duration
                stats['rate_per_second'] = stats['total'] / duration if duration > 0 else 0
            return stats

        def export_report(
            self,
            output_path: str,
            format: str = 'csv'
        ) -> None:
            """Export processing report.

            Args:
                output_path: Path to output file
                format: Output format ('csv' or 'excel')
            """
            stats = self.get_statistics()
            stats_df = pd.DataFrame([stats])
            stats_df.to_csv(output_path, index=False) if format == 'csv' else stats_df.to_excel(output_path, index=False)
            self._log(f"Report exported to {output_path}")

        def clear_cache(self) -> None:
            """Clear the validation cache."""
            self._cache.clear()
            self._log("Cache cleared")

    # Example usage
    if __name__ == '__main__':
        # Initialize processor
        processor = BatchProcessor(
            threshold=80.0,
            log_file='batch_processing.log',
            cache_results=True
        )

        # Process list of addresses
        addresses = [
            "Tongmageng, Tawi-Tawi",
            "Rosario, Batangas",
            "San Jose, Manila",
            "Invalid Address"
        ]
        df = processor.process(addresses, show_progress=True)
        print(df)

        # Process CSV file
        # processor.process_csv('input.csv', 'output.csv', address_column='address')

        # Get statistics
        stats = processor.get_statistics()
        print(f"Processing rate: {stats['rate_per_second']:.2f} addresses/second")

        # Export report
        processor.export_report('processing_report.csv')

Memory Management Tips
----------------------

1. **Process in chunks**: For very large files, process in chunks to avoid memory issues:

.. code-block:: python

    for chunk in pd.read_csv('large_file.csv', chunksize=10000):
        # Process chunk
        result = processor.process_dataframe(chunk, 'address')
        result.to_csv('output.csv', mode='a', header=not os.path.exists('output.csv'), index=False)

2. **Use efficient data types**: Convert columns to appropriate types:

.. code-block:: python

    df['is_valid'] = df['is_valid'].astype('bool')
    df['score'] = df['score'].astype('float32')

3. **Clear cache periodically**: If caching results, clear cache when it gets too large:

.. code-block:: python

    if len(processor._cache) > 100000:
        processor.clear_cache()

4. **Use generators**: For streaming data, use generators instead of lists:

.. code-block:: python

    def address_generator(file_path):
        with open(file_path) as f:
            for line in f:
                yield line.strip()

    for address in address_generator('addresses.txt'):
        result = process_single_address(address)

See Also
--------

* :ref:`api-search` - Search function API reference
* :ref:`examples-address-validation` - Address validation examples
* :ref:`advanced-caching` - Caching mechanisms
* :ref:`advanced-error-handling` - Error handling patterns