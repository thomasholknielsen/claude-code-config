# Frequently Asked Questions (FAQ)

Common questions and answers about the Claude Code Command System.

## General Questions

### What is the Claude Code Command System

The Claude Code Command System is a comprehensive development automation framework built on the Agent Specialist Framework architecture.
It
provides 55+ commands organized across 15 categories, coordinated by 8 specialized agents (3 analysis specialists + 5 execution specialists)
to automate complex development workflows.

### How is this different from regular Claude Code

This system extends Claude Code with:

- **Structured command system** with standardized templates
- **Agent Specialist Framework coordination** for complex task management
- **Automated workflows** for common development patterns
- **Security constraints** and validation systems
- **Cross-platform compatibility** for Windows, macOS, and Linux
- **Comprehensive documentation** and troubleshooting guides

### Do I need to install anything special

The system requires:

- **Claude Code application** (primary requirement)
- **Python 3.7+** for validation and automation scripts
- **Git** for version control operations
- **Cross-platform compatible shell** (PowerShell, Zsh, Bash)

Optional for enhanced features:

- **MCP tools** (Context7, Playwright) for external integrations

## Command System Questions

### How many commands are available

Currently **55 commands** across **15 categories**:

- analyze (3), clean (4), docs (6), explain (2), fix (2)
- git (6), implement (2), plan (1), prompt (1), refactor (6)
- review (3), speckit (7), to-do (5), workflows (7)

### What's the difference between analysis specialists and execution specialists

**Analysis Specialists** (3 total):

- **implementation-strategy-specialist**: Coordinates sequential code changes
- **task-analysis-specialist**: General task analysis and coordination
- **research-analysis-specialist**: Parallel information gathering

**Execution Specialists** (5 total):

- **reviewer**: Code, security, and design reviews
- **documenter**: Documentation creation and maintenance
- **code-writer**: Focused code generation
- **bug-fixer**: Debugging and issue resolution
- **test-writer**: Test creation and maintenance

### Can I create custom commands

Yes! Follow these steps:

1. Use the [command template](../developer/command-template.md)
2. Place in appropriate category: `commands/{category}/{name}.md`
3. Include required YAML frontmatter
4. Assign to existing agent
5. Validate with: `python scripts/validate_commands.py`

### Why do some commands fail with "Agent not found"

This usually means:

- Command has invalid agent assignment
- Agent file is missing or corrupted
- YAML frontmatter is malformed

**Fix:**

```bash
# Auto-fix agent assignments
python scripts/fix_command_templates.py

# Validate after fixing
python scripts/validate_commands.py
```

## Security Questions

### Why can't I run Git commands directly

The system implements **Git operation constraints** for security:

- Only `/git:*` commands can perform Git operations
- This prevents unauthorized repository modifications
- Ensures all Git operations go through proper validation

**Use these instead:**

```bash
# Instead of: git commit -m "message"
/git:commit "message"

# Instead of: git push
/git:push

# Instead of: git checkout -b branch
/git:branch "new-branch"
```

### What are MCP tools and are they safe

**MCP (Model Context Protocol) tools** provide external integrations:

- **Context7**: Access to current library documentation
- **Playwright**: Browser automation for testing

**Security measures:**

- Controlled access via `settings.json`
- Usage monitoring and logging
- Explicit allow/block lists
- No system-level access

### How do I know if my system is secure

Run security validation:

```bash
# Comprehensive security check
python scripts/system_health_monitor.py

# Security-specific validation
python hooks/security_enforcement.py --test-all

# Check security logs
tail ~/.claude/logs/security.log
```

## Usage Questions

### What's the best way to learn the command system

**Recommended learning path:**

1. Start with [User Guide](user-guide.md) for basic setup
2. Review [Typical Workflows](typical-workflows.md) for common patterns
3. Practice with simple commands: `/analyze:codebase`, `/review:code`
4. Try workflow commands: `/workflows:run-comprehensive-review`
5. Advanced: [Command Integration Guide](../developer/command-integration-guide.md)

### How do I know which command to use

**Command discovery strategies:**

1. **By goal**: Check [Typical Workflows](typical-workflows.md)
2. **By category**: Browse `commands/` directories
3. **By integration**: Use [Command Integration Guide](../developer/command-integration-guide.md)
4. **Interactive help**: Use `/help` or `/prompt:enhanced`

### Can I run multiple commands at once

Yes, the Agent Orchestra enables:

- **Parallel execution**: Independent tasks run simultaneously
- **Sequential coordination**: Dependent tasks in proper order
- **Workflow orchestration**: Complex multi-step processes

**Examples:**

```bash
# Parallel reviews (automatic)
/workflows:run-comprehensive-review

# Sequential workflow
/analyze:potential-issues → /fix:bug-quickly → /review:code → /git:commit
```

### Why do some commands take longer than others

**Command complexity varies:**

- **Simple commands** (explain, clean): Seconds
- **Moderate commands** (analyze, fix): Minutes
- **Complex commands** (workflows, implement): Longer

**Performance factors:**

- Agent coordination overhead
- File system operations
- External tool integrations
- Project size and complexity

## Platform Questions

### Does this work on Windows

Yes! Full Windows support with:

- **PowerShell Core 7+** recommended
- **Python 3.7+** (from Microsoft Store or python.org)
- **Git for Windows**
- **Windows Terminal** for best experience

**Windows-specific considerations:**

- Use forward slashes in Python scripts
- Set PowerShell execution policy
- Add Windows Defender exclusions if needed

### What about macOS compatibility

Full macOS support:

- **macOS 10.15+** (Catalina or later)
- **Zsh** (default) or **Bash**
- **Homebrew** for package management
- **Xcode Command Line Tools** for Git

**macOS-specific optimizations:**

- Native Python 3 support
- Terminal integration
- Spotlight exclusions for performance

### Linux distribution support

Tested on major distributions:

- **Ubuntu 18.04+** and **Debian 9+**
- **CentOS 7+** and **RHEL 8+**
- **Arch Linux** and derivatives
- **Fedora** recent versions

**Requirements:**

- Python 3.7+ (usually available)
- Git (via package manager)
- Bash or compatible shell

## Troubleshooting Questions

### My commands are failing validation. What's wrong

**Common validation issues:**

1. **Missing YAML frontmatter**: Commands need structured metadata
2. **Invalid agent assignments**: Agents must exist in the system
3. **Malformed templates**: Required sections missing

**Quick fix:**

```bash
# Auto-fix most issues
python scripts/fix_command_templates.py

# Check results
python scripts/validate_commands.py
```

### The system seems slow. How can I improve performance

**Performance optimization:**

1. **Clean up logs**: `rm ~/.claude/logs/*.log`
2. **Check disk usage**: `du -sh ~/.claude`
3. **Monitor health**: `python scripts/system_health_monitor.py`
4. **Optimize commands**: Ensure template compliance
5. **Check system resources**: Memory and CPU usage

### I'm getting permission errors. What should I do

**Permission fixes:**

**Unix (macOS/Linux):**

```bash
# Fix script permissions
chmod +x ~/.claude/scripts/*.py

# Fix ownership
sudo chown -R $(whoami):$(whoami) ~/.claude
```

**Windows:**

```powershell
# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run as administrator if needed
```

### Documentation links are broken after updates. How to fix

After reorganization, update links:

- **Old**: `[Guide](docs/user-guide.md)`
- **New**: `[Guide](user-guide.md)`

**Systematic fix:**

1. Check current documentation structure: `ls docs/`
2. Update internal links in your documents
3. Verify with: `find docs -name "*.md" -exec grep -l "\[.*\](" {} \;`

## Advanced Questions

### Can I integrate this with CI/CD pipelines

Yes! Use for automated quality gates:

**GitHub Actions example:**

```yaml
- name: Validate Commands
  run: python scripts/validate_commands.py

- name: Pre-commit Validation
  run: python scripts/pre_commit_validation.py

- name: System Health Check
  run: python scripts/system_health_monitor.py
```

### How do I customize the Agent Orchestra

**Agent customization:**

1. **Modify existing agents**: Edit agent files with proper YAML frontmatter
2. **Adjust permissions**: Update `settings.json` agent permissions
3. **Create specialized workflows**: Use `/workflows:*` patterns
4. **Custom command categories**: Create new command folders

**Important**: Maintain analysis specialist/execution specialist separation.

### Can I backup and restore my configuration

**Backup:**

```bash
# Full backup
cp -r ~/.claude ~/.claude.backup

# Configuration only
cp ~/.claude/settings.json ~/.claude.backup/
cp -r ~/.claude/docs/custom/ ~/.claude.backup/
```

**Restore:**

```bash
# Restore settings
cp ~/.claude.backup/settings.json ~/.claude/

# Restore custom content
cp -r ~/.claude.backup/docs/custom/ ~/.claude/docs/
```

### How do I monitor system health continuously

**Continuous monitoring:**

```bash
# Monitor every 5 minutes
python scripts/system_health_monitor.py --watch 300

# Save reports for analysis
python scripts/system_health_monitor.py --output health_$(date +%Y%m%d).json

# Set up cron job (Unix)
echo "0 */6 * * * cd ~/.claude && python scripts/system_health_monitor.py --quiet --output logs/health_check.json" | crontab -
```

## Development Questions

### I want to contribute. Where do I start

**Contribution workflow:**

1. Read [CONTRIBUTING.md](../../CONTRIBUTING.md)
2. Review [Developer Guide](../developer/developer-guide.md)
3. Check [Command Template](../developer/command-template.md)
4. Start with documentation improvements or simple commands
5. Follow quality standards and validation requirements

### How do I report bugs or request features

**Bug reports:**

1. Run system health check: `python scripts/system_health_monitor.py`
2. Include error messages and system information
3. Follow issue template in GitHub repository
4. For security issues: Use [SECURITY.md](../../SECURITY.md) process

**Feature requests:**

1. Check existing commands and workflows first
2. Describe use case and expected behavior
3. Consider if it fits Agent Orchestra patterns
4. Submit via GitHub issues with "enhancement" label

### What's the roadmap for future development

**Planned improvements:**

- Enhanced MCP tool integrations
- Additional workflow patterns
- Performance optimizations
- Extended cross-platform features
- Community-contributed commands
- Advanced agent coordination patterns

See [CHANGELOG.md](../../CHANGELOG.md) for version history and upcoming features.

## Getting More Help

### Where can I find additional resources

**Documentation:**

- [User Documentation](../user/) - Setup and usage guides
- [Developer Documentation](../developer/) - Architecture and contribution
- [Conceptual Documentation](../concepts/) - Deep architecture insights

**Support channels:**

- **GitHub Issues**: Bug reports and feature requests
- **Security Issues**: Responsible disclosure via SECURITY.md
- **Contributions**: Community development via CONTRIBUTING.md
- **Documentation**: Updates and improvements welcome

### Is there a community around this project

The project encourages community involvement through:

- **Open source development**: MIT licensed
- **Contribution guidelines**: Clear process for adding features
- **Documentation**: Community-maintained guides and examples
- **Quality standards**: Automated validation ensures consistency

**Ways to get involved:**

- Improve documentation
- Add new commands following templates
- Report bugs and suggest features
- Share workflow patterns and examples
- Help with cross-platform testing

Remember: The Claude Code Command System is designed to be extensible and community-friendly. Your contributions help make it better for everyone!
