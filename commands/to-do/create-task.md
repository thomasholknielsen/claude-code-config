---
description: "Captures work items into .specify/tasks.md with standardized lightweight entries"
category: "to-do"
agent: "documenter"
tools: ["Read", "Write", "Edit"]
complexity: "simple"
---

# Command: Create Task

## Purpose
Captures random work items and ideas into a standardized task list in .specify/tasks.md for later planning and breakdown.

## Usage
```
/to-do:create-task "task description"
```

**Arguments**: Description of the work item or task to capture

## Process
1. Read existing .specify/tasks.md (create if doesn't exist)
2. Parse input and clarify task description for readability
3. Add new task entry using standardized lightweight template
4. Save updated tasks.md file

## Agent Integration
- **Primary Agent**: documenter - Handles task capture and file management

## Examples
```bash
# Capture feature idea
/to-do:create-task "Add user authentication to login page"

# Capture bug report
/to-do:create-task "Fix broken search functionality in header"

# Capture technical debt
/to-do:create-task "Refactor payment processing module"
```

## Output
- Updated .specify/tasks.md with new task entry
- Confirmation of task captured with assigned ID
- Brief clarification of task description if modified

## Integration Points
- **Follows**: Idea generation, bug discovery, technical debt identification
- **Followed by**: /spec-kit:plan (for planning breakdown)
- **Related**: /spec-kit:tasks (for detailed task planning)

## Task Template Format
Each task entry follows this lightweight format:
```markdown
## Task #{ID}: {Clarified Title}
**Status**: Captured
**Added**: {Date}
**Original**: "{Original input text}"
**Description**: {Clarified version if modified}

---
```

## Quality Standards
- Tasks remain very close to original input
- No breakdown, acceptance criteria, or detailed planning added
- Clear, actionable task titles
- Consistent numbering and dating
- Simple status tracking (Captured → Planning → In Progress → Done)

## Constraints
**CRITICAL: This is a CAPTURE-ONLY command**
- **Allowed**: Only updating .specify/tasks.md with new task entries
- **Forbidden**: ANY implementation, code writing, feature development, or execution of captured tasks
- **Success**: Command completes by only modifying tasks.md
- **Failure**: Creating/modifying any code files or implementing features