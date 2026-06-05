from typing import Any

__all__ = [
    "ExplodeError",
    "classify_plugins",
    "explode_array",
    "explode_flat",
    "flatten_scalar",
    "validate_single_array",
]


class ExplodeError(Exception):
    pass


def classify_plugins(
    plugin_index: dict[str, dict[str, dict[str, Any]]],
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    scalar_plugins: dict[str, list[str]] = {}
    array_plugins: dict[str, list[str]] = {}

    seen_types: dict[str, type] = {}

    for psgc_id, plugins in plugin_index.items():
        for plugin_name, entry in plugins.items():
            data = entry.get("data")
            if data is None:
                continue

            current_type = type(data)

            if plugin_name in seen_types:
                if seen_types[plugin_name] is not current_type:
                    raise ExplodeError(
                        f"Plugin '{plugin_name}' has inconsistent data types "
                        f"(found both dict and list)"
                    )
            else:
                seen_types[plugin_name] = current_type

            if isinstance(data, dict):
                for key in data.keys():
                    if plugin_name not in scalar_plugins:
                        scalar_plugins[plugin_name] = []
                    if key not in scalar_plugins[plugin_name]:
                        scalar_plugins[plugin_name].append(key)
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        for key in item.keys():
                            if plugin_name not in array_plugins:
                                array_plugins[plugin_name] = []
                            if key not in array_plugins[plugin_name]:
                                array_plugins[plugin_name].append(key)

    return scalar_plugins, array_plugins


def validate_single_array(array_plugins: dict[str, list[str]]) -> None:
    if len(array_plugins) > 1:
        names = ", ".join(sorted(array_plugins.keys()))
        raise ExplodeError(
            f"Cannot enable more than one array-type plugin (found: {names})"
        )


def flatten_scalar(
    record: dict[str, Any],
    plugin_index: dict[str, dict[str, dict[str, Any]]],
    scalar_plugins: dict[str, list[str]],
) -> dict[str, Any]:
    result = dict(record)
    psgc_id = str(record.get("psgc_id", ""))
    plugins = plugin_index.get(psgc_id, {})

    for plugin_name in scalar_plugins:
        entry = plugins.get(plugin_name)
        if entry is None:
            continue
        data = entry.get("data")
        if not isinstance(data, dict):
            continue
        for key, value in data.items():
            result[f"{plugin_name}.{key}"] = value

    return result


def explode_array(
    record: dict[str, Any],
    plugin_index: dict[str, dict[str, dict[str, Any]]],
    array_plugin_name: str,
) -> list[dict[str, Any]]:
    psgc_id = str(record.get("psgc_id", ""))
    plugins = plugin_index.get(psgc_id, {})
    entry = plugins.get(array_plugin_name)
    data = entry.get("data") if entry else None

    if not isinstance(data, list) or len(data) == 0:
        return [dict(record)]

    rows = []
    for item in data:
        row = dict(record)
        if isinstance(item, dict):
            for key, value in item.items():
                row[f"{array_plugin_name}.{key}"] = value
        rows.append(row)

    return rows


def explode_flat(
    flat_data: list[dict[str, Any]],
    plugin_index: dict[str, dict[str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    if not plugin_index:
        return [dict(r) for r in flat_data]

    scalar_plugins, array_plugins = classify_plugins(plugin_index)
    validate_single_array(array_plugins)

    array_plugin_name = next(iter(array_plugins)) if array_plugins else None

    output: list[dict[str, Any]] = []
    for record in flat_data:
        row = flatten_scalar(record, plugin_index, scalar_plugins)

        if array_plugin_name:
            rows = explode_array(row, plugin_index, array_plugin_name)
            output.extend(rows)
        else:
            output.append(row)

    return output
