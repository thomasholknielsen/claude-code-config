# Pre-commit Hooks Setup Guide

This guide explains how to set up pre-commit hooks for automatic code quality enforcement.

## Overview

Pre-commit hooks automatically fix linting errors and formatting issues before commits, ensuring consistent code quality across the repository.

## Automatic Fixes Applied

### Markdown Files

- **Trailing whitespace removal**
- **Final newline insertion**
- **Line length adjustments**
- **List formatting standardization**
- **Header formatting consistency**

### Python Files

- **Code formatting** with Ruff formatter
- **Import sorting** and organization
- **Linting fixes** for common issues
- **Style consistency** enforcement

### YAML Files

- **Indentation standardization**
- **Syntax validation**
- **Formatting consistency**

### General Files

- **Trailing whitespace removal**
- **Final newline insertion**
- **Merge conflict detection**
- **Large file prevention** (>500KB)

## Installation Instructions

### Prerequisites

**macOS/Linux:**

```bash
# Install pre-commit via Homebrew (recommended)
brew install pre-commit

# Alternative: Install via pip
pip install pre-commit
```

**Windows:**

```bash
# Install via pip
pip install pre-commit

# Alternative: Install via chocolatey
choco install pre-commit
```

### Repository Setup

1. **Clone and navigate to repository:**

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install pre-commit hooks:**

   ```bash
   pre-commit install
   ```

3. **Verify installation:**

   ```bash
   pre-commit run --all-files
   ```

## Usage

### Automatic Operation

Once installed, pre-commit hooks run automatically on every `git commit`:

```bash
# Normal commit workflow
git add .
git commit -m "your commit message"

# Hooks run automatically and may:
# ✅ Fix issues and proceed with commit
# ❌ Fix issues but require re-staging and re-committing
```

### Manual Execution

Run hooks manually on all files:

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run markdownlint --all-files

# Run hooks on specific files
pre-commit run --files path/to/file.md
```

### Updating Hooks

Keep hooks up to date:

```bash
# Update to latest versions
pre-commit autoupdate

# Reinstall after updates
pre-commit install
```

## Configuration Details

### Hooks Included

The `.pre-commit-config.yaml` includes:

1. **General File Cleanup**
   - Trailing whitespace removal
   - Final newline insertion
   - Merge conflict detection
   - YAML/JSON syntax validation

2. **Markdown Processing**
   - Markdownlint auto-fixing
   - Line length enforcement
   - Formatting standardization

3. **Python Code Quality**
   - Ruff linting with auto-fix
   - Ruff formatting
   - Import organization

4. **Shell Script Validation**
   - Shellcheck warnings
   - Best practice enforcement

5. **YAML Formatting**
   - Prettier auto-formatting
   - Consistent indentation

### Exclusions

Certain files are excluded from processing:

- `.git/` directory
- `__pycache__/` directories
- Minified files (`.min.js`, `.min.css`)
- Virtual environments
- Environment files (`.env`)

## Troubleshooting

### Common Issues

**1. Hook Installation Fails**

```bash
# Ensure you're in the repository root
cd /path/to/repository

# Reinstall hooks
pre-commit clean
pre-commit install
```

**2. Hooks Run But Don't Fix Issues**

```bash
# Run hooks manually to see detailed output
pre-commit run --all-files --verbose

# Check configuration
pre-commit validate-config
```

**3. Python Environment Issues**

```bash
# Use system Python
pre-commit install --install-hooks

# Or specify Python version
pre-commit install --install-hooks --python python3.11
```

### Skipping Hooks (Emergency Only)

```bash
# Skip all pre-commit hooks (NOT RECOMMENDED)
git commit --no-verify -m "emergency commit"

# Skip specific hook
SKIP=markdownlint git commit -m "skip markdown linting"
```

## Team Guidelines

### For New Team Members

1. **Install pre-commit** using instructions above
2. **Run initial setup**: `pre-commit run --all-files`
3. **Verify hooks work** with a test commit
4. **Report issues** if hooks don't work as expected

### For Repository Maintainers

1. **Update hooks regularly**: `pre-commit autoupdate`
2. **Test configuration changes** before pushing
3. **Document any new exclusions** or special rules
4. **Monitor hook performance** and adjust if needed

### Best Practices

- **Let hooks fix issues** rather than manual fixes
- **Stage files after hook fixes** automatically applied
- **Don't skip hooks** unless absolutely necessary
- **Review auto-fixes** to understand what changed
- **Report persistent issues** that hooks can't fix

## Integration with Development Workflow

### VS Code Integration

Add to `.vscode/settings.json`:

```json
{
  "python.linting.enabled": true,
  "python.formatting.provider": "ruff",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  }
}
```

### GitHub Actions Integration

Pre-commit hooks can also run in CI/CD:

```yaml
# .github/workflows/pre-commit.yml
name: pre-commit
on: [push, pull_request]
jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
      - uses: pre-commit/action@v3.0.0
```

## Hook Configuration Reference

### Markdownlint Configuration

Located in `.markdownlint.yml`:

- Line length: 150 characters
- Allows inline HTML for specific elements
- Trailing punctuation allowed in headers
- Multiple headers with same content allowed

### Ruff Configuration

Located in `pyproject.toml`:

- Target Python version: 3.8+
- Line length: 120 characters
- Comprehensive rule selection
- Project-specific ignores

### Prettier Configuration

- YAML files auto-formatted
- Consistent indentation
- Trailing comma handling

This setup ensures consistent code quality while minimizing developer friction through automatic fixing.
