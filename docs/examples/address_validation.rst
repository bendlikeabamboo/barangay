Address Validation
==================

Use Case
--------
Validate user-submitted addresses to ensure they correspond to valid barangays in the Philippines. This is essential for e-commerce, delivery services, government forms, and any application that requires accurate Philippine addresses.

Common scenarios include:

* **E-commerce checkout**: Validate shipping addresses before order placement
* **Delivery services**: Ensure delivery addresses are valid before dispatching
* **Government forms**: Validate addresses in online applications
* **Data cleaning**: Standardize and validate address databases
* **Customer registration**: Verify addresses during user onboarding

Basic Validation
----------------

Single Address Validation
~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest approach validates a single address and returns whether it's valid along with the best match:

.. code-block:: python

    from barangay import search

    def validate_address(address: str, threshold: float = 80.0) -> tuple[bool, dict | None]:
        """Validate a single address against barangay data.

        Args:
            address: The address string to validate
            threshold: Minimum similarity score (0-100) to consider valid

        Returns:
            Tuple of (is_valid, matched_data)
        """
        results = search(address, n=1, threshold=threshold)
        if results and results[0]['max_score'] >= threshold:
            return True, results[0]
        return False, None

    # Example usage
    is_valid, match = validate_address("Tongmageng, Tawi-Tawi")
    if is_valid:
        print(f"Valid address: {match['barangay']}, {match['municipality_or_city']}")
    else:
        print("Invalid address")

Output:

.. code-block:: text

    Valid address: Tongmageng, Sitangkai

Handling Invalid Addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~

When validation fails, provide helpful feedback to users:

.. code-block:: python

    from barangay import search

    def validate_with_suggestions(address: str, threshold: float = 80.0) -> dict:
        """Validate address and provide suggestions if invalid.

        Args:
            address: The address string to validate
            threshold: Minimum similarity score (0-100) to consider valid

        Returns:
            Dictionary with validation result and suggestions
        """
        results = search(address, n=5, threshold=60.0)

        if not results:
            return {
                'is_valid': False,
                'message': 'No matching barangays found',
                'suggestions': []
            }

        best_match = results[0]
        is_valid = best_match['max_score'] >= threshold

        if is_valid:
            return {
                'is_valid': True,
                'message': 'Address is valid',
                'match': best_match,
                'suggestions': []
            }
        else:
            # Provide suggestions with lower threshold
            suggestions = [r for r in results if r['max_score'] >= 60.0]
            return {
                'is_valid': False,
                'message': f'Address not found. Did you mean?',
                'suggestions': suggestions
            }

    # Example usage
    result = validate_with_suggestions("Tongmagen, Tawi-Tawi")
    print(result['message'])
    for suggestion in result['suggestions']:
        print(f"  - {suggestion['barangay']}, {suggestion['municipality_or_city']} "
              f"(score: {suggestion['max_score']:.1f})")

Output:

.. code-block:: text

    Address not found. Did you mean?
      - Tongmageng, Sitangkai (score: 95.2)

Batch Validation
----------------

Validating Multiple Addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When processing multiple addresses, use batch validation for efficiency:

.. code-block:: python

    import pandas as pd
    from barangay import search

    def batch_validate_addresses(addresses: list[str], threshold: float = 80.0) -> pd.DataFrame:
        """Validate multiple addresses and return results as DataFrame.

        Args:
            addresses: List of address strings to validate
            threshold: Minimum similarity score (0-100) to consider valid

        Returns:
            DataFrame with validation results
        """
        results = []
        for address in addresses:
            matches = search(address, n=1, threshold=threshold)
            if matches and matches[0]['max_score'] >= threshold:
                results.append({
                    'original_address': address,
                    'is_valid': True,
                    'barangay': matches[0]['barangay'],
                    'municipality': matches[0]['municipality_or_city'],
                    'province': matches[0]['province_or_huc'],
                    'psgc_id': matches[0]['psgc_id'],
                    'score': matches[0]['max_score']
                })
            else:
                results.append({
                    'original_address': address,
                    'is_valid': False,
                    'barangay': None,
                    'municipality': None,
                    'province': None,
                    'psgc_id': None,
                    'score': None
                })

        return pd.DataFrame(results)

    # Example usage
    addresses = [
        "Tongmageng, Tawi-Tawi",
        "Rosario, Batangas",
        "Invalid Barangay Name, Invalid Province"
    ]

    df = batch_validate_addresses(addresses)
    print(df)

Output:

.. code-block:: text

                original_address  is_valid      barangay      municipality      province        psgc_id   score
    0    Tongmageng, Tawi-Tawi      True    Tongmageng         Sitangkai     Tawi-Tawi  157501001    95.2
    1        Rosario, Batangas      True      Rosario           Rosario      Batangas  175601001    90.5
    2  Invalid Barangay Name...     False          None               None          None         None     NaN

Processing Large Datasets
~~~~~~~~~~~~~~~~~~~~~~~~~

For large datasets, consider using progress tracking and parallel processing:

.. code-block:: python

    import pandas as pd
    from tqdm import tqdm
    from barangay import search

    def batch_validate_large_dataset(
        df: pd.DataFrame,
        address_column: str,
        threshold: float = 80.0
    ) -> pd.DataFrame:
        """Validate addresses in a large DataFrame with progress tracking.

        Args:
            df: DataFrame containing addresses
            address_column: Name of column containing addresses
            threshold: Minimum similarity score (0-100) to consider valid

        Returns:
            DataFrame with validation results added as new columns
        """
        results = []
        for idx, row in tqdm(df.iterrows(), total=len(df), desc="Validating addresses"):
            address = row[address_column]
            matches = search(address, n=1, threshold=threshold)

            if matches and matches[0]['max_score'] >= threshold:
                results.append({
                    'is_valid': True,
                    'barangay': matches[0]['barangay'],
                    'municipality': matches[0]['municipality_or_city'],
                    'province': matches[0]['province_or_huc'],
                    'psgc_id': matches[0]['psgc_id'],
                    'score': matches[0]['max_score']
                })
            else:
                results.append({
                    'is_valid': False,
                    'barangay': None,
                    'municipality': None,
                    'province': None,
                    'psgc_id': None,
                    'score': None
                })

        # Add results to DataFrame
        result_df = pd.DataFrame(results)
        return pd.concat([df.reset_index(drop=True), result_df], axis=1)

Integration with Forms or User Input
------------------------------------

Web Form Validation (Flask Example)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Integrate address validation into web forms:

.. code-block:: python

    from flask import Flask, request, jsonify
    from barangay import search

    app = Flask(__name__)

    @app.route('/api/validate-address', methods=['POST'])
    def validate_address_endpoint():
        """API endpoint to validate an address."""
        data = request.get_json()
        address = data.get('address')

        if not address:
            return jsonify({'error': 'Address is required'}), 400

        # Validate address
        results = search(address, n=3, threshold=70.0)

        if not results:
            return jsonify({
                'is_valid': False,
                'message': 'No matching barangays found',
                'suggestions': []
            })

        best_match = results[0]
        is_valid = best_match['max_score'] >= 80.0

        if is_valid:
            return jsonify({
                'is_valid': True,
                'match': {
                    'barangay': best_match['barangay'],
                    'municipality': best_match['municipality_or_city'],
                    'province': best_match['province_or_huc'],
                    'psgc_id': best_match['psgc_id'],
                    'score': best_match['max_score']
                }
            })
        else:
            suggestions = [
                {
                    'barangay': r['barangay'],
                    'municipality': r['municipality_or_city'],
                    'province': r['province_or_huc'],
                    'score': r['max_score']
                }
                for r in results if r['max_score'] >= 60.0
            ]
            return jsonify({
                'is_valid': False,
                'message': 'Address not found. Did you mean?',
                'suggestions': suggestions
            })

    if __name__ == '__main__':
        app.run(debug=True)

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

Create a CLI tool for address validation:

.. code-block:: python

    import argparse
    from barangay import search

    def main():
        parser = argparse.ArgumentParser(description='Validate Philippine addresses')
        parser.add_argument('address', help='Address to validate')
        parser.add_argument('--threshold', type=float, default=80.0,
                           help='Minimum similarity score (default: 80.0)')
        parser.add_argument('--show-suggestions', action='store_true',
                           help='Show suggestions if address is invalid')

        args = parser.parse_args()

        results = search(args.address, n=5, threshold=args.threshold)

        if not results:
            print(f"❌ No matching barangays found for: {args.address}")
            return

        best_match = results[0]
        is_valid = best_match['max_score'] >= args.threshold

        if is_valid:
            print(f"✅ Valid address: {args.address}")
            print(f"   Barangay: {best_match['barangay']}")
            print(f"   Municipality/City: {best_match['municipality_or_city']}")
            print(f"   Province: {best_match['province_or_huc']}")
            print(f"   PSGC ID: {best_match['psgc_id']}")
            print(f"   Confidence: {best_match['max_score']:.1f}%")
        else:
            print(f"❌ Invalid address: {args.address}")
            if args.show_suggestions:
                print("\nDid you mean?")
                for i, suggestion in enumerate(results[:3], 1):
                    print(f"   {i}. {suggestion['barangay']}, "
                          f"{suggestion['municipality_or_city']} "
                          f"(score: {suggestion['max_score']:.1f}%)")

    if __name__ == '__main__':
        main()

Complete AddressValidator Class
-------------------------------

Here's a comprehensive AddressValidator class that handles various validation scenarios:

.. code-block:: python

    import pandas as pd
    from typing import Optional, List, Dict, Any
    from barangay import search

    class AddressValidator:
        """Comprehensive address validator for Philippine barangays.

        This class provides methods for validating single and multiple addresses,
        with options for custom thresholds, suggestions, and detailed reporting.

        Attributes:
            default_threshold: Default minimum similarity score (0-100)
            suggestion_threshold: Threshold for providing suggestions
            max_suggestions: Maximum number of suggestions to return
        """

        def __init__(
            self,
            default_threshold: float = 80.0,
            suggestion_threshold: float = 60.0,
            max_suggestions: int = 5
        ):
            """Initialize the AddressValidator.

            Args:
                default_threshold: Default minimum similarity score for validation
                suggestion_threshold: Minimum score to include in suggestions
                max_suggestions: Maximum number of suggestions to return
            """
            self.default_threshold = default_threshold
            self.suggestion_threshold = suggestion_threshold
            self.max_suggestions = max_suggestions

        def validate(
            self,
            address: str,
            threshold: Optional[float] = None
        ) -> Dict[str, Any]:
            """Validate a single address.

            Args:
                address: The address string to validate
                threshold: Minimum similarity score (uses default if None)

            Returns:
                Dictionary with validation result and match data
            """
            if threshold is None:
                threshold = self.default_threshold

            results = search(address, n=self.max_suggestions, threshold=self.suggestion_threshold)

            if not results:
                return {
                    'is_valid': False,
                    'address': address,
                    'match': None,
                    'suggestions': [],
                    'message': 'No matching barangays found'
                }

            best_match = results[0]
            is_valid = best_match['max_score'] >= threshold

            if is_valid:
                return {
                    'is_valid': True,
                    'address': address,
                    'match': {
                        'barangay': best_match['barangay'],
                        'municipality': best_match['municipality_or_city'],
                        'province': best_match['province_or_huc'],
                        'psgc_id': best_match['psgc_id'],
                        'score': best_match['max_score']
                    },
                    'suggestions': [],
                    'message': 'Address is valid'
                }
            else:
                suggestions = [
                    {
                        'barangay': r['barangay'],
                        'municipality': r['municipality_or_city'],
                        'province': r['province_or_huc'],
                        'psgc_id': r['psgc_id'],
                        'score': r['max_score']
                    }
                    for r in results
                    if r['max_score'] >= self.suggestion_threshold
                ]
                return {
                    'is_valid': False,
                    'address': address,
                    'match': None,
                    'suggestions': suggestions,
                    'message': f'Address not found. {len(suggestions)} suggestion(s) available'
                }

        def validate_batch(
            self,
            addresses: List[str],
            threshold: Optional[float] = None,
            show_progress: bool = False
        ) -> pd.DataFrame:
            """Validate multiple addresses.

            Args:
                addresses: List of address strings to validate
                threshold: Minimum similarity score (uses default if None)
                show_progress: Whether to show progress bar

            Returns:
                DataFrame with validation results
            """
            if threshold is None:
                threshold = self.default_threshold

            results = []
            iterator = addresses
            if show_progress:
                try:
                    from tqdm import tqdm
                    iterator = tqdm(addresses, desc="Validating addresses")
                except ImportError:
                    pass

            for address in iterator:
                result = self.validate(address, threshold)
                results.append({
                    'original_address': address,
                    'is_valid': result['is_valid'],
                    'barangay': result['match']['barangay'] if result['match'] else None,
                    'municipality': result['match']['municipality'] if result['match'] else None,
                    'province': result['match']['province'] if result['match'] else None,
                    'psgc_id': result['match']['psgc_id'] if result['match'] else None,
                    'score': result['match']['score'] if result['match'] else None,
                    'message': result['message']
                })

            return pd.DataFrame(results)

        def get_statistics(self, df: pd.DataFrame) -> Dict[str, Any]:
            """Get validation statistics from a DataFrame of results.

            Args:
                df: DataFrame with validation results (from validate_batch)

            Returns:
                Dictionary with validation statistics
            """
            total = len(df)
            valid = df['is_valid'].sum()
            invalid = total - valid
            valid_rate = (valid / total * 100) if total > 0 else 0

            avg_score = df['score'].mean() if 'score' in df else None

            return {
                'total_addresses': total,
                'valid_addresses': int(valid),
                'invalid_addresses': int(invalid),
                'validation_rate': f'{valid_rate:.2f}%',
                'average_score': f'{avg_score:.2f}' if avg_score else None
            }

        def export_report(
            self,
            df: pd.DataFrame,
            output_path: str,
            format: str = 'csv'
        ) -> None:
            """Export validation results to a file.

            Args:
                df: DataFrame with validation results
                output_path: Path to output file
                format: Output format ('csv' or 'excel')
            """
            if format == 'csv':
                df.to_csv(output_path, index=False)
            elif format == 'excel':
                df.to_excel(output_path, index=False)
            else:
                raise ValueError(f"Unsupported format: {format}")

    # Example usage
    if __name__ == '__main__':
        validator = AddressValidator(
            default_threshold=80.0,
            suggestion_threshold=60.0,
            max_suggestions=5
        )

        # Single validation
        result = validator.validate("Tongmageng, Tawi-Tawi")
        print(f"Valid: {result['is_valid']}")
        if result['match']:
            print(f"Match: {result['match']['barangay']}, {result['match']['municipality']}")

        # Batch validation
        addresses = [
            "Tongmageng, Tawi-Tawi",
            "Rosario, Batangas",
            "Invalid Address"
        ]
        df = validator.validate_batch(addresses, show_progress=True)
        print(df)

        # Get statistics
        stats = validator.get_statistics(df)
        print(f"Validation rate: {stats['validation_rate']}")

        # Export report
        validator.export_report(df, 'validation_report.csv')

Error Handling and Edge Cases
-----------------------------

Handling Special Characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Addresses may contain special characters that need special handling:

.. code-block:: python

    from barangay import search, sanitize_input

    def validate_with_special_handling(address: str) -> dict:
        """Validate address with special character handling.

        Args:
            address: Address string that may contain special characters

        Returns:
            Validation result with special handling notes
        """
        # Define custom sanitizer for special characters
        custom_sanitizer = lambda x: sanitize_input(
            x,
            exclude=["#", "*", "&", "(", ")", "[", "]"]
        )

        # Try with custom sanitizer first
        results = search(address, n=3, threshold=70.0, search_sanitizer=custom_sanitizer)

        if not results:
            # Try with default sanitizer
            results = search(address, n=3, threshold=70.0)

        if not results:
            return {
                'is_valid': False,
                'message': 'No matches found even with special character handling',
                'notes': 'Address may contain invalid characters or be outside coverage'
            }

        best_match = results[0]
        is_valid = best_match['max_score'] >= 80.0

        return {
            'is_valid': is_valid,
            'match': best_match if is_valid else None,
            'notes': 'Address validated with special character handling'
        }

Handling Historical Addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate addresses against historical data for legacy systems:

.. code-block:: python

    from barangay import search

    def validate_historical_address(
        address: str,
        historical_date: str,
        threshold: float = 80.0
    ) -> dict:
        """Validate address against historical data.

        Args:
            address: Address string to validate
            historical_date: Date string (YYYY-MM-DD) for historical data
            threshold: Minimum similarity score (0-100)

        Returns:
            Validation result with historical context
        """
        results = search(address, n=3, threshold=threshold, as_of=historical_date)

        if not results:
            return {
                'is_valid': False,
                'message': f'No matches found in historical data ({historical_date})',
                'suggestion': 'Try validating with current data'
            }

        best_match = results[0]
        is_valid = best_match['max_score'] >= threshold

        return {
            'is_valid': is_valid,
            'match': best_match if is_valid else None,
            'historical_date': historical_date,
            'notes': f'Validated against historical data from {historical_date}'
        }

    # Example usage
    result = validate_historical_address(
        "Tongmageng, Tawi-Tawi",
        historical_date="2025-07-08"
    )
    print(f"Valid: {result['is_valid']}")
    print(f"Validated against: {result['historical_date']}")

Performance Tips
----------------

1. **Reuse FuzzBase instances**: For batch validation, create a FuzzBase instance once and reuse it:

.. code-block:: python

    from barangay import search, create_fuzz_base

    # Create FuzzBase once
    fuzz_base = create_fuzz_base()

    # Use for multiple searches
    for address in addresses:
        results = search(address, fuzz_base=fuzz_base)

2. **Adjust threshold based on use case**: Use higher thresholds (85-90) for critical applications and lower thresholds (70-75) for data exploration.

3. **Cache validation results**: Store validation results to avoid re-validating the same addresses:

.. code-block:: python

    import hashlib

    def get_address_hash(address: str) -> str:
        """Generate a hash for an address string."""
        return hashlib.md5(address.encode()).hexdigest()

    # Use hash as cache key
    cache = {}
    address_hash = get_address_hash(address)
    if address_hash in cache:
        result = cache[address_hash]
    else:
        result = validator.validate(address)
        cache[address_hash] = result

See Also
--------

* :ref:`api-search` - Search function API reference
* :ref:`userguide-fuzzy-search` - Fuzzy search user guide
* :ref:`examples-batch-processing` - Batch processing examples
* :ref:`advanced-error-handling` - Error handling patterns