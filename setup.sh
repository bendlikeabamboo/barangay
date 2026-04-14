#!/usr/bin/env zsh
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

confirm_prompt() {
    local message="$1"
    echo -n "$message (yes/no): "
    read -r response
    [[ "$response" == "yes" || "$response" == "y" ]]
}

echo ""
echo "============================================"
echo "  Barangay Environment Setup"
echo "============================================"
echo ""
echo -e "\033[33mThis script will install the following:\033[0m"
echo "  - uv (Python package manager)"
echo "  - poethepoet (task runner)"
echo "  - Python virtual environment (.venv) with all project"
echo "    dependencies (pandas, rapidfuzz, pydantic, click,"
echo "    rich, tornado, fastparquet, python-dotenv, etc.)"
echo "  - Dev dependencies (pytest, ruff, pre-commit,"
echo "    mypy stubs, ipykernel, etc.)"
echo ""

if ! confirm_prompt "Do you accept and want to proceed?"; then
    echo -e "\033[31mSetup cancelled.\033[0m"
    exit 0
fi

echo ""

if ! command -v uv &> /dev/null; then
    echo -e "\033[33m[uv] Not found.\033[0m"
    echo "  uv is an extremely fast Python package manager."
    echo "  It will be installed via the official installer."

    if confirm_prompt "  Install uv?"; then
        echo -e "\033[32m  Installing uv...\033[0m"
        curl -LsSf https://astral.sh/uv/install.sh | sh

        if ! command -v uv &> /dev/null; then
            export PATH="$HOME/.local/bin:$PATH"
        fi

        if ! command -v uv &> /dev/null; then
            echo -e "\033[31m  [ERROR] uv installation failed. Try restarting your terminal and running the script again.\033[0m"
            exit 1
        fi

        echo -e "\033[32m  uv installed successfully: $(uv --version)\033[0m"
    else
        echo "  Skipping uv installation."
        exit 1
    fi
else
    echo -e "\033[32m[uv] Already installed: $(uv --version)\033[0m"
fi

echo ""

if ! command -v poe &> /dev/null; then
    echo -e "\033[33m[poethepoet] Not found.\033[0m"
    echo "  poethepoet is a task runner for Python projects."
    echo "  It will be installed via uv tool install."

    if confirm_prompt "  Install poethepoet?"; then
        echo -e "\033[32m  Installing poethepoet...\033[0m"
        uv tool install poethepoet

        if ! command -v poe &> /dev/null; then
            echo -e "\033[31m  [ERROR] poethepoet installation failed. Try restarting your terminal and running the script again.\033[0m"
            exit 1
        fi

        echo -e "\033[32m  poethepoet installed successfully: $(poe --version)\033[0m"
    else
        echo "  Skipping poethepoet installation."
        exit 1
    fi
else
    echo -e "\033[32m[poethepoet] Already installed: $(poe --version)\033[0m"
fi

echo ""

if [ ! -d "$VENV_DIR" ]; then
    echo -e "\033[33m[.venv] Not found.\033[0m"
    echo "  A Python virtual environment will be created at:"
    echo "    $VENV_DIR"
    echo "  All project and dev dependencies will be installed into it."

    if confirm_prompt "  Create .venv and install dependencies?"; then
        echo -e "\033[32m  Creating virtual environment...\033[0m"
        uv sync --all-groups

        if [ ! -d "$VENV_DIR" ]; then
            echo -e "\033[31m  [ERROR] Virtual environment creation failed.\033[0m"
            exit 1
        fi

        echo -e "\033[32m  .venv created and dependencies installed.\033[0m"
    else
        echo "  Skipping .venv creation."
        exit 1
    fi
else
    echo -e "\033[32m[.venv] Already exists at $VENV_DIR\033[0m"
fi

echo ""
echo "============================================"
echo "  Activating virtual environment..."
echo "============================================"
echo ""

ACTIVATE_SCRIPT="$VENV_DIR/bin/activate"
if [ -f "$ACTIVATE_SCRIPT" ]; then
    # shellcheck source=/dev/null
    source "$ACTIVATE_SCRIPT"
    echo -e "\033[32mVirtual environment activated.\033[0m"
    echo ""
    echo -e "\033[33mTo activate in a new terminal, run:\033[0m"
    echo "  source .venv/bin/activate"
else
    echo -e "\033[31m[WARNING] Activate script not found at $ACTIVATE_SCRIPT\033[0m"
    exit 1
fi

echo ""
echo -e "\033[32mSetup complete!\033[0m"
