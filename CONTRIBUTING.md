# Contributing to Claude Code Command System

Thank you for your interest in contributing to the Claude
Code Command System! This document provides guidelines for contributing to this open-source automation framework.

## 🎯 Overview

The Claude Code Command System is built on the **Agent Orchestra Framework** with:

- **8 Agents**: 3 orchestrators + 5 workers for task coordination
- **54+ Commands**: Atomic operations across 15 categories
- **Cross-Platform Compatibility**: Windows, macOS, and Linux support
- **MCP Integration**: Context7 and Playwright tools

## 📋 How to Contribute

### Types of Contributions

We welcome several types of contributions:

1. **New Commands** - Atomic operations following our command template
2. **Agent Improvements** - Enhancements to orchestrators or workers
3. **Documentation** - User guides, technical docs, and examples
4. **Bug Fixes** - Corrections to existing functionality
5. **Security Improvements** - Enhanced security patterns and controls
6. **Cross-Platform Support** - Compatibility improvements

### Before You Start

1. **Search existing issues** to avoid duplicates
2. **Review the architecture** in `docs/agent-orchestra-framework.md`
3. **Read the developer guide** at `docs/developer-guide.md`
4. **Check command standards** in `docs/command-template.md`

## 🛠️ Development Guidelines

### Command Development

**All new commands must:**

- Follow the template in `docs/command-template.md`
- Include complete YAML frontmatter
- Be assigned to an existing Agent Orchestra agent
- Include practical examples and integration points
- Support cross-platform execution

**Required YAML frontmatter:**

```yaml
---
description: "Single clear sentence describing command purpose"
category: "folder_name"
agent: "primary-agent-name"
tools: ["Tool1", "Tool2"]
complexity: "simple|moderate|complex"
---
```yaml

**Required sections:**

- Purpose
- Usage
- Process (3-5 numbered steps)
- Agent Integration
- Examples
- Integration Points

### Agent Development

**New agents must:**

- Have single, focused responsibility
- Follow orchestrator/worker pattern
- Use appropriate model (Opus for orchestrators, Sonnet for workers)
- Not duplicate existing agent functionality
- Include complete YAML specification

### Code Standards

**All code must:**

- Use cross-platform patterns (Python `pathlib.Path`)
- Avoid hardcoded user paths
- Follow existing error handling patterns
- Include appropriate logging
- Respect security constraints

## 🔒 Security Guidelines

**Critical constraints:**

- Only `/git/*` commands can perform Git operations
- All agents must use SlashCommand tool for Git delegation
- No hardcoded secrets or credentials
- Input validation for all user inputs
- Path validation for file operations

## 📚 Documentation Standards

**All contributions must include:**

- Updated documentation for new features
- Examples demonstrating usage
- Integration points with existing commands
- Cross-platform compatibility notes

## 🧪 Testing Requirements

**Before submitting:**

- Test on multiple platforms (Windows, macOS, Linux preferred)
- Verify command template compliance
- Ensure agent assignments are correct
- Test integration with existing commands
- Validate security constraints

## 🔍 Code Quality & Linting

**All contributions must pass linting checks:**

### Markdown Linting

```bash
# Install markdownlint-cli globally
npm install -g markdownlint-cli

# Run markdownlint on all markdown files
markdownlint "**/*.md" --ignore node_modules --config .markdownlint.yml

# Auto-fix basic markdown formatting issues
markdownlint "**/*.md" --fix --ignore node_modules --config .markdownlint.yml
```text

### Python Linting (for hook scripts)

```bash
# Install ruff
pip install ruff

# Run code checks
ruff check .

# Run format checks
ruff format --check .

# Auto-fix formatting issues
ruff format .
```text

### Shell Script Linting

```bash
# Install shellcheck (platform-specific)
# macOS: brew install shellcheck
# Ubuntu: sudo apt-get install shellcheck

# Run shellcheck on shell scripts
shellcheck scripts/**/*.sh
```yaml

**Configuration files:**

- Markdown: `.markdownlint.yml` - Project-specific markdown rules
- Python: `pyproject.toml` - Ruff configuration for Python code
- Shell: Uses default shellcheck rules for cross-platform compatibility

**Automated CI/CD:**
All linting checks run automatically on pull requests via GitHub Actions (`.github/workflows/lint.yml`).

**Quick Auto-Fix Script:**
For convenience, use the comprehensive auto-fix script:

```bash
# Run all linting and auto-fixes
./scripts/lint-fix.sh
```text

## 📝 Pull Request Process

### 1. Preparation

```bash
# Fork the repository
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes following guidelines
# Test thoroughly on your platform
```yaml

### 2. Submission Requirements

**Your PR must include:**

- [ ] Clear description of changes and motivation
- [ ] Updated documentation for new features
- [ ] Examples demonstrating new functionality
- [ ] Cross-platform testing results
- [ ] Security impact assessment

**PR title format:**

```yaml
[category]: Brief description of change

Examples:
[command]: Add user authentication analysis command
[agent]: Improve code-writer error handling
[docs]: Update installation guide for Windows
[security]: Add input validation framework
```

### 3. Review Process

1. **Automated checks** run on all platforms
2. **Maintainer review** for architecture compliance
3. **Security review** for security-sensitive changes
4. **Documentation review** for user-facing changes
5. **Integration testing** with existing system

### 4. Merge Criteria

**Your PR will be merged when:**

- All automated tests pass
- Code follows established patterns
- Documentation is complete and accurate
- Security requirements are met
- At least one maintainer approves

## 🚫 What Not to Contribute

**Please avoid:**

- Commands that duplicate existing functionality
- Agents with overlapping responsibilities
- Platform-specific code without cross-platform alternatives
- Changes that break existing integrations
- Security vulnerabilities or anti-patterns
- Hardcoded user paths or credentials

## ❓ Questions and Support

**For questions:**

- Review existing documentation in `docs/`
- Search closed issues for similar questions
- Open a discussion for architecture questions
- Open an issue for bugs or feature requests

**For urgent security issues:**

- See `SECURITY.md` for responsible disclosure
- Do not open public issues for security vulnerabilities

## 📊 Recognition

Contributors are recognized in:

- `AUTHORS` file for significant contributions
- Release notes for feature contributions
- Documentation for documentation improvements

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License (see `LICENSE` file).

## 🙏 Thank You

Every contribution helps make the Claude Code Command System better for the entire community. Whether you're fixing a typo, adding a feature, or
improving documentation, your efforts are appreciated!

---

**Happy Contributing!** 🚀
