from typing import Any, Iterator


from barangay.models import AdminDivRecord, AdminLevel, PluginExtensionMetadata


class MultipleResultsError(Exception):
    """Raised when a name lookup matches multiple records."""

    pass


class PluginAccessor:
    """Attribute-accessible wrapper for a plugin's data dict."""

    __slots__ = ("_data", "_metadata")

    def __init__(
        self,
        data: dict[str, Any] | list[dict[str, Any]],
        metadata: PluginExtensionMetadata,
    ) -> None:
        self._data = data
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        try:
            return self._data[name]
        except (KeyError, TypeError) as e:
            raise AttributeError(
                f"Plugin '{self._metadata.name}' has no field '{name}'. "
                f"Available: {list(self._data.keys()) if isinstance(self._data, dict) else 'N/A (array plugin)'}"
            ) from e

    def __repr__(self) -> str:
        return f"<plugin:{self._metadata.name}>"

    def __bool__(self) -> bool:
        return bool(self._data)

    def to_dict(self) -> dict | list:
        return self._data

    @property
    def metadata(self) -> PluginExtensionMetadata:
        return self._metadata

    @property
    def is_array(self) -> bool:
        return isinstance(self._data, list)

    @property
    def rows(self) -> list[dict]:
        if isinstance(self._data, list):
            return list(self._data)
        return [self._data]


class HierarchyIndex:
    """Bidirectional index for PSGC hierarchy traversal."""

    def __init__(self, records: list[AdminDivRecord]) -> None:
        self._by_id: dict[str, AdminDivRecord] = {}
        self._children: dict[str, list[AdminDivRecord]] = {}

        for record in records:
            self._by_id[record.psgc_id] = record
            self._children.setdefault(record.parent_psgc_id, []).append(record)

    def get(self, psgc_id: str) -> AdminDivRecord | None:
        return self._by_id.get(psgc_id)

    def parent(self, record: AdminDivRecord) -> AdminDivRecord | None:
        if record.parent_psgc_id == "n/a":
            return None
        return self._by_id.get(record.parent_psgc_id)

    def children(self, psgc_id: str) -> list[AdminDivRecord]:
        return list(self._children.get(psgc_id, []))

    def ancestors(self, record: AdminDivRecord) -> list[AdminDivRecord]:
        chain: list[AdminDivRecord] = []
        current = self.parent(record)
        while current is not None:
            chain.append(current)
            current = self.parent(current)
        return chain

    def resolve_region(self, record: AdminDivRecord) -> AdminDivRecord | None:
        for ancestor in self.ancestors(record):
            if ancestor.type == AdminLevel.REGION:
                return ancestor
        return record if record.type == AdminLevel.REGION else None

    def resolve_province(self, record: AdminDivRecord) -> AdminDivRecord | None:
        for ancestor in self.ancestors(record):
            if ancestor.type == AdminLevel.PROVINCE:
                return ancestor
        return record if record.type == AdminLevel.PROVINCE else None

    def resolve_municipality(self, record: AdminDivRecord) -> AdminDivRecord | None:
        for ancestor in self.ancestors(record):
            if ancestor.type in (AdminLevel.MUNICIPALITY, AdminLevel.SUBMUNICIPALITY):
                return ancestor
        return (
            record
            if record.type
            in (
                AdminLevel.MUNICIPALITY,
                AdminLevel.SUBMUNICIPALITY,
            )
            else None
        )

    def resolve_city(self, record: AdminDivRecord) -> AdminDivRecord | None:
        for ancestor in self.ancestors(record):
            if ancestor.type == AdminLevel.CITY:
                return ancestor
        return record if record.type == AdminLevel.CITY else None

    def records_of_type(self, level: AdminLevel) -> list[AdminDivRecord]:
        return [r for r in self._by_id.values() if r.type == level]


class _EnrichedRecord:
    """Wraps an AdminDivRecord with computed hierarchy properties."""

    __slots__ = ("_record", "_index")

    def __init__(self, record: AdminDivRecord, index: HierarchyIndex) -> None:
        self._record = record
        self._index = index

    def __getattr__(self, name: str):
        for ext in self._record.extensions:
            if ext.field_group == name:
                return PluginAccessor(ext.data, ext.metadata)

        try:
            return getattr(self._record, name)
        except AttributeError:
            raise AttributeError(
                f"'{type(self).__name__}' has no attribute '{name}'. "
                f"Is '{name}' a plugin? Ensure it's enabled via use_plugins()."
            )

    @property
    def region(self) -> str | None:
        r = self._index.resolve_region(self._record)
        return r.name if r else None

    @property
    def province(self) -> str | None:
        r = self._index.resolve_province(self._record)
        return r.name if r else None

    @property
    def municipality(self) -> str | None:
        r = self._index.resolve_municipality(self._record)
        return r.name if r else None

    @property
    def city(self) -> str | None:
        r = self._index.resolve_city(self._record)
        return r.name if r else None

    @property
    def parent(self) -> "_EnrichedRecord | None":
        p = self._index.parent(self._record)
        if p is None:
            return None
        return _EnrichedRecord(p, self._index)

    @property
    def children(self) -> list["_EnrichedRecord"]:
        return [
            _EnrichedRecord(c, self._index)
            for c in self._index.children(self._record.psgc_id)
        ]

    @property
    def ancestors(self) -> list["_EnrichedRecord"]:
        return [
            _EnrichedRecord(a, self._index) for a in self._index.ancestors(self._record)
        ]

    def __repr__(self) -> str:
        return (
            f"<{self._record.type.value}: {self._record.name} ({self._record.psgc_id})>"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, _EnrichedRecord):
            return self._record.psgc_id == other._record.psgc_id
        if isinstance(other, AdminDivRecord):
            return self._record.psgc_id == other.psgc_id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self._record.psgc_id)

    def to_dict(self) -> dict:
        d = self._record.model_dump()
        d["region"] = self.region
        d["province"] = self.province
        d["municipality"] = self.municipality
        d["city"] = self.city
        return d


class _DatabaseView:
    """A filtered, iterable view over PSGC records of a specific admin level."""

    def __init__(
        self,
        *,
        records: list[AdminDivRecord],
        index: HierarchyIndex,
        level: AdminLevel | None,
        plugin_index: dict[str, dict[str, dict[str, Any]]] | None,
        version_state: "_VersionState",
    ) -> None:
        self._all_records = records
        self._index = index
        self._level = level
        self._plugin_index = plugin_index
        self._version_state = version_state

    def _filtered(self) -> list[AdminDivRecord]:
        if self._level is None:
            return self._all_records
        return [r for r in self._all_records if r.type == self._level]

    def get(
        self, *, psgc_id: str | None = None, name: str | None = None
    ) -> _EnrichedRecord | None:
        if psgc_id is not None and name is not None:
            raise ValueError("Provide exactly one of psgc_id or name, not both.")
        if psgc_id is None and name is None:
            raise ValueError("Provide exactly one of psgc_id or name.")

        if psgc_id is not None:
            record = self._index.get(psgc_id)
            if record is None:
                return None
            if self._level is not None and record.type != self._level:
                return None
            return _EnrichedRecord(record, self._index)

        if name is not None:
            candidates = [r for r in self._filtered() if r.name == name]
            if not candidates:
                return None
            if len(candidates) > 1:
                raise MultipleResultsError(
                    f"Name '{name}' matched {len(candidates)} records. "
                    f"Use psgc_id for exact lookup, or iterate."
                )
            return _EnrichedRecord(candidates[0], self._index)

        return None

    def lookup(self, psgc_id: str) -> _EnrichedRecord | None:
        record = self._index.get(psgc_id)
        if record is None:
            return None
        return _EnrichedRecord(record, self._index)

    def search_fuzzy(
        self,
        query: str,
        *,
        threshold: float = 60.0,
        limit: int = 5,
        as_of: str | None = None,
    ) -> list:
        from barangay.search import _search_fuzzy_new

        return _search_fuzzy_new(
            query,
            level=self._level,
            threshold=threshold,
            limit=limit,
            index=self._index,
            as_of=as_of or self._version_state.as_of,
        )

    def __iter__(self) -> Iterator[_EnrichedRecord]:
        for record in self._filtered():
            yield _EnrichedRecord(record, self._index)

    def __len__(self) -> int:
        return len(self._filtered())

    def __contains__(self, psgc_id: str) -> bool:
        record = self._index.get(psgc_id)
        if record is None:
            return False
        if self._level is not None and record.type != self._level:
            return False
        return True

    def __repr__(self) -> str:
        level_name = self._level.value if self._level else "all"
        return f"<PSGC {level_name} database: {len(self)} records>"

    def _should_explode(self) -> bool:
        if not self._plugin_index:
            return False
        from barangay.explode import classify_plugins

        _, array_plugins = classify_plugins(self._plugin_index)
        return len(array_plugins) > 0

    def to_dicts(self) -> list[dict]:
        if self._should_explode():
            from barangay.explode import explode_flat

            raw = [r._record.model_dump() for r in self]
            return explode_flat(raw, self._plugin_index)
        else:
            result = []
            for enriched in self:
                d = enriched.to_dict()
                for ext in enriched._record.extensions:
                    if isinstance(ext.data, dict):
                        for k, v in ext.data.items():
                            d[f"{ext.field_group}.{k}"] = v
                result.append(d)
            return result

    def to_frame(self):
        import pandas as pd

        dicts = self.to_dicts()
        return pd.DataFrame(dicts)


class _VersionState:
    """Manages the active data version for the Database singleton."""

    def __init__(self) -> None:
        self.as_of: str | None = None

    def set(self, as_of: str | None) -> None:
        if as_of is not None:
            from barangay.date_resolver import get_available_dates, resolve_date

            from pathlib import Path

            data_dir = Path(__file__).parent / "data"
            version_path = data_dir / "CURRENT_VERSION"
            current_date = (
                version_path.read_text().strip()
                if version_path.exists()
                else "2026-04-13"
            )
            available = get_available_dates() + [current_date]
            resolved, _ = resolve_date(as_of, available, current_date)
            if resolved is None:
                raise ValueError(
                    f"No data available for date '{as_of}'. Available: {available}"
                )
            self.as_of = resolved
        else:
            self.as_of = None


class Database:
    """Central PSGC data access point."""

    _instance: "Database | None" = None

    def __new__(cls) -> "Database":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            object.__setattr__(cls._instance, "_initialized", False)
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        object.__setattr__(self, "_initialized", True)
        object.__setattr__(self, "_version_state", _VersionState())
        object.__setattr__(self, "_cache_key", "default")
        object.__setattr__(self, "_raw_records", None)
        object.__setattr__(self, "_index", None)
        object.__setattr__(self, "_plugin_loader", None)
        object.__setattr__(self, "_plugin_levels", [])
        object.__setattr__(self, "_plugin_index", None)

    @property
    def regions(self) -> _DatabaseView:
        return self._view(AdminLevel.REGION)

    @property
    def provinces(self) -> _DatabaseView:
        return self._view(AdminLevel.PROVINCE)

    @property
    def municipalities(self) -> _DatabaseView:
        return self._view(AdminLevel.MUNICIPALITY)

    @property
    def cities(self) -> _DatabaseView:
        return self._view(AdminLevel.CITY)

    @property
    def submunicipalities(self) -> _DatabaseView:
        return self._view(AdminLevel.SUBMUNICIPALITY)

    @property
    def barangays(self) -> _DatabaseView:
        return self._view(AdminLevel.BARANGAY)

    @property
    def special_geographic_areas(self) -> _DatabaseView:
        return self._view(AdminLevel.SPECIAL_GEOGRAPHIC_AREA)

    @property
    def all_records(self) -> _DatabaseView:
        return self._view(None)

    def _ensure_loaded(self) -> None:
        if self._raw_records is not None:
            return

        from barangay.data import load_barangay_flat_data

        as_of = self._version_state.as_of
        flat_models = load_barangay_flat_data(as_of=as_of)

        plugin_levels: list[AdminLevel] = self._plugin_levels
        plugin_loader = self._plugin_loader

        if plugin_loader is not None and plugin_levels:
            flat_dicts = [f.model_dump() for f in flat_models]
            index = plugin_loader.build_index(as_of=as_of)
            from barangay.plugin_loader import enrich_flat

            enriched = enrich_flat(flat_dicts, index)
            self._raw_records = []
            for i, flat in enumerate(flat_models):
                if flat.type in [lvl.value for lvl in plugin_levels]:
                    self._raw_records.append(AdminDivRecord.model_validate(enriched[i]))
                else:
                    self._raw_records.append(
                        AdminDivRecord.model_validate(flat.model_dump())
                    )
        elif plugin_loader is not None:
            flat_dicts = [f.model_dump() for f in flat_models]
            enriched = plugin_loader.enrich_flat(flat_dicts, as_of=as_of)
            from barangay.models import AdminDivFlat

            flat_models = [AdminDivFlat.model_validate(d) for d in enriched]
            self._raw_records = [
                AdminDivRecord.model_validate(f.model_dump()) for f in flat_models
            ]
        else:
            self._raw_records = [
                AdminDivRecord.model_validate(f.model_dump()) for f in flat_models
            ]

        self._index = HierarchyIndex(self._raw_records)

        if plugin_loader is not None:
            object.__setattr__(
                self, "_plugin_index", plugin_loader.build_index(as_of=as_of)
            )
        else:
            object.__setattr__(self, "_plugin_index", None)

    def _view(self, level: AdminLevel | None) -> _DatabaseView:
        self._ensure_loaded()
        return _DatabaseView(
            records=self._raw_records,
            index=self._index,
            level=level,
            plugin_index=self._plugin_index,
            version_state=self._version_state,
        )

    def invalidate_cache(self) -> None:
        object.__setattr__(self, "_raw_records", None)
        object.__setattr__(self, "_index", None)

    def use_plugins(
        self,
        plugins: list[str] | None = None,
        levels: list[AdminLevel] | None = None,
        loader=None,
    ) -> None:
        if loader is None:
            from barangay.plugin_loader import PluginLoader

            loader = PluginLoader()
            if plugins:
                for name in plugins:
                    loader.enable_plugin(name)

        object.__setattr__(self, "_plugin_loader", loader)
        object.__setattr__(self, "_plugin_levels", levels or [])
        self.invalidate_cache()

    def available_plugins(self) -> list:
        from barangay.models import PluginInfo
        from barangay.plugin_loader import (
            load_manifest,
            load_plugin_config,
            resolve_plugin_sources,
        )

        config = load_plugin_config()
        dirs = resolve_plugin_sources()
        infos = []

        for name, enabled in config.items():
            try:
                manifest = load_manifest(name, dirs)
            except Exception:
                infos.append(
                    PluginInfo(
                        name=name, enabled=enabled, error="Failed to load manifest"
                    )
                )
                continue

            infos.append(
                PluginInfo(
                    name=name,
                    enabled=enabled,
                    description=manifest.get("description"),
                    version=manifest.get("version"),
                    format=manifest.get("format"),
                    repository=manifest.get("repository"),
                )
            )

        return infos

    def active_plugins(self) -> list[str]:
        return [p.name for p in self.available_plugins() if p.enabled]
