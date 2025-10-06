---
description: "Interactive command creation wizard using standardized command templates"
argument-hint: ""
allowed-tools: Read, Write, Edit
---

# Command: Create From Template

## Purpose

Guides users through interactive slash command creation using standardized templates (atomic or workflow), ensuring consistency and best practices.

## Usage

```bash
/slashcommand:create-from-template
```

**Arguments**: None (fully interactive)

## Process

1. **Select Template Type**: Ask "Atomic command or workflow command?"
2. **Load Template**:
   - If atomic → Read `templates/commands/command.md`
   - If workflow → Read `templates/commands/command-workflow.md`
3. **Interactive Prompts**: Collect command specifications:
   - Category (existing: clean, docs, explain, fix, git, implement, prompt, refactor, review, slashcommand, spec-kit, subagent, to-do, utility, workflows OR new category)
   - Command name (kebab-case, e.g., "analyze-performance")
   - Description (single clear sentence)
   - Arguments (argument-hint format)
   - Tools needed (for allowed-tools frontmatter)
   - **Agent Assignment**: Which domain analyst(s) should this command use? (Options: react-analyst, typescript-analyst, python-analyst, api-analyst, quality-analyst, architecture-analyst, refactoring-analyst, security-analyst, performance-analyst, testing-analyst, accessibility-analyst, documentation-analyst, database-analyst, frontend-analyst, research-analyst, shadcn-analyst - or suggest need for new analyst)
   - **MCP Integration**: Does this command need external documentation (Context7), browser automation (Playwright), or UI components (shadcn MCP)?
4. **File Placement Validation**:
   - MUST verify category directory exists at `~/.claude/commands/{category}/`
   - MUST create category directory if new category selected
   - MUST confirm full path `commands/{category}/{name}.md` with user before writing
   - MUST validate category name is kebab-case and command name is kebab-case
5. **Generate Command File**: Create command file from template with all collected specifications:
   - Include agent assignment in "Agent Integration" section if specified
   - Add MCP tool references to allowed-tools frontmatter if Context7/Playwright/shadcn selected
   - Document MCP usage patterns in command body if MCP tools included
   - For documentation-related commands: Include Mermaid diagram guidance and examples
6. **Confirm Creation**: Display command file path and usage instructions

## Agent Integration

- **Domain Analysts**: Uses quality-analyst for validation of generated command file
- **Pattern**: Template-based generation with validation

## Examples

### Example: Creating an Atomic Command

```
User: /slashcommand:create-from-template
