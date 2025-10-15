# Windows Compatibility Guide

This guide documents Windows-specific considerations for using the Claude Code Command System.

## MCP Server Compatibility

### ✅ Fully Compatible (No Changes Needed)

These MCP servers work identically on Windows, macOS, and Linux:

**1. fetch** - Web content fetching

- **Command**: `uvx` (cross-platform Python tool)
- **Prerequisites**: Python + uv installed
- **Windows Install**: `pip install uv`

**2. playwright** - Browser automation

- **Command**: `npx` (cross-platform npm)
- **Prerequisites**: Node.js 18+
- **Windows Install**: Download from nodejs.org

**3. sequential-thinking** - Enhanced reasoning

- **Command**: `npx` (cross-platform npm)
- **Prerequisites**: Node.js 18+
- **Windows Install**: Download from nodejs.org

**4. context7** - Library documentation

- **Type**: HTTP endpoint
- **Prerequisites**: API key only (no local installation)
- **Windows**: Works identically

**5. shadcn** - UI component integration

- **Type**: HTTP endpoint
- **Prerequisites**: None (public API)
- **Windows**: Works identically

### ⚠️ Platform Considerations (Docker-based)

**6. markitdown** - Document conversion

- **Command**: `docker` (works cross-platform when in PATH)
- **Prerequisites**: Docker Desktop installed and running
- **Windows Notes**:
  - Docker Desktop must be in system PATH
  - Uses `${HOME}` variable (resolves to user profile on Windows)
  - Works identically once Docker is configured

**7. terraform** - Infrastructure management

- **Command**: `docker` (works cross-platform when in PATH)
- **Prerequisites**: Docker Desktop installed and running
- **Windows Notes**: Same as markitdown

## Key Configuration Changes

### Template Updates for Cross-Platform Compatibility

**Before (macOS-specific):**

```json
"markitdown": {
  "command": "/Applications/Docker.app/Contents/Resources/bin/docker",
  "args": ["run", "--rm", "-i", "-v", "${HOME}:/workdir", "mcp/markitdown"]
}
```

**After (cross-platform):**

```json
"markitdown": {
  "command": "docker",
  "args": ["run", "--rm", "-i", "-v", "${HOME}:/workdir", "mcp/markitdown"]
}
```

**Why This Works:**

- `docker` command works when Docker Desktop adds itself to PATH
- `${HOME}` environment variable resolves correctly on:
  - **macOS/Linux**: `/Users/username` or `/home/username`
  - **Windows**: `C:\Users\username` (via Docker Desktop's variable expansion)

## Windows-Specific Setup

### Prerequisites Installation

**Python + uv (for fetch):**

```powershell
# Install Python from python.org, then:
pip install uv

# Verify installation
uvx --version
```

**Node.js + npm (for playwright, sequential-thinking):**

```powershell
# Download installer from nodejs.org
# Or use Chocolatey:
choco install nodejs

# Verify installation
node --version  # Should be v18+
npx --version
```

**Docker Desktop (for markitdown, terraform):**

```powershell
# Download from docker.com/products/docker-desktop/
# Or use Chocolatey:
choco install docker-desktop

# After installation:
# 1. Start Docker Desktop
# 2. Verify Docker is in PATH:
docker --version

# Pull required images:
docker pull mcp/markitdown:latest
docker pull hashicorp/terraform-mcp-server:0.2.3
```

### Path Configuration

Ensure these commands are in your system PATH:

1. **Check Current PATH:**

```powershell
$env:PATH -split ';'
```

1. **Add Docker to PATH** (if not automatic):

```powershell
# Docker Desktop usually adds itself to PATH automatically
# If not, add: C:\Program Files\Docker\Docker\resources\bin
```

1. **Add Node.js to PATH** (if not automatic):

```powershell
# Node.js installer adds to PATH automatically
# npm global bin is usually: C:\Users\YourName\AppData\Roaming\npm
```

### Project Path Format

Windows uses backslashes in paths, which must be escaped in JSON:

**Correct Windows Path in ~/.claude.json:**

```json
{
  "projects": {
    "C:\\Users\\username\\.claude": {
      "mcpServers": { ... }
    }
  }
}
```

**Common Mistakes:**

```json
// ❌ Wrong - single backslashes
"C:\Users\username\.claude"

// ❌ Wrong - forward slashes (not recognized by Windows)
"C:/Users/username/.claude"

// ✅ Correct - escaped backslashes
"C:\\Users\\username\\.claude"
```

## Troubleshooting Windows-Specific Issues

### Docker Not Found

**Problem:** `'docker' is not recognized as an internal or external command`

**Solution:**

1. Verify Docker Desktop is installed and running
2. Open new PowerShell/Command Prompt (PATH updates require restart)
3. Add Docker to PATH manually if needed:

   ```powershell
   setx PATH "$env:PATH;C:\Program Files\Docker\Docker\resources\bin"
   ```

4. Restart Claude Code after PATH changes

### uvx Not Found

**Problem:** `'uvx' is not recognized as an internal or external command`

**Solution:**

1. Ensure Python Scripts directory is in PATH:

   ```powershell
   python -m site --user-base
   # Add the \Scripts subdirectory to PATH
   ```

2. Or install uv globally:

   ```powershell
   pip install --user uv
   ```

3. Verify: `uvx --version`

### npx Not Found

**Problem:** `'npx' is not recognized as an internal or external command`

**Solution:**

1. Reinstall Node.js from nodejs.org (includes npm/npx)
2. Verify Node.js installation:

   ```powershell
   node --version
   npm --version
   ```

3. Ensure npm global bin in PATH:

   ```powershell
   npm config get prefix
   # Add \node_modules\.bin to PATH
   ```

### Docker Volume Mount Issues

**Problem:** Docker can't access `${HOME}` or volume mounts fail

**Solution:**

1. Ensure Docker Desktop has file sharing enabled:
   - Open Docker Desktop Settings
   - Go to Resources → File Sharing
   - Add `C:\Users` if not already present
2. Restart Docker Desktop
3. Verify with: `docker run --rm -v ${HOME}:/test alpine ls /test`

### PowerShell Execution Policy

**Problem:** Scripts blocked by execution policy

**Solution:**

```powershell
# Check current policy
Get-ExecutionPolicy

# Set to RemoteSigned (allows local scripts)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Windows vs Unix Path Translation

The system uses Python's `pathlib.Path` for cross-platform compatibility:

```python
from pathlib import Path

# Works on all platforms
project_root = Path.cwd()
home_dir = Path.home()
claude_config = Path.home() / ".claude.json"

# Automatically uses correct separator:
# Windows: C:\Users\username\.claude.json
# Unix: /Users/username/.claude.json
```

## Command Compatibility Matrix

| Command | Windows | macOS | Linux | Notes |
|---------|---------|-------|-------|-------|
| `uvx` | ✅ | ✅ | ✅ | Requires Python + uv |
| `npx` | ✅ | ✅ | ✅ | Requires Node.js |
| `docker` | ✅ | ✅ | ✅ | Requires Docker in PATH |
| HTTP endpoints | ✅ | ✅ | ✅ | Network only, no install |

## Testing Your Setup

### Verify All Prerequisites

```powershell
# Check Python + uv
python --version
uvx --version

# Check Node.js + npm
node --version
npm --version
npx --version

# Check Docker
docker --version
docker ps

# Check PATH includes all required binaries
where.exe docker
where.exe npx
where.exe uvx
```

### Test MCP Servers

After configuration, verify each server:

```powershell
# Test fetch server
uvx mcp-server-fetch --help

# Test Docker servers
docker pull mcp/markitdown:latest
docker pull hashicorp/terraform-mcp-server:0.2.3
docker images

# Test npm packages
npx @playwright/mcp@latest --help
npx @modelcontextprotocol/server-sequential-thinking --help
```

## Performance Considerations

### Docker on Windows

Docker Desktop on Windows uses WSL2 (Windows Subsystem for Linux) for better performance:

1. **Enable WSL2:**

   ```powershell
   wsl --install
   wsl --set-default-version 2
   ```

2. **Configure Docker to use WSL2:**
   - Docker Desktop Settings → General
   - Enable "Use the WSL 2 based engine"

3. **Performance Impact:**
   - With WSL2: Performance similar to native Linux
   - Without WSL2 (Hyper-V): Slower file I/O

### Antivirus Exclusions

Windows Defender may slow down Node.js and Docker operations:

**Recommended Exclusions:**

- `C:\Users\YourName\.claude`
- `C:\Users\YourName\AppData\Roaming\npm`
- Docker Desktop installation directory
- WSL2 distributions (if using Docker with WSL2)

## Cross-Platform Development Tips

### Use Forward Slashes in Code

Python and Node.js accept forward slashes on Windows:

```python
# Works on all platforms
path = Path("scripts/hooks/init-session.py")
```

### Environment Variables

Prefer cross-platform environment variables:

```json
// ✅ Works everywhere
"${HOME}:/workdir"

// ❌ Unix-only
"$HOME:/workdir"

// ❌ Windows-only
"%USERPROFILE%:/workdir"
```

### Line Endings

Git should handle line endings automatically, but verify:

```powershell
# Check git config
git config --global core.autocrlf

# Should be "true" on Windows
git config --global core.autocrlf true
```

## Summary

✅ **All 7 MCP servers work on Windows** with proper prerequisites

✅ **Templates updated** to use cross-platform configuration

✅ **Key changes**:

- Use `docker` command (not absolute path)
- Use `${HOME}` variable (works on all platforms)
- Escape backslashes in Windows paths

✅ **Prerequisites**:

- Python + uv (for fetch)
- Node.js + npm (for playwright, sequential-thinking)
- Docker Desktop (for markitdown, terraform)

✅ **No code changes needed** - Python hooks and scripts use `pathlib.Path` for cross-platform compatibility
