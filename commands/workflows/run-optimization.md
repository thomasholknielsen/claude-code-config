---
description: "Execute comprehensive optimization workflow using parallel domain analysis to improve performance, reduce bundle size, and enhance user experience"
allowed-tools: Task
---

# Command: Run Optimization

## Purpose

Orchestrates comprehensive optimization workflow using parallel domain analysis to identify and implement performance improvements,
reduce bundle size, and enhance user experience.

## Usage

```bash
/workflows:run-optimization
```

## Process

1. **Parallel Analysis Phase**: Launch 3 domain analysts concurrently for comprehensive optimization assessment
2. **Synthesis Phase**: Main thread consolidates findings and implements optimizations
3. **Validation Phase**: Verify optimizations maintain functionality and improve metrics

## Agent Integration

- **Primary Agent**: performance-analyst - Orchestrates parallel optimization analysis and synthesizes improvements
- **Parallel Domain Analysts** (3 concurrent):
  - performance-analyst - Bottleneck detection, algorithmic efficiency, resource optimization
  - database-analyst - Query optimization, indexing strategies, database performance
  - frontend-analyst - Bundle size analysis, code splitting, lazy loading, asset optimization

## Implementation Steps

### Phase 1: Parallel Optimization Analysis

```python
# Launch 3 analysts concurrently for comprehensive optimization assessment
Task("performance-analyst: Identify performance bottlenecks, memory leaks, algorithmic inefficiencies, and optimization opportunities across the application")
Task("database-analyst: Analyze query performance, identify N+1 queries, review indexing strategies, and assess database connection pooling")
Task("frontend-analyst: Evaluate bundle size, identify unused dependencies, assess code splitting opportunities, and review asset optimization")

# Each analyst:
# - Burns tokens on comprehensive optimization domain analysis
# - Persists findings to .artifacts/context/{domain}-analysis-{timestamp}.md
# - Returns 2-3 sentence summary to main thread
```

### Phase 2: Main Thread Synthesis & Implementation

```python
# Read all analyst artifacts
Read(.artifacts/context/performance-analysis-*.md)
Read(.artifacts/context/database-analysis-*.md)
Read(.artifacts/context/frontend-analysis-*.md)

# Based on consolidated findings, implement optimizations:
# 1. Refactor inefficient algorithms and data structures
# 2. Optimize database queries and add strategic indexes
# 3. Implement code splitting and lazy loading
# 4. Remove unused dependencies and reduce bundle size
# 5. Apply performance-focused refactoring patterns
# 6. Clean up development artifacts and temporary files

# Validate improvements with benchmarks
```

### Phase 3: Validation

```python
# Verify optimizations:
# - Run performance benchmarks (before/after comparison)
# - Validate build size reduction
# - Ensure tests pass
# - Confirm no functionality regressions
```

## Examples

**Basic optimization workflow:**

```bash
/workflows:run-optimization
```

**Expected workflow execution:**

```text
Phase 1: Parallel Analysis (quick parallel analysis)
→ Task("performance-analyst: Analyze application performance bottlenecks")
→ Task("database-analyst: Review query performance and indexing")
→ Task("frontend-analyst: Evaluate bundle size and asset optimization")

Analysts complete concurrently (vs much longer sequential)

Phase 2: Main Thread Synthesis
→ Consolidate findings from all analysts
→ Implement high-priority optimizations
→ Apply refactoring patterns for performance
→ Clean up artifacts and reduce bundle size

Phase 3: Validation
→ Run benchmarks: 40% performance improvement
→ Bundle size reduced: 1.2MB → 0.8MB (33% reduction)
→ All tests passing
→ No functionality regressions
```

**Integration with other commands:**

```bash
# Run optimization before deployment
/workflows:run-optimization
/git:commit "Optimize application performance and bundle size"
```

## Performance Characteristics

**Traditional Sequential Approach:**

- Performance analysis: 6-8 minutes
- Database analysis: 4-6 minutes
- Frontend analysis: 5-7 minutes
- Total: 15-21 minutes

**Parallel Analysis Approach:**

- 3 analysts run concurrently: quick parallel analysis
- Main thread implementation: 2-3 minutes
- Total: 5-7 minutes
- **Performance Gain: 65-70% faster**

## Domain Analyst Outputs

**performance-analyst** persists to `.artifacts/context/performance-analysis-{timestamp}.md`:

- Performance bottleneck locations and severity
- Algorithmic efficiency improvements
- Memory leak detection and resolution strategies
- Resource usage optimization opportunities

**database-analyst** persists to `.artifacts/context/database-analysis-{timestamp}.md`:

- Slow query identification with execution plans
- N+1 query detection and resolution
- Missing index recommendations
- Connection pooling and caching strategies

**frontend-analyst** persists to `.artifacts/context/frontend-analysis-{timestamp}.md`:

- Bundle size analysis and unused dependencies
- Code splitting opportunities
- Lazy loading implementation recommendations
- Asset optimization strategies (images, fonts, etc.)
