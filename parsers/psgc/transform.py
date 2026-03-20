from typing import Any, Dict, List, Set

import pandas as pd
from tqdm import tqdm
from pydantic import ValidationError

from parsers.psgc.models import FlatLocation, Location
from parsers.psgc.constants import GEOGRAPHIC_LEVEL_MAP


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
    ].sort_values(by=["region", "province_or_huc", "municipality_or_city"])

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
            if prov_or_huc["psgc_id"] == "0990100000":
                prov_or_huc["geographic_level"] = "city"
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
        df=df, geographic_level_map=GEOGRAPHIC_LEVEL_MAP
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
            if prov_or_huc["psgc_id"] == "0990100000":
                prov_or_huc["geographic_level"] = "city"
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


def transform_fuzzer(df: pd.DataFrame, geographic_level_map=GEOGRAPHIC_LEVEL_MAP):
    df: pd.DataFrame = transform_df(df, geographic_level_map=geographic_level_map)
    bdf: pd.DataFrame = df[df["geographic_level"] == "barangay"]
    fuzzer_base: pd.DataFrame = bdf[
        ["name", "province_or_huc", "municipality_or_city", "psgc_id"]
    ]
    fuzzer_base: pd.DataFrame = fuzzer_base.rename({"name": "barangay"}, axis=1)
    return fuzzer_base
