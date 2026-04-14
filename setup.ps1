$ErrorActionPreference = "Stop"

$ProjectDir = $PSScriptRoot
$VenvDir = Join-Path $ProjectDir ".venv"

function Confirm-Prompt($message) {
    $response = Read-Host "$message (yes/no)"
    return ($response -eq "yes" -or $response -eq "y")
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Barangay Environment Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script will install the following:" -ForegroundColor Yellow
Write-Host "  - uv (Python package manager)" -ForegroundColor White
Write-Host "  - poethepoet (task runner)" -ForegroundColor White
Write-Host "  - Python virtual environment (.venv) with all project" -ForegroundColor White
Write-Host "    dependencies (pandas, rapidfuzz, pydantic, click," -ForegroundColor White
Write-Host "    rich, tornado, fastparquet, python-dotenv, etc.)" -ForegroundColor White
Write-Host "  - Dev dependencies (pytest, ruff, pre-commit," -ForegroundColor White
Write-Host "    mypy stubs, ipykernel, etc.)" -ForegroundColor White
Write-Host ""

if (-not (Confirm-Prompt "Do you accept and want to proceed?")) {
    Write-Host "Setup cancelled." -ForegroundColor Red
    exit 0
}

Write-Host ""

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "[uv] Not found." -ForegroundColor Yellow
    Write-Host "  uv is an extremely fast Python package manager." -ForegroundColor Gray
    Write-Host "  It will be installed via the official installer." -ForegroundColor Gray

    if (Confirm-Prompt "  Install uv?") {
        Write-Host "  Installing uv..." -ForegroundColor Green
        Invoke-RestMethod -Uri https://astral.sh/uv/install.ps1 | Invoke-Expression
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

        if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
            Write-Host "  [ERROR] uv installation failed." -ForegroundColor Red
            exit 1
        }
        Write-Host "  uv installed successfully." -ForegroundColor Green
    } else {
        Write-Host "  Skipping uv installation." -ForegroundColor DarkGray
        exit 1
    }
} else {
    Write-Host "[uv] Already installed: $(uv --version)" -ForegroundColor Green
}

Write-Host ""

if (-not (Get-Command poe -ErrorAction SilentlyContinue)) {
    Write-Host "[poethepoet] Not found." -ForegroundColor Yellow
    Write-Host "  poethepoet is a task runner for Python projects." -ForegroundColor Gray
    Write-Host "  It will be installed via uv tool install." -ForegroundColor Gray

    if (Confirm-Prompt "  Install poethepoet?") {
        Write-Host "  Installing poethepoet..." -ForegroundColor Green
        uv tool install poethepoet

        if (-not (Get-Command poe -ErrorAction SilentlyContinue)) {
            Write-Host "  [ERROR] poethepoet installation failed." -ForegroundColor Red
            exit 1
        }
        Write-Host "  poethepoet installed successfully." -ForegroundColor Green
    } else {
        Write-Host "  Skipping poethepoet installation." -ForegroundColor DarkGray
        exit 1
    }
} else {
    Write-Host "[poethepoet] Already installed: $(poe --version)" -ForegroundColor Green
}

Write-Host ""

if (-not (Test-Path $VenvDir)) {
    Write-Host "[.venv] Not found." -ForegroundColor Yellow
    Write-Host "  A Python virtual environment will be created at:" -ForegroundColor Gray
    Write-Host "    $VenvDir" -ForegroundColor Gray
    Write-Host "  All project and dev dependencies will be installed into it." -ForegroundColor Gray

    if (Confirm-Prompt "  Create .venv and install dependencies?") {
        Write-Host "  Creating virtual environment..." -ForegroundColor Green
        uv sync --all-groups

        if (-not (Test-Path $VenvDir)) {
            Write-Host "  [ERROR] Virtual environment creation failed." -ForegroundColor Red
            exit 1
        }
        Write-Host "  .venv created and dependencies installed." -ForegroundColor Green
    } else {
        Write-Host "  Skipping .venv creation." -ForegroundColor DarkGray
        exit 1
    }
} else {
    Write-Host "[.venv] Already exists at $VenvDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Activating virtual environment..." -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

$ActivateScript = Join-Path $VenvDir "Scripts" "Activate.ps1"
if (Test-Path $ActivateScript) {
    & $ActivateScript
    Write-Host "Virtual environment activated." -ForegroundColor Green
    Write-Host ""
    Write-Host "To activate in a new terminal, run:" -ForegroundColor Yellow
    Write-Host "  .\.venv\Scripts\Activate.ps1" -ForegroundColor White
} else {
    Write-Host "[WARNING] Activate script not found at $ActivateScript" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Setup complete!" -ForegroundColor Green
