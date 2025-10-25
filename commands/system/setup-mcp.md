---
description: "Interactive wizard for setting up MCP servers in ~/.claude.json"
argument-hint: "[server-name]"
allowed-tools: Read, Write, Bash(docker:*), Bash(npm:*), Bash(brew:*), Bash(which:*), Bash(uvx:*), Bash(node:*), Bash(python:*), mcp__sequential-thinking__sequentialthinking
---

# Command: Setup MCP Servers

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Interactive wizard for setting up MCP servers in ~/.claude.json with prerequisite validation.

**YOU MUST:**
1. ✓ Parse input from $ARGUMENTS
2. ✓ Execute core operation
3. ✓ Generate or update required outputs
4. ✓ Report status and results

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Skip required operations
- ✗ Leave work incomplete

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Guide MCP server setup via interactive wizard or direct server name, check prerequisites (Docker, Node.js, uv), verify ~/.claude.json exists, prompt for server selection (all or individual), configure server-specific requirements (Context7 API key, Docker images, npm packages), update ~/.claude.json with mcpServers section, create backup before write

**P**urpose: Simplify MCP server configuration through prerequisite validation and step-by-step guidance, prevent misconfiguration errors via JSON validation, support both interactive (wizard) and non-interactive (server name) modes, enable team onboarding with clear install instructions

**E**xpectation: MCP servers configured in ~/.claude.json, prerequisites verified (Docker running, Node.js installed, uv available), backup created (~/.claude.json.backup), configuration validated (JSON syntax), restart instructions provided, verification commands suggested

## Setup Options

| Option | Action | Recommendation |
|--------|--------|-----------------|
| **A** | Interactive wizard with recommended servers | **← Recommended** for guided setup |
| **B** | Configure specific MCP servers only | When you know exactly which servers needed |
| **C** | Manual configuration with validation | For advanced customization of settings |

Your choice (A/B/C)?

## Next Steps

| Step | Action | Details |
|------|--------|---------|
| 1 | Configure selected MCP servers | Add authentication and connection details |
| 2 | Test server connections and access | Verify each server is working correctly |
| 3 | Add additional servers if needed | Expand capabilities with more MCP services |
| 4 | Save configuration and test commands | Verify setup with actual command usage |

What would you like to do next?

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% server config, Accuracy >90% prerequisite checks, Relevance >85% instructions, Efficiency <60s typical setup)

## Purpose

Interactive wizard that guides users through setting up Model Context Protocol (MCP) servers in their `~/.claude.json` configuration with prerequisite checking and validation.

## User Feedback

| Option | Action | Details |
|--------|--------|---------|
| A | Default workflow | [RECOMMENDED] |
| B | Alternative approach | For different use case |
| C | Skip | Exit without changes |

Your choice (A/B/C)?

## Next Steps

| Option | Action | Command |
|--------|--------|---------|
| 1 | Review output | Check generated content |
| 2 | Iterate or refine | Run command again [RECOMMENDED] |
| 3 | Continue workflow | Proceed to next step |
| 4 | Get help | Use /claude:guru for guidance |

What would you like to do next?


## Usage

```
/system:setup-mcp $ARGUMENTS
```

**Arguments**:

- `$1` (server-name): Specific MCP server to set up (optional - runs full wizard if omitted)
- Valid servers: `fetch`, `context7`, `markitdown`, `terraform`, `playwright`, `shadcn`, `sequential-thinking`, `all`

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - Run interactive wizard for all MCP servers
- `$ARGUMENTS = "all"` - Set up all MCP servers non-interactively
- `$ARGUMENTS = "context7"` - Set up only Context7 with API key prompt
- `$ARGUMENTS = "playwright"` - Set up only Playwright with prerequisite check

## Process

1. **Check Prerequisites**:
   - Verify `~/.claude.json` exists (create if missing)
   - Detect project path in `~/.claude.json`
   - Check installed prerequisites (Docker, Node.js, uv)
   - Report missing prerequisites with install instructions

2. **Interactive Server Selection** (if no server specified):
   - List all available MCP servers with descriptions
   - Show prerequisite status for each (✅ ready, ❌ missing, ⚠️ partial)
   - Allow user to select which servers to configure
   - Option to "Configure All" or select individually

3. **Server-Specific Configuration**:
   - **Context7**: Prompt for API key (with link to context7.com)
   - **Docker-based** (markitdown, terraform): Verify Docker running, pull images
   - **npm-based** (playwright, sequential-thinking): Verify Node.js/npm installed
   - **HTTP-based** (shadcn): No prerequisites, just add configuration
   - **Python-based** (fetch): Verify uv/uvx installed

4. **Update Configuration**:
   - Read current `~/.claude.json`
   - Locate project configuration block
   - Add or update `mcpServers` section
   - Validate JSON syntax before writing
   - Create backup: `~/.claude.json.backup`

5. **Verification**:
   - Test each configured server (optional)
   - Provide restart instructions
   - Show verification commands
   - Display summary of configured servers

## Examples

### Example 1: Full Interactive Setup

```
/system:setup-mcp
# where $ARGUMENTS = "" (run interactive wizard)

# Output:
🔧 MCP Server Setup Wizard
===========================

Checking prerequisites...
✅ Docker Desktop: Running
✅ Node.js: v20.10.0
✅ npm: 10.2.3
✅ uv: 0.1.9
❌ Context7 API key: Not configured

Found project in ~/.claude.json:
  /Users/username/.claude

Available MCP Servers:
  [1] fetch - Web content fetching (✅ Ready)
  [2] context7 - Library documentation (❌ Need API key)
  [3] markitdown - Document conversion (✅ Ready)
  [4] terraform - Infrastructure management (✅ Ready)
  [5] playwright - Browser automation (✅ Ready)
  [6] sequential-thinking - Enhanced reasoning (✅ Ready)
  [7] shadcn - UI component integration (✅ Ready)

Select servers to configure:
  [A] All servers
  [1-7] Individual servers (comma-separated)
  [Q] Quit

Selection: A

Configuring all servers...

[fetch] Adding fetch server configuration... ✅
[context7] Enter Context7 API key (get from https://context7.com):
> ctx7sk-xxxxx...
[context7] Validating API key... ✅
[markitdown] Pulling Docker image mcp/markitdown... ✅
[terraform] Pulling Docker image hashicorp/terraform-mcp-server:0.2.3... ✅
[playwright] Verifying npm package @playwright/mcp... ✅
[sequential-thinking] Verifying npm package @modelcontextprotocol/server-sequential-thinking... ✅
[shadcn] Adding shadcn HTTP endpoint... ✅

Creating backup: ~/.claude.json.backup
Updating ~/.claude.json... ✅

Setup Complete! ✨

Configured servers:
  ✅ fetch
  ✅ context7
  ✅ markitdown
  ✅ terraform
  ✅ playwright
  ✅ sequential-thinking
  ✅ shadcn

Next steps:
1. Restart Claude Code completely
2. Verify servers are loaded (check available tools)
3. Run verification tests (see below)

Verification commands:
  /system:setup-mcp verify  # Test all configured servers
```

### Example 2: Setup Single Server

```
/system:setup-mcp "context7"
# where $ARGUMENTS = "context7"

# Output:
🔧 Setting up Context7 MCP Server
===================================

Context7 provides access to up-to-date library documentation.

Get your API key:
1. Visit: https://context7.com
2. Sign up or log in
3. Navigate to API settings
4. Generate new API key (starts with ctx7sk-)

Enter Context7 API key:
> ctx7sk-xxxxx...

Validating API key... ✅

Creating backup: ~/.claude.json.backup
Updating ~/.claude.json... ✅

Context7 configured successfully! ✅

Next steps:
1. Restart Claude Code
2. Test: Ask me "Can you get React hooks documentation?"

I should use mcp__context7__resolve-library-id and mcp__context7__get-library-docs tools.
```

### Example 3: Setup with Missing Prerequisites

```
/system:setup-mcp "playwright"
# where $ARGUMENTS = "playwright"

# Output:
🔧 Setting up Playwright MCP Server
====================================

Checking prerequisites...
❌ Node.js not found

Playwright requires Node.js 18+ to be installed.

Install Node.js:
  Option 1 (Homebrew):
    brew install node

  Option 2 (nvm):
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
    nvm install 20

After installing Node.js, run this command again.

Would you like me to install Node.js via Homebrew? [y/N]:
```

### Example 4: Non-Interactive Setup All

```
/system:setup-mcp "all"
# where $ARGUMENTS = "all"

# Configures all servers with defaults (skips Context7 API key prompt if not provided)

# Output:
🔧 Setting up All MCP Servers
==============================

Checking prerequisites... ✅ All prerequisites met

Configuring servers...
  ✅ fetch
  ⚠️ context7 (skipped - API key required, run: /system:setup-mcp context7)
  ✅ markitdown
  ✅ terraform
  ✅ playwright
  ✅ sequential-thinking
  ✅ shadcn

6 of 7 servers configured successfully!

Restart Claude Code to load servers.
```

## Prerequisite Checking

### Docker-Based Servers (markitdown, terraform)

```bash
# Check Docker installed and running
docker ps > /dev/null 2>&1

# If failed:
if [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Install Docker Desktop: brew install --cask docker"
else
  echo "Install Docker: https://docs.docker.com/get-docker/"
fi
```

### npm-Based Servers (playwright, sequential-thinking)

```bash
# Check Node.js and npm
node --version  # Require v18+
npm --version

# If failed:
brew install node  # macOS
# Or: https://nodejs.org/
```

### Python-Based Servers (fetch)

```bash
# Check uv/uvx
uvx --version

# If failed:
brew install uv  # macOS
# Or: pip install uv
```

### API Key Servers (context7)

```bash
read -p "Enter Context7 API key: " api_key

# Validate format (starts with ctx7sk-)
if [[ ! $api_key =~ ^ctx7sk- ]]; then
  echo "❌ Invalid format. Key should start with 'ctx7sk-'"
  exit 1
fi
```

## Configuration Management

### Backup Strategy

```bash
# Always create backup before modifying
cp ~/.claude.json ~/.claude.json.backup

# If error occurs, restore:
cp ~/.claude.json.backup ~/.claude.json
```

### JSON Validation

```python
import json

# Validate before writing
try:
    config = json.loads(updated_content)
    # Write if valid
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
except json.JSONDecodeError as e:
    print(f"❌ Invalid JSON: {e}")
    # Restore backup
```

### Path Detection

```python
import os
from pathlib import Path

# Get this repository's path
repo_root = Path.cwd()

# Read ~/.claude.json
claude_config = Path.home() / ".claude.json"

# Find matching project
with open(claude_config) as f:
    config = json.load(f)

# Look for this project
for project_path in config.get("projects", {}):
    if Path(project_path) == repo_root:
        # Found our project
        project_config = config["projects"][project_path]
```

## Explicit Constraints

**IN SCOPE**: MCP server configuration (7 servers: fetch, context7, markitdown, terraform, playwright, sequential-thinking, shadcn), prerequisite checking (Docker, Node.js, uv), ~/.claude.json updates, server-specific setup (API keys, Docker pulls, npm installs), JSON validation, backup creation, interactive wizard mode, direct server selection
**OUT OF SCOPE**: MCP server implementation, custom server creation, server debugging/troubleshooting, project-specific MCP configs (use ~/.claude.json only), multi-user configuration, server uninstallation

## Integration Points

- **Follows**: Initial installation, new machine setup
- **Followed by**: Claude Code restart, server verification
- **Related**: `/claude:guru` (general guidance), MCP-USER-SETUP.md (manual setup guide)

## Quality Standards

- Always create backup before modifying `~/.claude.json`
- Validate JSON syntax before writing
- Check prerequisites before attempting installation
- Provide clear error messages with fix instructions
- Never store passwords/keys in plain text in repository
- Rollback on failure (restore from backup)

## Output

- Interactive prompts for user input
- Prerequisite check results
- Configuration progress indicators
- Success/error messages with clear next steps
- Summary of configured servers
- Restart and verification instructions
