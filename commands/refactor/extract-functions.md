---
description: "Identify complex code blocks and extract them into well-named functions for better readability"
argument-hint: "[path] [--min-lines=<number>] [--complexity=<threshold>] [--dry-run]"
category: "refactor"
tools: ["Read", "Edit", "Bash"]
complexity: "moderate"
allowed-tools: Read, Edit, Bash
---

# Command: Extract Functions

## Purpose

Identifies complex code blocks and extracts them into well-named functions for better readability and maintainability.

## Usage

```bash
/refactor:extract-functions [path] [--min-lines=<number>] [--complexity=<threshold>] [--dry-run]
```

**Arguments**:

- `path` (optional): Specific file or directory to analyze
- `--min-lines` (optional): Minimum lines for extraction (default: 8)
- `--complexity` (optional): Complexity threshold for extraction
- `--dry-run` (optional): Show extraction candidates without applying changes

## Process

1. **Parse Arguments**: Process user-provided arguments from $ARGUMENTS:
   - `$1` (path): Target file or directory path for analysis
   - `$2` (--min-lines): Minimum line count threshold for extraction
   - `$3` (--complexity): Complexity threshold parameter
   - `$4` (--dry-run): Preview mode flag

2. **Parallel Complexity Analysis**: Use Task() to analyze different complexity metrics with user parameters:

   ```python
   Task("analyze-cyclomatic", f"Calculate cyclomatic complexity for all methods in {$1 or 'current directory'}"),
   Task("analyze-length", f"Identify methods exceeding {$2 or 8} line threshold"),
   Task("analyze-nesting", "Find deeply nested code blocks suitable for extraction")
   ```

3. **Candidate Identification**: Score and prioritize extraction opportunities based on $ARGUMENTS criteria:
   - Long methods with clear logical sections
   - Repeated code patterns across methods
   - Complex conditional or loop structures
   - Code blocks with clear single responsibilities

4. **Function Extraction**: Create new functions with:
   - Descriptive, intention-revealing names
   - Minimal parameter lists
   - Clear return types and documentation
   - Proper error handling patterns

5. **Code Updates**: Replace extracted code with function calls and organize imports

6. **Testing Validation**: Ensure all tests pass and behavior is preserved (skip if --dry-run in $ARGUMENTS)

## Agent Integration

- **Specialist Options**: code-writer specialist can be spawned to analyze code structure and perform safe function extractions with comprehensive testing

## Parallelization Patterns

**Multi-File Analysis**: Simultaneously analyze complexity metrics across all files to identify patterns and prioritize extractions.

**Dependency Analysis**: Run parallel analysis of function dependencies to ensure safe extraction boundaries.

## Examples

```bash
# Extract functions from current directory (no arguments)
/refactor:extract-functions
# $ARGUMENTS would be empty, using defaults

# Find long methods for extraction (path and min-lines arguments)
/refactor:extract-functions src/ --min-lines=15
# $ARGUMENTS = "src/ --min-lines=15"
# $1 = "src/", $2 = "--min-lines=15"

# Preview extraction opportunities (dry-run flag)
/refactor:extract-functions --dry-run
# $ARGUMENTS = "--dry-run"
# $1 = "--dry-run"

# Complex extraction with multiple parameters
/refactor:extract-functions components/ --min-lines=10 --complexity=high --dry-run
# $ARGUMENTS = "components/ --min-lines=10 --complexity=high --dry-run"
# $1 = "components/", $2 = "--min-lines=10", $3 = "--complexity=high", $4 = "--dry-run"
