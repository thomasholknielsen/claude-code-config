---
description: "Move completed tasks to archive file for cleanup"
argument-hint: "[--completed-before=date]"
allowed-tools: Read, Write, Edit, mcp__sequential-thinking__sequentialthinking
---

# Command: Task Archive

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Archive completed tasks from tasks.md to tasks-archive.md.

**YOU MUST:**
1. ✓ Parse optional --completed-before date filter
2. ✓ Read tasks.md and find all completed tasks
3. ✓ Filter by date if specified
4. ✓ Move tasks to tasks-archive.md with Archived timestamp
5. ✓ Remove completed tasks from tasks.md
6. ✓ Report summary with task count and IDs

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Archive tasks without removing from active tasks.md
- ✗ Skip the summary report

---

## IMPLEMENTATION FLOW

### Step 1: Parse Arguments
Extract optional --completed-before date filter (YYYY-MM-DD or relative: 7d, 30d)

### Step 2: Read Active Tasks
Load tasks.md and parse all task entries

### Step 3: Filter Completed Tasks
Find tasks with **Status**: completed
Apply date filter if specified

### Step 4: Build Archive Entries
Extract task sections and add **Archived** timestamp

### Step 5: Update Files
Remove completed tasks from tasks.md
Append to tasks-archive.md with Archived timestamp

### Step 6: Report Results
Show count of archived tasks and IDs

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Move completed tasks from .agent/tasks.md to .agent/tasks-archive.md with date filtering (--completed-before: absolute YYYY-MM-DD or relative 7d/30d), preserve full task data + progress notes, add "Archived" timestamp, organize by date sections, update summary statistics

**P**urpose: Maintain clean focused active task list for current work, preserve completed work history without deletion, enable periodic cleanup (daily/weekly/sprint-end), improve tasks.md performance with fewer entries, support historical review and reflection

**E**xpectation: Completed tasks removed from tasks.md, appended to tasks-archive.md with timestamps, confirmation with count/IDs, statistics updated (total archived, by origin/category), archive organized by date, atomic operation (all or none)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% data preservation, Accuracy >90% date filtering, Relevance >85% cleanup benefit, Efficiency <5s typical archive)

## Purpose

Moves completed tasks from `.agent/tasks.md` to `.agent/tasks-archive.md` to keep the active task list clean and focused on current work.

## Usage

```bash
/task:archive $ARGUMENTS
```

**Arguments**:

- `--completed-before`: Archive tasks completed before date (optional, format: YYYY-MM-DD or relative: 7d, 30d)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - Archive all completed tasks
- `$ARGUMENTS = "--completed-before=2025-10-01"` - Archive completed before October 1st
- `$ARGUMENTS = "--completed-before=7d"` - Archive completed more than 7 days ago
- `$ARGUMENTS = "--completed-before=30d"` - Archive completed more than 30 days ago

## Process

1. **Parse Arguments**: Extract date filter if provided
2. **Read tasks.md**: Load active tasks from `.agent/tasks.md`
3. **Identify Completed**: Find tasks with status=completed
4. **Apply Date Filter**: If date provided, filter by completion date
5. **Read Archive File**: Load existing archive (create if doesn't exist)
6. **Move Tasks**: Remove from tasks.md, append to tasks-archive.md
7. **Update Counts**: Update summary statistics in both files
8. **Save Files**: Write updated tasks.md and tasks-archive.md
9. **Report Summary**: Show count of archived tasks

## Archive File Structure

`.agent/tasks-archive.md` maintains this structure:

```markdown
# Archived Tasks

**Total Archived**: 45
**Last Archive**: 2025-10-13T16:00:00Z

---

## Archive: 2025-10-13

### [TASK-001] Fix login validation error

**Status**: completed
**Priority**: high
**Category**: bug
**Origin**: adhoc
**Created**: 2025-10-05T09:00:00Z
**Completed**: 2025-10-06T10:00:00Z
**Archived**: 2025-10-13T16:00:00Z

**Description**:
Fix validation error with special characters in username field.

**Progress Notes**:
- 2025-10-05T14:30:00Z: Started investigation, found issue in regex pattern
- 2025-10-06T10:00:00Z: Fixed regex pattern and added unit tests

---

### [TASK-002] Add user profile page

**Status**: completed
**Priority**: high
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-05T10:00:00Z
**Completed**: 2025-10-12T15:30:00Z
**Archived**: 2025-10-13T16:00:00Z

**Description**:
Create user profile page with avatar upload, bio, and settings.

**Progress Notes**:
- 2025-10-06T11:00:00Z: Completed design mockups
- 2025-10-10T14:00:00Z: Implemented basic layout and avatar upload
- 2025-10-12T15:30:00Z: Completed all features, tests passing

---

## Archive: 2025-10-06

### [TASK-003] Update API documentation

...
```

## Agent Integration

- **No agents required** - Direct file operation
- **Specialist Options**: None needed for archiving

## Examples

### Example 1: Archive All Completed Tasks

```bash
/task:archive
# where $ARGUMENTS = ""

# Expected behavior:
→ Found 5 completed tasks
→ Archiving to .agent/tasks-archive.md...
→
→ Archived tasks:
→ [TASK-001] Fix login validation error
→ [TASK-005] Refactor authentication module
→ [TASK-012] Update deployment documentation
→ [TASK-018] Add unit tests for user service
→ [TASK-023] Fix database migration script
→
→ ✓ 5 tasks archived
→ ✓ Active task list cleaned
→ Archive location: .agent/tasks-archive.md
```

### Example 2: Archive Tasks Older Than 7 Days

```bash
/task:archive "--completed-before=7d"
# where $ARGUMENTS = "--completed-before=7d"

# Expected behavior:
→ Found 3 tasks completed more than 7 days ago
→ Archiving to .agent/tasks-archive.md...
→
→ Archived tasks:
→ [TASK-001] Fix login validation error (completed 8 days ago)
→ [TASK-005] Refactor authentication module (completed 10 days ago)
→ [TASK-012] Update deployment documentation (completed 15 days ago)
→
→ ✓ 3 tasks archived
→ ✓ 2 recent completed tasks remain in active list
```

### Example 3: Archive Before Specific Date

```bash
/task:archive "--completed-before=2025-10-01"
# where $ARGUMENTS = "--completed-before=2025-10-01"

# Expected behavior:
→ Found 8 tasks completed before 2025-10-01
→ Archiving to .agent/tasks-archive.md...
→
→ ✓ 8 tasks archived
→ ✓ Active task list now contains only recent completed tasks
```

### Example 4: No Completed Tasks to Archive

```bash
/task:archive
# where $ARGUMENTS = ""

# Expected behavior:
→ No completed tasks found in .agent/tasks.md
→ Nothing to archive
→
→ Suggestions:
→ - View active tasks: /task:execute
→ - Complete tasks: /task:execute TASK-XXX --status=completed
```

## Integration Points

- **Follows**: `/task:execute TASK-XXX --status=completed`
- **Followed by**: `/task:execute` (verify cleanup)
- **Related**: `/task:help` (guidance), `/task:execute` (verify before archiving)

## Quality Standards

- **Preserve Data**: All task information preserved in archive
- **Clean Removal**: Completed tasks cleanly removed from active list
- **Timestamp Addition**: Add "Archived" timestamp to each task
- **Organized Structure**: Group archived tasks by date
- **Update Counts**: Maintain accurate statistics
- **Atomic Operation**: All moves succeed or none do
- **Safe Operation**: Don't delete, only move to archive

## Output

- Count of tasks archived
- List of archived task IDs and titles
- Confirmation of archive location
- Updated task list summary
- Suggestions for next actions

## Workflow Examples

### Daily Cleanup

```bash
# End of day: Complete tasks
/task:execute TASK-001 --status=completed
/task:execute TASK-003 --status=completed

# Archive completed work
/task:archive

# Check active list is clean
/task:execute --status=pending,in-progress
```

### Weekly Maintenance

```bash
# Archive old completed tasks (keep recent ones visible)
/task:archive --completed-before=7d

# Review what's left
/task:execute --status=completed
```

### Sprint End Cleanup

```bash
# Complete all sprint tasks
/task:execute TASK-010 --status=completed
/task:execute TASK-011 --status=completed
/task:execute TASK-012 --status=completed

# Archive sprint work
/task:archive

# Verify clean slate for next sprint
/task:execute
```

### Monthly Archive

```bash
# Archive everything completed over a month ago
/task:archive --completed-before=30d

# Keep active list focused on recent work
```

## Best Practices

1. **Archive Regularly** - Keep active list clean and focused
2. **Review Before Archiving** - Use `/task:execute --status=completed` first
3. **Use Date Filters** - Archive old tasks, keep recent visible
4. **End of Sprint** - Archive completed sprint work
5. **Weekly Cleanup** - Run weekly to maintain hygiene
6. **Verify After** - Check `/task:execute` to confirm cleanup
7. **Don't Archive Too Early** - Keep recently completed tasks visible

## Archive Timing

**Immediate Archiving**:

```bash
# Archive right after completion
/task:execute TASK-001 --status=completed
/task:archive  # Archives all completed, including TASK-001
```

**Delayed Archiving** (recommended):

```bash
# Complete tasks throughout the day
/task:execute TASK-001 --status=completed
/task:execute TASK-003 --status=completed

# End of day: Review and archive
/task:execute --status=completed
/task:archive
```

**Periodic Archiving**:

```bash
# Keep recent completed tasks visible, archive old ones
/task:archive --completed-before=7d

# Or monthly cleanup
/task:archive --completed-before=30d
```

## Date Filter Formats

**Absolute Dates**:

- `2025-10-01` - Before October 1st, 2025
- `2025-09-15` - Before September 15th, 2025

**Relative Dates**:

- `7d` - More than 7 days ago
- `14d` - More than 14 days ago
- `30d` - More than 30 days ago
- `90d` - More than 90 days ago

## Archive Benefits

**Why Archive?**

1. **Clean Active List** - Focus on current work
2. **Preserve History** - Don't lose completed work
3. **Performance** - Faster list operations with fewer tasks
4. **Organization** - Historical record of completed work
5. **Reflection** - Review what was accomplished

**When to Archive**:

- End of day (completed that day)
- End of week (completed that week)
- End of sprint (completed that sprint)
- Monthly cleanup (old completed tasks)

## Retrieving Archived Tasks

**To view archived tasks**:

1. Open `.agent/tasks-archive.md`
2. Search by task ID: [TASK-XXX]
3. Search by keyword in description
4. Review by archive date section

**To "unarchive" a task** (if needed):

1. Find task in `.agent/tasks-archive.md`
2. Copy task content
3. Paste into `.agent/tasks.md`
4. Update status to `pending` or `in-progress`
5. Remove "Archived" timestamp
6. Optionally remove from archive file

## Archive Statistics

**Archive file maintains statistics**:

```markdown
# Archived Tasks

**Total Archived**: 45
**Last Archive**: 2025-10-13T16:00:00Z
**Origins**:
- adhoc: 25
- code-comment: 12
- github-issue: 8

**Categories**:
- feature: 18
- bug: 15
- refactor: 8
- docs: 4

**By Month**:
- 2025-10: 15 tasks
- 2025-09: 20 tasks
- 2025-08: 10 tasks
```

## Next Steps After Archiving

```bash
# After archiving, review active list
/task:execute

# Check pending work
/task:execute --status=pending

# Start next task
/task:execute TASK-XXX --status=in-progress

# Or add new tasks
/task:add "New task description"
```

## Error Handling

**No Completed Tasks**:

```
No completed tasks found in .agent/tasks.md
Nothing to archive

Suggestions:
- Complete some tasks: /task:execute TASK-XXX --status=completed
- View active tasks: /task:execute
```

**No Tasks Match Date Filter**:

```
No tasks found completed before 2025-10-01
Nothing to archive

Suggestions:
- Remove date filter: /task:archive
- Adjust date: /task:archive --completed-before=7d
- View completed tasks: /task:execute --status=completed
```

**Archive File Permission Error**:

```
Error: Cannot write to .agent/tasks-archive.md
Permission denied

Suggestions:
- Check file permissions
- Ensure .agent/ directory exists and is writable
```

## Archive vs Delete

**Archive (Recommended)**:

- ✅ Preserves all task information
- ✅ Maintains history
- ✅ Can be referenced later
- ✅ Safe operation

**Delete (Not Recommended)**:

- ❌ Loses task information permanently
- ❌ No history
- ❌ Cannot recover
- ❌ Risky operation

**Always archive, never delete completed tasks.**

## Archive Organization

**By Date**:

```markdown
## Archive: 2025-10-13
[Tasks completed/archived on this date]

## Archive: 2025-10-06
[Tasks completed/archived on this date]
```

**By Origin** (alternative):

```markdown
## Archived Adhoc Tasks
[All adhoc tasks]

## Archived Code Comment Tasks
[All code-comment tasks]

## Archived GitHub Issue Tasks
[All github-issue tasks]
```

**By Category** (alternative):

```markdown
## Archived Bug Fixes
[All bug fixes]

## Archived Features
[All features]
```

**Recommended**: Date-based (default) - easier to track when work was completed.
