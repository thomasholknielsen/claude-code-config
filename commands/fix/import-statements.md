---
description: "Systematically fix import statements broken by file moves or renames"
argument-hint: "[path] [--scope=<area>] [--strategy=<approach>] [--dry-run]"
category: "fix"
tools: ["Grep", "Edit", "Bash", "Read"]
complexity: "moderate"
---

# Command: Import Statements

## Purpose

Systematically fixes import statements broken by file moves, renames, or restructuring, resolving module resolution errors.

## Usage

```bash
/fix:import-statements [path] [--scope=<area>] [--strategy=<approach>] [--dry-run]
```

**Arguments**:

- `path` (optional): Specific file or directory to fix
- `--scope` (optional): Fix scope (relative, absolute, all)
- `--strategy` (optional): Fixing approach (automatic, interactive, conservative)
- `--dry-run` (optional): Show proposed fixes without applying changes

**$ARGUMENTS Usage**:
The command processes arguments through the $ARGUMENTS placeholder:

- `$ARGUMENTS` - Contains all user-provided arguments as a single string
- `$1` - First positional argument (target path)
- `$2` - Second positional argument (if provided)
- Named flags are parsed from $ARGUMENTS for scope, strategy, and dry-run options

## Process

1. **Argument Processing & Import Analysis**: Parse $ARGUMENTS and use Task() to comprehensively analyze import issues:

   ```python
   # Parse arguments from $ARGUMENTS
   target_path = $1 if $1 else "./"
   scope = parse_flag("--scope", $ARGUMENTS) or "all"
   strategy = parse_flag("--strategy", $ARGUMENTS) or "automatic"
   dry_run = "--dry-run" in $ARGUMENTS

   # Parallel import analysis tasks
   Task("scan-broken-imports", f"Identify import resolution errors in {target_path}"),
   Task("map-file-locations", f"Build file structure and available modules for {scope} scope"),
   Task("analyze-dependencies", f"Map import relationships and dependency chains")
   ```

2. **Issue Classification**: Categorize different types of import problems within specified scope:
   - Missing files due to moves or deletions (focus on $1 path if provided)
   - Incorrect relative paths after restructuring (based on --scope setting)
   - Outdated absolute import paths (when --scope=absolute)
   - Circular import dependencies (when --scope=all)
   - Missing package initialization files

3. **Resolution Strategy**: Determine best fix approach based on $ARGUMENTS:
   - **Automatic Fix**: Update paths for clear file moves (--strategy=automatic)
   - **Interactive Fix**: Prompt for ambiguous cases (--strategy=interactive)
   - **Conservative Fix**: Minimal changes, preserve existing structure (--strategy=conservative)
   - **Comprehensive Fix**: Include cleanup and optimization (default strategy)
   - **Dry Run Mode**: Show all proposed fixes without applying (--dry-run)

4. **Import Correction**: Apply fixes systematically based on parsed arguments:
   - Update relative paths based on current file structure (within $1 path if specified)
   - Convert between relative and absolute imports based on --scope setting
   - Resolve circular dependencies through refactoring (unless --strategy=conservative)
   - Add missing `__init__.py` files where needed
   - Remove unused imports and organize import blocks (unless --dry-run)
   - Preview changes only if --dry-run flag is set

5. **Validation**: Ensure all imports resolve correctly:
   - Test import resolution in Python/Node.js environment
   - Run linting tools to verify import correctness
   - Check for any remaining broken imports

## Agent Integration

- **Primary Specialist**: bug-fixer - A specialized agent that can be spawned for analyzing import structures and systematically resolving
  module resolution issues

## Parallelization Patterns

**Multi-File Scanning**: Simultaneously scan all files for import issues to build comprehensive fix plan.

**Dependency Mapping**: Run parallel analysis of import relationships to identify and resolve complex dependency issues.

## Examples

```bash
# Fix all import issues in current directory (default: $1="./", scope="all")
/fix:import-statements

# Fix specific directory ($1="src/")
/fix:import-statements src/

# Preview fixes before applying ($1="src/", --dry-run flag)
/fix:import-statements src/ --dry-run

# Conservative fixes for critical modules ($1="core/", --strategy=conservative)
/fix:import-statements core/ --strategy=conservative

# Interactive fixes with relative scope
/fix:import-statements components/ --scope=relative --strategy=interactive

# Comprehensive absolute import fixes with preview
/fix:import-statements --scope=absolute --dry-run
```

**$ARGUMENTS Processing Examples**:

- `src/` → $1="src/", $ARGUMENTS="src/"
- `--scope=relative --dry-run` → $ARGUMENTS="--scope=relative --dry-run"
- `core/ --strategy=conservative` → $1="core/", --strategy=conservative parsed
- `components/ --scope=relative --strategy=interactive` → $1="components/", multiple flags parsed
