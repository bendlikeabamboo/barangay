###############
 Models Module
##############

The models module provides Pydantic models for representing Philippine
barangay data with type validation and serialization support.


 Overview
*********

The BarangayModel is a Pydantic model that provides type validation and
serialization for Philippine barangay data. It includes the barangay
name, its administrative divisions (province/HUC and municipality/city),
and the Philippine Standard Geographic Code (PSGC).

Administrative Divisions
========================

The Philippines has a hierarchical administrative structure:

-  **Barangay**: The smallest administrative division, often referred to
   as a village or neighborhood. There are over 42,000 barangays in the
   Philippines.

-  **Province or Highly Urbanized City (HUC)**: The primary
   administrative division. HUCs are cities that are independent from
   any province and have their own legislative districts.

-  **Municipality or City**: The intermediate administrative division
   between the province/HUC and the barangay.

-  **Philippine Standard Geographic Code (PSGC)**: A unique identifier
   assigned by the Philippine Statistics Authority to each geographic
   area in the country. The code is typically 9 digits long and follows
   a hierarchical structure.


 API Reference
**************

.. autoclass:: barangay.models.BarangayModel
   :members:
   :undoc-members:
   :show-inheritance:


 Model Fields
*************

The BarangayModel includes the following fields:

.. py:attribute:: barangay
   :type: str

   Name of the barangay. This is the smallest administrative division in the
   Philippines, often referred to as a village or neighborhood.

.. py:attribute:: province_or_huc
   :type: str

   Name of the province or Highly Urbanized City (HUC). In the Philippines, HUCs
   are cities that are independent from any province and have their own legislative
   districts.

.. py:attribute:: municipality_or_city
   :type: str

   Name of the municipality or city. This is the intermediate administrative
   division between the province/HUC and the barangay.

.. py:attribute:: psgc_id
   :type: str

   Philippine Standard Geographic Code. This is a unique identifier assigned by
   the Philippine Statistics Authority to each geographic area in the country.
   The code is typically 9 digits long and follows a hierarchical structure.


 Examples
*********

Creating a BarangayModel Instance
=================================

.. code:: python

   from barangay import BarangayModel

   # Create a BarangayModel instance
   barangay = BarangayModel(
       barangay="Tongmageng",
       province_or_huc="Tawi-Tawi",
       municipality_or_city="Sitangkai",
       psgc_id="157501001",
   )

   # Access fields
   print(barangay.barangay)  # Tongmageng
   print(barangay.province_or_huc)  # Tawi-Tawi

Converting to Dictionary
========================

.. code:: python

   from barangay import BarangayModel

   # Create a BarangayModel instance
   barangay = BarangayModel(
       barangay="Barangay 1",
       province_or_huc="Province A",
       municipality_or_city="City 1",
       psgc_id="010010001",
   )

   # Convert to dictionary
   data = barangay.model_dump()
   print(data)
   # {'barangay': 'Barangay 1', 'province_or_huc': 'Province A', ...}

JSON Serialization
==================

.. code:: python

   from barangay import BarangayModel

   # Create a BarangayModel instance
   barangay = BarangayModel(
       barangay="Barangay 1",
       province_or_huc="Province A",
       municipality_or_city="City 1",
       psgc_id="010010001",
   )

   # Serialize to JSON
   json_str = barangay.model_dump_json()
   print(json_str)
   # {"barangay":"Barangay 1","province_or_huc":"Province A",...}

Creating from Dictionary
========================

.. code:: python

   from barangay import BarangayModel

   # Create from dictionary
   data = {
       "barangay": "Tongmageng",
       "province_or_huc": "Tawi-Tawi",
       "municipality_or_city": "Sitangkai",
       "psgc_id": "157501001",
   }

   barangay = BarangayModel(**data)
   print(barangay.barangay)  # Tongmageng

Validation
==========

.. code:: python

   from barangay import BarangayModel
   from pydantic import ValidationError

   # Valid data
   barangay = BarangayModel(
       barangay="Barangay 1",
       province_or_huc="Province A",
       municipality_or_city="City 1",
       psgc_id="010010001",
   )

   # Invalid data (missing field)
   try:
       barangay = BarangayModel(
           barangay="Barangay 1",
           province_or_huc="Province A",
           # Missing municipality_or_city
           psgc_id="010010001",
       )
   except ValidationError as e:
       print(e)

Using with Search Results
=========================

.. code:: python

   from barangay import search, BarangayModel

   # Search for a barangay
   results = search("Tongmageng")

   # Convert search results to BarangayModel
   if results:
       barangay = BarangayModel(
           barangay=results[0]["barangay"],
           province_or_huc=results[0]["province_or_huc"],
           municipality_or_city=results[0]["municipality_or_city"],
           psgc_id=results[0]["psgc_id"],
       )
       print(barangay)


 See Also
*********

-  :mod:`pydantic` - Pydantic documentation for BaseModel
-  :mod:`barangay.search` - Search functionality module
-  :mod:`barangay.data` - Data loading module