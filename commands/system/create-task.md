---
description: "Captures work items into tasks.md with industry-standard task tagging"
argument-hint: "\"task description\""
allowed-tools: Read, Write, Edit
---

# Command: Create Task

## Purpose

**CRITICAL: CAPTURE ONLY - NO IMPLEMENTATION**
Captures work items and ideas into a standardized tasks.md file in the `.agent/` directory for session-based task management.

**⚠️ STRICT CONSTRAINT: This command MUST NOT implement, code, or execute any tasks. It only captures task descriptions in the tasks.md file.**

## Usage

```bash
/system:create-task $ARGUMENTS
```

**Arguments**:

- `$1` (task-description): Description of the work item or task to capture (required)
- `$2` (--priority): Priority level (high|medium|low) (optional, default: medium)
- `$3` (--category): Task category (bug|feature|refactor|docs|test|research) (optional)
- `$4` (--due-date): Due date in YYYY-MM-DD format (optional)
- `$5` (--assigned-to): Assignee or owner of task (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "Fix login validation error"` - Basic task creation
- `$ARGUMENTS = "Add user profile page --priority=high --category=feature"` - High-priority feature task
- `$ARGUMENTS = "Update API documentation --category=docs --due-date=2025-12-01"` - Documentation task with deadline
- `$ARGUMENTS = "Research authentication patterns --priority=medium --category=research --assigned-to=@me"` - Research task

## Process

**FORBIDDEN ACTIONS**: Writing code, implementing features, executing tasks, creating files other than tasks.md, making code changes

**ALLOWED ACTIONS ONLY**:

1. **ENFORCE LOCATION**: Ensure task file is located at `{project_root}/.agent/tasks.md` only
2. Read existing `{project_root}/.agent/tasks.md` (create directory structure if doesn't exist)
3. Parse input and clarify task description for readability
4. Parse $ARGUMENTS for task description, priority, category, due date, and assignee
5. Add new task entry using industry-standard tagging format with parsed metadata
6. Save updated `{project_root}/.agent/tasks.md` file
7. **STOP IMMEDIATELY** - No further actions permitted

**⚠️ LOCATION CONSTRAINT**: Tasks MUST ONLY be created in `{project_root}/.agent/tasks.md`. Reject any attempts to create task files in other locations.

## Task Format

Tasks are captured in structured markdown format:

```markdown
## [TASK-001] Fix login validation error

**Status**: pending
**Priority**: high
**Category**: bug
**Created**: 2025-10-06T10:30:00Z
**Due Date**: 2025-10-15
**Assigned To**: @username

**Description**:
Fix the validation error that occurs when users attempt to login with special characters in their username.

**Related Issues**: #125

---
```

## Agent Integration

- **Specialist Options**: quality-analyst can be spawned to help categorize and prioritize tasks

## Examples

### Basic Task Creation

```bash
# Create basic task
/system:create-task "Fix login validation error"

Result:
✓ Task captured in .agent/tasks.md
[TASK-001] Fix login validation error
- Priority: medium (default)
- Category: uncategorized
- Status: pending
```

### High-Priority Feature Task

```bash
# Create high-priority feature task
/system:create-task "Add user profile page --priority=high --category=feature"

Result:
✓ Task captured in .agent/tasks.md
[TASK-002] Add user profile page
- Priority: high
- Category: feature
- Status: pending
```

### Documentation Task with Deadline

```bash
# Create documentation task with deadline
/system:create-task "Update API documentation --category=docs --due-date=2025-12-01"

Result:
✓ Task captured in .agent/tasks.md
[TASK-003] Update API documentation
- Priority: medium
- Category: docs
- Due Date: 2025-12-01
- Status: pending
```

### Research Task with Assignee

```bash
# Create research task assigned to specific person
/system:create-task "Research authentication patterns --priority=medium --category=research --assigned-to=@username"

Result:
✓ Task captured in .agent/tasks.md
[TASK-004] Research authentication patterns
- Priority: medium
- Category: research
- Assigned To: @username
- Status: pending
```

## Task Management Workflow

**Capture Tasks**:

```bash
# During work session, capture tasks as they arise
/system:create-task "Refactor authentication module"
/system:create-task "Add unit tests for user service --priority=high"
/system:create-task "Update deployment docs --category=docs"
```

**Reference Tasks**:

```text
# Tasks are immediately available for reference
"Show me all high-priority tasks"
"What tasks are pending for authentication?"
"Update task TASK-002 to in-progress"
```

**Convert to GitHub Issues**:

```bash
# Convert captured tasks to GitHub issues when ready
/system:create-github-issue --source=markdown .agent/tasks.md
```

## Output

- Updated `{project_root}/.agent/tasks.md` with new task entry
- Confirmation of task captured with proper tagging
- Task ID assignment (auto-incremented)
- Brief clarification of task description if modified
- Location validation confirmation

## Task Structure

The `.agent/tasks.md` file maintains this structure:

```markdown
# Project Tasks

**Last Updated**: 2025-10-06T10:30:00Z
**Total Tasks**: 5
**Pending**: 3
**In Progress**: 1
**Completed**: 1

---

## [TASK-001] Fix login validation error

**Status**: completed
**Priority**: high
**Category**: bug
**Created**: 2025-10-05T09:00:00Z
**Completed**: 2025-10-06T10:00:00Z
**Assigned To**: @username

**Description**:
Fix validation error with special characters in username field.

**Related Issues**: #125

---

## [TASK-002] Add user profile page

**Status**: in-progress
**Priority**: high
**Category**: feature
**Created**: 2025-10-05T10:00:00Z
**Due Date**: 2025-10-20
**Assigned To**: @username

**Description**:
Create user profile page with avatar upload, bio, and settings.

**Progress**:

- [x] Design mockups
- [x] Create basic layout
- [ ] Implement avatar upload
- [ ] Add settings form
- [ ] Write tests

---

## [TASK-003] Update API documentation

**Status**: pending
**Priority**: medium
**Category**: docs
**Created**: 2025-10-06T10:30:00Z
**Due Date**: 2025-12-01

**Description**:
Update API documentation to reflect new authentication endpoints.

---
```

## Integration Points

**Works Well With**:

- `/system:get-github-issues` - Pull GitHub issues to create tasks
- `/system:create-github-issue` - Convert tasks to GitHub issues
- `/implement:small` - Implement specific task
- `/spec-kit:specify` - Create detailed spec from task
- `/session:start` - Tasks persist across session boundaries

**Follows Well**:

- Idea generation sessions
- Bug discovery workflows
- Technical debt identification
- Sprint planning
- Daily standup preparation

## Quality Standards

- Tasks remain very close to original input
- No breakdown, acceptance criteria, or detailed planning added (unless requested)
- Clear, actionable task titles
- Consistent industry-standard tagging
- Proper categorization by type and priority
- ISO 8601 date format for timestamps
- Auto-incrementing task IDs

## Best Practices

1. **Capture immediately** - Don't wait, capture tasks as they arise during work
2. **Keep descriptions concise** - One-line summary is sufficient
3. **Add priority when important** - Use `--priority=high` for urgent items
4. **Categorize appropriately** - Helps with filtering and organization
5. **Set due dates sparingly** - Only when there's a real deadline
6. **Review regularly** - Check `.agent/tasks.md` at start of each session
7. **Convert to issues** - Move tasks to GitHub when ready for team visibility

## Task vs GitHub Issue

**Use `/system:create-task` for**:

- Personal work items during development
- Quick capture of ideas and bugs
- Session-specific tasks
- Items not ready for team visibility
- Research and exploration tasks

**Use `/system:create-github-issue` for**:

- Team-visible work items
- Official project backlog
- Issues requiring discussion
- Work spanning multiple sessions
- Items needing milestone/label tracking

**Convert tasks to issues** when they're ready for team collaboration.

## Location Benefits

**Why `.agent/tasks.md`?**

1. **Session-scoped**: Tasks naturally associated with work sessions
2. **No global pollution**: Separate from project-wide TODO.md
3. **Git-ignored**: Personal tasks don't clutter repository
4. **Context-aware**: Claude can reference tasks throughout session
5. **Easy cleanup**: Delete old session tasks without affecting project
6. **Flexible**: Convert to GitHub issues or TODO.md when needed
