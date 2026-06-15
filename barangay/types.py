from typing import Literal

DataType = Literal["basic", "extended", "flat", "fuzzer_base"]
AdminDivType = Literal[
    "country",
    "region",
    "province",
    "highly_urbanized_city",
    "independent_component_city",
    "component_city",
    "municipality",
    "barangay",
    "special_geographic_area",
    "submunicipality",
]
MatchHook = Literal[
    "region",
    "province",
    "highly_urbanized_city",
    "independent_component_city",
    "component_city",
    "municipality",
    "submunicipality",
    "special_geographic_area",
    "barangay",
]
PluginFormat = Literal["csv", "json", "parquet"]

__all__ = [
    "AdminDivType",
    "DataType",
    "MatchHook",
    "PluginFormat",
]
