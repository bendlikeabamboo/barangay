Data Models Overview
====================

The barangay package provides three different data models to suit various use cases. Each model has its own structure and is optimized for specific tasks.

Overview of Data Models
-----------------------

.. list-table:: Data Model Comparison
   :widths: 25 25 50
   :header-rows: 1

   * - Model
     - Best For
     - Structure
   * - BARANGAY
     - Simple lookups, hierarchical access
     - Nested dictionary (region → city/municipality → barangay)
   * - BARANGAY_EXTENDED
     - Complex hierarchies, rich metadata
     - Recursive with additional fields (code, level, population, etc.)
   * - BARANGAY_FLAT
     - Search, filtering, DataFrame operations
     - Flat list with parent references

When to Use Each Model
----------------------

BARANGAY (Basic Model)
~~~~~~~~~~~~~~~~~~~~~~

Use BARANGAY when you need:

* Simple, hierarchical access to barangay data
* Quick lookups by region, city/municipality, and barangay
* Memory-efficient storage for basic information
* A straightforward structure for navigation

Example use cases:

* Building a dropdown selector for addresses
* Displaying geographic hierarchies
* Simple data validation

BARANGAY_EXTENDED (Extended Model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use BARANGAY_EXTENDED when you need:

* Rich metadata about each administrative level
* Information about codes, levels, and other attributes
* Detailed hierarchical relationships
* Complete information for complex applications

Example use cases:

* Geographic information systems (GIS)
* Data analysis with additional attributes
* Applications requiring detailed administrative information

BARANGAY_FLAT (Flat Model)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use BARANGAY_FLAT when you need:

* Easy filtering and searching
* Integration with pandas DataFrame operations
* Batch processing of barangay data
* Parent references for navigation

Example use cases:

* Data analysis and visualization
* Machine learning feature engineering
* Exporting data to other formats

Quick Comparison Table
----------------------

.. list-table:: Feature Comparison
   :widths: 20 20 20 20
   :header-rows: 1

   * - Feature
     - BARANGAY
     - BARANGAY_EXTENDED
     - BARANGAY_FLAT
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

Basic Examples
--------------

Using BARANGAY (Basic Model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access data hierarchically:

.. code-block:: python

  from barangay import BARANGAY

  # Get all regions
  regions = list(BARANGAY.keys())
  print(f"Regions: {regions[:3]}")

  # Get cities/municipalities in a region
  ncr_cities = list(BARANGAY["National Capital Region (NCR)"].keys())
  print(f"NCR Cities: {ncr_cities[:3]}")

  # Get barangays in a city
  manila_municipalities = list(BARANGAY["National Capital Region (NCR)"]["City of Manila"].keys())
  print(f"Manila Municipalities: {manila_municipalities[:3]}")

  binondo_barangays = list(BARANGAY["National Capital Region (NCR)"]["City of Manila"]["Binondo"])
  print(f"Binondo Barangays: {binondo_barangays[:3]}")

Output:

.. code-block:: text

  Regions: ['Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)', 'Cordillera Administrative Region (CAR)', 'MIMAROPA Region']
  NCR Cities: ['City of Manila', 'City of Caloocan', 'City of Las Piñas']
  Manila Municipalities: ['Binondo', 'Ermita', 'Intramuros']
  Binondo Barangays: ['Barangay 291', 'Barangay 290', 'Barangay 293']

Using BARANGAY_EXTENDED (Extended Model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access rich metadata:

.. code-block:: python

  from barangay import BARANGAY_EXTENDED
  import random

  # Get region hierarchical tree
  regions = [x for x in BARANGAY_EXTENDED["components"]]
  region_names = [x["name"] for x in BARANGAY_EXTENDED["components"]]
  print(f"Sample regions in the Philippines: {random.sample(region_names, k=3)}")

  # Get region hierarchical tree
  davao_region = [x for x in regions if x["name"] == "Region XI (Davao Region)"][0]
  davao_provinces_and_hucs = [x for x in davao_region["components"]]
  davao_provinces_and_hucs_names = [x["name"] for x in davao_region["components"]]
  print(
      f"Sample provinces and HUCs in Davao Region: {random.sample(davao_provinces_and_hucs_names, k=3)}"
  )

  # Get HUC hierarchical tree
  print("\nSample hierarchy for highly urbanized cities (HUCs):")
  davao_city = [x for x in davao_provinces_and_hucs if x["name"] == "City of Davao"][0]
  davao_city_barangays = [x for x in davao_city["components"]]
  davao_city_barangay_names = [x["name"] for x in davao_city["components"]]
  print(f"Sample Davao City barangays: {random.sample(davao_city_barangay_names, k=3)}")

  # Get provincial hierarchical tree
  print("\nSample for provinces:")
  davao_oriental_province = [x for x in davao_provinces_and_hucs if x["name"] == "Davao Occidental"][0]
  davao_oriental_municipalities = [x for x in davao_oriental_province["components"]]
  davao_oriental_municipalities_names = [x["name"] for x in davao_oriental_province["components"]]
  print(f"Sample Davao Oriental municipalities: {random.sample(davao_oriental_municipalities_names, k=3)}")

  sarangani_province = [x for x in davao_oriental_municipalities if x["name"] == "Sarangani"][0]
  sarangani_barangays = [x for x in sarangani_province["components"]]
  sarangani_barangay_names = [x["name"] for x in sarangani_province["components"]]
  print(f"Sample Sarangani barangays: {random.sample(sarangani_barangay_names, k=3)}")


Output:

.. code-block:: text

  Sample regions in the Philippines: ['Region XII (SOCCSKSARGEN)', 'Region VIII (Eastern Visayas)', 'Region XI (Davao Region)']
  Sample provinces and HUCs in Davao Region: ['Davao Oriental', 'Davao del Norte', 'Davao del Sur']

  Sample hierarchy for highly urbanized cities (HUCs):
  Sample Davao City barangays: ['Barangay 15-B', 'Vicente Hizon Sr.', 'Barangay 35-D']

  Sample for provinces:
  Sample Davao Oriental municipalities: ['Malita', 'Sarangani', 'Don Marcelino']
  Sample Sarangani barangays: ['Konel', 'Batuganding', 'Camalig']

Using BARANGAY_FLAT (Flat Model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Work with pandas DataFrame:

.. code-block:: python

  from barangay import BARANGAY_FLAT

  # Find a specific barangay
  brgy = [loc for loc in BARANGAY_FLAT if loc["name"] == "Marayos"][0]

  # Trace hierarchy using parent_psgc_id
  parent = [loc for loc in BARANGAY_FLAT
          if loc["psgc_id"] == brgy["parent_psgc_id"]][0]

  print(f"Parent municipality of Brgy. Marayos: {parent}")

Output:

.. code-block:: text

  Parent municipality of Brgy. Marayos: {'name': 'Pinamalayan', 'type': 'municipality', 'psgc_id': '1705209000', 'parent_psgc_id': '1705200000', 'nicknames': None}


Data Model Selection Guide
--------------------------

.. list-table:: Quick Decision Guide
   :widths: 50 50
   :header-rows: 1

   * - If you want to...
     - Use...
   * - Access data hierarchically
     - BARANGAY
   * - Get rich metadata about each level
     - BARANGAY_EXTENDED
   * - Work with pandas DataFrame
     - BARANGAY_FLAT
   * - Filter and search easily
     - BARANGAY_FLAT
   * - Build dropdown selectors
     - BARANGAY
   * - Perform data analysis
     - BARANGAY_FLAT
   * - Use minimal memory
     - BARANGAY or BARANGAY_FLAT
   * - Get complete information
     - BARANGAY_EXTENDED

Memory and Performance Considerations
-------------------------------------

Memory Usage
~~~~~~~~~~~~

* **BARANGAY**: Most memory-efficient for hierarchical access
* **BARANGAY_EXTENDED**: Higher memory usage due to rich metadata
* **BARANGAY_FLAT**: Efficient for DataFrame operations, moderate memory

Access Speed
~~~~~~~~~~~~

* **BARANGAY**: Fast for hierarchical lookups (O(1) for direct access)
* **BARANGAY_EXTENDED**: Similar to BARANGAY, with additional attribute access
* **BARANGAY_FLAT**: Fast for filtering and searching with pandas operations

.. tip:: For most use cases, the performance difference between models is negligible. Choose the model based on your access pattern and data structure needs.


Next Steps
----------

Now that you understand the different data models, explore these topics:

* :doc:`../user_guide/data_models` - Detailed guide to each data model
* :doc:`../user_guide/search` - Learn about fuzzy search features
* :doc:`../user_guide/historical_data` - How to access historical data

For more detailed information about each model, see the :doc:`../user_guide/data_models` guide.