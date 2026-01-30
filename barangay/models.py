"""
Pydantic models for the barangay package.
"""

from pydantic import BaseModel


class BarangayModel(BaseModel):
    """Model representing a barangay with its administrative divisions."""

    barangay: str
    province_or_huc: str
    municipality_or_city: str
    psgc_id: str
