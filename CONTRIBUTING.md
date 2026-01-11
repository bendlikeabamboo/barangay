# Contributing to Barangay

First off, thank you for considering contributing to Barangay! It's people like you that make Barangay such a great tool.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/bendlikeabamboo/barangay.git
   cd barangay
   ```

2. Install dependencies using `uv`:
   ```bash
   uv sync
   ```

3. Install pre-commit hooks:
   ```bash
   uv run pre-commit install
   ```

## Development Workflow

### Pre-commit Hooks

We use `pre-commit` to ensure code quality. The following hooks are configured:
- **Ruff**: For linting and formatting.
- **Mypy**: For static type checking.
- **Pip-audit**: To check for known vulnerabilities in dependencies.
- **Pytest**: To run the test suite.

These hooks will run automatically on every commit. You can also run them manually:
```bash
uv run pre-commit run --all-files
```

### Running Tests

We use `pytest` for testing. You can run the tests using:
```bash
uv run pytest
```

### Code Style

We follow the default `ruff` formatting and linting rules. Please ensure your code passes the `ruff` checks before submitting a pull request.

## Submitting Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and ensure they are well-tested.
3. Commit your changes. The pre-commit hooks will run automatically.
4. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request on GitHub.

## Reporting Issues

If you find a bug or have a feature request, please open an issue on the [GitHub Issue Tracker](https://github.com/bendlikeabamboo/barangay/issues).

Thank you for your contributions!
