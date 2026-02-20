####################
 Contributing Guide
###################

This section covers how to contribute to the barangay package, including
code contributions, documentation improvements, and bug reports.


 Overview
*********

The barangay package welcomes contributions from the community! Whether
you're fixing a bug, adding a feature, improving documentation, or
reporting an issue, your help is appreciated.

Before contributing, please:

#. Read this contributing guide
#. Review the `Code of Conduct
   <https://github.com/bendlikeabamboo/barangay/blob/main/CODE_OF_CONDUCT.md>`_
#. Check existing issues and pull requests
#. Follow the project's coding standards and documentation style


 Ways to Contribute
*******************

Report Bugs
===========

Found a bug? Help us fix it by reporting it:

#. **Search existing issues** first to avoid duplicates

#. **Create a new issue** with: * Clear title describing the bug *
   Detailed description of the problem * Steps to reproduce the issue *
   Expected behavior vs actual behavior * Environment information
   (Python version, OS, package version) * Minimal reproducible example
   if possible

#. **Use the bug report template** if available

Example bug report:

.. code:: text

   **Title:** Search returns no results for valid barangay name

   **Description:**
   Searching for "Tongmageng" returns no results, but the barangay exists in the dataset.

   **Steps to reproduce:**
   ```python
   from barangay import search
   results = search("Tongmageng")
   print(results)  # []
   ```

   **Expected behavior:**
   Should return at least one result for "Tongmageng".

   **Actual behavior:**
   Returns empty list.

   **Environment:**
   - Python: 3.10.0
   - OS: Ubuntu 22.04
   - Package version: 2026.1.13.1

Suggest Enhancements
====================

Have an idea for an improvement? We'd love to hear it:

#. **Search existing issues** and pull requests

#. **Create a new issue** with: * Clear title describing the enhancement
   * Detailed description of the proposed feature * Use cases and
   benefits * Possible implementation approach (if you have ideas) *
   Alternative approaches considered

Example enhancement request:

.. code:: text

   **Title:** Add support for searching by PSGC code

   **Description:**
   It would be useful to search for barangays by their PSGC code directly, in addition to fuzzy name matching.

   **Use cases:**
   - Users with PSGC codes from other systems
   - Exact lookups when code is known
   - Integration with government databases

   **Benefits:**
   - Faster exact matches
   - More precise results
   - Better integration with existing systems

   **Possible implementation:**
   Add a new function `search_by_psgc(psgc_code)` that performs exact matching on PSGC codes.

Submit Code
===========

Want to contribute code? Here's how:

#. **Fork the repository** on GitHub

#. **Create a branch** for your changes:

   .. code:: bash

      git checkout -b feature/your-feature-name
      # or
      git checkout -b fix/your-bug-fix

#. **Make your changes** following the coding standards

#. **Write tests** for your changes

#. **Update documentation** if needed

#. **Commit your changes** with clear messages:

   .. code:: bash

      git commit -m "Add search_by_psgc function for exact PSGC code matching"

#. **Push to your fork**:

   .. code:: bash

      git push origin feature/your-feature-name

#. **Create a pull request** with: * Clear title and description *
   Reference to related issues * Explanation of changes * Screenshots or
   examples if applicable

Improve Documentation
=====================

Documentation is crucial for any project. Help us improve it:

#. **Read the documentation** to identify gaps or unclear sections
#. **Check for typos, grammatical errors, or outdated information**
#. **Add examples** for common use cases
#. **Improve explanations** of complex topics
#. **Add cross-references** between related sections

See the :ref:`documentation-style-guide` below for guidelines.


 Getting Started
****************

Development Setup
=================

Set up your development environment:

#. **Clone the repository**:

   .. code:: bash

      git clone https://github.com/bendlikeabamboo/barangay.git
      cd barangay

#. **Create a virtual environment**:

   .. code:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

#. **Install in development mode**:

   Using uv (recommended):

   .. code:: bash

      uv pip install -e ".[dev]"

   Using pip:

   .. code:: bash

      pip install -e ".[dev]"

#. **Verify installation**:

   .. code:: python

      import barangay

      print(barangay.current)

#. **Run tests**:

   .. code:: bash

      pytest

#. **Run linter**:

   .. code:: bash

      ruff check barangay/
      mypy barangay/

Project Structure
=================

Understanding the project structure:

.. list-table:: Project Structure
   :widths: 30 70
   :header-rows: 1

   -  -  Directory/File
      -  Description
   -  -  ``barangay/``
      -  Main package source code
   -  -  ``barangay/__init__.py``
      -  Package initialization and public API
   -  -  ``barangay/search.py``
      -  Fuzzy search functionality
   -  -  ``barangay/fuzz.py``
      -  Fuzzy matching utilities
   -  -  ``barangay/data_manager.py``
      -  Data loading and management
   -  -  ``barangay/data.py``
      -  Data loading functions
   -  -  ``barangay/downloader.py``
      -  Data downloading from GitHub
   -  -  ``barangay/date_resolver.py``
      -  Date resolution for historical data
   -  -  ``barangay/config.py``
      -  Configuration management
   -  -  ``barangay/models.py``
      -  Data models and schemas
   -  -  ``barangay/utils.py``
      -  Utility functions
   -  -  ``barangay/data/``
      -  Data files (JSON, YAML, Parquet)
   -  -  ``tests/``
      -  Test files
   -  -  ``docs/``
      -  Documentation source files
   -  -  ``notebooks/``
      -  Jupyter notebooks with examples
   -  -  ``pyproject.toml``
      -  Project configuration and dependencies

Coding Standards
================

Follow these coding standards:

#. **PEP 8 compliance**: Use `ruff` to check and format:

   .. code:: bash

      ruff check barangay/
      ruff format barangay/

#. **Type hints**: Use type hints for function signatures:

   .. code:: python

      from typing import List, Dict, Optional


      def search(
          search_string: str,
          n: int = 5,
          match_hooks: Optional[List[str]] = None,
          threshold: float = 60.0,
          as_of: Optional[str] = None,
          fuzz_base: Optional[Any] = None,
      ) -> List[Dict[str, Any]]:
          """Search for barangays with fuzzy matching."""
          ...

#. **Docstrings**: Use Google-style docstrings:

   .. code:: python

      def search(
          search_string: str,
          n: int = 5,
          match_hooks: Optional[List[str]] = None,
          threshold: float = 60.0,
          as_of: Optional[str] = None,
          fuzz_base: Optional[Any] = None,
      ) -> List[Dict[str, Any]]:
          """Search for barangays with fuzzy matching.

          Args:
              search_string: String to search for.
              n: Maximum number of results to return.
              match_hooks: Administrative levels to match against.
              threshold: Minimum similarity score (0-100).
              as_of: Date string for historical data (YYYY-MM-DD).
              fuzz_base: Pre-computed FuzzBase instance.

          Returns:
              List of search results, each a dictionary with match information.

          Raises:
              ValueError: If match_hooks contains invalid values.
          """
          ...

#. **Error handling**: Use descriptive error messages:

   .. code:: python

      if not search_string:
          raise ValueError("search_string cannot be empty")

      valid_hooks = ["province", "municipality", "barangay"]
      invalid_hooks = [h for h in match_hooks if h not in valid_hooks]
      if invalid_hooks:
          raise ValueError(
              f"Invalid match_hooks: {invalid_hooks}. " f"Valid options: {valid_hooks}"
          )

#. **Logging**: Use appropriate log levels:

   .. code:: python

      import logging

      logger = logging.getLogger(__name__)

      logger.debug("Debugging information")
      logger.info("General information")
      logger.warning("Warning message")
      logger.error("Error message")

Testing
=======

Write tests for your changes:

#. **Use pytest** for testing:

   .. code:: python

      import pytest
      from barangay import search


      def test_search_basic():
          """Test basic search functionality."""
          results = search("Tongmageng, Tawi-Tawi")
          assert len(results) > 0
          assert results[0]["barangay"] == "Tongmageng"


      def test_search_threshold():
          """Test threshold parameter."""
          results_high = search("San Jose", threshold=90.0)
          results_low = search("San Jose", threshold=40.0)
          assert len(results_low) >= len(results_high)

#. **Run tests**:

   .. code:: bash

      pytest

#. **Run specific tests**:

   .. code:: bash

      pytest tests/test_search.py::test_search_basic

#. **Run with coverage**:

   .. code:: bash

      pytest --cov=barangay --cov-report=html

#. **Test guidelines**: * Write descriptive test names * Test both
   success and failure cases * Use fixtures for common setup * Keep
   tests independent * Mock external dependencies


 Documentation Contributions
****************************

.. _documentation-style-guide:

Documentation Style Guide
=========================

When contributing to documentation, follow these guidelines:

#. **Use reStructuredText (reST)** formatting

#. **Section headings**:

   .. code:: rst

      Level 1 Heading
      ===============

      Level 2 Heading
      ---------------

      Level 3 Heading
      ~~~~~~~~~~~~~~~

#. **Code blocks** with syntax highlighting:

   .. code:: python

      from barangay import search

      results = search("Tongmageng")

   .. code:: bash

      pip install barangay

#. **Inline code** with double backticks:

   Use ``search()`` function to find barangays.

#. **Links**:

   -  Internal: :doc:`../user_guide/search`
   -  External: `PyPI <https://pypi.org/project/barangay/>`_

#. **Admonitions** for important information:

   .. note::

      This is a note.

   .. warning::

      This is a warning.

   .. tip::

      This is a tip.

#. **Lists**:

   -  Item 1
   -  Item 2

   #. Numbered item 1
   #. Numbered item 2

#. **Tables**:

   .. list-table:: Example Table
      :widths: 30 70
      :header-rows: 1

      -  -  Column 1
         -  Column 2
      -  -  Row 1, Col 1
         -  Row 1, Col 2

#. **Cross-references**:

   See :doc:`../user_guide/search` for more details. See
   :doc:`../api_reference/search` for the API reference.

Building Documentation Locally
==============================

Build and view the documentation locally:

#. **Install documentation dependencies**:

   .. code:: bash

      pip install -e ".[dev]"

#. **Navigate to docs directory**:

   .. code:: bash

      cd docs

#. **Build the documentation**:

   Using make (Linux/macOS):

   .. code:: bash

      make html

   Using make.bat (Windows):

   .. code:: bash

      make.bat html

   Or using sphinx-build directly:

   .. code:: bash

      sphinx-build -b html . _build/html

#. **View the documentation**:

   Open ``_build/html/index.html`` in your browser.

#. **Clean build files**:

   .. code:: bash

      make clean  # Linux/macOS
      # or
      make.bat clean  # Windows

#. **Watch for changes** (optional):

   Install sphinx-autobuild:

   .. code:: bash

      pip install sphinx-autobuild

   Run with auto-reload:

   .. code:: bash

      sphinx-autobuild . _build/html

Testing Documentation Changes
=============================

Test your documentation changes:

#. **Build the documentation** and check for errors:

   .. code:: bash

      make html 2>&1 | grep -E "(error|warning)"

#. **Check links**:

   .. code:: bash

      make linkcheck

#. **Verify code examples**:

   -  Copy code blocks from documentation
   -  Run them to ensure they work
   -  Update if they fail

#. **Check spelling**:

   .. code:: bash

      pip install sphinxcontrib-spelling
      make spelling

#. **Preview in browser**:

   -  Open ``_build/html/index.html``
   -  Navigate through the documentation
   -  Check formatting and layout
   -  Verify links work

Documentation Structure
=======================

Understanding the documentation structure:

.. list-table:: Documentation Structure
   :widths: 30 70
   :header-rows: 1

   -  -  Directory/File
      -  Description
   -  -  ``docs/index.rst``
      -  Main documentation landing page
   -  -  ``docs/conf.py``
      -  Sphinx configuration
   -  -  ``docs/quick_start/``
      -  Quick start guides
   -  -  ``docs/user_guide/``
      -  Comprehensive user guides
   -  -  ``docs/api_reference/``
      -  API reference documentation
   -  -  ``docs/advanced/``
      -  Advanced topics
   -  -  ``docs/examples/``
      -  Usage examples
   -  -  ``docs/troubleshooting/``
      -  Troubleshooting guides
   -  -  ``docs/contributing/``
      -  Contributing guidelines
   -  -  ``docs/_static/``
      -  Static files (CSS, images)
   -  -  ``docs/_templates/``
      -  Custom templates

Submitting Documentation PRs
============================

When submitting documentation pull requests:

#. **Follow the style guide** above

#. **Build locally** and verify no errors

#. **Test all code examples**

#. **Check all links** work

#. **Use clear commit messages**:

   .. code:: bash

      git commit -m "docs: Add example for batch processing"

#. **Reference related issues** in the PR description

#. **Include screenshots** if applicable (for UI changes)


 Pull Request Guidelines
************************

Before Submitting
=================

Before submitting a pull request:

#. **Ensure your code follows** the coding standards

#. **Write tests** for your changes

#. **Update documentation** if needed

#. **Run all tests** and ensure they pass:

   .. code:: bash

      pytest

#. **Run linter** and fix any issues:

   .. code:: bash

      ruff check barangay/
      mypy barangay/

#. **Build documentation** and check for errors:

   .. code:: bash

      cd docs && make html

#. **Squash commits** into logical units:

   .. code:: bash

      git rebase -i HEAD~n  # n = number of commits to squash

PR Description
==============

Write a clear PR description:

.. code:: text

   ## Summary
   Add search_by_psgc function for exact PSGC code matching.

   ## Changes
   - Added `search_by_psgc()` function in `search.py`
   - Added unit tests in `tests/test_search.py`
   - Updated API reference documentation
   - Added example in user guide

   ## Related Issues
   Fixes #123

   ## Testing
   - Added 5 new tests
   - All existing tests pass
   - Manual testing with various PSGC codes

   ## Checklist
   - [x] Code follows style guidelines
   - [x] Tests added and passing
   - [x] Documentation updated
   - [x] No new warnings

Code Review Process
===================

During code review:

#. **Be respectful** and constructive
#. **Ask questions** if something is unclear
#. **Suggest improvements** politely
#. **Test changes** locally if possible
#. **Respond promptly** to review comments
#. **Make requested changes** or explain why not

After Review
============

After your PR is reviewed:

#. **Address feedback** from reviewers
#. **Make necessary changes**
#. **Push updates** to your branch
#. **Request another review** if needed
#. **Celebrate** when your PR is merged! 🎉


 Community Guidelines
*********************

Code of Conduct
===============

Be respectful and inclusive:

-  **Be respectful**: Treat others with respect
-  **Be inclusive**: Welcome diverse perspectives
-  **Be constructive**: Provide helpful feedback
-  **Be patient**: Understand everyone has different experience levels
-  **Be collaborative**: Work together to improve the project

See the full `Code of Conduct
<https://github.com/bendlikeabamboo/barangay/blob/main/CODE_OF_CONDUCT.md>`_
for details.

Communication Channels
======================

Get in touch:

-  **GitHub Issues**: Report bugs and request features
-  **GitHub Discussions**: Ask questions and discuss ideas
-  **Pull Requests**: Submit code and documentation changes

Getting Help
============

Need help contributing?

#. **Read this guide** thoroughly
#. **Check existing issues** for similar questions
#. **Ask a question** in GitHub Discussions
#. **Contact maintainers** via GitHub issues


 Recognition
************

Contributors are recognized in:

-  ``CONTRIBUTORS.md`` file (if it exists)
-  Release notes
-  GitHub contributors list

Thank you for contributing to the barangay package! 🙏


 See Also
*********

-  `Code of Conduct
   <https://github.com/bendlikeabamboo/barangay/blob/main/CODE_OF_CONDUCT.md>`_
-  :doc:`../troubleshooting/common_errors` - Common errors and solutions
-  :doc:`../troubleshooting/faq` - Frequently asked questions
-  `GitHub Repository <https://github.com/bendlikeabamboo/barangay>`_