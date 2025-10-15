---
description: "Convert GitHub issues to tasks with origin tagging for local tracking"
argument-hint: "[--source-file=path] [--filter=\"query\"] [--milestone=name] [--label=name]"
allowed-tools: Read, Write, Edit, Bash(gh:*), mcp__sequential-thinking__sequentialthinking
---

# Command: GitHub Convert Issues To Tasks

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Convert GitHub issues to tasks in .agent/tasks.md with origin=github-issue, load issues from file (--source-file) OR fetch with filters (--filter/--milestone/--label), deduplicate against existing tasks, map metadata (labels → priority/category), save tasks with GitHub links

**P**urpose: Enable local task management of GitHub issues with independent status tracking, support sprint planning workflows (fetch → review → import selectively), maintain bidirectional GitHub links without automatic sync

**E**xpectation: New tasks in .agent/tasks.md with origin=github-issue, inferred priority/category from labels (critical/high/medium, bug/feature/refactor), GitHub issue URL preserved, deduplication complete, import summary with counts

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% issue data, Accuracy >90% label mapping, Relevance >85% selected issues, Efficiency <15s import)

## Purpose

Converts GitHub issues into trackable tasks in `.agent/tasks.md` with origin `github-issue`, enabling local task management while maintaining GitHub issue links.

## Usage

```bash
/github:convert-issues-to-tasks $ARGUMENTS
```

**Arguments**:

- `--source-file`: Path to fetched issues file from `/github:fetch-issues` (optional)
- `--filter`: GitHub search query (optional, e.g., "milestone:v2.0 AND label:bug")
- `--milestone`: Filter by milestone name (optional)
- `--label`: Filter by label(s) (optional, comma-separated)
- `--limit`: Max number of issues to import (optional, default: 50)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "--source-file=.agent/github-issues.md"` - Import from fetched file
- `$ARGUMENTS = "--filter=\"milestone:v2.0 AND label:bug\""` - Import matching issues
- `$ARGUMENTS = "--milestone=v2.0"` - Import all v2.0 milestone issues
- `$ARGUMENTS = "--label=bug,critical"` - Import critical bugs
- `$ARGUMENTS = "--milestone=sprint-5 --label=feature"` - Combined filters
- `$ARGUMENTS = ""` - Import all assigned open issues (default behavior)

## Process

1. **Parse Arguments**: Extract source file or filters
2. **Load Issues**: Read from file OR fetch with filters
3. **Deduplicate**: Check if issue already exists as task
4. **Convert to Tasks**: Create task entries with origin=github-issue
5. **Map Metadata**: Convert GitHub labels to priority/category
6. **Add GitHub Link**: Include issue URL in task
7. **Save to tasks.md**: Append new tasks
8. **Report Summary**: Show count and task IDs

## Metadata Mapping

**Priority Inference from Labels**:

- Labels `critical`, `urgent`, `p0` → `priority: critical`
- Labels `high-priority`, `p1` → `priority: high`
- Labels `medium-priority`, `p2` → `priority: medium`
- Labels `low-priority`, `p3` → `priority: low`
- Default: `medium`

**Category Inference from Labels**:

- Labels `bug`, `defect` → `category: bug`
- Labels `feature`, `enhancement` → `category: feature`
- Labels `tech-debt`, `refactor` → `category: refactor`
- Labels `documentation`, `docs` → `category: docs`
- Labels `testing`, `test` → `category: test`
- Labels `research`, `investigation` → `category: research`
- Labels `chore`, `maintenance` → `category: chore`
- Default: `feature`

**Status Inference**:

- Open issue → `status: pending`
- In progress (has assignee + recent activity) → `status: in-progress`
- Closed issue → Skip import (unless explicitly requested)

## Task Format for GitHub Issues

```markdown
## [TASK-015] Database connection leak (#125)

**Status**: pending
**Priority**: critical
**Category**: bug
**Origin**: github-issue
**GitHub Issue**: https://github.com/org/repo/issues/125
**Created**: 2025-10-13T16:00:00Z

**Description**:
Connection pool not releasing connections properly under high load, leading to connection exhaustion after several hours of operation.

**GitHub Details**:
- **Issue**: #125
- **Author**: @teammate
- **Labels**: bug, critical, p0
- **Milestone**: v2.1.0
- **Assignees**: @you, @teammate2
- **State**: open
- **Comments**: 8

**Acceptance Criteria**:
- [ ] Connection pool properly releases connections
- [ ] Handles high concurrent load
- [ ] Monitoring and alerting added

---
```

## Agent Integration

- **No agents required** - Direct import operation
- **Specialist Options**: None needed for importing

## Examples

### Example 1: Import from Fetched File

```bash
# First, fetch issues
/github:fetch-issues --milestone=v2.0

# Then import from file
/github:convert-issues-to-tasks "--source-file=.agent/github-issues.md"
# where $ARGUMENTS = "--source-file=.agent/github-issues.md"

# Expected behavior:
→ Importing from .agent/github-issues.md...
→ Found 12 issues
→ Checking for duplicates...
→ Importing 12 new issues as tasks...
→
→ Created tasks:
→ [TASK-020] Database connection leak (#125)
→ [TASK-021] Add user preferences page (#130)
→ [TASK-022] Refactor authentication middleware (#135)
→ ... (9 more)
→
→ ✓ 12 tasks added to .agent/tasks.md
→ Use /task:execute --origin=github-issue to view them
```

### Example 2: Import with Filter Query

```bash
/github:convert-issues-to-tasks "--filter=\"milestone:v2.0 AND label:bug AND priority:critical\""
# where $ARGUMENTS = "--filter=\"milestone:v2.0 AND label:bug AND priority:critical\""

# Expected behavior:
→ Fetching issues matching: milestone:v2.0 AND label:bug AND priority:critical
→ Found 3 issues
→ Importing as tasks...
→
→ Created tasks:
→ [TASK-025] Critical auth bypass (#142) - Priority: critical
→ [TASK-026] Data corruption in export (#145) - Priority: critical
→ [TASK-027] Security vulnerability in API (#148) - Priority: critical
→
→ ✓ 3 critical bugs imported
```

### Example 3: Import Milestone Issues

```bash
/github:convert-issues-to-tasks "--milestone=sprint-5"
# where $ARGUMENTS = "--milestone=sprint-5"

# Expected behavior:
→ Fetching issues for milestone: sprint-5
→ Found 18 open issues
→ Importing as tasks...
→
→ By category:
→ - Features: 10 tasks
→ - Bugs: 5 tasks
→ - Tech debt: 3 tasks
→
→ ✓ 18 tasks added for sprint-5
```

### Example 4: Import Specific Labels

```bash
/github:convert-issues-to-tasks "--label=feature,high-priority"
# where $ARGUMENTS = "--label=feature,high-priority"

# Expected behavior:
→ Fetching high-priority features...
→ Found 7 issues
→ Importing as tasks...
→
→ Created tasks:
→ [TASK-030] OAuth integration (#150) - Priority: high
→ [TASK-031] Multi-tenant support (#152) - Priority: high
→ ... (5 more)
→
→ ✓ 7 high-priority features imported
```

### Example 5: Import All Assigned Issues

```bash
/github:convert-issues-to-tasks
# where $ARGUMENTS = ""

# Expected behavior:
→ Fetching assigned open issues...
→ Found 12 issues
→ Importing as tasks...
→
→ ✓ 12 assigned issues imported
→ Use /task:execute --origin=github-issue --status=pending to start work
```

## Integration Points

- **Follows**: `/github:fetch-issues` (fetch to context first)
- **Followed by**: `/task:execute --origin=github-issue`, `/task:execute`
- **Related**: `/task:add`, `/task:scan`, `/github:create`

## Quality Standards

- **Deduplicate**: Don't import issues that already exist as tasks
- **Preserve Context**: Include all GitHub details
- **Smart Mapping**: Infer priority/category from labels
- **Bidirectional Links**: Maintain GitHub issue URL
- **Origin Tagging**: Always tag as `github-issue`
- **Rich Metadata**: Include labels, milestone, assignees

## Output

- Count of imported issues
- List of created task IDs with issue numbers
- Category/priority distribution
- Confirmation in tasks.md
- Suggestions for next steps

## Workflow Examples

### Sprint Planning Workflow

```bash
# Step 1: Fetch sprint issues for review
/github:fetch-issues --milestone=sprint-5

# Step 2: Review issues in file
# cat .agent/github-issues.md

# Step 3: Import selected issues
/github:convert-issues-to-tasks --source-file=.agent/github-issues.md

# Step 4: View imported tasks
/task:execute --origin=github-issue

# Step 5: Start working
/task:execute TASK-020 --status=in-progress
```

### Bug Triage Workflow

```bash
# Step 1: Fetch all open bugs
/github:fetch-issues --label=bug --state=open

# Step 2: Import critical and high priority
/github:convert-issues-to-tasks --filter="label:bug AND (priority:critical OR priority:high)"

# Step 3: Review and assign priorities
/task:execute --origin=github-issue --category=bug

# Step 4: Work on critical bugs first
/task:execute --priority=critical --origin=github-issue
```

### Feature Development Workflow

```bash
# Import feature issues for milestone
/github:convert-issues-to-tasks --milestone=v2.0 --label=feature

# Review features
/task:execute --origin=github-issue --category=feature

# Start working on first feature
/task:show TASK-030
/task:execute TASK-030 --status=in-progress
```

### Daily Standup Workflow

```bash
# Import today's assigned work
/github:convert-issues-to-tasks --filter="assignee:@me AND state:open"

# Check what's on your plate
/task:execute --origin=github-issue --status=pending

# Continue in-progress work
/task:execute --origin=github-issue --status=in-progress
```

## Best Practices

1. **Fetch First, Import Selectively** - Review issues before importing
2. **Use Filters** - Import only relevant issues
3. **Milestone-Based** - Organize by sprint/milestone
4. **Deduplicate** - Command handles this automatically
5. **Local Status Management** - Update task status locally
6. **Manual GitHub Sync** - Update GitHub when appropriate
7. **Archive When Done** - Use `/task:archive` for completed work

## Deduplication

**Automatic Duplicate Detection**:

- Checks GitHub issue URL in existing tasks
- Skips import if issue already exists
- Reports skipped issues

**Example Output**:

```
Found 15 issues to import
Checking for duplicates...

Duplicates (skipped):
- Issue #125 already exists as TASK-015
- Issue #130 already exists as TASK-021

Importing 13 new issues...
✓ 13 tasks added
✓ 2 duplicates skipped
```

## Filter Query Syntax

**GitHub Search Operators**:

- `milestone:v2.0` - Issues in milestone
- `label:bug` - Issues with label
- `assignee:@me` - Assigned to you
- `state:open` - Open issues
- `state:closed` - Closed issues
- `author:@username` - Created by user

**Logical Operators**:

- `AND` - Both conditions must match
- `OR` - Either condition matches
- `NOT` - Exclude condition

**Example Queries**:

```bash
# Critical bugs in milestone
--filter="milestone:v2.0 AND label:bug AND priority:critical"

# Features OR enhancements
--filter="label:feature OR label:enhancement"

# Assigned to you, not closed
--filter="assignee:@me AND NOT state:closed"

# High priority, any category
--filter="priority:high OR priority:critical"
```

## Source File vs Filters

**Use --source-file when**:

- Already fetched issues with `/github:fetch-issues`
- Want to review before importing
- Working offline or with cached data
- Multiple import operations from same fetch

**Use --filter when**:

- Direct import without pre-fetch
- Dynamic query needed
- One-time import
- Automated workflows

**Pattern 1** (Fetch → Review → Import):

```bash
/github:fetch-issues --milestone=v2.0
# Review .agent/github-issues.md
/github:convert-issues-to-tasks --source-file=.agent/github-issues.md
```

**Pattern 2** (Direct Import):

```bash
/github:convert-issues-to-tasks --milestone=v2.0 --label=feature,high-priority
```

## Next Steps After Importing

```bash
# After importing issues:

# View imported tasks
/task:execute --origin=github-issue

# Check priority distribution
/task:execute --origin=github-issue --priority=high,critical

# Start working on first task
/task:show TASK-020
/task:execute TASK-020 --status=in-progress

# Update progress locally
/task:execute TASK-020 --notes="Working on connection pool fix"

# Complete task
/task:execute TASK-020 --status=completed

# Manually update GitHub issue
# Comment: "Fix implemented in commit abc123"
# Close issue or let git reference close it
```

## GitHub CLI Requirements

**Prerequisites**:

1. Install GitHub CLI: `brew install gh`
2. Authenticate: `gh auth login`
3. Verify: `gh auth status`

**Required Permissions**:

- Read issues
- Read labels
- Read milestones

## Error Handling

**gh CLI Not Found**:

```
Error: GitHub CLI (gh) not found
Install: brew install gh
Then authenticate: gh auth login
```

**Source File Not Found**:

```
Error: Source file not found: .agent/github-issues.md

Suggestions:
- Fetch issues first: /github:fetch-issues
- Check file exists: ls .agent/github-issues.md
- Use --filter instead of --source-file
```

**No Issues Found**:

```
No issues found matching filters

Suggestions:
- Remove some filters
- Check milestone/label names
- Use /github:fetch-issues first to verify issues exist
```

**All Issues Already Imported**:

```
Found 10 issues
All issues already exist as tasks (10 duplicates)
Nothing to import

✓ No action needed
```

## Import Confirmation

**Success Output**:

```markdown
# GitHub Import Summary

✓ Imported 15 issues successfully

## Created Tasks

### By Priority
- **Critical**: 2 tasks
- **High**: 5 tasks
- **Medium**: 8 tasks

### By Category
- **Bug**: 5 tasks
- **Feature**: 7 tasks
- **Tech Debt**: 3 tasks

## Task Details

- [TASK-020] Database connection leak (#125) - Critical bug
- [TASK-021] Add user preferences page (#130) - High priority feature
- [TASK-022] Refactor authentication (#135) - Medium priority refactor
... (12 more)

## Next Steps

- View tasks: /task:execute --origin=github-issue
- Start work: /task:execute TASK-020 --status=in-progress
- Filter by priority: /task:execute --origin=github-issue --priority=critical
```

## Skipped Issues

**Already Imported**:

```
Skipped 3 duplicate issues:
- Issue #125 already exists as TASK-015
- Issue #130 already exists as TASK-021
- Issue #140 already exists as TASK-023

Imported 12 new issues
```

**Closed Issues** (by default):

```
Skipped 5 closed issues:
- Issue #100 (closed 7 days ago)
- Issue #105 (closed 14 days ago)
... (3 more)

Import closed issues explicitly with --state=closed if needed
Imported 10 open issues
```

## Advanced Filtering

**Milestone + Priority**:

```bash
/github:convert-issues-to-tasks --milestone=v2.0 --filter="priority:critical OR priority:high"
```

**Multiple Labels (AND)**:

```bash
/github:convert-issues-to-tasks --label=bug,security
# Issues with BOTH bug AND security labels
```

**Assignee Filter**:

```bash
/github:convert-issues-to-tasks --filter="assignee:@me AND milestone:sprint-5"
```

**Date-Based** (via filter):

```bash
/github:convert-issues-to-tasks --filter="created:>2025-10-01 AND label:bug"
```

## Local vs GitHub Status

**Independent Status Management**:

- Task status in `.agent/tasks.md` is local
- GitHub issue state is separate
- No automatic sync (intentional design)
- Manual sync when appropriate

**Update Pattern**:

```bash
# Local work
/task:execute TASK-020 --status=in-progress
/task:execute TASK-020 --notes="Found root cause"
/task:execute TASK-020 --status=completed

# Manual GitHub update (when ready)
# Comment on issue
# Reference in commit: "Fix #125"
# Close issue or let git reference close it
```

**Rationale**: Gives you control over when team sees updates, prevents accidental status changes, allows local experimentation.

## Import vs Fetch vs Create

**Fetch** (`/github:fetch-issues`):

- Purpose: Get issues for reference
- Output: Context file only
- No tasks created
- Quick review

**Import** (`/github:convert-issues-to-tasks`):

- Purpose: Convert issues to tasks
- Output: Tasks in tasks.md
- Origin: github-issue
- For work tracking

**Create** (`/github:create`):

- Purpose: Export tasks to GitHub
- Input: Tasks from tasks.md
- Output: New GitHub issues
- Share with team

**Workflow**:

```
GitHub Issues → Fetch (context) → Import (tasks) → Work → Update → Archive
Local Ideas → Add (tasks) → Work → Create (issues) → Team visibility
```
