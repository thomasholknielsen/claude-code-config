# Cross-Platform Setup Guide

Complete setup instructions for Windows, macOS, and Linux systems, with troubleshooting for common cross-platform issues.

## Quick Start by Platform

### Windows Setup

#### Prerequisites

- **Windows 10/11** with PowerShell 5.1+ or PowerShell Core 7+
- **Python 3.7+** installed and in PATH
- **Git** installed and configured
- **Claude Code** application installed

#### Installation Steps

1. **Open PowerShell as Administrator**

   ```powershell
   # Check Python version
   python --version

   # Check Git installation
   git --version
   ```

1. **Clone to Claude Directory**

   ```powershell
   # Create Claude directory if it doesn't exist
   New-Item -Path "$env:USERPROFILE\.claude" -ItemType Directory -Force

   # Navigate to Claude directory
   Set-Location "$env:USERPROFILE\.claude"

   # Clone repository (replace with actual repo URL)
   git clone <repository-url> .
   ```

1. **Set Execution Policy (if needed)**

   ```powershell
   # Allow script execution (choose one)
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   # OR for more restrictive
   Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
   ```

1. **Make Scripts Executable**

   ```powershell
   # Python scripts should work by default
   # Test installation
   python scripts\validate_commands.py --help
   ```

1. **Test Installation**

   ```powershell
   # Start Claude Code and test
   claude /help
   ```

#### Windows-Specific Configuration

**PowerShell Profile Setup:**

```powershell
# Add to PowerShell profile for easier access
$profilePath = $PROFILE.CurrentUserAllHosts
New-Item -Path $profilePath -ItemType File -Force

# Add alias (optional)
Add-Content $profilePath 'Set-Alias claude "C:\Path\To\Claude.exe"'
```

**Environment Variables:**

```powershell
# Set Claude root environment variable
[Environment]::SetEnvironmentVariable("CLAUDE_ROOT", "$env:USERPROFILE\.claude", "User")
```

### macOS Setup

#### Prerequisites

- **macOS 10.15+** (Catalina or later)
- **Python 3.7+** (use Homebrew, pyenv, or built-in)
- **Git** (installed via Xcode Command Line Tools or Homebrew)
- **Claude Code** application

#### Installation Steps

1. **Open Terminal**

   ```bash
   # Check Python version
   python --version

   # Check Git installation
   git --version
   ```

1. **Install Prerequisites (if needed)**

   ```bash
   # Install Homebrew (if not installed)
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install Python 3 via Homebrew (if needed)
   brew install python

   # Install Git (if needed)
   brew install git
   ```

1. **Clone to Claude Directory**

   ```bash
   # Navigate to home directory
   cd ~

   # Clone repository
   git clone <repository-url> .claude
   cd .claude
   ```

1. **Set Permissions**

   ```bash
   # Make Python scripts executable
   chmod +x scripts/*.py
   chmod +x hooks/*.py

   # Test permissions
   ls -la scripts/
   ```

1. **Test Installation**

   ```bash
   # Test validation script
   python scripts/validate_commands.py --help

   # Test Claude Code
   claude /help
   ```

#### macOS-Specific Configuration

**Shell Configuration (Zsh - default in macOS 10.15+):**

```bash
# Add to ~/.zshrc for easier access
echo 'export CLAUDE_ROOT="$HOME/.claude"' >> ~/.zshrc
echo 'alias claude-validate="python $CLAUDE_ROOT/scripts/validate_commands.py"' >> ~/.zshrc

# Reload configuration
source ~/.zshrc
```

**For Bash Users:**

```bash
# Add to ~/.bash_profile
echo 'export CLAUDE_ROOT="$HOME/.claude"' >> ~/.bash_profile
source ~/.bash_profile
```

### Linux Setup

#### Prerequisites

- **Linux distribution** (Ubuntu 18.04+, CentOS 7+, Debian 9+, etc.)
- **Python 3.7+**
- **Git**
- **Claude Code** application

#### Installation Steps (Ubuntu/Debian)

1. **Update Package Manager**

   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

1. **Install Prerequisites**

   ```bash
   # Install Python 3 and pip
   sudo apt install python3 python3-pip git -y

   # Verify installation
   python --version
   git --version
   ```

1. **Clone Repository**

   ```bash
   # Clone to home directory
   cd ~
   git clone <repository-url> .claude
   cd .claude
   ```

1. **Set Permissions**

   ```bash
   # Make scripts executable
   chmod +x scripts/*.py
   chmod +x hooks/*.py

   # Verify permissions
   ls -la scripts/
   ```

1. **Test Installation**

   ```bash
   # Test validation
   python scripts/validate_commands.py --help

   # Test Claude Code
   claude /help
   ```

#### CentOS/RHEL/Fedora

```bash
# Install prerequisites
sudo yum install python3 python3-pip git -y
# OR for newer versions
sudo dnf install python3 python3-pip git -y

# Follow same steps as Ubuntu/Debian
```

#### Arch Linux

```bash
# Install prerequisites
sudo pacman -S python git

# Follow same steps as Ubuntu/Debian
```

## Cross-Platform Troubleshooting

### Common Issues and Solutions

#### 1. Python Version Issues

**Problem:** "Python not found" or version too old

**Windows Solution:**

```powershell
# Install Python from Microsoft Store or python.org
# Add Python to PATH
$env:PATH += ";C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python39"

# Or use Chocolatey
choco install python
```

**macOS Solution:**

```bash
# Install via Homebrew
brew install python

# Or use pyenv for version management
brew install pyenv
pyenv install 3.9.7
pyenv global 3.9.7
```

**Linux Solution:**

```bash
# Ubuntu/Debian
sudo apt install python3.9 python3.9-pip

# CentOS/RHEL (enable EPEL first)
sudo yum install epel-release
sudo yum install python39 python39-pip
```

#### 2. Permission Denied Errors

**Problem:** Cannot execute scripts

**Windows Solution:**

```powershell
# Check execution policy
Get-ExecutionPolicy

# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Alternative: Run Python directly
python scripts\validate_commands.py
```

**macOS/Linux Solution:**

```bash
# Fix permissions
chmod +x scripts/*.py
chmod +x hooks/*.py

# Check ownership
ls -la scripts/

# Fix ownership if needed
sudo chown -R $(whoami):$(whoami) ~/.claude
```

#### 3. Path Issues

**Problem:** Commands not found or incorrect paths

**Windows Solution:**

```powershell
# Use PowerShell path resolution
$claudeRoot = Resolve-Path "$env:USERPROFILE\.claude"
Set-Location $claudeRoot

# Check if directory exists
Test-Path "$env:USERPROFILE\.claude"

# Use forward slashes in Python scripts
python scripts/validate_commands.py --claude-root "$env:USERPROFILE/.claude"
```

**macOS/Linux Solution:**

```bash
# Use proper path expansion
export CLAUDE_ROOT="$HOME/.claude"
cd "$CLAUDE_ROOT"

# Check path exists
ls -la "$CLAUDE_ROOT"

# Use proper quoting for paths with spaces
python scripts/validate_commands.py --claude-root "$HOME/.claude"
```

#### 4. Git Configuration Issues

**Problem:** Git operations fail or authentication issues

**Universal Solution:**

```bash
# Configure Git (if not done)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# For Windows, handle line endings
git config --global core.autocrlf true

# For macOS/Linux
git config --global core.autocrlf input

# Test Git access
git status
```

#### 5. Script Import/Module Issues

**Problem:** Python scripts fail with import errors

**Universal Solution:**

```bash
# Install required packages (if any)
pip3 install --user pyyaml  # Only if script requires YAML

# Check Python path
python3 -c "import sys; print(sys.path)"

# Run from correct directory
cd ~/.claude
python3 scripts/validate_commands.py
```

### Platform-Specific Optimizations

#### Windows Performance Tips

1. **Use Windows Terminal** instead of Command Prompt
1. **Enable Developer Mode** for better symlink support
1. **Use PowerShell Core 7+** for better cross-platform compatibility
1. **Configure Windows Defender exclusions** for Claude directory

```powershell
# Add Claude directory to Windows Defender exclusions
Add-MpPreference -ExclusionPath "$env:USERPROFILE\.claude"
```

#### macOS Performance Tips

1. **Use Terminal with Rosetta** on Apple Silicon if needed
1. **Install command line tools**:

   ```bash
   xcode-select --install
   ```

1. **Use native Python** when possible
1. **Configure spotlight exclusions**:

   ```bash
   # Add .claude to Spotlight privacy
   # System Preferences > Spotlight > Privacy > Add .claude folder
   ```

#### Linux Performance Tips

1. **Use package manager Python** when possible
1. **Install development tools**:

   ```bash
   # Ubuntu/Debian
   sudo apt install build-essential python3-dev

   # CentOS/RHEL
   sudo yum groupinstall "Development Tools"
   sudo yum install python3-devel
   ```

1. **Configure proper locale**:

   ```bash
   export LC_ALL=C.UTF-8
   export LANG=C.UTF-8
   ```

## Environment Configuration

### Environment Variables

Set these environment variables for optimal cross-platform experience:

```bash
# Universal settings
export CLAUDE_ROOT="$HOME/.claude"          # Unix
set CLAUDE_ROOT=%USERPROFILE%\.claude       # Windows

export PYTHONPATH="$CLAUDE_ROOT/scripts:$PYTHONPATH"
export PATH="$CLAUDE_ROOT/scripts:$PATH"
```

### Shell Configuration

#### Bash (~/.bashrc or ~/.bash_profile)

```bash
# Claude Code configuration
export CLAUDE_ROOT="$HOME/.claude"
alias claude-validate="python $CLAUDE_ROOT/scripts/validate_commands.py"
alias claude-fix="python $CLAUDE_ROOT/scripts/fix_command_templates.py"

# Add to PATH for easy access
export PATH="$CLAUDE_ROOT/scripts:$PATH"
```

#### Zsh (~/.zshrc)

```bash
# Claude Code configuration
export CLAUDE_ROOT="$HOME/.claude"
alias claude-validate="python $CLAUDE_ROOT/scripts/validate_commands.py"
alias claude-fix="python $CLAUDE_ROOT/scripts/fix_command_templates.py"

# Auto-completion (if available)
autoload -U compinit && compinit
```

#### PowerShell (Profile)

```powershell
# Claude Code configuration
$env:CLAUDE_ROOT = "$env:USERPROFILE\.claude"

# Aliases
Set-Alias claude-validate "python"
function claude-validate { python "$env:CLAUDE_ROOT\scripts\validate_commands.py" $args }
function claude-fix { python "$env:CLAUDE_ROOT\scripts\fix_command_templates.py" $args }
```

## Advanced Cross-Platform Considerations

### File System Differences

#### Path Separators

```python
# Good: Use pathlib for cross-platform paths
from pathlib import Path
claude_root = Path.home() / '.claude'

# Bad: Hardcoded separators
claude_root = "~/.claude"  # Won't work on Windows
claude_root = "~\.claude"  # Won't work on Unix
```

#### Case Sensitivity

```text
# macOS and Windows are typically case-insensitive
# Linux is case-sensitive

# Good: Consistent casing
commands/analyze/dependencies.md

# Bad: Inconsistent casing
Commands/Analyze/Dependencies.md  # May work on some platforms, not others
```

#### Character Encoding

```python
# Good: Explicit UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Bad: Platform-dependent encoding
with open(file_path, 'r') as f:  # May use cp1252 on Windows
    content = f.read()
```

### Terminal and Shell Differences

#### Command Execution

```python
# Good: Use subprocess with shell=False for security
import subprocess
result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)

# Platform-aware approach (usually not needed)
import platform
if platform.system() == 'Windows':
    cmd = ['python', 'script.py']
else:
    cmd = ['python', 'script.py']  # Both use 'python' for consistency
```

#### Environment Variables

```python
# Good: Cross-platform environment access
import os
from pathlib import Path

claude_root = Path(os.environ.get('CLAUDE_ROOT', Path.home() / '.claude'))

# Bad: Platform-specific assumptions
claude_root = os.environ['HOME'] + '/.claude'  # Fails on Windows
```

## Testing Cross-Platform Compatibility

### Validation Checklist

- [ ] Scripts run on Windows PowerShell
- [ ] Scripts run on macOS Terminal (Zsh)
- [ ] Scripts run on Linux Bash
- [ ] File paths resolve correctly on all platforms
- [ ] No hardcoded platform-specific paths
- [ ] UTF-8 encoding handled properly
- [ ] No shell-specific commands in Python scripts
- [ ] Git operations work on all platforms

### Test Commands

Run these on each platform to verify setup:

```bash
# Basic functionality
python scripts/validate_commands.py --help
python scripts/fix_command_templates.py --help
python hooks/security_enforcement.py --help

# Path resolution
python -c "from pathlib import Path; print(Path.home() / '.claude')"

# File operations
ls ~/.claude  # Unix
dir %USERPROFILE%\.claude  # Windows

# Git operations
git status
git log --oneline -5
```

## Getting Help

### Platform-Specific Support

#### Windows

- **PowerShell Documentation**: `Get-Help about_*`
- **Windows Terminal**: Use for better Unicode support
- **WSL**: Consider using Linux instructions in WSL environment

#### macOS

- **Terminal Help**: `man terminal`
- **Homebrew**: Primary package manager for missing tools
- **Apple Developer**: Additional development tools

#### Linux

- **Distribution Documentation**: Check your distro's wiki
- **Package Manager**: Use your distribution's package manager
- **Community Forums**: Distribution-specific communities

### Common Resources

- **Python Documentation**: <https://docs.python.org/3/>
- **Git Documentation**: <https://git-scm.com/doc>
- **Cross-Platform Development**: Platform-specific guides in repository

This guide ensures Claude Code Command System works consistently across all supported platforms while respecting platform-specific conventions and optimizations.
