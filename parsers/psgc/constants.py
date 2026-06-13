from typing import Dict

GEOGRAPHIC_LEVEL_MAP: Dict[str, str] = {
    "Reg": "region",
    "City": "city",
    "Mun": "municipality",
    "Prov": "province",
    "SubMun": "submunicipality",
    "Bgy": "barangay",
    "SGU": "special_geographic_area",
}

CITY_CLASS_MAP: Dict[str, str] = {
    "HUC": "highly_urbanized_city",
    "ICC": "independent_component_city",
    "CC": "component_city",
}
