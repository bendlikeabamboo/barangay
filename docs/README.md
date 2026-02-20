# Barangay Documentation

This directory contains the Sphinx documentation for the barangay package.

## Building the Documentation

### Prerequisites

Install the documentation dependencies:

```bash
uv sync --group docs
```

Or using pip:

```bash
pip install sphinx furo sphinx-copybutton sphinx-design sphinx-autodoc-typehints sphinx-autobuild
```

### Building HTML Documentation

To build the HTML documentation:

```bash
cd docs
make html
```

The built documentation will be in `_build/html/`. Open `_build/html/index.html` in your browser to view it.

### Building Other Formats

Sphinx supports multiple output formats:

- **HTML**: `make html`
- **PDF**: `make latexpdf`
- **EPUB**: `make epub`
- **Man pages**: `make man`

### Live Preview

To build the documentation with live preview (automatically rebuilds on changes):

```bash
cd docs
make livehtml
```

Then open `http://127.0.0.1:8000` in your browser.

### Cleaning Build Files

To clean the build directory:

```bash
cd docs
make clean
```

## Documentation Structure

```
docs/
├── conf.py                          # Sphinx configuration
├── index.rst                        # Main documentation index
├── Makefile                         # Build commands (Unix/Linux/macOS)
├── make.bat                         # Build commands (Windows)
├── _static/                         # Static files (CSS, images, etc.)
├── _templates/                      # Custom Jinja2 templates
├── quick_start/                     # Quick start guide
├── user_guide/                      # User guides
├── api_reference/                   # API reference
├── advanced/                        # Advanced topics
├── examples/                        # Real-world examples
├── troubleshooting/                 # Troubleshooting guide
└── contributing/                    # Contributing guide
```

## Adding Content

### Creating New Pages

1. Create a new `.rst` file in the appropriate directory
2. Add it to the table of contents in `index.rst` or the appropriate section index
3. Build the documentation to verify

### Editing Existing Pages

1. Edit the `.rst` file
2. Build the documentation to verify changes

### reST Syntax

The documentation uses reStructuredText (reST). For syntax reference:

- [reST Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Sphinx Directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)

## Configuration

The Sphinx configuration is in `conf.py`. Key settings:

- **Theme**: furo (modern, clean design)
- **Extensions**: autodoc, napoleon, viewcode, intersphinx, copybutton, design
- **Python Version**: 3.10+
- **Source Directory**: `docs/`
- **Build Directory**: `docs/_build/`

## Troubleshooting

### Build Errors

If you encounter build errors:

1. Ensure all dependencies are installed
2. Check that the Python version is 3.10+
3. Verify that the `barangay` package is importable
4. Check the error message for specific issues

### Missing API Documentation

If API documentation is missing:

1. Ensure the package is installed in development mode
2. Check that `sys.path` in `conf.py` includes the parent directory
3. Verify that docstrings follow Google or NumPy style

### Style Issues

If the documentation looks incorrect:

1. Check the theme options in `conf.py`
2. Verify that `_static/custom.css` exists
3. Clear the build directory and rebuild

## Contributing

When contributing to the documentation:

1. Follow the existing style and structure
2. Use clear, concise language
3. Include code examples where appropriate
4. Test all code examples
5. Build the documentation before submitting

## Additional Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Furo Theme Documentation](https://pradyunsg.me/furo/)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Napoleon Extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
