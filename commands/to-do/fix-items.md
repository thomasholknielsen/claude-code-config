---
description: "Systematically find and resolve TODO comments in codebase with intelligent understanding"
category: "to-do"
agent: "task-orchestrator"
tools: ["SlashCommand", "Read", "Write"]
complexity: "moderate"
---

# Command: Fix Items

## Purpose

Executes to-do operations for fix items functionality.

## Usage

```bash
/to-do:fix-items [arguments]
```python

**Arguments**: Optional parameters specific to the operation

## Process

1. **ENFORCE LOCATION CONSTRAINT**: Work only with TODOs from `{project_root}/.claude/.todos/TODO.md`
2. Analyze the current state and requirements
3. Execute the to-do operation using only approved location
4. Validate results and provide feedback
5. Update relevant documentation or state

**⚠️ LOCATION CONSTRAINT**: All TODO operations MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Primary Agent**: code-writer - Handles to-do operations and coordination

## Examples

```bash
