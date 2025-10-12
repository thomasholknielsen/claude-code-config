---
description: "Orchestrated cleanup workflow that runs multiple cleanup operations in parallel"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch
---

# Command: Run Cleanup Workflow

## Purpose

Executes a comprehensive cleanup workflow by launching parallel domain analyst tasks to improve code quality, remove artifacts, and standardize formatting.

## Usage

```bash
/workflows:run-cleanup-workflow
```

**Arguments**: No arguments required - executes all cleanup commands in predefined sequence

## Process

1. **Launch Parallel Cleanup Tasks**: Invoke quality-analyst and refactoring-analyst to perform cleanup operations concurrently
2. **Synthesize Results**: Collect recommendations from all analysts
3. **Report Completion**: Provide unified cleanup summary

## Agent Integration

**Critical Constraint**: **Subagents provide analysis ONLY - no implementation allowed**

- **Phase 1**: Domain analysts conduct cleanup analysis and return recommendations to main thread
- **Phase 2**: **Main thread synthesizes analyst findings and implements all cleanup operations**
- **Phase 3**: Main thread executes all cleanup fixes and validation

**Primary Agent**: quality-analyst - Analyzes code quality and provides cleanup recommendations (advisory only)
**Supporting Agents**: refactoring-analyst - Provides refactoring and readability recommendations (advisory only)

**Implementation Responsibility**: Main thread executes all cleanup operations using Edit/Bash tools

## Implementation Pattern

The workflow launches parallel analyst tasks using the Task tool:

```python
# Launch parallel cleanup analyses (ANALYSIS ONLY)
Task("quality-analyst: Analyze development artifacts and temporary files, identify formatting rule violations (prettier, eslint)")
Task("refactoring-analyst: Analyze code readability issues, identify naming improvements, structure optimization opportunities, and comment cleanup needs")

# Main thread then implements all cleanup operations based on analyst recommendations
```

## Examples

```bash
# Execute complete cleanup workflow
/workflows:run-cleanup-workflow

# Expected execution:
# 1. Launching parallel cleanup analyses...
# 2. quality-analyst: Analyzing code quality and formatting...
# 3. refactoring-analyst: Identifying readability improvements...
# 4. Cleanup recommendations ready
```

## Integration Points

This workflow command works with:

- **Domain Analysts**: Leverages quality-analyst and refactoring-analyst for comprehensive cleanup analysis
- **Pre-commit workflows**: Often executed before commits to ensure code quality
- **CI/CD pipelines**: Can be integrated into automated quality gates
- **Development workflows**: Regular cleanup during development cycles

## Dependencies

Requires the following domain analysts to be available:

- `quality-analyst` - Code quality analysis and formatting
- `refactoring-analyst` - Readability and structure improvements
