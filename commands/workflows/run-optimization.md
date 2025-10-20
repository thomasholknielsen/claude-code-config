---
description: "Execute comprehensive optimization workflow using parallel domain analysis to improve performance, reduce bundle size, and enhance user experience"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch, mcp__sequential-thinking__sequentialthinking
---

# Command: Run Optimization

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Execute comprehensive performance optimization using parallel analysis for backend, database, and frontend.

**YOU MUST:**
1. ✓ Establish baseline performance benchmarks
2. ✓ Launch performance-analyst, database-analyst, frontend-analyst in parallel
3. ✓ Read all context files with optimization recommendations
4. ✓ Consolidate findings and prioritize by impact (highest slowdown first)
5. ✓ Implement optimizations (queries, algorithms, bundle reduction)
6. ✓ Validate with before/after benchmark comparisons

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Implement without baseline metrics
- ✗ Skip performance validation

---

## EXECUTE THIS NOW

**You MUST execute this optimization workflow immediately using the Task tool:**

1. Detect session context directory using: `python ~/.claude/scripts/session/session_manager.py context_dir`
2. Establish baseline performance metrics (response times, bundle size, query times)
3. Launch performance-analyst, database-analyst, frontend-analyst in parallel concurrently
4. Each analyst analyzes codebase and writes recommendations to `.agent/context/{session-id}/{analyst-name}.md`
5. Collect all recommendations, prioritize by performance impact
6. Implement optimizations and validate with before/after benchmark comparisons

Do NOT just describe what should happen - actively execute this optimization workflow NOW using the Task tool.

---

## IMPLEMENTATION FLOW

### Step 1: Baseline Benchmarking
Capture response times, bundle size, memory usage, query times

### Step 2: Parallel Optimization Analysis
Launch 3 performance specialists concurrently

### Step 3: Read Context Files
Collect optimization recommendations

### Step 4: Consolidate & Prioritize
Aggregate by impact, prioritize high-impact optimizations first

### Step 5: Implement Optimizations
Apply query optimizations, refactor algorithms, add indexes, reduce bundles

### Step 6: Validate
Measure improvements, compare before/after benchmarks

---

## Framework Structure (S-Tier Pattern)

### CO-STAR Framework (Orchestration)

**C**ontext: Comprehensive performance optimization workflow covering full-stack performance improvements (backend: algorithmic efficiency, memory leaks; database: query optimization, N+1 detection, indexing; frontend: bundle size reduction, code splitting, lazy loading, asset optimization)

**O**bjective: Execute parallel optimization analysis across 3 domains (application performance, database performance, frontend optimization), consolidate findings, implement optimizations (refactor algorithms, optimize queries, add indexes, apply code splitting, remove unused dependencies), validate with before/after benchmarks

**S**tyle: Metrics-driven optimization with quantifiable improvements (response time reduction, bundle size decrease, memory usage improvement), benchmark comparisons (before/after), and incremental optimization approach

**T**one: Data-focused, improvement-oriented with emphasis on measurable performance gains - clear metrics, specific optimization techniques, concrete results

**A**udience: Performance engineers, full-stack developers requiring end-to-end optimization across backend, database, and frontend layers with measurable performance improvements

**R**esults: Optimized codebase with measurable performance improvements (response time, bundle size, memory usage), passing validation benchmarks, maintained functionality (all tests passing), and documented optimization techniques applied

## Analysis Methodology

### 1. Pre-Optimization Benchmarking: Baseline performance metrics (application response times, database query times, frontend bundle size, memory usage), identify optimization targets (slowest endpoints, largest bundle chunks, most expensive queries)

### 2. Parallel Optimization Analysis: Launch 3 domain analysts concurrently (performance-analyst for bottlenecks/algorithms, database-analyst for queries/indexes, frontend-analyst for bundle/assets)

### 3. Consolidation & Prioritization: Aggregate findings, prioritize by impact (high-impact optimizations first: N+1 queries causing 400% slowdown, unused dependencies adding 2MB to bundle)

### 4. Implementation: Apply optimizations incrementally (refactor inefficient algorithms, add strategic indexes, implement code splitting, remove unused dependencies), validate after each change

### 5. Validation: Run performance benchmarks, compare before/after metrics, ensure tests pass, confirm no functionality regressions, document improvements achieved

## Explicit Constraints

**IN SCOPE**: Performance optimization (algorithmic efficiency, memory leaks, resource usage), database optimization (query performance, N+1 queries, indexing, connection pooling), frontend optimization (bundle size, code splitting, lazy loading, unused dependencies, asset optimization)
**OUT OF SCOPE**: Functional behavior changes (feature modifications), architecture redesigns (structural changes), infrastructure scaling (use infrastructure-cloud-analyst), CDN configuration (use infrastructure-network-analyst)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% optimization opportunities, Accuracy >90% performance improvements, Relevance >85% prioritized by impact, Efficiency <45s parallel analysis)

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
# - Persists lean findings to .agent/context/{session-id}/{agent-name}.md
# - Returns 2-3 sentence summary to main thread
```

### Phase 2: Main Thread Synthesis & Implementation

```python
# Read all analyst artifacts
Read(.agent/context/${session_id}/performance-analyst.md)
Read(.agent/context/${session_id}/database-analyst.md)
Read(.agent/context/${session_id}/frontend-analyst.md)

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

Analysts complete concurrently (significantly faster than sequential execution)

Phase 2: Main Thread Synthesis
→ Consolidate findings from all analysts
→ Implement high-priority optimizations
→ Apply refactoring patterns for performance
→ Clean up artifacts and reduce bundle size

Phase 3: Validation
→ Run benchmarks showing substantial performance improvement
→ Bundle size significantly reduced
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

**Sequential Approach:**

- Analysts execute one after another
- Total time scales linearly with analyst count
- Single-threaded execution pattern

**Parallel Approach:**

- Multiple analysts run simultaneously using Task tool
- Execution time approaches slowest analyst (Amdahl's Law)
- **Performance Gain: Significantly faster through concurrent execution**

**Note**: Actual performance depends on system resources, network latency for MCP tools, and analysis complexity.

## Domain Analyst Outputs

**performance-analyst** persists to `.agent/context/performance-analysis-{timestamp}.md`:

- Performance bottleneck locations and severity
- Algorithmic efficiency improvements
- Memory leak detection and resolution strategies
- Resource usage optimization opportunities

**database-analyst** persists to `.agent/context/database-analysis-{timestamp}.md`:

- Slow query identification with execution plans
- N+1 query detection and resolution
- Missing index recommendations
- Connection pooling and caching strategies

**frontend-analyst** persists to `.agent/context/frontend-analysis-{timestamp}.md`:

- Bundle size analysis and unused dependencies
- Code splitting opportunities
- Lazy loading implementation recommendations
- Asset optimization strategies (images, fonts, etc.)
