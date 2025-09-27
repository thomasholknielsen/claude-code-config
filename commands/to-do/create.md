---
description: "Captures work items into TODO.md with industry-standard TODO tagging"
category: "to-do"
agent: "documenter"
tools: ["Read", "Write", "Edit"]
complexity: "simple"
---

# Command: Create

## Purpose

**CRITICAL: CAPTURE ONLY - NO IMPLEMENTATION**
Captures work items and ideas into a standardized TODO.md file using industry-standard TODO tagging conventions.

**⚠️ STRICT CONSTRAINT: This command MUST NOT implement, code, or execute any tasks. It only captures task descriptions in the tasks.md file.**

## Usage

```bash
/to-do:create "task description"
```yaml

**Arguments**: Description of the work item or task to capture

## Process

**FORBIDDEN ACTIONS**: Writing code, implementing features, executing tasks, creating files other than tasks.md, making code changes

**ALLOWED ACTIONS ONLY**:

1. **ENFORCE LOCATION CONSTRAINT**: Ensure TODO file is located at `{project_root}/.claude/.todos/TODO.md` only
2. Read existing .claude/.todos/TODO.md (create directory structure if doesn't exist)
3. Parse input and clarify TODO description for readability
4. Add new TODO entry using industry-standard tagging format
5. Save updated .claude/.todos/TODO.md file
6. **STOP IMMEDIATELY** - No further actions permitted

**⚠️ LOCATION CONSTRAINT**: TODOs MUST ONLY be created in `{project_root}/.claude/.todos/TODO.md`. Reject any attempts to create TODO files in other locations.

## Agent Integration

- **Primary Agent**: documenter - Handles task capture and file management

## Examples

```bash

## Output
- Updated .claude/.todos/TODO.md with new TODO entry
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
