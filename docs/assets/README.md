# docs/assets

Reusable branding and OG/social assets for the `barangay` project.

## Files

| File | Purpose |
|------|---------|
| `og-card.svg` | Master source for the 1200×630 social/OG card |

## Producing `og-card.png`

Social platforms (Twitter/X, Facebook, LinkedIn, Slack) generally require a
**PNG/JPG** OG image — SVG is not reliably supported. To export the card:

```bash
# Using rsvg-convert (librsvg)
rsvg-convert -w 1200 -h 630 og-card.svg -o og-card.png

# Or using ImageMagick
convert -density 144 -resize 1200x630\! og-card.svg og-card.png

# Or using Inkscape
inkscape og-card.svg --export-type=png --export-filename=og-card.png -w 1200 -h 630
```

After exporting `og-card.png`, update `extra.meta` → `og:image` in `mkdocs.yml`
to point at `https://bendlikeabamboo.github.io/barangay/og-card.png`, and upload
the same image as the GitHub repository **Social preview** (repo Settings →
Social preview).
