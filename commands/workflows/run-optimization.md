---
description: "Execute comprehensive optimization workflow by orchestrating atomic slash commands to improve performance, reduce bundle size, and enhance user experience"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand"]
complexity: "complex"
allowed-tools: SlashCommand(/analyze:*), SlashCommand(/refactor:*)
---

# Command: Run Optimization

## Purpose

Orchestrates comprehensive optimization workflow by executing atomic slash commands sequentially to improve performance, reduce bundle size, and
enhance user experience.

## Usage

```bash
/workflows:run-optimization
```

## Process

1. **Performance Analysis**: Execute `/analyze:performance` to identify bottlenecks and optimization opportunities
2. **Dependency Analysis**: Execute `/analyze:dependencies` to identify outdated or inefficient packages
3. **Code Simplification**: Execute `/refactor:simplify-logic` to reduce complexity and improve performance
4. **Readability Improvements**: Execute `/clean:improve-readability` to optimize code structure
5. **Style Optimization**: Execute `/clean:apply-style-rules` to ensure consistent formatting
6. **Development Artifacts Cleanup**: Execute `/clean:development-artifacts` to remove unnecessary files
7. **Validation**: Verify optimizations through build and test execution

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates sequential execution of optimization commands with validation between steps

## Implementation Steps

**Step 1: Performance Analysis**

```bash
SlashCommand("/analyze:performance")
```

Identifies performance bottlenecks, memory usage patterns, and optimization opportunities.

**Step 2: Dependency Analysis**

```bash
SlashCommand("/analyze:dependencies")
```

Evaluates package efficiency, identifies outdated dependencies, and security vulnerabilities.

**Step 3: Logic Simplification**

```bash
SlashCommand("/refactor:simplify-logic")
```

Reduces code complexity, eliminates nested conditionals, and improves algorithmic efficiency.

**Step 4: Code Readability**

```bash
SlashCommand("/clean:improve-readability")
```

Optimizes variable names, function structure, and code organization for better performance.

**Step 5: Style Consistency**

```bash
SlashCommand("/clean:apply-style-rules")
```

Applies automated formatting to reduce parsing overhead and improve maintainability.

**Step 6: Cleanup Artifacts**

```bash
SlashCommand("/clean:development-artifacts")
```

Removes temporary files, unused assets, and development-only code that impacts bundle size.

## Examples

**Basic optimization workflow:**

```bash
/workflows:run-optimization
```

**Expected workflow execution:**

1. Analyzes performance bottlenecks across the application
2. Reviews dependencies for optimization opportunities
3. Simplifies complex logic patterns for better performance
4. Improves code readability and structure
5. Applies consistent formatting and style rules
6. Cleans up development artifacts and unused files
7. Validates all changes maintain functionality

**Integration with other commands:**

```bash
# Run optimization before deployment
/workflows:run-optimization
/git:commit "Optimize application performance and bundle size"
```
