---
description: "Saves Claude plan mode output to versioned markdown files in project/.claude/.plans"
category: "plan"
agent: "task-orchestrator"
tools: ["Bash", "Write"]
complexity: "simple"
---

# Command: Save Plan to Markdown

## Purpose
Saves plans generated from Claude's plan mode (Shift+Tab twice) to versioned markdown files in the project's `.claude/.plans` directory.

## Usage
```
/plan:save-plan-to-markdown
```

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

## Workflow
1. **Enter Plan Mode**: Press Shift+Tab twice to activate Claude's plan mode
2. **Generate Plan**: Claude creates a structured plan outline for your feature
3. **Save Plan**: Run `/plan:save-plan-to-markdown` to save the plan to disk

## Examples
```bash
# After generating a plan in plan mode:
/plan:save-plan-to-markdown
# Saves current plan to project/.claude/.plans/plan-20250927-155306-add-user-authentication.md

# With custom title:
/plan:save-plan-to-markdown --title "User Auth Implementation"
# Saves as: plan-20250927-155306-user-auth-implementation.md
```

## Output
- Plan saved to `project/.claude/.plans/plan-{timestamp}-{title}.md`
- Includes metadata headers (creation date, project name, status)
- Preserves original plan structure and formatting
- Automatic project detection and directory creation

## Integration Points
- **Follows**: Claude plan mode (Shift+Tab twice), initial planning session
- **Followed by**: /spec-kit:tasks (for task breakdown), /spec-kit:implement
- **Related**: /spec-kit:plan, /spec-kit:analyze, /spec-kit:specify

## Features
- **Project Detection**: Automatically finds project root via .git, package.json, etc.
- **Smart Titles**: Extracts meaningful titles from plan content
- **Metadata**: Adds creation date, project name, and status headers
- **Versioning**: Timestamp-based filenames prevent overwrites
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Quality Standards
- Preserves original plan structure and formatting
- Adds consistent metadata without disrupting content
- Creates project-specific storage location
- Generates meaningful, searchable filenames
- Maintains plan versioning through timestamps