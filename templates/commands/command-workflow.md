---
description: "<Orchestrate [action] using parallel domain analyst invocations>"
agent: "<appropriate-domain-analyst>"
allowed-tools: Task
---

# Command: <Workflow Name>

## Purpose

<Single sentence describing the workflow's goal using parallel analysis and consolidated recommendations>

## Usage

```
/workflows:<workflow-name> $ARGUMENTS
```

**Arguments**: <Optional parameters specific to the workflow operation>

## Process

1. **Launch Parallel Analysis Tasks**: Invoke relevant domain analysts to perform specialized analysis concurrently
2. **Parallel Implementation Phase**: Main thread executes multiple independent implementations concurrently
3. **Synthesis & Validation**: Consolidate results and provide unified summary

## Core Parallelization Principle

**MAXIMIZE PARALLELIZATION**: Use concurrent execution for both analysis AND implementation whenever possible

## Implementation Pattern

The workflow leverages maximum parallelization across all phases:

```python
# Phase 1: Parallel Domain Analysis (ANALYSIS ONLY)
Task("<analyst-1>: Analyze [domain] and identify [specific issues/violations/opportunities]")
Task("<analyst-2>: Analyze [domain] and identify [specific issues/violations/opportunities]")
Task("<analyst-3>: Analyze [domain] and identify [specific issues/violations/opportunities]")

# Phase 2: Parallel Implementation (Main thread executes multiple operations concurrently)
# Use multiple tool calls in single message for maximum parallel execution:
Bash("command1")  # Execute linting for language 1
Bash("command2")  # Execute linting for language 2
Bash("command3")  # Execute linting for language 3
Edit("file1", old, new)  # Fix issues in file 1
Edit("file2", old, new)  # Fix issues in file 2

# CRITICAL: Analysts provide recommendations only - main thread implements in parallel
```

**FORBIDDEN Task Patterns** (never use these):
```python
# ❌ WRONG - Asking analysts to implement/fix/apply/execute
Task("analyst: Fix the issues")
Task("analyst: Apply auto-fixes")
Task("analyst: Implement changes")
Task("analyst: Execute linting with auto-fix enabled")

# ✅ CORRECT - Analysis only
Task("analyst: Analyze code and identify linting violations")
Task("analyst: Identify security vulnerabilities and recommend fixes")
Task("analyst: Assess performance bottlenecks and suggest optimizations")
```

**Analyst Selection**:

- Choose analysts based on domain expertise needed (react-analyst, security-analyst, performance-analyst, etc.)
- Typical workflow: 3-6 parallel analysts
- Analysts are advisory (provide recommendations, not implementations)

## Coordination Patterns

**Parallelization Patterns:**

1. **Parallel Analysis**: Task tool enables true concurrent execution of domain analysts
   - Launch 3-6 analysts in parallel for comprehensive multi-perspective analysis
   - Significantly faster execution through concurrent processing
   - Analysts run in isolated contexts with independent token budgets

2. **Parallel Implementation**: Main thread executes multiple independent operations concurrently
   - Use multiple tool calls in single message for maximum parallel execution
   - Parallel file editing, command execution, and validation operations
   - Independent operations can run simultaneously (linting different languages, editing separate files)

3. **Context Elision**: Analysts conduct extensive research, return concise summaries
   - Detailed findings persisted to `.agent/context/{session-id}/{agent-name}.md`
   - Main thread receives focused summaries with actionable insights
   - Main thread reads artifacts as needed for synthesis

4. **Advisory Pattern**: Analysts provide recommendations, not implementations
   - Quality-analyst: Complexity assessment, code smell detection
   - Security-analyst: Vulnerability identification, mitigation strategies
   - Performance-analyst: Bottleneck detection, optimization recommendations

## Parallelization Examples

**Maximum Parallel Implementation**:
```python
# Single message with multiple concurrent operations
Bash("npm run lint:typescript")    # Parallel linting
Bash("python -m ruff check .")     # Parallel linting
Bash("markdownlint *.md")          # Parallel linting
Edit("file1.ts", old_ts, new_ts)   # Parallel file fix
Edit("file2.py", old_py, new_py)   # Parallel file fix
Edit("file3.md", old_md, new_md)   # Parallel file fix
```

**Performance Benefit**: 6 operations execute concurrently vs sequential execution

**SlashCommand Pattern (Special Cases Only):**

Use SlashCommand ONLY for:

- **Git Operations**: Only `/git:*` commands can perform git operations (repository constraint)
- **Final Consolidation**: Optional ONE SlashCommand as absolute final step (no post-processing after)

**Git Workflow Exception Example:**

```
# Git operations MUST use SlashCommand (only /git:* commands can do git ops)
SlashCommand("/git:branch")  # Creates branch
SlashCommand("/git:commit")  # Commits changes
SlashCommand("/git:pr")      # Creates PR
# This violates "ONE SlashCommand" but is required by git constraint
```

## Agent Integration

**Critical Constraint**: **Subagents provide analysis ONLY - no implementation allowed**

- **Phase 1**: Domain analysts conduct analysis and return recommendations to main thread
- **Phase 2**: **Main thread synthesizes analyst findings and implements all changes**
- **Phase 3**: Main thread executes all implementations and validations

**Primary Agent**: <appropriate-domain-analyst> - Coordinates parallel analysis (advisory only)
**Supporting Analysts** (analysis only):
  - <analyst-1> - <Domain expertise> recommendations
  - <analyst-2> - <Domain expertise> recommendations
  - <analyst-n> - <Domain expertise> recommendations

**Implementation Responsibility**: Main thread executes all recommendations using Edit/MultiEdit/Bash tools

## Examples

### Basic Usage

```
/workflows:<workflow-name> $ARGUMENTS
```

**Expected Outcome**: Parallel analysis across N domains (X-Y minutes), consolidated recommendations with prioritized action items.

### Output Structure

```
## <Workflow Name> Summary

**Analysis Scope**: N domain specialists (<list analysts>)
**Analysis Time**: X-Y minutes (parallel execution)

### Key Findings
- <Finding 1 with context>
- <Finding 2 with context>
- <Finding 3 with context>

### Recommendations Roadmap (Prioritized)
1. **Phase 1** (timeframe): <High-priority actions>
2. **Phase 2** (timeframe): <Medium-priority actions>
3. **Phase 3** (timeframe): <Long-term improvements>

**Detailed Reports**:
- `.artifacts/context/<domain-1>-analysis-*.md`
- `.artifacts/context/<domain-2>-analysis-*.md`
- `.artifacts/context/<domain-n>-analysis-*.md`
```

## Integration Points

- **Domain Analysts**: Leverages <list analysts> for comprehensive multi-perspective analysis
- **Workflow Integration**: Often used as part of larger development workflows
- **Artifact Outputs**: Analysts persist detailed findings to `.artifacts/context/` for reference
- **Follow-up**: <Suggested next steps after workflow completes>

## Dependencies

**Domain Analysts**:

- <analyst-1> (coordination and synthesis)
- <analyst-2> (<domain expertise>)
- <analyst-n> (<domain expertise>)

## Performance Notes

- **Analysis Speed**: X-Y% faster than sequential (X-Y min vs X-Y min)
- **Parallel Tasks**: N concurrent analyst invocations
- **Context Management**: Analysts persist detailed findings to artifacts, return concise summaries
