# Plugins

Plugins extend `barangay` by enriching PSGC records with supplementary data. Each plugin is a data package keyed by `psgc_id` that is joined onto the flat data model — adding fields like population, income classification, old names, and more.

## How Plugins Work

Plugins are **data packages** — not code. Each plugin provides a data file (JSON, CSV, or Parquet) keyed by `psgc_id`, and the plugin loader joins that data onto PSGC records at query time.

There are two plugin shapes:

| Type | Description | Limit |
|------|-------------|-------|
| **Scalar** | Each `psgc_id` maps to a single object. Fields are flattened as `plugin_name.field`. | No limit on simultaneous scalar plugins |
| **Array** | Each `psgc_id` maps to a list of objects. Each element is cross-joined with the base record. | Only **one** array plugin active at a time |

## Entry Points

The plugin system can be accessed through three entry points:

| Entry Point | Best For | See |
|-------------|----------|-----|
| **CLI** (`barangay search` / `barangay export`) | Quick one-off enrichment, scripting | [CLI Reference](cli.md) |
| **Python API** (`PluginLoader`) | Programmatic use in applications | [Python API](python_api.md) |
| **Configuration** (`BARANGAY_PLUGINS_DIR`, `barangay.yaml`) | Persistent setup across sessions | [Configuration](configuration.md) |

## Quick Start

The **psgc-aux-data** plugin is enabled by default. It ships supplementary PSGC metadata from official PSA releases.

### CLI

```bash
barangay search "City of Lapu-Lapu" --plugin psgc-aux-data --format json --limit 1
```

```json
[
  {
    "barangay": "Ibo",
    "province_or_huc": "City of Lapu-Lapu",
    "municipality_or_city": null,
    "psgc_id": "0731100013",
    "f_0p0b_ratio_score": 80.0,
    "f_00mb_ratio_score": 0.0,
    "f_0pmb_ratio_score": 64.0,
    "000b": "ibo",
    "0p0b": "lapulapu ibo",
    "00mb": "none ibo",
    "0pmb": "lapulapu none ibo",
    "psgc-aux-data.correspondence_code": "0072226013",
    "psgc-aux-data.old_names": null,
    "psgc-aux-data.city_class": null,
    "psgc-aux-data.income_classification": null,
    "psgc-aux-data.urban_rural": "U",
    "psgc-aux-data.population": 7453,
    "psgc-aux-data.status": null
  }
]
```

### Python API

```python
from barangay import barangay_flat
from barangay.plugin_loader import PluginLoader

loader = PluginLoader(env=True)
loader.enable_plugin("psgc-aux-data")

enriched = loader.enrich_flat([r.model_dump() for r in barangay_flat])

for r in enriched:
    if r.get("extensions"):
        print(r["name"], r["extensions"][0]["data"])
        break
```

```text
Bangsamoro Autonomous Region In Muslim Mindanao (BARMM) {'correspondence_code': '0150000000', 'old_names': None, 'city_class': None, 'income_classification': None, 'urban_rural': None, 'population': 4545486, 'status': None}
```

## Plugin Directory Structure

Each plugin lives in its own subdirectory within a plugin source directory:

```
plugins/
├── plugins.yaml              # plugin activation config
├── psgc-aux-data/
│   └── manifest.yaml         # plugin metadata (remote — no local data/)
├── sample_elevation/
│   ├── manifest.yaml
│   └── data/
│       └── sample_elevation.csv
├── sample_population/
│   ├── manifest.yaml
│   └── data/
│       ├── 2020-01-01/
│       │   └── sample_population.json
│       └── 2023-01-01/
│           └── sample_population.json
└── sample_schools/
    ├── manifest.yaml
    └── data/
        ├── 2024-04-13/
        │   └── sample_schools.json
        └── 2024-07-13/
            └── sample_schools.json
```

## Manifest File

Every plugin must have a `manifest.yaml`:

```yaml
name: psgc-aux-data                          # required
description: Supplementary PSGC data...     # optional
version: 0.1.0                               # optional
format: json                                # required: csv | json | parquet
key: psgc_id                                # required: join key column
repository: https://github.com/user/repo    # optional: remote data source
ref: main                                    # optional: git ref (default: main)
current: "2026-04-13"                       # optional: current version date
dates:                                       # optional: available snapshot dates
  - "2021-08-19"
  - "2026-04-13"
```

## Data Formats

Plugins support three data formats. The key column (`psgc_id` by default) is used for joining and is excluded from the output fields.

**JSON** — an array of objects:

```json
[
  { "psgc_id": "0731100000", "correspondence_code": "0072226000", "old_names": "Opon", "population": 497813 }
]
```

**CSV** — a headered CSV file:

```csv
psgc_id,correspondence_code,old_names,population
0731100000,0072226000,Opon,497813
```

**Parquet** — a Parquet file with the same column layout.

## Remote Plugins

Plugins with a `repository` field in their manifest fetch data from GitHub. The file is downloaded and cached locally. Time-aware remote plugins list date directories via the GitHub API.

When using `--as-of`, the loader resolves to the closest available plugin date that is `<=` the requested date.

## Time-Aware Plugins

A plugin is time-aware if its data directory contains `YYYY-MM-DD/` subdirectories (local) or declares `dates` in its manifest (remote). When `--as-of` is not specified, the `current` date from the manifest is used.

## Built-in Plugins

| Plugin | Enabled | Type | Description |
|--------|---------|------|-------------|
| `psgc-aux-data` | Yes | Scalar, JSON, remote, time-aware | Supplementary PSGC data from official PSA releases |
| `sample_elevation` | No | Scalar, CSV, local, non-time-aware | Average elevation by province (demo) |
| `sample_population` | No | Scalar, JSON, local, time-aware | Population counts by city/municipality (demo) |
| `sample_schools` | No | Array, JSON, local, time-aware | BEISS school records per barangay (demo) |
| `sample_elevation_time` | No | Scalar, JSON, local, time-aware | Elevation data with date folders (demo) |

See [Built-in Plugins](built-in.md) for detailed field references.

## Next Steps

- [CLI Reference](cli.md) — Using plugins with `barangay search` and `barangay export`
- [Python API](python_api.md) — Programmatic enrichment with `PluginLoader`
- [Configuration](configuration.md) — Environment variables, config files, plugin discovery
- [Creating a Plugin](creating.md) — Step-by-step guide to building your own plugin
- [Built-in Plugins](built-in.md) — Field reference for bundled plugins
