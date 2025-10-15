# MCP User Configuration Setup

This guide helps you set up **all MCP servers** in your user-local configuration.

## MCP Configuration Architecture

All MCP servers are configured in `~/.claude.json` (per-project nested config). This repository provides a template that you'll merge into your configuration.

**Why user-local configuration?**

- Contains personal API keys (context7)
- Uses system-specific paths (Docker, npm)
- Requires local prerequisites (Docker Desktop, Node.js)
- Not checked into git (personal settings)

## MCP Servers Included

**Documentation & Content:**

- **fetch** - Web content fetching (Python via uvx)
- **context7** - Library documentation (HTTP, requires API key)

**Document Processing:**

- **markitdown** - Document conversion to Markdown (Docker)

**Infrastructure:**

- **terraform** - Terraform management (Docker)

**Browser & UI:**

- **playwright** - Browser automation and testing (npm)
- **shadcn** - shadcn/ui component integration (HTTP)

**Reasoning:**

- **sequential-thinking** - Enhanced reasoning capabilities (npm)

## Setup Instructions

### Step 1: Install Prerequisites

#### macOS / Linux

```bash
# Python package manager (for fetch server)
brew install uv              # macOS
# Or: pip install uv         # Linux

# Node.js (for playwright, sequential-thinking)
brew install node            # macOS
# Or use nvm (cross-platform)

# Docker Desktop (for markitdown and terraform)
brew install --cask docker   # macOS
# Linux: Follow https://docs.docker.com/engine/install/
```

#### Windows

```powershell
# Python package manager (for fetch server)
pip install uv

# Node.js (for playwright, sequential-thinking)
# Download from: https://nodejs.org/
# Or use nvm-windows

# Docker Desktop (for markitdown and terraform)
# Download from: https://www.docker.com/products/docker-desktop/
# Ensure Docker is in PATH after installation
```

### Step 2: Get Context7 API Key

1. Visit: <https://context7.com>
2. Sign up or log in
3. Navigate to API settings
4. Generate a new API key (starts with `ctx7sk-`)
5. Copy the API key

### Step 3: Locate Your Project in `~/.claude.json`

Open `~/.claude.json` in your home directory and find this project:

**macOS/Linux:**

```json
{
  "projects": {
    "/Users/yourusername/path/to/.claude": {
      "mcpServers": {},
    }
  }
}
```

**Windows:**

```json
{
  "projects": {
    "C:\\Users\\yourusername\\path\\to\\.claude": {
      "mcpServers": {},
    }
  }
}
```

**Note:** The project path should match this repository's `.claude` directory path exactly (use absolute path).

### Step 4: Add All MCP Servers

Replace the empty `"mcpServers": {}` with the configuration from `.claude.json.user-local.template` (macOS/Linux) or `.claude.json.windows.template` (Windows).

**Cross-Platform Configuration (Works on all platforms):**

```json
{
  "projects": {
    "YOUR_PROJECT_PATH_HERE": {
      "mcpServers": {
        "fetch": {
          "command": "uvx",
          "args": ["mcp-server-fetch"]
        },
        "markitdown": {
          "command": "docker",
          "args": ["run", "--rm", "-i", "-v", "${HOME}:/workdir", "mcp/markitdown"]
        },
        "terraform": {
          "command": "docker",
          "args": ["run", "-i", "--rm", "hashicorp/terraform-mcp-server:0.2.3"]
        },
        "playwright": {
          "type": "stdio",
          "command": "npx",
          "args": ["@playwright/mcp@latest"],
          "env": {}
        },
        "context7": {
          "type": "http",
          "url": "https://mcp.context7.com/mcp",
          "headers": {
            "CONTEXT7_API_KEY": "ctx7sk-your-actual-api-key-here"
          }
        },
        "sequential-thinking": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
        },
        "shadcn": {
          "type": "http",
          "url": "https://www.shadcn.io/api/mcp"
        }
      }
    }
  }
}
```

**Important Notes:**

- Replace `YOUR_PROJECT_PATH_HERE` with your actual project path
- Replace `ctx7sk-your-actual-api-key-here` with your actual Context7 API key
- **macOS/Linux**: Uses `${HOME}` for home directory (works automatically)
- **Windows**: `${HOME}` is also supported and resolves to user profile
- **Docker command**: Use `docker` (not full path) - works when Docker is in PATH

### Step 5: Pull Docker Images

```bash
# Pull required Docker images (one-time setup)
docker pull mcp/markitdown:latest
docker pull hashicorp/terraform-mcp-server:0.2.3
```

### Step 6: Restart Claude Code

After updating `~/.claude.json`:

1. Save the file
2. Close Claude Code completely
3. Reopen Claude Code
4. All MCP servers should now be available

## Verification

### Test fetch

```bash
# Verify uvx can access the package
uvx mcp-server-fetch --help
```

### Test Docker servers

```bash
# Verify Docker is running and images are pulled
docker images | grep -E "mcp/markitdown|terraform-mcp-server"
```

### Test Playwright

Ask Claude Code to take a screenshot:

```text
Can you take a screenshot of https://example.com?
```

Claude should use `mcp__playwright__browser_navigate` and `mcp__playwright__browser_take_screenshot` tools.

### Test Context7

Ask Claude Code to fetch documentation:

```text
Can you get the latest React documentation for hooks?
```

Claude should use `mcp__context7__resolve-library-id` and `mcp__context7__get-library-docs` tools.

### Test shadcn

Ask Claude Code about shadcn/ui components:

```text
What shadcn/ui components are available?
```

Claude should use `mcp__shadcn__getComponents` tool.

### Test sequential-thinking

The sequential-thinking server enhances Claude's reasoning automatically - no explicit test needed. It provides structured thinking capabilities in the background.

### Check Available Tools

In Claude Code, you can view available MCP tools by looking at the permissions in your conversation.

## Troubleshooting

### fetch Server Not Working

**Problem:** "Command not found: uvx"

**Solution:**

1. Install uv: `brew install uv`
2. Or use pip: `pip install uv`
3. Verify: `uvx --version`

### Context7 Not Working

**Problem:** "Error: Unauthorized" or "Invalid API key"

**Solution:**

1. Verify your API key is correct in `~/.claude.json`
2. Ensure there are no extra spaces or quotes around the key
3. Check that the key starts with `ctx7sk-`
4. Generate a new API key if needed

### Docker Servers Not Working

**Problem:** "Docker command not found" or "Cannot connect to Docker daemon"

**Solution:**

1. Verify Docker Desktop is installed and running
2. Check Docker is accessible: `docker ps`
3. If using different Docker path, update command in configuration
4. Ensure images are pulled: `docker images`

### Playwright Not Working

**Problem:** "Command not found: npx" or "Playwright failed to start"

**Solution:**

1. Verify Node.js is installed: `node --version` (should be v18+)
2. Verify npx is available: `npx --version`
3. Try manually installing: `npm install -g @playwright/mcp@latest`
4. Check your PATH includes npm global bin directory

### VSCode MCP Server Not Working

**Problem:** "Connection refused" or "Cannot connect to localhost:3000"

**Solution:**

1. Verify mcp-remote server is running: `ps aux | grep mcp-remote`
2. Start the server: `mcp-remote start --port 3000`
3. Check port 3000 is not used by another service: `lsof -i :3000`
4. If you don't need VSCode integration, remove this server from config

### sequential-thinking Not Working

**Problem:** "Package not found" or installation errors

**Solution:**

1. Update npm: `npm install -g npm@latest`
2. Clear npm cache: `npm cache clean --force`
3. Try manual install: `npm install -g @modelcontextprotocol/server-sequential-thinking`

### shadcn Not Working

**Problem:** "Cannot reach shadcn.io API"

**Solution:**

1. Verify internet connection
2. Check shadcn.io is accessible: `curl https://www.shadcn.io/api/mcp`
3. May require VPN if region-blocked

### MCP Servers Not Loading

**Problem:** MCP servers don't appear after restart

**Solution:**

1. Verify the project path in `~/.claude.json` matches exactly
   - Use absolute path: `/Users/yourusername/path/to/.claude`
   - Check for typos in the path
2. Verify JSON syntax is valid (no trailing commas, proper quotes)
3. Check Claude Code logs for errors
4. Ensure all prerequisites are installed

### JSON Syntax Errors

**Problem:** "Failed to parse ~/.claude.json"

**Solution:**

1. Use a JSON validator to check syntax
2. Common issues:
   - Missing or extra commas
   - Unmatched brackets/braces
   - Unescaped quotes in strings
3. Make a backup before editing: `cp ~/.claude.json ~/.claude.json.backup`

## Security Best Practices

### API Key Security

1. **Never commit** `~/.claude.json` to git (it's in your home directory, not the repo)
2. **Never share** your Context7 API key publicly
3. **Rotate keys** periodically from Context7 dashboard
4. **Use environment variables** if sharing team configurations

### Docker Security

1. **Review images** before pulling (use official sources)
2. **Keep Docker updated** for security patches
3. **Limit volume mounts** to necessary directories only
4. **Monitor running containers**: `docker ps`

### Safe Editing

1. **Backup first**: `cp ~/.claude.json ~/.claude.json.backup`
2. **Validate JSON** before saving (use an editor with JSON validation)
3. **Test immediately** after changes by restarting Claude Code
4. **Keep template** handy at `.claude.json.user-local.template`

## Template Reference

The template configuration is maintained at:

```text
.claude/.claude.json.user-local.template
```

If you need to reconfigure or set up on a new machine, copy from the template and replace:

- `YOUR_CONTEXT7_API_KEY_HERE` with your actual Context7 API key

## Complete Configuration Structure

### Your `~/.claude.json` Structure

```json
{
  "projects": {
    "/absolute/path/to/.claude": {
      "mcpServers": {
        "fetch": {},
        "markitdown": {},
        "terraform": {},
        "playwright": {},
        "context7": {},
        "sequential-thinking": {},
        "shadcn": {}
      },
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "hasTrustDialogAccepted": true
    }
  }
}
```

### All 7 MCP Servers Available

1. **fetch** - Web content fetching
2. **markitdown** - Document conversion
3. **terraform** - Infrastructure management
4. **playwright** - Browser automation
5. **context7** - Library documentation
6. **sequential-thinking** - Enhanced reasoning
7. **shadcn** - UI component integration

## Getting Help

If you encounter issues:

1. **Check Documentation**
   - [MCP Configuration Guide](docs/user/mcp-configuration-guide.md)
   - [Claude Code MCP Docs](https://docs.claude.com/en/docs/claude-code/mcp)

2. **Verify Prerequisites**
   - Docker Desktop running
   - Node.js/npx installed
   - uv/uvx installed
   - Valid Context7 API key

3. **Check Logs**
   - Claude Code debug output
   - Docker logs: `docker logs <container>`

4. **Ask for Help**
   - Create an issue in this repository
   - Include sanitized error messages (remove API keys)

## Related Documentation

- [MCP Configuration Guide](docs/user/mcp-configuration-guide.md) - Comprehensive MCP details
- [Project CLAUDE.md](CLAUDE.md) - Section "🔌 MCP Integration"
- `.claude.json.user-local.template` - Template for all MCP servers
