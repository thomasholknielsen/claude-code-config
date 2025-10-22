# Troubleshooting Guide

Comprehensive troubleshooting guide for common issues in the Claude Code Command System.

## Quick Diagnostic Tools

Before diving into specific issues, run these diagnostic tools:

```bash
# System health check
python scripts/system_health_monitor.py

# Command validation
python scripts/validate_commands.py

# Pre-commit validation
python scripts/pre_commit_validation.py
```

## Common Issues and Solutions

### Installation and Setup Issues

#### Issue: "Command not found" errors

**Symptoms:**

- `claude` command not recognized
- Scripts not found
- "No such file or directory" errors

**Diagnosis:**

```bash
# Check if Claude Code is installed
which claude

# Check if directory exists
ls ~/.claude

# Check Python availability
python --version
```

**Solutions:**

**For Windows:**

```powershell
# Verify installation path
Test-Path "$env:USERPROFILE\.claude"

# Check PATH environment variable
$env:PATH -split ';' | Select-String claude

# Reinstall Claude Code if needed
# Download from official source and reinstall
```

**For macOS/Linux:**

```bash
# Check installation
ls -la ~/.claude

# Verify permissions
ls -la ~/.claude/scripts

# Fix permissions if needed
chmod +x ~/.claude/scripts/*.py

# Add to PATH if needed
echo 'export PATH="$HOME/.claude/scripts:$PATH"' >> ~/.zshrc
```

#### Issue: Permission denied errors

**Symptoms:**

- Cannot execute scripts
- "Permission denied" when running commands
- Files cannot be read/written

**Diagnosis:**

```bash
# Check file permissions
ls -la ~/.claude/scripts/

# Check ownership
ls -la ~/.claude/
```

**Solutions:**

**Unix (macOS/Linux):**

```bash
# Fix script permissions
chmod +x ~/.claude/scripts/*.py
chmod +x ~/.claude/hooks/*.py

# Fix ownership
sudo chown -R $(whoami):$(whoami) ~/.claude

# Check for restrictive umask
umask
# Should be 022 or similar
```

**Windows:**

```powershell
# Check execution policy
Get-ExecutionPolicy

# Set appropriate policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run as administrator if needed
Start-Process powershell -Verb RunAs
```

### Command Execution Issues

#### Issue: Commands fail with "Agent not found" errors

**Symptoms:**

- "Unknown agent" in validation reports
- Commands execute but agents don't respond
- Agent assignment errors

**Diagnosis:**

```bash
# Check agent directory
ls ~/.claude/agents/

# Validate command templates
python scripts/validate_commands.py | grep agent

# Check specific command
grep -A 5 "agent:" ~/.claude/commands/category/command.md
```

**Solutions:**

```bash
# Fix agent assignments
python scripts/fix_command_templates.py

# Verify agents exist
ls ~/.claude/agents/analysis-specialists/
ls ~/.claude/agents/execution-specialists/

# Check agent frontmatter
head -20 ~/.claude/agents/execution-specialists/reviewer.md
```

#### Issue: Git operations blocked or fail

**Symptoms:**

- "Git operations only allowed via /git/* commands"
- Git commands fail with security violations
- Commits rejected

**Diagnosis:**

```bash
# Check security logs
tail ~/.claude/logs/security.log

# Test security enforcement
python hooks/security_enforcement.py --test-git "git status" "unauthorized-agent"

# Check settings
grep -A 10 "git_constraints" ~/.claude/settings.json
```

**Solutions:**

```bash
# Use proper Git commands
/git:commit "Your commit message"
/git:push
/git:pr "Pull request title"

# Check security settings
cat ~/.claude/settings.json | jq '.security.git_constraints'

# Verify you're using authorized commands
python scripts/validate_commands.py | grep git
```

#### Issue: Template validation failures

**Symptoms:**

- Commands marked as invalid
- Missing YAML frontmatter errors
- Template compliance below 100%

**Diagnosis:**

```bash
# Run detailed validation
python scripts/validate_commands.py --output validation_report.md

# Check specific command
head -20 ~/.claude/commands/category/problematic-command.md

# Look for pattern issues
grep -l "^---" ~/.claude/commands/**/*.md | wc -l
```

**Solutions:**

```bash
# Auto-fix template issues
python scripts/fix_command_templates.py

# Manual fix for specific command
# Add YAML frontmatter:
# ---
# description: "Command description"
# category: "category_name"
# agent: "agent-name"
# tools: ["Tool1", "Tool2"]
# complexity: "simple|moderate|complex"
# ---

# Re-validate after fixes
python scripts/validate_commands.py
```

### Performance Issues

#### Issue: Slow command execution

**Symptoms:**

- Commands take longer than expected
- System appears unresponsive
- Timeout errors

**Diagnosis:**

```bash
# Run performance monitoring
python scripts/system_health_monitor.py

# Check system resources
# macOS/Linux:
top -p $(pgrep -f claude)

# Windows:
Get-Process | Where-Object {$_.ProcessName -like "*claude*"}
```

**Solutions:**

```bash
# Clean up large files
du -sh ~/.claude/*
# Remove large log files if needed

# Optimize command files
python scripts/fix_command_templates.py

# Check for infinite loops in scripts
ps aux | grep python
```

#### Issue: High memory usage

**Symptoms:**

- System becomes slow
- Memory warnings
- Application crashes

**Diagnosis:**

```bash
# Check memory usage
# macOS/Linux:
ps aux | grep claude
free -h

# Windows:
Get-Process | Where-Object {$_.ProcessName -like "*claude*"} | Select-Object WorkingSet64
```

**Solutions:**

```bash
# Restart Claude Code application
# Clear temporary files
rm -rf ~/.claude/logs/*.tmp

# Limit parallel operations
# Check settings.json for concurrent limits

# Monitor with health check
python scripts/system_health_monitor.py --watch 60
```

### Documentation and Integration Issues

#### Issue: Broken documentation links

**Symptoms:**

- "File not found" when clicking links
- Documentation references non-existent files
- Navigation broken after updates

**Diagnosis:**

```bash
# Check for broken links
find ~/.claude/docs -name "*.md" -exec grep -l "\[.*\](.*)" {} \;

# Validate documentation structure
ls -la ~/.claude/docs/user/
ls -la ~/.claude/docs/developer/
```

**Solutions:**

```bash
# Update documentation links after reorganization
# Old: [Guide](docs/user-guide.md)
# New: [Guide](docs/user/user-guide.md)

# Verify all index files exist
ls ~/.claude/docs/*/index.md

# Update README links
# Edit ~/.claude/README.md to use new structure
```

#### Issue: MCP tool integration failures

**Symptoms:**

- Context7 tools not working
- Playwright browser automation fails
- "MCP tool not found" errors

**Diagnosis:**

```bash
# Check MCP configuration
grep -A 10 "mcp_tools" ~/.claude/settings.json

# Test MCP tools
python hooks/security_enforcement.py --test-mcp "mcp__context7__get-library-docs"

# Check Claude Code MCP setup
# Refer to setup guide
```

**Solutions:**

```bash
# Verify MCP tools are allowed in settings.json
# Check tools list in:
cat ~/.claude/settings.json | jq '.mcp_tools.allowed'

# Update MCP configuration if needed
# See docs/user/mcp-setup-guide.md

# Test individual MCP tools
# Use Claude Code interface to test connectivity
```

## Platform-Specific Troubleshooting

### Windows-Specific Issues

#### PowerShell Execution Policy

```powershell
# Check current policy
Get-ExecutionPolicy

# Common issues and fixes
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# OR
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

#### Path Separator Issues

```powershell
# Use proper path separators
$env:CLAUDE_ROOT = "$env:USERPROFILE\.claude"

# Convert paths for Python scripts
python scripts\validate_commands.py --claude-root "$env:USERPROFILE/.claude"
```

#### Windows Defender Issues

```powershell
# Add exclusion for Claude directory
Add-MpPreference -ExclusionPath "$env:USERPROFILE\.claude"
```

### macOS-Specific Issues

#### Gatekeeper and Security

```bash
# If scripts are blocked by Gatekeeper
sudo spctl --master-disable  # Temporarily disable
# Then re-enable: sudo spctl --master-enable

# For specific scripts
sudo xattr -rd com.apple.quarantine ~/.claude/scripts/
```

#### Python Path Issues

```bash
# Use Homebrew Python
brew install python
which python

# Or use system Python with proper path
export PATH="/usr/bin/python:$PATH"
```

### Linux-Specific Issues

#### Package Manager Issues

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python python-pip git

# CentOS/RHEL
sudo yum install python python-pip git
# OR
sudo dnf install python python-pip git

# Arch Linux
sudo pacman -S python git
```

#### Permission Issues

```bash
# SELinux issues (CentOS/RHEL)
sudo setsebool -P allow_execheap 1

# AppArmor issues (Ubuntu)
sudo aa-complain /usr/bin/python
```

## Advanced Troubleshooting

### Debug Mode Execution

Enable debug mode for detailed troubleshooting:

```bash
# Set debug environment
export CLAUDE_DEBUG=1

# Run with verbose output
python -v scripts/validate_commands.py

# Enable logging
export PYTHONPATH="$HOME/.claude/scripts:$PYTHONPATH"
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
# Your debugging code here
"
```

### Network and Connectivity Issues

```bash
# Test internet connectivity for MCP tools
curl -I https://api.github.com

# Test DNS resolution
nslookup github.com

# Check proxy settings
echo $HTTP_PROXY
echo $HTTPS_PROXY
```

### File System Issues

```bash
# Check disk space
df -h ~/.claude

# Check for corrupted files
find ~/.claude -name "*.md" -exec head -1 {} \; | grep -v "^#"

# Verify file integrity
find ~/.claude -type f -name "*.py" -exec python -m py_compile {} \;
```

## Getting Additional Help

### Self-Diagnostic Checklist

Before seeking help, run through this checklist:

- [ ] System health check completed
- [ ] Command validation successful
- [ ] Security constraints verified
- [ ] Documentation structure correct
- [ ] Cross-platform compatibility confirmed
- [ ] Recent logs reviewed
- [ ] Error messages documented

### Log Analysis

Check these log files for detailed error information:

```bash
# Security events
tail -n 50 ~/.claude/logs/security.log

# Command execution
tail -n 50 ~/.claude/logs/commands.log

# Git operations
tail -n 50 ~/.claude/logs/git.log

# Health monitoring
ls ~/.claude/logs/health_report_*.json | tail -1 | xargs cat
```

### Creating Effective Bug Reports

When reporting issues, include:

1. **System Information:**

   ```bash
   uname -a  # Unix
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion  # Windows
   python --version
   ```

1. **Error Messages:**
   - Complete error text
   - Command that triggered the error
   - Expected vs. actual behavior

1. **System Health Report:**

   ```bash
   python scripts/system_health_monitor.py --output health_report.json
   # Include the generated health_report.json
   ```

1. **Configuration:**

   ```bash
   # Sanitized settings (remove sensitive data)
   cat ~/.claude/settings.json | jq 'del(.secrets)'
   ```

### Community Resources

- **GitHub Issues**: Report bugs and feature requests
- **Documentation**: Latest guides and references
- **Security Issues**: Use responsible disclosure via SECURITY.md
- **Contributions**: See CONTRIBUTING.md for development help

### Emergency Recovery

If the system becomes completely unusable:

```bash
# Backup current state
cp -r ~/.claude ~/.claude.backup

# Reset to clean state
rm -rf ~/.claude
# Re-install Claude Code from official source

# Restore custom configurations
cp ~/.claude.backup/settings.json ~/.claude/
# Manually restore any custom commands or documentation
```

This troubleshooting guide covers the most common issues and
their solutions. For complex problems, start with the diagnostic tools and work through the relevant sections systematically.
