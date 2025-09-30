---
description: "Analyze recent operations and create contextual TODO comments in code"
argument-hint: "[arguments]"
category: "to-do"
tools: ["SlashCommand", "Write", "Read"]
complexity: "moderate"
---

# Command: Create List

## Purpose

Executes to-do operations for create list functionality.

## Usage

```bash
/to-do:create-list $ARGUMENTS
```

**Arguments**:

- `$1` (context): Context for TODO creation (recent-operations, git-changes, manual) (optional, default: recent-operations)
- `$2` (--limit): Maximum number of TODOs to create (optional)
- `$3` (--priority): Default priority for created TODOs (high|medium|low) (optional, default: medium)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "git-changes --priority=high"` - Create high-priority TODOs from recent Git changes
- `$ARGUMENTS = "recent-operations --limit=10"` - Create up to 10 TODOs from recent operations
- `$ARGUMENTS = "manual"` - Manual TODO creation mode

## Process

1. **ENFORCE LOCATION CONSTRAINT**: Validate TODO file location is `{project_root}/.claude/.todos/TODO.md`
2. Parse $ARGUMENTS for context source and creation parameters
3. Analyze recent operations or changes based on specified context
4. Generate contextual TODO items with appropriate priorities
5. Execute the to-do operation using only approved location
6. Add generated TODOs to TODO.md with proper categorization
7. Validate results and provide feedback
8. Update relevant documentation or state

**⚠️ LOCATION CONSTRAINT**: All TODO operations MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Specialist Options**: task-analysis-specialist can be spawned to handle to-do operations and coordination

## Examples

```bash
