---
description: "Review code with context-appropriate depth and spec-kit integration"
argument-hint: "[file_pattern] [--focus=area] [--fix]"
category: "review"
tools: ["Read", "Grep", "Bash"]
complexity: "moderate"
allowed-tools: Read, Grep, Bash
---

# Command: Review Code

## Purpose

Performs comprehensive code quality analysis with parallel assessment of multiple quality dimensions
including syntax, patterns, maintainability, and performance.

## Usage

```bash
/review:code $ARGUMENTS
```

**Arguments**:

- `$1` (file_pattern): Specific files or glob patterns to review (optional, default: entire project)
- `$2` (--focus): Focus on specific areas (quality|performance|maintainability|patterns) (optional)
- `$3` (--fix): Automatically apply safe fixes for identified issues (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "src/components/**/*.js --focus=performance"` - Performance review of components
- `$ARGUMENTS = "--fix"` - Project-wide code review with auto-fixes
- `$ARGUMENTS = "auth/*.ts --focus=security"` - Security-focused review of auth modules

## Process

1. **Parse Review Scope**: Extract file patterns and focus areas from $ARGUMENTS
2. **Discovery Phase**: Identify codebase structure and review scope
3. **Parallel Analysis**: Launch concurrent quality assessments across multiple dimensions
4. **Synthesis**: Aggregate findings and prioritize issues by severity
5. **Remediation**: Apply fixes or generate actionable recommendations
6. **Documentation**: Update code quality metrics and create improvement roadmap

## Parallelization Patterns

**Multi-Dimensional Analysis**: Review spawns parallel tasks for comprehensive assessment:

```python
# Parallel quality analysis
Task("Analyze code syntax, style, and linting violations across all source files")
Task("Evaluate code complexity, cyclomatic complexity, and maintainability metrics")
Task("Assess design patterns, SOLID principles, and architectural compliance")
Task("Review error handling, logging, and debugging capabilities")
Task("Analyze performance patterns, memory usage, and optimization opportunities")
```

**Technology-Specific Reviews**: Framework-aware parallel analysis:

```python
# React/Frontend specific
Task("Review React component patterns, hooks usage, and state management")
Task("Analyze bundle size, code splitting, and loading performance")
Task("Evaluate accessibility compliance and semantic HTML usage")

# Backend/API specific
Task("Review API design patterns, endpoint structure, and response handling")
Task("Analyze database queries, connection handling, and transaction management")
Task("Evaluate security patterns, input validation, and authentication flows")
```

**File-Level Parallel Processing**: Concurrent file analysis for large codebases:

```python
# Parallel file processing
Task("Review critical business logic files for correctness and edge cases")
Task("Analyze configuration files for security and environment management")
Task("Evaluate test files for coverage, quality, and maintenance needs")
Task("Review build and deployment scripts for reliability and security")
```

## Agent Integration

- **Specialist Options**: reviewer specialist can be spawned to coordinate parallel code analysis and synthesize quality findings
- **Coordination**: Spawns concurrent analysis tasks for different quality dimensions
- **Integration**: Works with `code-writer` for automated fixes, `test-writer` for coverage gaps

## Examples

```bash
# Comprehensive project review
/review:code

# Focus on specific component
/review:code $ARGUMENTS
# where $ARGUMENTS = "src/components/Auth* --focus=security"

# Review with automatic fixes
/review:code $ARGUMENTS
# where $ARGUMENTS = "--fix"

# Performance-focused review
/review:code $ARGUMENTS
# where $ARGUMENTS = "--focus=performance"
