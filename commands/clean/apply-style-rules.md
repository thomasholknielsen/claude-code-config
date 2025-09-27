---
description: "Automated code formatting using project's configured formatter (prettier, eslint --fix, etc.)"
category: "clean"
agent: "code-writer"
tools: ["Read", "Edit", "MultiEdit", "Bash"]
complexity: "simple"
---

# Command: Apply Style Rules

## Purpose

Executes clean operations for apply style rules functionality.

## Usage

```bash
/clean:apply-style-rules [arguments]
```yaml

**Arguments**: Optional parameters specific to the operation

## Process

1. Analyze the current state and requirements
2. Execute the clean operation
3. Validate results and provide feedback
4. Update relevant documentation or state

## Agent Integration

- **Primary Agent**: code-writer - Handles clean operations and coordination

## Examples

```bash
