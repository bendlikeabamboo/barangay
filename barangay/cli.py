import csv
import json
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from barangay import (
    barangay,
    barangay_extended,
    barangay_flat,
    DataManager,
    available_dates,
    current,
    get_available_dates,
    get_cache_dir,
    search,
)
from barangay.explode import ExplodeError, explode_flat
from barangay.plugin_loader import (
    PluginLoader,
)

console = Console()


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
def search_cmd(query, limit, threshold, as_of, output_format, plugins):
    """Search for barangays by name.

    Args:
        query: Search query string.
        limit: Maximum number of results.
        threshold: Minimum similarity score (0-100).
        as_of: Historical date (YYYY-MM-DD).
        output_format: Output format (json or table).

    Returns:
        None
    """
    try:
        results = search(query, n=limit, threshold=threshold, as_of=as_of)

        if not results:
            console.print("[yellow]No results found.[/yellow]")
            return

        if plugins:
            results = _apply_plugins_to_results(results, plugins, as_of)

        if output_format == "json":
            console.print_json(data=results)
        else:
            table = Table(title=f"Search Results for '{query}'")
            table.add_column("Barangay", style="cyan")
            table.add_column("Municipality/City", style="magenta")
            table.add_column("Province/HUC", style="green")
            table.add_column("PSGC ID", style="blue")
            table.add_column("Score", style="yellow")

            plugin_columns: list[str] = []
            for r in results:
                for key in r:
                    if "." in key and key not in plugin_columns:
                        plugin_columns.append(key)

            for col in plugin_columns:
                table.add_column(col, style="dim")

            for r in results:
                max_score = max(v for k, v in r.items() if k.endswith("_score"))
                values = [
                    r["barangay"],
                    r["municipality_or_city"],
                    r["province_or_huc"],
                    r["psgc_id"],
                    f"{max_score:.1f}",
                ]
                for col in plugin_columns:
                    values.append(str(r.get(col, "")))
                table.add_row(*values)
            console.print(table)
    except ExplodeError as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


def _apply_plugins_to_results(
    results: list[dict],
    plugins: tuple[str, ...],
    as_of: str | None,
) -> list[dict]:
    loader = PluginLoader(env=True)
    for name in plugins:
        loader.enable_plugin(name)
    plugin_index = loader.build_index(as_of=as_of)

    if plugin_index:
        from barangay.explode import classify_plugins, validate_single_array

        _, array_plugins = classify_plugins(plugin_index)
        validate_single_array(array_plugins)
        if array_plugins:
            click.echo(
                click.style(
                    "Warning: Array-type plugins are not supported with search. "
                    "Only scalar plugin data will be included.",
                    fg="yellow",
                ),
                err=True,
            )

    output: list[dict] = []
    for r in results:
        psgc_id = str(r.get("psgc_id", ""))
        plugins_data = plugin_index.get(psgc_id, {})
        row = dict(r)
        for plugin_name, entry in plugins_data.items():
            data = entry.get("data")
            if isinstance(data, dict):
                for key, value in data.items():
                    row[f"{plugin_name}.{key}"] = value
        output.append(row)
    return output


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
    """Display data statistics.

    Returns:
        None
    """

    def count_barangays_nested(d):
        """Count total barangays in nested dict.

        Args:
            d: Nested dictionary to count barangays from.

        Returns:
            Total count of barangays.
        """
        count = 0
        for v in d.values():
            if isinstance(v, dict):
                count += count_barangays_nested(v)
            elif isinstance(v, list):
                count += len(v)
        return count

    def count_barangays_extended(data):
        """Count barangays in AdminDivExtended model.

        Args:
            data: AdminDivExtended instance.

        Returns:
            Total count of barangays.
        """
        count = 1 if data.type == "barangay" else 0
        for comp in data.components:
            count += count_barangays_extended(comp)
        return count

    # Count barangays in each model
    barangay_dict = barangay.model_dump()
    basic_count = count_barangays_nested(barangay_dict)
    flat_count = sum(1 for item in barangay_flat if item.type == "barangay")
    extended_count = count_barangays_extended(barangay_extended)

    table = Table(title="Barangay Statistics")
    table.add_column("Model", style="cyan")
    table.add_column("Barangay Count", style="green")

    table.add_row("Basic (nested)", str(basic_count))
    table.add_row("Flat (list)", str(flat_count))
    table.add_row("Extended (recursive)", str(extended_count))
    console.print(table)


@info.command()
def list_regions():
    """List all regions.

    Returns:
        None
    """
    table = Table(title="Regions")
    table.add_column("Region", style="cyan")

    # Cache model_dump() result to avoid repeated conversions
    barangay_dict = barangay.model_dump()
    for region in sorted(barangay_dict.keys()):
        table.add_row(region)
    console.print(table)


@info.command()
@click.argument("region")
def list_municipalities(region):
    """List municipalities in a region.

    Args:
        region: Region name.

    Returns:
        None
    """
    # Cache model_dump() result to avoid repeated conversions
    barangay_dict = barangay.model_dump()
    if region not in barangay_dict:
        console.print(f"[red]Region '{region}' not found.[/red]")
        raise click.ClickException(f"Region '{region}' not found")

    table = Table(title=f"Municipalities in {region}")
    table.add_column("Municipality/City", style="cyan")

    for municipality in sorted(barangay_dict[region].keys()):
        table.add_row(municipality)
    console.print(table)


@info.command()
@click.argument("municipality")
def list_barangays(municipality):
    """List barangays in a municipality.

    Args:
        municipality: Municipality name.

    Returns:
        None
    """
    # Cache model_dump() result to avoid repeated conversions
    barangay_dict = barangay.model_dump()
    found = False
    for region, municipalities in barangay_dict.items():
        if municipality in municipalities:
            table = Table(title=f"Barangays in {municipality} ({region})")
            table.add_column("Barangay", style="cyan")

            for brgy in sorted(municipalities[municipality]):
                table.add_row(brgy)
            console.print(table)
            found = True
            break

    if not found:
        console.print(f"[red]Municipality '{municipality}' not found.[/red]")
        raise click.ClickException(f"Municipality '{municipality}' not found")


@app.command()
@click.option(
    "--model",
    type=click.Choice(["flat", "extended", "basic"]),
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
    help="Enable a specific plugin for enrichment (repeatable)",
)
def export(model, output_format, output, as_of, plugins):
    """Export data to JSON or CSV.

    Args:
        model: Data model (flat, extended, or basic).
        output_format: Output format (json or csv).
        output: Output file path.
        as_of: Historical date (YYYY-MM-DD).
        plugins: Plugin names to enable for enrichment.
    """
    try:
        if plugins and model != "flat":
            raise click.ClickException("Plugins are only supported with --model flat")

        dm = DataManager()
        data_type = {"basic": "basic", "flat": "flat", "extended": "extended"}[model]
        data = dm.get_data(as_of=as_of, data_type=data_type)

        if plugins and model == "flat":
            loader = PluginLoader(env=True)
            for name in plugins:
                loader.enable_plugin(name)
            plugin_index = loader.build_index(as_of=as_of)
            data = explode_flat(data, plugin_index)

        if output_format == "json":
            output_data = json.dumps(data, indent=2, ensure_ascii=False)
        else:
            if model == "flat":
                output_data = _dict_to_csv(data)
            else:
                output_data = _nested_to_csv(data)

        if output:
            Path(output).write_text(output_data, encoding="utf-8")
            console.print(f"[green]Exported to {output}[/green]")
        else:
            console.print(output_data)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


def _dict_to_csv(data):
    """Convert list of dicts to CSV string.

    Args:
        data: List of dictionaries to convert.

    Returns:
        CSV formatted string.
    """
    import io

    output = io.StringIO()
    if data:
        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return output.getvalue()


def _nested_to_csv(data):
    """Convert nested dict to CSV string.

    Args:
        data: Nested dictionary with regions and municipalities.

    Returns:
        CSV formatted string.
    """
    import io

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Region", "Municipality", "Barangay"])

    for region, municipalities in data.items():
        for municipality, barangays in municipalities.items():
            for brgy in barangays:
                writer.writerow([region, municipality, brgy])
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


@history.command()
@click.argument("query")
@click.option("--as-of", required=True, help="Historical date (YYYY-MM-DD)")
@click.option("--limit", "-l", default=5, help="Maximum number of results")
@click.option(
    "--threshold", "-t", default=60.0, help="Minimum similarity score (0-100)"
)
@click.option(
    "--format",
    "-f",
    "output_format",
    type=click.Choice(["json", "table"]),
    default="table",
    help="Output format",
)
def search_history(query, as_of, limit, threshold, output_format):
    """Search historical data for barangays.

    Args:
        query: Search query string.
        as_of: Historical date (YYYY-MM-DD).
        limit: Maximum number of results.
        threshold: Minimum similarity score (0-100).
        output_format: Output format (json or table).

    Returns:
        None
    """
    try:
        results = search(query, n=limit, threshold=threshold, as_of=as_of)

        if not results:
            console.print("[yellow]No results found.[/yellow]")
            return

        if output_format == "json":
            console.print_json(data=results)
        else:
            table = Table(title=f"Search Results for '{query}' (as of {as_of})")
            table.add_column("Barangay", style="cyan")
            table.add_column("Municipality/City", style="magenta")
            table.add_column("Province/HUC", style="green")
            table.add_column("PSGC ID", style="blue")
            table.add_column("Score", style="yellow")

            for r in results:
                max_score = max(v for k, v in r.items() if k.endswith("_score"))
                table.add_row(
                    r["barangay"],
                    r["municipality_or_city"],
                    r["province_or_huc"],
                    r["psgc_id"],
                    f"{max_score:.1f}",
                )
            console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@history.command()
@click.option("--as-of", required=True, help="Historical date (YYYY-MM-DD)")
@click.option(
    "--model",
    type=click.Choice(["flat", "extended", "basic"]),
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
        model: Data model (flat, extended, or basic).
        output_format: Output format (json or csv).
        output: Output file path.

    Returns:
        None
    """
    try:
        dm = DataManager()
        data_type = {"basic": "basic", "flat": "flat", "extended": "extended"}[model]
        data = dm.get_data(as_of=as_of, data_type=data_type)

        if output_format == "json":
            output_data = json.dumps(data, indent=2, ensure_ascii=False)
        else:
            if model == "flat":
                output_data = _dict_to_csv(data)
            else:
                output_data = _nested_to_csv(data)

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

    import shutil

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
            dm.get_data(as_of=date, data_type="basic")
            console.print(f"[green]Downloaded data for {date}[/green]")
        else:
            console.print("[cyan]Downloading current data...[/cyan]")
            dm.get_data(data_type="basic")
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


@batch.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--limit", "-l", default=5, help="Maximum number of results per query")
@click.option(
    "--threshold", "-t", default=60.0, help="Minimum similarity score (0-100)"
)
@click.option("--as-of", help="Historical date (YYYY-MM-DD)")
@click.option("--output", "-o", help="Output JSON file (default: stdout)")
def batch_search(file, limit, threshold, as_of, output):
    """Run batch search for multiple queries.

    Args:
        file: Input file with one query per line.
        limit: Maximum results per query.
        threshold: Minimum similarity score (0-100).
        as_of: Historical date (YYYY-MM-DD).
        output: Output JSON file path.

    Returns:
        None
    """
    try:
        queries = Path(file).read_text(encoding="utf-8").strip().split("\n")
        results = {}

        with console.status("[cyan]Processing queries...") as status:
            for query in queries:
                query = query.strip()
                if not query:
                    continue
                status.update(f"[cyan]Searching: {query}[/cyan]")
                results[query] = search(
                    query, n=limit, threshold=threshold, as_of=as_of
                )

        output_data = json.dumps(results, indent=2, ensure_ascii=False)

        if output:
            Path(output).write_text(output_data, encoding="utf-8")
            console.print(f"[green]Results saved to {output}[/green]")
        else:
            console.print_json(data=results)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


@batch.command()
@click.argument("file", type=click.Path(exists=True))
def validate(file):
    """Validate barangay names from file.

    Args:
        file: Input file with one name per line.

    Returns:
        None
    """
    try:
        barangay_names = Path(file).read_text(encoding="utf-8").strip().split("\n")

        table = Table(title="Validation Results")
        table.add_column("Barangay", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Match", style="yellow")

        for name in barangay_names:
            name = name.strip()
            if not name:
                continue

            results = search(name, n=1, threshold=95.0)
            if results and results[0]["max_score"] >= 95.0:
                table.add_row(name, "[green]Valid[/green]", results[0]["barangay"])
            else:
                table.add_row(name, "[red]Not found[/red]", "-")

        console.print(table)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    app()
