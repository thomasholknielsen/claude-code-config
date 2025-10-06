# Command Workflow Base Template

**Purpose**: Shared template for workflow commands that execute parallel domain analyst analysis.

## Standard Workflow Structure

All workflow commands follow this three-phase pattern:

### Phase 1: Parallel Analysis

Launch multiple domain analysts concurrently using Task tool. Each analyst:
- Conducts comprehensive domain-specific analysis
- Persists findings to `.agent/context/{domain}-analysis-{timestamp}.md`
- Returns 2-3 sentence summary to main thread

**Pattern**:
```python
# Launch N analysts concurrently
Task("analyst-1: Specific analysis task description")
Task("analyst-2: Specific analysis task description")
Task("analyst-3: Specific analysis task description")
```

### Phase 2: Main Thread Synthesis

Main thread consolidates findings and implements improvements:

**Pattern**:
```python
# Read all analyst artifacts
Read(.agent/context/analyst-1-analysis-*.md)
Read(.agent/context/analyst-2-analysis-*.md)
Read(.agent/context/analyst-3-analysis-*.md)

# Based on consolidated findings:
# 1. [Specific implementation steps for this workflow]
# 2. [Additional steps]
# 3. [Validation]
```

### Phase 3: Validation/Action

Verify improvements or take final actions:

**Pattern**:
```python
# Workflow-specific validation:
# - Run tests
# - Verify improvements
# - Generate reports
# - Create artifacts
```

## Common Workflow Elements

### Performance Characteristics Section

**Standard Text**:

```markdown
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
```

### Domain Analyst Outputs Section

**Pattern**:

```markdown
## Domain Analyst Outputs

**{analyst-name}** persists to `.agent/context/{artifact-pattern}`:
- Finding type 1
- Finding type 2
- Finding type 3

**{analyst-name-2}** persists to `.agent/context/{artifact-pattern-2}`:
- Finding type 1
- Finding type 2
```

### Agent Integration Section

**Pattern**:

```markdown
## Agent Integration

- **Primary Agent**: {primary-analyst} - Orchestrates parallel analysis and synthesizes findings
- **Parallel Domain Analysts** ({N} concurrent):
  - {analyst-1} - {description}
  - {analyst-2} - {description}
  - {analyst-3} - {description}
```

### Example Section

**Pattern**:

```markdown
## Examples

### Complete {Workflow Name}

\`\`\`bash
/workflows:{workflow-slug}
\`\`\`

**Expected workflow execution:**

\`\`\`
Phase 1: Parallel Analysis (quick parallel analysis)
→ Task("{analyst-1}: {task description}")
→ Task("{analyst-2}: {task description}")
→ Task("{analyst-3}: {task description}")

Analysts complete concurrently (significantly faster than sequential execution)

Phase 2: Main Thread Synthesis
→ Consolidate findings from all analysts
→ {Workflow-specific actions}

Phase 3: {Validation/Action Phase Name}
→ {Workflow-specific validation/actions}
\`\`\`
```

### Integration Points Section

**Pattern**:

```markdown
## Integration Points

- **Before Execution**: {Commands that prepare for this workflow}
- **After Execution**: {Commands that follow this workflow}
- **Works With**: {Related commands}
```

## Workflow Command Template

Use this structure for new workflow commands:

```markdown
---
description: "Execute {workflow purpose} using parallel domain analysis"
allowed-tools: Task
---

# Command: {Workflow Name}

## Purpose

{Detailed purpose description}

## Usage

\`\`\`bash
/workflows:{workflow-slug}
\`\`\`

## Process

1. **Parallel Analysis Phase**: Launch {N} domain analysts concurrently
2. **Synthesis Phase**: Main thread consolidates findings and {implements/reports}
3. **{Action} Phase**: {Validation/reporting/implementation description}

## Agent Integration

- **Primary Agent**: {primary-analyst}
- **Parallel Domain Analysts** ({N} concurrent):
  - {analyst-1} - {description}
  - {analyst-2} - {description}

## Implementation Steps

### Phase 1: Parallel {Domain} Analysis

\`\`\`python
# Launch {N} analysts concurrently
Task("{analyst-1}: {task description}")
Task("{analyst-2}: {task description}")

# Each analyst persists findings to .agent/context/
\`\`\`

### Phase 2: Main Thread Synthesis & {Implementation/Reporting}

\`\`\`python
# Read all analyst artifacts
Read(.agent/context/{pattern-1})
Read(.agent/context/{pattern-2})

# Based on consolidated findings:
# {Workflow-specific actions}
\`\`\`

### Phase 3: {Validation/Action}

\`\`\`python
# {Workflow-specific validation or actions}
\`\`\`

## Examples

### Complete {Workflow Name}

\`\`\`bash
/workflows:{workflow-slug}
\`\`\`

**Expected workflow execution:**

\`\`\`
Phase 1: Parallel Analysis (quick parallel analysis)
→ Task("{analyst-1}: {task}")
→ Task("{analyst-2}: {task}")

Analysts complete concurrently (significantly faster than sequential execution)

Phase 2: Main Thread Synthesis
→ Consolidate findings
→ {Workflow actions}

Phase 3: {Validation/Action}
→ {Results}
\`\`\`

## Integration Points

- **Before Execution**: {Prerequisites or preparatory commands}
- **After Execution**: {Follow-up commands}
- **Works With**: {Related commands}

## Performance Characteristics

**Sequential Approach:**
- Analysts execute one after another
- Total time scales linearly with analyst count

**Parallel Approach:**
- Multiple analysts run simultaneously using Task tool
- Execution time approaches slowest analyst (Amdahl's Law)
- **Performance Gain: Significantly faster through concurrent execution**

**Note**: Actual performance depends on system resources, network latency for MCP tools, and analysis complexity.

## Domain Analyst Outputs

**{analyst-1}** persists to \`.agent/context/{pattern}\`:
- {Output type 1}
- {Output type 2}

**{analyst-2}** persists to \`.agent/context/{pattern}\`:
- {Output type 1}
- {Output type 2}
```

## Best Practices

1. **Keep analyst tasks focused**: Each Task() should have single clear objective
2. **Use descriptive task descriptions**: Include what analyst should analyze and report
3. **Persist comprehensive findings**: Analysts should write detailed reports to context files
4. **Return concise summaries**: 2-3 sentence summaries to main thread
5. **Avoid hardcoded metrics**: Use qualitative descriptions (anti-drift compliance)
6. **Validate after synthesis**: Always include validation or verification step
7. **Document integration points**: Show how workflow fits into larger development process

## Common Patterns

### Quality Improvement Workflows

Focus: Code quality, refactoring, cleanup
Analysts: refactoring-analyst, quality-analyst, architecture-analyst
Action: Implement improvements based on findings

### Security/Performance Audits

Focus: Assessment and reporting
Analysts: Domain-specific (security, performance, database)
Action: Generate comprehensive report with recommendations

### Documentation Workflows

Focus: Documentation generation/updates
Analysts: documentation-analyst, architecture-analyst, quality-analyst
Action: Generate or update documentation artifacts

### Comprehensive Reviews

Focus: Multi-perspective analysis
Analysts: Dynamic selection based on file types
Action: Consolidated review report
