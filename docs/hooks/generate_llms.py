"""Append generated LGU landing pages to docs/llms-full.txt.

After running `poe gen-lgus`, run `poe gen-llms` so LLMs that consume
llms-full.txt can surface the per-LGU pages (e.g. "list of barangays in
Quezon City"). This script adds a trailing "## LGU landing pages" section and
is idempotent: it rebuilds that section on each run.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent
LGU_DIR = DOCS_DIR / "lgus"
LLMS_FULL = DOCS_DIR / "llms-full.txt"
SITE_URL = "https://bendlikeabamboo.github.io/barangay"

_SECTION_START = "## LGU landing pages"


def load_index_titles() -> list[tuple[str, str]]:
    index_path = LGU_DIR / "index.md"
    if not index_path.exists():
        return []
    text = index_path.read_text(encoding="utf-8")
    titles = re.findall(r"^\- \[(.*?)\]\(\./(.*?)\.md\)", text, flags=re.MULTILINE)
    return titles


def main() -> None:
    if not LLMS_FULL.exists():
        print(f"{LLMS_FULL} not found; nothing to update.", file=sys.stderr)
        return

    titles = load_index_titles()
    # Drop any previous generated section.
    base = (
        LLMS_FULL.read_text(encoding="utf-8").split(_SECTION_START)[0].rstrip() + "\n"
    )

    if not titles:
        LLMS_FULL.write_text(base, encoding="utf-8")
        print("Cleared LGU section (no LGU pages found).")
        return

    lines = [
        "",
        _SECTION_START,
        "",
        "Programmatic PSGC landing pages (one per major Philippine city/municipality) "
        "listing its barangays and PSGC codes:",
        "",
    ]
    for label, slug in titles:
        lines.append(f"- [{label}]({SITE_URL}/lgus/{slug}/)")
    lines.append("")

    LLMS_FULL.write_text(base + "\n".join(lines), encoding="utf-8")
    print(f"Added {len(titles)} LGU links to {LLMS_FULL}")


if __name__ == "__main__":
    main()
