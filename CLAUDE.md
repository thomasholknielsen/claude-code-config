# Claude Code Configuration - Command System Project

This file contains **project-specific** configuration for the Claude Code command system project, providing
comprehensive instructions for CRUD operations on repository artifacts.

## 🎯 Repository Overview

The Claude Code Command System is a comprehensive development automation system built on the **Agent Specialist Framework**. This repository contains:

- **8 Agents**: 3 strategic specialists + 5 technical specialists providing advisory domain expertise
- **63 Commands**: Atomic operations organized across 15 categories (includes 11 review commands)
- **Complete Documentation**: User guides, technical docs, and visual workflows
- **Hooks System**: Cross-platform Python-based automation
- **MCP Integration**: Context7 and Playwright tools for enhanced capabilities

## 🏗️ Agent Specialist Framework

### Strategic Specialists (3 advisory agents)

Provide strategic analysis and planning guidance for complex development scenarios:

1. **implementation-strategy-specialist** - Provides advisory analysis for sequential code changes ensuring consistency and preventing conflicts
2. **task-analysis-specialist** - General task analysis specialist that evaluates complexity and provides recommendations for specialized approaches
3. **research-analysis-specialist** - Provides advisory guidance for comprehensive information gathering and
   analysis across multiple sources and domains

### Technical Specialists (5 advisory agents)

Provide focused domain advisory expertise for specific development functions:

1. **reviewer** - Specialized code review advisory specialist providing quality, security, and design guidance
2. **documenter** - Specialized documentation advisory specialist providing guidance on technical documentation creation and maintenance
3. **code-writer** - Focused code generation advisory specialist providing guidance on structured development operations
4. **bug-fixer** - Specialized debugging and bug resolution advisory specialist providing troubleshooting guidance
5. **test-writer** - Specialized test creation and maintenance advisory specialist providing testing strategy guidance

### Agent Specialist Patterns

**Use strategic specialists for:**

- Complex strategic planning and analysis guidance
- Multi-step workflow recommendations
- Comprehensive research and evaluation strategies
- Cross-domain advisory expertise

**Use technical specialists for:**

- Domain-specific implementation advisory guidance
- Focused technical area consultation (coding, testing, documentation)
- Specialized tool and technique recommendations
- Targeted problem-solving advisory approaches

## 📁 Command System Structure

### Command Categories

```text
commands/
├── analyze/
├── artifact/
├── clean/
├── docs/
├── explain/
├── fix/
├── git/
├── implement/
├── plan/
├── prompt/
├── refactor/
├── review/
├── spec-kit/
├── to-do/
├── workflows/
```

### Command Design Principles

**Atomic Operations**: All commands (except workflows) are atomic, single-purpose operations that can be:

- Used directly by Claude Code users
- Recommended by strategic specialists for complex workflows
- Informed by technical specialist guidance as part of larger tasks
- Combined with other commands for sophisticated automation

**Clear Responsibility**: Each command has one primary function and clear expected outcomes.

**Integration Ready**: Commands include integration points showing how they work with other commands.

## 🔌 MCP Integration

The system integrates Model Context Protocol (MCP) servers for enhanced capabilities: **Context7** provides
access to current library/framework documentation (used by docs, review, and analysis commands), and
**Playwright** enables browser automation for UI testing and visual regression (used by design review and
testing commands). See individual command frontmatter for specific MCP tool usage.

## 🌐 Cross-Platform Compatibility

All automation scripts use Python with `pathlib.Path` for cross-platform compatibility (Windows, macOS, Linux).
Use user-agnostic paths (`~/.claude/`) and avoid hardcoded usernames or shell-specific commands.

## 🔐 Security & Permission Guidelines

### Critical Git Operations Constraint

**MANDATORY**: Only `/git/*` commands can perform Git operations.

- **All other agents/commands**: Must use SlashCommand tool for Git operations (main thread executes)
- **Explicit consent required**: All Git operations outside `/git/*` must ask user permission
- **Agent limitation**: Agents cannot call Git commands directly
- **Enforcement**: Use SlashCommand tool for all Git delegation

### Git Naming Conventions

All git operations (commits, branches, PRs) use conventional commit format with auto-detected types from
uncommitted file analysis. Standard types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`,
`ci`, `build`, `revert`. See `/git:commit`, `/git:branch`, and `/git:pr` for detailed type detection rules,
format patterns, and scope extraction.

### Permission Configuration

Located in `settings.json`:

**MCP Tools Allowed:**

- Context7: `mcp__context7__resolve-library-id`, `mcp__context7__get-library-docs`
- Playwright: All browser automation tools (`mcp__playwright__*`)

**Security Protections:**

- Block access to secrets: `.env`, `*.key`, `*.pem`, credentials
- Restrict dangerous operations: `rm -rf`, `sudo`, network tools
- Allow safe development operations: npm/yarn commands, standard Git ops

## 📦 Artifact Management System

Use `/artifact:save` to capture and preserve Claude outputs (plans, reviews, research, analysis, specifications,
documentation, reports) in `.artifacts/` with type-based organization and automatic naming. Replaces
`/plan:save-plan-to-markdown`.

## 🤖 AI Code Review System

The repository includes a comprehensive AI-powered code review system with 11 specialized atomic review commands
(readability, performance, testing, style, architecture, documentation, observability, security, code, design)
and synthesis capabilities.

**Primary Workflow:** Use `/workflows:run-comprehensive-review` to orchestrate multi-perspective reviews with
dynamic selection, parallel execution, and unified reporting. See command documentation for details on individual
reviews, GitHub Actions integration, and output formats.

## 📚 Documentation Structure

Comprehensive documentation is available in `docs/` covering user guides, developer architecture, command
templates, hooks system, and implementation details. Start with `README.md` for overview and
`docs/user-guide.md` for setup.

## 🔧 Development Standards

### Markdown Linting Standards

All markdown files follow project linting rules configured in `.markdownlint.yml`: maximum line length 150
characters (code blocks 200 chars), ATX-style headers with surrounding blank lines, fenced code blocks with
language specification (bash/python/typescript/yaml/json/mermaid), asterisk-style emphasis, 2-space list
indentation, and inline HTML allowed for specific elements (br/sub/sup/kbd/details/summary). Exceptions defined
in `.markdownlintignore` protect spec-kit commands and gitignored directories.

### Command Development

**Required Format** (follow `docs/command-template.md`):

```markdown
---
description: "Single clear sentence describing command purpose"
category: "folder_name"
agent: "primary-agent-from-specialist-framework"
tools: ["Tool1", "Tool2"]
complexity: "simple|moderate|complex"
---

# Command: {Action Verb} {Object}

## Purpose
Single sentence describing primary function.

## Usage
/{category}:{command-name} [arguments]

## Process
1. Step 1: Clear action
2. Step 2: Next action
3. Step 3: Final outcome

## Agent Integration
- **Primary Agent**: agent-name - role description

## Examples
[Real usage examples]
```bash

### Agent Development

**Agent Requirements:**

- **Single Responsibility**: One clear, focused purpose
- **No Overlap**: Must not duplicate existing agent functionality
- **Specialist Compliance**: Follow analysis/execution specialist pattern
- **Model Selection**: Opus for analysis specialists, Sonnet for execution specialists
- **Tool Integration**: Use SlashCommand for delegation, direct tools for execution

**Required YAML Frontmatter:**

```yaml
---
name: agent-name
description: "Clear description of agent purpose"
color: color-name
model: opus|sonnet
tools: ["Tool1", "Tool2"]
---
```

### Spec-Kit Integration

When `.specify/` folder exists, commands automatically:

- Reference `spec.md` for requirements validation
- Check `plan.md` for architectural alignment
- Verify `tasks.md` for completion criteria
- Validate `contracts/` for API compliance
- Align work with current feature context

This ensures all development work stays aligned with planned features.

### Spec-Kit Cross-Repository Modifications

**CRITICAL**: Spec-kit commands have been modified to use `~/.claude/.specify/scripts/` and
`~/.claude/.specify/templates/` instead of project-relative paths. This enables commands to work from any
repository when Claude config is user-scoped.

**Reapply modifications:**

```bash
/utility:apply-spec-kit-mods
```

## 🔄 Development Workflows

**TODO Management:** All TODO operations use standardized location `{project_root}/.claude/.todos/TODO.md`.
Use `/to-do:*` commands for centralized task tracking.

**Creating/Modifying Commands and Agents:** Follow templates in `docs/command-template.md` and existing agent
patterns. Assign commands to Agent Specialist Framework agents, maintain atomic design, and update CLAUDE.md
after changes. See `docs/developer-guide.md` for complete CRUD workflows.

## 🎯 Quality Standards

### Command Quality

- **Atomic Design**: Single, clear purpose
- **Documentation**: Complete template compliance
- **Integration**: Clear relationship to other commands
- **Testing**: Verify functionality works as documented

### Agent Quality

- **Responsibility**: Single, focused capability
- **Specialization**: Proper analysis/execution specialist relationship
- **Tools**: Appropriate tool selection and MCP usage
- **Documentation**: Clear purpose and usage patterns

### System Quality

- **Cross-Platform**: Works on Windows, macOS, Linux
- **User-Agnostic**: No hardcoded user paths
- **Security**: Git constraints enforced
- **Performance**: Efficient execution patterns

## 📊 Success Metrics

Track system effectiveness by monitoring:

- **Command Usage**: Which commands are most/least used
- **Agent Collaboration**: Analysis specialist → execution specialist advisory patterns
- **Documentation Quality**: User feedback and completion rates
- **System Performance**: Command execution speed and reliability
- **Error Rates**: Failed commands and common issues

## ⚠️ Critical Constraints

### What NOT to do

- **Don't bypass Git constraints**: Only `/git/*` commands can perform Git operations
- **Don't hardcode paths**: Use user-agnostic path patterns
- **Don't duplicate agents**: Each agent must have unique responsibility
- **Don't ignore MCP integration**: Use Context7/Playwright where appropriate
- **Don't break atomic design**: Keep commands single-purpose

### Required Practices

- **Use Agent Specialist Framework**: Always assign commands to existing agents
- **Follow templates**: Use provided templates for consistency
- **Cross-platform thinking**: Test on multiple operating systems
- **Document thoroughly**: Include examples and integration points
- **Validate security**: Ensure Git constraints are respected
- **Maintain CLAUDE.md synchronization**: After creating, modifying, or deleting agents or commands to update descriptions in this file

---

This configuration provides comprehensive instructions for working with all repository artifacts while maintaining quality, security, and
cross-platform compatibility standards.

- in markdown files, when writing code be sure to declare the script language tag
