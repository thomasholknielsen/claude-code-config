---
description: "Analyze project documentation coverage, quality, and freshness to identify improvement opportunities"
argument-hint: "[scope] [--detailed] [--output-report]"
allowed-tools: Glob, Read, Grep, Bash
---

# Command: Analyze

## Purpose

Executes docs operations for analyze functionality.

## Usage

```bash
/docs:analyze $ARGUMENTS
```

**Arguments**:

- `$1` (scope): Documentation scope to analyze (optional)
- `$2` (--detailed): Provide detailed analysis report (optional)
- `$3` (--output-report): Generate output report file (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "docs/ --detailed"` - Detailed analysis of docs directory
- `$ARGUMENTS = "--output-report"` - Generate analysis report
- `$ARGUMENTS = "README.md --detailed --output-report"` - Comprehensive README analysis

## Process

1. Analyze documentation coverage, quality, and freshness based on $ARGUMENTS scope
2. Check README.md links and verify they match actual documentation structure
3. Identify gaps, outdated content, and improvement opportunities
4. **README.md Validation**: Ensure README accurately represents current docs structure
5. Generate recommendations for documentation improvements
6. Validate results and provide detailed feedback report

## Agent Integration

- **Specialist Agent**: documenter - Can be spawned to handle documentation analysis and quality assessment

## Examples

```bash
