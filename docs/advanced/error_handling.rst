Error Handling
==============

This section provides a comprehensive guide to error handling patterns and best practices when using the barangay package.

Overview
--------

The barangay package may raise various exceptions depending on the operation being performed. Proper error handling ensures your application remains robust and provides helpful feedback to users.

Common Exception Types:

* **ValueError**: Invalid parameters or configuration
* **RuntimeError**: Download failures or data loading errors
* **FileNotFoundError**: Missing data files
* **ConnectionError**: Network-related issues
* **KeyError**: Missing data keys or columns

Common Exceptions and Their Causes
----------------------------------

ValueError
~~~~~~~~~~

**When it occurs**: Invalid parameters are passed to functions.

**Common causes**:

1. **Invalid match_hooks**: Using non-existent administrative levels

.. code-block:: python

    from barangay import search

    # This will raise ValueError
    try:
        results = search(
            "Tongmageng",
            match_hooks=["invalid_level"]  # Invalid match hook
        )
    except ValueError as e:
        print(f"Error: {e}")

2. **Invalid data_type**: Using unsupported data types

.. code-block:: python

    from barangay.data_manager import DataManager

    # This will raise ValueError
    try:
        dm = DataManager()
        data = dm.get_data(data_type="invalid_type")
    except ValueError as e:
        print(f"Error: {e}")

3. **Invalid date format**: Using incorrect date format

.. code-block:: python

    from barangay import resolve_date, get_available_dates

    # This will raise ValueError
    try:
        available = get_available_dates()
        resolved, _ = resolve_date("2025/07/08", available, "2026-01-13")
    except ValueError as e:
        print(f"Error: {e}")

**Handling pattern**:

.. code-block:: python

    from barangay import search

    def safe_search(address: str, match_hooks: list = None) -> dict:
        """Search with error handling.

        Args:
            address: Address string to search
            match_hooks: List of administrative levels to match

        Returns:
            Dictionary with search result or error information
        """
        try:
            if match_hooks is None:
                match_hooks = ["province", "municipality", "barangay"]

            # Validate match_hooks
            valid_hooks = ["province", "municipality", "barangay"]
            invalid_hooks = [h for h in match_hooks if h not in valid_hooks]

            if invalid_hooks:
                raise ValueError(
                    f"Invalid match_hooks: {invalid_hooks}. "
                    f"Valid options: {valid_hooks}"
                )

            results = search(address, match_hooks=match_hooks)

            return {
                'success': True,
                'results': results,
                'error': None
            }

        except ValueError as e:
            return {
                'success': False,
                'results': None,
                'error': f"Validation error: {str(e)}"
            }
        except Exception as e:
            return {
                'success': False,
                'results': None,
                'error': f"Unexpected error: {str(e)}"
            }

RuntimeError
~~~~~~~~~~~~

**When it occurs**: Operations fail due to runtime conditions.

**Common causes**:

1. **Download failures**: Cannot download data from GitHub

.. code-block:: python

    from barangay.data_manager import DataManager

    # This may raise RuntimeError if download fails
    try:
        dm = DataManager()
        data = dm.get_data(as_of="2025-07-08", data_type="basic")
    except RuntimeError as e:
        print(f"Error: {e}")

2. **Data corruption**: Cached data is corrupted

.. code-block:: python

    from barangay import load_fuzzer_base

    # This may raise RuntimeError if cache is corrupted
    try:
        df = load_fuzzer_base(as_of="2025-07-08")
    except RuntimeError as e:
        print(f"Error: {e}")

**Handling pattern**:

.. code-block:: python

    from barangay.data_manager import DataManager
    import time

    def safe_load_with_retry(
        data_type: str = "basic",
        as_of: str = None,
        max_retries: int = 3,
        retry_delay: float = 1.0
    ) -> dict:
        """Load data with retry logic.

        Args:
            data_type: Type of data to load
            as_of: Optional date string
            max_retries: Maximum number of retry attempts
            retry_delay: Delay between retries in seconds

        Returns:
            Dictionary with data or error information
        """
        dm = DataManager()

        for attempt in range(max_retries):
            try:
                data = dm.get_data(as_of=as_of, data_type=data_type)
                return {
                    'success': True,
                    'data': data,
                    'error': None,
                    'attempts': attempt + 1
                }
            except RuntimeError as e:
                if attempt < max_retries - 1:
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {retry_delay}s...")
                    time.sleep(retry_delay)
                else:
                    return {
                        'success': False,
                        'data': None,
                        'error': f"Failed after {max_retries} attempts: {str(e)}",
                        'attempts': max_retries
                    }
            except Exception as e:
                return {
                    'success': False,
                    'data': None,
                    'error': f"Unexpected error: {str(e)}",
                    'attempts': attempt + 1
                }

FileNotFoundError
~~~~~~~~~~~~~~~~~

**When it occurs**: Required data files are missing.

**Common causes**:

1. **Missing package data**: Installation is incomplete

.. code-block:: python

    from barangay import load_barangay_data

    # This may raise FileNotFoundError if package data is missing
    try:
        data = load_barangay_data()
    except FileNotFoundError as e:
        print(f"Error: {e}")

2. **Missing cache file**: Expected cache file doesn't exist

.. code-block:: python

    from barangay import load_fuzzer_base

    # This may raise FileNotFoundError if cache is missing
    try:
        df = load_fuzzer_base(as_of="2025-07-08")
    except FileNotFoundError as e:
        print(f"Error: {e}")

**Handling pattern**:

.. code-block:: python

    from barangay import load_barangay_data
    from barangay.data_manager import DataManager

    def safe_load_with_fallback(data_type: str = "basic") -> dict:
        """Load data with fallback to download.

        Args:
            data_type: Type of data to load

        Returns:
            Dictionary with data or error information
        """
        # Try to load from package first
        try:
            if data_type == "basic":
                from barangay import load_barangay_data
                data = load_barangay_data()
            elif data_type == "extended":
                from barangay import load_barangay_extended_data
                data = load_barangay_extended_data()
            elif data_type == "flat":
                from barangay import load_barangay_flat_data
                data = load_barangay_flat_data()
            else:
                raise ValueError(f"Invalid data_type: {data_type}")

            return {
                'success': True,
                'data': data,
                'source': 'package',
                'error': None
            }

        except FileNotFoundError:
            # Package data not found, try DataManager
            try:
                dm = DataManager()
                data = dm.get_data(data_type=data_type)
                return {
                    'success': True,
                    'data': data,
                    'source': 'downloaded',
                    'error': None
                }
            except Exception as e:
                return {
                    'success': False,
                    'data': None,
                    'source': None,
                    'error': f"Failed to load data: {str(e)}"
                }

Error Handling Patterns
-----------------------

Try-Except Patterns
~~~~~~~~~~~~~~~~~~~

Basic Pattern
~~~~~~~~~~~~~

The most common error handling pattern:

.. code-block:: python

    from barangay import search

    try:
        results = search("Tongmageng, Tawi-Tawi")
        # Process results
        for result in results:
            # Get the maximum score from active matching strategies
            scores = [
                result.get('f_000b_ratio_score', 0),
                result.get('f_0p0b_ratio_score', 0),
                result.get('f_00mb_ratio_score', 0),
                result.get('f_0pmb_ratio_score', 0)
            ]
            score = max(scores)
            print(f"{result['barangay']} (score: {score:.1f})")
    except ValueError as e:
        print(f"Invalid parameters: {e}")
    except RuntimeError as e:
        print(f"Runtime error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

Nested Pattern
~~~~~~~~~~~~~~

Handle errors at multiple levels:

.. code-block:: python

    from barangay import search, load_barangay_data

    def process_address(address: str) -> dict:
        """Process address with nested error handling.

        Args:
            address: Address string to process

        Returns:
            Dictionary with processing result
        """
        result = {
            'address': address,
            'success': False,
            'barangay': None,
            'error': None
        }

        try:
            # Level 1: Search for address
            matches = search(address, n=1, threshold=80.0)

            if not matches:
                result['error'] = 'No matching barangays found'
                return result

            # Level 2: Validate match
            best_match = matches[0]
            # Get the maximum score from active matching strategies
            scores = [
                best_match.get('f_000b_ratio_score', 0),
                best_match.get('f_0p0b_ratio_score', 0),
                best_match.get('f_00mb_ratio_score', 0),
                best_match.get('f_0pmb_ratio_score', 0)
            ]
            best_score = max(scores)
            if best_score < 80.0:
                result['error'] = f'Low confidence match (score: {best_score:.1f})'
                return result

            # Level 3: Load additional data
            try:
                from barangay import load_barangay_flat_data
                flat_data = load_barangay_flat_data()

                # Find additional information
                for item in flat_data:
                    if item['psgc_id'] == best_match['psgc_id']:
                        result['barangay'] = item
                        result['success'] = True
                        break

            except Exception as e:
                # Level 3 error - still return the match
                result['barangay'] = best_match
                result['success'] = True
                result['warning'] = f'Could not load additional data: {str(e)}'

        except ValueError as e:
            result['error'] = f'Invalid search parameters: {str(e)}'
        except RuntimeError as e:
            result['error'] = f'Search runtime error: {str(e)}'
        except Exception as e:
            result['error'] = f'Unexpected error: {str(e)}'

        return result

Logging and Debugging
---------------------

Enabling Verbose Logging
~~~~~~~~~~~~~~~~~~~~~~~~

Enable verbose logging to diagnose issues:

.. code-block:: python

    import os
    import logging
    from barangay import search

    # Enable verbose logging
    os.environ['BARANGAY_VERBOSE'] = '1'

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Perform search with verbose output
    results = search("Tongmageng, Tawi-Tawi")

Output:

.. code-block:: text

    2026-02-19 04:00:00 - barangay.data_manager - INFO - [barangay] Using 2026-01-13 dataset
    2026-02-19 04:00:00 - barangay.search - INFO - Searching for: Tongmageng, Tawi-Tawi

Debugging with Custom Logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create custom logging for specific operations:

.. code-block:: python

    import logging
    from barangay import search

    # Create custom logger
    logger = logging.getLogger('barangay_debug')
    logger.setLevel(logging.DEBUG)

    # Add file handler
    file_handler = logging.FileHandler('barangay_debug.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    def debug_search(address: str) -> list:
        """Search with detailed debugging.

        Args:
            address: Address string to search

        Returns:
            List of search results
        """
        logger.debug(f"Starting search for: {address}")

        try:
            results = search(address, n=5, threshold=70.0)
            logger.debug(f"Found {len(results)} results")

            for i, result in enumerate(results):
                # Get the maximum score from active matching strategies
                scores = [
                    result.get('f_000b_ratio_score', 0),
                    result.get('f_0p0b_ratio_score', 0),
                    result.get('f_00mb_ratio_score', 0),
                    result.get('f_0pmb_ratio_score', 0)
                ]
                score = max(scores)
                logger.debug(
                    f"Result {i+1}: {result['barangay']} "
                    f"(score: {score:.1f})"
                )

            return results

        except Exception as e:
            logger.error(f"Search failed: {str(e)}", exc_info=True)
            raise

    # Example usage
    results = debug_search("Tongmageng, Tawi-Tawi")

Network Error Handling
----------------------

Handling Connection Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~

Network operations can fail due to various reasons:

.. code-block:: python

    from barangay.data_manager import DataManager
    import requests

    def safe_download_with_timeout(
        as_of: str,
        data_type: str = "basic",
        timeout: float = 30.0
    ) -> dict:
        """Download data with timeout and connection error handling.

        Args:
            as_of: Date string for historical data
            data_type: Type of data to load
            timeout: Timeout in seconds

        Returns:
            Dictionary with download result
        """
        dm = DataManager()

        try:
            data = dm.get_data(as_of=as_of, data_type=data_type)
            return {
                'success': True,
                'data': data,
                'error': None
            }

        except requests.exceptions.Timeout:
            return {
                'success': False,
                'data': None,
                'error': f'Download timeout after {timeout} seconds'
            }

        except requests.exceptions.ConnectionError:
            return {
                'success': False,
                'data': None,
                'error': 'Connection error - check internet connection'
            }

        except requests.exceptions.HTTPError as e:
            return {
                'success': False,
                'data': None,
                'error': f'HTTP error: {e.response.status_code}'
            }

        except Exception as e:
            return {
                'success': False,
                'data': None,
                'error': f'Unexpected error: {str(e)}'
            }

Handling Rate Limiting
~~~~~~~~~~~~~~~~~~~~~~

GitHub API has rate limits. Handle them gracefully:

.. code-block:: python

    from barangay.data_manager import DataManager
    import time
    import random

    def download_with_rate_limit(
        as_of: str,
        data_type: str = "basic",
        max_retries: int = 5,
        base_delay: float = 1.0
    ) -> dict:
        """Download with exponential backoff for rate limiting.

        Args:
            as_of: Date string for historical data
            data_type: Type of data to load
            max_retries: Maximum number of retry attempts
            base_delay: Base delay between retries

        Returns:
            Dictionary with download result
        """
        dm = DataManager()

        for attempt in range(max_retries):
            try:
                data = dm.get_data(as_of=as_of, data_type=data_type)
                return {
                    'success': True,
                    'data': data,
                    'error': None,
                    'attempts': attempt + 1
                }

            except Exception as e:
                error_str = str(e).lower()

                # Check for rate limiting
                if 'rate limit' in error_str or '429' in error_str:
                    if attempt < max_retries - 1:
                        # Exponential backoff with jitter
                        delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                        print(f"Rate limited. Waiting {delay:.1f}s before retry...")
                        time.sleep(delay)
                        continue
                    else:
                        return {
                            'success': False,
                            'data': None,
                            'error': f'Rate limit exceeded after {max_retries} attempts',
                            'attempts': max_retries
                        }
                else:
                    # Non-rate-limit error, return immediately
                    return {
                        'success': False,
                        'data': None,
                        'error': str(e),
                        'attempts': attempt + 1
                    }

Data Validation Errors
----------------------

Validating Input Data
~~~~~~~~~~~~~~~~~~~~~

Validate input data before processing:

.. code-block:: python

    from barangay import search

    def validate_search_input(
        search_string: str,
        threshold: float = None,
        n: int = None
    ) -> dict:
        """Validate search input parameters.

        Args:
            search_string: String to search for
            threshold: Optional threshold value
            n: Optional number of results

        Returns:
            Dictionary with validation result
        """
        errors = []

        # Validate search_string
        if not search_string or not isinstance(search_string, str):
            errors.append("search_string must be a non-empty string")

        if search_string and len(search_string.strip()) == 0:
            errors.append("search_string cannot be empty or whitespace")

        # Validate threshold
        if threshold is not None:
            if not isinstance(threshold, (int, float)):
                errors.append("threshold must be a number")
            elif threshold < 0 or threshold > 100:
                errors.append("threshold must be between 0 and 100")

        # Validate n
        if n is not None:
            if not isinstance(n, int):
                errors.append("n must be an integer")
            elif n < 1:
                errors.append("n must be at least 1")

        return {
            'valid': len(errors) == 0,
            'errors': errors
        }

    # Example usage
    validation = validate_search_input(
        search_string="Tongmageng",
        threshold=80.0,
        n=5
    )

    if validation['valid']:
        results = search("Tongmageng", threshold=80.0, n=5)
    else:
        print("Validation errors:")
        for error in validation['errors']:
            print(f"  - {error}")

Validating Output Data
~~~~~~~~~~~~~~~~~~~~~~

Validate output data before using it:

.. code-block:: python

    from barangay import search

    def validate_search_results(results: list) -> dict:
        """Validate search results.

        Args:
            results: List of search results

        Returns:
            Dictionary with validation result
        """
        errors = []
        warnings = []

        # Check if results is a list
        if not isinstance(results, list):
            errors.append("results must be a list")
            return {'valid': False, 'errors': errors, 'warnings': warnings}

        # Check each result
        for i, result in enumerate(results):
            if not isinstance(result, dict):
                errors.append(f"Result {i} must be a dictionary")
                continue

            # Check required fields
            required_fields = ['barangay', 'province_or_huc', 'municipality_or_city', 'psgc_id']
            for field in required_fields:
                if field not in result:
                    errors.append(f"Result {i} missing required field: {field}")

            # Check score range
            score_fields = ['f_000b_ratio_score', 'f_0p0b_ratio_score', 'f_00mb_ratio_score', 'f_0pmb_ratio_score']
            for score_field in score_fields:
                if score_field in result:
                    score = result[score_field]
                    if not isinstance(score, (int, float)):
                        errors.append(f"Result {i} {score_field} must be a number")
                    elif score < 0 or score > 100:
                        warnings.append(f"Result {i} {score_field} out of range: {score}")

        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }

    # Example usage
    results = search("Tongmageng")
    validation = validate_search_results(results)

    if validation['valid']:
        print("Results are valid")
    else:
        print("Validation errors:")
        for error in validation['errors']:
            print(f"  - {error}")

    if validation['warnings']:
        print("Warnings:")
        for warning in validation['warnings']:
            print(f"  - {warning}")

Code Examples with Try/Except Patterns
--------------------------------------

Comprehensive Error Handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A comprehensive error handler for all barangay operations:

.. code-block:: python

    import logging
    from typing import Any, Callable, Optional
    from barangay import search, create_fuzz_base
    from barangay.data_manager import DataManager

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger('barangay_handler')

    class BarangayErrorHandler:
        """Comprehensive error handler for barangay operations."""

        def __init__(self, verbose: bool = True):
            """Initialize the error handler.

            Args:
                verbose: Whether to log verbose messages
            """
            self.verbose = verbose
            self.error_count = 0
            self.success_count = 0

        def execute(
            self,
            operation: Callable,
            *args,
            operation_name: str = "operation",
            **kwargs
        ) -> dict:
            """Execute an operation with error handling.

            Args:
                operation: Function to execute
                *args: Positional arguments for operation
                operation_name: Name of the operation for logging
                **kwargs: Keyword arguments for operation

            Returns:
                Dictionary with operation result or error information
            """
            result = {
                'operation': operation_name,
                'success': False,
                'data': None,
                'error': None
            }

            try:
                if self.verbose:
                    logger.info(f"Starting {operation_name}")

                # Execute operation
                data = operation(*args, **kwargs)

                result['success'] = True
                result['data'] = data
                self.success_count += 1

                if self.verbose:
                    logger.info(f"Successfully completed {operation_name}")

            except ValueError as e:
                result['error'] = f"Validation error: {str(e)}"
                self.error_count += 1
                logger.error(f"{operation_name} failed: {result['error']}")

            except RuntimeError as e:
                result['error'] = f"Runtime error: {str(e)}"
                self.error_count += 1
                logger.error(f"{operation_name} failed: {result['error']}")

            except FileNotFoundError as e:
                result['error'] = f"File not found: {str(e)}"
                self.error_count += 1
                logger.error(f"{operation_name} failed: {result['error']}")

            except Exception as e:
                result['error'] = f"Unexpected error: {str(e)}"
                self.error_count += 1
                logger.error(f"{operation_name} failed: {result['error']}", exc_info=True)

            return result

        def search_with_handling(
            self,
            search_string: str,
            **kwargs
        ) -> dict:
            """Search with error handling.

            Args:
                search_string: String to search for
                **kwargs: Additional arguments for search()

            Returns:
                Dictionary with search result or error information
            """
            return self.execute(
                search,
                search_string,
                operation_name="search",
                **kwargs
            )

        def load_data_with_handling(
            self,
            data_type: str = "basic",
            as_of: Optional[str] = None
        ) -> dict:
            """Load data with error handling.

            Args:
                data_type: Type of data to load
                as_of: Optional date string

            Returns:
                Dictionary with data or error information
            """
            def load_operation():
                dm = DataManager()
                return dm.get_data(as_of=as_of, data_type=data_type)

            return self.execute(
                load_operation,
                operation_name=f"load_{data_type}_data"
            )

        def get_statistics(self) -> dict:
            """Get error handling statistics.

            Returns:
                Dictionary with statistics
            """
            total = self.success_count + self.error_count
            success_rate = (self.success_count / total * 100) if total > 0 else 0

            return {
                'total_operations': total,
                'successful': self.success_count,
                'failed': self.error_count,
                'success_rate': f'{success_rate:.1f}%'
            }

    # Example usage
    if __name__ == '__main__':
        handler = BarangayErrorHandler(verbose=True)

        # Search with error handling
        result = handler.search_with_handling(
            "Tongmageng, Tawi-Tawi",
            n=5,
            threshold=80.0
        )

        if result['success']:
            print(f"Found {len(result['data'])} results")
        else:
            print(f"Search failed: {result['error']}")

        # Load data with error handling
        data_result = handler.load_data_with_handling(data_type="basic")

        if data_result['success']:
            print(f"Loaded data successfully")
        else:
            print(f"Failed to load data: {data_result['error']}")

        # Get statistics
        stats = handler.get_statistics()
        print(f"Statistics: {stats}")

See Also
--------

* :doc:`../api_reference/search` - Search function API reference
* :doc:`../api_reference/data_manager` - DataManager class API reference
* :doc:`../troubleshooting/common_errors` - Common errors and solutions
* :doc:`caching` - Caching mechanisms