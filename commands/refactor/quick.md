---
description: "Rapidly apply common refactoring patterns for daily code improvements"
argument-hint: "[path] [--pattern=<pattern>] [--type=<refactor_type>]"
category: "refactor"
tools: ["Read", "Edit", "Bash"]
complexity: "simple"
---

# Command: Quick

## Purpose

Rapidly applies common refactoring patterns like variable renaming, method extraction, and code organization for daily code improvements.

## Usage

```bash
/refactor:quick [path] [--pattern=<pattern>] [--type=<refactor_type>]
```

**Arguments**:

- `path` (optional): Specific file or directory to refactor
- `--pattern` (optional): Focus on specific code patterns (e.g., long-methods, duplicate-code)
- `--type` (optional): Refactor type (rename, extract, simplify, organize)

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

3. **Apply Quick Refactors**: Execute refactoring patterns based on $ARGUMENTS type filter:
   - Variable/method renaming for clarity
   - Extract small, focused functions from long methods
   - Organize imports and remove unused code
   - Apply consistent formatting patterns

4. **Validation**: Run tests and linting to ensure refactors preserve behavior

5. **Summary Report**: Provide summary of applied refactors and recommendations

## Agent Integration

- **Specialist Options**: code-writer specialist can be spawned to execute safe, atomic refactoring operations with immediate validation

## Parallelization Patterns

**Analysis Phase**: Run simultaneous code quality checks across different dimensions to identify the most impactful quick wins.

**Batch Processing**: Apply multiple safe refactors in a single pass to minimize file system operations.

## Examples

```bash
# Quick refactor current directory (no arguments)
/refactor:quick
# $ARGUMENTS would be empty, using defaults

# Focus on method complexity in src directory
/refactor:quick src/ --pattern=long-methods
# $ARGUMENTS = "src/ --pattern=long-methods"
# $1 = "src/", $2 = "--pattern=long-methods"

# Rename variables for clarity in components
/refactor:quick components/ --type=rename
# $ARGUMENTS = "components/ --type=rename"
# $1 = "components/", $2 = "--type=rename"

# Complex quick refactor with all parameters
/refactor:quick lib/ --pattern=duplicate-code --type=extract
# $ARGUMENTS = "lib/ --pattern=duplicate-code --type=extract"
# $1 = "lib/", $2 = "--pattern=duplicate-code", $3 = "--type=extract"
