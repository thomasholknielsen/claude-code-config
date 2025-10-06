---
description: "Rapidly apply common refactoring patterns for daily code improvements"
argument-hint: "[path] [--pattern=<pattern>] [--type=<refactor_type>]"
allowed-tools: Read, Edit, Bash
---

# Command: Apply

## Purpose

Applies atomic refactoring patterns including variable renaming, function extraction, logic simplification, and duplication removal for code improvements.

## Usage

```bash
/refactor:apply [path] [--pattern=<pattern>] [--type=<refactor_type>]
```

**Arguments**:

- `path` (optional): Specific file or directory to refactor
- `--pattern` (optional): Focus on specific code patterns (e.g., long-methods, duplicate-code)
- `--type` (optional): Refactor type (rename, extract, simplify, remove-duplication)

## Process

1. **Parse Arguments**: Process user-provided arguments from $ARGUMENTS:
   - `$1` (path): Target file or directory for refactoring
   - `$2` (--pattern): Specific code patterns to focus on
   - `$3` (--type): Type of refactor to perform

2. **Parallel Code Analysis**: Use Task() to analyze aspects based on $ARGUMENTS:

   ```python
   Task("analyze-complexity", f"Analyze method complexity in {$1 or 'current directory'}"),
   Task("analyze-naming", "Review variable and method names for clarity improvements"),
   Task("analyze-patterns", f"Detect {$2 or 'common'} refactoring opportunities")
   ```

3. **Apply Refactoring Patterns**: Execute refactoring patterns based on $ARGUMENTS type filter:
   - **rename**: Variable/method/class renaming for clarity
   - **extract**: Extract small, focused functions from long methods
   - **simplify**: Simplify complex logic and reduce nesting
   - **remove-duplication**: Identify and eliminate duplicated code

4. **Validation**: Run tests and linting to ensure refactors preserve behavior

5. **Summary Report**: Provide summary of applied refactors and recommendations

## Agent Integration

- **Domain Analysts**: Uses refactoring-analyst and quality-analyst for analysis and refactoring recommendations
- **Pattern**: Analysts identify opportunities, main thread applies safe refactorings

## Parallelization Patterns

**Analysis Phase**: Run simultaneous code quality checks across different dimensions to identify the most impactful quick wins.

**Batch Processing**: Apply multiple safe refactors in a single pass to minimize file system operations.

## Examples

```bash
# Apply refactoring to current directory (no arguments)
/refactor:apply
# $ARGUMENTS would be empty, using defaults

# Extract functions from long methods in src directory
/refactor:apply src/ --type=extract
# $ARGUMENTS = "src/ --type=extract"
# $1 = "src/", $2 = "--type=extract"

# Rename variables for clarity in components
/refactor:apply components/ --type=rename
# $ARGUMENTS = "components/ --type=rename"
# $1 = "components/", $2 = "--type=rename"

# Remove code duplication in lib directory
/refactor:apply lib/ --type=remove-duplication
# $ARGUMENTS = "lib/ --type=remove-duplication"
# $1 = "lib/", $2 = "--type=remove-duplication"

# Simplify complex logic patterns
/refactor:apply --type=simplify --pattern=nested-conditionals
# $ARGUMENTS = "--type=simplify --pattern=nested-conditionals"
