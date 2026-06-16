import shutil
import xml.etree.ElementTree as ET
from pathlib import Path


def on_post_build(config, **kwargs):
    site_url = config["site_url"].rstrip("/")
    if not site_url:
        return

    output_dir = Path(config["site_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    nav = config["nav"]
    pages = _collect_pages(nav)

    for page_url in pages:
        url = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url, "loc")
        if page_url == "index.md":
            loc.text = site_url
        else:
            loc.text = f"{site_url}/{page_url.replace('.md', '/')}"
        priority = ET.SubElement(url, "priority")
        priority.text = "1.0" if page_url == "index.md" else "0.8"

    # Include any built HTML pages not represented in nav (generated LGU pages,
    # blog posts, etc.) by globbing the site directory.
    seen_locs: set[str] = {
        loc.text
        for url in urlset.findall("url")
        if (loc := url.find("loc")) is not None and loc.text
    }
    for html_file in sorted(output_dir.rglob("*.html")):
        rel = html_file.relative_to(output_dir).as_posix()
        if rel == "index.html":
            continue
        loc_text = (
            f"{site_url}/{rel[:-5]}/" if rel.endswith(".html") else f"{site_url}/{rel}"
        )
        if loc_text in seen_locs:
            continue
        seen_locs.add(loc_text)
        url = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = loc_text
        ET.SubElement(url, "priority").text = "0.6"

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(output_dir / "sitemap.xml", xml_declaration=True, encoding="utf-8")

    docs_dir = Path(config["docs_dir"])
    for txt_file in ["llms.txt", "llms-full.txt"]:
        src = docs_dir / txt_file
        if src.exists():
            shutil.copy2(src, output_dir / txt_file)


def _collect_pages(nav):
    pages = []
    for item in nav:
        if isinstance(item, str):
            pages.append(item)
        elif isinstance(item, dict):
            for _key, value in item.items():
                if isinstance(value, list):
                    pages.extend(_collect_pages(value))
                elif isinstance(value, str):
                    pages.append(value)
    return pages
