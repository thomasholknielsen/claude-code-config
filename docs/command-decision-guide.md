# Command Decision Guide

## Overview

This guide helps you select the right command for your task. Commands are organized by intent and workflow stage.

## Quick Decision Flowchart

```text
START: What do you want to accomplish?
│
├─ "I want comprehensive analysis/cleanup/optimization"
│  └─ Use WORKFLOW commands (/workflows:*)
│
├─ "I want to commit/push/manage git operations"
│  └─ Use GIT commands (/git:*)
│
├─ "I want to manage feature specifications and implementation"
│  └─ Use SPEC-KIT commands (/speckit:*)
│
├─ "I want to improve code quality or apply formatting"
│  └─ Use LINT commands (/lint:*)
│
├─ "I want to create/update documentation"
│  └─ Use DOCUMENTATION commands (/docs:*)
│
├─ "I want to understand code or architecture"
│  └─ Use EXPLAIN commands (/explain:*, /guru)
│
└─ "I want to manage tasks, sessions, or create new agents/commands"
   └─ Use SYSTEM/CLAUDE commands (/task:*, /session:*, /claude:*, /system:*)
```

## Category Deep Dive

### Workflows (`/workflows:*`) - Orchestrated Multi-Step Processes

**When to use**: You want comprehensive, automated analysis or operations across multiple domains.

**Available Commands**:

- `/workflows:run-comprehensive-review` - Multi-perspective code review with dynamic analyst selection
- `/workflows:run-refactor-workflow` - Comprehensive refactoring using parallel domain analysis
- `/workflows:run-cleanup-workflow` - Orchestrated cleanup across quality and readability
- `/workflows:run-complete-overhaul` - Full codebase analysis across all quality perspectives
- `/workflows:docs` - Idempotent documentation workflow (CRUD operations on all doc types)
- `/workflows:run-optimization` - Performance, database, and bundle optimization
- `/workflows:run-security-audit` - Security vulnerability assessment across all layers

**Characteristics**:

- Parallel domain analyst execution for speed
- Comprehensive coverage across multiple perspectives
- Self-contained (can use Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch)
- Generates consolidated reports in `.artifacts/`

---

### Git (`/git:*`) - Version Control Operations

**When to use**: You need to perform git operations with safety checks and team workflows.

**Available Commands**:

**Standard Git Operations:**

- `/git:commit` - Smart commit message generation with quality checks
- `/git:push` - Push with safety checks and force-push protection
- `/git:pr` - Create and manage pull requests with GitHub CLI (git-flow aware)
- `/git:worktree` - Manage git worktrees for parallel development
- `/git:worktree-consolidate` - Merge changes from multiple worktrees
- `/workflows:git` - Complete workflow with logical commits: branch, commit, push, PR (git-flow aware)

**Workflow Mode Auto-Detection:**
Commands automatically detect repository mode:

- **Git-Flow mode**: When both `main` and `develop` branches exist
  - feature/* branches from develop → PR targets develop
  - release/* branches from develop → PR targets main
  - hotfix/* branches from main → PR targets main
- **Conventional mode**: When develop doesn't exist (default)
  - feat/fix/docs/* branches from HEAD → PR targets main

---

### Git-Flow (`/git-flow:*`) - Git Flow Branching Model

**When to use**: You're working with the Git Flow branching model (main/develop with feature/release/hotfix branches).

**Available Commands**:

- `/git-flow:feature <name>` - Create feature branch from develop
- `/git-flow:release <version>` - Create release branch with version management and changelog
- `/git-flow:hotfix <name>` - Create emergency hotfix branch from main
- `/git-flow:finish` - Complete and merge current branch (feature/release/hotfix) with cleanup
- `/git-flow:status` - Display comprehensive Git Flow repository status

**Git Flow Workflow:**

1. **Features**: Branch from develop → merge back to develop
2. **Releases**: Branch from develop → merge to main AND develop, create tag
3. **Hotfixes**: Branch from main → merge to main AND develop, create tag

**Multi-Language Version Support:**

- Node.js: Updates `package.json` and `package-lock.json`
- Python: Updates `pyproject.toml`
- Rust: Updates `Cargo.toml` and `Cargo.lock`

**Characteristics**:

- Only commands authorized for git operations
- Automatic workflow mode detection (git-flow vs conventional)
- Built-in safety protocols and validation
- Team coordination features
- GitHub integration via gh CLI
- Semantic versioning support (git-flow)

---

### Spec-Kit (`/speckit:*`) - Feature Specification & Implementation

**When to use**: You're following a structured feature development workflow from specification to implementation.

**Available Commands**:

- `/speckit:specify` - Create/update feature specification from natural language
- `/speckit:plan` - Execute implementation planning workflow
- `/speckit:clarify` - Identify underspecified areas with targeted questions
- `/speckit:tasks` - Generate actionable, dependency-ordered task list
- `/speckit:analyze` - Cross-artifact consistency and quality analysis
- `/speckit:implement` - Execute implementation plan from tasks.md
- `/speckit:constitution` - Create/update project constitution

**Characteristics**:

- Structured workflow: specify → plan → clarify → tasks → implement
- Artifact-based approach (spec.md, plan.md, tasks.md)
- Cross-artifact consistency validation
- Project constitution integration

---

### Lint (`/lint:*`) - Code Quality & Formatting

**When to use**: You want to automatically fix linting and formatting issues across the codebase.

**Available Commands**:

- `/lint:correct-all` - Detect project languages and run all applicable linters with auto-fix in parallel

**Characteristics**:

- Automatic language detection (Python, JavaScript/TypeScript, Shell, Markdown)
- Parallel execution of multiple linters
- Auto-fix formatting issues
- Project-specific linter configuration support

---

### Documentation (`/docs:*`) - Documentation Management

**When to use**: You need to create, update, or maintain project documentation.

**Available Commands**:

- `/workflows:docs` - Idempotent documentation workflow (handles all CRUD operations)
- `/docs:changelog` - Manage CHANGELOG.md following Keep a Changelog v1.1.0

**Characteristics**:

- Documentation completeness
- External library integration (Context7)
- Automated generation from code
- Version history management

---

### Explain (`/explain:*`, `/guru`) - Understanding & Learning

**When to use**: You want to understand code, architecture, or get guidance on workflows.

**Available Commands**:

- `/explain:code` - Clear code explanations with context-appropriate depth
- `/explain:architecture` - Analyze application architecture and component relationships
- `/guru` - Context-aware intelligent assistant with personalized guidance

**Characteristics**:

- No code changes
- Educational focus
- Project-aware guidance
- Architecture understanding

---

### Task Management (`/task:*`) - Task Tracking & Execution

**When to use**: You need unified task management with origin tagging and GitHub integration.

**Available Commands**:

- `/task:execute` - Intelligent task triaging and execution with speckit integration
- `/task:add` - Capture adhoc tasks with standardized metadata
- `/task:scan-project` - Find code comments (TODO, FIXME, HACK, BUG) and consolidate to tasks
- `/task:archive` - Move completed tasks to archive file
- `/task:help` - Guide to using the unified task management system

**Characteristics**:

- Origin tagging (adhoc, code-comment, github-issue)
- Bidirectional GitHub sync
- Stored in `.agent/tasks.md` (active) and `tasks-archive.md` (completed)

---

### GitHub Integration (`/github:*`) - Issue Management

**When to use**: You need to sync tasks with GitHub issues for team collaboration.

**Available Commands**:

- `/github:fetch-issues` - Fetch GitHub issues to session context
- `/github:convert-issues-to-tasks` - Convert GitHub issues to local tasks with origin tagging
- `/github:create-issue-from-task` - Create GitHub issue from task with proper labeling

**Characteristics**:

- Bidirectional sync between local tasks and GitHub issues
- Origin tagging for traceability
- Milestone and label support

---

### Session Management (`/session:*`) - Session Lifecycle

**When to use**: You need to initialize or end development sessions with context tracking.

**Available Commands**:

- `/session:start` - Start new session with topic label for context file organization
- `/session:end` - End current session and optionally archive context files

**Characteristics**:

- Session context tracking in `.agent/Session-{name}/context/`
- Topic-based organization
- Optional archival of completed sessions

---

### Claude System (`/claude:*`) - Agent & Command Creation

**When to use**: You need to create new agents or commands, or get intelligent guidance.

**Available Commands**:

- `/claude:create-agent` - Intelligent agent creation with expert consultation
- `/claude:create-command` - Intelligent command creation with expert consultation
- `/claude:guru` - Context-aware intelligent assistant with personalized guidance
- `/claude:review-claude-md` - Review CLAUDE.md quality with interactive fixes
- `/claude:apply-global-claude-md-to-current-user` - Sync CLAUDE-GLOBAL.md to user CLAUDE.md

**Characteristics**:

- Expert-guided creation process
- Context-aware recommendations
- Template compliance validation
- Configuration management

---

### System Utilities (`/system:*`) - System-Level Operations

**When to use**: You need to perform system-level operations like artifact saving or MCP setup.

**Available Commands**:

- `/system:save-artifact-to-markdown` - Save Claude artifacts to organized folders
- `/system:setup-mcp` - Interactive wizard for setting up MCP servers
- `/system:find-comments` - Locate code comments (TODO, FIXME, HACK, BUG) in codebase

**Characteristics**:

- Artifact organization
- MCP server configuration
- Code comment discovery

---

### Prompt Engineering (`/prompt:*`) - Prompt Enhancement

**When to use**: You need to enhance prompts using S-tier frameworks.

**Available Commands**:

- `/prompt:enhance` - Transform prompts using frameworks (RISEN, COSTAR, APE, auto)

**Characteristics**:

- S-tier prompt engineering frameworks
- Framework auto-detection
- Quick and complete enhancement modes

## Workflow vs Atomic Command Strategy

### Use Workflows When

- ✅ You want comprehensive analysis across multiple domains
- ✅ Speed matters (parallel execution is significantly faster)
- ✅ You need consolidated findings from multiple perspectives
- ✅ The task spans multiple quality dimensions (security + performance + architecture)
- ✅ You're willing to let the system make decisions within defined parameters

### Use Atomic Commands When

- ✅ You need surgical, targeted operations
- ✅ You want explicit control over each step
- ✅ The task is highly specific to one domain
- ✅ You're working iteratively and need intermediate feedback
- ✅ You want to chain commands manually for custom workflows

### Complementary Usage

Many workflows **use** atomic commands internally. You can also:

- Run a workflow for analysis, then use atomic commands for specific fixes
- Use atomic commands during development, then run workflows for comprehensive QA
- Combine workflow analysis with manual implementation using atomic commands

## Examples by User Intent

### "I want to improve my codebase before a release"

```bash
/workflows:run-comprehensive-review    # Multi-perspective analysis
/workflows:run-optimization            # Performance improvements
/workflows:run-security-audit          # Security validation
/git:commit                            # Commit improvements
```

### "I want to implement a new feature following best practices"

```bash
/speckit:specify                      # Create specification
/speckit:plan                         # Plan architecture
/speckit:tasks                        # Generate task list
/speckit:implement                    # Execute implementation
/workflows:git                          # Logical commits, push, PR
```

### "I want to debug an issue"

```bash
/explain:code path/to/problematic/file  # Understand the code
# Make manual fixes
/git:commit                             # Commit the fix
```

### "I want to understand this codebase"

```bash
/explain:architecture                  # Understand system design
/explain:code [target]                 # Understand specific code
/guru                                  # Get personalized guidance
```

### "I need to clean up my code before review"

```bash
/workflows:run-cleanup-workflow        # Comprehensive cleanup
/lint:correct-all                      # Auto-fix linting issues
/git:commit                            # Commit cleanup changes
```

### "I want to update my documentation"

```bash
/workflows:docs                        # Idempotent doc workflow (all CRUD operations)
# OR for manual changelog:
/docs:changelog [version]              # Manage CHANGELOG.md manually
```

## Command Relationships

### Workflows That Replace Deprecated Commands

| Deprecated Command | Replacement Workflow | Migration Path |
|-------------------|---------------------|----------------|
| `/review:code` | `/workflows:run-comprehensive-review` | Direct replacement with multi-perspective analysis |
| `/refactor:apply` | `/workflows:run-refactor-workflow` | Use workflow for comprehensive refactoring |
| `/refactor:large-scale` | `/workflows:run-refactor-workflow` | Same workflow handles both small and large refactoring |

See `commands/deprecated/MIGRATION-GUIDE.md` for full details.

### Common Command Sequences

**Feature Development:**

```text
/speckit:specify → /speckit:plan → /speckit:tasks → /speckit:implement → /workflows:git
```

**Pre-Release Quality Check:**

```text
/workflows:run-comprehensive-review → /workflows:run-security-audit → /workflows:run-optimization → /git:commit
```

**Documentation Update Cycle:**

```text
/workflows:docs → /git:commit
```

**Bug Fix Cycle:**

```text
/explain:code [file] → manual fixes → /git:commit → /git:push
```

## Tips for Command Selection

1. **Start Broad, Then Narrow**: Use workflows for initial comprehensive analysis, then atomic commands for specific fixes

2. **Leverage Parallelization**: Workflows run analysts in parallel - significantly faster than sequential atomic commands

3. **Check for Workflows First**: Most common multi-step tasks have optimized workflow commands

4. **Use Git Commands Exclusively**: Never use raw git commands - always use `/git:*` or `/git-flow:*` for safety checks

5. **Follow Spec-Kit for Features**: For new features, speckit provides structured workflow from idea to implementation

6. **Consult /guru**: When unsure, `/guru` provides context-aware guidance on command selection
