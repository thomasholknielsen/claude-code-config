---
description: "Captures work items into TODO.md with industry-standard TODO tagging"
argument-hint: "\"task description\""
allowed-tools: Read, Write, Edit
---

# Command: Create

## Purpose

**CRITICAL: CAPTURE ONLY - NO IMPLEMENTATION**
Captures work items and ideas into a standardized TODO.md file using industry-standard TODO tagging conventions.

**⚠️ STRICT CONSTRAINT: This command MUST NOT implement, code, or execute any tasks. It only captures task descriptions in the tasks.md file.**

## Usage

```bash
/to-do:create $ARGUMENTS
```

**Arguments**:

- `$1` (task-description): Description of the work item or task to capture (required)
- `$2` (--priority): Priority level (high|medium|low) (optional, default: medium)
- `$3` (--category): TODO category (bug|feature|refactor|docs|test) (optional)
- `$4` (--due-date): Due date in YYYY-MM-DD format (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "Fix login validation error"` - Basic TODO creation
- `$ARGUMENTS = "Add user profile page --priority=high --category=feature"` - High-priority feature TODO
- `$ARGUMENTS = "Update API documentation --category=docs --due-date=2024-12-01"` - Documentation TODO with deadline

## Process

**FORBIDDEN ACTIONS**: Writing code, implementing features, executing tasks, creating files other than tasks.md, making code changes

**ALLOWED ACTIONS ONLY**:

1. **ENFORCE LOCATION CONSTRAINT**: Ensure TODO file is located at `{project_root}/.claude/.todos/TODO.md` only
2. Read existing {project_root}/.claude/.todos/TODO.md (create directory structure if doesn't exist)
3. Parse input and clarify TODO description for readability
4. Parse $ARGUMENTS for task description, priority, category, and due date
5. Add new TODO entry using industry-standard tagging format with parsed metadata
6. Save updated {project_root}/.claude/.todos/TODO.md file
7. **STOP IMMEDIATELY** - No further actions permitted

**⚠️ LOCATION CONSTRAINT**: TODOs MUST ONLY be created in `{project_root}/.claude/.todos/TODO.md`. Reject any attempts to create TODO files in other locations.

## Agent Integration

- **Specialist Options**: documenter specialist can be spawned to handle task capture and file management

## Examples

```bash

## Output
- Updated {project_root}/.claude/.todos/TODO.md with new TODO entry
- Confirmation of TODO captured with proper tagging
- Brief clarification of TODO description if modified
- Location validation confirmation

## Integration Points
- **Follows**: Idea generation, bug discovery, technical debt identification
- **Followed by**: /to-do:fix-items (for TODO resolution)
- **Related**: /to-do:find-comments (for existing TODO discovery)

## Quality Standards
- TODOs remain very close to original input
- No breakdown, acceptance criteria, or detailed planning added
- Clear, actionable TODO titles
- Consistent industry-standard tagging
- Proper categorization by type and priority
- ISO date format for timestamps
