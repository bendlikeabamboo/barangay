import pandas as pd
from pathlib import Path


def read(fp: Path) -> pd.DataFrame:
    if fp.suffix == ".csv":
        df: pd.DataFrame = pd.read_csv(filepath_or_buffer=fp)
    elif fp.suffix == ".xlsx":
        df: pd.DataFrame = pd.read_excel(io=fp, sheet_name="PSGC")
    else:
        raise ValueError("Invalid file suffix.")

    # Validation
    if {"psgc_id", "name", "geographic_level"} in set(list(df.columns)):
        pass
    elif {"10-digit PSGC", "Name", "Geographic Level"}.issubset(set(list(df.columns))):
        df = df.rename(
            mapper={
                "10-digit PSGC": "psgc_id",
                "Name": "name",
                "Geographic Level": "geographic_level",
            },
            axis=1,
        )
    elif {"Code", "Name", "Geographic Level"}.issubset(set(list(df.columns))):
        df = df.rename(
            mapper={
                "Code": "psgc_id",
                "Name": "name",
                "Geographic Level": "geographic_level",
            },
            axis=1,
        )
    else:
        raise ValueError(
            "Missing required columns."
            " None of ['psgc_id', 'name','geographic_level'] found"
        )

    df: pd.DataFrame = df[~df["psgc_id"].isna()].copy()
    df["psgc_id"] = (
        df["psgc_id"].astype(dtype="int32").astype(dtype=str).str.zfill(width=10)
    )
    df: pd.DataFrame = df.map(func=lambda x: x.strip() if isinstance(x, str) else x)
    return df
