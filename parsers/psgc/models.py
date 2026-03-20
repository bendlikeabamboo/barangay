from typing import Literal, Optional, List
from pydantic import BaseModel, Field


class FlatLocation(BaseModel):
    name: str
    type: Literal[
        "country",
        "region",
        "province",
        "city",
        "municipality",
        "barangay",
        "special_geographic_area",
        "submunicipality",
    ]
    psgc_id: str | Literal["n/a"]
    parent_psgc_id: str | Literal["n/a"]
    nicknames: Optional[List[str]] = None
    # components: List["Location"] = Field(default_factory=list)


class Location(BaseModel):
    name: str
    type: Literal[
        "country",
        "region",
        "province",
        "city",
        "municipality",
        "barangay",
        "special_geographic_area",
        "submunicipality",
    ]
    psgc_id: str | Literal["n/a"]
    parent_psgc_id: str | Literal["n/a"]
    nicknames: Optional[List[str]] = None
    components: List["Location"] = Field(default_factory=list)
