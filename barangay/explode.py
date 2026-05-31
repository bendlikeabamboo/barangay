from typing import Any


class ExplodeError(Exception):
    """Raised when explode constraints are violated."""

    pass


def classify_plugins(
    plugin_index: dict[str, dict[str, dict[str, Any]]],
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Classify plugins into scalar (dict) and array (list) types.

    Args:
        plugin_index: psgc_id -> {plugin_name: {metadata, data}}

    Returns:
        Tuple of (scalar_plugins, array_plugins), each mapping
        plugin_name to a list of field names discovered across all records.
    """
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
    """Raise ExplodeError if more than one array plugin is present.

    Args:
        array_plugins: Mapping of array plugin name to field names.

    Raises:
        ExplodeError: If len(array_plugins) > 1.
    """
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
    """Merge scalar plugin fields into the record with "plugin.field" keys.

    Args:
        record: A single flat record (dict).
        plugin_index: psgc_id -> {plugin_name: {metadata, data}}
        scalar_plugins: Mapping of scalar plugin names to field names.

    Returns:
        New record dict with scalar plugin fields merged in.
    """
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
    """Cross-join a record with each element of its array plugin data.

    Args:
        record: A single flat record (dict).
        plugin_index: psgc_id -> {plugin_name: {metadata, data}}
        array_plugin_name: Name of the single array plugin to explode.

    Returns:
        List of records, one per array element. If no array data exists for
        the record, returns a list with the original record (no array columns).
    """
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
    """Orchestrate the explode pipeline: classify, validate, flatten, explode.

    Args:
        flat_data: List of flat records (dicts).
        plugin_index: psgc_id -> {plugin_name: {metadata, data}}

    Returns:
        Final 3NF-ready row set as a list of dicts.
    """
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
