import logging
from typing import Any, Dict, List, Set

import pandas as pd
from tqdm import tqdm
from pydantic import ValidationError

from parsers.psgc.models import FlatLocation, Location
from parsers.psgc.constants import GEOGRAPHIC_LEVEL_MAP, CITY_CLASS_MAP

logger = logging.getLogger(__name__)

_CITY_LEVELS: set[str] = {
    "highly_urbanized_city",
    "independent_component_city",
    "component_city",
}

_POS_TO_COL: list[str] = [
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

_PRE_CONCAT_COLS: list[str] = [
    "r0h00000b",
    "r0h000s0b",
    "r0000m00b",
    "rp000m00b",
    "rp00c000b",
    "rp0i0000b",
    "r0000m0gb",
]


def _build_pre_concat_value(row: dict, col_name: str) -> str:
    parts: list[str] = []
    for pos, letter in enumerate(col_name):
        if letter != "0":
            admin_col = _POS_TO_COL[pos]
            val = row.get(admin_col, "")
            if val:
                parts.append(str(val))
    return " ".join(parts)


def transform_df(
    df: pd.DataFrame, geographic_level_map=GEOGRAPHIC_LEVEL_MAP
) -> pd.DataFrame:
    df["geographic_level"] = df["geographic_level"].replace(
        to_replace=geographic_level_map
    )
    df["barangay_code"] = df["psgc_id"].str[-3:]
    df["municipal_or_city_code"] = df["psgc_id"].str[-5:-3]
    df["province_or_huc_code"] = df["psgc_id"].str[-8:-5]
    df["region_code"] = df["psgc_id"].str[-10:-8]

    df["barangay_mapper"] = df["psgc_id"].str[-10:]
    df["municipal_or_city_mapper"] = df["psgc_id"].str[-10:-3]
    df["province_or_huc_mapper"] = df["psgc_id"].str[-10:-5]
    df["region_mapper"] = df["psgc_id"].str[-10:-8]

    regions_filter: pd.Series = (
        (df["province_or_huc_code"] == "000")
        & (df["municipal_or_city_code"] == "00")
        & (df["barangay_code"] == "000")
    )
    regions_mapper: pd.DataFrame = (
        df.loc[regions_filter, ["region_mapper", "name"]]
        .sort_values(by="region_mapper")
        .set_index(keys="region_mapper", drop=True)
        .to_dict()["name"]
    )

    province_or_huc_filter: pd.Series = (
        ~(df["province_or_huc_code"] == "000")
        & (df["municipal_or_city_code"] == "00")
        & (df["barangay_code"] == "000")
    )

    province_or_huc_mapper: pd.DataFrame = (
        df.loc[province_or_huc_filter, ["province_or_huc_mapper", "name"]]
        .sort_values(by="province_or_huc_mapper")
        .set_index(keys="province_or_huc_mapper")
        .to_dict()["name"]
    )

    municipal_or_city_filter: pd.Series = (
        ~(df["province_or_huc_code"] == "000")
        & ~(df["municipal_or_city_code"] == "00")
        & (df["barangay_code"] == "000")
    )

    municipal_or_city_mapper: pd.DataFrame = (
        df.loc[municipal_or_city_filter, ["municipal_or_city_mapper", "name"]]
        .sort_values(by="municipal_or_city_mapper")
        .set_index(keys="municipal_or_city_mapper")
        .to_dict()["name"]
    )
    df["region"] = df["region_mapper"].map(arg=regions_mapper)
    df["province_or_huc"] = df["province_or_huc_mapper"].map(arg=province_or_huc_mapper)
    df["municipality_or_city"] = df["municipal_or_city_mapper"].map(
        arg=municipal_or_city_mapper
    )

    city_mask = df["geographic_level"] == "city"
    if "city_class" in df.columns and city_mask.any():
        for code, city_type in CITY_CLASS_MAP.items():
            mask = city_mask & (df["city_class"] == code)
            df.loc[mask, "geographic_level"] = city_type
        unresolved = city_mask & df["geographic_level"] == "city"
        if unresolved.any():
            logger.warning(
                "City rows with missing/unmapped city_class: %d rows",
                unresolved.sum(),
            )

    isabela_mask = df["psgc_id"] == "0990100000"
    if isabela_mask.any():
        df.loc[isabela_mask, "geographic_level"] = "independent_component_city"

    return df


def transform_main(
    df: pd.DataFrame,
    geographic_level_map=GEOGRAPHIC_LEVEL_MAP,
):
    df: pd.DataFrame = transform_df(df, geographic_level_map=geographic_level_map)

    barangay_df: pd.DataFrame = df[df["geographic_level"] == "barangay"].reset_index(
        drop=True
    )
    empty_municipality: pd.Series = barangay_df["municipality_or_city"].isna()
    empty_province_or_huc: pd.Series = barangay_df["province_or_huc"].isna()

    mdf: pd.DataFrame = barangay_df[~empty_municipality & ~empty_province_or_huc][
        [
            "region",
            "region_mapper",
            "province_or_huc",
            "province_or_huc_mapper",
            "municipality_or_city",
            "municipal_or_city_mapper",
            "name",
        ]
    ].sort_values(["region", "province_or_huc", "municipality_or_city"])

    empty_municipality_df: pd.DataFrame = barangay_df[
        empty_municipality & ~empty_province_or_huc
    ][
        [
            "region",
            "region_mapper",
            "province_or_huc",
            "province_or_huc_mapper",
            "municipality_or_city",
            "municipal_or_city_mapper",
            "name",
        ]
    ].sort_values(by=["region", "province_or_huc", "municipality_or_city"])

    empty_province_df: pd.DataFrame = barangay_df[
        ~empty_municipality & empty_province_or_huc
    ][
        [
            "region",
            "region_mapper",
            "province_or_huc",
            "province_or_huc_mapper",
            "municipality_or_city",
            "municipal_or_city_mapper",
            "name",
        ]
    ].sort_values(by=["region", "municipality_or_city"])

    root_dict: Dict[str, Dict[str, Set[str] | Dict[str, Set[str]]]] = {}
    for idx, (i, j, k, l) in mdf[  # noqa: E741
        ["region", "province_or_huc", "municipality_or_city", "name"]
    ].iterrows():
        if i not in root_dict.keys():
            root_dict[i] = {}
        if j not in root_dict[i].keys():
            root_dict[i][j] = {}
        if k not in root_dict[i][j].keys():  # ty:ignore[unresolved-attribute]
            root_dict[i][j][k] = set()  # ty:ignore[invalid-assignment]
        root_dict[i][j][k].add(l)  # ty:ignore[not-subscriptable]

    # handling empty municipality
    for idx, (i, j, k) in empty_municipality_df[
        ["region", "province_or_huc", "name"]
    ].iterrows():
        if i not in root_dict.keys():
            root_dict[i] = {}
        if j not in root_dict[i].keys():
            root_dict[i][j] = set()
        root_dict[i][j].add(k)  # ty:ignore[unresolved-attribute]

    # handling empty prov
    for idx, (i, j, k) in empty_province_df[
        ["region", "municipality_or_city", "name"]
    ].iterrows():
        if i not in root_dict.keys():
            root_dict[i] = {}
        if j not in root_dict[i].keys():
            root_dict[i][j] = set()
        root_dict[i][j].add(k)  # ty:ignore[unresolved-attribute]
    return root_dict


def transform_extended(
    df: pd.DataFrame, geographic_level_map=GEOGRAPHIC_LEVEL_MAP
) -> Location:
    root_dict: dict[str, dict[str, set[str] | dict[str, set[str]]]] = transform_main(
        df=df, geographic_level_map=geographic_level_map
    )
    root = Location(
        name="Philippines", psgc_id="0000000000", type="country", parent_psgc_id="n/a"
    )
    for region in root_dict:
        row: pd.Series[Any] = df[df["name"] == region].iloc[0]
        new_location = Location(
            name=row["name"],
            type="region",
            psgc_id=row["psgc_id"],
            parent_psgc_id="0000000000",
        )
        if new_location not in root.components:
            root.components.append(new_location)

    # RESOLVE PROVINCES & HUC UNDER REGIONS
    for region in root.components:
        provinces_or_hucs_in_region: pd.DataFrame = df[
            (df["region"] == region.name)
            & ~(
                df["province_or_huc_code"] == "000"
            )  # this means that this is a province
            & (df["municipal_or_city_code"] == "00")
            & (df["barangay_code"] == "000")
        ]
        for idx, prov_or_huc in provinces_or_hucs_in_region.iterrows():
            if prov_or_huc["psgc_id"] == "1999900000":
                prov_or_huc["geographic_level"] = "special_geographic_area"
            try:
                newloc = Location(
                    name=prov_or_huc["name"],
                    type=prov_or_huc["geographic_level"],
                    psgc_id=prov_or_huc["psgc_id"],
                    parent_psgc_id=region.psgc_id,
                )
            except ValidationError:
                print("############## ERROR")
                print(prov_or_huc)
            region.components.append(newloc)

    # RESOLVE CITIES & MUNICIPALITIES DIRECTLY UNDER REGIONS
    for region in root.components:
        municipality_or_city_in_region: pd.DataFrame = df[
            (df["region"] == region.name)
            & ~(
                df["province_or_huc_code"] == "000"
            )  # this means that this is a province
            & ~(df["municipal_or_city_code"] == "00")
            & (df["barangay_code"] == "000")
            & ~(df["province_or_huc"].notna())
        ]
        for idx, mun_or_city in municipality_or_city_in_region.iterrows():
            try:
                newloc = Location(
                    name=mun_or_city["name"],
                    type=mun_or_city["geographic_level"],
                    psgc_id=mun_or_city["psgc_id"],
                    parent_psgc_id=region.psgc_id,
                )
            except ValidationError:
                print("############## ERROR")
                print(mun_or_city)
            region.components.append(newloc)

    # RESOLVE CITIES & MUNICIPALITIES UNDER PROVINCE & HUCs
    for region in root.components:
        for province_or_huc in region.components:
            municipality_or_city_in_province_or_huc: pd.DataFrame = df[
                (df["province_or_huc"] == province_or_huc.name)
                & (df["region"] == region.name)
                & ~(df["province_or_huc_code"] == "000")
                & ~(df["municipal_or_city_code"] == "00")
                & (df["barangay_code"] == "000")
                & (df["province_or_huc"].notna())
                & (df["municipality_or_city"].notna())
            ]
            for idx, mun_or_city in municipality_or_city_in_province_or_huc.iterrows():
                try:
                    newloc = Location(
                        name=mun_or_city["name"],
                        type=mun_or_city["geographic_level"],
                        psgc_id=mun_or_city["psgc_id"],
                        parent_psgc_id=province_or_huc.psgc_id,
                    )
                except ValidationError as e:
                    print(e)
                    print("############## ERROR")
                    print(mun_or_city)
                province_or_huc.components.append(newloc)

    # RESOLVE BARANGAY IF ITS UNDER A MUNICIPALITY OR CITY AND UNDER A PROVINCE OR HUC
    for region in tqdm(root.components, leave=True, ascii=True):
        for province_or_huc in region.components:
            for municipality_or_city in province_or_huc.components:
                barangay_in_municipality_or_city: pd.DataFrame = df[
                    (df["municipality_or_city"] == municipality_or_city.name)
                    & (df["region"] == region.name)
                    & (df["province_or_huc"] == province_or_huc.name)
                    & ~(df["province_or_huc_code"] == "000")
                    & ~(df["municipal_or_city_code"] == "00")
                    & ~(df["barangay_code"] == "000")
                    & (df["province_or_huc"].notna())
                    & (df["municipality_or_city"].notna())
                ]
                for idx, barangay in barangay_in_municipality_or_city.iterrows():
                    try:
                        newloc = Location(
                            name=barangay["name"],
                            type=barangay["geographic_level"],
                            psgc_id=barangay["psgc_id"],
                            parent_psgc_id=municipality_or_city.psgc_id,
                        )
                    except ValidationError as e:
                        print(e)
                        print("############## ERROR")
                        print(barangay)
                    municipality_or_city.components.append(newloc)

    # RESOLVE BARANGAYS DIRECTLY UNDER PROVINCE OR HUCS
    for region in tqdm(root.components, leave=True, ascii=True):
        for province_or_huc in region.components:
            barangay_in_province_or_huc = df[
                (df["province_or_huc"] == province_or_huc.name)
                & (df["region"] == region.name)
                & ~(df["province_or_huc_code"] == "000")
                & (df["municipal_or_city_code"] == "00")
                & ~(df["barangay_code"] == "000")
                & (df["province_or_huc"].notna())
                & ~(df["municipality_or_city"].notna())
            ]
            for idx, barangay in barangay_in_province_or_huc.iterrows():
                try:
                    newloc = Location(
                        name=barangay["name"],
                        type=barangay["geographic_level"],
                        psgc_id=barangay["psgc_id"],
                        parent_psgc_id=province_or_huc.psgc_id,
                    )
                except ValidationError as e:
                    print(e)
                    print("############## ERROR")
                    print(province_or_huc)
                province_or_huc.components.append(newloc)

    # RESOLVE BARANGAY UNDER MUNICIPALITY THAT IS UNDER REGIONS DIRECTLY
    for region in tqdm(root.components, leave=True, ascii=True):
        for municipality_or_city in region.components:
            barangay_in_municipality_or_city: pd.DataFrame = df[
                (df["municipality_or_city"] == municipality_or_city.name)
                & (df["region"] == region.name)
                & ~(df["province_or_huc_code"] == "000")
                & ~(df["municipal_or_city_code"] == "00")
                & ~(df["barangay_code"] == "000")
                & ~(df["province_or_huc"].notna())
                & (df["municipality_or_city"].notna())
            ]
            for idx, barangay in barangay_in_municipality_or_city.iterrows():
                try:
                    newloc = Location(
                        name=barangay["name"],
                        type=barangay["geographic_level"],
                        psgc_id=barangay["psgc_id"],
                        parent_psgc_id=municipality_or_city.psgc_id,
                    )
                except ValidationError as e:
                    print(e)
                    print("############## ERROR")
                    print(mun_or_city)
                municipality_or_city.components.append(newloc)
    return root


def transform_flat(
    df: pd.DataFrame, geographic_level_map=GEOGRAPHIC_LEVEL_MAP
) -> List[FlatLocation]:
    root_dict: dict[str, dict[str, set[str] | dict[str, set[str]]]] = transform_main(
        df=df, geographic_level_map=geographic_level_map
    )
    flat_dict: List[FlatLocation] = []
    root = Location(
        name="Philippines", psgc_id="0000000000", type="country", parent_psgc_id="n/a"
    )
    for region in root_dict:
        row: pd.Series[Any] = df[df["name"] == region].iloc[0]
        new_location = Location(
            name=row["name"],
            type="region",
            psgc_id=row["psgc_id"],
            parent_psgc_id="0000000000",
        )
        flat_location = FlatLocation(
            name=row["name"],
            type="region",
            psgc_id=row["psgc_id"],
            parent_psgc_id="0000000000",
        )
        root.components.append(new_location)
        flat_dict.append(flat_location)

    # RESOLVE PROVINCES & HUC UNDER REGIONS
    for region in root.components:
        provinces_or_hucs_in_region: pd.DataFrame = df[
            (df["region"] == region.name)
            & ~(
                df["province_or_huc_code"] == "000"
            )  # this means that this is a province
            & (df["municipal_or_city_code"] == "00")
            & (df["barangay_code"] == "000")
        ]
        for idx, prov_or_huc in provinces_or_hucs_in_region.iterrows():
            if prov_or_huc["psgc_id"] == "1999900000":
                prov_or_huc["geographic_level"] = "special_geographic_area"
            try:
                newloc = Location(
                    name=prov_or_huc["name"],
                    type=prov_or_huc["geographic_level"],
                    psgc_id=prov_or_huc["psgc_id"],
                    parent_psgc_id=region.psgc_id,
                )
                newflatloc = FlatLocation(
                    name=prov_or_huc["name"],
                    type=prov_or_huc["geographic_level"],
                    psgc_id=prov_or_huc["psgc_id"],
                    parent_psgc_id=region.psgc_id,
                )
            except ValidationError:
                print("############## ERROR")
                print(prov_or_huc)
            region.components.append(newloc)
            flat_dict.append(newflatloc)

    # RESOLVE CITIES & MUNICIPALITIES DIRECTLY UNDER REGIONS
    for region in root.components:
        municipality_or_city_in_region: pd.DataFrame = df[
            (df["region"] == region.name)
            & ~(
                df["province_or_huc_code"] == "000"
            )  # this means that this is a province
            & ~(df["municipal_or_city_code"] == "00")
            & (df["barangay_code"] == "000")
            & ~(df["province_or_huc"].notna())
        ]
        for idx, mun_or_city in municipality_or_city_in_region.iterrows():
            try:
                newloc = Location(
                    name=mun_or_city["name"],
                    type=mun_or_city["geographic_level"],
                    psgc_id=mun_or_city["psgc_id"],
                    parent_psgc_id=region.psgc_id,
                )
                newflatloc = FlatLocation(
                    name=mun_or_city["name"],
                    type=mun_or_city["geographic_level"],
                    psgc_id=mun_or_city["psgc_id"],
                    parent_psgc_id=region.psgc_id,
                )
            except ValidationError:
                print("############## ERROR")
                print(mun_or_city)
            region.components.append(newloc)
            flat_dict.append(newflatloc)

    # RESOLVE CITIES & MUNICIPALITIES UNDER PROVINCE & HUCs
    for region in root.components:
        for province_or_huc in region.components:
            municipality_or_city_in_province_or_huc: pd.DataFrame = df[
                (df["province_or_huc"] == province_or_huc.name)
                & (df["region"] == region.name)
                & ~(df["province_or_huc_code"] == "000")
                & ~(df["municipal_or_city_code"] == "00")
                & (df["barangay_code"] == "000")
                & (df["province_or_huc"].notna())
                & (df["municipality_or_city"].notna())
            ]
            for idx, mun_or_city in municipality_or_city_in_province_or_huc.iterrows():
                try:
                    newloc = Location(
                        name=mun_or_city["name"],
                        type=mun_or_city["geographic_level"],
                        psgc_id=mun_or_city["psgc_id"],
                        parent_psgc_id=province_or_huc.psgc_id,
                    )
                    newflatloc = FlatLocation(
                        name=mun_or_city["name"],
                        type=mun_or_city["geographic_level"],
                        psgc_id=mun_or_city["psgc_id"],
                        parent_psgc_id=province_or_huc.psgc_id,
                    )

                except ValidationError as e:
                    print(e)
                    print("############## ERROR")
                    print(mun_or_city)
                province_or_huc.components.append(newloc)
                flat_dict.append(newflatloc)

    # RESOLVE BARANGAY IF ITS UNDER A MUNICIPALITY OR CITY AND UNDER A PROVINCE OR HUC
    for region in tqdm(root.components, leave=True, ascii=True):
        for province_or_huc in region.components:
            for municipality_or_city in province_or_huc.components:
                barangay_in_municipality_or_city: pd.DataFrame = df[
                    (df["municipality_or_city"] == municipality_or_city.name)
                    & (df["region"] == region.name)
                    & (df["province_or_huc"] == province_or_huc.name)
                    & ~(df["province_or_huc_code"] == "000")
                    & ~(df["municipal_or_city_code"] == "00")
                    & ~(df["barangay_code"] == "000")
                    & (df["province_or_huc"].notna())
                    & (df["municipality_or_city"].notna())
                ]
                for idx, barangay in barangay_in_municipality_or_city.iterrows():
                    try:
                        newloc = Location(
                            name=barangay["name"],
                            type=barangay["geographic_level"],
                            psgc_id=barangay["psgc_id"],
                            parent_psgc_id=municipality_or_city.psgc_id,
                        )
                        newflatloc = FlatLocation(
                            name=barangay["name"],
                            type=barangay["geographic_level"],
                            psgc_id=barangay["psgc_id"],
                            parent_psgc_id=municipality_or_city.psgc_id,
                        )
                    except ValidationError as e:
                        print(e)
                        print("############## ERROR")
                        print(barangay)
                    municipality_or_city.components.append(newloc)
                    flat_dict.append(newflatloc)

    # RESOLVE BARANGAYS DIRECTLY UNDER PROVINCE OR HUCS
    for region in tqdm(root.components, leave=True, ascii=True):
        for province_or_huc in region.components:
            barangay_in_province_or_huc: pd.DataFrame = df[
                (df["province_or_huc"] == province_or_huc.name)
                & (df["region"] == region.name)
                & ~(df["province_or_huc_code"] == "000")
                & (df["municipal_or_city_code"] == "00")
                & ~(df["barangay_code"] == "000")
                & (df["province_or_huc"].notna())
                & ~(df["municipality_or_city"].notna())
            ]
            for idx, barangay in barangay_in_province_or_huc.iterrows():
                try:
                    newloc = Location(
                        name=barangay["name"],
                        type=barangay["geographic_level"],
                        psgc_id=barangay["psgc_id"],
                        parent_psgc_id=province_or_huc.psgc_id,
                    )
                    newflatloc = FlatLocation(
                        name=barangay["name"],
                        type=barangay["geographic_level"],
                        psgc_id=barangay["psgc_id"],
                        parent_psgc_id=province_or_huc.psgc_id,
                    )
                except ValidationError as e:
                    print(e)
                    print("############## ERROR")
                    print(province_or_huc)
                province_or_huc.components.append(newloc)
                flat_dict.append(newflatloc)

    # RESOLVE BARANGAY UNDER MUNICIPALITY THAT IS UNDER REGIONS DIRECTLY
    for region in tqdm(root.components, leave=True, ascii=True):
        for municipality_or_city in region.components:
            barangay_in_municipality_or_city: pd.DataFrame = df[
                (df["municipality_or_city"] == municipality_or_city.name)
                & (df["region"] == region.name)
                & ~(df["province_or_huc_code"] == "000")
                & ~(df["municipal_or_city_code"] == "00")
                & ~(df["barangay_code"] == "000")
                & ~(df["province_or_huc"].notna())
                & (df["municipality_or_city"].notna())
            ]
            for idx, barangay in barangay_in_municipality_or_city.iterrows():
                try:
                    newloc = Location(
                        name=barangay["name"],
                        type=barangay["geographic_level"],
                        psgc_id=barangay["psgc_id"],
                        parent_psgc_id=municipality_or_city.psgc_id,
                    )
                    newflatloc = FlatLocation(
                        name=barangay["name"],
                        type=barangay["geographic_level"],
                        psgc_id=barangay["psgc_id"],
                        parent_psgc_id=municipality_or_city.psgc_id,
                    )
                except ValidationError as e:
                    print(e)
                    print("############## ERROR")
                    print(mun_or_city)
                municipality_or_city.components.append(newloc)
                flat_dict.append(newflatloc)
    return flat_dict


def transform_fuzzer(
    df: pd.DataFrame, geographic_level_map=GEOGRAPHIC_LEVEL_MAP
) -> pd.DataFrame:
    df: pd.DataFrame = transform_df(df, geographic_level_map=geographic_level_map)

    admin_df: pd.DataFrame = df[df["barangay_code"] == "000"]

    admin_psgc_to_type: dict[str, str] = dict(
        zip(admin_df["psgc_id"], admin_df["geographic_level"])
    )
    admin_psgc_to_name: dict[str, str] = dict(
        zip(admin_df["psgc_id"], admin_df["name"])
    )
    admin_psgc_to_type["1999900000"] = "special_geographic_area"
    admin_psgc_to_type["0990100000"] = "independent_component_city"

    prov_level: pd.Series = (
        (df["province_or_huc_code"] != "000")
        & (df["municipal_or_city_code"] == "00")
        & (df["barangay_code"] == "000")
    )
    prov_level_df: pd.DataFrame = df[prov_level]
    prov_mapper_to_type: dict[str, str] = dict(
        zip(prov_level_df["province_or_huc_mapper"], prov_level_df["geographic_level"])
    )
    prov_mapper_to_type["09901"] = "independent_component_city"
    prov_mapper_to_type["19999"] = "special_geographic_area"

    mun_level: pd.Series = (
        (df["province_or_huc_code"] != "000")
        & (df["municipal_or_city_code"] != "00")
        & (df["barangay_code"] == "000")
    )
    mun_level_df: pd.DataFrame = df[mun_level]
    mun_mapper_to_type: dict[str, str] = dict(
        zip(
            mun_level_df["municipal_or_city_mapper"],
            mun_level_df["geographic_level"],
        )
    )

    submun_df: pd.DataFrame = df[df["geographic_level"] == "submunicipality"]
    submun_mappers: set[str] = set(submun_df["psgc_id"].str[:-3].tolist())
    submun_psgc_to_name: dict[str, str] = dict(
        zip(submun_df["psgc_id"], submun_df["name"])
    )

    bdf: pd.DataFrame = df[df["geographic_level"] == "barangay"].copy()

    province_vals: list[str] = []
    huc_vals: list[str] = []
    icc_vals: list[str] = []
    cc_vals: list[str] = []
    municipality_vals: list[str] = []
    submunicipality_vals: list[str] = []
    sga_vals: list[str] = []

    for _, row in bdf.iterrows():
        prov_or_huc_name: str | None = row.get("province_or_huc")
        mun_or_city_name: str | None = row.get("municipality_or_city")

        province = ""
        huc = ""
        icc = ""
        cc = ""
        municipality = ""
        submunicipality = ""
        sga = ""

        resolved = False

        if pd.notna(prov_or_huc_name):
            prov_mapper: str = row["province_or_huc_mapper"]
            prov_type: str = prov_mapper_to_type.get(prov_mapper, "")

            if prov_type == "special_geographic_area":
                sga = prov_or_huc_name
            elif prov_type in _CITY_LEVELS:
                if pd.notna(mun_or_city_name):
                    mun_mapper: str = row["municipal_or_city_mapper"]
                    mun_type: str = mun_mapper_to_type.get(mun_mapper, "")
                    if mun_type in _CITY_LEVELS:
                        province = prov_or_huc_name
                        if mun_type == "highly_urbanized_city":
                            huc = mun_or_city_name
                        elif mun_type == "independent_component_city":
                            icc = mun_or_city_name
                        else:
                            cc = mun_or_city_name
                        resolved = True
                    else:
                        if prov_type == "highly_urbanized_city":
                            huc = prov_or_huc_name
                        elif prov_type == "independent_component_city":
                            icc = prov_or_huc_name
                        else:
                            cc = prov_or_huc_name
                else:
                    if prov_type == "highly_urbanized_city":
                        huc = prov_or_huc_name
                    elif prov_type == "independent_component_city":
                        icc = prov_or_huc_name
                    else:
                        cc = prov_or_huc_name
            else:
                province = prov_or_huc_name

        if not resolved and pd.notna(mun_or_city_name):
            mun_mapper = row["municipal_or_city_mapper"]
            mun_type: str = mun_mapper_to_type.get(mun_mapper, "")

            if mun_mapper in submun_mappers:
                submun_psgc: str = mun_mapper + "000"
                submunicipality = submun_psgc_to_name.get(submun_psgc, "")
                parent_psgc_id: str = submun_psgc[:7] + "000"
                parent_type: str = admin_psgc_to_type.get(parent_psgc_id, "")
                if parent_type in _CITY_LEVELS:
                    if parent_type == "highly_urbanized_city":
                        huc = admin_psgc_to_name.get(parent_psgc_id, "")
                    elif parent_type == "independent_component_city":
                        icc = admin_psgc_to_name.get(parent_psgc_id, "")
                    else:
                        cc = admin_psgc_to_name.get(parent_psgc_id, "")
            elif mun_type in _CITY_LEVELS:
                if mun_type == "highly_urbanized_city":
                    huc = mun_or_city_name
                elif mun_type == "independent_component_city":
                    icc = mun_or_city_name
                else:
                    cc = mun_or_city_name
            else:
                municipality = mun_or_city_name

        if pd.isna(prov_or_huc_name) and pd.notna(mun_or_city_name):
            mun_mapper = row["municipal_or_city_mapper"]
            mun_type = mun_mapper_to_type.get(mun_mapper, "")
            if mun_type == "municipality":
                municipality = mun_or_city_name

        province_vals.append(province)
        huc_vals.append(huc)
        icc_vals.append(icc)
        cc_vals.append(cc)
        municipality_vals.append(municipality)
        submunicipality_vals.append(submunicipality)
        sga_vals.append(sga)

    bdf["province"] = province_vals
    bdf["highly_urbanized_city"] = huc_vals
    bdf["independent_component_city"] = icc_vals
    bdf["component_city"] = cc_vals
    bdf["municipality"] = municipality_vals
    bdf["submunicipality"] = submunicipality_vals
    bdf["special_geographic_area"] = sga_vals

    result: pd.DataFrame = bdf[
        [
            "psgc_id",
            "name",
            "region",
            "province",
            "highly_urbanized_city",
            "independent_component_city",
            "component_city",
            "municipality",
            "submunicipality",
            "special_geographic_area",
        ]
    ].reset_index(drop=True)

    for col in [
        "province",
        "highly_urbanized_city",
        "independent_component_city",
        "component_city",
        "municipality",
        "submunicipality",
        "special_geographic_area",
    ]:
        result[col] = result[col].fillna("")

    result["barangay"] = result["name"]
    result = result.drop(columns=["name"])

    for pre_col in _PRE_CONCAT_COLS:
        result[pre_col] = result.apply(
            lambda row, c=pre_col: _build_pre_concat_value(row.to_dict(), c), axis=1
        )

    return result
