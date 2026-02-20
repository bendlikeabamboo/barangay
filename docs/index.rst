#####################
 Welcome to Barangay
#####################

Barangay is a Python package for Philippine geographic/administrative
data with fuzzy search capabilities.

.. image:: https://img.shields.io/pypi/v/barangay
   :target: https://pypi.org/project/barangay/
   :alt: PyPI - Version

.. image:: https://static.pepy.tech/badge/barangay
   :target: https://pepy.tech/projects/barangay
   :alt: Downloads - Pepy.Tech

.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT License

.. image:: https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml/badge.svg
   :target: https://github.com/bendlikeabamboo/barangay/actions/workflows/publish.yaml
   :alt: barangay build


Features
*********

-  **Fuzzy Search**: Fast, customizable matching for unstandardized
   addresses
-  **Multiple Data Models**: Basic (nested), Extended (recursive), and
   Flat (list) structures
-  **Historical Data**: Access previous PSGC releases by date
-  **Smart Caching**: Automatic caching for faster subsequent loads
-  **On-demand Download**: Download historical data from GitHub
   repository


Quick Start
************

Installation:

.. code:: bash

   pip install barangay


Basic usage:

.. code:: python

   from barangay import search

   results = search("Tongmageng, Tawi-Tawi")
   print(results[0]["barangay"])  # Tongmageng


Documentation Sections
***********************

.. toctree::
   :maxdepth: 2
   :caption: Quick Start

   quick_start/installation
   quick_start/first_search
   quick_start/data_models_overview

.. toctree::
   :maxdepth: 2
   :caption: User Guides

   user_guide/search
   user_guide/data_models
   user_guide/historical_data
   user_guide/configuration
   user_guide/performance
   user_guide/cli

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api_reference/search
   api_reference/fuzz
   api_reference/data_manager
   api_reference/models
   api_reference/config
   api_reference/date_resolver
   api_reference/data
   api_reference/downloader
   api_reference/utils
   api_reference/cli

.. toctree::
   :maxdepth: 2
   :caption: Advanced Topics

   advanced/fuzzy_matching
   advanced/caching
   advanced/error_handling
   advanced/custom_sanitizers

.. toctree::
   :maxdepth: 2
   :caption: Examples

   examples/address_validation
   examples/geocoding
   examples/data_analysis
   examples/batch_processing
   examples/cli

.. toctree::
   :maxdepth: 2
   :caption: Troubleshooting

   troubleshooting/common_errors
   troubleshooting/performance
   troubleshooting/faq

.. toctree::
   :maxdepth: 2
   :caption: Contributing

   contributing/index


Indices and tables
###################

-  :ref:`genindex`
-  :ref:`modindex`
-  :ref:`search`


Links
******

-  :doc:`ARCHITECTURE` - Documentation architecture
-  `GitHub Repository <https://github.com/bendlikeabamboo/barangay>`_
-  `Issue Tracker <https://github.com/bendlikeabamboo/barangay/issues>`_
-  `PyPI <https://pypi.org/project/barangay/>`_

Documentation Status
*********************

.. list-table:: Documentation Completeness
   :widths: 25 25 25 25
   :header-rows: 1

   -  - Section
      - Status
      - Files
      - Description

   -  - Quick Start
      - ✅ Complete
      - 3 files
      - Installation, first search, data models overview

   -  - User Guides
      - ✅ Complete
      - 6 files
      - Search, data models, historical data, configuration,
        performance, CLI

   -  - API Reference
      - ✅ Complete
      - 8 files
      - Complete API documentation for all modules

   -  - Advanced Topics
      - ✅ Complete
      - 4 files
      - Fuzzy matching, caching, error handling, custom sanitizers

   -  - Examples
      - ✅ Complete
      - 5 files
      - Address validation, geocoding, data analysis, batch processing,
        CLI usage

   -  - Troubleshooting
      - ✅ Complete
      - 3 files
      - Common errors, performance issues, FAQ

   -  - Contributing
      - ✅ Complete
      - 1 file
      - Contributing guide and documentation guidelines