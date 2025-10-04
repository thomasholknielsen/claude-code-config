---
description: "Systematically find and resolve TODO comments in codebase with intelligent understanding"
argument-hint: "[arguments]"
category: "to-do"
tools: ["SlashCommand", "Read", "Write"]
complexity: "moderate"
allowed-tools: SlashCommand, Read, Write
---

# Command: Fix Items

## Purpose

Executes to-do operations for fix items functionality.

## Usage

```bash
/to-do:fix-items $ARGUMENTS
```

**Arguments**:

- `$1` (priority): Priority level to fix (high|medium|low|all) (optional, default: all)
- `$2` (--limit): Maximum number of items to fix (optional)
- `$3` (--category): Specific TODO category to fix (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "high --limit=5"` - Fix top 5 high-priority TODOs
- `$ARGUMENTS = "--category=bug"` - Fix only bug-related TODOs
- `$ARGUMENTS = "medium"` - Fix all medium-priority TODOs

## Process

1. **ENFORCE LOCATION CONSTRAINT**: Work only with TODOs from `{project_root}/.claude/.todos/TODO.md`
2. Parse $ARGUMENTS for priority level and filtering options
3. Analyze the current TODO state and requirements based on filters
4. Execute the to-do operation using only approved location
5. Systematically resolve filtered TODO items
6. Update TODO.md with completion status
7. Validate results and provide feedback

**⚠️ LOCATION CONSTRAINT**: All TODO operations MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Specialist Options**: task-analysis-specialist can be spawned to handle to-do operations and coordination

## Examples

```bash
