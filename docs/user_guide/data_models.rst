Data Models Guide
=================

This guide provides detailed information about the three data models available in the barangay package: BARANGAY (basic), BARANGAY_EXTENDED (extended), and BARANGAY_FLAT (flat).

Overview of Data Models
-----------------------

The barangay package provides three data models to suit different use cases:

* **BARANGAY** - Basic nested dictionary structure
* **BARANGAY_EXTENDED** - Extended recursive structure with rich metadata
* **BARANGAY_FLAT** - Flat list with parent references

Each model has its own strengths and is optimized for specific tasks.

Comparison Table
~~~~~~~~~~~~~~~~

.. list-table:: Data Model Comparison
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Feature
     - BARANGAY
     - BARANGAY_EXTENDED
     - BARANGAY_FLAT
   * - Structure
     - Nested dict
     - Recursive dict
     - Flat list
   * - Hierarchical Access
     - ✓
     - ✓
     - ✗
   * - Rich Metadata
     - ✗
     - ✓
     - ✓
   * - DataFrame Compatible
     - ✗
     - ✗
     - ✓
   * - Memory Efficient
     - ✓
     - ✗
     - ✓
   * - Easy Filtering
     - ✗
     - ✗
     - ✓
   * - Best For
     - Simple lookups
     - Complex hierarchies
     - Data analysis

BARANGAY (Basic Model)
----------------------

Structure
~~~~~~~~~

BARANGAY is a nested dictionary with three levels:


region → municipality_or_city → barangay
````````````````````````````````````````

Each level contains:

* **region**: Region name (e.g., "National Capital Region (NCR)")
* **municipality_or_city**: City or municipality name (e.g., "City of Manila")
* **barangay**: Barangay name (e.g., "Barangay 128")

Data Structure Diagram
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   BARANGAY
   ├── "National Capital Region (NCR)"
   │   ├── "City of Manila"
   │   │   ├── "Barangay 128"
   │   │   ├── "Barangay 129"
   │   │   └── ...
   │   ├── "Quezon City"
   │   │   ├── "Barangay 1"
   │   │   ├── "Barangay 2"
   │   │   └── ...
   │   └── ...
   ├── "Cordillera Administrative Region (CAR)"
   │   └── ...
   └── ...

Access Patterns
~~~~~~~~~~~~~~~

Access data hierarchically:

.. code-block:: python

   from barangay import BARANGAY

   # Get all regions
   regions = list(BARANGAY.keys())
   print(f"Total regions: {len(regions)}")

   # Get cities/municipalities in a region
   ncr = BARANGAY["National Capital Region (NCR)"]
   ncr_cities = list(ncr.keys())
   print(f"NCR cities: {len(ncr_cities)}")

   # Get barangays in a city
   manila = ncr["City of Manila"]
   manila_barangays = list(manila.keys())
   print(f"Manila barangays: {len(manila_barangays)}")

   # Access a specific barangay
   barangay_128 = manila["Barangay 128"]
   print(f"Barangay 128: {barangay_128}")

Use Cases
~~~~~~~~~

* Building dropdown selectors for forms
* Displaying geographic hierarchies
* Simple data validation
* Quick lookups by region, city, or barangay
* Memory-constrained applications

Limitations
~~~~~~~~~~~

* No additional metadata (codes, levels, etc.)
* Not directly compatible with pandas DataFrame
* Limited filtering capabilities
* No parent references for navigation

Example: Building a Dropdown Selector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import BARANGAY

   def build_region_options():
       """Build options for region dropdown."""
       return [{"value": region, "label": region} for region in BARANGAY.keys()]

   def build_city_options(region):
       """Build options for city dropdown based on selected region."""
       if region not in BARANGAY:
           return []
       return [{"value": city, "label": city} for city in BARANGAY[region].keys()]

   def build_barangay_options(region, city):
       """Build options for barangay dropdown based on selected region and city."""
       if region not in BARANGAY or city not in BARANGAY[region]:
           return []
       return [{"value": brgy, "label": brgy} for brgy in BARANGAY[region][city].keys()]

   # Example usage
   region_options = build_region_options()
   print(f"Region options: {region_options[:3]}")

   city_options = build_city_options("National Capital Region (NCR)")
   print(f"City options: {city_options[:3]}")

   barangay_options = build_barangay_options("National Capital Region (NCR)", "City of Manila")
   print(f"Barangay options: {barangay_options[:3]}")

BARANGAY_EXTENDED (Extended Model)
----------------------------------

Structure
~~~~~~~~~

BARANGAY_EXTENDED is a recursive dictionary structure with rich metadata. Each administrative level contains:

* **name**: The name of the administrative unit
* **code**: The PSGC code
* **level**: The administrative level (region, province, city, municipality, barangay)
* **children**: A dictionary of child administrative units

Data Structure Diagram
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   BARANGAY_EXTENDED
   ├── "National Capital Region (NCR)"
   │   ├── name: "National Capital Region (NCR)"
   │   ├── code: 13
   │   ├── level: "region"
   │   └── children
   │       ├── "City of Manila"
   │       │   ├── name: "City of Manila"
   │       │   ├── code: 137501000
   │       │   ├── level: "city"
   │       │   └── children
   │       │       ├── "Barangay 128"
   │       │       │   ├── name: "Barangay 128"
   │       │       │   ├── code: 137501128
   │       │       │   ├── level: "barangay"
   │       │       │   └── children: {}
   │       │       └── ...
   │       └── ...
   └── ...

Access Patterns
~~~~~~~~~~~~~~~

Access data with metadata:

.. code-block:: python

   from barangay import BARANGAY_EXTENDED

   # Get region information
   ncr = BARANGAY_EXTENDED["National Capital Region (NCR)"]
   print(f"Region: {ncr['name']}")
   print(f"Code: {ncr['code']}")
   print(f"Level: {ncr['level']}")

   # Get city information
   manila = ncr["children"]["City of Manila"]
   print(f"\nCity: {manila['name']}")
   print(f"Code: {manila['code']}")
   print(f"Level: {manila['level']}")

   # Get barangay information
   barangay_128 = manila["children"]["Barangay 128"]
   print(f"\nBarangay: {barangay_128['name']}")
   print(f"Code: {barangay_128['code']}")
   print(f"Level: {barangay_128['level']}")

Use Cases
~~~~~~~~~

* Geographic Information Systems (GIS)
* Applications requiring detailed administrative information
* Data analysis with additional attributes
* Building comprehensive address forms
* Applications that need PSGC codes

Handling Complex Hierarchies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The extended model handles complex hierarchies with multiple levels:

.. code-block:: python

   from barangay import BARANGAY_EXTENDED

   def traverse_hierarchy(data, level=0):
       """Traverse the hierarchical structure."""
       indent = "  " * level
       print(f"{indent}{data['name']} ({data['level']}) - Code: {data['code']}")

       for child_name, child_data in data.get("children", {}).items():
           traverse_hierarchy(child_data, level + 1)

   # Example: Traverse NCR hierarchy
   ncr = BARANGAY_EXTENDED["National Capital Region (NCR)"]
   traverse_hierarchy(ncr)

Example: Building a Comprehensive Address Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import BARANGAY_EXTENDED

   def get_region_info():
       """Get all regions with codes."""
       return [
           {
               "name": region_data["name"],
               "code": region_data["code"],
               "level": region_data["level"]
           }
           for region_data in BARANGAY_EXTENDED.values()
       ]

   def get_city_info(region_name):
       """Get all cities/municipalities in a region with codes."""
       if region_name not in BARANGAY_EXTENDED:
           return []

       region = BARANGAY_EXTENDED[region_name]
       return [
           {
               "name": city_data["name"],
               "code": city_data["code"],
               "level": city_data["level"]
           }
           for city_data in region["children"].values()
       ]

   def get_barangay_info(region_name, city_name):
       """Get all barangays in a city with codes."""
       if region_name not in BARANGAY_EXTENDED:
           return []

       region = BARANGAY_EXTENDED[region_name]
       if city_name not in region["children"]:
           return []

       city = region["children"][city_name]
       return [
           {
               "name": barangay_data["name"],
               "code": barangay_data["code"],
               "level": barangay_data["level"]
           }
           for barangay_data in city["children"].values()
       ]

   # Example usage
   regions = get_region_info()
   print(f"Total regions: {len(regions)}")
   print(f"First region: {regions[0]}")

   cities = get_city_info("National Capital Region (NCR)")
   print(f"\nNCR cities: {len(cities)}")
   print(f"First city: {cities[0]}")

   barangays = get_barangay_info("National Capital Region (NCR)", "City of Manila")
   print(f"\nManila barangays: {len(barangays)}")
   print(f"First barangay: {barangays[0]}")

BARANGAY_FLAT (Flat Model)
--------------------------

Structure
~~~~~~~~~

BARANGAY_FLAT is a flat list of dictionaries, each representing a barangay with parent references:

* **barangay**: Barangay name
* **municipality_or_city**: City or municipality name
* **province_or_huc**: Province or Highly Urbanized City name
* **region**: Region name
* **psgc_id**: Philippine Standard Geographic Code

Data Structure Diagram
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   BARANGAY_FLAT
   ├── [
   │   {
   │       "barangay": "Barangay 128",
   │       "municipality_or_city": "City of Manila",
   │       "province_or_huc": "National Capital Region (NCR)",
   │       "region": "National Capital Region (NCR)",
   │       "psgc_id": "137501128"
   │   },
   │   {
   │       "barangay": "Barangay 129",
   │       "municipality_or_city": "City of Manila",
   │       "province_or_huc": "National Capital Region (NCR)",
   │       "region": "National Capital Region (NCR)",
   │       "psgc_id": "137501129"
   │   },
   │   ...
   │ ]

Access Patterns
~~~~~~~~~~~~~~~

Convert to pandas DataFrame for easy manipulation:

.. code-block:: python

   import pandas as pd
   from barangay import BARANGAY_FLAT

   # Convert to DataFrame
   df = pd.DataFrame(BARANGAY_FLAT)

   # Display first few rows
   print(df.head())

   # Get basic statistics
   print(f"\nTotal barangays: {len(df)}")
   print(f"Total regions: {df['region'].nunique()}")
   print(f"Total cities: {df['municipality_or_city'].nunique()}")

Use Cases
~~~~~~~~~

* Data analysis and visualization
* Machine learning feature engineering
* Exporting data to other formats (CSV, Excel, etc.)
* Batch processing
* Filtering and searching with pandas

DataFrame Integration
~~~~~~~~~~~~~~~~~~~~~

The flat model is designed for seamless pandas integration:

.. code-block:: python

   import pandas as pd
   from barangay import BARANGAY_FLAT

   # Convert to DataFrame
   df = pd.DataFrame(BARANGAY_FLAT)

   # Filter by region
   ncr_df = df[df['region'] == 'National Capital Region (NCR)']
   print(f"NCR barangays: {len(ncr_df)}")

   # Filter by city
   manila_df = df[df['municipality_or_city'] == 'City of Manila']
   print(f"Manila barangays: {len(manila_df)}")

   # Filter by barangay name pattern
   barangay_1xx = df[df['barangay'].str.startswith('Barangay 1')]
   print(f"Barangays starting with 'Barangay 1': {len(barangay_1xx)}")

   # Group by region and count
   region_counts = df.groupby('region').size().sort_values(ascending=False)
   print(f"\nTop 5 regions by barangay count:")
   print(region_counts.head())

Example: Data Analysis
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pandas as pd
   from barangay import BARANGAY_FLAT

   # Convert to DataFrame
   df = pd.DataFrame(BARANGAY_FLAT)

   # Analysis 1: Barangay count by region
   print("=== Barangay Count by Region ===")
   region_counts = df.groupby('region').size().sort_values(ascending=False)
   print(region_counts.head(10))

   # Analysis 2: Barangay count by city (top 10)
   print("\n=== Top 10 Cities by Barangay Count ===")
   city_counts = df.groupby('municipality_or_city').size().sort_values(ascending=False)
   print(city_counts.head(10))

   # Analysis 3: Average barangays per city by region
   print("\n=== Average Barangays per City by Region ===")
   avg_per_city = df.groupby('region').agg({
       'municipality_or_city': 'nunique',
       'barangay': 'count'
   })
   avg_per_city['avg_per_city'] = avg_per_city['barangay'] / avg_per_city['municipality_or_city']
   print(avg_per_city.head(10))

   # Analysis 4: Export to CSV
   print("\n=== Exporting to CSV ===")
   df.to_csv('philippine_barangays.csv', index=False)
   print("Exported to philippine_barangays.csv")

Data Model Selection Guide
--------------------------

Decision Tree
~~~~~~~~~~~~~

1. **Do you need to work with pandas DataFrame?**
   * Yes → Use BARANGAY_FLAT
   * No → Continue to step 2

2. **Do you need rich metadata (codes, levels, etc.)?**
   * Yes → Use BARANGAY_EXTENDED
   * No → Continue to step 3

3. **Do you need hierarchical access (region → city → barangay)?**
   * Yes → Use BARANGAY
   * No → Use BARANGAY_FLAT

Use Case Matrix
~~~~~~~~~~~~~~~

.. list-table:: Use Case Matrix
   :widths: 40 20 20 20
   :header-rows: 1

   * - Use Case
     - BARANGAY
     - BARANGAY_EXTENDED
     - BARANGAY_FLAT
   * - Dropdown selectors
     - ✓
     - ✓
     - ✗
   * - Data analysis
     - ✗
     - ✗
     - ✓
   * - GIS applications
     - ✗
     - ✓
     - ✓
   * - Simple lookups
     - ✓
     - ✓
     - ✓
   * - Export to CSV/Excel
     - ✗
     - ✗
     - ✓
   * - Memory-constrained apps
     - ✓
     - ✗
     - ✓
   * - Need PSGC codes
     - ✗
     - ✓
     - ✓

Working with Different Models
-----------------------------

Converting Between Models
~~~~~~~~~~~~~~~~~~~~~~~~~

You can convert between models as needed:

.. code-block:: python

   from barangay import BARANGAY, BARANGAY_EXTENDED, BARANGAY_FLAT
   import pandas as pd

   # Convert BARANGAY to BARANGAY_FLAT
   def basic_to_flat(basic_data):
       """Convert basic model to flat model."""
       flat_data = []
       for region, cities in basic_data.items():
           for city, barangays in cities.items():
               for barangay in barangays:
                   flat_data.append({
                       'barangay': barangay,
                       'municipality_or_city': city,
                       'province_or_huc': region,
                       'region': region,
                       'psgc_id': None  # Not available in basic model
                   })
       return flat_data

   # Convert BARANGAY_FLAT to BARANGAY
   def flat_to_basic(flat_data):
       """Convert flat model to basic model."""
       basic_data = {}
       for item in flat_data:
           region = item['region']
           city = item['municipality_or_city']
           barangay = item['barangay']

           if region not in basic_data:
               basic_data[region] = {}
           if city not in basic_data[region]:
               basic_data[region][city] = {}

           basic_data[region][city][barangay] = barangay

       return basic_data

Filtering and Searching
~~~~~~~~~~~~~~~~~~~~~~~

Each model supports different filtering approaches:

.. code-block:: python

   from barangay import BARANGAY, BARANGAY_FLAT
   import pandas as pd

   # Filtering with BARANGAY (basic)
   print("=== Filtering with BARANGAY ===")
   ncr = BARANGAY["National Capital Region (NCR)"]
   manila = ncr["City of Manila"]
   manila_barangays = list(manila.keys())
   print(f"Manila barangays: {len(manila_barangays)}")

   # Filtering with BARANGAY_FLAT (pandas)
   print("\n=== Filtering with BARANGAY_FLAT ===")
   df = pd.DataFrame(BARANGAY_FLAT)
   manila_df = df[df['municipality_or_city'] == 'City of Manila']
   print(f"Manila barangays: {len(manila_df)}")

Exporting Data
~~~~~~~~~~~~~~

Export to different formats:

.. code-block:: python

   from barangay import BARANGAY_FLAT
   import pandas as pd
   import json

   # Convert to DataFrame
   df = pd.DataFrame(BARANGAY_FLAT)

   # Export to CSV
   df.to_csv('philippine_barangays.csv', index=False)
   print("Exported to CSV")

   # Export to Excel
   df.to_excel('philippine_barangays.xlsx', index=False)
   print("Exported to Excel")

   # Export to JSON
   df.to_json('philippine_barangays.json', orient='records', indent=2)
   print("Exported to JSON")

Memory and Performance Considerations
-------------------------------------

Memory Usage
~~~~~~~~~~~~

.. list-table:: Memory Usage Comparison
   :widths: 30 35 35
   :header-rows: 1

   * - Model
     - Memory Usage
     - Notes
   * - BARANGAY
     - Low
     - Most efficient for hierarchical access
   * - BARANGAY_EXTENDED
     - High
     - Contains rich metadata for each level
   * - BARANGAY_FLAT
     - Medium
     - Efficient for DataFrame operations

Access Speed
~~~~~~~~~~~~

.. list-table:: Access Speed Comparison
   :widths: 30 35 35
   :header-rows: 1

   * - Operation
     - BARANGAY
     - BARANGAY_FLAT
   * - Hierarchical lookup
     - O(1) - Very fast
     - N/A
   * - Filter by region
     - O(n) - Slow
     - O(n) - Fast with pandas
   * - Filter by city
     - O(n) - Slow
     - O(n) - Fast with pandas
   * - Search by barangay
     - O(n) - Slow
     - O(n) - Fast with pandas

.. tip:: For most use cases, the performance difference between models is negligible. Choose the model based on your access pattern and data structure needs.

Optimization Tips
~~~~~~~~~~~~~~~~~

* **Use BARANGAY** for simple hierarchical lookups
* **Use BARANGAY_FLAT** for data analysis and filtering
* **Use BARANGAY_EXTENDED** only if you need rich metadata
* **Convert to DataFrame** only when needed (BARANGAY_FLAT is already a list)
* **Avoid unnecessary conversions** between models

Complete Example
----------------

Here's a complete example demonstrating all three models:

.. code-block:: python

   from barangay import BARANGAY, BARANGAY_EXTENDED, BARANGAY_FLAT
   import pandas as pd

   class BarangayDataManager:
       """Manage barangay data using all three models."""

       def __init__(self):
           self.basic = BARANGAY
           self.extended = BARANGAY_EXTENDED
           self.flat = pd.DataFrame(BARANGAY_FLAT)

       def get_barangay_info_basic(self, region, city, barangay):
           """Get barangay info using basic model."""
           if region not in self.basic:
               return None
           if city not in self.basic[region]:
               return None
           if barangay not in self.basic[region][city]:
               return None
           return {
               'barangay': barangay,
               'city': city,
               'region': region
           }

       def get_barangay_info_extended(self, region, city, barangay):
           """Get barangay info using extended model."""
           if region not in self.extended:
               return None
           if city not in self.extended[region]['children']:
               return None
           if barangay not in self.extended[region]['children'][city]['children']:
               return None

           region_data = self.extended[region]
           city_data = region_data['children'][city]
           barangay_data = city_data['children'][barangay]

           return {
               'barangay': barangay_data['name'],
               'barangay_code': barangay_data['code'],
               'city': city_data['name'],
               'city_code': city_data['code'],
               'region': region_data['name'],
               'region_code': region_data['code']
           }

       def get_barangay_info_flat(self, region, city, barangay):
           """Get barangay info using flat model."""
           result = self.flat[
               (self.flat['region'] == region) &
               (self.flat['municipality_or_city'] == city) &
               (self.flat['barangay'] == barangay)
           ]
           if len(result) == 0:
               return None
           row = result.iloc[0]
           return {
               'barangay': row['barangay'],
               'city': row['municipality_or_city'],
               'region': row['region'],
               'psgc_id': row['psgc_id']
           }

       def analyze_barangays(self):
           """Analyze barangay data using flat model."""
           print("=== Barangay Analysis ===")

           # Total counts
           print(f"Total barangays: {len(self.flat)}")
           print(f"Total regions: {self.flat['region'].nunique()}")
           print(f"Total cities: {self.flat['municipality_or_city'].nunique()}")

           # Top 5 regions by barangay count
           print("\n=== Top 5 Regions by Barangay Count ===")
           region_counts = self.flat.groupby('region').size().sort_values(ascending=False)
           print(region_counts.head(5))

           # Top 5 cities by barangay count
           print("\n=== Top 5 Cities by Barangay Count ===")
           city_counts = self.flat.groupby('municipality_or_city').size().sort_values(ascending=False)
           print(city_counts.head(5))

   # Usage
   manager = BarangayDataManager()

   # Get info using different models
   print("=== Using Basic Model ===")
   info_basic = manager.get_barangay_info_basic(
       "National Capital Region (NCR)",
       "City of Manila",
       "Barangay 128"
   )
   print(info_basic)

   print("\n=== Using Extended Model ===")
   info_extended = manager.get_barangay_info_extended(
       "National Capital Region (NCR)",
       "City of Manila",
       "Barangay 128"
   )
   print(info_extended)

   print("\n=== Using Flat Model ===")
   info_flat = manager.get_barangay_info_flat(
       "National Capital Region (NCR)",
       "City of Manila",
       "Barangay 128"
   )
   print(info_flat)

   # Analyze data
   manager.analyze_barangays()

Next Steps
----------

Now that you understand the data models, explore these topics:

* :doc:`search` - Learn about fuzzy search features
* :doc:`historical_data` - How to access historical data
* :doc:`configuration` - Configure the package for your needs
* :doc:`performance` - Performance optimization tips

For API reference, see :doc:`../api_reference/data`.