---
description: "Quick implementation for small tasks bypassing spec-kit, using focused Agent Orchestra coordination"
category: "implement"
agent: "implementation-orchestrator"
tools: ["Task", "SlashCommand", "TodoWrite"]
complexity: "complex"
---

# Command: Small

## Purpose

Executes implement operations for small functionality.

## Usage

```bash
/implement:small [arguments]
```yaml

**Arguments**: Optional parameters specific to the operation

## Process

1. Analyze the current state and requirements
2. Execute the implement operation
3. Validate results and provide feedback
4. Update relevant documentation or state

## Agent Integration

- **Primary Agent**: implementation-orchestrator - Handles implement operations and coordination

## Examples

### Quick Bug Fix

```yaml
User: "/implement:small fix login error message"
→ task-orchestrator identifies as bug
→ Spawns bug-fixer
→ Fix applied directly
→ Done in one step
```text

### Small Feature

```yaml
User: "/implement:small add email validation helper"
→ task-orchestrator identifies as feature
→ Spawns code-writer
→ Creates validation function
→ Optionally spawns test-writer
```text

### Minor Refactor

```yaml
User: "/implement:small extract duplicate code in utils.js"
→ task-orchestrator identifies as refactor
→ Spawns code-writer with /refactor:extract-functions
→ Code cleaned up
→ Done
```text

## Additional Information

```yaml
User: "/implement:small fix login error message"
→ task-orchestrator identifies as bug
→ Spawns bug-fixer
→ Fix applied directly
→ Done in one step
```text

```yaml
User: "/implement:small add email validation helper"
→ task-orchestrator identifies as feature
→ Spawns code-writer
→ Creates validation function
→ Optionally spawns test-writer
```text

```yaml
User: "/implement:small extract duplicate code in utils.js"
→ task-orchestrator identifies as refactor
→ Spawns code-writer with /refactor:extract-functions
→ Code cleaned up
→ Done
```
