####################
 Welcome to Barangay
####################

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
********

-  **Fuzzy Search**: Fast, customizable matching for unstandardized
   addresses
-  **Multiple Data Models**: Basic (nested), Extended (recursive), and
   Flat (list) structures
-  **Historical Data**: Access previous PSGC releases by date
-  **Smart Caching**: Automatic caching for faster subsequent loads
-  **On-demand Download**: Download historical data from GitHub
   repository


Quick Start
***********

Installation:

.. code:: bash

   pip install barangay


Basic usage:

.. code:: python

   from barangay import search

   results = search("Tongmageng, Tawi-Tawi")
   print(results[0]["barangay"])  # Tongmageng


Documentation Sections
**********************

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting_started/installation
   getting_started/first_search
   getting_started/common_patterns

.. toctree::
   :maxdepth: 2
   :caption: Core Concepts

   core_concepts/index.rst

.. toctree::
   :maxdepth: 2
   :caption: How-To Guides

   how_to/address_validation
   how_to/batch_processing
   how_to/cli_operations
   how_to/performance
   how_to/custom_matching

.. toctree::
   :maxdepth: 2
   :caption: Examples

   examples/cli
   examples/geocoding
   examples/data_analysis
   examples/recipes

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api_reference/index

.. toctree::
   :maxdepth: 2
   :caption: Advanced

   advanced/caching
   advanced/custom_sanitizers
   advanced/error_handling
   advanced/fuzzy_matching

.. toctree::
   :maxdepth: 2
   :caption: Troubleshooting

   troubleshooting/common_errors
   troubleshooting/faq
   troubleshooting/issues
   troubleshooting/performance

.. toctree::
   :maxdepth: 2
   :caption: Contributing

   contributing/index


Indices and tables
##################

-  :ref:`genindex`
-  :ref:`modindex`
-  :ref:`search`


Links
*****

-  `GitHub Repository <https://github.com/bendlikeabamboo/barangay>`_
-  `Issue Tracker <https://github.com/bendlikeabamboo/barangay/issues>`_
-  `PyPI <https://pypi.org/project/barangay/>`_