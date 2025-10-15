---
description: "Capture adhoc tasks with standardized metadata and origin tagging"
argument-hint: "\"task description\" [--priority=level] [--category=type]"
allowed-tools: Read, Write, Edit, mcp__sequential-thinking__sequentialthinking
---

# Command: Task Add

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Capture adhoc work items to .agent/tasks.md with origin=adhoc tagging, parse description + flags (--priority, --category), generate auto-incremented TASK-XXX ID, create standardized entry (status: pending, metadata, ISO timestamp), save file

**P**urpose: Enable quick idea/bug capture without implementation commitment, maintain unified task system with origin tracking (adhoc vs code-comment vs github-issue), support filtered workflows by origin/priority/category, prevent context loss from mental notes

**E**xpectation: New task entry in .agent/tasks.md with TASK-ID, confirmation message, metadata validated, NO implementation/execution, strict capture-only operation

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% metadata fields, Accuracy >90% ID increment, Relevance >85% categorization, Efficiency <3s capture)

## Purpose

Captures adhoc work items and ideas into the unified task management system at `.agent/tasks.md` with origin tagging.

**⚠️ STRICT CONSTRAINT: This command MUST NOT implement, code, or execute any tasks. It only captures task descriptions.**

## Usage

```bash
/task:add $ARGUMENTS
```

**Arguments**:

- `$1` (task-description): Description of the work item or task to capture (required)
- `--priority`: Priority level: `low | medium | high | critical` (optional, default: medium)
- `--category`: Task category: `bug | feature | refactor | docs | test | research | chore` (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "Fix login validation error"` - Basic adhoc task
- `$ARGUMENTS = "Add user profile page --priority=high --category=feature"` - High-priority feature
- `$ARGUMENTS = "Update API documentation --category=docs"` - Documentation task
- `$ARGUMENTS = "Research authentication patterns --priority=high --category=research"` - Research task

## Process

**FORBIDDEN ACTIONS**: Implementing features, executing tasks, creating files other than tasks.md, making code changes

**ALLOWED ACTIONS ONLY**:

1. **Parse Arguments**: Extract task description, priority, and category from $ARGUMENTS
2. **Read Existing File**: Read `{project_root}/.agent/tasks.md` (create if doesn't exist)
3. **Generate Task ID**: Auto-increment from highest existing TASK-XXX number
4. **Tag Origin**: Set origin to `adhoc` (distinguishes from code-comment and github-issue)
5. **Create Task Entry**: Use standardized format with metadata
6. **Save File**: Write updated tasks.md
7. **Report Success**: Confirm task captured with ID
8. **STOP IMMEDIATELY** - No further actions permitted

## Task Format

All adhoc tasks use this standardized format:

```markdown
## [TASK-001] Fix login validation error

**Status**: pending
**Priority**: high
**Category**: bug
**Origin**: adhoc
**Created**: 2025-10-13T10:30:00Z

**Description**:
Fix the validation error that occurs when users attempt to login with special characters in their username.

---
```

**Metadata Fields**:

- **Status**: Always `pending` for new tasks
- **Priority**: `low | medium | high | critical`
- **Category**: `bug | feature | refactor | docs | test | research | chore`
- **Origin**: Always `adhoc` (user-created task)
- **Created**: ISO 8601 timestamp (UTC)

## Explicit Constraints

**IN SCOPE**: Task capture only (description parsing, ID generation, metadata tagging with origin=adhoc, file write to .agent/tasks.md), priority/category flags, ISO timestamps, auto-increment logic
**OUT OF SCOPE**: Task implementation/execution (FORBIDDEN), code changes, file creation beyond tasks.md, task analysis/breakdown, agent invocation, GitHub integration (use /github:create-issue-from-task)

## Agent Integration

- **No agents required** - Simple capture operation
- **Specialist Options**: code-quality-analyst can help categorize/prioritize if needed

## Examples

### Example 1: Basic Bug Task

```bash
/task:add "Fix login validation error"
# where $ARGUMENTS = "Fix login validation error"

# Expected behavior:
→ Task captured in .agent/tasks.md
→ [TASK-001] Fix login validation error
→ Priority: medium (default)
→ Category: (none)
→ Origin: adhoc
→ Status: pending
```

### Example 2: High-Priority Feature

```bash
/task:add "Add dark mode toggle --priority=high --category=feature"
# where $ARGUMENTS = "Add dark mode toggle --priority=high --category=feature"

# Expected behavior:
→ Task captured in .agent/tasks.md
→ [TASK-002] Add dark mode toggle
→ Priority: high
→ Category: feature
→ Origin: adhoc
→ Status: pending
```

### Example 3: Research Task

```bash
/task:add "Investigate OAuth integration strategies --priority=medium --category=research"
# where $ARGUMENTS = "Investigate OAuth integration strategies --priority=medium --category=research"

# Expected behavior:
→ Task captured in .agent/tasks.md
→ [TASK-003] Investigate OAuth integration strategies
→ Priority: medium
→ Category: research
→ Origin: adhoc
→ Status: pending
```

### Example 4: Technical Debt

```bash
/task:add "Refactor authentication module --category=refactor"
# where $ARGUMENTS = "Refactor authentication module --category=refactor"

# Expected behavior:
→ Task captured in .agent/tasks.md
→ [TASK-004] Refactor authentication module
→ Priority: medium (default)
→ Category: refactor
→ Origin: adhoc
→ Status: pending
```

## Integration Points

- **Follows**: Brainstorming, code review, bug discovery
- **Followed by**: `/task:execute` (triage and work on tasks)
- **Related**: `/task:scan-project` (code comments), `/github:convert-issues-to-tasks` (GitHub issues)

## Quality Standards

- Keep task description concise and actionable
- Use clear, descriptive titles
- Set priority when impact is known
- Categorize for better organization
- No breakdown or detailed planning (unless requested)
- ISO 8601 timestamps (UTC)
- Auto-incrementing task IDs
- Origin always tagged as `adhoc`

## Output

- Updated `{project_root}/.agent/tasks.md` with new task entry
- Task ID assignment (auto-incremented)
- Confirmation message with task details
- Brief validation of metadata

## Workflow Examples

### Quick Capture During Development

```bash
# Found a bug while coding
/task:add "Fix null pointer in user service --priority=high --category=bug"

# Idea for improvement
/task:add "Add caching to API responses --category=feature"

# Technical debt discovered
/task:add "Remove deprecated authentication code --category=refactor"
```

### Sprint Planning

```bash
# Capture sprint backlog items
/task:add "Implement user registration --priority=high --category=feature"
/task:add "Add password reset flow --priority=high --category=feature"
/task:add "Update user documentation --priority=medium --category=docs"
/task:add "Add integration tests --priority=medium --category=test"
```

### Research Phase

```bash
# Research tasks before implementation
/task:add "Research microservices patterns --category=research"
/task:add "Evaluate authentication libraries --priority=high --category=research"
/task:add "Performance benchmarking comparison --category=research"
```

## Best Practices

1. **Capture Immediately** - Don't wait, capture tasks as you think of them
2. **Keep Descriptions Concise** - One clear sentence is sufficient
3. **Use Priority Wisely** - Reserve `critical` for urgent blockers
4. **Categorize Consistently** - Helps with filtering and organization
5. **Review Regularly** - Check tasks at start of each session (`/task:execute`)
6. **Update Status** - Use `/task:execute` when starting work
7. **Convert to Issues** - Use `/github:create-issue-from-task` for team visibility

## Task vs GitHub Issue

**Use `/task:add` for**:

- Personal work items during development
- Quick capture of ideas and bugs
- Session-specific tasks
- Items not ready for team visibility
- Research and exploration

**Use `/github:create` for**:

- Team-visible work items
- Official project backlog
- Issues requiring discussion
- Work spanning multiple sessions

**Convert adhoc tasks to GitHub issues** when ready for team collaboration.

## Adhoc Task Benefits

**Why origin=adhoc?**

1. **Distinguishes from code comments** - Can filter by origin
2. **Separate from GitHub issues** - Local work vs team work
3. **Flexible workflow** - Convert to issues or archive as needed
4. **Quick capture** - No GitHub authentication required
5. **Private brainstorming** - Ideas stay local until ready

**Workflow Pattern**:

```
Idea/Bug → /task:add (adhoc) → Work locally → /github:create (team visibility)
```
