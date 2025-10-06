---
description: "Execute comprehensive refactoring workflow using parallel domain analysis to improve code quality, readability, and maintainability"
allowed-tools: Task
---

# Command: Run Refactor Workflow

## Purpose

Executes a comprehensive refactoring workflow using parallel domain analysis to identify and implement improvements
to code quality, readability, and maintainability.

## Usage

```bash
/workflows:run-refactor-workflow
```

## Process

1. **Parallel Analysis Phase**: Launch 3 domain analysts concurrently for comprehensive refactoring assessment
2. **Synthesis Phase**: Main thread consolidates findings and implements refactoring improvements
3. **Validation Phase**: Verify refactoring maintains behavior and improves quality metrics

## Agent Integration

- **Primary Agent**: refactoring-analyst - Orchestrates parallel refactoring analysis and synthesizes improvements
- **Parallel Domain Analysts** (3 concurrent):
  - refactoring-analyst - Code smell detection, refactoring opportunities, technical debt assessment
  - quality-analyst - Complexity analysis, maintainability metrics, SOLID principles validation
  - architecture-analyst - Design pattern recommendations, structural improvements, architectural consistency

## Implementation Steps

### Phase 1: Parallel Refactoring Analysis

```python
# Launch 3 analysts concurrently for comprehensive refactoring assessment
Task("refactoring-analyst: Identify code smells, duplication, long methods, complex conditionals, and refactoring opportunities across the codebase")
Task("quality-analyst: Analyze code complexity, detect maintainability issues, validate SOLID principles, and assess technical debt")
Task("architecture-analyst: Review design patterns, identify structural improvements, and recommend architectural enhancements for better modularity")

# Each analyst:
# - Burns tokens on comprehensive refactoring domain analysis
# - Persists findings to .artifacts/context/{domain}-analysis-{timestamp}.md
# - Returns 2-3 sentence summary to main thread
```

### Phase 2: Main Thread Synthesis & Implementation

```python
# Read all analyst artifacts
Read(.artifacts/context/refactoring-analysis-*.md)
Read(.artifacts/context/quality-analysis-*.md)
Read(.artifacts/context/architecture-analysis-*.md)

# Based on consolidated findings, implement refactoring:
# 1. Apply quick refactoring patterns (common improvements)
# 2. Simplify complex logic and reduce nested conditionals
# 3. Extract functions from complex code blocks
# 4. Remove code duplication using DRY principles
# 5. Rename variables for improved clarity
# 6. Perform large-scale architectural restructuring
# 7. Apply design patterns for better structure

# Ensure all changes preserve behavior
```

### Phase 3: Validation

```python
# Verify refactoring improvements:
# - Run full test suite (all tests must pass)
# - Measure complexity reduction (cyclomatic complexity)
# - Validate SOLID principles compliance
# - Confirm improved maintainability metrics
# - Ensure no functionality regressions
```

## Examples

### Complete Refactoring Workflow

```bash
/workflows:run-refactor-workflow
```

**Expected workflow execution:**

```text
Phase 1: Parallel Analysis (quick parallel analysis)
→ Task("refactoring-analyst: Identify code smells and refactoring opportunities")
→ Task("quality-analyst: Analyze complexity and maintainability metrics")
→ Task("architecture-analyst: Review design patterns and structural improvements")

Analysts complete concurrently (vs 12-18 minutes sequential)

Phase 2: Main Thread Synthesis
→ Consolidate findings from all analysts
→ Apply quick refactoring patterns
→ Simplify complex logic and extract functions
→ Remove code duplication (DRY principles)
→ Rename variables for clarity
→ Implement architectural improvements

Phase 3: Validation
→ All tests passing
→ Complexity reduced: 15 → 8 (47% improvement)
→ Duplication eliminated: 23 instances → 3
→ Maintainability index improved: 65 → 82
→ No functionality regressions
```

### Integration Points

- **Before Execution**: Works with `/git:branch` to create refactoring branch
- **After Execution**: Integrates with `/git:commit` for structured commit messages
- **Quality Assurance**: Pairs with `/review:code` for post-refactoring validation
- **Documentation**: Coordinates with `/docs:update` to reflect structural changes

### Success Criteria

- All refactoring analysis complete with comprehensive findings
- Code quality metrics improve (complexity, duplication, readability)
- Tests continue to pass after all refactoring operations
- No functional behavior changes introduced
- Codebase structure is more maintainable and readable

## Performance Characteristics

**Traditional Sequential Approach:**

- Refactoring analysis: 5-7 minutes
- Quality analysis: 4-6 minutes
- Architecture review: much faster concurrent execution
- Total: 12-18 minutes

**Parallel Analysis Approach:**

- 3 analysts run concurrently: quick parallel analysis
- Main thread implementation: 4-6 minutes
- Total: 7-10 minutes
- **Performance Gain: 40-50% faster**

## Domain Analyst Outputs

**refactoring-analyst** persists to `.artifacts/context/refactoring-analysis-{timestamp}.md`:

- Code smell identification and severity
- Duplication detection with locations
- Long method and complex conditional detection
- Refactoring pattern recommendations

**quality-analyst** persists to `.artifacts/context/quality-analysis-{timestamp}.md`:

- Cyclomatic complexity metrics by function
- Maintainability index assessment
- SOLID principles violation detection
- Technical debt quantification

**architecture-analyst** persists to `.artifacts/context/architecture-analysis-{timestamp}.md`:

- Design pattern opportunities
- Structural improvement recommendations
- Architectural consistency assessment
- Modularity and separation of concerns analysis
