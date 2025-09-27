# MCP Setup Guide - Context7 & Playwright Integration

This guide walks you through setting up MCP (Model Context Protocol) servers for enhanced Claude Code functionality.

## Overview

The Claude Code Command System integrates with two powerful MCP servers:

- **Context7 MCP** - Access up-to-date library documentation and code examples
- **Playwright MCP** - Browser automation for testing and UI analysis

## Prerequisites

- Claude Code CLI installed
- Node.js 18+ (for MCP server installation)
- Python 3.8+ (for some MCP server dependencies)

## Context7 MCP Setup

Context7 provides access to current library documentation and code examples from popular frameworks and libraries.

### 1. Install Context7 MCP Server

```bash
# Install the Context7 MCP server
npm install -g @context7/mcp-server

# Or install locally in your project
npm install @context7/mcp-server
```text

### 2. Configure Context7 in Claude Code

Add Context7 to your Claude Code configuration:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["@context7/mcp-server"],
      "env": {
        "CONTEXT7_API_KEY": "your-api-key-here"
      }
    }
  }
}
```python

### 3. Get Context7 API Key

1. Visit [Context7 website](https://context7.com)
2. Sign up for an account
3. Generate an API key from your dashboard
4. Add the key to your environment variables:

```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export CONTEXT7_API_KEY="your-api-key-here"

# Or create a .env file in your project root
echo "CONTEXT7_API_KEY=your-api-key-here" >> .env
```text

### 4. Verify Context7 Setup

Test the Context7 integration:

```bash
# In Claude Code, try resolving a library
claude "Use Context7 to find React documentation"
```yaml

The system will automatically use these tools:

- `mcp__context7__resolve-library-id` - Map package names to documentation IDs
- `mcp__context7__get-library-docs` - Fetch current documentation content

## Playwright MCP Setup

Playwright MCP enables browser automation for testing, UI analysis, and web scraping tasks.

### 1. Install Playwright MCP Server

```bash
# Install Playwright MCP server
npm install -g @playwright/mcp-server

# Install Playwright browsers
npx playwright install
```text

### 2. Configure Playwright in Claude Code

Add Playwright to your Claude Code configuration:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp-server"],
      "env": {
        "PLAYWRIGHT_BROWSER": "chromium"
      }
    }
  }
}
```text

### 3. Browser Setup

Configure which browsers Playwright should use:

```bash
# Install all browsers (recommended)
npx playwright install

# Or install specific browsers
npx playwright install chromium firefox webkit
```text

### 4. Verify Playwright Setup

Test the Playwright integration:

```bash
# In Claude Code, try a browser automation task
claude "Use Playwright to take a screenshot of example.com"
```bash

Available Playwright tools include:

- `mcp__playwright__browser_navigate` - Navigate to URLs
- `mcp__playwright__browser_click` - Click elements
- `mcp__playwright__browser_type` - Type text
- `mcp__playwright__browser_snapshot` - Take accessibility snapshots
- `mcp__playwright__browser_take_screenshot` - Capture screenshots
- And many more browser automation capabilities

## Complete Configuration Example

Here's a complete Claude Code configuration with both MCP servers:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["@context7/mcp-server"],
      "env": {
        "CONTEXT7_API_KEY": "your-context7-key"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp-server"],
      "env": {
        "PLAYWRIGHT_BROWSER": "chromium",
        "PLAYWRIGHT_HEADLESS": "true"
      }
    }
  },
  "tools": {
    "allowedMcpTools": [
      "mcp__context7__resolve-library-id",
      "mcp__context7__get-library-docs",
      "mcp__playwright__browser_navigate",
      "mcp__playwright__browser_click",
      "mcp__playwright__browser_type",
      "mcp__playwright__browser_snapshot",
      "mcp__playwright__browser_take_screenshot",
      "mcp__playwright__browser_wait_for",
      "mcp__playwright__browser_evaluate"
    ]
  }
}
```yaml

## Command Integration

### Commands That Use Context7

Several commands automatically leverage Context7 for up-to-date documentation:

- `/docs:extract-external` - Primary Context7 integration command
- `/docs:api` - Current API documentation standards
- `/review:security` - Latest OWASP guidelines and vulnerabilities
- `/analyze:dependencies` - Current security advisories
- `/implement` - Framework-specific best practices

### Commands That Use Playwright

Playwright integration enhances browser-related tasks:

- `/review:design` - UI analysis and accessibility testing
- `/test` commands - Automated browser testing
- Any command involving web interface analysis

## Agent Orchestra Integration

### Agents Using Context7

- **documenter** - For up-to-date documentation standards
- **code-writer** - For current API patterns and implementations
- **reviewer** - For latest security practices and guidelines
- **bug-fixer** - For known issue patterns and solutions
- **research-orchestrator** - For gathering current best practices

### Agents Using Playwright

- **test-writer** - For browser-based testing automation
- **reviewer** - For UI and accessibility analysis
- **bug-fixer** - For reproducing and analyzing UI bugs

## Troubleshooting

### Context7 Issues

**API Key Not Working:**

```bash
# Verify your API key is set
echo $CONTEXT7_API_KEY

# Test the key directly
curl -H "Authorization: Bearer $CONTEXT7_API_KEY" https://api.context7.com/health
```yaml

**Library Not Found:**

- Use `mcp__context7__resolve-library-id` to find correct library IDs
- Try alternative library names or versions
- Check Context7 documentation for supported libraries

### Playwright Issues

**Browsers Not Installed:**

```bash
# Reinstall browsers
npx playwright install --force

# Check installed browsers
npx playwright install --dry-run
```text

**Permission Errors:**

```bash
# On Linux, install dependencies
sudo npx playwright install-deps

# On macOS, grant accessibility permissions
# System Preferences > Security & Privacy > Accessibility
```text

**Headless Mode Issues:**

```bash
# Try running with GUI for debugging
export PLAYWRIGHT_HEADLESS=false
```

## Environment Variables Reference

### Context7 Variables

- `CONTEXT7_API_KEY` - Your Context7 API key (required)
- `CONTEXT7_BASE_URL` - Custom API endpoint (optional)
- `CONTEXT7_TIMEOUT` - Request timeout in milliseconds (default: 30000)

### Playwright Variables

- `PLAYWRIGHT_BROWSER` - Browser to use (chromium, firefox, webkit)
- `PLAYWRIGHT_HEADLESS` - Run in headless mode (true/false)
- `PLAYWRIGHT_TIMEOUT` - Page timeout in milliseconds (default: 30000)
- `PLAYWRIGHT_VIEWPORT_WIDTH` - Browser width (default: 1280)
- `PLAYWRIGHT_VIEWPORT_HEIGHT` - Browser height (default: 720)

## Security Considerations

### Context7 Security

- Store API keys in environment variables, never in code
- Use project-specific API keys when possible
- Regularly rotate API keys
- Monitor API usage through Context7 dashboard

### Playwright Security

- Run in sandboxed environments when possible
- Be cautious with `--no-sandbox` flags
- Use headless mode in production
- Limit network access for automated browsers
- Regularly update Playwright and browsers

## Next Steps

1. **Test Integration** - Try both MCP servers with simple commands
2. **Explore Commands** - Use `/docs:extract-external` and `/review:design`
3. **Custom Workflows** - Create custom commands that leverage MCP capabilities
4. **Monitor Usage** - Check logs and performance of MCP integrations

For advanced configuration and custom MCP server development, see the [Developer Guide](developer-guide.md).
