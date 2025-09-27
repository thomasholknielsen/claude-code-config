---
description: "Locate all TODO comments and unfinished work markers in the codebase"
category: "to-do"
agent: "task-orchestrator"
tools: ["Grep", "Read", "Write"]
complexity: "simple"
---

# Command: Find Comments

## Purpose

Executes to-do operations for find comments functionality.

## Usage

```bash
/to-do:find-comments [arguments]
```yaml

**Arguments**: Optional parameters specific to the operation

## Process

1. Search for TODO comments in codebase using Grep
2. **ENFORCE LOCATION CONSTRAINT**: Report findings to `{project_root}/.claude/.todos/TODO.md` only
3. Analyze found TODOs and requirements
4. Update consolidated TODO file with findings
5. Validate results and provide feedback

**⚠️ LOCATION CONSTRAINT**: All TODO consolidation MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Primary Agent**: code-writer - Handles to-do operations and coordination

## Examples

```bash
