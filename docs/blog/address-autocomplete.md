---
title: "Build a Philippine Address Autocomplete with barangay"
description: "Build a fast Philippine address autocomplete using the barangay package's offline fuzzy search. No API calls, no rate limits — instant suggestions across 42,011 barangays."
image: "https://bendlikeabamboo.github.io/barangay/favicon.png"
author: "bendlikeabamboo"
---

# Build a Philippine Address Autocomplete with barangay

A good address autocomplete turns messy free text into a canonical PSGC record.
This post sketches a small, offline autocomplete backed by the `barangay`
package's fuzzy search.

## Install

```bash
pip install barangay
```

## A minimal suggester

```python
from barangay import search_fuzzy

def suggest(query: str, limit: int = 8):
    """Return ranked address suggestions for a partial query."""
    results = []
    for r in search_fuzzy(query, limit=limit, threshold=60.0):
        results.append(
            {
                "label": r.name,
                "psgc_id": r.psgc_id,
                "score": r.score,
            }
        )
    return results

print(suggest("Tongmagen, Tawi"))
```

## Adding context to disambiguate

Many barangay names repeat across provinces. Accept province or municipality
context to push the intended match to the top:

```python
suggest("Bagumbayan, Quezon City")
```

Because `search_fuzzy()` scores province+barangay and
municipality+barangay patterns, adding context naturally raises the right
result's score.

## Wiring it into a backend

Because the whole dataset is bundled and in-process, you can expose `suggest()`
behind a tiny HTTP endpoint (FastAPI, Flask) or call it directly from a
notebook. There are no external API rate limits to worry about, and latency is
dominated by your fuzzy threshold and result limit.

## Next steps

- Persist selected `psgc_id`s as canonical keys in your database.
- Pair `suggest()` with `validate()` to confirm a final, complete address.
- Enrich results with the **plugin system** (population, income class, old
  names) for richer suggestions.

---

See the [fuzzy search blog post](fuzzy-search-barangays.md) and the
[address validation tutorial](../tutorials/address_validation.md).
