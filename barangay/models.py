from pydantic import BaseModel, Field, RootModel
from typing import Any, Literal, Optional, List


class BarangayModel(BaseModel):
    """Model representing a barangay with its location details.

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
