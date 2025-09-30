# Claude Code Command System

A comprehensive development automation system built on the **Agent Specialist Framework** that
transforms Claude Code into a powerful, coordinated development environment.

## 🎨 Professional Output Styles

Transform Claude Code into specialized domain experts with our collection of **12 professional output styles**.
Each style adapts Claude's communication to match industry-specific roles, terminology, and thinking patterns.

👉 **[Professional Output Styles Collection](docs/output-styles.md)** - Complete guide and style library

**Categories Available:**

- **Business & Strategy** (3 styles) - Product Manager, Strategic Consultant, Marketing Strategist
- **Technical & Analysis** (3 styles) - Data Scientist, Technical Writer, System Administrator
- **Creative & Design** (3 styles) - Brand Voice Curator, Presentation Designer, UX Researcher
- **Operations & Compliance** (3 styles) - Project Coordinator, Quality Assurance, Compliance Officer

## 🚀 Quick Start

### New User? Start Here

👉 **[User Guide](docs/user-guide.md)** - Complete setup and usage guide

### Developer? Extend the System

👉 **[Developer Guide](docs/developer-guide.md)** - Architecture and customization

### Want to See It in Action

👉 **[Typical Workflows](docs/typical-workflows.md)** - Common usage patterns with visual diagrams

## 🏗️ Architecture Overview

This system is built on the **Agent Specialist Framework** - a task-focused coordination system that uses 8 specialized agents
as advisory subagents to handle complex development tasks efficiently. Only the main Claude Code thread can orchestrate parallel execution.

### Agent Specialist Components

- **3 Analysis Specialists**: Provide strategic analysis and guidance
  - `task-analysis-specialist` - Complexity analysis and execution recommendations
  - `research-analysis-specialist` - Multi-domain research and synthesis
  - `implementation-strategy-specialist` - Dependency analysis and sequential guidance
- **5 Execution Specialists**: Provide focused domain expertise
  - `code-writer`, `test-writer`, `bug-fixer`, `reviewer`, `documenter`

### Command Categories (54 Commands)

- **`/analyze/*`** - Performance and dependency analysis
- **`/clean/*`** - Code cleanup and formatting
- **`/docs/*`** - Documentation generation and maintenance
- **`/fix/*`** - Bug fixes and issue resolution
- **`/git/*`** - Git operations (only commands that can perform Git operations)
- **`/review/*`** - Code review and quality analysis
- **`/spec-kit/*`** - Complete 7-step feature development workflow
- **`/workflows/*`** - Multi-step orchestrated processes

## 📚 Documentation

### For Users

- **[User Documentation](docs/user/)** - Setup, usage, and workflow guides
  - [User Guide](docs/user/user-guide.md) - Complete setup and usage instructions
  - [Typical Workflows](docs/user/typical-workflows.md) - Common usage patterns with diagrams
  - [MCP Setup Guide](docs/user/mcp-setup-guide.md) - External tool integration

### For Developers

- **[Developer Documentation](docs/developer/)** - Architecture and contribution guidelines
  - [Developer Guide](docs/developer/developer-guide.md) - Architecture and contribution workflow
  - [Command Template](docs/developer/command-template.md) - Standard format for new commands
  - [Hooks System](docs/developer/hooks-system.md) - Cross-platform automation guide
  - [Developer Workflows](docs/developer/developer-workflows.md) - Advanced development patterns

### For Administrators

- **[Admin Documentation](docs/admin/)** - System administration and monitoring
  - [Command Audit Report](docs/admin/command-audit-report.md) - System analysis and compliance
  - [Implementation Summary](docs/admin/implementation-summary.md) - Technical implementation details

### Concepts and Architecture

- **[Conceptual Documentation](docs/concepts/)** - Deep architecture insights
  - [Agent Specialist Framework](docs/concepts/agent-orchestra-framework.md) - Specialist agent coordination
  - [Spec-Kit Workflow](docs/concepts/spec-kit-workflow.md) - Feature development process
  - [Parallel Execution Patterns](docs/concepts/parallel-execution-patterns.md) - Performance optimization

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
```text

## 📁 System Structure

```text
├── agents/                    # Agent Specialist definitions
│   ├── analysis-specialists/  # Strategic analysis agents
│   └── execution-specialists/ # Domain expertise agents
├── commands/                 # 54 organized commands
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

5. **Optional: Set up MCP Integration:**
   See [docs/mcp-setup-guide.md](docs/mcp-setup-guide.md) for Context7 and Playwright setup.

## 🎨 Visual Documentation

All complex workflows include **Mermaid diagrams** for clear understanding:

- Agent coordination patterns
- Hook system flows
- Spec-kit workflow steps
- Typical usage patterns

## 🚦 Development Standards

This system follows strict development standards:

- **Template-based development** for consistency
- **Agent Specialist Framework compliance** for coordination
- **Security-first design** with Git operation constraints
- **Quality gates** for all changes
- **Visual documentation** for complex processes

See [CLAUDE.md](CLAUDE.md) for complete development rules.

## 🤝 Contributing

1. **Follow the templates** in `docs/command-template.md`
2. **Use Agent Specialist Framework patterns** from the developer guide
3. **Include visual documentation** for complex features
4. **Test Git operation constraints** thoroughly
5. **Update relevant documentation** with all changes

## 📖 Learn More

- **[Agent Specialist Framework](docs/concepts/agent-orchestra-framework.md)** - Deep dive into the architecture
- **[Hooks System](docs/hooks-system.md)** - Event-driven automation details
- **[Spec-Kit Workflow](docs/spec-kit-workflow.md)** - Complete feature development process
- **[Developer Guide](docs/developer-guide.md)** - Extend and customize the system

---

**Ready to supercharge your development workflow?** Start with the [User Guide](docs/user/user-guide.md) and
discover what the Agent Specialist Framework can do for you! 🎼✨
