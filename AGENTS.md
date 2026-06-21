# AGENTS.md

AI coding agent reference for the **barangay** project — a Philippine Standard Geographic Code (PSGC) Python package providing offline access to all 42,011 barangays with fuzzy search, address validation, CLI, plugin system, and historical data support.

See [README.md](README.md) for user-facing documentation and [quarto-docs/](quarto-docs/) for the full docs site.

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| `barangay/` | Main package — core library, public API re-exports |
| `barangay/data/` | Bundled PSGC data files (version from `CURRENT_VERSION`) |
| `barangay/plugins/` | Plugin system |
| `tests/` | Test suite |
| `parsers/` | PSGC data parsing scripts (excluded from ty checking) |
| `quarto-docs/` | Quarto documentation source |
| `architecture/` | Architecture decision records |
| `.github/workflows/` | CI: publish (PyPI), docs (GitHub Pages) |

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13+ | Runtime |
| `uv` | Dependency management |
| `hatchling` | Build system |
| `ruff` | Linting + formatting |
| `ty` | Type checking (NOT mypy) |
| `pytest` + `pytest-xdist` + `pytest-cov` | Testing |
| `pre-commit` | Pre-commit hooks |
| `quarto` + `quarto-cli` | Documentation (Quarto) |
| `click` + `rich` | CLI framework |
| `poe` (poethepoet) | Task runner |

## Commands

```bash
uv sync                          # Install dependencies
uv run ruff check --fix --exit-non-zero-on-fix --ignore E741  # Lint
uv run ruff format               # Format
uv run ty check                  # Type check (NOT mypy)
uv run pytest                    # Run tests (local dev)
uv run pytest -n auto            # Run tests in parallel (pre-commit uses this)
uv run pytest --cov              # Run tests with coverage
uv run pre-commit run --all-files  # Run all pre-commit hooks manually
uv build                         # Build package
poe barpar                       # Run PSGC data parser (parsers/psgc/cli.py)
quarto preview quarto-docs       # Local docs preview (port 4444)```

## Code Conventions

- `ruff` default formatting — no custom config
- Type hints required (`ty check` is enforced)
- Python 3.13+ syntax allowed (e.g. `X | Y` union types, `str | None`)
- Follow existing import ordering in neighboring files
- Tests go in `tests/` with `test_*.py` naming
- No comments unless explicitly requested

## Branching Strategy (GitHub Flow)

- `main` is the only long-lived branch
- Feature/fix/docs branches: `feature/<name>`, `fix/<name>`, `docs/<name>`
- PR required to merge into `main` — no direct commits
- Tags matching `*.*.*.*` trigger PyPI publish via GitHub Actions

## AI Workflow

1. **Understand context** — read relevant files before making changes
2. **Make changes** — follow existing code conventions and patterns
3. **Run verification** before considering done:
   ```bash
   uv run ruff check --fix --exit-non-zero-on-fix --ignore E741
   uv run ruff format
   uv run ty check
   uv run pytest
   ```
4. **Follow PR template** — reference CONTRIBUTING.md and PR template checklist

## Testing

- Test directory: `tests/`
- Naming: `test_*.py`
- Local dev: `uv run pytest` (sequential)
- Pre-commit: `uv run pytest -n auto` (parallel via xdist)
- Coverage: `uv run pytest --cov`
- `tests/` is excluded from `ty` type checking

## CI/CD

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `publish.yaml` | Tag push (`*.*.*.*`) | Build and publish to PyPI |
| `docs.yaml` | Push to `quarto-docs/**` or `quarto-docs/_quarto.yml` | Build and deploy docs to GitHub Pages (deploy only from `main`) |

## Hierarchy Level Indicator (`rphicmsgb`)

A 9-character string pattern used to indicate which PSGC hierarchy levels are active/included in a query or match result. Each position corresponds to a level; replace the placeholder `0` with the level's letter when active.

| Position | Letter | Level |
|----------|--------|-------|
| 1 | `r` | Region |
| 2 | `p` | Province |
| 3 | `h` | Highly urbanized city |
| 4 | `i` | Independent component city |
| 5 | `c` | Component city |
| 6 | `m` | Municipality |
| 7 | `s` | Sub-municipality |
| 8 | `g` | Special geographic area / unit |
| 9 | `b` | Barangay |

Example: `r0h000s0b` means the result spans region, highly urbanized city, sub-municipality, and barangay levels.

## Notes / Gotchas

- `parsers/` and `tests/` are excluded from `ty` type checking (`pyproject.toml` `[tool.ty.src]`)
- `search()` (dict-based, deprecated) and `search_fuzzy()` (typed, recommended) coexist — always use `search_fuzzy()`
- `BARANGAY`, `BARANGAY_EXTENDED`, `BARANGAY_FLAT` dict aliases are deprecated — use Database API (`barangays.get(name=...)`)
- CLI entry point: `barangay.cli:app`
- `barpar` poe task = `python parsers/psgc/cli.py` (PSGC data parsing)
- Data version comes from `barangay/data/CURRENT_VERSION` file, not hardcoded
- Module-level attributes: `barangay.current`, `barangay.as_of`, `barangay.available_dates`
- Public API re-exports are defined in `barangay/__init__.py` — check `__all__` for the full list
