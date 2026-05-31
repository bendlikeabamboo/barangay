# Built-in Plugins

## psgc-aux-data (enabled by default)

Supplementary PSGC data sourced from official PSA releases.

| Field | Type | Description |
|-------|------|-------------|
| `correspondence_code` | `str \| None` | Legacy PSA correspondence code |
| `old_names` | `str \| None` | Previous official name (if renamed) |
| `city_class` | `str \| None` | City classification (e.g., `HUC`, `ICC`, `Component`) |
| `income_classification` | `str \| None` | Income class (e.g., `1st`, `2nd`–`6th`) |
| `urban_rural` | `str \| None` | `U` (urban) or `R` (rural), null for non-barangay levels |
| `population` | `int \| None` | Population count |
| `status` | `str \| None` | Special status (e.g., `Capital`) |

**Properties:**

| Property | Value |
|----------|-------|
| Format | JSON |
| Type | Scalar |
| Source | Remote (GitHub) |
| Time-aware | Yes |
| Current date | 2026-04-13 |
| Available dates | 2021-08-19, 2022-04-29, 2022-11-08, 2023-01-25, 2023-04-18, 2023-08-15, 2023-10-24, 2024-01-23, 2024-04-23, 2024-05-08, 2024-07-12, 2024-10-18, 2025-01-30, 2025-04-23, 2025-08-29, 2025-10-13, 2026-01-13, 2026-04-13 |
| Repository | [github.com/bendlikeabamboo/psgc-aux-data-repository](https://github.com/bendlikeabamboo/psgc-aux-data-repository) |

### Example output

```json
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
```

---

## Sample Plugins

These are bundled for demonstration only. They contain fabricated data — do not use for real analysis.

### sample_elevation

Average elevation above sea level by province.

| Property | Value |
|----------|-------|
| Format | CSV |
| Type | Scalar |
| Source | Local |
| Time-aware | No |

**Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `elevation_m` | `str` | Average elevation in meters |
| `terrain` | `str` | Terrain classification (`lowland`, `upland`, `highland`) |

**Data (excerpt):**

```csv
psgc_id,elevation_m,terrain
1300000000,16,lowland
0800000000,52,lowland
0400000000,322,upland
1400000000,1500,highland
1900000000,88,lowland
```

**Example output for NCR:**

```json
{
  "sample_elevation.elevation_m": "16",
  "sample_elevation.terrain": "lowland"
}
```

### sample_population

Population counts by city/municipality. Demonstrates time-aware JSON plugin.

| Property | Value |
|----------|-------|
| Format | JSON |
| Type | Scalar |
| Source | Local |
| Time-aware | Yes |
| Current date | 2023-01-01 |
| Available dates | 2020-01-01, 2023-01-01 |

**Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `population` | `int` | Population count |
| `households` | `int` | Number of households |

**Raw data structure:**

```python
{
    "1380100000": {
        "population": 1582050,
        "households": 345120
    }
}
```

### sample_schools

BEISS school records per barangay. Demonstrates **array** data extension.

| Property | Value |
|----------|-------|
| Format | JSON |
| Type | **Array** |
| Source | Local |
| Time-aware | Yes |
| Current date | 2024-07-13 |
| Available dates | 2024-04-13, 2024-07-13 |

**Fields (per array element):**

| Field | Type | Description |
|-------|------|-------------|
| `beiss_id` | `int` | School identifier |
| `name` | `str` | School name |
| `classification` | `str` | School level (`Elementary`, `Junior`, `Senior`) |
| `students` | `int` | Number of students |

**Raw data structure:**

```python
{
    "1380100001": {
        "data": [
            {"beiss_id": 10001, "name": "Caloocan North Elementary School", "classification": "Elementary", "students": 1200},
            {"beiss_id": 10002, "name": "North City National High School", "classification": "Junior", "students": 850},
            {"beiss_id": 10003, "name": "Caloocan City Science High School", "classification": "Senior", "students": 420}
        ]
    }
}
```

### sample_elevation_time

Elevation data with `YYYY-MM-DD/` folder layout. Demonstrates time-aware plugins with date subdirectories.

| Property | Value |
|----------|-------|
| Format | JSON |
| Type | Scalar |
| Source | Local |
| Time-aware | Yes |
| Current date | 2025-01-15 |
| Available dates | 2024-01-15, 2025-01-15 |

**Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `elevation_m` | `int` | Average elevation in meters |
| `terrain` | `str` | Terrain classification |

**Raw data structure:**

```python
{
    "1300000000": {
        "elevation_m": 16,
        "terrain": "lowland"
    }
}
```
