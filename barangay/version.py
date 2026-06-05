from typing import Any


def use_version(as_of: str | None) -> None:
    """Switch the global Database to a specific data version.

    This invalidates the cache and triggers a reload on next access.

    Args:
        as_of: Date string (YYYY-MM-DD) or None for latest.

    Example:
        barangay.use_version("2025-07-08")
        brgy = barangay.barangays.get(psgc_id="1907005010")
        barangay.use_version(None)
    """
    from barangay.database import Database

    db = Database()
    db._version_state.set(as_of)
    db.invalidate_cache()


def use_plugins(
    plugins: list[str] | None = None,
    levels: list[Any] | None = None,
) -> None:
    """Enable plugins on the global Database singleton.

    Args:
        plugins: Plugin names to enable.
        levels: Restrict to specific admin levels.

    Example:
        barangay.use_plugins(["population"], levels=[barangay.AdminLevel.CITY])
    """
    from barangay.database import Database

    Database().use_plugins(plugins=plugins, levels=levels)
