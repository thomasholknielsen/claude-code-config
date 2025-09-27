---
description: "Scan codebase for TODO comments and create professional GitHub issues"
category: "to-do"
agent: "task-orchestrator"
tools: ["Grep", "Bash", "Read"]
complexity: "moderate"
---

# Command: Convert To Github

## Purpose

Executes to-do operations for convert to github functionality.

## Usage

```bash
/to-do:convert-to-github [arguments]
```python

**Arguments**: Optional parameters specific to the operation

## Process

1. **ENFORCE LOCATION CONSTRAINT**: Read TODOs from `{project_root}/.claude/.todos/TODO.md` only
2. Analyze TODO items for GitHub issue conversion
3. Create professional GitHub issues using Bash/gh CLI
4. Update TODO file to mark items as converted
5. Validate results and provide feedback

**⚠️ LOCATION CONSTRAINT**: All TODO operations MUST use `{project_root}/.claude/.todos/TODO.md` location only.

## Agent Integration

- **Primary Agent**: code-writer - Handles to-do operations and coordination

## Examples

```bash
