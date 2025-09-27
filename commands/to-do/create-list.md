---
description: "Analyze recent operations and create contextual TODO comments in code"
category: "to-do"
agent: "task-orchestrator"
tools: ["SlashCommand", "Write", "Read"]
complexity: "moderate"
---

# Command: Create List

## Purpose

Executes to-do operations for create list functionality.

## Usage

```bash
/to-do:create-list [arguments]
```yaml

**Arguments**: Optional parameters specific to the operation

## Process

1. **ENFORCE LOCATION CONSTRAINT**: Validate TODO file location is `{project_root}/.claude/.todos/TODO.md`
2. Analyze the current state and requirements
3. Execute the to-do operation using only approved location
4. Validate results and provide feedback
5. Update relevant documentation or state

**⚠️ LOCATION CONSTRAINT**: All TODO operations MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Primary Agent**: code-writer - Handles to-do operations and coordination

## Examples

```bash
