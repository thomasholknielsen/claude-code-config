---
description: "Saves Claude plan mode output to versioned markdown files in project/.claude/.plans"
category: "plan"
agent: "task-orchestrator"
tools: ["Bash", "Write"]
complexity: "simple"
---

# Command: Save Plan To Markdown

## Purpose

Saves plans generated from Claude's plan mode (Shift+Tab twice) to versioned markdown files in the project's `.claude/.plans` directory.

## Usage

```bash
/plan:save-plan-to-markdown
```python

**No arguments**: Reads the current plan from conversation context

## Process

1. Extract the plan content from the current conversation/plan mode
2. Detect the project root directory automatically
3. Create or use existing `.claude/.plans` directory in the project
4. Generate filename with timestamp and meaningful title from plan content
5. Save formatted markdown with metadata headers

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates plan generation and file management
- **Secondary Agents**: None (uses plan mode directly)

## Examples

```bash

## Output
- Plan saved to `project/.claude/.plans/plan-{timestamp}-{title}.md`
- Includes metadata headers (creation date, project name, status)
- Preserves original plan structure and formatting
- Automatic project detection and directory creation

## Integration Points
- **Follows**: Claude plan mode (Shift+Tab twice), initial planning session
- **Followed by**: /spec-kit:tasks (for task breakdown), /spec-kit:implement
- **Related**: /spec-kit:plan, /spec-kit:analyze, /spec-kit:specify

## Quality Standards
- Preserves original plan structure and formatting
- Adds consistent metadata without disrupting content
- Creates project-specific storage location
- Generates meaningful, searchable filenames
- Maintains plan versioning through timestamps
