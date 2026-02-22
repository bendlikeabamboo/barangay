#############
  API Reference
###############

This section provides detailed API documentation for all modules in the barangay package.

Core Modules
============

.. toctree::
   :maxdepth: 1

   data_manager
   data
   search
   config
   models

**Data Manager Module**

Provides the DataManager class for handling data loading, caching, and downloading of Philippine barangay data. Supports multiple data formats and can load data from bundled package files, local cache, or download from GitHub.

**Data Module**

Provides functions for loading Philippine barangay data in different formats (basic, extended, flat). Data can be loaded from bundled package files, local cache, or downloaded from GitHub repository.

**Search Module**

Provides fuzzy string matching capabilities for searching Philippine barangay data across different administrative levels (province, municipality, barangay) using the RapidFuzz library.

**Config Module**

Provides functions for resolving configuration settings from multiple sources, including environment variables, module attributes, and function parameters.

**Models Module**

Provides Pydantic models for representing Philippine barangay data with type validation and serialization support.

Utility Modules
===============

.. toctree::
   :maxdepth: 1

   fuzz
   date_resolver
   downloader
   utils

**Fuzz Module**

Provides the FuzzBase class and related functions for performing fuzzy string matching on Philippine barangay data using the RapidFuzz library.

**Date Resolver Module**

Provides functions for resolving approximate dates to the closest available dataset, with support for fetching available dates from GitHub API and caching results locally.

**Downloader Module**

Provides functions for downloading Philippine barangay data from the GitHub repository, supporting different data types and saving them to a local cache directory.

**Utils Module**

Provides utility functions for string sanitization and data processing, used internally by the search and fuzzy matching modules.

CLI Module
==========

.. toctree::
   :maxdepth: 1

   cli

**CLI Module**

Provides a command-line interface for the barangay package, built using the Click framework. Offers convenient access to all package functionality including search, export, data information, historical data access, cache management, and batch processing.