from __future__ import annotations

import warnings
from enum import Enum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PrivateAttr,
    RootModel,
    model_validator,
)
from typing import TYPE_CHECKING, Any, Literal, Optional, List

if TYPE_CHECKING:
    from barangay.database import EnrichedRecord


class BarangayModel(BaseModel):
    """Model representing a barangay with its location details.

    .. deprecated::
        BarangayModel is deprecated and will be removed in 2027.X.X.X.
        Use AdminDivRecord (via the Database API) instead.

    Attributes:
        barangay: Name of the barangay.
        province_or_huc: Province or highly urbanized city name.
        municipality_or_city: Municipality or city name.
        psgc_id: Philippine Standard Geographic Code identifier.
    """

    barangay: str
    province_or_huc: str
    municipality_or_city: str
    psgc_id: str

    @model_validator(mode="wrap")
    @classmethod
    def _deprecation_warning(cls, values, handler, info):
        warnings.warn(
            "BarangayModel is deprecated and will be removed in 2027.X.X.X. "
            "Use AdminDivRecord (via the Database API) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return handler(values)


class PluginExtensionMetadata(BaseModel):
    """Metadata describing a plugin extension.

    Attributes:
        name: Name of the plugin extension.
        description: Optional description of the plugin extension.
        version: Optional version string of the plugin extension.
        repository: Optional repository URL for the plugin extension.
        format: Optional format identifier for the extension data.
        as_of: Optional date string indicating when the data was current.
    """

    name: str
    description: str | None = None
    version: str | None = None
    repository: str | None = None
    format: str | None = None
    as_of: str | None = None


class PluginExtension(BaseModel):
    """A plugin extension attached to an administrative division.

    Attributes:
        field_group: Logical grouping name for the extension fields.
        metadata: Metadata describing the plugin extension.
        data: Dictionary or list of dictionaries of extension field names to values.
    """

    field_group: str
    metadata: PluginExtensionMetadata
    data: dict[str, Any] | list[dict[str, Any]]


class AdminDivExtended(BaseModel):
    """Model for extended administrative division data with nesting.

    Attributes:
        name: Name of the administrative division.
        type: Type of administrative division.
        psgc_id: PSGC identifier or 'n/a'.
        parent_psgc_id: Parent PSGC identifier or 'n/a'.
        nicknames: Optional list of alternative names.
        components: List of nested administrative divisions.
    """

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
    components: List["AdminDivExtended"] = Field(default_factory=list)
    extensions: List["PluginExtension"] = Field(default_factory=list)


class AdminDiv(RootModel):
    """Root model for administrative division mapping or list.

    Attributes:
        root: Either a dict mapping PSGC IDs to AdminDiv or a list of IDs.
    """

    root: dict[str, "AdminDiv"] | List[str]

    def __getitem__(self, key):
        return self.root[key]

    def __contains__(self, key):
        return key in self.root

    def __iter__(self):
        """Iterate over the root structure.

        Returns:
            Iterator over dict keys or list items.
        """
        return iter(self.root)

    def keys(self):
        return self.root.keys() if isinstance(self.root, dict) else []

    def values(self):
        return self.root.values() if isinstance(self.root, dict) else []

    def items(self):
        return self.root.items() if isinstance(self.root, dict) else []


class AdminDivFlat(BaseModel):
    """Flat model for administrative division data without nesting.

    Attributes:
        name: Name of the administrative division.
        type: Type of administrative division.
        psgc_id: PSGC identifier or 'n/a'.
        parent_psgc_id: Parent PSGC identifier or 'n/a'.
        nicknames: Optional list of alternative names.
        extensions: List of plugin extensions attached to this division.
    """

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
    extensions: List["PluginExtension"] = Field(default_factory=list)


class AdminLevel(str, Enum):
    COUNTRY = "country"
    REGION = "region"
    PROVINCE = "province"
    CITY = "city"
    MUNICIPALITY = "municipality"
    SUBMUNICIPALITY = "submunicipality"
    BARANGAY = "barangay"
    SPECIAL_GEOGRAPHIC_AREA = "special_geographic_area"


class AdminDivRecord(BaseModel):
    """Unified record model for administrative divisions.

    Attributes:
        name: Name of the administrative division.
        type: AdminLevel enum value for the division type.
        psgc_id: PSGC identifier.
        parent_psgc_id: Parent PSGC identifier.
        nicknames: Optional list of alternative names.
        extensions: List of plugin extensions attached to this division.
    """

    model_config = ConfigDict(frozen=False, extra="forbid")

    name: str
    type: AdminLevel
    psgc_id: str
    parent_psgc_id: str
    nicknames: list[str] | None = None
    extensions: list[PluginExtension] = Field(default_factory=list)


def record_from_flat(flat: AdminDivFlat) -> AdminDivRecord:
    """Convert an AdminDivFlat to an AdminDivRecord.

    Args:
        flat: The flat record to convert.

    Returns:
        An AdminDivRecord with matching fields.
    """
    return AdminDivRecord(
        name=flat.name,
        type=AdminLevel(flat.type),
        psgc_id=flat.psgc_id,
        parent_psgc_id=flat.parent_psgc_id,
        nicknames=flat.nicknames,
        extensions=flat.extensions,
    )


class SearchResult(BaseModel):
    """Search result wrapping an AdminDivRecord with scoring metadata.

    Attributes:
        record: The matched administrative division record.
        score: Relevance score for the match.
        match_type: Type of match (e.g., 'exact', 'fuzzy', 'nickname').
        _index: Optional internal index reference.
    """

    model_config = ConfigDict(frozen=False, extra="forbid")

    record: AdminDivRecord
    score: float
    match_type: str
    _index: Any = PrivateAttr(default=None)

    @property
    def name(self) -> str:
        return self.record.name

    @property
    def psgc_id(self) -> str:
        return self.record.psgc_id

    @property
    def province(self) -> str | None:
        val = getattr(self.record, "province", None)
        return val if isinstance(val, str) else None

    @property
    def municipality(self) -> str | None:
        val = getattr(self.record, "municipality", None)
        return val if isinstance(val, str) else None

    @property
    def region(self) -> str | None:
        val = getattr(self.record, "region", None)
        return val if isinstance(val, str) else None

    @property
    def enriched(self) -> EnrichedRecord:
        if self._index is None:
            raise RuntimeError("Hierarchy index not available on this SearchResult")
        from barangay.database import EnrichedRecord

        return EnrichedRecord(self.record, self._index)

    def __getattr__(self, name: str):
        private_attrs = object.__getattribute__(self, "__private_attributes__")
        if name in private_attrs:
            private_values = object.__getattribute__(self, "__pydantic_private__")
            if private_values and name in private_values:
                return private_values[name]
        for ext in self.record.extensions:
            if ext.field_group == name:
                from barangay.database import PluginAccessor

                return PluginAccessor(ext.data, ext.metadata)
        raise AttributeError(f"'SearchResult' has no attribute '{name}'")


class ValidationResult(BaseModel):
    """Validation result for an administrative division input.

    Attributes:
        input: The original input string that was validated.
        valid: Whether the input matched a valid record.
        matched_record: The matched record, if any.
        score: Confidence score for the match, if any.
    """

    model_config = ConfigDict(frozen=False, extra="forbid")

    input: str
    valid: bool
    matched_record: AdminDivRecord | None = None
    score: float | None = None

    @property
    def matched_name(self) -> str | None:
        return self.matched_record.name if self.matched_record else None

    @property
    def matched_psgc_id(self) -> str | None:
        return self.matched_record.psgc_id if self.matched_record else None

    def __getattr__(self, name: str):
        private_attrs = object.__getattribute__(self, "__private_attributes__")
        if name in private_attrs:
            private_values = object.__getattribute__(self, "__pydantic_private__")
            if private_values and name in private_values:
                return private_values[name]
        if self.matched_record is None:
            raise AttributeError(f"'ValidationResult' has no attribute '{name}'")
        for ext in self.matched_record.extensions:
            if ext.field_group == name:
                from barangay.database import PluginAccessor

                return PluginAccessor(ext.data, ext.metadata)
        raise AttributeError(f"'ValidationResult' has no attribute '{name}'")


class PluginInfo(BaseModel):
    """Metadata about a registered plugin.

    Attributes:
        name: Name of the plugin.
        enabled: Whether the plugin is enabled.
        description: Optional description of the plugin.
        version: Optional version string of the plugin.
        format: Optional format identifier for the plugin data.
        repository: Optional repository URL for the plugin.
        error: Optional error message if the plugin failed to load.
    """

    name: str
    enabled: bool
    description: str | None = None
    version: str | None = None
    format: str | None = None
    repository: str | None = None
    error: str | None = None
