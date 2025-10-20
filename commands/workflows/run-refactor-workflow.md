---
description: "Execute comprehensive refactoring workflow using parallel domain analysis to improve code quality, readability, and maintainability"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch, mcp__sequential-thinking__sequentialthinking
---

# Command: Run Refactor Workflow

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Execute comprehensive refactoring using parallel analysis to improve code quality, readability, and maintainability.

**YOU MUST:**
1. ✓ Establish baseline complexity metrics
2. ✓ Launch refactoring-analyst, code-quality-analyst, architecture-analyst in parallel
3. ✓ Read all context files with refactoring recommendations
4. ✓ Consolidate findings and prioritize by impact
5. ✓ Implement refactoring improvements while preserving behavior
6. ✓ Validate quality improvements through tests and metrics

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Skip behavior-preserving validation
- ✗ Implement without test coverage

---

## IMPLEMENTATION FLOW

### Step 1: Pre-Refactoring Assessment
Baseline complexity metrics, identify high-priority targets

### Step 2: Parallel Analysis
Launch 3 refactoring specialists concurrently

### Step 3: Read Context Files
Collect findings and recommendations

### Step 4: Consolidate & Prioritize
Aggregate findings, prioritize by impact (complexity reduction)

### Step 5: Implement Refactoring
Apply refactoring patterns while preserving behavior

### Step 6: Validate
Run tests and measure quality improvements

---

## Framework Structure (S-Tier Pattern)

### CO-STAR Framework (Orchestration)

**C**ontext: Comprehensive refactoring workflow for improving code quality, readability, and maintainability through code smell detection, complexity reduction, SOLID principles validation, and architectural improvements

**O**bjective: Execute parallel refactoring analysis across 3 domains (code smells, quality metrics, architecture), consolidate findings, implement refactoring improvements while preserving behavior, and validate quality improvements through metrics and tests

**S**tyle: Structured refactoring approach with metric-based assessment (cyclomatic complexity, maintainability index), specific refactoring patterns (Extract Method, Replace Conditional with Polymorphism), and behavior-preserving transformations

**T**one: Constructive, improvement-focused with emphasis on technical debt reduction, maintainability gains, and concrete refactoring techniques - clear before/after metrics

**A**udience: Software engineers, technical leads, architecture teams requiring maintainability improvements with preserved functionality and measurable quality gains

**R**esults: Improved codebase with reduced complexity, eliminated duplication, better structure, passing test suite, and measurable quality metric improvements (complexity reduction, maintainability index increase)

## Analysis Methodology

### 1. Pre-Refactoring Assessment: Baseline complexity metrics (cyclomatic complexity per function), identify high-priority refactoring targets (long methods >50 lines, complex conditionals, code duplication)

### 2. Parallel Refactoring Analysis: Launch 3 domain analysts concurrently (refactoring-analyst for code smells, code-quality-analyst for metrics, architecture-analyst for structural improvements)

### 3. Consolidation & Prioritization: Aggregate findings, prioritize by impact (high complexity reduction, critical duplication removal), plan refactoring sequence

### 4. Implementation: Apply refactoring patterns (Extract Method, Simplify Conditional, Remove Duplication), preserve behavior through incremental changes

### 5. Validation: Run full test suite (all tests must pass), measure complexity reduction, validate SOLID compliance, confirm no functionality regressions

## Explicit Constraints

**IN SCOPE**: Code smell detection (long methods, complex conditionals, duplication), complexity analysis (cyclomatic complexity, maintainability index), SOLID principles validation, design pattern application, structural improvements
**OUT OF SCOPE**: Functional behavior changes (feature additions/modifications), architecture redesigns requiring API changes, performance optimization (performance-analyst), test creation (testing-analyst)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% code smell coverage, Accuracy >90% refactoring safety, Relevance >85% prioritized by impact, Efficiency <45s parallel analysis)

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
  - code-quality-analyst - Complexity analysis, maintainability metrics, SOLID principles validation
  - architecture-analyst - Design pattern recommendations, structural improvements, architectural consistency

## Implementation Steps

### Phase 1: Parallel Refactoring Analysis

```python
# Launch 3 analysts concurrently for comprehensive refactoring assessment
Task("refactoring-analyst: Identify code smells, duplication, long methods, complex conditionals, and refactoring opportunities across the codebase")
Task("code-quality-analyst: Analyze code complexity, detect maintainability issues, validate SOLID principles, and assess technical debt")
Task("architecture-analyst: Review design patterns, identify structural improvements, and recommend architectural enhancements for better modularity")

# Each analyst:
# - Burns tokens on comprehensive refactoring domain analysis
# - Persists lean findings to .agent/context/{session-id}/{agent-name}.md
# - Returns 2-3 sentence summary to main thread
```

### Phase 2: Main Thread Synthesis & Implementation

```python
# Read all analyst artifacts
Read(.agent/context/${session_id}/refactoring-analyst.md)
Read(.agent/context/${session_id}/code-quality-analyst.md)
Read(.agent/context/${session_id}/architecture-analyst.md)

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
→ Task("code-quality-analyst: Analyze complexity and maintainability metrics")
→ Task("architecture-analyst: Review design patterns and structural improvements")

Analysts complete concurrently (significantly faster than sequential execution)

Phase 2: Main Thread Synthesis
→ Consolidate findings from all analysts
→ Apply quick refactoring patterns
→ Simplify complex logic and extract functions
→ Remove code duplication (DRY principles)
→ Rename variables for clarity
→ Implement architectural improvements

Phase 3: Validation
→ All tests passing
→ Complexity substantially reduced
→ Duplication significantly eliminated
→ Maintainability index notably improved
→ No functionality regressions
```

### Integration Points

- **Before Execution**: Works with `/git:branch` to create refactoring branch
- **After Execution**: Integrates with `/git:commit` for structured commit messages
- **Quality Assurance**: Pairs with `/review:code` for post-refactoring validation
- **Documentation**: Coordinates with `/workflows:docs` to reflect structural changes

### Success Criteria

- All refactoring analysis complete with comprehensive findings
- Code quality metrics improve (complexity, duplication, readability)
- Tests continue to pass after all refactoring operations
- No functional behavior changes introduced
- Codebase structure is more maintainable and readable

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

**refactoring-analyst** persists to `.agent/context/refactoring-analysis-{timestamp}.md`:

- Code smell identification and severity
- Duplication detection with locations
- Long method and complex conditional detection
- Refactoring pattern recommendations

**code-quality-analyst** persists to `.agent/context/quality-analysis-{timestamp}.md`:

- Cyclomatic complexity metrics by function
- Maintainability index assessment
- SOLID principles violation detection
- Technical debt quantification

**architecture-analyst** persists to `.agent/context/architecture-analysis-{timestamp}.md`:

- Design pattern opportunities
- Structural improvement recommendations
- Architectural consistency assessment
- Modularity and separation of concerns analysis
