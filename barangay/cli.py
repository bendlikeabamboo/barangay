"""CLI for barangay package."""

import csv
import json
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from barangay import (
    BARANGAY,
    BARANGAY_EXTENDED,
    BARANGAY_FLAT,
    DataManager,
    available_dates,
    current,
    get_available_dates,
    get_cache_dir,
    search,
)

console = Console()


@click.group()
@click.version_option(version=current)
def app():
    """Barangay: Philippine Geographic/Administrative Data CLI."""
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
def search_cmd(query, limit, threshold, as_of, output_format):
    """Fuzzy search for barangays."""
    try:
        results = search(query, n=limit, threshold=threshold, as_of=as_of)

        if not results:
            console.print("[yellow]No results found.[/yellow]")
            return

        if output_format == "json":
            console.print_json(data=results)
        else:
            table = Table(title=f"Search Results for '{query}'")
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


@app.group()
def info():
    """Show data information."""
    pass


@info.command()
def version():
    """Show current data version."""
    console.print(f"[cyan]Current version:[/cyan] {current}")
    console.print(f"[cyan]Available dates:[/cyan] {', '.join(available_dates)}")


@info.command()
def stats():
    """Show data statistics."""

    def count_dict(d):
        count = 0
        for v in d.values():
            if isinstance(v, dict):
                count += count_dict(v)
            else:
                count += 1
        return count

    basic_count = count_dict(BARANGAY)
    flat_count = len(BARANGAY_FLAT)
    extended_count = count_dict(BARANGAY_EXTENDED)

    table = Table(title="Data Statistics")
    table.add_column("Model", style="cyan")
    table.add_column("Count", style="green")

    table.add_row("Basic (nested)", str(basic_count))
    table.add_row("Flat (list)", str(flat_count))
    table.add_row("Extended (recursive)", str(extended_count))
    console.print(table)


@info.command()
def list_regions():
    """List all regions."""
    table = Table(title="Regions")
    table.add_column("Region", style="cyan")

    for region in sorted(BARANGAY.keys()):
        table.add_row(region)
    console.print(table)


@info.command()
@click.argument("region")
def list_municipalities(region):
    """List municipalities in a region."""
    if region not in BARANGAY:
        console.print(f"[red]Region '{region}' not found.[/red]")
        raise click.ClickException(f"Region '{region}' not found")

    table = Table(title=f"Municipalities in {region}")
    table.add_column("Municipality/City", style="cyan")

    for municipality in sorted(BARANGAY[region].keys()):
        table.add_row(municipality)
    console.print(table)


@info.command()
@click.argument("municipality")
def list_barangays(municipality):
    """List barangays in a municipality."""
    found = False
    for region, municipalities in BARANGAY.items():
        if municipality in municipalities:
            table = Table(title=f"Barangays in {municipality} ({region})")
            table.add_column("Barangay", style="cyan")

            for barangay in sorted(municipalities[municipality]):
                table.add_row(barangay)
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
def export(model, output_format, output, as_of):
    """Export data to JSON/CSV."""
    try:
        dm = DataManager()
        data_type = {"basic": "basic", "flat": "flat", "extended": "extended"}[model]
        data = dm.get_data(as_of=as_of, data_type=data_type)

        if model == "flat":
            items = data
        else:
            items = data

        if output_format == "json":
            output_data = json.dumps(items, indent=2, ensure_ascii=False)
        else:
            if model == "flat":
                output_data = _dict_to_csv(items)
            else:
                output_data = _nested_to_csv(items)

        if output:
            Path(output).write_text(output_data, encoding="utf-8")
            console.print(f"[green]Exported to {output}[/green]")
        else:
            console.print(output_data)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise click.ClickException(str(e))


def _dict_to_csv(data):
    """Convert flat data to CSV string."""
    import io

    output = io.StringIO()
    if data:
        writer = csv.DictWriter(output, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return output.getvalue()


def _nested_to_csv(data):
    """Convert nested data to CSV string."""
    import io

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Region", "Municipality", "Barangay"])

    for region, municipalities in data.items():
        for municipality, barangays in municipalities.items():
            for barangay in barangays:
                writer.writerow([region, municipality, barangay])
    return output.getvalue()


@app.group()
def history():
    """Historical data operations."""
    pass


@history.command()
def list_dates():
    """List available historical dates."""
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
    """Search historical data."""
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
    """Export historical data."""
    try:
        dm = DataManager()
        data_type = {"basic": "basic", "flat": "flat", "extended": "extended"}[model]
        data = dm.get_data(as_of=as_of, data_type=data_type)

        if model == "flat":
            items = data
        else:
            items = data

        if output_format == "json":
            output_data = json.dumps(items, indent=2, ensure_ascii=False)
        else:
            if model == "flat":
                output_data = _dict_to_csv(items)
            else:
                output_data = _nested_to_csv(items)

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
    """Cache management."""
    pass


@cache.command()
def clear():
    """Clear cache directory."""
    cache_dir = get_cache_dir()
    if not cache_dir.exists():
        console.print("[yellow]Cache directory is empty.[/yellow]")
        return

    import shutil

    shutil.rmtree(cache_dir)
    console.print(f"[green]Cache cleared: {cache_dir}[/green]")


@cache.command()
def info():
    """Show cache information."""
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
    """Download data to cache."""
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
    """Batch processing."""
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
    """Batch search from file (one query per line)."""
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
    """Validate barangay names from file (one per line)."""
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
