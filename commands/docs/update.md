---
description: "Intelligently update existing project documentation by analyzing changes and keeping content current"
category: "docs"
agent: "documenter"
tools: ["Read", "Edit", "Bash", "Grep"]
complexity: "moderate"
---

# Command: Update

## Purpose

Executes docs operations for update functionality.

## Usage

```bash
/docs:update [arguments]
```yaml

**Arguments**: Optional parameters specific to the operation

## Process

1. Analyze the current state and documentation changes needed
2. Update existing documentation files with current information
3. **README.md Synchronization**: Review and update README.md for consistency
4. Validate documentation links and cross-references
5. Ensure README links match actual documentation structure
6. Validate results and provide feedback

## Agent Integration

- **Primary Agent**: documenter - Handles docs operations and coordination

## Examples

```bash

## Integration Points
Works with other commands:
- After `/implement` or `/scaffold` - Document new features
- After `/fix bug-quickly` - Update CHANGELOG and troubleshooting
- After `/refactor` - Update architecture and migration docs
- After `/test` - Update test documentation coverage
- After `/review security` - Update security documentation
