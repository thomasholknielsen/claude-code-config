---
description: "Create GitHub issue from task with proper labeling and linking"
argument-hint: "TASK-XXX [--labels=label1,label2] [--milestone=name] [--assignee=user]"
allowed-tools: Read, Edit, Bash(gh:*), mcp__sequential-thinking__sequentialthinking
---

# Command: GitHub Create Issue From Task

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Create GitHub issue from task with proper labeling and linking.

**YOU MUST:**
1. ✓ Parse TASK-XXX from $ARGUMENTS
2. ✓ Read task details from .agent/tasks.md
3. ✓ Format issue (title, body with metadata)
4. ✓ Apply labels (explicit + auto-inferred)
5. ✓ Create issue via gh CLI
6. ✓ Update task with GitHub URL

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Fail to update task with URL
- ✗ Skip label application

---

## IMPLEMENTATION FLOW

### Step 1: Parse Task ID
Extract TASK-XXX from $ARGUMENTS

### Step 2: Read Task Details
Load from .agent/tasks.md

### Step 3: Format Issue
Create title and body with metadata

### Step 4: Apply Labels
Add explicit + auto-inferred labels

### Step 5: Create Issue
Execute gh issue create

### Step 6: Update Task
Link task to GitHub issue URL

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create GitHub issues from tasks in .agent/tasks.md via gh CLI, read task details (TASK-XXX), format issue (title, body with metadata/description/progress notes), apply labels (explicit --labels + auto-inferred --auto-labels from category/priority/origin), create issue, update task with GitHub URL

**P**urpose: Share local tasks with team via GitHub issues, support collaboration workflows (local work → create issue for visibility), maintain bidirectional links (task ↔ issue), enable batch creation (multiple TASK-IDs)

**E**xpectation: GitHub issues created with task context, task updated with issue URL (#XXX and full URL), labels applied (explicit + auto-inferred), milestone/assignee set, issue creation summary with URLs

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% task details, Accuracy >90% label mapping, Relevance >85% context preservation, Efficiency <10s per issue)

## Purpose

Creates GitHub issues from tasks in `.agent/tasks.md` using the `gh` CLI, preserving task details and establishing bidirectional links.

## Usage

```bash
/github:create-issue-from-task $ARGUMENTS
```

**Arguments**:

- `$1` (task-ids): One or more task IDs (required, space-separated or comma-separated)
- `--labels`: GitHub labels to apply (optional, comma-separated)
- `--milestone`: Milestone name (optional)
- `--assignee`: GitHub username to assign (optional, default: current user)
- `--auto-labels`: Automatically infer labels from task category and origin (optional flag)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "TASK-001"` - Create issue from single task
- `$ARGUMENTS = "TASK-001 TASK-002 TASK-003"` - Create issues from multiple tasks
- `$ARGUMENTS = "TASK-001,TASK-002,TASK-003"` - Comma-separated task IDs
- `$ARGUMENTS = "TASK-001 --labels=bug,critical"` - Create with specific labels
- `$ARGUMENTS = "TASK-001 --milestone=v2.0"` - Create in milestone
- `$ARGUMENTS = "TASK-001 --assignee=@teammate"` - Assign to teammate
- `$ARGUMENTS = "TASK-001 --auto-labels"` - Auto-infer labels from task metadata
- `$ARGUMENTS = "TASK-001 --labels=priority:high --milestone=v2.1 --auto-labels"` - Combined options

## Process

1. **Parse Arguments**: Extract task IDs and options
2. **Verify gh CLI**: Ensure GitHub CLI is installed and authenticated
3. **Read tasks.md**: Load task details from `.agent/tasks.md`
4. **Find Tasks**: Locate specified tasks by ID
5. **Prepare Issue Data**: Format title, body, labels
6. **Auto-Label (if enabled)**: Infer labels from category and origin
7. **Create Issues**: Execute `gh issue create` for each task
8. **Update Tasks**: Add GitHub issue link to task metadata
9. **Report Success**: Show created issue URLs and numbers

## Label Inference

**Auto-Labels from Category**:

- `bug` → `bug`
- `feature` → `enhancement`, `feature`
- `refactor` → `tech-debt`, `refactor`
- `docs` → `documentation`
- `test` → `testing`
- `research` → `research`
- `chore` → `maintenance`, `chore`

**Auto-Labels from Origin**:

- `code-comment` → `tech-debt` (if not already added)
- `adhoc` → No additional label
- `github-issue` → Skip (already has GitHub issue)

**Auto-Labels from Priority**:

- `critical` → `priority:critical`, `urgent`
- `high` → `priority:high`
- `medium` → No priority label (default)
- `low` → `priority:low`

## Issue Format

**Title**: Task title (without TASK-ID prefix)

**Body Template**:

```markdown
## Description

{Task description}

## Metadata

- **Task ID**: TASK-XXX
- **Priority**: {priority}
- **Category**: {category}
- **Origin**: {origin}
- **Created**: {created date}

## Source Information

{For code-comment tasks:}
- **Source File**: {file:line}
- **Code Context**:
```{language}
{code snippet}
```

{For adhoc tasks:}

- **Captured**: {date}
- **Local Task**: .agent/tasks.md#TASK-XXX

## Progress Notes

{If progress notes exist:}

- {timestamp}: {note}
- {timestamp}: {note}

---

*Created from local task TASK-XXX via Claude Code task management*

```

## Agent Integration

- **No agents required** - Direct gh CLI operation
- **Specialist Options**: None needed for issue creation

## Examples

### Example 1: Create Issue from Single Task

```bash
/github:create-issue-from-task "TASK-001"
# where $ARGUMENTS = "TASK-001"

# Expected behavior:
→ Creating GitHub issue from TASK-001...
→ Issue created: #145 - Fix login validation error
→ URL: https://github.com/org/repo/issues/145
→ Updated TASK-001 with GitHub issue link
```

### Example 2: Create Issues from Multiple Tasks

```bash
/github:create-issue-from-task "TASK-001 TASK-002 TASK-003"
# where $ARGUMENTS = "TASK-001 TASK-002 TASK-003"

# Expected behavior:
→ Creating 3 GitHub issues...
→ #145 - Fix login validation error (TASK-001)
→ #146 - Add user profile page (TASK-002)
→ #147 - Refactor authentication module (TASK-003)
→ All tasks updated with issue links
```

### Example 3: Create with Specific Labels

```bash
/github:create-issue-from-task "TASK-001 --labels=bug,critical,security"
# where $ARGUMENTS = "TASK-001 --labels=bug,critical,security"

# Expected behavior:
→ Creating GitHub issue with labels: bug, critical, security
→ Issue created: #145 - Fix login validation error
→ Labels applied: bug, critical, security
→ URL: https://github.com/org/repo/issues/145
```

### Example 4: Create in Milestone

```bash
/github:create-issue-from-task "TASK-002 --milestone=v2.0"
# where $ARGUMENTS = "TASK-002 --milestone=v2.0"

# Expected behavior:
→ Creating GitHub issue in milestone v2.0...
→ Issue created: #146 - Add user profile page
→ Milestone: v2.0
→ URL: https://github.com/org/repo/issues/146
```

### Example 5: Create with Auto-Labels

```bash
/github:create-issue-from-task "TASK-003 --auto-labels"
# where $ARGUMENTS = "TASK-003 --auto-labels"
# Assuming TASK-003 is category=refactor, priority=high, origin=code-comment

# Expected behavior:
→ Creating GitHub issue with auto-inferred labels...
→ Inferred labels: tech-debt, refactor, priority:high
→ Issue created: #147 - Refactor authentication module
→ Labels applied: tech-debt, refactor, priority:high
→ URL: https://github.com/org/repo/issues/147
```

### Example 6: Create and Assign to Teammate

```bash
/github:create-issue-from-task "TASK-004 --assignee=@teammate --labels=feature --milestone=v2.1"
# where $ARGUMENTS = "TASK-004 --assignee=@teammate --labels=feature --milestone=v2.1"

# Expected behavior:
→ Creating GitHub issue assigned to @teammate...
→ Issue created: #148 - Add OAuth integration
→ Assigned to: @teammate
→ Labels: feature
→ Milestone: v2.1
→ URL: https://github.com/org/repo/issues/148
```

## Updated Task Format

**Before Creating Issue**:

```markdown
## [TASK-001] Fix login validation error

**Status**: pending
**Priority**: high
**Category**: bug
**Origin**: adhoc
**Created**: 2025-10-13T10:00:00Z

**Description**:
Fix validation error with special characters in username field.

---
```

**After Creating Issue**:

```markdown
## [TASK-001] Fix login validation error

**Status**: pending
**Priority**: high
**Category**: bug
**Origin**: adhoc
**Created**: 2025-10-13T10:00:00Z
**GitHub Issue**: #145 - https://github.com/org/repo/issues/145

**Description**:
Fix validation error with special characters in username field.

**GitHub Details**:
- Issue Number: #145
- Created: 2025-10-13T16:30:00Z
- URL: https://github.com/org/repo/issues/145

---
```

## Integration Points

- **Follows**: `/task:add`, `/task:scan-project --consolidate`, `/github:convert-issues-to-tasks`
- **Followed by**: Manual GitHub updates, team collaboration
- **Related**: `/github:fetch-issues`, `/task:execute`

## Quality Standards

- **Preserve Context**: Include all task details in issue
- **Bidirectional Links**: Update task with issue URL
- **Rich Formatting**: Use markdown in issue body
- **Label Consistency**: Map categories to appropriate labels
- **Source Tracking**: Include file location for code-comment tasks
- **Progress History**: Include progress notes if available

## Output

- Created GitHub issue URLs
- Issue numbers
- Applied labels and milestone
- Confirmation of task updates
- Summary of created issues

## Workflow Examples

### Share Local Work with Team

```bash
# Work on adhoc task locally
/task:add "Fix critical security vulnerability --priority=critical --category=bug"
/task:execute TASK-001  # Auto-sets to in-progress
/task:execute TASK-001 --notes="Found SQL injection in user input"
/task:execute TASK-001 --complete

# Share with team via GitHub issue
/github:create-issue-from-task TASK-001 --labels=security,critical,bug --milestone=hotfix
```

### Convert Code Comments to Team Backlog

```bash
# Scan codebase for technical debt
/task:scan-project --types=TODO,HACK --consolidate

# Review code comment tasks using interactive triaging
/task:execute

# Create GitHub issues for team visibility
/github:create-issue-from-task TASK-010 TASK-011 TASK-012 --auto-labels --milestone=tech-debt-sprint
```

### Sprint Planning Export

```bash
# Create tasks during planning
/task:add "Implement user registration --priority=high --category=feature"
/task:add "Add password reset flow --priority=high --category=feature"
/task:add "Update user documentation --priority=medium --category=docs"

# Export to GitHub for team tracking
/github:create-issue-from-task TASK-001 TASK-002 TASK-003 --milestone=sprint-5 --auto-labels
```

### Bug Discovery and Reporting

```bash
# Capture bug during development
/task:add "Race condition in checkout process --priority=critical --category=bug"
/task:execute TASK-001 --notes="Occurs under high concurrent load"

# Create GitHub issue for team awareness
/github:create-issue-from-task TASK-001 --labels=bug,critical,p0 --assignee=@team-lead
```

## Best Practices

1. **Review Before Creating** - Use `/task:execute TASK-XXX` to verify details
2. **Use Auto-Labels** - Save time with `--auto-labels` flag
3. **Set Milestones** - Organize issues by sprint/release
4. **Assign Appropriately** - Assign to responsible team member
5. **Batch Create** - Create multiple issues at once
6. **Include Context** - Ensure task has good description before creating
7. **Track Locally First** - Work on tasks locally, create issues when ready

## Label Strategy

**Explicit Labels** (manual):

```bash
/github:create TASK-001 --labels=bug,critical,security
```

**Auto Labels** (inferred):

```bash
/github:create TASK-001 --auto-labels
# Infers from category, priority, origin
```

**Combined** (best of both):

```bash
/github:create TASK-001 --labels=security --auto-labels
# Explicit 'security' + auto-inferred 'bug', 'priority:high'
```

## GitHub CLI Requirements

**Prerequisites**:

1. Install GitHub CLI: `brew install gh`
2. Authenticate: `gh auth login`
3. Verify: `gh auth status`

**Required Permissions**:

- Create issues
- Add labels
- Set milestones
- Assign issues

## Manual vs Automated Sync

**This Command (Manual)**:

- ✅ Creates GitHub issue from task
- ✅ Updates task with issue link
- ❌ Does NOT sync status updates
- ❌ Does NOT sync comment updates

**Why Manual?**:

1. **Control** - Decide when to share with team
2. **Privacy** - Work locally before making public
3. **Flexibility** - Update GitHub independently
4. **No Surprises** - Explicit sharing action

**Status Sync Pattern**:

```bash
# Local work
/task:execute TASK-001  # Auto-sets to in-progress
/task:execute TASK-001 --notes="Making progress"

# Create issue
/github:create-issue-from-task TASK-001

# Manual GitHub update (when appropriate)
# Comment on issue: "Work in progress, see commit abc123"
# Update issue status manually
```

## Next Steps After Creating

```bash
# After creating issues:

# View GitHub issue in browser
# https://github.com/org/repo/issues/145

# Continue working on task locally
/task:execute TASK-001

# Team can now see and comment on issue
# You can reference issue in commits: "Fix #145"

# Complete task locally
/task:execute TASK-001 --complete

# Optionally close GitHub issue
# (or let it close automatically via commit reference)
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

**Task Not Found**:

```
Error: Task TASK-999 not found in .agent/tasks.md
Check task ID: /task:execute
```

**Already Has GitHub Issue**:

```
Warning: TASK-001 already has GitHub issue #145
Skipping creation to avoid duplicates
URL: https://github.com/org/repo/issues/145
```

**Invalid Milestone**:

```
Error: Milestone 'v99.0' not found
Check available milestones: gh api repos/:owner/:repo/milestones
```

**Invalid Assignee**:

```
Error: User @invalid-user not found
Check username and try again
```

## Issue Creation Confirmation

**Success Output**:

```markdown
# GitHub Issue Creation Summary

✓ Created 3 issues successfully

## Created Issues

### TASK-001 → Issue #145
- **Title**: Fix login validation error
- **URL**: https://github.com/org/repo/issues/145
- **Labels**: bug, priority:high
- **Milestone**: v2.0
- **Status**: Task updated with issue link

### TASK-002 → Issue #146
- **Title**: Add user profile page
- **URL**: https://github.com/org/repo/issues/146
- **Labels**: feature, enhancement
- **Milestone**: v2.0
- **Status**: Task updated with issue link

### TASK-003 → Issue #147
- **Title**: Refactor authentication module
- **URL**: https://github.com/org/repo/issues/147
- **Labels**: tech-debt, refactor
- **Milestone**: v2.1
- **Status**: Task updated with issue link

## Next Steps

- View issues on GitHub
- Team can now see and comment
- Reference issues in commits: "Fix #145"
- Continue working on tasks locally
```

## Skipping Issues

**Tasks with Existing Issues**:

If task already has GitHub issue link, skip creation:

```
Warning: TASK-001 already has GitHub issue #145
Skipping creation to avoid duplicate

Continuing with remaining tasks...
```

**GitHub Origin Tasks**:

Tasks with `origin=github-issue` already have issues, skip:

```
Info: TASK-005 originated from GitHub issue #125
Skipping creation (already exists)

Continuing with remaining tasks...
```

## Bulk Creation

**Batch by Origin**:

```bash
# Create issues for all code comment tasks
/task:execute  # Review via interactive triaging
/github:create-issue-from-task TASK-010 TASK-011 TASK-012 TASK-013 --auto-labels --milestone=tech-debt

# Create issues for all adhoc high-priority
/task:execute  # Use triaging to filter for high-priority adhoc
/github:create-issue-from-task TASK-001 TASK-003 TASK-007 --auto-labels
```

**Batch by Category**:

```bash
# Create issues for all bugs
/task:execute  # Use triaging to filter for bugs
/github:create-issue-from-task TASK-020 TASK-021 TASK-022 --labels=bug --milestone=bug-fix-sprint
```
