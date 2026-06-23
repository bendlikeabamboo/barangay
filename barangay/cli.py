import csv
import io
import json
import shutil
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from barangay import (
    Database,
    DataManager,
    available_dates,
    current,
    get_available_dates,
    get_cache_dir,
    search_fuzzy,
    validate,
)
from barangay.database import EnrichedRecord
from barangay.models import AdminLevel, SearchResult

console = Console()

_RPHICMSGB = "rphicmsgb"

# Ordered (letter, attribute) pairs for the 9 PSGC hierarchy levels.
_RPHICMSGB_LEVELS: list[tuple[str, str]] = [
    ("r", "region"),
    ("p", "province"),
    ("h", "highly_urbanized_city"),
    ("i", "independent_component_city"),
    ("c", "component_city"),
    ("m", "municipality"),
    ("s", "submunicipality"),
    ("g", "special_geographic_area"),
    ("b", "barangay"),
]

_LEVEL_LABELS: dict[str, str] = {
    "region": "Region",
    "province": "Province",
    "highly_urbanized_city": "HUC",
    "independent_component_city": "ICC",
    "component_city": "Component City",
    "municipality": "Municipality",
    "submunicipality": "Sub-Mun",
    "special_geographic_area": "Special Geo",
    "barangay": "Barangay",
}

_LEVEL_CHOICES: list[str] = [attr for _, attr in _RPHICMSGB_LEVELS] + ["cities"]

# The 9 PSGC level names that may be used as a --level filter or a --match-hook.
_MATCH_HOOK_CHOICES: list[str] = [attr for _, attr in _RPHICMSGB_LEVELS]


def _resolve_level(level: str | None) -> AdminLevel | None:
    """Translate a CLI level string to an AdminLevel (or None)."""
    return AdminLevel(level) if level else None


def rphicmsgb(enriched) -> str:
    """Build the 9-char hierarchy indicator from an EnrichedRecord.

    Args:
        enriched: An EnrichedRecord (or object exposing the 9 level
            properties) describing a resolved record.

    Returns:
        A 9-character string where each position holds the level's letter
        when the level resolves, else ``0``.
    """
    chars: list[str] = []
    for letter, attr in _RPHICMSGB_LEVELS:
        value = getattr(enriched, attr)
        chars.append(letter if value else "0")
    return "".join(chars)


def to_result_dict(sr: SearchResult) -> dict:
    """Serialise a SearchResult into a JSON-friendly dict.

    Starts from ``EnrichedRecord.to_dict()`` (name, type, psgc_id,
    parent_psgc_id, nicknames and the 9 resolved level fields), drops the
    verbose ``extensions`` list, flattens scalar plugin fields as
    ``plugin.field``, and appends ``rphicmsgb``, ``score`` and
    ``match_type``.

    Args:
        sr: A SearchResult returned by ``search_fuzzy()``.

    Returns:
        A plain dict suitable for JSON output.
    """
    d = sr.enriched.to_dict()
    d.pop("extensions", None)
    d["rphicmsgb"] = rphicmsgb(sr.enriched)
    d["score"] = sr.score
    d["match_type"] = sr.match_type
    for ext in sr.record.extensions:
        if isinstance(ext.data, dict):
            for key, value in ext.data.items():
                d[f"{ext.field_group}.{key}"] = value
    return d


def _collect_plugin_columns(results: list[SearchResult]) -> list[str]:
    """Collect ordered ``plugin.field`` column names that have any value.

    Only columns with at least one non-empty value across the results are
    returned, so fully-blank plugin columns are omitted from the table.
    """
    columns: list[str] = []
    seen_values: dict[str, bool] = {}
    for sr in results:
        for ext in sr.record.extensions:
            if isinstance(ext.data, dict):
                for key, value in ext.data.items():
                    col = f"{ext.field_group}.{key}"
                    if col not in columns:
                        columns.append(col)
                    if value not in (None, "", [], {}):
                        seen_values[col] = True
    return [col for col in columns if seen_values.get(col)]


def _active_levels(results: list[SearchResult]) -> list[str]:
    """Return the ordered level attributes that resolve for any result."""
    return [
        attr
        for _, attr in _RPHICMSGB_LEVELS
        if any(getattr(sr.enriched, attr) for sr in results)
    ]


def _build_hierarchy_table(
    title: str,
    active_levels: list[str] | None = None,
    plugin_columns: list[str] | None = None,
) -> Table:
    """Build a table exposing the resolved hierarchy levels + rphicmsgb + PSGC ID.

    Args:
        title: Table title.
        active_levels: Ordered level attributes to include as columns.
            Defaults to all 9 levels. Blank-only columns should be filtered
            out by the caller.
        plugin_columns: Optional extra ``plugin.field`` column names.

    Returns:
        A configured rich Table (no rows yet).
    """
    table = Table(title=title)
    levels = (
        active_levels
        if active_levels is not None
        else [a for _, a in _RPHICMSGB_LEVELS]
    )
    for attr in levels:
        table.add_column(_LEVEL_LABELS[attr], style="cyan")
    table.add_column(_RPHICMSGB, style="magenta")
    table.add_column("PSGC ID", style="blue")
    table.add_column("Score", style="yellow")
    for col in plugin_columns or []:
        table.add_column(col, style="dim")
    return table


def _render_results(
    query_label: str,
    results: list[SearchResult],
    output_format: str,
    plugin_columns: list[str] | None = None,
) -> None:
    """Render search results as a hierarchy-loyal table or JSON.

    Blank-only level and plugin columns are omitted from the table.

    Args:
        query_label: Title suffix describing the query.
        results: Search results to render.
        output_format: ``"table"`` or ``"json"``.
        plugin_columns: Pre-computed plugin column names (table only).
    """
    if output_format == "json":
        console.print_json(data=[to_result_dict(sr) for sr in results])
        return

    active_levels = _active_levels(results)
    plugin_cols = _collect_plugin_columns(results) if plugin_columns else []
    table = _build_hierarchy_table(query_label, active_levels, plugin_cols)
    for sr in results:
        row = to_result_dict(sr)
        values = [row.get(attr) or "" for attr in active_levels]
        values.append(row["rphicmsgb"])
        values.append(row["psgc_id"])
        values.append(f"{sr.score:.1f}")
        for col in plugin_cols:
            value = row.get(col)
            values.append("" if value is None else str(value))
        table.add_row(*values)
    console.print(table)


def _resolve_enriched(record) -> EnrichedRecord | None:
    """Look up an EnrichedRecord for a plain record via the Database index.

    Args:
        record: An AdminDivRecord (e.g. from ValidationResult).

    Returns:
        An EnrichedRecord, or None if not found.
    """
    return Database().all_records.lookup(record.psgc_id)


@click.group()
@click.version_option(version=current)
def app():
    """Main CLI entry point.

    Returns:
        None
    """
    pass


@app.command()
@click.argument("query")
@click.option("--limit", "-l", default=5, help="Maximum number of results")
@click.option(
    "--threshold", "-t", default=60.0, help="Minimum similarity score (0-100)"
)
@click.option("--as-of", help="Historical date (YYYY-MM-DD)")
@click.option(
    "--level",
    "-L",
    "level",
    type=click.Choice(_MATCH_HOOK_CHOICES),
    default=None,
    help="Filter results to a specific admin level (e.g. province, barangay)",
)
@click.option(
    "--match-hook",
    "match_hooks",
    multiple=True,
    type=click.Choice(_MATCH_HOOK_CHOICES),
    help="Name-levels to score against (repeatable); defaults to barangay",
)
@click.option(
    "--format",
    "-f",
    "output_format",
    type=click.Choice(["json", "table"]),
    default="table",
    help="Output format",
)
@click.option(
    "--plugin",
    "plugins",
    multiple=True,
    help="Enable a specific plugin for enrichment (repeatable)",
)
def search_cmd(
    query, limit, threshold, as_of, level, match_hooks, output_format, plugins
):
    """Search PSGC records by name (fuzzy).

    Args:
        query: Search query string.
        limit: Maximum number of results.
        threshold: Minimum similarity score (0-100).
        as_of: Historical date (YYYY-MM-DD).
        level: Filter results to a specific admin level.
        match_hooks: Name-levels to score against (defaults to barangay).
        output_format: Output format (json or table).
        plugins: Plugin names to enable for enrichment.

    Returns:
        None
    """
    try:
        if plugins:
            Database().use_plugins(list(plugins))

        results = search_fuzzy(
            query,
            level=_resolve_level(level),
            match_hooks=list(match_hooks) or None,
            threshold=threshold,
            limit=limit,
            as_of=as_of,
        )

        if not results:
            console.print("[yellow]No results found.[/yellow]")
            return

        plugin_columns = _collect_plugin_columns(results) if plugins else None
        _render_results(
            f"Search Results for '{query}'",
            results,
            output_format,
            plugin_columns,
        )
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@app.group()
def info():
    """Information commands group.

    Returns:
        None
    """
    pass


@info.command()
def version():
    """Show current version and available dates.

    Returns:
        None
    """
    console.print(f"[cyan]Current version:[/cyan] {current}")
    console.print(f"[cyan]Available dates:[/cyan] {', '.join(available_dates)}")


@info.command()
def stats():
    """Display record counts per PSGC hierarchy level.

    Returns:
        None
    """
    level_views: list[tuple[str, str]] = [
        ("region", "regions"),
        ("province", "provinces"),
        ("highly_urbanized_city", "hucs"),
        ("independent_component_city", "iccs"),
        ("component_city", "component_cities"),
        ("municipality", "municipalities"),
        ("submunicipality", "submunicipalities"),
        ("special_geographic_area", "special_geographic_areas"),
        ("barangay", "barangays"),
    ]
    db = Database()
    table = Table(title="PSGC Record Statistics")
    table.add_column("Level", style="cyan")
    table.add_column("Count", style="green")

    for attr, view_name in level_views:
        table.add_row(_LEVEL_LABELS[attr], str(len(getattr(db, view_name))))
    table.add_row("[bold]Total[/bold]", str(len(db.all_records)))
    console.print(table)


@info.command("list")
@click.argument(
    "level",
    type=click.Choice(_LEVEL_CHOICES),
)
@click.option(
    "--parent",
    help="Restrict to descendants of a parent given by name or PSGC ID",
)
def list_cmd(level, parent):
    """List records at a given hierarchy level.

    Args:
        level: Hierarchy level (one of the 9 PSGC levels, or ``cities``).
        parent: Optional ancestor name or PSGC ID to filter descendants.

    Returns:
        None
    """
    try:
        db = Database()
        if level == "cities":
            view = db.cities
        else:
            view = db._view(AdminLevel(level))

        records = list(view)

        if parent:
            parent_record = _resolve_parent(db, parent)
            if parent_record is None:
                console.print(f"[red]Parent '{parent}' not found.[/red]")
                raise click.ClickException(f"Parent '{parent}' not found")
            parent_id = parent_record.psgc_id
            records = [r for r in records if _has_ancestor(r, parent_id)]

        title = f"{_LEVEL_LABELS.get(level, level.title())}"
        if parent:
            title += f" under '{parent}'"
        table = Table(title=title)
        table.add_column("Name", style="cyan")
        table.add_column("Type", style="green")
        table.add_column("PSGC ID", style="blue")

        for r in sorted(records, key=lambda rec: rec.name):
            table.add_row(r.name, r.type.value, r.psgc_id)
        console.print(table)
    except click.ClickException:
        raise
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


def _resolve_parent(db: Database, parent: str):
    """Resolve a parent identifier to an EnrichedRecord.

    Tries PSGC ID first, then exact name match, then a fuzzy name search
    so common abbreviations (e.g. ``BARMM``) resolve.

    Args:
        db: Database instance.
        parent: PSGC ID or (possibly abbreviated) name.

    Returns:
        An EnrichedRecord, or None.
    """
    record = db.all_records.lookup(parent)
    if record is not None:
        return record
    matches = [r for r in db.all_records if r.name == parent]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        raise click.ClickException(
            f"Parent '{parent}' matched {len(matches)} records; use a PSGC ID."
        )
    results = search_fuzzy(parent, threshold=60.0, limit=1)
    if results:
        return results[0].enriched
    return None


def _has_ancestor(enriched, ancestor_psgc_id: str) -> bool:
    """Return True if ancestor_psgc_id appears in the enriched record's chain."""
    return any(a.psgc_id == ancestor_psgc_id for a in enriched.ancestors)


@app.command()
@click.option(
    "--model",
    type=click.Choice(["flat", "extended"]),
    default="flat",
    help="Data model",
)
@click.option(
    "--format",
    "-f",
    "output_format",
    type=click.Choice(["json", "csv"]),
    default="json",
    help="Output format",
)
@click.option("--output", "-o", help="Output file (default: stdout)")
@click.option("--as-of", help="Historical date (YYYY-MM-DD)")
@click.option(
    "--plugin",
    "plugins",
    multiple=True,
    help="Enable a specific plugin for enrichment (repeatable; flat only)",
)
def export(model, output_format, output, as_of, plugins):
    """Export data to JSON or CSV.

    Args:
        model: Data model (flat or extended).
        output_format: Output format (json or csv).
        output: Output file path.
        as_of: Historical date (YYYY-MM-DD).
        plugins: Plugin names to enable for enrichment (flat only).

    Returns:
        None
    """
    try:
        if plugins and model != "flat":
            raise click.ClickException("Plugins are only supported with --model flat")
        if model == "extended" and output_format == "csv":
            raise click.ClickException("CSV export is only supported with --model flat")

        db = Database()
        if as_of:
            db._version_state.set(as_of)
            db.invalidate_cache()

        flat_records: list[dict] = []
        extended_payload: object | None = None
        if model == "flat":
            if plugins:
                db.use_plugins(list(plugins))
            flat_records = db.all_records.to_dicts()
        else:
            extended_payload = DataManager().get_data(as_of=as_of, data_type="extended")

        if output_format == "json":
            payload = flat_records if model == "flat" else extended_payload
            output_data = json.dumps(payload, indent=2, ensure_ascii=False, default=str)
        else:
            output_data = _dict_to_csv(flat_records)

        if output:
            Path(output).write_text(output_data, encoding="utf-8")
            console.print(f"[green]Exported to {output}[/green]")
        else:
            console.print(output_data)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


def _dict_to_csv(data: list[dict]) -> str:
    """Convert a list of dicts to a CSV string.

    Args:
        data: List of dictionaries to convert.

    Returns:
        CSV formatted string.
    """
    output = io.StringIO()
    if data:
        fieldnames: list[str] = []
        for row in data:
            for key in row:
                if key not in fieldnames:
                    fieldnames.append(key)
        writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
    return output.getvalue()


@app.group()
def history():
    """History commands group.

    Returns:
        None
    """
    pass


@history.command()
def list_dates():
    """List available historical dates.

    Returns:
        None
    """
    dates = get_available_dates()
    table = Table(title="Available Historical Dates")
    table.add_column("Date", style="cyan")
    table.add_column("Type", style="green")

    for date in dates:
        table.add_row(date, "Historical")
    table.add_row(current, "Current")
    console.print(table)


@history.command("search-history")
@click.argument("query")
@click.option("--as-of", required=True, help="Historical date (YYYY-MM-DD)")
@click.option("--limit", "-l", default=5, help="Maximum number of results")
@click.option(
    "--threshold", "-t", default=60.0, help="Minimum similarity score (0-100)"
)
@click.option(
    "--level",
    "-L",
    "level",
    type=click.Choice(_MATCH_HOOK_CHOICES),
    default=None,
    help="Filter results to a specific admin level (e.g. province, barangay)",
)
@click.option(
    "--match-hook",
    "match_hooks",
    multiple=True,
    type=click.Choice(_MATCH_HOOK_CHOICES),
    help="Name-levels to score against (repeatable); defaults to barangay",
)
@click.option(
    "--format",
    "-f",
    "output_format",
    type=click.Choice(["json", "table"]),
    default="table",
    help="Output format",
)
def search_history(query, as_of, limit, threshold, level, match_hooks, output_format):
    """Search historical data for PSGC records.

    Args:
        query: Search query string.
        as_of: Historical date (YYYY-MM-DD).
        limit: Maximum number of results.
        threshold: Minimum similarity score (0-100).
        level: Filter results to a specific admin level.
        match_hooks: Name-levels to score against (defaults to barangay).
        output_format: Output format (json or table).

    Returns:
        None
    """
    try:
        results = search_fuzzy(
            query,
            level=_resolve_level(level),
            match_hooks=list(match_hooks) or None,
            threshold=threshold,
            limit=limit,
            as_of=as_of,
        )

        if not results:
            console.print("[yellow]No results found.[/yellow]")
            return

        _render_results(
            f"Search Results for '{query}' (as of {as_of})",
            results,
            output_format,
        )
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@history.command("export-history")
@click.option("--as-of", required=True, help="Historical date (YYYY-MM-DD)")
@click.option(
    "--model",
    type=click.Choice(["flat", "extended"]),
    default="flat",
    help="Data model",
)
@click.option(
    "--format",
    "-f",
    "output_format",
    type=click.Choice(["json", "csv"]),
    default="json",
    help="Output format",
)
@click.option("--output", "-o", help="Output file (default: stdout)")
def export_history(as_of, model, output_format, output):
    """Export historical data to JSON or CSV.

    Args:
        as_of: Historical date (YYYY-MM-DD).
        model: Data model (flat or extended).
        output_format: Output format (json or csv).
        output: Output file path.

    Returns:
        None
    """
    try:
        if model == "extended" and output_format == "csv":
            raise click.ClickException("CSV export is only supported with --model flat")

        db = Database()
        db._version_state.set(as_of)
        db.invalidate_cache()

        flat_records: list[dict] = []
        extended_payload: object | None = None
        if model == "flat":
            flat_records = db.all_records.to_dicts()
        else:
            extended_payload = DataManager().get_data(as_of=as_of, data_type="extended")

        if output_format == "json":
            payload = flat_records if model == "flat" else extended_payload
            output_data = json.dumps(payload, indent=2, ensure_ascii=False, default=str)
        else:
            output_data = _dict_to_csv(flat_records)

        if output:
            Path(output).write_text(output_data, encoding="utf-8")
            console.print(f"[green]Exported to {output}[/green]")
        else:
            console.print(output_data)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@app.group()
def cache():
    """Cache commands group.

    Returns:
        None
    """
    pass


@cache.command()
def clear():
    """Clear the cache directory.

    Returns:
        None
    """
    cache_dir = get_cache_dir()
    if not cache_dir.exists():
        console.print("[yellow]Cache directory is empty.[/yellow]")
        return

    shutil.rmtree(cache_dir)
    console.print(f"[green]Cache cleared: {cache_dir}[/green]")


@cache.command()
def info():
    """Show cache information.

    Returns:
        None
    """
    cache_dir = get_cache_dir()

    table = Table(title="Cache Information")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Cache directory", str(cache_dir))

    if cache_dir.exists():
        files = list(cache_dir.iterdir())
        total_size = sum(f.stat().st_size for f in files)
        table.add_row("Files", str(len(files)))
        table.add_row("Total size", f"{total_size / 1024 / 1024:.2f} MB")

        if files:
            table.add_row("\nCached files", "")
            for f in sorted(files):
                size = f.stat().st_size / 1024 / 1024
                table.add_row("", f"{f.name} ({size:.2f} MB)")
    else:
        table.add_row("Files", "0")
        table.add_row("Total size", "0.00 MB")

    console.print(table)


@cache.command()
@click.option("--date", help="Date to download (YYYY-MM-DD)")
def download(date):
    """Download cached data.

    Args:
        date: Date to download (YYYY-MM-DD).

    Returns:
        None
    """
    try:
        dm = DataManager()
        if date:
            console.print(f"[cyan]Downloading data for {date}...[/cyan]")
            dm.get_data(as_of=date, data_type="flat")
            console.print(f"[green]Downloaded data for {date}[/green]")
        else:
            console.print("[cyan]Downloading current data...[/cyan]")
            dm.get_data(as_of=None, data_type="flat")
            console.print("[green]Downloaded current data[/green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@app.group()
def batch():
    """Batch commands group.

    Returns:
        None
    """
    pass


@batch.command("batch-search")
@click.argument("file", type=click.Path(exists=True))
@click.option("--limit", "-l", default=5, help="Maximum number of results per query")
@click.option(
    "--threshold", "-t", default=60.0, help="Minimum similarity score (0-100)"
)
@click.option("--as-of", help="Historical date (YYYY-MM-DD)")
@click.option(
    "--level",
    "-L",
    "level",
    type=click.Choice(_MATCH_HOOK_CHOICES),
    default=None,
    help="Filter results to a specific admin level (e.g. province, barangay)",
)
@click.option(
    "--match-hook",
    "match_hooks",
    multiple=True,
    type=click.Choice(_MATCH_HOOK_CHOICES),
    help="Name-levels to score against (repeatable); defaults to barangay",
)
@click.option("--output", "-o", help="Output JSON file (default: stdout)")
def batch_search(file, limit, threshold, as_of, level, match_hooks, output):
    """Run batch search for multiple queries.

    Args:
        file: Input file with one query per line.
        limit: Maximum results per query.
        threshold: Minimum similarity score (0-100).
        as_of: Historical date (YYYY-MM-DD).
        level: Filter results to a specific admin level.
        match_hooks: Name-levels to score against (defaults to barangay).
        output: Output JSON file path.

    Returns:
        None
    """
    try:
        queries = Path(file).read_text(encoding="utf-8").strip().split("\n")
        results: dict[str, list[dict]] = {}
        resolved_level = _resolve_level(level)
        hooks = list(match_hooks) or None

        with console.status("[cyan]Processing queries...") as status:
            for query in queries:
                query = query.strip()
                if not query:
                    continue
                status.update(f"[cyan]Searching: {query}[/cyan]")
                srs = search_fuzzy(
                    query,
                    level=resolved_level,
                    match_hooks=hooks,
                    threshold=threshold,
                    limit=limit,
                    as_of=as_of,
                )
                results[query] = [to_result_dict(sr) for sr in srs]

        output_data = json.dumps(results, indent=2, ensure_ascii=False, default=str)

        if output:
            Path(output).write_text(output_data, encoding="utf-8")
            console.print(f"[green]Results saved to {output}[/green]")
        else:
            console.print_json(data=results)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@batch.command("validate")
@click.argument("file", type=click.Path(exists=True))
@click.option("--as-of", help="Historical date (YYYY-MM-DD)")
@click.option(
    "--threshold",
    "-t",
    default=95.0,
    help="Minimum score for a valid match (0-100)",
)
def batch_validate(file, as_of, threshold):
    """Validate addresses from file (one full address per line).

    Args:
        file: Input file with one address per line.
        as_of: Historical date (YYYY-MM-DD).
        threshold: Minimum score for a valid match (0-100).

    Returns:
        None
    """
    try:
        addresses = Path(file).read_text(encoding="utf-8").strip().split("\n")

        table = Table(title="Validation Results")
        table.add_column("Input", style="cyan")
        table.add_column("Valid", style="green")
        table.add_column("Match", style="yellow")
        table.add_column(_RPHICMSGB, style="magenta")
        table.add_column("Score", style="blue")

        for address in addresses:
            address = address.strip()
            if not address:
                continue

            result = validate(address, threshold=threshold, as_of=as_of)
            if result.valid and result.matched_record is not None:
                enriched = _resolve_enriched(result.matched_record)
                rphi = rphicmsgb(enriched) if enriched else "000000000"
                match = enriched.name if enriched else result.matched_record.name
                score = f"{result.score:.1f}" if result.score is not None else "-"
                table.add_row(address, "[green]Valid[/green]", match, rphi, score)
            else:
                table.add_row(
                    address,
                    "[red]Not found[/red]",
                    "-",
                    "000000000",
                    "-",
                )

        console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@app.group()
def plugins():
    """Plugin management commands."""
    pass


@plugins.command("list")
def plugins_list():
    """List available plugins."""
    db = Database()
    table = Table(title="Available Plugins")
    table.add_column("Name", style="cyan")
    table.add_column("Status", style="green")
    table.add_column("Description", style="dim")

    for p in db.available_plugins():
        status = "[green]enabled[/green]" if p.enabled else "[dim]disabled[/dim]"
        table.add_row(p.name, status, p.description or "")

    console.print(table)


@plugins.command("info")
@click.argument("name")
def plugins_info(name):
    """Show details for a specific plugin."""
    db = Database()
    for p in db.available_plugins():
        if p.name == name:
            table = Table(title=f"Plugin: {p.name}")
            table.add_column("Property", style="cyan")
            table.add_column("Value", style="green")
            table.add_row("Name", p.name)
            table.add_row("Enabled", str(p.enabled))
            table.add_row("Description", p.description or "N/A")
            table.add_row("Version", p.version or "N/A")
            table.add_row("Format", p.format or "N/A")
            table.add_row("Repository", p.repository or "N/A")
            if p.error:
                table.add_row("Error", f"[red]{p.error}[/red]")
            console.print(table)
            return

    console.print(f"[red]Plugin '{name}' not found.[/red]")
    raise click.ClickException(f"Plugin '{name}' not found")


if __name__ == "__main__":
    app()
