---
description: "Improve code clarity by renaming variables, functions, and identifiers to be more descriptive"
argument-hint: "[path] [--target=<type>] [--convention=<style>] [--suggest-only]"
category: "refactor"
tools: ["Grep", "Edit", "Bash"]
complexity: "simple"
---

# Command: Rename Variables

## Purpose

Improves code clarity by renaming variables, functions, and identifiers to be more descriptive and follow consistent naming conventions.

## Usage

```bash
/refactor:rename-variables [path] [--target=<type>] [--convention=<style>] [--suggest-only]
```

**Arguments**:

- `path` (optional): Specific file or directory to analyze
- `--target` (optional): Focus on specific identifier types (variables, functions, classes, constants)
- `--convention` (optional): Naming convention to apply (camelCase, snake_case, PascalCase)
- `--suggest-only` (optional): Show renaming suggestions without applying changes

## Process

1. **Parse Arguments**: Process user-provided arguments from $ARGUMENTS:
   - `$1` (path): Target file or directory for analysis
   - `$2` (--target): Specific identifier types to focus on
   - `$3` (--convention): Naming convention to apply
   - `$4` (--suggest-only): Preview mode flag

2. **Parallel Naming Analysis**: Use Task() with parameters from $ARGUMENTS:

   ```python
   Task("analyze-clarity", f"Identify unclear {$2 or 'all'} identifiers in {$1 or 'current directory'}"),
   Task("analyze-conventions", f"Check {$3 or 'existing'} naming convention consistency"),
   Task("analyze-context", "Evaluate names against their usage context and purpose")
   ```

3. **Identifier Assessment**: Evaluate names based on $ARGUMENTS target filter:
   - Single-letter variables (except loop counters)
   - Abbreviated or cryptic names
   - Inconsistent naming conventions
   - Names that don't reflect current purpose
   - Misleading or outdated identifiers

4. **Suggestion Generation**: Create names following $ARGUMENTS convention:
   - Follow established project conventions
   - Use domain-specific terminology
   - Maintain consistent patterns across related code
   - Ensure names accurately reflect purpose and type

5. **Safe Renaming**: Apply renames with scope awareness (skip if --suggest-only in $ARGUMENTS):
   - Analyze identifier scope and usage patterns
   - Update all references consistently
   - Avoid naming conflicts
   - Preserve API compatibility where needed

6. **Validation**: Ensure all renames are applied correctly and tests pass

## Agent Integration

- **Specialist Options**: code-writer specialist can be spawned to analyze naming patterns and perform safe, scope-aware identifier renaming

## Parallelization Patterns

**Multi-Scope Analysis**: Simultaneously analyze identifier usage across different scopes (local, class, module, global) to ensure safe renaming.

**Convention Checking**: Run parallel analysis against different naming conventions to identify and resolve inconsistencies.

## Examples

```bash
# Rename unclear variables in current directory (no arguments)
/refactor:rename-variables
# $ARGUMENTS would be empty, using defaults for all identifier types

# Focus on function names only in src
/refactor:rename-variables src/ --target=functions
# $ARGUMENTS = "src/ --target=functions"
# $1 = "src/", $2 = "--target=functions"

# Preview renaming suggestions without applying changes
/refactor:rename-variables --suggest-only
# $ARGUMENTS = "--suggest-only"
# $1 = "--suggest-only"

# Apply specific naming convention to variables
/refactor:rename-variables components/ --target=variables --convention=camelCase
# $ARGUMENTS = "components/ --target=variables --convention=camelCase"
# $1 = "components/", $2 = "--target=variables", $3 = "--convention=camelCase"

# Complete renaming with all options
/refactor:rename-variables lib/ --target=classes --convention=PascalCase --suggest-only
# $ARGUMENTS = "lib/ --target=classes --convention=PascalCase --suggest-only"
# $1 = "lib/", $2 = "--target=classes", $3 = "--convention=PascalCase", $4 = "--suggest-only"
