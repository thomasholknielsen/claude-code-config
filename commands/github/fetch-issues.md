---
description: "Fetch GitHub issues to session context for reference"
argument-hint: "[--filter=type] [--milestone=name] [--label=name] [--state=open]"
allowed-tools: Read, Write, Bash(gh:*), mcp__sequential-thinking__sequentialthinking
---

# Command: GitHub Fetch Issues

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Fetch GitHub issues to session context for reference.

**YOU MUST:**
1. ✓ Parse filter options (--filter, --milestone, --label, --state)
2. ✓ Fetch issues via gh CLI
3. ✓ Parse response (number, title, labels, body, assignees)
4. ✓ Format as markdown
5. ✓ Save to .agent/github-issues.md
6. ✓ Display summary stats

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Auto-import as tasks (use convert command)
- ✗ Skip formatting

---

## IMPLEMENTATION FLOW

### Step 1: Parse Filters
Extract filter options from $ARGUMENTS

### Step 2: Fetch Issues
Call gh CLI with filters

### Step 3: Parse Response
Extract issue metadata

### Step 4: Format Markdown
Create formatted markdown

### Step 5: Save File
Write to .agent/github-issues.md

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Fetch GitHub issues via gh CLI with filters (--filter=assigned/created/mentioned/all, --milestone, --label, --state=open/closed/all, --limit), parse response (number, title, labels, body, assignees), format as markdown, save to .agent/github-issues.md (overwrites previous)

**P**urpose: Provide GitHub issues as session context for reference without task import (use /github:convert-issues-to-tasks for that), support sprint planning and daily standup review, maintain always-current issue snapshot

**E**xpectation: Issues saved to .agent/github-issues.md with rich context (labels, milestones, descriptions), summary stats (count by priority/label), NO automatic task import (explicit via convert command), clear next steps guidance

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% issue data, Accuracy >90% gh CLI parsing, Relevance >85% filtered issues, Efficiency <10s fetch)

## Purpose

Fetches GitHub issues using the `gh` CLI and saves them to `.agent/github-issues.md` for reference during development sessions without importing them as tasks.

## Usage

```bash
/github:fetch-issues-issues $ARGUMENTS
```

**Arguments**:

- `--filter`: Issue filter: `assigned | created | mentioned | all` (optional, default: assigned)
- `--milestone`: Filter by milestone name (optional)
- `--label`: Filter by label name (optional, comma-separated for multiple)
- `--state`: Issue state: `open | closed | all` (optional, default: open)
- `--limit`: Max number of issues to fetch (optional, default: 50)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - Fetch your assigned open issues
- `$ARGUMENTS = "--filter=assigned"` - Explicitly fetch assigned issues
- `$ARGUMENTS = "--filter=created"` - Fetch issues you created
- `$ARGUMENTS = "--milestone=v2.0"` - Fetch issues in milestone v2.0
- `$ARGUMENTS = "--label=bug"` - Fetch issues with bug label
- `$ARGUMENTS = "--label=bug,critical"` - Fetch issues with bug AND critical labels
- `$ARGUMENTS = "--filter=assigned --milestone=v2.0 --label=bug"` - Combined filters
- `$ARGUMENTS = "--state=all --limit=100"` - Fetch all issues (open and closed), up to 100

## Process

1. **Parse Arguments**: Extract filter criteria
2. **Verify gh CLI**: Ensure GitHub CLI is installed and authenticated
3. **Build gh Query**: Construct gh issue list command with filters
4. **Fetch Issues**: Execute gh CLI command
5. **Parse Response**: Extract issue data (number, title, labels, body, etc.)
6. **Format Output**: Create organized markdown
7. **Save to File**: Write to `.agent/github-issues.md` (overwrites previous fetch)
8. **Report Summary**: Show count and location
9. **NO TASK IMPORT**: Issues stay in file, not converted to tasks (use `/github:convert-issues-to-tasks` for that)

## User Feedback Table

| Option | Description | Recommended |
|--------|-------------|-------------|
| **A. Assigned Issues** | Fetch your assigned open issues (no filters needed) | ← Recommended: Daily standup & task review |
| **B. Milestone/Sprint** | Fetch issues from a specific milestone for sprint planning | - Use: `--milestone=sprint-X` or `--milestone=v2.0` |
| **C. Bug Triage** | Fetch all open bugs across the repository for prioritization | - Use: `--label=bug --filter=all` |
| **D. Other Filter** | Custom filter (e.g., created issues, all issues, combined filters) | - Specify your own arguments |

**What type of issues would you like to fetch?**

## Next Steps Table

| Step | Action | Command |
|------|--------|---------|
| **1. Review Issues** | Read the fetched issues in markdown format to understand current state | `cat .agent/github-issues.md` |
| **2. Import as Tasks** | Convert selected issues into trackable tasks for work management | `/github:convert-issues-to-tasks --source-file=.agent/github-issues.md` ← Recommended: Typical workflow |
| **3. Refetch Updates** | Get the latest issue status and changes from GitHub | `/github:fetch-issues --filter=assigned` |
| **4. Filter & Re-import** | Fetch again with different filters, then import specific subset | `/github:fetch-issues --label=bug` → `/github:convert-issues-to-tasks --filter="label:bug AND priority:critical"` |

**What would you like to do next?**

## Output File Location

Issues are saved to:

```
.agent/github-issues.md
```

**Note**: Each fetch overwrites the previous file. This keeps the file current with latest GitHub state.

## Output Format

```markdown
# GitHub Issues

**Last Fetched**: 2025-10-13T16:00:00Z
**Repository**: org/repo
**Filters Applied**:
- Filter: assigned
- State: open
- Milestone: v2.0
- Label: bug

**Total Issues**: 12

---

## Issue #125: Database connection leak

**Labels**: bug, critical, p0
**Milestone**: v2.1.0
**State**: open
**Author**: @teammate
**Assignees**: @you, @teammate2
**Created**: 2025-10-10T09:00:00Z
**Updated**: 2025-10-13T14:30:00Z
**URL**: https://github.com/org/repo/issues/125

**Description**:
Connection pool not releasing connections properly under high load, leading to connection exhaustion after several hours of operation.

**Comments**: 8
**Recent Activity**:
- @you commented 2 hours ago: "Identified issue in connection pool configuration"

---

## Issue #130: Add user preferences page

**Labels**: feature, frontend
**Milestone**: v2.1.0
**State**: open
**Author**: @product-manager
**Assignees**: @you
**Created**: 2025-10-11T10:00:00Z
**Updated**: 2025-10-12T16:00:00Z
**URL**: https://github.com/org/repo/issues/130

**Description**:
Users should be able to customize their dashboard layout, notification preferences, and theme settings.

**Acceptance Criteria**:
- [ ] User can change theme (light/dark)
- [ ] User can configure notification preferences
- [ ] User can customize dashboard widgets
- [ ] Settings persist across sessions

---

## Issue #135: Refactor authentication middleware

**Labels**: tech-debt, refactor
**Milestone**: v2.2.0
**State**: open
**Author**: @you
**Assignees**: @you
**Created**: 2025-10-12T14:00:00Z
**Updated**: 2025-10-12T14:00:00Z
**URL**: https://github.com/org/repo/issues/135

**Description**:
Current authentication middleware is tightly coupled and difficult to test. Extract into separate service with proper dependency injection.

---

# Next Steps

## To Import Issues as Tasks

Use `/github:convert-issues-to-tasks` to convert specific issues to trackable tasks:

```bash
# Import all fetched issues
/github:convert-issues-to-tasks --source-file=.agent/github-issues.md

# Or import with additional filters
/github:convert-issues-to-tasks --filter="milestone:v2.1 AND label:bug"
```

## To View Issues

Read this file for reference during work:

```
.agent/github-issues.md
```

## To Fetch Again

Fetch latest updates:

```bash
/github:fetch-issues --filter=assigned
```

```

## Agent Integration

- **No agents required** - Direct gh CLI operation
- **Specialist Options**: None needed for fetching

## Examples

### Example 1: Fetch Assigned Issues

```bash
/github:fetch-issues
# where $ARGUMENTS = ""

# Expected behavior:
→ Fetching assigned GitHub issues...
→ Found 12 open issues
→ Saved to: .agent/github-issues.md
→
→ Summary:
→ - Critical: 2
→ - High: 5
→ - Medium: 5
→
→ Next steps:
→ - Review: cat .agent/github-issues.md
→ - Import: /github:convert-issues-to-tasks --source-file=.agent/github-issues.md
```

### Example 2: Fetch Milestone Issues

```bash
/github:fetch-issues "--milestone=v2.0"
# where $ARGUMENTS = "--milestone=v2.0"

# Expected behavior:
→ Fetching issues for milestone v2.0...
→ Found 25 open issues
→ Saved to: .agent/github-issues.md
→
→ By label:
→ - bug: 8
→ - feature: 12
→ - tech-debt: 5
```

### Example 3: Fetch Bug Issues

```bash
/github:fetch-issues "--label=bug --filter=all"
# where $ARGUMENTS = "--label=bug --filter=all"

# Expected behavior:
→ Fetching all bug issues...
→ Found 18 open issues
→ Saved to: .agent/github-issues.md
→
→ Priority distribution:
→ - critical: 3
→ - high: 7
→ - medium: 8
```

### Example 4: Fetch Your Created Issues

```bash
/github:fetch-issues "--filter=created --state=all"
# where $ARGUMENTS = "--filter=created --state=all"

# Expected behavior:
→ Fetching issues you created (open and closed)...
→ Found 45 issues
→ - Open: 12
→ - Closed: 33
→ Saved to: .agent/github-issues.md
```

### Example 5: Combined Filters

```bash
/github:fetch-issues "--filter=assigned --milestone=v2.1 --label=bug,critical"
# where $ARGUMENTS = "--filter=assigned --milestone=v2.1 --label=bug,critical"

# Expected behavior:
→ Fetching assigned critical bugs for v2.1...
→ Found 3 open issues
→ Saved to: .agent/github-issues.md
→
→ All critical - requires immediate attention
```

## Integration Points

- **Follows**: Sprint planning, daily standup, milestone review
- **Followed by**: `/github:convert-issues-to-tasks` (convert to tasks), issue review
- **Related**: `/task:execute --origin=github-issue`, `/github:create`

## Quality Standards

- **No Authentication Needed**: Uses existing gh CLI auth
- **Efficient Fetching**: Batch fetch, limit to reasonable count
- **Rich Context**: Include labels, milestone, assignees, description
- **Simple Storage**: Single file, always current
- **No Task Import**: Keep issues separate from tasks (explicit import via `/github:convert-issues-to-tasks`)
- **Summary Stats**: Provide helpful overview

## Output

- GitHub issues saved to `.agent/github-issues.md`
- Summary of fetched issues (count, labels, priority)
- File location for reference
- Suggestions for next steps
- No tasks created (use `/github:convert-issues-to-tasks` for that)

## Workflow Examples

### Sprint Planning

```bash
# Fetch all sprint issues
/github:fetch-issues --milestone=sprint-5

# Review issues
# Read .agent/github-issues.md

# Import high-priority issues as tasks
/github:convert-issues-to-tasks --filter="milestone:sprint-5 AND priority:high"
```

### Daily Standup

```bash
# Fetch assigned issues
/github:fetch-issues --filter=assigned

# Review what's on your plate
# Read file

# Import issues you'll work on today
/github:convert-issues-to-tasks --source-file=.agent/github-issues.md
```

### Bug Triage

```bash
# Fetch all open bugs
/github:fetch-issues --label=bug --state=open

# Review and prioritize
# Read context file

# Import critical bugs
/github:convert-issues-to-tasks --filter="label:bug AND priority:critical"
```

### Milestone Review

```bash
# Fetch all milestone issues (open and closed)
/github:fetch-issues --milestone=v2.0 --state=all

# Review progress
# Check completed vs open

# Import remaining open issues
/github:convert-issues-to-tasks --filter="milestone:v2.0 AND state:open"
```

## Best Practices

1. **Fetch Regularly** - Get latest issue updates
2. **Use Filters** - Narrow down to relevant issues
3. **Review Before Import** - Read context file first
4. **Import Selectively** - Only import issues you'll work on
5. **Milestone-Based** - Organize by sprint/milestone
6. **Label Filtering** - Focus on specific types (bug, feature)
7. **Limit Results** - Use `--limit` for large repositories

## GitHub CLI Requirements

**Prerequisites**:

1. Install GitHub CLI: `brew install gh`
2. Authenticate: `gh auth login`
3. Verify: `gh auth status`

**If gh CLI not installed**:

```
Error: GitHub CLI (gh) not found

Install:
  brew install gh

Authenticate:
  gh auth login

Verify:
  gh auth status
```

## Issue Filters

**Filter Types**:

- `assigned` - Issues assigned to you (default)
- `created` - Issues you created
- `mentioned` - Issues mentioning you
- `all` - All issues (may be many)

**State Options**:

- `open` - Open issues only (default)
- `closed` - Closed issues only
- `all` - Both open and closed

**Combining Filters**:

```bash
# Assigned open bugs in v2.0
/github:fetch-issues --filter=assigned --label=bug --milestone=v2.0

# All issues you created (open and closed)
/github:fetch-issues --filter=created --state=all

# Critical bugs (anyone assigned)
/github:fetch-issues --filter=all --label=bug,critical
```

## Context vs Tasks

**Context (via /github:fetch-issues)**:

- ✅ Reference material for session
- ✅ Review issues without commitment
- ✅ See full team workload
- ✅ Refresh anytime
- ❌ Not tracked as work items
- ❌ Not in tasks.md

**Tasks (via /github:convert-issues-to-tasks)**:

- ✅ Tracked work items
- ✅ Status management
- ✅ In tasks.md
- ✅ Can update and complete locally
- ❌ Manual sync to GitHub
- ❌ Requires explicit import

**Pattern**: Fetch → Review → Import selectively

## Fetch vs Import

**Use `/github:fetch-issues` when**:

- Starting sprint planning
- Daily standup review
- Need to see all team issues
- Want latest issue updates
- Haven't decided what to work on yet

**Use `/github:convert-issues-to-tasks` when**:

- Ready to work on specific issues
- Want to track progress locally
- Need task management features
- Have sanitized/prioritized list

**Workflow**:

```bash
# 1. Fetch for review
/github:fetch-issues --milestone=v2.0

# 2. Review in context file
# Decide which issues to work on

# 3. Import specific ones
/github:convert-issues-to-tasks --filter="milestone:v2.0 AND priority:high"

# 4. Work on tasks locally
/task:execute --origin=github-issue
/task:execute TASK-XXX --status=in-progress
```

## Next Steps After Fetching

```bash
# Review fetched issues
cat .agent/github-issues.md

# Import specific issues
/github:convert-issues-to-tasks --source-file=.agent/github-issues.md

# Or import with filters
/github:convert-issues-to-tasks --filter="label:bug AND priority:critical"

# List tasks from GitHub
/task:execute --origin=github-issue

# Fetch again for updates
/github:fetch-issues --filter=assigned
```

## File Management

**Location**: `.agent/github-issues.md`

**Behavior**: Each fetch overwrites the previous file

**Why Single File?**:

- Always contains latest GitHub state
- Simple file management
- No need to track multiple files
- Easy to reference: always same path
- Automatically stays current

**Viewing File**:

```bash
# View fetched issues
cat .agent/github-issues.md

# Or open in editor
open .agent/github-issues.md
```

## Error Handling

**gh CLI Not Found**:

```
Error: GitHub CLI (gh) not found
Install: brew install gh
Then authenticate: gh auth login
```

**Not Authenticated**:

```
Error: Not authenticated with GitHub
Run: gh auth login
```

**No Issues Found**:

```
No issues found matching filters
Try:
- Remove some filters
- Check milestone/label names
- Use --filter=all to see all issues
```

**Repository Not Found**:

```
Error: Not in a git repository
This command must be run from within a GitHub repository
```

## Advanced Filtering

**Multiple Labels (AND)**:

```bash
/github:fetch-issues --label=bug,critical
# Issues with BOTH bug AND critical labels
```

**Milestone + Label**:

```bash
/github:fetch-issues --milestone=v2.0 --label=feature
# Features in v2.0 milestone
```

**Created by You + Assigned to Others**:

```bash
/github:fetch-issues --filter=created --state=all
# Review issues you created (delegated work)
```

**All Open Issues** (large repos):

```bash
/github:fetch-issues --filter=all --limit=100
# Get overview of repository (limited to 100)
```
