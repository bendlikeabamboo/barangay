"""
List of Barangay in the Philippines

This package provides tools for searching and working with Philippine barangay data,
including fuzzy matching capabilities and multiple data formats.

Main exports:
    - search: Main search function for finding barangays
    - FuzzBase: Class for fuzzy matching operations
    - BarangayModel: Pydantic model for barangay data
    - BARANGAY: Basic barangay data dictionary
    - BARANGAY_EXTENDED: Extended barangay data dictionary
    - BARANGAY_FLAT: Flat barangay data dictionary
    - sanitize_input: Utility function for string sanitization
"""

# Import data
from barangay.data import (
    BARANGAY,
    BARANGAY_EXTENDED,
    BARANGAY_FLAT,
)

# Import models
from barangay.models import BarangayModel

# Import fuzzy matching
from barangay.fuzz import FuzzBase

# Import search functionality
from barangay.search import search

# Import utilities
from barangay.utils import sanitize_input

__all__ = [
    # Main search function
    "search",
    # Classes
    "FuzzBase",
    "BarangayModel",
    # Data
    "BARANGAY",
    "BARANGAY_EXTENDED",
    "BARANGAY_FLAT",
    # Utilities
    "sanitize_input",
]
