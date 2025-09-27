---
description: "Captures work items into TODO.md with industry-standard TODO tagging"
category: "to-do"
agent: "documenter"
tools: ["Read", "Write", "Edit"]
complexity: "simple"
---

# Command: Create TODO

## Purpose
**CRITICAL: CAPTURE ONLY - NO IMPLEMENTATION**
Captures work items and ideas into a standardized TODO.md file using industry-standard TODO tagging conventions.

**⚠️ STRICT CONSTRAINT: This command MUST NOT implement, code, or execute any tasks. It only captures task descriptions in the tasks.md file.**

## Usage
```
/to-do:create "task description"
```

**Arguments**: Description of the work item or task to capture

## Process
**FORBIDDEN ACTIONS**: Writing code, implementing features, executing tasks, creating files other than tasks.md, making code changes

**ALLOWED ACTIONS ONLY**:
1. Read existing TODO.md (create if doesn't exist)
2. Parse input and clarify TODO description for readability
3. Add new TODO entry using industry-standard tagging format
4. Save updated TODO.md file
5. **STOP IMMEDIATELY** - No further actions permitted

## Agent Integration
- **Primary Agent**: documenter - Handles task capture and file management

## Examples
```bash
# Capture feature idea
/to-do:create "Add user authentication to login page"

# Capture bug report
/to-do:create "Fix broken search functionality in header"

# Capture technical debt
/to-do:create "Refactor payment processing module"
```

## Output
- Updated TODO.md with new TODO entry
- Confirmation of TODO captured with proper tagging
- Brief clarification of TODO description if modified

## Integration Points
- **Follows**: Idea generation, bug discovery, technical debt identification
- **Followed by**: /to-do:fix-items (for TODO resolution)
- **Related**: /to-do:find-comments (for existing TODO discovery)

## TODO Template Format
Each TODO entry follows industry-standard format:
```markdown
## TODO: {Clarified Title}
**Priority**: [HIGH|MEDIUM|LOW]
**Type**: [FEATURE|BUG|REFACTOR|DOCS|SECURITY|PERFORMANCE]
**Added**: {ISO Date}
**Author**: {GitHub Username or Name}
**Original**: "{Original input text}"
**Description**: {Clarified version if modified}

**Tags**: #TODO #type #priority

---
```

## Quality Standards
- TODOs remain very close to original input
- No breakdown, acceptance criteria, or detailed planning added
- Clear, actionable TODO titles
- Consistent industry-standard tagging
- Proper categorization by type and priority
- ISO date format for timestamps

## CRITICAL ENFORCEMENT
**⚠️ VIOLATION ALERT**: If this command performs ANY implementation work, it is a CRITICAL ERROR.
**✅ SUCCESS CRITERIA**: Command completes by only updating TODO.md file and nothing else.
**🚫 FAILURE INDICATORS**: Creating code files, modifying existing code, running other commands, implementing features.