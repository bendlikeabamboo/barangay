# Data Models

The barangay package provides three distinct data model formats, each optimized for specific use cases.

## BARANGAY

A compact nested structure ideal for quick lookups and simple hierarchical access. Organizes barangays by region, province/HUC, and municipality/city.

```json
{
    "Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)": {
        "Basilan": {
            "City of Lamitan": [
                "Arco",
                "Ba-as",
                "Baimbing"
            ]
        }
    }
}
```

## BARANGAY_EXTENDED

A fully hierarchical tree structure that preserves the complete administrative lineage. Each node contains its PSGC identifier, parent reference, type, and optional nicknames.

```json
{
    "name": "Philippines",
    "type": "country",
    "psgc_id": "0000000000",
    "parent_psgc_id": "n/a",
    "nicknames": null,
    "components": [
        {
            "name": "Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)",
            "type": "region",
            "psgc_id": "1900000000",
            "parent_psgc_id": "0000000000",
            "nicknames": null,
            "components": [
                {
                    "name": "Basilan",
                    "type": "province",
                    "psgc_id": "1900700000",
                    "parent_psgc_id": "1900000000",
                    "nicknames": null,
                    "components": [
                        {
                            "name": "City of Lamitan",
                            "type": "highly_urbanized_city",
                            "psgc_id": "1900702000",
                            "parent_psgc_id": "1900700000",
                            "nicknames": null,
                            "components": [
                                {
                                    "name": "Arco",
                                    "type": "barangay",
                                    "psgc_id": "1900702001",
                                    "parent_psgc_id": "1900702000",
                                    "nicknames": null,
                                    "components": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```

## BARANGAY_FLAT

A denormalized array format optimized for database storage and bulk operations. Each entry is independent, with parent relationships established through `parent_psgc_id`.

```json
[
    {
        "name": "Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)",
        "type": "region",
        "psgc_id": "1900000000",
        "parent_psgc_id": "0000000000",
        "nicknames": null
    },
    {
        "name": "Basilan",
        "type": "province",
        "psgc_id": "1900700000",
        "parent_psgc_id": "1900000000",
        "nicknames": null
    },
    {
        "name": "City of Lamitan",
        "type": "highly_urbanized_city",
        "psgc_id": "1900702000",
        "parent_psgc_id": "1900700000",
        "nicknames": null
    },
    {
        "name": "Arco",
        "type": "barangay",
        "psgc_id": "1900702001",
        "parent_psgc_id": "1900702000",
        "nicknames": null
    }
]
```
