# Claude Code Command System

A comprehensive development automation system built on the **Agent Orchestra Framework** that transforms Claude Code into a powerful, coordinated development environment.

## 🚀 Quick Start

### New User? Start Here
👉 **[User Guide](docs/user-guide.md)** - Complete setup and usage guide

### Developer? Extend the System
👉 **[Developer Guide](docs/developer-guide.md)** - Architecture and customization

### Want to See It in Action?
👉 **[Typical Workflows](docs/typical-workflows.md)** - Common usage patterns with visual diagrams

## 🏗️ Architecture Overview

This system is built on the **Agent Orchestra Framework** - a task-focused coordination system that uses specialized orchestrators and workers to handle complex development tasks efficiently.

### Agent Orchestra Components
- **3 Orchestrators**: Coordinate complex, multi-step tasks
  - `task-orchestrator` - General task coordination
  - `research-orchestrator` - Parallel information gathering
  - `implementation-orchestrator` - Sequential code changes
- **5 Workers**: Execute specific functions
  - `code-writer`, `test-writer`, `bug-fixer`, `reviewer`, `documenter`

### Command Categories (47 Commands)
- **`/analyze/*`** - Performance and dependency analysis
- **`/clean/*`** - Code cleanup and formatting
- **`/docs/*`** - Documentation generation and maintenance
- **`/fix/*`** - Bug fixes and issue resolution
- **`/git/*`** - Git operations (only commands that can perform Git operations)
- **`/review/*`** - Code review and quality analysis
- **`/spec-kit/*`** - Complete 7-step feature development workflow
- **`/workflows/*`** - Multi-step orchestrated processes

## 📚 Complete Documentation

### Getting Started
- **[User Guide](docs/user-guide.md)** - Setup, configuration, and basic usage
- **[Typical Workflows](docs/typical-workflows.md)** - Common development patterns

### System Architecture
- **[Agent Orchestra Framework](docs/agent-orchestra-framework.md)** - Technical architecture details
- **[Hooks System](docs/hooks-system.md)** - Event-driven automation with diagrams
- **[Spec-Kit Workflow](docs/spec-kit-workflow.md)** - 7-step feature development process

### Development & Extension
- **[Developer Guide](docs/developer-guide.md)** - Extending and customizing the system
- **[Command Template](docs/command-template.md)** - Standard format for new commands
- **[Command Audit Report](docs/command-audit-report.md)** - Standardization analysis

### Implementation Reference
- **[Implementation Summary](docs/implementation-summary.md)** - Complete work overview

## 🛠️ Key Features

### Intelligent Task Orchestration
- **Complexity Analysis**: Automatically determines optimal execution strategy
- **Parallel Execution**: Independent tasks run simultaneously for efficiency
- **Sequential Coordination**: Dependent tasks execute in proper order
- **Quality Gates**: Built-in validation at each step

### Advanced Automation
- **Smart Notifications**: macOS integration with context-aware messages
- **Automatic Logging**: Complete session tracking and analysis
- **Hook System**: Event-driven automation for custom workflows
- **Spec-Kit Integration**: Complete feature development lifecycle

### Security & Quality
- **Git Operation Safety**: Only `/git/*` commands can perform Git operations
- **Permission System**: Granular control over tool access and operations
- **Agent Constraints**: Secure delegation through SlashCommand system
- **Quality Assurance**: Built-in review and validation processes

## 🎯 Common Use Cases

```bash
# Quick feature implementation
claude /implement "Add user authentication"

# Comprehensive code review
claude /workflows:run-comprehensive-review

# Complete feature development lifecycle
claude /spec-kit:specify "E-commerce checkout process"
claude /spec-kit:plan
claude /spec-kit:implement

# Performance optimization
claude /analyze:performance
claude /workflows:run-optimization

# Documentation generation
claude /docs:generate
claude /workflows:run-docs-workflow
```

## 📁 System Structure

```
├── agents/                    # Agent Orchestra definitions
│   ├── orchestrators/        # Task coordination agents
│   └── workers/              # Execution specialists
├── commands/                 # 47 organized commands
│   ├── analyze/, clean/, docs/, fix/, git/
│   ├── review/, spec-kit/, workflows/
│   └── [11 other categories]
├── docs/                     # Comprehensive documentation
├── scripts/                  # Hook automation scripts
├── settings.json             # System configuration
└── CLAUDE.md                 # Project-specific rules
```

## 🔧 Installation & Setup

1. **Clone to Claude config directory:**
   ```bash
   git clone <repo-url> ~/.claude
   cd ~/.claude
   ```

2. **Make scripts executable:**
   ```bash
   chmod +x scripts/*.sh
   ```

3. **Test installation:**
   ```bash
   claude /help
   ```

4. **Follow the User Guide:**
   See [docs/user-guide.md](docs/user-guide.md) for detailed setup instructions.

## 🎨 Visual Documentation

All complex workflows include **Mermaid diagrams** for clear understanding:
- Agent coordination patterns
- Hook system flows
- Spec-kit workflow steps
- Typical usage patterns

## 🚦 Development Standards

This system follows strict development standards:
- **Template-based development** for consistency
- **Agent Orchestra compliance** for coordination
- **Security-first design** with Git operation constraints
- **Quality gates** for all changes
- **Visual documentation** for complex processes

See [CLAUDE.md](CLAUDE.md) for complete development rules.

## 🤝 Contributing

1. **Follow the templates** in `docs/command-template.md`
2. **Use Agent Orchestra patterns** from the developer guide
3. **Include visual documentation** for complex features
4. **Test Git operation constraints** thoroughly
5. **Update relevant documentation** with all changes

## 📖 Learn More

- **[Agent Orchestra Framework](docs/agent-orchestra-framework.md)** - Deep dive into the architecture
- **[Hooks System](docs/hooks-system.md)** - Event-driven automation details
- **[Spec-Kit Workflow](docs/spec-kit-workflow.md)** - Complete feature development process
- **[Developer Guide](docs/developer-guide.md)** - Extend and customize the system

---

**Ready to supercharge your development workflow?** Start with the [User Guide](docs/user-guide.md) and discover what the Agent Orchestra can do for you! 🎼✨