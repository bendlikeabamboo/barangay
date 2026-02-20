Utils Module
============

The utils module provides utility functions for string sanitization and data
processing. These utilities are used internally by the search and fuzzy matching
modules.

Overview
--------

The utils module provides string sanitization utilities that are used to normalize
input strings before fuzzy matching. The main function is :func:`sanitize_input`,
which removes whitespaces, converts to lowercase, and removes specified strings
from the input.

API Reference
-------------

.. autofunction:: barangay.utils.sanitize_input

Module Constants
----------------

.. autodata:: barangay.utils._basic_sanitizer
   :annotation: = partial(sanitize_input, exclude=[...])

Examples
--------

Basic Sanitization
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import sanitize_input
   
   # Basic sanitization (lowercase only)
   sanitized = sanitize_input("City of San Jose")
   print(sanitized)
   # city of san jose

With None Input
~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import sanitize_input
   
   # None input is converted to empty string
   sanitized = sanitize_input(None)
   print(sanitized)
   # 

With Custom Exclusions
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import sanitize_input
   
   # Remove specific strings
   sanitized = sanitize_input(
       "Barangay (Pob.)",
       exclude=["(pob.)"]
   )
   print(sanitized)
   # barangay
   
   # Remove multiple strings
   sanitized = sanitize_input(
       "City of Manila, NCR",
       exclude=["city of ", ", ncr"]
   )
   print(sanitized)
   # manila

With Non-String Input
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import sanitize_input
   
   # Non-string input is converted to empty string
   sanitized = sanitize_input(123)
   print(sanitized)
   # 

Using the Basic Sanitizer
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay.utils import _basic_sanitizer
   
   # The basic sanitizer has common exclusions pre-configured
   sanitized = _basic_sanitizer("City of Manila")
   print(sanitized)
   # manila
   
   sanitized = _basic_sanitizer("Barangay (Pob.)")
   print(sanitized)
   # barangay
   
   sanitized = _basic_sanitizer("San Jose, City")
   print(sanitized)
   # san jose

Basic Sanitizer Exclusions
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``_basic_sanitizer`` is a partial function of :func:`sanitize_input` with
the following pre-configured exclusions:

- ``(pob.)``: Place of birth abbreviation
- ``(pob)``: Place of birth abbreviation
- ``pob.``: Place of birth abbreviation
- ``city of ``: Common prefix
- `` city``: Common suffix
- ``.``: Periods
- ``-``: Hyphens
- ``(``: Opening parentheses
- ``)``: Closing parentheses
- ``&``: Ampersands
- ``,``: Commas

Creating Custom Sanitizers
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from functools import partial
   from barangay import sanitize_input
   
   # Create a custom sanitizer
   custom_sanitizer = partial(
       sanitize_input,
       exclude=["city of ", "municipality of ", ", ncr"]
   )
   
   # Use the custom sanitizer
   sanitized = custom_sanitizer("City of Manila, NCR")
   print(sanitized)
   # manila

Using with Search
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import search, sanitize_input
   
   # Use a custom sanitizer with search
   results = search(
       "City of San Jose",
       search_sanitizer=lambda x: sanitize_input(x, exclude=["city of "]),
   )
   
   for result in results:
       print(f"{result['barangay']}, {result['municipality_or_city']}")

Using with FuzzBase
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from barangay import FuzzBase, sanitize_input
   
   # Create a custom sanitizer
   custom_sanitizer = lambda x: sanitize_input(x, exclude=["city of "])
   
   # Create FuzzBase with custom sanitizer
   fuzz_base = FuzzBase(fuzzer_base=your_dataframe, sanitizer=custom_sanitizer)

See Also
--------

* :mod:`barangay.search` - Search functionality module
* :mod:`barangay.fuzz` - Fuzzy matching module
* :func:`barangay.search.search` - Search function with custom sanitizers
* :class:`barangay.fuzz.FuzzBase` - Fuzzy matching class