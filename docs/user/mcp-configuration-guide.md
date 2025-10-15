# MCP Configuration Guide

This guide explains how MCP servers are configured in this repository.

## Configuration Architecture

### User-Local MCP Configuration (`~/.claude.json`)

**Location:** `~/.claude.json` (in user's home directory, per-project nested config)

**Purpose:** All MCP servers for this project are configured in the user-local file.

**Why user-local only?**

- Contains personal API keys (context7)
- Uses system-specific paths (Docker, npm, Python)
- Requires local prerequisites (Docker Desktop, Node.js, uv)
- Not checked into git (personal configuration)

**Current Configuration:**
All 7 MCP servers are configured in `~/.claude.json`:

- **fetch** - Web content fetching (Python via uvx)
- **markitdown** - Document conversion to Markdown (Docker)
- **terraform** - Terraform infrastructure management (Docker)
- **playwright** - Browser automation (stdio via npx)
- **context7** - Library documentation (HTTP with API key)
- **sequential-thinking** - Enhanced reasoning (npm)
- **shadcn** - UI component integration (HTTP)

## MCP Server Details

### fetch

```json
{
  "command": "uvx",
  "args": ["mcp-server-fetch"]
}
```

- **Type:** Python-based (via uvx)
- **Purpose:** Fetch web content and convert to markdown
- **Requirements:** `uv` must be installed (`brew install uv`)
- **No Docker required**

### markitdown

```json
{
  "command": "/Applications/Docker.app/Contents/Resources/bin/docker",
  "args": [
    "run",
    "--rm",
    "-i",
    "-v",
    "${HOME}:/workdir",
    "mcp/markitdown"
  ]
}
```

- **Type:** Docker container
- **Purpose:** Convert files and office documents to Markdown
- **Requirements:** Docker Desktop running
- **Volume Mount:** `${HOME}:/workdir` (user-agnostic)
- **Image:** `mcp/markitdown:latest` (910MB)

### terraform

```json
{
  "command": "/Applications/Docker.app/Contents/Resources/bin/docker",
  "args": [
    "run",
    "-i",
    "--rm",
    "hashicorp/terraform-mcp-server:0.2.3"
  ]
}
```

- **Type:** Docker container
- **Purpose:** Terraform infrastructure management
- **Requirements:** Docker Desktop running
- **Image:** `hashicorp/terraform-mcp-server:0.2.3` (10.2MB)

### context7

```json
{
  "type": "http",
  "url": "https://mcp.context7.com/mcp",
  "headers": {
    "CONTEXT7_API_KEY": "ctx7sk-xxxxx"
  }
}
```

- **Type:** HTTP-based cloud service
- **Purpose:** Up-to-date library and framework documentation
- **Requirements:** API key (user-specific)
- **User-local only:** Contains personal API key

### playwright

```json
{
  "type": "stdio",
  "command": "npx",
  "args": ["@playwright/mcp@latest"]
}
```

- **Type:** npm package (stdio)
- **Purpose:** Browser automation for testing and screenshots
- **Requirements:** Node.js and npx
- **Auto-installed:** Via npx when first used

### sequential-thinking

```json
{
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-sequential-thinking"
  ]
}
```

- **Type:** npm package (stdio)
- **Purpose:** Enhanced reasoning and structured thinking capabilities
- **Requirements:** Node.js and npx
- **Auto-installed:** Via npx -y when first used
- **Background:** Runs automatically to enhance Claude's reasoning

### shadcn

```json
{
  "type": "http",
  "url": "https://www.shadcn.io/api/mcp"
}
```

- **Type:** HTTP-based cloud service
- **Purpose:** shadcn/ui component integration and queries
- **Requirements:** Internet connection
- **No setup:** Direct HTTP connection to shadcn.io API

## Tool References in Code

MCP tools are referenced in agent and command frontmatter:

```yaml
# Example from agents
tools: mcp__context7__resolve-library-id, mcp__context7__get-library-docs, WebSearch, Write, Edit, Read, Grep, Glob

# Playwright tools
tools: mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_click

# shadcn tools
tools: mcp__shadcn__getComponents, mcp__shadcn__getComponent
```

**Format:** `mcp__<server-name>__<tool-name>`

## Integration Architecture

**Delegation Pattern**: Commands → Agents → MCP Tools

### How MCP Tools Are Used

**Commands** (Orchestration):

- Coordinate workflows and delegate to agents
- NEVER use MCP tools directly (architecture constraint)
- Exception: Main thread can use MCP for quick lookups (rare)

**Domain Analysts** (Primary MCP Consumers):

- Research agents: fetch, context7, markitdown for external content
- Security agents: fetch, context7, playwright, terraform for audits
- Architecture agents: context7, markitdown, terraform for design analysis
- UI agents: shadcn for component queries

**MCP Tool Categories**:

1. **Always-Available Tools** (Traditional MCP):
   - `mcp__fetch__fetch` - Web content retrieval
   - `mcp__markitdown__convert_to_markdown` - Document conversion
   - `mcp__terraform__*` - Terraform registry/docs access
   - `mcp__context7__*` - Library documentation
   - `mcp__playwright__*` - Browser automation
   - `mcp__shadcn__*` - UI components

2. **Reasoning Framework** (Special):
   - **sequential-thinking** - Not called like traditional tools
   - Invoked by model for complex multi-step reasoning
   - Provides transparent, revisable step-by-step analysis
   - Can integrate other MCP tools mid-reasoning

### Sequential Thinking MCP

**Purpose**: Structured multi-step reasoning with transparency and revision capability

**When Agents Use It**:

- Large-scale architectural decomposition (architecture-analyst)
- Multi-domain research requiring ordered investigation (research-analyst)
- Complex refactoring with phased transformations (refactoring-analyst)
- Systematic quality assessment across dimensions (quality-analyst)
- Structured threat modeling with OWASP categories (security-analyst)

**How It Works**:

1. Agent describes complex task requiring sequential reasoning
2. Model invokes sequential-thinking framework
3. Breaks problem into numbered, visible steps
4. Can revise/backtrack during reasoning
5. Can call other MCP tools mid-process (e.g., fetch docs at step 3)
6. Returns structured audit trail with justification

**Example** (architecture-analyst analyzing microservices):

```text
Step 1: Identify service boundaries and data flows
Step 2: Evaluate coupling between services
Step 3: [Uses terraform tools] Analyze infrastructure patterns
Step 4: [Uses context7] Fetch microservices best practices
Step 5: Assess SOLID principle adherence
Step 6: Generate prioritized recommendations
```

**Key Benefit**: Transparent reasoning with ability to backtrack, unlike black-box extended thinking

**Rationale**: Commands orchestrate → Agents leverage domain expertise + MCP tools → Main thread implements

## Permissions

MCP tools are allowed in `settings.json`:

```json
"allow": [
  "mcp__context7",
  "mcp__playwright",
  "mcp__shadcn",
  "mcp__ide",
  "mcp__sequential-thinking",
  // ... other tools
]
```

## Prerequisites

### For All Users

1. **Docker Desktop** (for markitdown and terraform)

   ```bash
   brew install --cask docker
   # Start Docker Desktop from Applications
   ```

2. **uv** (for fetch server)

   ```bash
   brew install uv
   # Or: curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Node.js** (for playwright, sequential-thinking)

   ```bash
   brew install node
   # Or use nvm
   ```

### For Docker on macOS

If `docker` command is not in PATH, the full path is used:

```text
/Applications/Docker.app/Contents/Resources/bin/docker
```

To add to PATH permanently:

```bash
echo 'export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## Verifying MCP Servers

### Test fetch server

```bash
uvx mcp-server-fetch
# Should start without errors
```

### Test Docker images

```bash
docker images | grep -E "mcp/markitdown|terraform-mcp-server"
# Should show:
# mcp/markitdown                   latest        e6f01428d8c8   910MB
# hashicorp/terraform-mcp-server   0.2.3         b64972eb0a0a   10.2MB
```

### Test Docker access

```bash
docker ps
# Should list running containers (or be empty but not error)
```

### Test sequential-thinking

```bash
# Verify npx can access the package
npx @modelcontextprotocol/server-sequential-thinking --help
```

### Test shadcn API

```bash
# Verify shadcn.io API is accessible
curl https://www.shadcn.io/api/mcp
```

## Configuration Template

The repository provides a template at `.claude.json.user-local.template` with all servers pre-configured.

To set up:

1. Copy configuration from template to your `~/.claude.json`
2. Replace `YOUR_CONTEXT7_API_KEY_HERE` with your actual Context7 API key
3. Install prerequisites (Docker, uv, Node.js)
4. Restart Claude Code

See [MCP User Setup](../../MCP-USER-SETUP.md) for detailed step-by-step instructions.

## Troubleshooting

### Docker Not Found

```bash
# Check if Docker Desktop is installed
ls -la /Applications/Docker.app

# Check if running
docker ps

# If not running, start Docker Desktop from Applications
open /Applications/Docker.app
```

### MCP Server Not Loading

1. Check Docker is running (for markitdown/terraform)
2. Verify image is pulled: `docker images`
3. Check Claude Code permissions in `settings.json`
4. Restart Claude Code after configuration changes

### sequential-thinking Not Working

1. Update npm: `npm install -g npm@latest`
2. Clear cache: `npm cache clean --force`
3. Manual install: `npm install -g @modelcontextprotocol/server-sequential-thinking`

### shadcn API Unreachable

1. Check internet connection
2. Verify shadcn.io is accessible: `curl https://www.shadcn.io`
3. May require VPN if region-blocked

### Permission Denied

- Docker commands may fail if Docker Desktop is not running
- Ensure MCP tool names are in `settings.json` allow list
- Check that all npm packages can be executed by current user

## Best Practices

1. **Path Variables**
   - Use `${HOME}` instead of `/Users/username`
   - Use absolute paths for Docker binary on macOS

2. **Documentation**
   - Document configuration changes in this guide
   - Update `CLAUDE.md` when adding servers
   - Keep template in sync with documentation

3. **Version Pinning**
   - Pin Docker image versions (e.g., `:0.2.3`)
   - Use `@latest` for npm packages that auto-update
   - Use `@next` for packages in active development (mcp-remote)
   - Document version requirements

4. **Security**
   - Never commit API keys to git
   - Use environment variables for sensitive data
   - Rotate API keys periodically

## Related Documentation

- [MCP User Setup](../../MCP-USER-SETUP.md) - Step-by-step setup guide
- Project CLAUDE.md - Section "🔌 MCP Integration"
- [Claude Code MCP Documentation](https://docs.claude.com/en/docs/claude-code/mcp)
