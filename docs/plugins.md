# Plugins

Plugins extend `barangay` by enriching PSGC records with supplementary data. Each plugin is a data package keyed by `psgc_id` that is joined onto the flat data model — adding fields like population, income classification, old names, and more.

## Quick Start

The **psgc-aux-data** plugin is enabled by default. It ships supplementary PSGC metadata (correspondence codes, old names, city class, income classification, urban/rural, population, status) from official PSA releases.

### Search with plugin enrichment

```bash
barangay search "City of Lapu-Lapu" --plugin psgc-aux-data --format json --limit 1
```

Output:

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

The `psgc-aux-data.*` fields are injected by the plugin. Fields that are not applicable for a given record (e.g., `city_class` on a barangay) appear as `null`.

### Table output

```bash
barangay search "Tondo" --plugin psgc-aux-data --format table --limit 5 --threshold 50
```

Output:

```
                           Search Results for 'Tondo'                           
┏━━━━━━┳━━━━━━┳━━━━━┳━━━━━━┳━━━━━┳━━━━━━┳━━━━━┳━━━━━━┳━━━━━┳━━━━━━┳━━━━━┳━━━━━━┓
┃      ┃      ┃     ┃ PSGC ┃     ┃      ┃     ┃      ┃     ┃      ┃     ┃      ┃
┃ Bar… ┃ Mun… ┃ Pr… ┃ ID   ┃ Sc… ┃ psg… ┃ ps… ┃ psg… ┃ ps… ┃ psg… ┃ ps… ┃ psg… ┃
┡━━━━━━╇━━━━━━╇━━━━━╇━━━━━━╇━━━━━╇━━━━━━╇━━━━━╇━━━━━━╇━━━━━╇━━━━━━╇━━━━━╇━━━━━━┩
│ Ton… │ Anda │ Pa… │ 010… │ 62… │ 001… │ No… │ None │ No… │ R    │ 35… │ None │
│ Uni… │ Tago │ Su… │ 160… │ 62… │ 016… │ No… │ None │ No… │ R    │ 13… │ None │
│      │      │ del │      │     │      │     │      │     │      │     │      │
│      │      │ Sur │      │     │      │     │      │     │      │     │      │
│ Pudo │ Nat… │ Mo… │ 140… │ 58… │ 014… │ No… │ None │ No… │ R    │ 572 │ None │
│      │      │ Pr… │      │     │      │     │      │     │      │     │      │
│ Ton… │ Tan… │ Ak… │ 060… │ 58… │ 006… │ No… │ None │ No… │ R    │ 21… │ None │
│ Bato │      │ Ci… │ 113… │ 57… │ 011… │ No… │ None │ No… │ U    │ 12… │ None │
│      │      │ of  │      │     │      │     │      │     │      │     │      │
│      │      │ Da… │      │     │      │     │      │     │      │     │      │
└──────┴──────┴─────┴──────┴─────┴──────┴─────┴──────┴─────┴──────┴─────┴──────┘
```

Plugin columns are automatically appended to the table. The columns shown are: `psgc-aux-data.correspondence_code`, `psgc-aux-data.old_names`, `psgc-aux-data.city_class`, `psgc-aux-data.income_classification`, `psgc-aux-data.urban_rural`, `psgc-aux-data.population`, `psgc-aux-data.status`.

### Export with plugins

Export the flat model with plugin data merged into every record. Use `--model flat` (plugins are only supported with the flat model):

```bash
barangay export --model flat --plugin psgc-aux-data --format json --output enriched.json
```

Each record now includes plugin fields directly:

```json
[
  {
    "name": "City of Lapu-Lapu",
    "type": "city",
    "psgc_id": "0731100000",
    "parent_psgc_id": "0700000000",
    "nicknames": null,
    "psgc-aux-data.correspondence_code": "0072226000",
    "psgc-aux-data.old_names": "Opon",
    "psgc-aux-data.city_class": "HUC",
    "psgc-aux-data.income_classification": "1st",
    "psgc-aux-data.urban_rural": null,
    "psgc-aux-data.population": 497813,
    "psgc-aux-data.status": null
  }
]
```

CSV export works the same way:

```bash
barangay export --model flat --plugin psgc-aux-data --format csv --output enriched.csv
```

CSV header:

```csv
name,type,psgc_id,parent_psgc_id,nicknames,psgc-aux-data.correspondence_code,psgc-aux-data.old_names,psgc-aux-data.city_class,psgc-aux-data.income_classification,psgc-aux-data.urban_rural,psgc-aux-data.population,psgc-aux-data.status
Bangsamoro Autonomous Region In Muslim Mindanao (BARMM),region,1900000000,0000000000,,0150000000,,,,,4545486,
Cordillera Administrative Region (CAR),region,1400000000,0000000000,,0140000000,,,,,1808985,
```

### Historical plugin data

The `psgc-aux-data` plugin is time-aware — it provides snapshots matching PSGC release dates. Use `--as-of` to fetch the supplementary data that was current at that date:

```bash
barangay export --model flat --plugin psgc-aux-data --format json --as-of "2025-08-29" --output enriched_2025.json
```

Output (first two barangay records):

```json
[
  {
    "name": "Arco",
    "type": "barangay",
    "psgc_id": "1900702001",
    "parent_psgc_id": "1900702000",
    "nicknames": null,
    "psgc-aux-data.correspondence_code": "0150702001",
    "psgc-aux-data.old_names": null,
    "psgc-aux-data.city_class": null,
    "psgc-aux-data.income_classification": null,
    "psgc-aux-data.urban_rural": "R",
    "psgc-aux-data.population": 1224,
    "psgc-aux-data.status": null
  },
  {
    "name": "Ba-as",
    "type": "barangay",
    "psgc_id": "1900702002",
    "parent_psgc_id": "1900702000",
    "nicknames": null,
    "psgc-aux-data.correspondence_code": "0150702002",
    "psgc-aux-data.old_names": null,
    "psgc-aux-data.city_class": null,
    "psgc-aux-data.income_classification": null,
    "psgc-aux-data.urban_rural": "R",
    "psgc-aux-data.population": 2268,
    "psgc-aux-data.status": null
  }
]
```

### Multiple plugins

You can enable multiple plugins at once by repeating the `--plugin` flag:

```bash
barangay export --model flat --plugin psgc-aux-data --plugin sample_elevation --format json --output multi.json
```

!!! warning
    Only one array-type plugin can be active at a time. Scalar plugins (where each `psgc_id` maps to a single dict of fields) have no limit.

---

## How Plugins Work

### Plugin discovery

Plugins are discovered from these sources, in order of priority (lowest to highest):

1. **Built-in plugins directory** — `{package}/barangay/plugins/`
2. **`BARANGAY_PLUGINS_DIR` environment variable** — one or more directories separated by your OS path separator (`:` on Linux/Mac, `;` on Windows)
3. **Project config file** — `barangay.yaml` or `barangay_config.yaml` in your project root (or any parent directory), under the `plugin_dirs` key
4. **Programmatic extra dirs** — passed to `PluginLoader(extra_dirs=[...])`

### Plugin configuration

A `plugins.yaml` file in each plugin source directory controls which plugins are active:

```yaml
# barangay/plugins/plugins.yaml
plugins:
  - name: psgc-aux-data
    enabled: true
  - name: sample_elevation
    enabled: false
  - name: sample_population
    enabled: false
```

Higher-priority sources override the `enabled` status of lower-priority ones. When using `--plugin` on the CLI, the specified plugins are enabled on top of whatever the config files say.

### Plugin directory structure

Each plugin lives in its own subdirectory within a plugin source directory:

```
plugins/
├── plugins.yaml              # plugin activation config
├── psgc-aux-data/
│   └── manifest.yaml         # plugin metadata
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

### Manifest file

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
  - "2022-04-29"
  - "2026-04-13"
```

### Data formats

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

### Scalar vs array plugins

- **Scalar plugins** map each `psgc_id` to a single object (dict). Fields are flattened into the record with `plugin_name.field` keys. There is no limit on how many scalar plugins can be active simultaneously.

- **Array plugins** map each `psgc_id` to a list of objects. Each element is cross-joined with the base record, producing multiple rows per `psgc_id`. Only one array plugin can be active at a time.

### Remote plugins

Plugins with a `repository` field in their manifest fetch data from GitHub. The file is downloaded and cached locally. Time-aware remote plugins list date directories via the GitHub API.

When using `--as-of`, the loader resolves to the closest available plugin date that is <= the requested date.

### Time-aware plugins

A plugin is time-aware if its data directory contains `YYYY-MM-DD/` subdirectories (local) or declares `dates` in its manifest (remote). When `--as-of` is not specified, the `current` date from the manifest is used.

---

## Built-in Plugins

### psgc-aux-data (enabled by default)

Supplementary PSGC data sourced from official PSA releases.

| Field | Description |
|-------|-------------|
| `correspondence_code` | Legacy PSA correspondence code |
| `old_names` | Previous official name (if renamed) |
| `city_class` | City classification (e.g., `HUC`, `ICC`, `Component`) |
| `income_classification` | Income class (e.g., `1st`, `2nd`–`6th`) |
| `urban_rural` | `U` (urban) or `R` (rural), null for non-barangay levels |
| `population` | Population count |
| `status` | Special status (e.g., `Capital`) |

Source: [github.com/bendlikeabamboo/psgc-aux-data-repository](https://github.com/bendlikeabamboo/psgc-aux-data-repository)

### Sample plugins (disabled by default)

These are bundled for demonstration only. They contain fabricated data — do not use for real analysis.

| Plugin | Type | Description |
|--------|------|-------------|
| `sample_elevation` | Scalar, CSV, non-time-aware | Average elevation by province |
| `sample_population` | Scalar, JSON, time-aware | Population counts by city/municipality |
| `sample_elevation_time` | Scalar, JSON, time-aware | Elevation data with `YYYY-MM-DD/` folder layout |
| `sample_schools` | Array, JSON, time-aware | BEISS school records per barangay |

---

## Python API

### Enriching flat data programmatically

```python
from barangay import barangay_flat
from barangay.plugin_loader import PluginLoader

loader = PluginLoader(env=True)
loader.enable_plugin("psgc-aux-data")

plugin_index = loader.build_index()
enriched = loader.enrich_flat(barangay_flat)

print(enriched[0])
```

### Enriching extended (tree) data

```python
from barangay import barangay_extended
from barangay.plugin_loader import PluginLoader

loader = PluginLoader(env=True)
loader.enable_plugin("psgc-aux-data")

plugin_index = loader.build_index()
enriched = loader.enrich_extended(barangay_extended.model_dump())
```

### Using the low-level `enrich_flat` function

```python
from barangay.plugin_loader import build_plugin_index, enrich_flat
from barangay import barangay_flat

plugin_index = build_plugin_index()  # uses default config
enriched = enrich_flat(barangay_flat, plugin_index)
```

### Adding custom plugin directories

```python
from barangay.plugin_loader import PluginLoader

loader = PluginLoader(env=True)
loader.add_plugin_dir("/path/to/my/plugins")
loader.enable_plugin("my_custom_plugin")

enriched = loader.enrich_flat(flat_data, as_of="2025-08-29")
```

---

## Environment Variable

### BARANGAY_PLUGINS_DIR

Set one or more directories to scan for plugins. Multiple paths are separated by the OS path separator:

```bash
# Linux / macOS
export BARANGAY_PLUGINS_DIR="/opt/barangay-plugins:/home/user/custom-plugins"

# Windows
set BARANGAY_PLUGINS_DIR=C:\barangay-plugins;D:\custom-plugins
```

---

## Project Config File

Create a `barangay.yaml` (or `barangay_config.yaml`) in your project root to configure plugin directories:

```yaml
plugin_dirs:
  - ./plugins
  - /shared/barangay-plugins
```

The config file is searched upward from the current working directory, so it can live in any parent directory of your project.

---

## Creating a Plugin

### 1. Create the plugin directory

```
plugins/
└── my_plugin/
    ├── manifest.yaml
    └── data/
        └── my_plugin.json
```

### 2. Write the manifest

```yaml
name: my_plugin
description: My custom enrichment data
version: 1.0.0
format: json
key: psgc_id
```

### 3. Add the data file

```json
[
  { "psgc_id": "0731100000", "my_field": "my_value" }
]
```

### 4. Enable the plugin

Add it to `plugins.yaml`:

```yaml
plugins:
  - name: my_plugin
    enabled: true
```

Or enable it on the CLI with `--plugin my_plugin`.

### Time-aware plugins

For versioned data, use `YYYY-MM-DD/` subdirectories:

```
my_plugin/
├── manifest.yaml
└── data/
    ├── 2025-01-01/
    │   └── my_plugin.json
    └── 2025-07-01/
        └── my_plugin.json
```

Include `current` and `dates` in the manifest so the loader knows which snapshot to use by default:

```yaml
name: my_plugin
format: json
key: psgc_id
current: "2025-07-01"
dates:
  - "2025-01-01"
  - "2025-07-01"
```
