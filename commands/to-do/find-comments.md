---
description: "Locate all TODO comments and unfinished work markers in the codebase"
argument-hint: "[arguments]"
category: "to-do"
tools: ["Grep", "Read", "Write"]
complexity: "simple"
allowed-tools: Grep, Read, Write
---

# Command: Find Comments

## Purpose

Executes to-do operations for find comments functionality.

## Usage

```bash
/to-do:find-comments $ARGUMENTS
```

**Arguments**:

- `$1` (scope): Search scope (files, directories, or patterns) (optional, default: entire project)
- `$2` (--types): TODO comment types to find (TODO, FIXME, HACK, NOTE) (optional, default: all)
- `$3` (--consolidate): Consolidate findings to TODO.md (optional, default: true)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "src/"` - Find TODO comments only in src directory
- `$ARGUMENTS = "--types=TODO,FIXME"` - Find only TODO and FIXME comments
- `$ARGUMENTS = "*.js --consolidate"` - Find in JS files and consolidate to TODO.md

## Process

1. Parse $ARGUMENTS for search scope and comment types
2. Search for TODO comments in codebase using Grep with specified filters
3. **ENFORCE LOCATION CONSTRAINT**: Report findings to `{project_root}/.claude/.todos/TODO.md` only
4. Analyze found TODOs and categorize by type and priority
5. Update consolidated TODO file with findings
6. Remove duplicate entries and organize by priority
7. Validate results and provide feedback

**⚠️ LOCATION CONSTRAINT**: All TODO consolidation MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Specialist Options**: task-analysis-specialist can be spawned to handle to-do operations and coordination

## Examples

```bash
