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
   ```bash

2. **Make scripts executable:**

   ```bash
   chmod +x scripts/*.sh

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
- **`agents/`** - Agent Orchestra Framework definitions
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
   claude /docs:generate
   ```

### Understanding Command Categories

Commands are organized by action type:

- **`/analyze/*`** - Performance and dependency analysis
- **`/clean/*`** - Code cleanup operations
- **`/docs/*`** - Documentation generation and maintenance
- **`/fix/*`** - Bug fixes and issue resolution
- **`/git/*`** - Git operations
- **`/review/*`** - Code review and quality analysis
- **`/spec-kit/*`** - Complete feature development workflow

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

## Agent Orchestra Framework

The system uses specialized agents:

### Orchestrators (Coordinate Tasks)

- **task-orchestrator** - General task coordination
- **research-orchestrator** - Information gathering
- **implementation-orchestrator** - Code implementation

### Workers (Execute Tasks)

- **code-writer** - Code generation
- **test-writer** - Test creation
- **bug-fixer** - Debugging
- **reviewer** - Code analysis
- **documenter** - Documentation

## Common Workflows

### Feature Development

```bash
# Full featured workflow
claude /spec-kit:specify "User authentication system"
claude /spec-kit:plan
claude /spec-kit:implement

# Or quick implementation
claude /implement "Add user authentication"
```text

### Code Quality

```bash
# Full review
claude /workflows:run-comprehensive-review

# Specific reviews
claude /review:security
claude /review:code
claude /clean:apply-style-rules
```text

### Bug Fixing

```bash
claude /fix:bug-quickly "Login button not working"
claude /analyze:potential-issues
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

Agents are pre-configured but can be extended:

1. Add new workers in `agents/workers/`
2. Update orchestrators in `agents/orchestrators/`
3. Follow the Agent Orchestra patterns

## Troubleshooting

### Common Issues

**Command not found**

- Check the command exists in the appropriate category
- Verify the command format matches the documentation

**Hook not executing**

- Ensure scripts are executable: `chmod +x scripts/*.sh`
- Check Python is available and scripts have no syntax errors

**Permission denied**

- Check `settings.json` permissions
- Ensure the operation is allowed in the permissions list

**Agent not responding**

- Check agent definitions in `agents/` directory
- Verify Agent Orchestra framework is properly configured

### Getting Help

- Run `claude /help` for available commands
- Check the developer guide for advanced customization
- Review agent documentation for specific capabilities

## Next Steps

1. **Set up MCP integration** - Follow the [MCP Setup Guide](mcp-setup-guide.md) for Context7 and Playwright
2. **Try the spec-kit workflow** for complex features
3. **Set up custom notifications** by modifying hook scripts
4. **Explore advanced commands** in each category
5. **Customize agents** for your specific needs

For advanced usage and customization, see the [Developer Guide](developer-guide.md).
