# Claude Code Command System

A comprehensive development automation system built on the **Domain Analyst Framework** that
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

👉 **[User Guide](docs/user/user-guide.md)** - Complete setup and usage guide

**Important:** After cloning, configure MCP servers in your `~/.claude.json`:
👉 **[MCP User Setup](MCP-USER-SETUP.md)** - Required for full functionality

### Developer? Extend the System

👉 **[Developer Guide](docs/developer/developer-guide.md)** - Architecture and customization

### Want to See It in Action

👉 **[Developer Workflows Guide](docs/typical-workflows.md)** - Realistic workflows with review-lint-commit pattern

- **Visual diagrams** showing workflow patterns, timing comparisons, and command orchestration
- Real-world workflow examples with realistic task complexity
- Performance analysis: Significantly faster with local review

## 🏗️ Architecture Overview

This system provides development automation via **comprehensive domain analysts**, **streamlined command library**, and **cross-platform Python hooks**,
with MCP integration (7 servers: Context7 for docs, Playwright for browser automation, fetch for web content, markitdown for document conversion, terraform for infrastructure, shadcn for UI components, sequential-thinking for enhanced reasoning).

### Domain Analyst Framework

**Research Analysts**:

- `research-codebase-analyst` - Comprehensive sequential codebase research across domains
- `research-web-analyst` - Advanced web research and multi-source verification

**Domain Analysts** (45 total across 13 domains):

- **API**: api-rest-analyst, api-graphql-analyst, api-docs-analyst
- **Database**: database-analyst, database-sql-analyst, database-nosql-analyst, database-architecture-analyst
- **Frontend**: frontend-analyst, frontend-react-analyst, frontend-nextjs-analyst, frontend-accessibility-analyst, frontend-shadcn-analyst
- **Code Quality**: code-python-analyst, code-typescript-analyst, code-javascript-analyst, code-csharp-analyst, code-quality-analyst
- **Infrastructure**: infrastructure-terraform-analyst, infrastructure-cloud-analyst, infrastructure-network-analyst, infrastructure-devops-analyst, infrastructure-monitoring-analyst
- **Mobile**: mobile-react-native-analyst, mobile-flutter-analyst, mobile-ios-swift-analyst
- **Documentation**: docs-analyst, docs-docusaurus-analyst
- **UI/UX**: ui-ux-analyst, ui-ux-cli-analyst
- **Compliance**: compliance-analyst
- **Standalone**: architecture-analyst, security-analyst, performance-analyst, testing-analyst, refactoring-analyst, debugger-analyst, seo-analyst, product-roadmap-analyst, prompt-analyst
- **Meta**: agent-expert, command-expert, git-flow-analyst

**Pattern**: Analysts conduct extensive research → persist to `.agent/context/{session-id}/{agent-name}.md` → return concise summaries

### Command Categories (12 total)

- **`/claude/*`** - Agent/command creation and system guidance
- **`/docs/*`** - Documentation generation and maintenance
- **`/explain/*`** - Code and architecture explanation
- **`/git/*`** - Complete Git operation toolset (only /git/* commands can perform git operations)
- **`/git-flow/*`** - Git-Flow workflow commands (feature, release, hotfix)
- **`/github/*`** - GitHub issue integration and task conversion
- **`/lint/*`** - Linting and formatting automation
- **`/prompt/*`** - Prompt engineering and enhancement
- **`/session/*`** - Session management and tracking
- **`/speckit/*`** - Feature development workflow automation
- **`/system/*`** - System utilities and setup
- **`/task/*`** - Task management and execution

## 📚 Documentation

### For Users

- **[User Documentation](docs/user/)** - Setup, usage, and workflow guides
  - [User Guide](docs/user/user-guide.md) - Complete setup and usage instructions
  - [MCP Setup Guide](docs/user/mcp-setup-guide.md) - External tool integration
  - **[MCP User Setup](MCP-USER-SETUP.md)** - Configure all MCP servers in `~/.claude.json`
- **[Developer Workflows Guide](docs/typical-workflows.md)** - Realistic patterns with review-lint-commit workflow
  - Includes local PR review before committing (significantly faster than team reviews)
  - Comprehensive linting automation
  - Performance comparisons and best practices

### For Developers

- **[Developer Documentation](docs/developer/)** - Architecture and contribution guidelines
  - [Developer Guide](docs/developer/developer-guide.md) - Architecture and contribution workflow
  - [Command Template](docs/developer/command-template.md) - Standard format for new commands
  - [Hooks System](docs/developer/hooks-system.md) - Cross-platform automation guide
  - [Developer Workflows](docs/developer/developer-workflows.md) - Advanced development patterns

### Concepts and Architecture

- **[Conceptual Documentation](docs/concepts/)** - Deep architecture insights
  - [Spec-Kit Workflow](docs/concepts/speckit-workflow.md) - Feature development process
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

## 🎯 Quick Command Reference

### 🔍 Not Sure Which Command to Use

```bash
/claude:guru                       # Get context-aware command suggestions
/claude:guru [topic]               # Get detailed guidance on specific topic
```

👉 **[Command Selection Guide](docs/user/command-selection-guide.md)** - Visual decision trees for finding the right command

### 🚀 Most Used Commands

**Git & Version Control:**

```bash
/git:commit "message"              # Smart commit with validation
/git:complete branch-name          # Feature branch: commit, push, PR
/git:pr "title"                    # Create pull request
/git:worktree feature-name         # Parallel development
```

**Code Quality & Linting:**

```bash
/lint:correct-all                  # Fix all linting issues
/git-flow:status                   # Check Git-Flow branch status
```

**Feature Development:**

```bash
/speckit:specify "feature"         # Create feature spec
/speckit:plan                      # Generate implementation plan
/speckit:implement                 # Execute implementation
```

**Code Understanding:**

```bash
/explain:code path/to/file         # Explain specific code
/explain:architecture              # Explain system architecture
/claude:guru                       # Get context-aware command suggestions
```

**Documentation:**

```bash
/docs:sync                         # Sync docs to match code changes
/docs:changelog version            # Manage CHANGELOG.md
```

**Task Management:**

```bash
/task:execute TASK-XXX             # Execute specific task
/task:search "keyword"             # Search tasks
/session:start topic               # Start work session
```

### 📖 Complete Command List

See [Command Selection Guide](docs/user/command-selection-guide.md) for visual decision trees and complete command reference.

## 📁 System Structure

```text
├── agents/                   # 45 Domain Analysts across 13 domains
├── commands/                 # 45 Commands across 12 categories
│   ├── claude/              # Agent/command creation and guru
│   ├── docs/                # Documentation management
│   ├── explain/             # Code and architecture explanation
│   ├── git/                 # Git operations (exclusive)
│   ├── git-flow/            # Git-Flow workflow commands
│   ├── github/              # GitHub issue integration
│   ├── lint/                # Linting and formatting
│   ├── prompt/              # Prompt engineering
│   ├── session/             # Session management
│   ├── speckit/             # Feature development workflow
│   ├── system/              # System utilities
│   └── task/                # Task management
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
   chmod +x scripts/**/*.py
   ```

3. **Test installation:**

   ```bash
   claude /help
   ```

4. **Follow the User Guide:**
   See [docs/user-guide.md](docs/user/user-guide.md) for detailed setup instructions.

5. **Optional: Set up MCP Integration:**
   See [docs/mcp-setup-guide.md](docs/user/mcp-setup-guide.md) for Context7 and Playwright setup.

## 🎨 Visual Documentation

All complex workflows include **Mermaid diagrams** for clear understanding:

- **Multiple workflow diagrams** in [Developer Workflows Guide](docs/typical-workflows.md):
  - Review-Lint-Commit pattern flowchart with decision points
  - Bug fix sequence diagram showing command interactions
  - Performance comparison showing significant improvement with parallel execution
  - Daily development timelines (morning feature work, afternoon bug fixes)
  - Command chaining patterns visualization
  - Large-scale refactoring parallel execution flow
- Agent coordination patterns
- Hook system flows
- Spec-kit workflow steps

## 🚦 Development Standards

This system follows strict development standards:

- **Template-based development** for consistency
- **Domain Analyst Framework compliance** for coordination
- **Security-first design** with Git operation constraints
- **Quality gates** for all changes
- **Visual documentation** for complex processes

See [CLAUDE.md](CLAUDE.md) for complete development rules.

## 🤝 Contributing

1. **Follow the templates** in `docs/command-template.md`
2. **Use Domain Analyst Framework patterns** from the developer guide
3. **Include visual documentation** for complex features
4. **Test Git operation constraints** thoroughly
5. **Update relevant documentation** with all changes

## 📖 Learn More

- **[Hooks System](docs/developer/hooks-system.md)** - Event-driven automation details
- **[Spec-Kit Workflow](docs/concepts/speckit-workflow.md)** - Complete feature development process
- **[Developer Guide](docs/developer/developer-guide.md)** - Extend and customize the system
- **[Domain Analyst Framework](CLAUDE.md)** - Complete framework documentation

---

**Ready to supercharge your development workflow?** Start with the [User Guide](docs/user/user-guide.md) and
discover what the Domain Analyst Framework can do for you! 🎼✨
