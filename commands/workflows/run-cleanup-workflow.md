---
description: "Orchestrated cleanup workflow that runs multiple cleanup commands in sequence"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand"]
complexity: "complex"
---

# Command: Run Cleanup Workflow

## Purpose

Executes a comprehensive cleanup workflow by orchestrating multiple atomic cleanup commands in logical sequence to improve code quality, remove
artifacts, and standardize formatting.

## Usage

```bash
/workflows:run-cleanup-workflow
```

**Arguments**: No arguments required - executes all cleanup commands in predefined sequence

## Process

1. **Clean Development Artifacts**: Execute `/clean:development-artifacts` to remove temporary files, build artifacts, and development debris
2. **Apply Style Rules**: Execute `/clean:apply-style-rules` to run automated formatters (prettier, eslint --fix, etc.)
3. **Improve Code Readability**: Execute `/clean:improve-readability` to enhance naming, structure, and manual code beautification
4. **Clean Code Comments**: Execute `/clean:code-comments` to remove redundant comments while preserving valuable documentation
5. **Validate Results**: Verify all cleanup operations completed successfully and report final status

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates sequential execution of atomic cleanup commands ensuring proper order and dependencies

## Implementation Pattern

The orchestrator executes each cleanup command sequentially using SlashCommand:

```python
# Step 1: Clean development artifacts
SlashCommand("/clean:development-artifacts")

# Step 2: Apply automated style rules
SlashCommand("/clean:apply-style-rules")

# Step 3: Manual readability improvements
SlashCommand("/clean:improve-readability")

# Step 4: Clean up comments
SlashCommand("/clean:code-comments")
```

## Examples

```bash
# Execute complete cleanup workflow
/workflows:run-cleanup-workflow

# Expected sequence:
# 1. Removing temporary files and build artifacts...
# 2. Running prettier, eslint --fix, and other formatters...
# 3. Improving variable names and code structure...
# 4. Cleaning redundant comments...
# 5. Cleanup workflow completed successfully
```

## Integration Points

This workflow command works with:

- **Individual cleanup commands**: Can be run separately if only specific cleanup is needed
- **Pre-commit workflows**: Often executed before commits to ensure code quality
- **CI/CD pipelines**: Can be integrated into automated quality gates
- **Development workflows**: Regular cleanup during development cycles

## Dependencies

Requires the following atomic cleanup commands to be available:

- `/clean:development-artifacts`
- `/clean:apply-style-rules`
- `/clean:improve-readability`
- `/clean:code-comments`
