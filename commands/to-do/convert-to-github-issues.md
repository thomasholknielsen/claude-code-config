---
description: "Scan codebase for TODO comments and create professional GitHub issues"
argument-hint: "[arguments]"
allowed-tools: Grep, Bash, Read
---

# Command: Convert To Github

## Purpose

Executes to-do operations for convert to github functionality.

## Usage

```bash
/to-do:convert-to-github $ARGUMENTS
```

**Arguments**:

- `$1` (filter): Filter TODOs to convert (priority, category, or all) (optional, default: all)
- `$2` (--labels): Default GitHub issue labels to apply (optional)
- `$3` (--milestone): GitHub milestone to assign issues (optional)
- `$4` (--assignee): Default assignee for created issues (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "high --labels=bug,urgent"` - Convert high-priority TODOs as urgent bugs
- `$ARGUMENTS = "--milestone=v2.0"` - Convert all TODOs to v2.0 milestone
- `$ARGUMENTS = "bug --assignee=@username"` - Convert bug TODOs and assign to user

## Process

1. **ENFORCE LOCATION CONSTRAINT**: Read TODOs from `{project_root}/.claude/.todos/TODO.md` only
2. Parse $ARGUMENTS for filtering and GitHub issue options
3. Filter TODO items based on specified criteria
4. Analyze filtered TODO items for GitHub issue conversion
5. Create professional GitHub issues using Bash/gh CLI with labels and assignments
6. Update TODO file to mark items as converted with issue links
7. Validate results and provide feedback with issue URLs

**⚠️ LOCATION CONSTRAINT**: All TODO operations MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Specialist Options**: task-analysis-specialist can be spawned to handle to-do operations and coordination

## Examples

```bash
