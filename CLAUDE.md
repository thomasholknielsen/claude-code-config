# Claude Code Configuration - Command System Project

This file contains **project-specific** configuration for the Claude Code command system project, providing
comprehensive instructions for CRUD operations on repository artifacts.

## 🎯 Repository Overview

The Claude Code Command System is a comprehensive development automation system built on the **Agent Specialist Framework**. This repository contains:

- **8 Agents**: 3 strategic specialists + 5 technical specialists providing advisory domain expertise
- **54 Commands**: Atomic operations organized across 15 categories
- **Complete Documentation**: User guides, technical docs, and visual workflows
- **Hooks System**: Cross-platform Python-based automation
- **MCP Integration**: Context7 and Playwright tools for enhanced capabilities

## 🏗️ Agent Specialist Framework

### Strategic Specialists (3 advisory agents)

Provide strategic analysis and planning guidance for complex development scenarios:

1. **implementation-strategy-specialist** - Provides advisory analysis for sequential code changes ensuring consistency and preventing conflicts
2. **task-analysis-specialist** - General task analysis specialist that evaluates complexity and provides recommendations for specialized approaches
3. **research-analysis-specialist** - Provides advisory guidance for comprehensive information gathering and analysis across multiple sources and domains

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

### Actual Command Categories (54 total)

```text
commands/
├── analyze/      # 3 commands
├── clean/        # 4 commands
├── docs/         # 6 commands
├── explain/      # 2 commands
├── fix/          # 2 commands
├── git/          # 6 commands
├── implement/    # 2 commands
├── plan/         # 1 command
├── prompt/       # 1 command
├── refactor/     # 6 commands
├── review/       # 3 commands
├── spec-kit/     # 7 commands
├── to-do/        # 5 commands
├── workflows/    # 7 commands
```bash

### Command Design Principles

**Atomic Operations**: All commands (except workflows) are atomic, single-purpose operations that can be:

- Used directly by Claude Code users
- Recommended by strategic specialists for complex workflows
- Informed by technical specialist guidance as part of larger tasks
- Combined with other commands for sophisticated automation

**Clear Responsibility**: Each command has one primary function and clear expected outcomes.

**Integration Ready**: Commands include integration points showing how they work with other commands.

## 🔌 MCP Integration

### Context7 MCP - External Documentation

Provides access to current library and framework documentation:

**Tools Available:**

- `mcp__context7__resolve-library-id` - Map package names to documentation IDs
- `mcp__context7__get-library-docs` - Fetch current documentation content

**Used By:**

- **research-analysis-specialist**: For advisory guidance on gathering current best practices
- **documenter**: For advisory guidance on up-to-date documentation standards
- **code-writer**: For advisory guidance on current API patterns and implementations
- **reviewer**: For advisory guidance on latest security practices and guidelines
- **bug-fixer**: For advisory guidance on known issue patterns and solutions

**Commands Enhanced:**

- `/docs:extract-external` - Primary Context7 integration command
- `/docs:api` - Current API documentation standards
- `/review:security` - Latest OWASP guidelines and vulnerabilities
- `/analyze:dependencies` - Current security advisories
- `/implement` - Framework-specific best practices

### Playwright MCP - Browser Automation

Provides comprehensive browser automation capabilities for testing and UI work:

**Tools Available:**

- Navigation: `navigate`, `navigate_back`, `tabs`
- Interaction: `click`, `type`, `hover`, `drag`, `select_option`
- Analysis: `snapshot`, `take_screenshot`, `console_messages`
- Forms: `fill_form`, `file_upload`
- Advanced: `evaluate`, `wait_for`, `network_requests`

**Integration Patterns:**

- UI testing automation
- Web application analysis
- Visual regression testing
- User interaction simulation
- Performance monitoring

## 🌐 Cross-Platform Compatibility

### Python-Based Hooks

All automation scripts are Python-based for cross-platform compatibility:

**Supported Platforms:**

- macOS (primary development)
- Windows (full compatibility)
- Linux (full compatibility)

**Hook Implementation:**

- Use `pathlib.Path` for all file operations
- Use `Path.home()` for user directory references
- Cross-platform environment variable handling
- No shell-specific scripts or commands

**Example Cross-Platform Pattern:**

```python
from pathlib import Path

# User-agnostic path handling
logs_dir = Path.home() / '.claude' / 'logs'
script_dir = Path(__file__).parent if '__file__' in globals() else Path.home() / '.claude' / 'scripts'
```bash

### User-Agnostic Design

All paths and configurations work regardless of username:

- Use `~/.claude/` instead of `/Users/specific-user/.claude/`
- Scripts detect their location dynamically
- No hardcoded user directories
- Portable configuration across systems

## 🔐 Security & Permission Guidelines

### Critical Git Operations Constraint

**MANDATORY**: Only `/git/*` commands can perform Git operations.

- **All other agents/commands**: Must use SlashCommand tool for Git operations (main thread executes)
- **Explicit consent required**: All Git operations outside `/git/*` must ask user permission
- **Agent limitation**: Agents cannot call Git commands directly
- **Enforcement**: Use SlashCommand tool for all Git delegation

### Permission Configuration

Located in `settings.json`:

**MCP Tools Allowed:**

- Context7: `mcp__context7__resolve-library-id`, `mcp__context7__get-library-docs`
- Playwright: All browser automation tools (`mcp__playwright__*`)

**Security Protections:**

- Block access to secrets: `.env`, `*.key`, `*.pem`, credentials
- Restrict dangerous operations: `rm -rf`, `sudo`, network tools
- Allow safe development operations: npm/yarn commands, standard Git ops

## 📚 Documentation Structure

The repository includes comprehensive documentation in `docs/`:

**User Documentation:**

- `docs/user-guide.md` - Complete setup and usage guide
- `docs/typical-workflows.md` - Common patterns with Mermaid diagrams

**Developer Documentation:**

- `docs/developer-guide.md` - Architecture and extension patterns
- `docs/agent-specialist-framework.md` - Technical framework details
- `docs/command-template.md` - Standard format for new commands

**System Documentation:**

- `docs/hooks-system.md` - Complete hooks system with diagrams
- `docs/spec-kit-workflow.md` - 7-step feature development process
- `docs/command-audit-report.md` - Standardization analysis

**Implementation Reference:**

- `docs/implementation-summary.md` - Complete work overview

## 🔧 Development Standards

### Command Development

**Required Format** (follow templates):

- **Atomic commands**: Use `templates/command.md`
- **Workflow commands**: Use `templates/command-workflow.md`

**Required frontmatter fields**:
- `description`: Single clear sentence describing command purpose
- `argument-hint`: Parameter guidance for CLI
- `category`: Command category folder name
- `tools`: Array of Claude Code tools used
- `complexity`: simple | moderate | complex
- `allowed-tools`: Permission specification (e.g., `Tool1, Tool2, Bash(command:*)`)

**Template Selection**:
- Use base template (`templates/command.md`) for atomic, single-purpose operations
- Use workflow template (`templates/command-workflow.md`) for commands that orchestrate other slash commands using SlashCommand tool

**Example Format** (base template):

```markdown
---
description: "Single clear sentence describing command purpose"
argument-hint: "[arg1] [--flag=value]"
category: "folder_name"
tools: ["Tool1", "Tool2"]
complexity: "simple|moderate|complex"
allowed-tools: Tool1, Tool2, Bash(command:*)
---

# Command: {Action Verb} {Object}

## Purpose
Single sentence describing primary function.

## Usage
/{category}:{command-name} $ARGUMENTS

## Process
1. Step 1: Clear action
2. Step 2: Next action
3. Step 3: Final outcome

## Agent Integration
- **Primary Agent**: agent-name - role description

## Examples
[Real usage examples with $ARGUMENTS]
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

## 🔄 CRUD Operations Guide

### 🚨 TODO File Location Constraint

**CRITICAL REQUIREMENT**: All TODO operations MUST use the standardized location:

- **Required Location**: `{project_root}/.claude/.todos/TODO.md`
- **Prohibited**: TODO files in any other location (project root, docs/, etc.)
- **Enforcement**: All `/to-do:*` commands validate and enforce this constraint
- **Rationale**: Centralized task tracking, consistent file management, prevents scattered TODO files

### Create Operations

**New Commands:**

1. Use command template from `docs/command-template.md`
2. Place in appropriate category folder: `commands/{category}/{name}.md`
3. Assign to existing Agent Specialist Framework agent
4. Include MCP tools if relevant (Context7 for docs, Playwright for UI)
5. Ensure atomic operation design

**New Agents:**

1. Follow agent template pattern from existing agents
2. Place in `agents/analysis-specialists/` or `agents/execution-specialists/`
3. Single responsibility only
4. Include model specification (Opus/Sonnet)
5. Document MCP tool usage if applicable

### Read Operations

**Understanding System:**

- Start with `README.md` for overview
- Use `docs/user-guide.md` for setup
- Review `docs/developer-guide.md` for architecture
- Check specific `docs/` files for detailed topics

**Command Discovery:**

- Browse `commands/` folders by category
- Check command YAML frontmatter for quick info
- Use `/help` in Claude Code for available commands

### Update Operations

**Modifying Commands:**

1. Follow existing template format
2. Update YAML frontmatter if changing agent/tools
3. Maintain atomic operation principle
4. Update related documentation if integration points change

**Modifying Agents:**

1. Maintain single responsibility
2. Update model specification if complexity changes
3. Keep MCP tool listings current
4. Update related command agent assignments

### Delete Operations

**Removing Commands:**

1. Check for dependencies in other commands
2. Update documentation referencing the command
3. Remove from any workflow sequences
4. Clean up empty categories if needed

**Removing Agents:**

1. Reassign all commands using the agent
2. Update Agent Specialist Framework documentation
3. Remove from workflow patterns

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
