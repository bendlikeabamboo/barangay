from typing import Literal

DataType = Literal["basic", "extended", "flat", "fuzzer_base"]
AdminDivType = Literal[
    "country",
    "region",
    "province",
    "city",
    "municipality",
    "barangay",
    "special_geographic_area",
    "submunicipality",
]
MatchHook = Literal["region", "province", "municipality", "barangay"]
PluginFormat = Literal["csv", "json", "parquet"]

__all__ = [
    "AdminDivType",
    "DataType",
    "MatchHook",
    "PluginFormat",
]
