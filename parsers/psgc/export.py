import json
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import yaml

from parsers.psgc.models import FlatLocation, Location


def export(
    dated_folder_path: Path,
    obj: List[FlatLocation] | Location | dict | pd.DataFrame,
):
    # For the Main data model
    if isinstance(obj, dict):
        json_str: str = json.dumps(
            obj=obj, default=lambda o: list(o) if isinstance(o, set) else o, indent=4
        )
        json_dict: Dict[str, Any] = json.loads(s=json_str)
        yaml_str: str = yaml.safe_dump(data=json_dict)

        with open(
            file=f"{dated_folder_path}/barangay.json", encoding="utf8", mode="w"
        ) as fp:
            fp.write(json_str)
        with open(
            file=f"{dated_folder_path}/barangay.yaml", encoding="utf8", mode="w"
        ) as fp:
            fp.write(yaml_str)

    # For the Extended data model
    elif isinstance(obj, Location):
        json_dump: str = json.dumps(obj=obj.model_dump(), indent=4)
        yaml_dump: str = yaml.safe_dump(data=obj.model_dump(), sort_keys=False)
        with open(
            file=f"{dated_folder_path}/barangay_extended.json",
            encoding="utf8",
            mode="w",
        ) as fp:
            fp.write(json_dump)
        with open(
            file=f"{dated_folder_path}/barangay_extended.yaml",
            encoding="utf8",
            mode="w",
        ) as fp:
            fp.write(yaml_dump)

    # For the Flat data model
    elif isinstance(obj, list):
        json_dump: str = json.dumps(obj=[item.model_dump() for item in obj], indent=4)
        yaml_dump: str = yaml.safe_dump(
            data=[item.model_dump() for item in obj], sort_keys=False
        )
        with open(
            file=f"{dated_folder_path}/barangay_flat.json", encoding="utf8", mode="w"
        ) as fp:
            fp.write(json_dump)
        with open(
            file=f"{dated_folder_path}/barangay_flat.yaml", encoding="utf8", mode="w"
        ) as fp:
            fp.write(yaml_dump)

    elif isinstance(obj, pd.DataFrame):
        obj.to_parquet(path=f"{dated_folder_path}/fuzzer_base.parquet")
