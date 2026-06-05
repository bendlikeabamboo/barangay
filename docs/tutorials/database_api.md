# Getting Started with the Database API

A quick walkthrough of the `barangay` Database API for browsing, searching, validating, and exporting Philippine geographic data.

## Installation

```bash
pip install barangay
```

## 1. Browse Administrative Levels

Pre-built views give you direct access to every admin level in the PSGC database:

```python
from barangay import regions, provinces, municipalities, cities, barangays

print(regions)     # <PSGC region database: 18 records>
print(provinces)   # <PSGC province database: 82 records>
print(barangays)   # <PSGC barangay database: 42010 records>
```

Each view supports iteration, containment checks, and counting:

```python
print(len(barangays))          # 42010
print("1907005010" in barangays)  # True

for region in regions:
    print(region.name)
# Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)
# Cordillera Administrative Region (CAR)
# MIMAROPA Region
# ...
```

## 2. Look Up a Record

Look up a single record by name or PSGC ID:

```python
# By name
brgy = barangays.get(name="Tongmageng")
print(brgy)  # <barangay: Tongmageng (1907005010)>

# By PSGC ID (always unique)
brgy = barangays.lookup("1907005010")
print(brgy.name)  # Tongmageng
```

If a name matches multiple records, `get()` raises `MultipleResultsError`. Use `lookup()` with a PSGC ID for guaranteed-unique lookups.

## 3. Traverse the Hierarchy

Each record knows its position in the administrative hierarchy:

```python
brgy = barangays.get(name="Tongmageng")

print(brgy.region)       # Bangsamoro Autonomous Region In Muslim Mindanao (BARMM)
print(brgy.province)     # Tawi-Tawi
print(brgy.municipality)  # Sitangkai
print(brgy.parent)       # <municipality: Sitangkai (1907005000)>

for ancestor in brgy.ancestors:
    print(repr(ancestor))
# <municipality: Sitangkai (1907005000)>
# <province: Tawi-Tawi (1907000000)>
# <region: Bangsamoro Autonomous Region In Muslim Mindanao (BARMM) (1900000000)>
```

Navigate downward with `.children`:

```python
manila = cities.get(name="City of Manila")
for child in manila.children[:3]:
    print(repr(child))
# <submunicipality: Tondo I/II (1380601000)>
# <submunicipality: Binondo (1380602000)>
# <submunicipality: Quiapo (1380603000)>
```

## 4. Export to Pandas

Export any view directly to a DataFrame or list of dicts:

```python
df = barangays.to_frame()
print(df.columns.tolist())
# ['name', 'type', 'psgc_id', 'parent_psgc_id', 'nicknames', 'extensions',
#  'region', 'province', 'municipality', 'city']
print(df.shape)  # (42010, 10)

data = barangays.to_dicts()
print(len(data))  # 42010
print(data[0])
# {'name': 'Arco', 'type': 'barangay', 'psgc_id': '1900702001', ...}
```

Each record includes resolved hierarchy fields (`region`, `province`, `municipality`, `city`) for immediate use in analysis.

## 5. Fuzzy Search

Search with fuzzy matching, returning typed `SearchResult` objects:

```python
from barangay import search_fuzzy

results = search_fuzzy("Tongmagen, Tawi-Tawi", threshold=60.0, limit=5)
for r in results:
    print(f"{r.name} ({r.psgc_id}) — score: {r.score}")
# Tongmageng (1907005010) — score: 100.0
# Tonggosong (1907004005) — score: 84.21
# Tongbangkaw (1907007042) — score: 82.05
# Tongusong (1907005012) — score: 81.08
# Tongehat (1907011014) — score: 77.78
```

Each result exposes `.name`, `.psgc_id`, `.score`, and `.match_type`.

## 6. Validate Addresses

Validate addresses against the PSGC masterlist with a high-confidence threshold:

```python
from barangay import validate, validate_many

v = validate("Tongmageng, Tawi-Tawi")
print(v.valid, v.matched_name, v.score)  # True Tongmageng 100.0
```

Validate multiple addresses at once:

```python
results = validate_many([
    "Tongmageng, Tawi-Tawi",
    "Brgy 291, City of Manila",
    "Nonexistent Place",
])
for r in results:
    status = "valid" if r.valid else "invalid"
    print(f"{r.input!r} -> {status}")
# 'Tongmageng, Tawi-Tawi' -> valid
# 'Brgy 291, City of Manila' -> invalid
# 'Nonexistent Place' -> invalid
```

The default threshold is 95.0. Lower it for more lenient matching:

```python
v = validate("Brgy 291, City of Manila", threshold=80.0)
print(v.valid, v.score)  # True 88.24
```

## Next Steps

- [API Reference](../api.md) — full documentation of all Database API methods
- [Address Validation](address_validation.md) — deep dive into validation techniques
- [Bulk Barangay Lookup](bulk_barangay_lookup.md) — batch processing at scale
- [Plugins](../plugins/index.md) — enriching data with plugins
