"""Pydantic models for the barangay package.

This module provides Pydantic models for representing Philippine barangay data
with type validation and serialization support.

Main Classes:
    :class:`BarangayModel`: Model representing a barangay with administrative divisions

Examples:
    Creating a BarangayModel instance:

    >>> from barangay import BarangayModel
    >>> barangay = BarangayModel(
    ...     barangay="Tongmageng",
    ...     province_or_huc="Tawi-Tawi",
    ...     municipality_or_city="Sitangkai",
    ...     psgc_id="157501001"
    ... )
    >>> print(barangay.barangay)
    Tongmageng

    Converting to dictionary:

    >>> from barangay import BarangayModel
    >>> barangay = BarangayModel(
    ...     barangay="Barangay 1",
    ...     province_or_huc="Province A",
    ...     municipality_or_city="City 1",
    ...     psgc_id="010010001"
    ... )
    >>> data = barangay.model_dump()
    >>> print(data)
    {'barangay': 'Barangay 1', 'province_or_huc': 'Province A', ...}

See Also:
    :mod:`pydantic`: Pydantic documentation for BaseModel
"""

from pydantic import BaseModel


class BarangayModel(BaseModel):
    """Model representing a barangay with its administrative divisions.

    This Pydantic model provides type validation and serialization for Philippine
    barangay data. It includes the barangay name, its administrative divisions
    (province/HUC and municipality/city), and the Philippine Standard Geographic
    Code (PSGC).

    Attributes:
        barangay: Name of the barangay. This is the smallest administrative
            division in the Philippines, often referred to as a village or
            neighborhood.
        province_or_huc: Name of the province or Highly Urbanized City (HUC).
            In the Philippines, HUCs are cities that are independent from
            any province and have their own legislative districts.
        municipality_or_city: Name of the municipality or city. This is the
            intermediate administrative division between the province/HUC and
            the barangay.
        psgc_id: Philippine Standard Geographic Code. This is a unique
            identifier assigned by the Philippine Statistics Authority to each
            geographic area in the country. The code is typically 9 digits
            long and follows a hierarchical structure.

    Examples:
        Creating a BarangayModel instance:

        >>> from barangay import BarangayModel
        >>> barangay = BarangayModel(
        ...     barangay="Tongmageng",
        ...     province_or_huc="Tawi-Tawi",
        ...     municipality_or_city="Sitangkai",
        ...     psgc_id="157501001"
        ... )
        >>> print(barangay.barangay)
        Tongmageng

        Converting to dictionary:

        >>> from barangay import BarangayModel
        >>> barangay = BarangayModel(
        ...     barangay="Barangay 1",
        ...     province_or_huc="Province A",
        ...     municipality_or_city="City 1",
        ...     psgc_id="010010001"
        ... )
        >>> data = barangay.model_dump()
        >>> print(data)
        {'barangay': 'Barangay 1', 'province_or_huc': 'Province A', ...}

        JSON serialization:

        >>> from barangay import BarangayModel
        >>> barangay = BarangayModel(
        ...     barangay="Barangay 1",
        ...     province_or_huc="Province A",
        ...     municipality_or_city="City 1",
        ...     psgc_id="010010001"
        ... )
        >>> json_str = barangay.model_dump_json()
        >>> print(json_str)
        {"barangay":"Barangay 1","province_or_huc":"Province A",...}

    See Also:
        :class:`pydantic.BaseModel`: Base Pydantic model class
    """

    barangay: str
    province_or_huc: str
    municipality_or_city: str
    psgc_id: str
