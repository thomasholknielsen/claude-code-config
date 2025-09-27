---
description: "Generates comprehensive documentation from codebase structure and code analysis"
category: "docs"
agent: "documenter"
tools: ["Read", "Write", "Glob", "Grep"]
complexity: "moderate"
---

# Command: Generate

## Purpose

Creates comprehensive documentation from codebase analysis, matching project structure and conventions.

## Usage

```bash
/docs:generate [type]
```python

**Arguments**: Optional documentation type (api, user, developer, or all)

## Process

1. Analyze project structure to understand architecture and patterns
2. Extract information from code, configurations, and existing documentation
3. Generate contextually appropriate documentation for the project type
4. Follow established documentation standards and formats
5. **README.md Synchronization**: Update README.md with new documentation structure and links
6. Validate README links match actual documentation files and sections
7. Ensure consistency with existing style and conventions

## Agent Integration

- **Primary Agent**: documenter - Handles complete documentation generation workflow

## Examples

```bash
