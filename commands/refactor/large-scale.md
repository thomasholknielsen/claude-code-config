---
description: "Systematic code restructuring with behavior preservation"
argument-hint: "[--target=<pattern>] [--strategy=<approach>] [--validate-each-step] [--backup]"
category: "refactor"
tools: ["Read", "Write", "Edit", "MultiEdit", "Glob", "Grep", "Bash"]
complexity: "moderate"
allowed-tools: Read, Write, Edit, MultiEdit, Glob, Grep, Bash
---

# Command: Large Scale

## Purpose

Performs systematic code restructuring with behavior preservation, including architectural changes, module reorganization, and design pattern implementations.

## Usage

```bash
/refactor:large-scale [--target=<pattern>] [--strategy=<approach>] [--validate-each-step] [--backup]
```

**Arguments**:

- `--target` (optional): Specific refactoring target (architecture, patterns, modules, dependencies)
- `--strategy` (optional): Refactoring approach (incremental, big-bang, feature-branch)
- `--validate-each-step` (optional): Run tests after each major change
- `--backup` (optional): Create git checkpoint before starting

## Process

1. **Parse Arguments**: Process user-provided arguments from $ARGUMENTS:
   - `$1` (--target): Specific refactoring target pattern
   - `$2` (--strategy): Refactoring approach method
   - `$3` (--validate-each-step): Step-by-step validation flag
   - `$4` (--backup): Backup creation flag

2. **Comprehensive Analysis**: Use Task() to evaluate refactoring scope based on $ARGUMENTS:

   ```python
   Task("analyze-architecture", f"Map current architecture focusing on {$1 or 'all areas'}"),
   Task("analyze-dependencies", "Analyze module dependencies and coupling issues"),
   Task("analyze-patterns", "Identify opportunities for design pattern implementations"),
   Task("analyze-testing", f"Assess test coverage and refactoring safety with {$2 or 'incremental'} strategy")
   ```

3. **Refactoring Planning**: Create detailed execution plan based on $ARGUMENTS parameters:
   - Change impact assessment
   - Risk analysis and mitigation strategies
   - Step-by-step transformation sequence
   - Rollback procedures for each phase

4. **Incremental Execution**: Apply changes using strategy from $ARGUMENTS (incremental/big-bang/feature-branch):
   - Extract interfaces and abstract dependencies
   - Restructure modules and move components
   - Implement design patterns and architectural improvements
   - Update import statements and references

5. **Continuous Validation**: Test after each change if --validate-each-step in $ARGUMENTS

6. **Documentation Updates**: Update architecture docs, README files, and code comments

## Agent Integration

- **Specialist Options**: code-writer specialist can be spawned to execute complex structural changes with comprehensive analysis and safety validation

## Parallelization Patterns

**Architecture Analysis**: Simultaneously analyze different architectural aspects (coupling, cohesion, patterns) to build comprehensive refactoring plan.

**Impact Assessment**: Run parallel analysis of change impacts across different system components and test suites.

**Incremental Validation**: Execute test suites in parallel during refactoring to quickly identify any breaking changes.

## Examples

```bash
# Full large-scale refactoring with validation and backup
/refactor:large-scale --validate-each-step --backup
# $ARGUMENTS = "--validate-each-step --backup"
# $1 = "--validate-each-step", $2 = "--backup"

# Focus on architectural improvements
/refactor:large-scale --target=architecture
# $ARGUMENTS = "--target=architecture"
# $1 = "--target=architecture"

# Incremental approach with safety checks
/refactor:large-scale --strategy=incremental --validate-each-step
# $ARGUMENTS = "--strategy=incremental --validate-each-step"
# $1 = "--strategy=incremental", $2 = "--validate-each-step"

# Complete refactoring with all options
/refactor:large-scale --target=patterns --strategy=feature-branch --validate-each-step --backup
# $ARGUMENTS = "--target=patterns --strategy=feature-branch --validate-each-step --backup"
# $1 = "--target=patterns", $2 = "--strategy=feature-branch", $3 = "--validate-each-step", $4 = "--backup"
