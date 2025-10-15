# User Guide - Claude Code Command System

## Quick Start

### Prerequisites

- Claude Code CLI installed
- Python 3.7+ (for hook scripts)
- Git configured
- Node.js 18+ (for MCP server integration)
- Optional: Context7 API key and Playwright browsers for enhanced functionality

### Installation

1. **Clone this repository to your Claude config directory:**

   ```bash
   git clone <repo-url> ~/.claude
   cd ~/.claude
   ```

2. **Make scripts executable:**

   ```bash
   chmod +x scripts/**/*.py
   ```

3. **Test the setup:**

   ```bash
   claude /help
   ```

4. **Optional: Set up MCP servers for enhanced functionality:**
   See the [MCP Setup Guide](mcp-setup-guide.md) for Context7 and Playwright integration.

## Configuration Overview

### Core Files

- **`settings.json`** - Main configuration with hooks, permissions, and MCP servers
- **`CLAUDE.md`** - Project-specific instructions and agent configuration
- **`scripts/`** - Hook scripts for notifications and logging
- **`agents/`** - Agent Specialist Framework definitions
- **`commands/`** - Custom command definitions organized by category

### MCP Integration

The system integrates with Model Context Protocol (MCP) servers for enhanced functionality:

- **Context7 MCP** - Access current library documentation and code examples
- **Playwright MCP** - Browser automation for testing and UI analysis

For setup instructions, see the [MCP Setup Guide](mcp-setup-guide.md).

### Permissions System

The system uses a allowlist approach in `settings.json`:

- **Allowed tools** - Approved bash commands and file operations
- **Denied patterns** - Blocked access to secrets and sensitive files

## Basic Usage

### Getting Started Commands

1. **View available commands:**

   ```bash
   claude /help
   ```

2. **Create a simple feature:**

   ```bash
   claude /implement "Add a login button to the header"
   ```

3. **Review your code:**

   ```bash
   claude /review:code
   ```

4. **Generate documentation:**

   ```bash
   claude /workflows:docs
   ```

### Understanding Command Categories

Commands are organized by action type:

- **`/analyze/*`** - Performance and dependency analysis
- **`/clean/*`** - Code cleanup operations
- **`/docs/*`** - Documentation generation and maintenance
- **`/fix/*`** - Bug fixes and issue resolution
- **`/git/*`** - Git operations
- **`/review/*`** - Code review and quality analysis
- **`/speckit/*`** - Complete feature development workflow

## Hooks System

The system includes three automatic hooks:

### 1. Prompt Logging

- **Trigger**: Every user prompt
- **Action**: Logs prompts to `/logs/prompt-log-YYYY.log`
- **Purpose**: Track your Claude interactions

### 2. Smart Notifications (macOS)

- **Trigger**: Task completion
- **Action**: Desktop notifications with task summary
- **Purpose**: Stay informed about long-running tasks

### 3. Search Year Updates

- **Trigger**: Before web searches
- **Action**: Updates search queries with current year
- **Purpose**: Get current information

## Domain Analyst Framework

The system uses **43 domain analysts** as advisory subagents. Only the main Claude Code thread can orchestrate parallel execution. Domain analysts conduct comprehensive research in their specialty, persist findings to `.agent/context/` files, and return concise summaries.

### Analyst Organization (12 Domains)

- **API** - api-rest-analyst, api-graphql-analyst, api-docs-analyst
- **Database** - database-analyst, database-sql-analyst, database-nosql-analyst, database-architecture-analyst
- **Frontend** - frontend-analyst, frontend-react-analyst, frontend-nextjs-analyst, frontend-accessibility-analyst, frontend-shadcn-analyst
- **Code Quality** - code-python-analyst, code-typescript-analyst, code-javascript-analyst, code-csharp-analyst, code-quality-analyst
- **Infrastructure** - infrastructure-terraform-analyst, infrastructure-cloud-analyst, infrastructure-network-analyst, infrastructure-devops-analyst, infrastructure-monitoring-analyst
- **Mobile** - mobile-react-native-analyst, mobile-flutter-analyst, mobile-ios-swift-analyst
- **Research** - research-codebase-analyst, research-web-analyst
- **Documentation** - docs-analyst, docs-docusaurus-analyst
- **UI/UX** - ui-ux-analyst, ui-ux-cli-analyst
- **Standalone** - architecture-analyst, security-analyst, performance-analyst, testing-analyst, refactoring-analyst, debugger-analyst, seo-analyst, product-roadmap-analyst
- **Engineering** - prompt-analyst
- **Meta** - agent-expert, command-expert, git-flow-analyst

**Pattern**: Main thread invokes analysts → Analysts research → Persist to `.agent/context/{session-id}/{analyst-name}.md` → Return summary → Main thread implements

For complete analyst details, see [Agent Specialist System](../concepts/agent-specialist-system.md)

## Common Workflows

### Feature Development

```bash
# Full featured workflow with spec-kit
claude /speckit:specify "User authentication system"
claude /speckit:plan
claude /speckit:tasks
claude /speckit:implement

# Task-based workflow
claude /task:add "Implement user authentication"
claude /task:execute TASK-001
```

### Code Quality

```bash
# Comprehensive review
claude /workflows:run-comprehensive-review

# Specific workflows
claude /workflows:run-security-audit
claude /workflows:run-refactor-workflow
claude /lint:correct-all
```

### Documentation

```bash
# Smart documentation workflow (idempotent)
claude /workflows:docs

# Changelog management
claude /docs:changelog 1.2.0 --add-entry
```

## Customization

### Adding Custom Commands

1. Create a new `.md` file in the appropriate `commands/` category
2. Follow the existing command format
3. Test your command

### Modifying Hooks

1. Edit `settings.json` to add new hooks
2. Create corresponding Python scripts in `scripts/`
3. Ensure scripts are executable

### Agent Configuration

Agents are pre-configured in a flat structure at `agents/*.md`. To create new agents:

1. Use `/claude:create-agent` with agent-expert consultation
2. Follow domain analyst patterns (analyze, persist, summarize)
3. Place in `agents/{analyst-name}.md`
4. Update CLAUDE.md agent tables

## Troubleshooting

### Common Issues

**Command not found**

- Check the command exists in the appropriate category
- Verify the command format matches the documentation

**Hook not executing**

- Ensure scripts are executable: `chmod +x scripts/**/*.py`
- Check Python is available and scripts have no syntax errors

**Permission denied**

- Check `settings.json` permissions
- Ensure the operation is allowed in the permissions list

**Agent not responding**

- Check agent definitions in `agents/` directory
- Verify Agent Specialist Framework is properly configured

### Getting Help

- Run `claude /help` for available commands
- Check the developer guide for advanced customization
- Review agent documentation for specific capabilities

## Next Steps

1. **Set up MCP integration** - Follow the [MCP Setup Guide](mcp-setup-guide.md) for Context7 and Playwright
2. **Try the speckit workflow** for complex features
3. **Set up custom notifications** by modifying hook scripts
4. **Explore advanced commands** in each category
5. **Customize agents** for your specific needs

For advanced usage and customization, see the [Developer Guide](../developer/developer-guide.md).
