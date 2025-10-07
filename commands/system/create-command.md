---
description: "Interactive command creation wizard using standardized command templates"
argument-hint: ""
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Command: Create Command From Template

## Purpose

Guides users through interactive slash command creation using standardized command templates, ensuring consistency and best practices.

## Usage

```bash
/system:create-command
```

**Arguments**: None (fully interactive)

## Process

1. **Select Template Type**: Prompt user to choose template:
   - `command.md` - Atomic single-purpose command
   - `command-workflow.md` - Orchestrated multi-step workflow command

2. **Read Template**: Load selected template from `templates/commands/`

3. **Interactive Prompts**: Collect command specifications:
   - **Command category** (git, docs, workflows, system, etc.)
   - **Command name** (kebab-case: create-todo, run-review, etc.)
   - **Description** (single clear sentence)
   - **Purpose** (primary function description)
   - **Arguments** (list of positional args and flags)
   - **Allowed tools** (Read, Write, Edit, Bash, Task, etc.)
   - **Process steps** (3-7 steps describing execution)
   - **Agent integration** (which analysts to invoke, if any)
   - **Examples** (2-3 usage examples)

4. **Validate Input**:
   - Check command name follows kebab-case
   - Verify category exists in commands/ directory
   - Ensure no duplicate command names
   - Validate allowed-tools syntax

5. **Generate Command File**: Create `commands/{category}/{name}.md` from template with user inputs

6. **Update Documentation**:
   - Add command to `docs/command-decision-guide.md` in appropriate category
   - Update CLAUDE.md command system section if needed

7. **Run Validation**:
   - Check frontmatter syntax
   - Verify markdown linting compliance
   - Validate command follows template structure

8. **Confirm Creation**: Display command file path, usage instructions, and next steps

## Agent Integration

- **Specialist Options**: quality-analyst can be spawned to validate generated command file structure and compliance

## Examples

### Example Interaction: Creating Atomic Command

```text
User: /system:create-command
Claude: Which type of command would you like to create?
  1. Atomic command (single-purpose)
  2. Workflow command (orchestrated)

User: 1 (atomic)

Claude: What category will this command be in?
  Options: git, docs, workflows, development, quality, documentation, explain, system

User: system

Claude: What is the command name (kebab-case)?

User: backup-config

Claude: What is the single-sentence description?

User: "Back up project configuration files to versioned archive"

Claude: What is the primary purpose?

User: "Creates timestamped archives of critical configuration files for disaster recovery"

Claude: What arguments does this command accept? (Enter "done" when finished)

User: $1 (--output): Output directory for backup archives (optional, default: .backups/)
User: $2 (--include): Additional file patterns to include (optional)
User: done

Claude: What tools does this command need?
  Common: Read, Write, Edit, Bash, Task, Grep, Glob, WebFetch, WebSearch

User: Read, Write, Bash, Glob

Claude: Generating command file...
Created: commands/system/backup-config.md

Next steps:
1. Review generated file for accuracy
2. Add command to docs/command-decision-guide.md
3. Test command invocation: /system:backup-config
4. Restart Claude Code to register new command
```

### Example Interaction: Creating Workflow Command

```text
User: /system:create-command

Claude: Which type of command would you like to create?
  1. Atomic command (single-purpose)
  2. Workflow command (orchestrated)

User: 2 (workflow)

Claude: What category will this command be in?

User: workflows

Claude: What is the command name (kebab-case)?

User: run-integration-tests

Claude: What agents will this workflow coordinate? (Enter "done" when finished)

User: testing-analyst
User: quality-analyst
User: security-analyst
User: done

Claude: Generating workflow command file...
Created: commands/workflows/run-integration-tests.md

Workflow will:
1. Launch 3 analysts in parallel
2. Consolidate findings from .agent/context/*.md
3. Generate consolidated report

Next steps:
1. Review generated file
2. Update docs/command-decision-guide.md
3. Restart Claude Code
```

## Command Name Rules

**Kebab-case format**: lowercase with hyphens

**Good Names**:

- create-todo
- run-comprehensive-review
- backup-config
- convert-to-github-issues

**Bad Names**:

- createTodo (camelCase)
- Create_TODO (mixed case)
- runtests (missing hyphens)
- CREATE-TODO (uppercase)

## Template Selection Guide

**Use `command.md` for**:

- Single-purpose atomic operations
- Direct tool usage without analyst coordination
- Quick targeted commands
- CRUD operations

**Use `command-workflow.md` for**:

- Multi-analyst coordination
- Parallel execution patterns
- Comprehensive analysis operations
- Orchestrated multi-step processes

## Validation Checks

**Frontmatter Validation**:

- description: Single sentence, clear, concise
- argument-hint: Matches actual arguments
- allowed-tools: Valid tool names, proper Bash(*) syntax

**Structure Validation**:

- All required sections present (Purpose, Usage, Process, Examples)
- Markdown linting compliance (.markdownlint.yml)
- Code blocks have language specifiers
- Lists have blank lines before/after

**Naming Validation**:

- Command name is kebab-case
- Category directory exists
- No duplicate command names in category
- Filename matches command name

## Integration Points

**Works Well With**:

- `/system:create-agent` - Create supporting domain analyst
- `/docs:update` - Update documentation after creation
- `/git:commit` - Commit new command file

**Follows Well**:

- Command system planning
- Template customization
- Command refactoring

## Output

Provides:

- Generated command file at `commands/{category}/{name}.md`
- Validation results (frontmatter, structure, naming)
- Next steps for testing and documentation
- Reminder to restart Claude Code to register command

## Best Practices

1. **Follow single responsibility** - one command, one clear purpose
2. **Use descriptive names** - make purpose obvious from name
3. **Provide comprehensive examples** - show common use cases
4. **Document agent coordination** - clarify how analysts interact
5. **Validate before committing** - run markdown linting
6. **Update decision guide** - add command to appropriate category
7. **Test immediately** - verify command works as expected
