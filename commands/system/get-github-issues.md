---
description: "Fetch GitHub issues and integrate them into current work session"
argument-hint: "[arguments]"
allowed-tools: Bash, Read, Write, Grep
---

# Command: Get GitHub Issues

## Purpose

Fetches GitHub issues from repository and integrates them into the current work session for immediate context and reference. Issues are persisted to `.agent/context/` for session-wide awareness.

## Usage

```bash
/system:get-github-issues $ARGUMENTS
```

**Interactive Mode** (no arguments):

```bash
/system:get-github-issues
→ Prompts for: filters, labels, milestone, assignee, state
```

**Arguments**:

- `$1` (--filter): Issue filter query (optional, default: all open issues)
  - `assigned`: Issues assigned to you
  - `created`: Issues you created
  - `mentioned`: Issues mentioning you
  - `milestone:<name>`: Issues in specific milestone
  - `label:<label>`: Issues with specific label
  - Custom gh issue list query
- `$2` (--state): Issue state (optional, default: open)
  - `open`: Open issues only
  - `closed`: Closed issues only
  - `all`: Both open and closed
- `$3` (--labels): Comma-separated label filters (optional)
- `$4` (--milestone): Milestone filter (optional)
- `$5` (--assignee): Assignee filter (optional, @me for assigned to you)
- `$6` (--limit): Maximum number of issues to fetch (optional, default: 50)
- `$7` (--sync-to-tasks): Sync issues to tasks.md (optional, default: false)
- `$8` (--format): Output format (optional, default: session)
  - `session`: Save to .agent/context/ for session awareness
  - `tasks`: Sync to .agent/tasks.md
  - `both`: Both session and tasks.md

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - Interactive mode: fetch all open issues
- `$ARGUMENTS = "--filter=assigned"` - Fetch issues assigned to you
- `$ARGUMENTS = "--milestone=v2.0"` - Fetch all issues in v2.0 milestone
- `$ARGUMENTS = "--labels=bug,critical --state=open"` - Fetch open critical bugs
- `$ARGUMENTS = "--assignee=@me --limit=20"` - Fetch your 20 most recent assigned issues
- `$ARGUMENTS = "--filter=assigned --sync-to-tasks=true"` - Fetch assigned issues and sync to tasks.md
- `$ARGUMENTS = "--labels=feature --format=both"` - Fetch features, save to session + tasks.md

## Process

### Interactive Mode (No Arguments)

1. **Prompt for Filters**:

   ```text
   What would you like to fetch?
   1. All open issues
   2. Issues assigned to me
   3. Issues I created
   4. Issues by milestone
   5. Issues by label
   6. Custom query
   ```

2. **Collect Additional Filters**:

   ```text
   State (open/closed/all):
   > open

   Labels (comma-separated, optional):
   > bug, critical

   Limit (max issues, default 50):
   > 20

   Sync to tasks.md? (yes/no):
   > no
   ```

3. **Fetch and Process**: Use gh CLI to fetch issues

4. **Persist to Session**: Save to `.agent/context/github-issues-{timestamp}.md`

5. **Display Summary**: Show fetched issues with key details

### Standard Mode (With Arguments)

1. **Parse Arguments**: Extract filters, state, labels, milestone, assignee, limit

2. **Build gh CLI Query**: Construct query string for gh issue list

3. **Fetch Issues**: Execute gh issue list command with filters:

   ```bash
   gh issue list --state=open --label=bug --limit=20 --json number,title,state,labels,milestone,assignee,body,url,createdAt,updatedAt
   ```

4. **Parse JSON Response**: Extract issue details and format for session context

5. **Create Session Context File**: Save to `.agent/context/github-issues-{timestamp}.md` with structured format:

   ```markdown
   # GitHub Issues - Fetched {timestamp}

   **Repository**: org/repo
   **Filter**: assigned to @me
   **State**: open
   **Count**: 12 issues

   ---

   ## Issue #123: Implement user authentication

   **State**: open
   **Labels**: feature, authentication
   **Milestone**: v2.0
   **Assignee**: @username
   **Created**: 2025-10-01
   **Updated**: 2025-10-05
   **URL**: https://github.com/org/repo/issues/123

   **Description**:
   Build JWT-based authentication with refresh tokens...

   **Acceptance Criteria**:
   - [ ] JWT token generation
   - [ ] Refresh token rotation
   ...

   ---
   ```

6. **Optional: Sync to tasks.md**: If --sync-to-tasks=true or --format includes tasks:
   - Convert issues to tasks.md format
   - Append to `.agent/tasks.md` with issue links
   - Mark as synced from GitHub

7. **Display Summary**:

   ```text
   ✓ Fetched 12 issues from org/repo
   ✓ Saved to .agent/context/github-issues-2025-10-06.md
   ✓ Issues are now available for reference in this session

   Summary:
   - 8 features (label:feature)
   - 3 bugs (label:bug)
   - 1 enhancement (label:enhancement)

   Top priorities:
   - #123: Implement user authentication (v2.0)
   - #125: Fix login validation bug (v2.0)
   - #127: Add password reset (v2.0)
   ```

## Session Integration

### How Issues Become Session-Aware

When issues are fetched and saved to `.agent/context/`:

1. **Automatic Context**: Claude can reference these issues throughout the session
2. **No Manual Loading**: Issues are immediately available for queries
3. **Persistent Context**: Issues remain available until session ends
4. **Rich Context**: Full issue details (description, labels, assignees, etc.)

### Using Issues in Session

Once fetched, you can:

```bash
# Reference issues directly
"Work on issue #123"
"Show me all the authentication-related issues"
"What's the status of milestone v2.0 issues?"

# Create implementation plans
"Create implementation plan for issue #123"

# Generate commits
"Implement fix for issue #125 and commit"

# Link work to issues
"I've implemented #123, create PR linking to this issue"
```

## Agent Integration

- **Specialist Options**: documentation-analyst can be spawned to analyze issue descriptions and generate implementation plans

## Examples

### Interactive Mode

```bash
/system:get-github-issues

Claude: What would you like to fetch?
1. All open issues
2. Issues assigned to me
3. Issues I created
4. Issues by milestone
5. Issues by label
6. Custom query

User: 2

Claude: Fetching issues assigned to you...

✓ Fetched 8 issues
✓ Saved to .agent/context/github-issues-2025-10-06.md

Issues available:
- #123: Implement user authentication (feature, v2.0)
- #125: Fix login validation bug (bug, v2.0)
- #127: Add password reset (feature, v2.0)
... (5 more)
```

### Fetch Issues by Milestone

```bash
/system:get-github-issues --milestone=v2.0

✓ Fetched 15 issues in milestone v2.0
✓ Saved to .agent/context/github-issues-2025-10-06.md

Milestone v2.0 progress: 8/15 complete (53%)

Open issues:
- #123: Implement user authentication
- #125: Fix login validation bug
- #127: Add password reset
... (4 more)
```

### Fetch Assigned Issues and Sync to Tasks

```bash
/system:get-github-issues --filter=assigned --sync-to-tasks=true

✓ Fetched 12 issues assigned to you
✓ Saved to .agent/context/github-issues-2025-10-06.md
✓ Synced to .agent/tasks.md

Your assigned issues:
- #123: Implement user authentication (v2.0) → tasks.md line 15
- #125: Fix login validation bug (v2.0) → tasks.md line 23
... (10 more)
```

### Fetch Critical Bugs

```bash
/system:get-github-issues --labels=bug,critical --state=open --limit=10

✓ Fetched 5 critical bugs
✓ Saved to .agent/context/github-issues-2025-10-06.md

Critical bugs requiring attention:
- #125: Fix login validation bug (assigned: @you, created 2 days ago)
- #142: Database connection leak (assigned: @lead, created 1 week ago)
... (3 more)
```

### Custom Query

```bash
/system:get-github-issues --filter="is:open label:feature milestone:v2.0 assignee:@me"

✓ Fetched 6 feature issues in v2.0 assigned to you
✓ Saved to .agent/context/github-issues-2025-10-06.md
```

### Fetch All Issues for Planning

```bash
/system:get-github-issues --state=all --format=both --limit=100

✓ Fetched 100 issues
✓ Saved to .agent/context/github-issues-2025-10-06.md
✓ Synced to .agent/tasks.md

Issue breakdown:
- 45 open (45%)
- 55 closed (55%)

By label:
- 30 features
- 25 bugs
- 15 enhancements
- 30 other
```

## Session Context File Format

The generated `.agent/context/github-issues-{timestamp}.md` file uses this structure:

```markdown
# GitHub Issues Session Context

**Generated**: 2025-10-06T10:30:00Z
**Repository**: org/repo
**Filter**: assignee:@me state:open
**Total Issues**: 12

## Quick Reference

| # | Title | Labels | Milestone | State |
|---|-------|--------|-----------|-------|
| 123 | Implement user authentication | feature, auth | v2.0 | open |
| 125 | Fix login validation bug | bug, critical | v2.0 | open |
| 127 | Add password reset | feature, auth | v2.0 | open |
...

---

## Detailed Issues

### Issue #123: Implement user authentication

- **URL**: https://github.com/org/repo/issues/123
- **State**: open
- **Labels**: feature, authentication
- **Milestone**: v2.0
- **Assignee**: @username
- **Created**: 2025-10-01T14:20:00Z
- **Updated**: 2025-10-05T09:15:00Z

**Description**:

Build JWT-based authentication with refresh tokens, password hashing, and session management.

**Acceptance Criteria**:

- [ ] JWT token generation
- [ ] Refresh token rotation
- [ ] Password hashing with bcrypt
- [ ] Session management

**Comments**: 3 comments (view on GitHub)

---

### Issue #125: Fix login validation bug

...

---

## Summary Statistics

- **Total Issues**: 12
- **By State**: 12 open, 0 closed
- **By Label**:
  - feature: 8
  - bug: 3
  - enhancement: 1
- **By Milestone**:
  - v2.0: 10
  - v2.1: 2
- **By Assignee**:
  - @username: 12

## Usage Suggestions

You can now:
- Reference issues by number: "Work on issue #123"
- Query by label: "Show me all authentication issues"
- Check milestone progress: "What's left for v2.0?"
- Create implementation plans: "Plan implementation for #123"
```

## tasks.md Integration

When syncing to tasks.md (`--sync-to-tasks=true` or `--format=both`), issues are appended in this format:

```markdown
# Project Tasks - Synced from GitHub Issues

## From GitHub (Synced 2025-10-06T10:30:00Z)

## [TASK-012] Implement user authentication (GitHub #123)

**Status**: pending
**Priority**: high
**Category**: feature
**Created**: 2025-10-06T10:30:00Z
**Labels**: authentication
**Milestone**: v2.0
**Assignee**: @username
**GitHub Issue**: https://github.com/org/repo/issues/123

**Description**:
Build JWT-based authentication with refresh tokens

**Acceptance Criteria**:

- [ ] JWT token generation
- [ ] Refresh token rotation
- [ ] Password hashing with bcrypt
- [ ] Session management

---

## [TASK-013] Fix login validation bug (GitHub #125)

**Status**: pending
**Priority**: high
**Category**: bug
...

---
```

## Best Practices

1. **Start each work session** by fetching your assigned issues
2. **Use milestone filters** to focus on current sprint work
3. **Sync to tasks.md** for offline reference and planning
4. **Refresh periodically** during long sessions to get updates
5. **Use label filters** to focus on specific work types (bugs, features)
6. **Reference issues by number** in commits and conversations
7. **Check session context** before implementing to ensure you have latest details

## Integration Points

**Works Well With**:

- `/system:create-github-issue` - Create new issues from work session
- `/system:create-task` - Capture local tasks alongside GitHub issues
- `/implement:small` - Implement issue with context
- `/spec-kit:specify` - Create spec from issue requirements
- `/git:commit` - Reference issue numbers in commits
- `/git:pr` - Link PRs to issues automatically

**Typical Workflow**:

```bash
# 1. Start work session - fetch your issues
/system:get-github-issues --filter=assigned

# 2. Pick an issue to work on
"I'll work on issue #123"

# 3. Create implementation plan
/spec-kit:specify
# Use issue details from .agent/context/github-issues-*.md

# 4. Implement
/implement:small

# 5. Commit with issue reference
/git:commit
# Commit message includes: "Closes #123"

# 6. Create PR
/git:pr
# PR automatically links to #123
```

## Output

Provides:

- Fetched issue count and breakdown
- Session context file location
- Quick reference table of all issues
- Detailed issue information
- Summary statistics
- Usage suggestions

## Advanced Filters

**Complex queries** using gh CLI syntax:

```bash
# Issues updated in last 7 days
/system:get-github-issues --filter="is:open updated:>2025-09-29"

# High priority issues
/system:get-github-issues --filter="is:open label:priority-high"

# Issues with no assignee
/system:get-github-issues --filter="is:open no:assignee"

# Issues in multiple milestones
/system:get-github-issues --filter="is:open milestone:v2.0,v2.1"

# Recently closed issues
/system:get-github-issues --filter="is:closed closed:>2025-09-29" --state=closed
```

## Session Refresh

To refresh issues during a session:

```bash
# Re-fetch with same filters (updates existing context file)
/system:get-github-issues --filter=assigned

# Or fetch different set
/system:get-github-issues --milestone=v2.1
```

The most recent fetch replaces previous context, so you always have current state.
