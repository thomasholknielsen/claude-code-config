---
description: "<Orchestrate [action] using parallel domain analyst invocations>"
agent: "<appropriate-domain-analyst>"
allowed-tools: Task
---

# Command: Run <Workflow Name>

## Purpose

<Single sentence describing the workflow's goal using parallel analysis and consolidated recommendations>

## Usage

```bash
/workflows:<workflow-name> $ARGUMENTS
```

**Arguments**: <Optional parameters specific to the workflow operation>

## Process

1. **Launch Parallel Analysis Tasks**: Invoke relevant domain analysts to perform specialized analysis concurrently
2. **Synthesis Phase**: Collect recommendations from all analysts
3. **Report Completion**: Provide unified summary with prioritized action items

## Implementation Pattern

The workflow launches parallel analyst tasks using the Task tool:

```python
# Phase 1: Parallel Domain Analysis
Task("<analyst-1>: Specific analysis instructions for this domain")
Task("<analyst-2>: Specific analysis instructions for this domain")
Task("<analyst-3>: Specific analysis instructions for this domain")

# Phase 2: Main thread synthesizes all findings and provides consolidated recommendations
```

**Analyst Selection**:

- Choose analysts based on domain expertise needed (react-analyst, security-analyst, performance-analyst, etc.)
- Typical workflow: 3-6 parallel analysts
- Analysts are advisory (provide recommendations, not implementations)

## Coordination Patterns

**Task Tool Pattern (Recommended):**

1. **Parallel Execution**: Task tool enables true concurrent execution of domain analysts
   - Launch 3-6 analysts in parallel for comprehensive multi-perspective analysis
   - 70-85% performance improvement over sequential patterns
   - Analysts run in isolated contexts with independent token budgets

2. **Context Elision**: Analysts conduct extensive research, return concise summaries
   - Detailed findings persisted to `.artifacts/context/{domain}-analysis-*.md`
   - Main thread receives 2-3 sentence summaries (76% signal vs 91% noise)
   - Main thread reads artifacts as needed for synthesis

3. **Advisory Pattern**: Analysts provide recommendations, not implementations
   - Quality-analyst: Complexity assessment, code smell detection
   - Security-analyst: Vulnerability identification, mitigation strategies
   - Performance-analyst: Bottleneck detection, optimization recommendations

**SlashCommand Pattern (Special Cases Only):**

Use SlashCommand ONLY for:
- **Git Operations**: Only `/git:*` commands can perform git operations (repository constraint)
- **Final Consolidation**: Optional ONE SlashCommand as absolute final step (no post-processing after)

**Git Workflow Exception Example:**

```python
# Git operations MUST use SlashCommand (only /git:* commands can do git ops)
SlashCommand("/git:branch")  # Creates branch
SlashCommand("/git:commit")  # Commits changes
SlashCommand("/git:pr")      # Creates PR
# This violates "ONE SlashCommand" but is required by git constraint
```

## Agent Integration

- **Primary Agent**: <appropriate-domain-analyst> - Coordinates parallel analysis and synthesizes findings
- **Supporting Analysts**:
  - <analyst-1> - <Domain expertise>
  - <analyst-2> - <Domain expertise>
  - <analyst-n> - <Domain expertise>

## Examples

### Basic Usage

```bash
/workflows:<workflow-name> $ARGUMENTS
```

**Expected Outcome**: Parallel analysis across N domains (X-Y minutes), consolidated recommendations with prioritized action items.

### Output Structure

```markdown
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
