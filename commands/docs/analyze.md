---
description: "Analyze project documentation coverage, quality, and freshness to identify improvement opportunities"
category: "docs"
agent: "documenter"
tools: ["Glob", "Read", "Grep", "Bash"]
complexity: "complex"
---

# Command: Analyze

## Purpose

Executes docs operations for analyze functionality.

## Usage

```bash
/docs:analyze [arguments]
```yaml

**Arguments**: Optional parameters specific to the operation

## Process

1. Analyze documentation coverage, quality, and freshness across the project
2. Check README.md links and verify they match actual documentation structure
3. Identify gaps, outdated content, and improvement opportunities
4. **README.md Validation**: Ensure README accurately represents current docs structure
5. Generate recommendations for documentation improvements
6. Validate results and provide detailed feedback report

## Agent Integration

- **Primary Agent**: documenter - Handles docs operations and coordination

## Examples

```bash
