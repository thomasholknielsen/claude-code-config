---
description: "Identify and eliminate code duplication by applying DRY principles through function extraction"
argument-hint: "[path] [--min-similarity=<percentage>] [--min-lines=<number>] [--extract-to=<location>]"
category: "refactor"
tools: ["Grep", "Read", "Edit"]
complexity: "moderate"
---

# Command: Remove Duplication

## Purpose

Identifies and eliminates code duplication by applying DRY principles through function extraction, shared utilities, and pattern consolidation.

## Usage

```bash
/refactor:remove-duplication [path] [--min-similarity=<percentage>] [--min-lines=<number>] [--extract-to=<location>]
```

**Arguments**:

- `path` (optional): Specific file or directory to analyze
- `--min-similarity` (optional): Minimum similarity percentage for duplication detection (default: 80%)
- `--min-lines` (optional): Minimum lines for duplication consideration (default: 5)
- `--extract-to` (optional): Target location for extracted shared code (utils/, shared/, common/)

## Process

1. **Parse Arguments**: Process user-provided arguments from $ARGUMENTS:
   - `$1` (path): Target file or directory for duplication analysis
   - `$2` (--min-similarity): Minimum similarity percentage threshold
   - `$3` (--min-lines): Minimum line count for duplication consideration
   - `$4` (--extract-to): Target location for extracted shared code

2. **Parallel Duplication Detection**: Use Task() with parameters from $ARGUMENTS:

   ```python
   Task("detect-exact-duplicates", f"Find identical code blocks in {$1 or 'current directory'}"),
   Task("detect-similar-patterns", f"Identify code with {$2 or '80%'} similarity"),
   Task("detect-logic-duplication", f"Find duplicated logic with minimum {$3 or '5'} lines")
   ```

3. **Duplication Analysis**: Categorize and prioritize found duplications using $ARGUMENTS criteria:
   - Exact code duplicates (highest priority)
   - Similar patterns with minor variations
   - Duplicated logic with different implementations
   - Repeated configuration or data structures

4. **Extraction Strategy**: Determine consolidation approach based on --extract-to from $ARGUMENTS:
   - Extract common functions for identical code
   - Create configurable functions for similar patterns
   - Establish shared utilities for repeated logic
   - Consolidate configuration into shared files

5. **Code Refactoring**: Apply DRY principles safely:
   - Extract shared functions with clear interfaces
   - Update all usage sites to use shared code
   - Maintain backward compatibility during transition
   - Organize extracted code in logical modules

6. **Validation**: Ensure functionality is preserved and duplication is eliminated

## Agent Integration

- **Specialist Options**: code-writer specialist can be spawned to analyze duplication patterns and safely extract shared code with comprehensive testing

## Parallelization Patterns

**Multi-Pattern Detection**: Simultaneously scan for different types of duplication to build comprehensive elimination strategy.

**Cross-File Analysis**: Run parallel analysis across entire codebase to identify duplication patterns that span multiple modules.

## Examples

```bash
# Remove duplication from current directory (no arguments)
/refactor:remove-duplication
# $ARGUMENTS would be empty, using defaults (80% similarity, 5 lines minimum)

# Focus on high-similarity duplicates in src
/refactor:remove-duplication src/ --min-similarity=90%
# $ARGUMENTS = "src/ --min-similarity=90%"
# $1 = "src/", $2 = "--min-similarity=90%"

# Extract shared code to utilities
/refactor:remove-duplication --extract-to=utils/
# $ARGUMENTS = "--extract-to=utils/"
# $1 = "--extract-to=utils/"

# Complete duplication removal with all parameters
/refactor:remove-duplication lib/ --min-similarity=85% --min-lines=8 --extract-to=shared/
# $ARGUMENTS = "lib/ --min-similarity=85% --min-lines=8 --extract-to=shared/"
# $1 = "lib/", $2 = "--min-similarity=85%", $3 = "--min-lines=8", $4 = "--extract-to=shared/"
