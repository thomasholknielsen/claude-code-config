---
description: "Simplify complex conditionals, nested statements, and convoluted logic for better readability"
argument-hint: "[path] [--max-complexity=<number>] [--max-nesting=<level>] [--focus=<area>]"
category: "refactor"
tools: ["Read", "Edit", "Bash"]
complexity: "moderate"
allowed-tools: Read, Edit, Bash
---

# Command: Simplify Logic

## Purpose

Simplifies complex conditionals, nested statements, and convoluted logic for better readability and maintainability.

## Usage

```bash
/refactor:simplify-logic [path] [--max-complexity=<number>] [--max-nesting=<level>] [--focus=<area>]
```

**Arguments**:

- `path` (optional): Specific file or directory to analyze
- `--max-complexity` (optional): Maximum cyclomatic complexity threshold (default: 10)
- `--max-nesting` (optional): Maximum nesting level to allow (default: 4)
- `--focus` (optional): Focus area (conditionals, loops, expressions, boolean-logic)

## Process

1. **Parse Arguments**: Process user-provided arguments from $ARGUMENTS:
   - `$1` (path): Target file or directory for analysis
   - `$2` (--max-complexity): Maximum cyclomatic complexity threshold
   - `$3` (--max-nesting): Maximum nesting level to allow
   - `$4` (--focus): Focus area for simplification

2. **Parallel Complexity Analysis**: Use Task() with parameters from $ARGUMENTS:

   ```python
   Task("analyze-conditionals", f"Find complex conditionals in {$1 or 'current directory'}"),
   Task("analyze-nesting", f"Identify code exceeding {$3 or '4'} nesting levels"),
   Task("analyze-boolean-logic", f"Focus on {$4 or 'all'} complex logic patterns")
   ```

3. **Logic Assessment**: Categorize complexity issues based on $ARGUMENTS thresholds:
   - Long if/else chains that could use polymorphism
   - Deeply nested loops and conditionals
   - Complex boolean expressions
   - Repeated conditional patterns
   - Mixed abstraction levels within methods

4. **Simplification Strategies**: Apply patterns focused on $ARGUMENTS area:
   - Extract guard clauses to reduce nesting
   - Replace conditional chains with polymorphism or strategy pattern
   - Break complex boolean expressions into named variables
   - Extract nested logic into smaller methods
   - Use early returns to flatten control flow

5. **Logic Restructuring**: Apply transformations systematically:
   - Invert conditionals to use guard clauses
   - Extract complex expressions into well-named variables
   - Replace nested loops with functional approaches where appropriate
   - Consolidate similar conditional branches

6. **Validation**: Ensure logical equivalence and improved readability

## Agent Integration

- **Specialist Options**: code-writer specialist can be spawned to analyze complex logic patterns and apply systematic simplification with behavior preservation

## Parallelization Patterns

**Multi-Pattern Detection**: Simultaneously analyze different complexity patterns (nesting, conditionals, expressions) to prioritize simplification efforts.

**Refactoring Validation**: Run parallel test execution during logic simplification to ensure behavior preservation.

## Examples

```bash
# Simplify complex logic in current directory (no arguments)
/refactor:simplify-logic
# $ARGUMENTS would be empty, using defaults (complexity=10, nesting=4)

# Focus on high-complexity methods in src
/refactor:simplify-logic src/ --max-complexity=8
# $ARGUMENTS = "src/ --max-complexity=8"
# $1 = "src/", $2 = "--max-complexity=8"

# Target nested conditionals specifically
/refactor:simplify-logic --focus=conditionals
# $ARGUMENTS = "--focus=conditionals"
# $1 = "--focus=conditionals"

# Complete logic simplification with all parameters
/refactor:simplify-logic components/ --max-complexity=6 --max-nesting=3 --focus=boolean-logic
# $ARGUMENTS = "components/ --max-complexity=6 --max-nesting=3 --focus=boolean-logic"
# $1 = "components/", $2 = "--max-complexity=6", $3 = "--max-nesting=3", $4 = "--focus=boolean-logic"
