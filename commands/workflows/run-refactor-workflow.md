---
description: "Execute comprehensive refactoring workflow by orchestrating atomic refactor commands in optimal sequence"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand"]
complexity: "complex"
allowed-tools: SlashCommand(/refactor:*)
---

# Command: Run Refactor Workflow

## Purpose

Executes a comprehensive refactoring workflow by orchestrating multiple atomic refactor commands in logical sequence to improve code quality,
readability, and maintainability.

## Usage

```bash
/workflows:run-refactor-workflow
```

## Process

1. **Quick Refactoring Pass**: Execute `/refactor:quick` to apply common refactoring patterns
2. **Logic Simplification**: Run `/refactor:simplify-logic` to reduce complex conditionals and nested statements
3. **Function Extraction**: Execute `/refactor:extract-functions` to break down complex code blocks
4. **Duplication Removal**: Run `/refactor:remove-duplication` to eliminate code duplication using DRY principles
5. **Variable Renaming**: Execute `/refactor:rename-variables` to improve identifier clarity
6. **Large-Scale Restructuring**: Run `/refactor:large-scale` for systematic architectural improvements
7. **Validation**: Verify all refactoring changes maintain behavior and improve code quality

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates sequential refactoring operations ensuring consistency and preventing conflicts

## Implementation Steps

### Step 1: Quick Refactoring Foundation

```bash
# Apply common refactoring patterns first
SlashCommand("/refactor:quick")
```

### Step 2: Simplify Complex Logic

```bash
# Reduce conditional complexity and nested statements
SlashCommand("/refactor:simplify-logic")
```

### Step 3: Extract Functions

```bash
# Break down complex code blocks into well-named functions
SlashCommand("/refactor:extract-functions")
```

### Step 4: Remove Code Duplication

```bash
# Apply DRY principles through function extraction
SlashCommand("/refactor:remove-duplication")
```

### Step 5: Improve Naming

```bash
# Enhance code clarity with descriptive identifiers
SlashCommand("/refactor:rename-variables")
```

### Step 6: Large-Scale Restructuring

```bash
# Perform systematic architectural improvements
SlashCommand("/refactor:large-scale")
```

## Examples

### Complete Refactoring Workflow

```bash
/workflows:run-refactor-workflow
```

This command will execute the following sequence:

1. `/refactor:quick` - Apply common patterns
2. `/refactor:simplify-logic` - Reduce complexity
3. `/refactor:extract-functions` - Improve modularity
4. `/refactor:remove-duplication` - Eliminate redundancy
5. `/refactor:rename-variables` - Enhance clarity
6. `/refactor:large-scale` - Architectural improvements

### Integration Points

- **Before Execution**: Works with `/git:branch` to create refactoring branch
- **After Execution**: Integrates with `/git:commit` for structured commit messages
- **Quality Assurance**: Pairs with `/review:code` for post-refactoring validation
- **Documentation**: Coordinates with `/docs:update` to reflect structural changes

### Success Criteria

- All refactor commands execute successfully without conflicts
- Code quality metrics improve (complexity, duplication, readability)
- Tests continue to pass after all refactoring operations
- No functional behavior changes introduced
- Codebase structure is more maintainable and readable
