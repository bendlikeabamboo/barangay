Geocoding
=========

Use Case
--------
Convert Philippine addresses to geographic coordinates (latitude/longitude) and perform reverse geocoding to find the nearest barangay. This is essential for:

* **Mapping applications**: Display addresses on maps
* **Location-based services**: Find nearby services and amenities
* **Delivery routing**: Optimize delivery routes
* **Demographic analysis**: Analyze population distribution
* **Emergency services**: Locate incidents accurately

.. note::
   The barangay package does not include geocoding functionality directly. You need to integrate
   with external geocoding services like Google Maps API, OpenStreetMap/Nominatim, or
   Mapbox. This guide shows how to combine barangay validation with external geocoding services.

Basic Geocoding
---------------

Forward Geocoding with Address Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combine address validation with geocoding to ensure accuracy:

.. code-block:: python

    import requests
    from barangay import search

    class GeocodingHelper:
        """Helper class for geocoding Philippine addresses."""

        def __init__(self, nominatim_email: str):
            """Initialize with Nominatim email (required for API usage).

            Args:
                nominatim_email: Email address for Nominatim API (required by policy)
            """
            self.nominatim_url = "https://nominatim.openstreetmap.org/search"
            self.nominatim_email = nominatim_email

        def geocode(
            self,
            address: str,
            validate_barangay: bool = True,
            threshold: float = 80.0
        ) -> dict:
            """Geocode an address with optional barangay validation.

            Args:
                address: Address string to geocode
                validate_barangay: Whether to validate barangay before geocoding
                threshold: Minimum similarity score for barangay validation

            Returns:
                Dictionary with geocoding results and validation status
            """
            result = {
                'original_address': address,
                'is_valid_barangay': None,
                'barangay_match': None,
                'coordinates': None,
                'formatted_address': None
            }

            # Validate barangay if requested
            if validate_barangay:
                matches = search(address, n=1, threshold=threshold)
                if matches and matches[0]['max_score'] >= threshold:
                    result['is_valid_barangay'] = True
                    result['barangay_match'] = {
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    }
                else:
                    result['is_valid_barangay'] = False

            # Geocode using Nominatim
            params = {
                'q': address,
                'format': 'json',
                'limit': 1,
                'countrycodes': 'ph',
                'email': self.nominatim_email
            }

            try:
                response = requests.get(self.nominatim_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()

                if data:
                    result['coordinates'] = {
                        'latitude': float(data[0]['lat']),
                        'longitude': float(data[0]['lon'])
                    }
                    result['formatted_address'] = data[0].get('display_name')
            except requests.RequestException as e:
                result['error'] = f"Geocoding failed: {str(e)}"

            return result

    # Example usage
    geocoder = GeocodingHelper(nominatim_email="your-email@example.com")
    result = geocoder.geocode("Tongmageng, Tawi-Tawi")

    print(f"Valid Barangay: {result['is_valid_barangay']}")
    if result['coordinates']:
        print(f"Coordinates: {result['coordinates']['latitude']}, {result['coordinates']['longitude']}")
    if result['barangay_match']:
        print(f"Barangay: {result['barangay_match']['barangay']}")

Batch Geocoding
~~~~~~~~~~~~~~~

Geocode multiple addresses with validation:

.. code-block:: python

    import pandas as pd
    from barangay import search
    from tqdm import tqdm

    def batch_geocode(
        addresses: list[str],
        geocoding_helper: GeocodingHelper,
        validate_barangay: bool = True
    ) -> pd.DataFrame:
        """Geocode multiple addresses with barangay validation.

        Args:
            addresses: List of address strings to geocode
            geocoding_helper: GeocodingHelper instance
            validate_barangay: Whether to validate barangays

        Returns:
            DataFrame with geocoding results
        """
        results = []
        for address in tqdm(addresses, desc="Geocoding addresses"):
            result = geocoding_helper.geocode(address, validate_barangay=validate_barangay)
            results.append(result)

        return pd.DataFrame(results)

    # Example usage
    addresses = [
        "Tongmageng, Tawi-Tawi",
        "Rosario, Batangas",
        "San Jose, Manila"
    ]

    df = batch_geocode(addresses, geocoder)
    print(df[['original_address', 'is_valid_barangay', 'coordinates']])

Reverse Geocoding with Barangay Lookup
--------------------------------------

Finding Nearest Barangay from Coordinates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reverse geocode coordinates and match to nearest barangay:

.. code-block:: python

    import requests
    import math
    from barangay import BARANGAY_FLAT

    class ReverseGeocoder:
        """Reverse geocode coordinates to find nearest barangay."""

        def __init__(self, nominatim_email: str):
            """Initialize with Nominatim email.

            Args:
                nominatim_email: Email address for Nominatim API
            """
            self.nominatim_url = "https://nominatim.openstreetmap.org/reverse"
            self.nominatim_email = nominatim_email
            self._load_barangay_coordinates()

        def _load_barangay_coordinates(self):
            """Load barangay data for coordinate matching.

            Note: This is a placeholder. In production, you would need
            actual coordinate data for each barangay.
            """
            # In a real implementation, you would load a dataset
            # with barangay coordinates. For this example, we'll use
            # a simple lookup structure.
            self.barangay_coords = {}
            # This would be populated with actual coordinate data
            # Format: {psgc_id: {'lat': float, 'lon': float}}

        def reverse_geocode(
            self,
            lat: float,
            lon: float,
            find_nearest_barangay: bool = True
        ) -> dict:
            """Reverse geocode coordinates to address.

            Args:
                lat: Latitude
                lon: Longitude
                find_nearest_barangay: Whether to find nearest barangay

            Returns:
                Dictionary with reverse geocoding results
            """
            result = {
                'coordinates': {'latitude': lat, 'longitude': lon},
                'address': None,
                'nearest_barangay': None
            }

            # Reverse geocode using Nominatim
            params = {
                'lat': lat,
                'lon': lon,
                'format': 'json',
                'email': self.nominatim_email
            }

            try:
                response = requests.get(self.nominatim_url, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()

                if 'address' in data:
                    result['address'] = data['address']

                    # Find nearest barangay if requested
                    if find_nearest_barangay:
                        # Use the address components to search for barangay
                        address_parts = data['address']
                        search_string = self._build_search_string(address_parts)
                        result['nearest_barangay'] = self._find_barangay(search_string)

            except requests.RequestException as e:
                result['error'] = f"Reverse geocoding failed: {str(e)}"

            return result

        def _build_search_string(self, address_parts: dict) -> str:
            """Build search string from address components."""
            parts = []
            if 'suburb' in address_parts:
                parts.append(address_parts['suburb'])
            if 'city' in address_parts or 'town' in address_parts:
                parts.append(address_parts.get('city', address_parts.get('town', '')))
            if 'state' in address_parts:
                parts.append(address_parts['state'])
            return ', '.join(parts)

        def _find_barangay(self, search_string: str) -> dict:
            """Find barangay matching the search string."""
            from barangay import search
            matches = search(search_string, n=1, threshold=70.0)
            if matches:
                return {
                    'barangay': matches[0]['barangay'],
                    'municipality': matches[0]['municipality_or_city'],
                    'province': matches[0]['province_or_huc'],
                    'psgc_id': matches[0]['psgc_id'],
                    'score': matches[0]['max_score']
                }
            return None

    # Example usage
    reverse_geocoder = ReverseGeocoder(nominatim_email="your-email@example.com")

    # Reverse geocode coordinates (example: Manila coordinates)
    result = reverse_geocoder.reverse_geocode(14.5995, 120.9842)

    print(f"Address: {result['address']}")
    if result['nearest_barangay']:
        print(f"Nearest Barangay: {result['nearest_barangay']['barangay']}")

Integration with Geospatial Libraries
-------------------------------------

Creating GeoDataFrames from Barangay Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use geopandas to work with barangay data as geographic data:

.. code-block:: python

    import pandas as pd
    import geopandas as gpd
    from shapely.geometry import Point
    from barangay import BARANGAY_FLAT

    def create_geodataframe(
        coordinates_data: pd.DataFrame,
        barangay_data: dict = None
    ) -> gpd.GeoDataFrame:
        """Create a GeoDataFrame from coordinates with barangay matching.

        Args:
            coordinates_data: DataFrame with 'lat' and 'lon' columns
            barangay_data: Optional barangay data (uses BARANGAY_FLAT if None)

        Returns:
            GeoDataFrame with geometry and barangay information
        """
        if barangay_data is None:
            barangay_data = BARANGAY_FLAT

        # Create geometry column
        geometry = [Point(xy) for xy in zip(coordinates_data['lon'], coordinates_data['lat'])]

        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(coordinates_data, geometry=geometry, crs="EPSG:4326")

        # Add barangay information
        from barangay import search
        barangay_info = []

        for _, row in coordinates_data.iterrows():
            # Use reverse geocoding to get address components
            # This is simplified - in practice, use a reverse geocoding service
            search_string = f"{row.get('address', '')}"
            matches = search(search_string, n=1, threshold=70.0)

            if matches:
                barangay_info.append({
                    'barangay': matches[0]['barangay'],
                    'municipality': matches[0]['municipality_or_city'],
                    'province': matches[0]['province_or_huc'],
                    'psgc_id': matches[0]['psgc_id']
                })
            else:
                barangay_info.append({
                    'barangay': None,
                    'municipality': None,
                    'province': None,
                    'psgc_id': None
                })

        # Add barangay columns
        barangay_df = pd.DataFrame(barangay_info)
        gdf = pd.concat([gdf.reset_index(drop=True), barangay_df], axis=1)

        return gdf

    # Example usage
    coordinates_df = pd.DataFrame({
        'name': ['Location 1', 'Location 2', 'Location 3'],
        'lat': [14.5995, 14.6042, 14.6091],
        'lon': [120.9842, 120.9890, 120.9938],
        'address': ['Manila', 'Manila', 'Manila']
    })

    gdf = create_geodataframe(coordinates_df)
    print(gdf[['name', 'barangay', 'municipality', 'geometry']])

Spatial Analysis with Barangay Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perform spatial analysis using barangay boundaries:

.. code-block:: python

    import geopandas as gpd
    import matplotlib.pyplot as plt
    from barangay import BARANGAY_FLAT

    def analyze_barangay_distribution(
        points_gdf: gpd.GeoDataFrame,
        barangay_boundaries: gpd.GeoDataFrame = None
    ) -> pd.DataFrame:
        """Analyze point distribution by barangay.

        Args:
            points_gdf: GeoDataFrame with point geometries
            barangay_boundaries: GeoDataFrame with barangay polygons

        Returns:
            DataFrame with point counts by barangay
        """
        if barangay_boundaries is None:
            # This is a placeholder - in practice, you would load
            # actual barangay boundary data from a shapefile or GeoJSON
            raise ValueError("Barangay boundaries data required")

        # Spatial join to find which barangay each point belongs to
        points_with_barangay = gpd.sjoin(
            points_gdf,
            barangay_boundaries,
            how='left',
            predicate='within'
        )

        # Count points by barangay
        counts = points_with_barangay.groupby('barangay_name').size().reset_index(name='point_count')

        return counts

    # Example usage (requires actual boundary data)
    # points_gdf = gpd.GeoDataFrame(...)
    # barangay_boundaries = gpd.read_file('barangay_boundaries.geojson')
    # distribution = analyze_barangay_distribution(points_gdf, barangay_boundaries)

Complete GeocodingHelper Class
------------------------------

Here's a comprehensive GeocodingHelper class with various features:

.. code-block:: python

    import requests
    import pandas as pd
    from typing import Optional, List, Dict, Any
    from barangay import search, create_fuzz_base

    class GeocodingHelper:
        """Comprehensive geocoding helper for Philippine addresses.

        This class provides methods for forward and reverse geocoding,
        with optional barangay validation and batch processing support.

        Attributes:
            nominatim_url: Base URL for Nominatim API
            nominatim_email: Email for Nominatim API (required)
            fuzz_base: Pre-computed fuzzy base for efficient searches
        """

        def __init__(
            self,
            nominatim_email: str,
            nominatim_url: str = "https://nominatim.openstreetmap.org"
        ):
            """Initialize the GeocodingHelper.

            Args:
                nominatim_email: Email address for Nominatim API (required)
                nominatim_url: Base URL for Nominatim API
            """
            self.nominatim_url = nominatim_url
            self.nominatim_email = nominatim_email
            self.fuzz_base = create_fuzz_base()

        def geocode(
            self,
            address: str,
            validate_barangay: bool = True,
            threshold: float = 80.0,
            return_full_response: bool = False
        ) -> Dict[str, Any]:
            """Geocode an address with optional barangay validation.

            Args:
                address: Address string to geocode
                validate_barangay: Whether to validate barangay
                threshold: Minimum similarity score for validation
                return_full_response: Whether to return full API response

            Returns:
                Dictionary with geocoding results
            """
            result = {
                'original_address': address,
                'is_valid_barangay': None,
                'barangay_match': None,
                'coordinates': None,
                'formatted_address': None
            }

            # Validate barangay if requested
            if validate_barangay:
                matches = search(
                    address,
                    n=1,
                    threshold=threshold,
                    fuzz_base=self.fuzz_base
                )
                if matches and matches[0]['max_score'] >= threshold:
                    result['is_valid_barangay'] = True
                    result['barangay_match'] = {
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    }
                else:
                    result['is_valid_barangay'] = False

            # Geocode using Nominatim
            params = {
                'q': address,
                'format': 'json',
                'limit': 1,
                'countrycodes': 'ph',
                'email': self.nominatim_email
            }

            try:
                response = requests.get(
                    f"{self.nominatim_url}/search",
                    params=params,
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()

                if data:
                    result['coordinates'] = {
                        'latitude': float(data[0]['lat']),
                        'longitude': float(data[0]['lon'])
                    }
                    result['formatted_address'] = data[0].get('display_name')

                    if return_full_response:
                        result['full_response'] = data[0]
            except requests.RequestException as e:
                result['error'] = f"Geocoding failed: {str(e)}"

            return result

        def reverse_geocode(
            self,
            lat: float,
            lon: float,
            find_nearest_barangay: bool = True,
            threshold: float = 70.0
        ) -> Dict[str, Any]:
            """Reverse geocode coordinates to address.

            Args:
                lat: Latitude
                lon: Longitude
                find_nearest_barangay: Whether to find nearest barangay
                threshold: Minimum similarity score for barangay matching

            Returns:
                Dictionary with reverse geocoding results
            """
            result = {
                'coordinates': {'latitude': lat, 'longitude': lon},
                'address': None,
                'nearest_barangay': None
            }

            # Reverse geocode using Nominatim
            params = {
                'lat': lat,
                'lon': lon,
                'format': 'json',
                'email': self.nominatim_email
            }

            try:
                response = requests.get(
                    f"{self.nominatim_url}/reverse",
                    params=params,
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()

                if 'address' in data:
                    result['address'] = data['address']

                    # Find nearest barangay if requested
                    if find_nearest_barangay:
                        search_string = self._build_search_string(data['address'])
                        matches = search(
                            search_string,
                            n=1,
                            threshold=threshold,
                            fuzz_base=self.fuzz_base
                        )
                        if matches:
                            result['nearest_barangay'] = {
                                'barangay': matches[0]['barangay'],
                                'municipality': matches[0]['municipality_or_city'],
                                'province': matches[0]['province_or_huc'],
                                'psgc_id': matches[0]['psgc_id'],
                                'score': matches[0]['max_score']
                            }
            except requests.RequestException as e:
                result['error'] = f"Reverse geocoding failed: {str(e)}"

            return result

        def batch_geocode(
            self,
            addresses: List[str],
            validate_barangay: bool = True,
            show_progress: bool = False
        ) -> pd.DataFrame:
            """Geocode multiple addresses.

            Args:
                addresses: List of address strings to geocode
                validate_barangay: Whether to validate barangays
                show_progress: Whether to show progress bar

            Returns:
                DataFrame with geocoding results
            """
            results = []
            iterator = addresses
            if show_progress:
                try:
                    from tqdm import tqdm
                    iterator = tqdm(addresses, desc="Geocoding addresses")
                except ImportError:
                    pass

            for address in iterator:
                result = self.geocode(address, validate_barangay=validate_barangay)
                results.append(result)

            return pd.DataFrame(results)

        def _build_search_string(self, address_parts: dict) -> str:
            """Build search string from address components.

            Args:
                address_parts: Dictionary with address components from Nominatim

            Returns:
                Search string for barangay matching
            """
            parts = []
            if 'suburb' in address_parts:
                parts.append(address_parts['suburb'])
            if 'city' in address_parts or 'town' in address_parts:
                parts.append(address_parts.get('city', address_parts.get('town', '')))
            if 'state' in address_parts:
                parts.append(address_parts['state'])
            return ', '.join(parts)

        def calculate_distance(
            self,
            lat1: float,
            lon1: float,
            lat2: float,
            lon2: float
        ) -> float:
            """Calculate Haversine distance between two coordinates.

            Args:
                lat1, lon1: First point coordinates
                lat2, lon2: Second point coordinates

            Returns:
                Distance in kilometers
            """
            from math import radians, cos, sin, asin, sqrt

            # Convert decimal degrees to radians
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

            # Haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))
            r = 6371  # Radius of earth in kilometers
            return c * r

    # Example usage
    if __name__ == '__main__':
        geocoder = GeocodingHelper(nominatim_email="your-email@example.com")

        # Forward geocoding
        result = geocoder.geocode("Tongmageng, Tawi-Tawi")
        print(f"Coordinates: {result['coordinates']}")

        # Reverse geocoding
        result = geocoder.reverse_geocode(14.5995, 120.9842)
        print(f"Address: {result['address']}")

        # Batch geocoding
        addresses = ["Tongmageng, Tawi-Tawi", "Rosario, Batangas"]
        df = geocoder.batch_geocode(addresses, show_progress=True)
        print(df)

Integration with External Libraries
-----------------------------------

Using Google Maps Geocoding API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import googlemaps
    from barangay import search

    class GoogleMapsGeocoder:
        """Geocoding helper using Google Maps API."""

        def __init__(self, api_key: str):
            """Initialize with Google Maps API key.

            Args:
                api_key: Google Maps API key
            """
            self.client = googlemaps.Client(key=api_key)

        def geocode_with_validation(
            self,
            address: str,
            validate_barangay: bool = True,
            threshold: float = 80.0
        ) -> dict:
            """Geocode address with barangay validation.

            Args:
                address: Address string to geocode
                validate_barangay: Whether to validate barangay
                threshold: Minimum similarity score for validation

            Returns:
                Dictionary with geocoding results
            """
            result = {
                'original_address': address,
                'is_valid_barangay': None,
                'barangay_match': None,
                'coordinates': None,
                'formatted_address': None
            }

            # Validate barangay if requested
            if validate_barangay:
                matches = search(address, n=1, threshold=threshold)
                if matches and matches[0]['max_score'] >= threshold:
                    result['is_valid_barangay'] = True
                    result['barangay_match'] = {
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    }
                else:
                    result['is_valid_barangay'] = False

            # Geocode using Google Maps
            try:
                geocode_result = self.client.geocode(
                    address,
                    components={'country': 'PH'}
                )

                if geocode_result:
                    location = geocode_result[0]['geometry']['location']
                    result['coordinates'] = {
                        'latitude': location['lat'],
                        'longitude': location['lng']
                    }
                    result['formatted_address'] = geocode_result[0]['formatted_address']
            except Exception as e:
                result['error'] = f"Geocoding failed: {str(e)}"

            return result

Using Mapbox Geocoding API
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import requests
    from barangay import search

    class MapboxGeocoder:
        """Geocoding helper using Mapbox API."""

        def __init__(self, access_token: str):
            """Initialize with Mapbox access token.

            Args:
                access_token: Mapbox access token
            """
            self.access_token = access_token
            self.base_url = "https://api.mapbox.com/geocoding/v5/mapbox.places"

        def geocode_with_validation(
            self,
            address: str,
            validate_barangay: bool = True,
            threshold: float = 80.0
        ) -> dict:
            """Geocode address with barangay validation.

            Args:
                address: Address string to geocode
                validate_barangay: Whether to validate barangay
                threshold: Minimum similarity score for validation

            Returns:
                Dictionary with geocoding results
            """
            result = {
                'original_address': address,
                'is_valid_barangay': None,
                'barangay_match': None,
                'coordinates': None,
                'formatted_address': None
            }

            # Validate barangay if requested
            if validate_barangay:
                matches = search(address, n=1, threshold=threshold)
                if matches and matches[0]['max_score'] >= threshold:
                    result['is_valid_barangay'] = True
                    result['barangay_match'] = {
                        'barangay': matches[0]['barangay'],
                        'municipality': matches[0]['municipality_or_city'],
                        'province': matches[0]['province_or_huc'],
                        'psgc_id': matches[0]['psgc_id'],
                        'score': matches[0]['max_score']
                    }
                else:
                    result['is_valid_barangay'] = False

            # Geocode using Mapbox
            params = {
                'access_token': self.access_token,
                'autocomplete': 'false',
                'country': 'PH',
                'limit': 1
            }

            try:
                response = requests.get(
                    f"{self.base_url}/{address}.json",
                    params=params,
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()

                if data['features']:
                    coords = data['features'][0]['geometry']['coordinates']
                    result['coordinates'] = {
                        'latitude': coords[1],
                        'longitude': coords[0]
                    }
                    result['formatted_address'] = data['features'][0]['place_name']
            except requests.RequestException as e:
                result['error'] = f"Geocoding failed: {str(e)}"

            return result

Performance Tips
----------------

1. **Use rate limiting**: Geocoding APIs have rate limits. Implement delays between requests:

.. code-block:: python

    import time

    def batch_geocode_with_rate_limit(
        addresses: list[str],
        geocoding_helper: GeocodingHelper,
        requests_per_second: int = 1
    ) -> pd.DataFrame:
        """Batch geocode with rate limiting."""
        delay = 1.0 / requests_per_second
        results = []

        for address in addresses:
            result = geocoding_helper.geocode(address)
            results.append(result)
            time.sleep(delay)

        return pd.DataFrame(results)

2. **Cache geocoding results**: Store geocoding results to avoid redundant API calls:

.. code-block:: python

    import hashlib
    import json
    from pathlib import Path

    class CachedGeocoder(GeocodingHelper):
        """Geocoding helper with caching."""

        def __init__(self, nominatim_email: str, cache_dir: str = None):
            super().__init__(nominatim_email)
            self.cache_dir = Path(cache_dir) if cache_dir else Path.home() / '.geocode_cache'
            self.cache_dir.mkdir(parents=True, exist_ok=True)

        def _get_cache_key(self, address: str) -> str:
            """Generate cache key for address."""
            return hashlib.md5(address.encode()).hexdigest()

        def geocode(self, address: str, **kwargs) -> dict:
            """Geocode with caching."""
            cache_key = self._get_cache_key(address)
            cache_file = self.cache_dir / f"{cache_key}.json"

            # Try to load from cache
            if cache_file.exists():
                with open(cache_file) as f:
                    return json.load(f)

            # Geocode and cache result
            result = super().geocode(address, **kwargs)
            with open(cache_file, 'w') as f:
                json.dump(result, f)

            return result

3. **Batch when possible**: Use batch geocoding APIs when available to reduce API calls.

See Also
--------

* :ref:`api-search` - Search function API reference
* :ref:`examples-data-analysis` - Data analysis examples
* :ref:`examples-batch-processing` - Batch processing examples
* :ref:`advanced-caching` - Caching mechanisms