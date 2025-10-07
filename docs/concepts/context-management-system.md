# Context Management System

Comprehensive guide to the enhanced context management system for coordinating between subagents and main thread.

## Overview

The context management system provides a hierarchical, incremental, collaborative structure for coordinating analysis and implementation between domain analysts and the main thread.

**Key Benefits**:

- Clean session-based organization
- Incremental updates avoid duplicate work
- Lean, actionable context files (<30 seconds to read)
- Clear audit trail of decisions and implementations
- Human-editable without special tooling

## Directory Structure

```text
.agent/context/
└── {session-id}/
    ├── session.md              # Session metadata and high-level summary
    ├── python-analyst.md       # Python-specific findings
    ├── security-analyst.md     # Security-specific findings
    ├── quality-analyst.md      # Quality-specific findings
    └── {agent-name}.md         # One file per agent
```

**Benefits**:

- No date/session in filename (cleaner)
- Easy to locate specific agent output
- Better for git diffs
- Clear separation of concerns

## Session Management Commands

### Initialize Session

```bash
python3 ~/.claude/.agent/scripts/session_manager.py init [topic]
```

Creates session directory and `session.md` file with metadata.

### Get Current Session ID

```bash
python3 ~/.claude/.agent/scripts/session_manager.py current
```

Returns the current session ID (8-character UUID).

### Get Context Directory

```bash
python3 ~/.claude/.agent/scripts/session_manager.py context_dir
```

Returns full path to current session's context directory.

### List Agents Invoked

```bash
python3 ~/.claude/.agent/scripts/session_manager.py list_agents
```

Lists all agents that have been invoked in the current session.

### Archive Session

```bash
python3 ~/.claude/.agent/scripts/session_manager.py archive
```

Marks the current session as completed in `session.md`.

## Context File Format (Lean & Actionable)

Each agent context file follows this structure:

```markdown
# {Agent Name} Analysis

**Objective**: {1-sentence: what was analyzed and why}
**Last Updated**: {timestamp}
**Iteration**: {#}

---

## Analysis

### {Finding Category 1}
- **Issue**: {concise description} - {file}:{line}
- **Pattern**: {what was found}

### {Finding Category 2}
- **Issue**: {concise description} - {file}:{line}
- **Pattern**: {what was found}

---

## Actionable Tasks

### Critical (Do First)
- [ ] {specific action} - {file}:{line} - {1-line rationale}
- [ ] {specific action} - {file}:{line} - {1-line rationale}

### Important (Do Next)
- [ ] {specific action} - {file}:{line} - {1-line rationale}
- [ ] {specific action} - {file}:{line} - {1-line rationale}

### Enhancements (Nice to Have)
- [ ] {specific action} - {file}:{line} - {1-line rationale}

---

## Main Thread Log

### {timestamp}
**Completed**: {comma-separated task references}
**Deferred**: {comma-separated task references} - {why}
```

### Lean Context Principles

1. ✅ **No Executive Summaries** - Redundant with main thread response
2. ✅ **No Verbose Methodology** - Keep focused on findings
3. ✅ **Tasks, Not Paragraphs** - Checkbox format for actions
4. ✅ **Scannable in <30 seconds** - Human can read entire file quickly
5. ✅ **Concrete References** - Every finding has {file}:{line}
6. ✅ **Grouped by Priority** - Clear Critical/Important/Enhancement sections

## Incremental Update Pattern

### When Context File Already Exists

Subagents follow this pattern:

```python
# 1. Read existing context
context_file = f".agent/context/{session_id}/{agent_name}.md"

# 2. Check what changed
# - New files analyzed?
# - New issues found?
# - Previous tasks now obsolete?

# 3. Update Analysis sections
# - Add new findings
# - Mark obsolete findings with ~~strikethrough~~

# 4. Update Actionable Tasks
# - Add new tasks to appropriate priority
# - Mark completed tasks: - [x] ~~task~~

# 5. Increment iteration number
# Update metadata: **Iteration**: {n+1}
```

### Example Incremental Update

```markdown
## Analysis

### Type Safety Issues
- **Issue**: Missing type hints in auth module - auth.py:45
- **Issue**: Any types in API routes - routes/api.py:123
- ~~Issue: Untyped config (fixed in iteration 1)~~

## Actionable Tasks

### Critical (Do First)
- [ ] Add type hints to auth.authenticate() - auth.py:45 - Security impact
- [x] ~~Add types to config loader - config.py:12~~

### Important (Do Next)
- [ ] Replace Any with proper types - routes/api.py:123 - Maintainability
```

## Subagent Behavior

### When Invoked

1. Get session ID: `python3 ~/.claude/.agent/scripts/session_manager.py current`
2. Get context directory: `python3 ~/.claude/.agent/scripts/session_manager.py context_dir`
3. Check if context file exists: `{context_dir}/{agent-name}.md`

**If file exists**:

- Read existing content
- Identify what changed (new files, new issues)
- Update "Analysis" sections with new findings only
- Add new tasks to "Actionable Tasks"
- Mark obsolete tasks as ~~strikethrough~~
- Update iteration number

**If file is new**:

- Create full structure with lean format
- Add Objective, Analysis, Actionable Tasks, Main Thread Log sections

1. Write concise, actionable findings
2. Return focused summary to main thread

### Response Format to Main Thread

```markdown
## {Agent} Analysis Complete

**Objective**: {what was analyzed}

**Key Finding**: {most critical insight}

**Tasks Added**:
- {count} Critical
- {count} Important
- {count} Enhancements

**Updates** (for incremental): {Updated sections | New findings}

**See**: `.agent/context/{session-id}/{agent-name}.md`
```

## Main Thread Responsibilities

### After Receiving Subagent Response

1. Read context file for full understanding
2. Execute tasks based on recommendations
3. **Update context file** "Main Thread Log":

```markdown
### 2025-10-06 14:23
**Completed**: Critical #1, Critical #2, Important #1
**Deferred**: Enhancement #3 - out of scope for current sprint
```

This creates audit trail without bloat.

## Session Metadata File

### session.md Format

```markdown
# Session: {session-id}

**Started**: {timestamp}
**Topic**: {optional topic label}
**Status**: active | completed

## Agents Invoked
- python-analyst - {timestamp}
- security-analyst - {timestamp}

## Overview
{2-3 sentences: what was accomplished this session}

## Key Artifacts
- {files created/modified}
```

**No bloat**: Just essential tracking information.

## Avoiding Duplicate Work

### Mechanisms

1. **Check Previous Analysis**: Agents read their existing context file before starting
2. **Incremental Updates**: Only add net-new findings, don't recreate
3. **Main Thread Marks Completed**: Tasks marked immediately after completion
4. **Obsolete Tracking**: Old tasks/findings marked with ~~strikethrough~~
5. **Session Registry**: `session.md` shows which agents already ran

### Example Workflow

```python
# First invocation
Task("python-analyst: Analyze codebase for PEP 8 compliance")
# Creates: .agent/context/{session-id}/python-analyst.md
# Iteration: 1

# Second invocation (after code changes)
Task("python-analyst: Re-analyze after refactoring")
# Updates: .agent/context/{session-id}/python-analyst.md
# Iteration: 2
# - Adds new findings
# - Marks old findings as resolved with ~~strikethrough~~
# - Increments iteration counter
```

## Human Editability

### Features

- Pure markdown with standard ATX headers
- Max 2 levels of nesting (h1, h2 only)
- Checkbox tasks are GitHub-flavored markdown
- Clear section boundaries
- No special tooling needed to read/edit
- Git-diff friendly format
- Can manually check off tasks or add notes

### Example Manual Edit

```markdown
## Actionable Tasks

### Critical (Do First)
- [x] Add type hints to auth module - auth.py:45 - Security impact ← manually checked
- [ ] Fix SQL injection vulnerability - api.py:123 - CRITICAL
  <!-- Note: Discussed with team, using parameterized queries -->

### Important (Do Next)
- [ ] Optimize database query - models.py:67 - Performance
  <!-- TODO: Benchmark before/after -->
```

## Actionable Task Handoff

### Task Format

Every task includes:

- **Priority**: Critical/Important/Enhancement
- **Action**: Specific, executable step
- **Location**: {file}:{line} reference
- **Rationale**: 1-line why this matters

### Example

```markdown
### Critical (Do First)
- [ ] Add input validation to login endpoint - routes/auth.py:45 - Prevents SQL injection
- [ ] Implement rate limiting on API - middleware/rate_limit.py:23 - Prevents DoS attacks

### Important (Do Next)
- [ ] Add error logging to payment processor - services/payment.py:89 - Debugging production issues
- [ ] Update API documentation for v2 endpoints - docs/api.md:156 - Client integration

### Enhancements (Nice to Have)
- [ ] Add caching layer for user profiles - models/user.py:234 - Improve response time
- [ ] Refactor duplicated validation logic - utils/validators.py:12 - Code maintainability
```

## Integration with Workflow Commands

### Pattern

```python
# Workflow invokes analyst for research
1. Invoke {domain}-analyst for analysis
2. Read .agent/context/{session-id}/{domain}-analyst.md
3. Execute actionable tasks from context
4. Update Main Thread Log with completion status
5. Delegate to next command (daisy-chain)
```

### Example: Comprehensive Review Workflow

```python
# Phase 1: Parallel Analysis
Task("quality-analyst: Analyze code quality for feature/x")
Task("security-analyst: Perform vulnerability assessment for feature/x")
Task("testing-analyst: Assess test coverage for feature/x")

# Each creates: .agent/context/{session-id}/{agent}-analyst.md

# Phase 2: Main Thread Synthesis
Read(.agent/context/{session-id}/quality-analyst.md)
Read(.agent/context/{session-id}/security-analyst.md)
Read(.agent/context/{session-id}/testing-analyst.md)

# Phase 3: Execute Tasks
# Implement recommendations from all analysts

# Phase 4: Update Context
# Update each agent's Main Thread Log section with completion status
```

## Best Practices

### For Subagents

1. **Always check for existing context file** before creating new
2. **Update incrementally** - add new, mark old as obsolete
3. **Keep it lean** - target <30 seconds to read entire file
4. **Concrete references** - every finding needs {file}:{line}
5. **Actionable tasks** - checkbox format with clear rationale
6. **Return task counts** in summary to main thread

### For Main Thread

1. **Read context files** before implementing
2. **Execute tasks by priority** - Critical first
3. **Update Main Thread Log** after completion
4. **Mark deferred tasks** with brief rationale
5. **Archive session** when complete

### For Humans

1. **Context files are readable** - no special tools needed
2. **Can manually edit** - add notes, check off tasks
3. **Git-friendly** - easy to see changes in diffs
4. **Scannable** - find what you need quickly
5. **Clear structure** - always same format

## Migration from Old System

### Backward Compatibility

- Old `.agent/context/{YYYY-MM-DD}-{topic}-{sessionid}.md` files remain untouched
- New sessions automatically use new structure
- No breaking changes to existing workflows
- Session manager creates directories as needed

### Key Differences

**Old System**:

```text
.agent/context/2025-10-06-python-analysis-abc123.md
.agent/context/2025-10-06-security-scan-abc123.md
```

**New System**:

```text
.agent/context/abc123/python-analyst.md
.agent/context/abc123/security-analyst.md
.agent/context/abc123/session.md
```

## Troubleshooting

### Context File Not Found

```bash
# Check session ID
python3 ~/.claude/.agent/scripts/session_manager.py current

# Check context directory exists
python3 ~/.claude/.agent/scripts/session_manager.py context_dir

# Initialize if needed
python3 ~/.claude/.agent/scripts/session_manager.py init
```

### Subagent Not Creating Context File

1. Verify session is initialized
2. Check agent has Write tool access
3. Verify path construction in agent prompt
4. Check for permission errors

### Context Files Too Large

1. Review for verbose explanations (should be lean)
2. Check for duplicate findings (use incremental updates)
3. Verify Main Thread Log isn't growing unbounded
4. Consider archiving completed sessions

## Advanced Usage

### Context Helper Python Module

For programmatic access to context files:

```python
from context_helper import (
    get_context_file,
    read_context,
    write_context,
    add_tasks,
    mark_task_obsolete,
    add_main_thread_log
)

# Get context file path
context_file = get_context_file("python-analyst")

# Read parsed context
sections = read_context("python-analyst")

# Add tasks to a priority level
add_tasks("python-analyst", [
    "Fix type hint in auth.py:45 - Security issue",
    "Add validation to input.py:23 - Data integrity"
], priority="Critical")

# Mark task as obsolete
mark_task_obsolete("python-analyst", "Fix type hint")

# Update main thread log
add_main_thread_log("python-analyst",
    completed=["Critical #1", "Important #2"],
    deferred=["Enhancement #1 - out of scope"]
)
```

## Summary

The enhanced context management system provides:

1. ✅ **Clean Organization**: Session-based directory structure
2. ✅ **Incremental Updates**: Agents update existing context, don't recreate
3. ✅ **Lean Context**: Files scannable in <30 seconds
4. ✅ **Actionable Handoff**: Tasks grouped by priority with clear rationale
5. ✅ **Audit Trail**: Main Thread Log tracks what was done
6. ✅ **Human-Editable**: Standard markdown, no special tools
7. ✅ **Avoids Duplicate Work**: Check existing analysis before re-analyzing
8. ✅ **Clear Coordination**: Well-defined responsibilities for agents and main thread

This system significantly improves coordination between subagents and main thread while keeping context manageable and actionable.
