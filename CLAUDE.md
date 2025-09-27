# Claude Code Configuration - Command System Project

This file contains **project-specific** configuration for the Claude Code command system project, providing comprehensive instructions for CRUD operations on repository artifacts.

## 🎯 Repository Overview

The Claude Code Command System is a comprehensive development automation system built on the **Agent Orchestra Framework**. This repository contains:

- **8 Agents**: 3 orchestrators + 5 workers for task coordination and execution
- **54 Commands**: Atomic operations organized across 13 categories
- **Complete Documentation**: User guides, technical docs, and visual workflows
- **Hooks System**: Cross-platform Python-based automation
- **MCP Integration**: Context7 and Playwright tools for enhanced capabilities

## 🏗️ Agent Orchestra Framework

### Orchestrators (3 agents)
Coordinate complex, multi-step tasks and delegate to workers:

1. **implementation-orchestrator** - Coordinates sequential code changes ensuring consistency and preventing conflicts
2. **task-orchestrator** - General task coordinator that analyzes complexity and spawns appropriate specialized workers
3. **research-orchestrator** - Coordinates parallel information gathering across multiple sources and domains

### Workers (5 agents)
Execute specific functions with focused responsibilities:

1. **reviewer** - Specialized code review agent performing parallel quality, security, and design checks
2. **documenter** - Specialized documentation agent creating and maintaining all forms of technical documentation
3. **code-writer** - Focused code generation specialist using slash commands for structured operations
4. **bug-fixer** - Specialized debugging and bug resolution agent using fix-focused slash commands
5. **test-writer** - Specialized test creation and maintenance agent using test-focused slash commands
### Agent Coordination Patterns

**Use orchestrators for:**
- Complex tasks requiring planning and coordination
- Multi-step workflows with dependencies
- Tasks requiring parallel execution
- Cross-domain work requiring multiple workers

**Use workers for:**
- Single-responsibility atomic operations
- Specific expertise areas (coding, testing, documentation)
- Tasks that can be executed independently
- Operations that don't require coordination

## 📁 Command System Structure

### Actual Command Categories (54 total)

```
commands/
├── analyze/      # 3 commands
├── clean/        # 4 commands
├── docs/         # 6 commands
├── explain/      # 2 commands
├── fix/          # 2 commands
├── git/          # 6 commands
├── implement/    # 2 commands
├── plan/         # 1 commands
├── refactor/     # 6 commands
├── review/       # 3 commands
├── spec-kit/     # 7 commands
├── to-do/        # 5 commands
├── workflows/    # 7 commands
```

### Command Design Principles

**Atomic Operations**: All commands (except workflows) are atomic, single-purpose operations that can be:
- Used directly by Claude Code users
- Called by orchestrators for complex workflows
- Executed by subagents as part of larger tasks
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
- **research-orchestrator**: For gathering current best practices
- **documenter**: For up-to-date documentation standards
- **code-writer**: For current API patterns and implementations
- **reviewer**: For latest security practices and guidelines
- **bug-fixer**: For known issue patterns and solutions

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
```

### User-Agnostic Design
All paths and configurations work regardless of username:
- Use `~/.claude/` instead of `/Users/specific-user/.claude/`
- Scripts detect their location dynamically
- No hardcoded user directories
- Portable configuration across systems

## 🔐 Security & Permission Guidelines

### Critical Git Operations Constraint
**MANDATORY**: Only `/git/*` commands can perform Git operations.

- **All other agents/commands**: Must use SlashCommand tool to delegate Git operations
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
- `docs/agent-orchestra-framework.md` - Technical framework details
- `docs/command-template.md` - Standard format for new commands

**System Documentation:**
- `docs/hooks-system.md` - Complete hooks system with diagrams
- `docs/spec-kit-workflow.md` - 7-step feature development process
- `docs/command-audit-report.md` - Standardization analysis

**Implementation Reference:**
- `docs/implementation-summary.md` - Complete work overview

## 🔧 Development Standards

### Command Development

**Required Format** (follow `docs/command-template.md`):
```markdown
---
description: "Single clear sentence describing command purpose"
category: "folder_name"
agent: "primary-agent-from-orchestra"
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
```

### Agent Development

**Agent Requirements:**
- **Single Responsibility**: One clear, focused purpose
- **No Overlap**: Must not duplicate existing agent functionality
- **Orchestra Compliance**: Follow orchestrator/worker pattern
- **Model Selection**: Opus for orchestrators, Sonnet for workers
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

### Create Operations

**New Commands:**
1. Use command template from `docs/command-template.md`
2. Place in appropriate category folder: `commands/{category}/{name}.md`
3. Assign to existing Agent Orchestra agent
4. Include MCP tools if relevant (Context7 for docs, Playwright for UI)
5. Ensure atomic operation design
6. Run `/docs:sync-claude-md` to update CLAUDE.md with current command counts

**New Agents:**
1. Follow agent template pattern from existing agents
2. Place in `agents/orchestrators/` or `agents/workers/`
3. Single responsibility only
4. Include model specification (Opus/Sonnet)
5. Document MCP tool usage if applicable
6. Run `/docs:sync-claude-md` to update CLAUDE.md with current agent information

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
5. Run `/docs:sync-claude-md` to update CLAUDE.md with current agent information

### Delete Operations

**Removing Commands:**
1. Check for dependencies in other commands
2. Update documentation referencing the command
3. Remove from any workflow sequences
4. Clean up empty categories if needed
5. Run `/docs:sync-claude-md` to update CLAUDE.md with current command counts

**Removing Agents:**
1. Reassign all commands using the agent
2. Update Agent Orchestra documentation
3. Remove from workflow patterns
4. Run `/docs:sync-claude-md` to update CLAUDE.md with current agent counts

## 🎯 Quality Standards

### Command Quality
- **Atomic Design**: Single, clear purpose
- **Documentation**: Complete template compliance
- **Integration**: Clear relationship to other commands
- **Testing**: Verify functionality works as documented

### Agent Quality
- **Responsibility**: Single, focused capability
- **Coordination**: Proper orchestrator/worker relationship
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
- **Agent Coordination**: Orchestrator → worker delegation patterns
- **Documentation Quality**: User feedback and completion rates
- **System Performance**: Command execution speed and reliability
- **Error Rates**: Failed commands and common issues

## ⚠️ Critical Constraints

### What NOT to do:
- **Don't bypass Git constraints**: Only `/git/*` commands can perform Git operations
- **Don't hardcode paths**: Use user-agnostic path patterns
- **Don't duplicate agents**: Each agent must have unique responsibility
- **Don't ignore MCP integration**: Use Context7/Playwright where appropriate
- **Don't break atomic design**: Keep commands single-purpose

### Required Practices:
- **Use Agent Orchestra**: Always assign commands to existing agents
- **Follow templates**: Use provided templates for consistency
- **Cross-platform thinking**: Test on multiple operating systems
- **Document thoroughly**: Include examples and integration points
- **Validate security**: Ensure Git constraints are respected
- **Maintain CLAUDE.md synchronization**: After creating, modifying, or deleting agents or commands, run `/docs:sync-claude-md` to automatically update counts and descriptions in this file

---

This configuration provides comprehensive instructions for working with all repository artifacts while maintaining quality, security, and cross-platform compatibility standards.