---
description: "Automated code formatting using project's configured formatter (prettier, eslint --fix, etc.)"
argument-hint: "[path] [--tool=<formatter>] [--config=<config_file>] [--check-only]"
allowed-tools: Read, Edit, MultiEdit, Bash
---

# Command: Apply Style Rules

## Purpose

Applies automated code formatting using project's configured formatters (Prettier, ESLint --fix, Black, etc.) to ensure consistent code style.

## Usage

```bash
/clean:apply-style-rules $ARGUMENTS
```

**Arguments**:

- `$1` (path): Specific file or directory to format (optional)
- `$2` (--tool): Specific formatter to use (prettier, eslint, black, rustfmt) (optional)
- `$3` (--config): Custom configuration file to use (optional)
- `$4` (--check-only): Only check for style violations without fixing (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "src/"` - Format all files in src directory
- `$ARGUMENTS = "--tool=prettier --check-only"` - Check style with Prettier
- `$ARGUMENTS = "components/ --tool=eslint --config=.eslintrc.custom"` - Use custom config

## Process

1. **Parallel Tool Detection**: Use Task() to identify available formatters and configurations:

   ```python
   Task("detect-formatters", "Scan for available formatting tools (prettier, eslint, black, etc.)")
   Task("detect-configs", "Find project configuration files (.prettierrc, .eslintrc, etc.)")
   Task("analyze-file-types", "Identify file types and their appropriate formatters")
   ```

2. **Configuration Analysis**: Determine optimal formatting strategy:
   - Check for project-specific formatter configurations
   - Identify file types and their appropriate tools
   - Validate formatter availability and versions
   - Handle conflicting or overlapping tool configurations

3. **Batch Formatting**: Apply style rules efficiently based on $ARGUMENTS scope:
   - Group files by formatter type for batch processing
   - Run formatters in parallel for different file types
   - Handle formatter-specific options and exclusions
   - Preserve file permissions and timestamps

4. **Validation**: Ensure formatting was applied correctly:
   - Verify no syntax errors were introduced
   - Check that all targeted files were processed
   - Report any files that couldn't be formatted
   - Validate consistent style across project

5. **Results Summary**: Provide comprehensive formatting report

## Agent Integration

- **Primary Agent**: quality-analyst - Can be spawned to execute automated formatting with project-aware tool selection and parallel processing

## Parallelization Patterns

**Multi-Tool Execution**: Run different formatters in parallel for different file types to maximize processing speed.

**Batch Processing**: Group similar files together for efficient formatter execution and reduced startup overhead.

## Examples

```bash
# Auto-format all files with detected tools
/clean:apply-style-rules

# Format specific directory with Prettier
/clean:apply-style-rules $ARGUMENTS
# where $ARGUMENTS = "src/ --tool=prettier"

# Check style violations without fixing
/clean:apply-style-rules $ARGUMENTS
# where $ARGUMENTS = "--check-only"
```
