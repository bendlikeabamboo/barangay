"""Generate SEO landing pages for top Philippine LGUs (cities + municipalities).

Each page targets high-volume queries like "list of barangays in Quezon City"
or "PSGC code of Makati" with: a barangay table, a runnable code snippet,
per-page metadata, and a schema.org `Place` JSON-LD block.

Run via:  poe gen-quarto-lgus
(or `uv run python quarto-docs/_generate_lgus.py`)

LGUs are ranked by number of barangays (a fully-offline proxy for size/
population). Override the count with --top N.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html import escape
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent
LGU_DIR = DOCS_DIR / "locations"
SITE_URL = "https://bendlikeabamboo.github.io/barangay"
DATA_VERSION = "2026-04-13"

_LGU_LEVELS = {
    "highly_urbanized_city",
    "independent_component_city",
    "component_city",
    "municipality",
}


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def load_db():
    sys.path.insert(0, str(DOCS_DIR.parent))
    import barangay  # noqa: PLC0415

    _ = len(barangay.barangays)
    return barangay


def collect_lgus(db, top: int) -> list[dict]:
    index = db._db._index  # noqa: SLF001 - reuse built HierarchyIndex
    levels = db.AdminLevel

    lgu_level_set = {
        levels.HIGHLY_URBANIZED_CITY,
        levels.INDEPENDENT_COMPONENT_CITY,
        levels.COMPONENT_CITY,
        levels.MUNICIPALITY,
    }

    lgus = []
    for record in index._by_id.values():  # noqa: SLF001
        if record.type not in lgu_level_set:
            continue
        children = index.children(record.psgc_id)
        brgy_children = [c for c in children if c.type == levels.BARANGAY]
        if not brgy_children:
            continue
        region = index.resolve_region(record)
        province = index.resolve_province(record)
        lgus.append(
            {
                "name": record.name,
                "type": record.type.value,
                "psgc_id": record.psgc_id,
                "region": region.name if region else None,
                "province": province.name if province else None,
                "barangay_count": len(brgy_children),
                "barangays": sorted(brgy_children, key=lambda c: c.name),
            }
        )

    lgus.sort(key=lambda x: (-x["barangay_count"], x["name"]))
    return lgus[:top]


def place_label(lgu: dict) -> str:
    return "City" if lgu["type"] != "municipality" else "Municipality"


def display_name(lgu: dict) -> str:
    return lgu["name"]


def qualifier(lgu: dict) -> str:
    province = lgu["province"]
    if lgu["type"] == "municipality":
        return province or lgu["region"] or "the Philippines"
    return province or lgu["region"] or "the Philippines"


def render_page(lgu: dict) -> str:
    name = display_name(lgu)
    kind = place_label(lgu)
    prov = qualifier(lgu)
    title = f"Barangays in {name}, {prov} — PSGC Codes"
    description = (
        f"Complete list of {lgu['barangay_count']} barangays in {name}, {prov} "
        f"with their PSGC codes. Lookup, fuzzy search, and Python examples for "
        f"the Philippine Standard Geographic Code."
    )

    rows = []
    for c in lgu["barangays"]:
        rows.append(f"| {escape(c.name)} | {c.psgc_id} |")
    table = "| Barangay | PSGC Code |\n|----------|-----------|\n" + "\n".join(rows)

    place_jsonld = {
        "@context": "https://schema.org",
        "@type": "Place",
        "name": f"{name}, {prov}",
        "description": f"{kind} in the Philippines with {lgu['barangay_count']} "
        f"barangays listed under the Philippine Standard Geographic Code (PSGC).",
        "address": {
            "@type": "PostalAddress",
            "addressRegion": prov,
            "addressCountry": "PH",
        },
        "containedInPlace": {
            "@type": "AdministrativeArea",
            "name": prov,
        },
    }

    example_name = name.replace("City of ", "").replace("City of", "").strip()

    return f"""---
title: "{title}"
description: "{escape(description)}"
author: "bendlikeabamboo"
toc: true
toc-location: right
---

# PSGC Barangays in {name}, {prov}

<script type="application/ld+json">
{json.dumps(place_jsonld, indent=2)}
</script>

{name} is a **{kind.lower()}** in {prov} (Philippines) with
**{lgu["barangay_count"]} barangays** in the Philippine Standard Geographic
Code (PSGC) masterlist as of {DATA_VERSION}. Use the table below for the
official barangay names and 10-digit PSGC codes.

## List of barangays

{table}

## Look up {example_name} with Python

```python
from barangay import municipalities, cities, search_fuzzy

# Exact lookup by PSGC code (always unique)
rec = municipalities.lookup("{lgu["psgc_id"]}") or cities.lookup("{lgu["psgc_id"]}")
print(rec, rec.region, rec.province)

# Iterate its barangays
for child in rec.children:
    print(child.name, child.psgc_id)
```

## Search barangays in {example_name}

```python
from barangay import search_fuzzy

for r in search_fuzzy("{example_name}", limit=10):
    print(r.name, r.psgc_id, r.score)
```

---

Data source: [Philippine Statistics Authority PSGC masterlist ({DATA_VERSION})](https://psa.gov.ph/classification/psgc/).
See the [barangay package](../index.qmd) for fuzzy search, validation, and bulk export.
"""


def render_index(lgus: list[dict]) -> str:
    items = []
    for lgu in lgus:
        slug = lgu["slug"]
        label = f"{display_name(lgu)} ({qualifier(lgu)})"
        items.append(f"- [{label}](./{slug}.qmd) — {lgu['barangay_count']} barangays")
    listing = "\n".join(items)
    return f"""---
title: "Philippine LGUs — Barangays & PSGC Codes — barangay"
description: "Browse Philippine cities and municipalities with their complete list of barangays and PSGC codes. Programmatic PSGC landing pages for address lookup and fuzzy search."
author: "bendlikeabamboo"
toc: true
toc-location: right
---

# Philippine Cities & Municipalities — Barangay Lists

Browse the complete list of barangays and their PSGC codes for major Philippine
cities and municipalities. Each page includes a barangay table, PSGC codes, and
ready-to-run Python examples for the `barangay` package.

{listing}

> These pages are generated programmatically from the bundled PSGC dataset
> ({DATA_VERSION}). To regenerate or extend the list, run `poe gen-quarto-lgus`.

See the [full package documentation](../index.qmd) for fuzzy search, address
validation, hierarchy traversal, and bulk export.
"""


def assign_slugs(lgus: list[dict]) -> None:
    seen: dict[str, int] = {}
    for lgu in lgus:
        base = slugify(lgu["name"])
        slug = base
        if slug in seen:
            seen[slug] += 1
            slug = f"{base}-{seen[base]}"
        else:
            seen[slug] = 0
        lgu["slug"] = slug


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate LGU landing pages.")
    parser.add_argument(
        "--top", type=int, default=150, help="Number of LGUs (default 150)."
    )
    args = parser.parse_args()

    db = load_db()
    lgus = collect_lgus(db, args.top)
    assign_slugs(lgus)

    LGU_DIR.mkdir(parents=True, exist_ok=True)
    for old in LGU_DIR.glob("*.qmd"):
        old.unlink()

    for lgu in lgus:
        (LGU_DIR / f"{lgu['slug']}.qmd").write_text(render_page(lgu), encoding="utf-8")

    (LGU_DIR / "index.qmd").write_text(render_index(lgus), encoding="utf-8")

    print(f"Generated {len(lgus)} LGU pages in {LGU_DIR}")


if __name__ == "__main__":
    main()
