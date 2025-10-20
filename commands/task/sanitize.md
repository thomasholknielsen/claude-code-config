---
description: "Check task dependency integrity and fix inconsistencies"
argument-hint: "[--auto-fix] [--verbose]"
allowed-tools: Read, Write, Edit, mcp__sequential-thinking__sequentialthinking
---

# Command: Task Sanitize

## Purpose

Validates task dependency integrity and detects/fixes data inconsistencies:
- Orphaned dependencies (depends on deleted tasks)
- Circular dependencies (A→B→C→A)
- Status conflicts (completed tasks blocking pending work)
- Epic integrity (tasks in non-existent epics)
- Priority inversions (low priority blocking high priority)

**⚠️ STRICT CONSTRAINT: This command is READ-HEAVY. Write only with `--auto-fix` flag and user confirmation.**

## Quick Start

```bash
# Check for issues (no changes)
/task:sanitize

# Auto-fix critical issues with confirmation
/task:sanitize --auto-fix
```

## Usage

```bash
/task:sanitize [--auto-fix] [--verbose]
```

**Arguments**:

- `--auto-fix` (optional): Automatically fix detected issues after listing them
- `--verbose` (optional): Show detailed reasoning for each issue

## Process

### STEP 1: Read Tasks File

```bash
# Load .agent/tasks.md and parse all tasks
# Build dependency graph: depends_on relationships
# Extract epic assignments
```

### STEP 2: Validate Each Task

**For each task, check:**

1. **Orphaned Dependencies**
   - Does task depend on a task that doesn't exist?
   - Example: TASK-010 depends on TASK-999 (deleted)
   - Action: Flag for removal

2. **Circular Dependencies**
   - Build dependency graph
   - Detect cycles: A→B→C→A
   - Algorithm: DFS cycle detection
   - Action: Flag both directions

3. **Status Conflicts**
   - Is a completed task blocking pending work?
   - Example: TASK-030 (completed, high) blocks TASK-040 (pending, critical)
   - Action: Flag as warning (user decision to unblock)

4. **Priority Inversions**
   - Is low-priority task blocking high-priority task?
   - Example: TASK-050 (low priority) blocks TASK-060 (high priority)
   - Action: Flag as warning

5. **Epic Integrity**
   - Does task reference non-existent epic?
   - Is epic empty (no tasks)?
   - Action: Flag for review

6. **Dependency Status**
   - Are dependencies marked as deleted/non-existent?
   - Action: Flag for removal

### STEP 3: Report Issues

**Organize by severity:**

```
⚠️ Dependency Issues Found:

[CRITICAL] (must fix for integrity)
- TASK-010 depends on TASK-999 (deleted task)
- TASK-015 → TASK-020 → TASK-015 (circular dependency detected)

[WARNING] (should consider)
- TASK-030 (completed, high priority) blocks TASK-040 (pending, critical priority)
- TASK-050 (low priority) blocks TASK-060 (high priority)
- Epic "Old Project" has no tasks (cleanup?)

[INFO] (non-blocking)
- TASK-070 is blocked by 5 tasks (critical path length)
```

### STEP 4: Prompt for Action

**If issues found:**

```
Detected 4 issues:
- 2 Critical (orphaned/circular)
- 2 Warnings (status/priority conflicts)

| Option | Description |
|--------|-------------|
| A | Auto-fix all CRITICAL issues |
| B | Show detailed explanation of each issue |
| C | Manually review before fixing (interactive) |
| Skip | Exit without making changes |

Your choice: _
```

### STEP 5: Apply Fixes (if --auto-fix)

**For each CRITICAL issue:**

1. **Orphaned dependency** → Remove from Depends On list
2. **Circular dependency** → Flag for manual review (cannot auto-fix)
3. **Deleted task reference** → Remove dependency

**For each WARNING issue:**

- List but require explicit confirmation before fixing

### STEP 6: Save Changes

```bash
# Write updated tasks.md
# Report what was changed
# Summary: "Fixed X issues, flagged Y for review"
```

## Data Structures

### Task Object (minimal for sanitize)

```python
{
    "id": "TASK-001",
    "title": "Title",
    "status": "pending|in-progress|completed|deleted",
    "priority": "low|medium|high|critical",
    "epic": "Epic Name",
    "depends_on": ["TASK-015", "TASK-020"],  # List of task IDs
    "related": ["TASK-010"]
}
```

### Issue Object

```python
{
    "type": "orphaned|circular|status_conflict|priority_inversion|epic_integrity",
    "severity": "critical|warning|info",
    "task_id": "TASK-010",
    "description": "Human-readable explanation",
    "related_tasks": ["TASK-999"],
    "auto_fixable": True|False,
    "suggested_fix": "Remove TASK-999 from depends_on"
}
```

## Issue Types

### CRITICAL Issues

**Orphaned Dependencies**
- Task depends on non-existent task
- Fix: Remove dependency from Depends On list
- Auto-fixable: Yes

**Circular Dependencies**
- A→B→C→A cycle detected
- Fix: Manual review (multiple solutions possible)
- Auto-fixable: No

### WARNING Issues

**Status Conflicts**
- Completed task still has "Blocked By" entries
- Fix: Suggest unblocking dependent tasks
- Auto-fixable: No (requires manual decision)

**Priority Inversions**
- Low-priority task blocks high-priority task
- Fix: Alert user, suggest re-prioritizing
- Auto-fixable: No

**Epic Integrity**
- Task references non-existent epic
- Empty epic has no tasks
- Fix: Reassign or create epic
- Auto-fixable: Partial

## Algorithm: Circular Dependency Detection

```python
def detect_cycles(task_graph):
    """
    task_graph: Dict[task_id] -> List[dependencies]
    Returns: List[cycles] where each cycle is a list of task_ids
    """
    cycles = []

    for start_node in task_graph:
        visited = set()
        path = []

        def dfs(node):
            if node in visited:
                if node in path:
                    # Found cycle
                    cycle_start = path.index(node)
                    cycles.append(path[cycle_start:] + [node])
                return

            visited.add(node)
            path.append(node)

            for neighbor in task_graph.get(node, []):
                dfs(neighbor)

            path.pop()

    return cycles
```

## Output Format

### Issue Report

```
⚠️ Dependency Integrity Check

Scanned 32 tasks
Found 4 issues:

[CRITICAL - 2 issues]
1. TASK-010 depends on TASK-999 (deleted)
   Fix: Remove TASK-999 from TASK-010's Depends On

2. Circular dependency: TASK-015 → TASK-020 → TASK-015
   Fix: Manual review - choose which relationship to remove

[WARNING - 2 issues]
3. TASK-030 (completed, HIGH) blocks TASK-040 (pending, CRITICAL)
   Action: Consider marking TASK-040 as unblocked

4. Epic "Old Project" has 0 tasks
   Action: Delete empty epic or add tasks

Summary:
✓ 2 auto-fixable issues identified
⚠️ 2 issues require manual review
```

### After Auto-Fix

```
✓ Task Integrity Restored

Changes made:
- Removed 1 orphaned dependency (TASK-010 ← TASK-999)
- Flagged 1 circular dependency for manual review
- Updated 1 epic assignment

Status: READY FOR WORK
```

## Constraints

**ALLOWED ACTIONS**:
- Read tasks.md
- Parse dependency graphs
- Detect issues (non-destructive)
- Report findings with --auto-fix flag
- Write changes only after explicit --auto-fix confirmation

**FORBIDDEN ACTIONS**:
- Deleting tasks
- Making assumptions about fixes (must ask user)
- Modifying task descriptions
- Changing status without user approval
- Writing without --auto-fix flag

## Integration Points

- **Follows**: Task migration, bulk task creation
- **Followed by**: `/task:execute` (start working on validated tasks)
- **Related**: `/task:add` (smart inference prevents many issues)

## Examples

### Example 1: Detect and Report Issues

```bash
/task:sanitize
# Output: Lists 4 issues (critical and warnings)
# Prompts: "Fix automatically? [A] All Critical / [B] Review / [C] Skip"
```

### Example 2: Auto-Fix CRITICAL Issues

```bash
/task:sanitize --auto-fix
# Output: Automatically fixes orphaned/deleted dependencies
# Result: "Fixed 2 issues, flagged 2 for manual review"
```

### Example 3: Verbose Report

```bash
/task:sanitize --verbose
# Output: Detailed explanation of each issue with reasoning
# Shows: Task relationships, why it's an issue, suggested fixes
```

## Best Practices

1. **Run After Migration** - After moving tasks between files
2. **Run After Bulk Operations** - After `/task:add` or editing tasks
3. **Run Before Important Workflows** - Before `/task:execute` on many tasks
4. **Use --auto-fix Wisely** - Review output before fixing
5. **Monitor Epic Health** - Watch for empty epics
6. **Keep Dependency Trees Shallow** - Avoid long chains (3+ levels)

## Failure Modes

**Issue: "Could not parse tasks.md"**
- Action: Check file format, validate syntax
- Solution: Fix or restore from backup

**Issue: "Cannot detect cycle - too large"**
- Action: Task graph has >1000 nodes
- Solution: Break tasks into smaller files or simplify structure

**Issue: "Unknown epic reference"**
- Action: Task refers to epic that doesn't exist
- Solution: Create epic or reassign task
