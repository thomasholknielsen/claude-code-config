---
description: "Orchestrated cleanup workflow that runs multiple cleanup operations in parallel"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch, mcp__sequential-thinking__sequentialthinking
---

# Command: Run Cleanup Workflow

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Execute cleanup workflow - remove artifacts, standardize formatting, improve readability, reduce technical debt.

**YOU MUST:**
1. ✓ Identify cleanup targets (temp files, formatting violations, naming issues)
2. ✓ Launch code-quality-analyst and refactoring-analyst in parallel
3. ✓ Read all context files with cleanup recommendations
4. ✓ Consolidate findings and prioritize by impact
5. ✓ Implement cleanup (remove artifacts, fix formatting, improve naming)
6. ✓ Validate improvements (tests still passing, no functionality lost)

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Remove code without understanding impact
- ✗ Skip test validation

---

## EXECUTE THIS NOW

**You MUST execute this cleanup workflow immediately using the Task tool:**

1. Detect session context directory using: `python ~/.claude/scripts/session/session_manager.py context_dir`
2. Identify cleanup targets: temp files, formatting violations, code smells, naming issues
3. Launch code-quality-analyst and refactoring-analyst in parallel concurrently
4. Each analyst analyzes codebase and writes recommendations to `.agent/context/{session-id}/{analyst-name}.md`
5. Collect all recommendations, prioritize by impact
6. Implement cleanup (remove artifacts, fix formatting, improve naming, reduce tech debt)
7. Validate improvements (tests still passing, no functionality lost)

Do NOT just describe what should happen - actively execute this cleanup workflow NOW using the Task tool.

---

## IMPLEMENTATION FLOW

### Step 1: Pre-Cleanup Assessment
Identify targets: temp files, formatting issues, naming problems

### Step 2: Parallel Cleanup Analysis
Launch 2 cleanup specialists concurrently

### Step 3: Read Context Files
Collect cleanup recommendations

### Step 4: Consolidate & Prioritize
Aggregate by impact, prioritize critical artifacts first

### Step 5: Implement Cleanup
Remove artifacts, standardize formatting, improve naming

### Step 6: Validate
Run tests, verify functionality maintained

---

## Framework Structure (S-Tier Pattern)

### CO-STAR Framework (Orchestration)

**C**ontext: Comprehensive cleanup workflow for removing development artifacts, standardizing code formatting, improving readability, and reducing technical debt through parallel code quality and refactoring analysis

**O**bjective: Launch parallel cleanup analyses (code-quality-analyst for formatting/artifacts, refactoring-analyst for readability/structure), synthesize recommendations, implement cleanup operations (remove temp files, fix formatting, improve naming, clean comments), validate improvements

**S**tyle: Automated code hygiene with systematic artifact removal (temp files, logs, caches), formatting standardization (prettier, eslint auto-fix), readability improvements (variable naming, comment cleanup), and incremental cleanup approach

**T**one: Efficient, quality-focused, systematic with emphasis on codebase hygiene - clear cleanup categories, measurable improvements, minimal disruption

**A**udience: Development teams requiring codebase hygiene maintenance, pre-commit cleanup, technical debt reduction without functional changes

**R**esults: Clean codebase with removed artifacts, standardized formatting, improved readability, reduced technical debt, and maintained functionality (all tests passing)

## Analysis Methodology

### 1. Pre-Cleanup Assessment: Identify cleanup targets (temp files, formatting violations, naming issues), baseline code quality metrics

### 2. Parallel Cleanup Analysis: Launch 2 domain analysts concurrently (code-quality-analyst for artifacts/formatting, refactoring-analyst for readability/structure)

### 3. Consolidation: Main thread synthesizes analyst findings, prioritizes cleanup operations by impact (critical artifacts removal, high-priority formatting fixes)

### 4. Implementation: Execute cleanup operations incrementally (remove artifacts, apply formatters, improve naming, clean comments), validate after each operation

### 5. Validation: Verify artifacts removed, formatting standardized, readability improved, all tests passing, no functionality changes

## Explicit Constraints

**IN SCOPE**: Development artifact removal (temp files, logs, caches, build artifacts), code formatting standardization (prettier, eslint, language-specific formatters), readability improvements (naming, comments), technical debt reduction
**OUT OF SCOPE**: Functional code changes (feature modifications), architecture refactoring (structural changes), dependency updates (version bumps), test creation/modification

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% artifact removal, Accuracy >90% formatting compliance, Relevance >85% impactful improvements, Efficiency <30s parallel analysis)

## Purpose

Executes a comprehensive cleanup workflow by launching parallel domain analyst tasks to improve code quality, remove artifacts, and standardize formatting.

## Usage

```bash
/workflows:run-cleanup-workflow
```

**Arguments**: No arguments required - executes all cleanup commands in predefined sequence

## Process

1. **Launch Parallel Cleanup Tasks**: Invoke code-quality-analyst and refactoring-analyst to perform cleanup operations concurrently
2. **Synthesize Results**: Collect recommendations from all analysts
3. **Report Completion**: Provide unified cleanup summary

## Agent Integration

**Critical Constraint**: **Subagents provide analysis ONLY - no implementation allowed**

- **Phase 1**: Domain analysts conduct cleanup analysis and return recommendations to main thread
- **Phase 2**: **Main thread synthesizes analyst findings and implements all cleanup operations**
- **Phase 3**: Main thread executes all cleanup fixes and validation

**Primary Agent**: code-quality-analyst - Analyzes code quality and provides cleanup recommendations (advisory only)
**Supporting Agents**: refactoring-analyst - Provides refactoring and readability recommendations (advisory only)

**Implementation Responsibility**: Main thread executes all cleanup operations using Edit/Bash tools

## Implementation Pattern

The workflow launches parallel analyst tasks using the Task tool:

```python
# Launch parallel cleanup analyses (ANALYSIS ONLY)
Task("code-quality-analyst: Analyze development artifacts and temporary files, identify formatting rule violations (prettier, eslint)")
Task("refactoring-analyst: Analyze code readability issues, identify naming improvements, structure optimization opportunities, and comment cleanup needs")

# Main thread then implements all cleanup operations based on analyst recommendations
```

## Examples

```bash
# Execute complete cleanup workflow
/workflows:run-cleanup-workflow

# Expected execution:
# 1. Launching parallel cleanup analyses...
# 2. code-quality-analyst: Analyzing code quality and formatting...
# 3. refactoring-analyst: Identifying readability improvements...
# 4. Cleanup recommendations ready
```

## Integration Points

This workflow command works with:

- **Domain Analysts**: Leverages code-quality-analyst and refactoring-analyst for comprehensive cleanup analysis
- **Pre-commit workflows**: Often executed before commits to ensure code quality
- **CI/CD pipelines**: Can be integrated into automated quality gates
- **Development workflows**: Regular cleanup during development cycles

## Dependencies

Requires the following domain analysts to be available:

- `code-quality-analyst` - Code quality analysis and formatting
- `refactoring-analyst` - Readability and structure improvements
