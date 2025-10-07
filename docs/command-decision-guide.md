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
│  └─ Use SPEC-KIT commands (/spec-kit:*)
│
├─ "I want to develop/fix specific functionality"
│  └─ Use DEVELOPMENT commands (/implement:*, /fix:*)
│
├─ "I want to improve code quality or apply formatting"
│  └─ Use QUALITY commands (/clean:*)
│
├─ "I want to create/update documentation"
│  └─ Use DOCUMENTATION commands (/docs:*)
│
├─ "I want to understand code or architecture"
│  └─ Use EXPLAIN commands (/explain:*, /guru)
│
└─ "I want to manage TODOs, sessions, or create new commands"
   └─ Use SYSTEM commands (/to-do:*, /session:*, /slashcommand:*, /subagent:*)
```

## Category Deep Dive

### Workflows (`/workflows:*`) - Orchestrated Multi-Step Processes

**When to use**: You want comprehensive, automated analysis or operations across multiple domains.

**Available Commands**:

- `/workflows:run-comprehensive-review` - Multi-perspective code review with dynamic analyst selection
- `/workflows:run-refactor-workflow` - Comprehensive refactoring using parallel domain analysis
- `/workflows:run-cleanup-workflow` - Orchestrated cleanup across quality and readability
- `/workflows:run-complete-overhaul` - Full codebase analysis across all quality perspectives
- `/workflows:run-docs-workflow` - Documentation analysis, generation, and validation
- `/workflows:run-optimization` - Performance, database, and bundle optimization
- `/workflows:run-security-audit` - Security vulnerability assessment across all layers
- `/workflows:run-lint-and-correct-all` - Detect languages and run all applicable linters

**Characteristics**:

- Parallel domain analyst execution for speed
- Comprehensive coverage across multiple perspectives
- Self-contained (can use Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch)
- Generates consolidated reports in `.artifacts/`

---

### Git (`/git:*`) - Version Control Operations

**When to use**: You need to perform git operations with safety checks and team workflows.

**Available Commands**:

- `/git:commit` - Smart commit message generation with quality checks
- `/git:branch` - Branch management with safety checks
- `/git:merge` - Controlled merge operations with conflict resolution
- `/git:push` - Push with safety checks and force-push protection
- `/git:pr` - Create and manage pull requests with GitHub CLI
- `/git:worktree` - Manage git worktrees for parallel development
- `/git:worktree-consolidate` - Merge changes from multiple worktrees
- `/git:full-workflow` - Complete workflow: branch, commit, push, PR in one command

**Characteristics**:

- Only commands authorized for git operations
- Built-in safety protocols and validation
- Team coordination features
- GitHub integration via gh CLI

---

### Spec-Kit (`/spec-kit:*`) - Feature Specification & Implementation

**When to use**: You're following a structured feature development workflow from specification to implementation.

**Available Commands**:

- `/spec-kit:specify` - Create/update feature specification from natural language
- `/spec-kit:plan` - Execute implementation planning workflow
- `/spec-kit:clarify` - Identify underspecified areas with targeted questions
- `/spec-kit:tasks` - Generate actionable, dependency-ordered task list
- `/spec-kit:analyze` - Cross-artifact consistency and quality analysis
- `/spec-kit:implement` - Execute implementation plan from tasks.md
- `/spec-kit:constitution` - Create/update project constitution

**Characteristics**:

- Structured workflow: specify → plan → clarify → tasks → implement
- Artifact-based approach (spec.md, plan.md, tasks.md)
- Cross-artifact consistency validation
- Project constitution integration

---

### Development (`/implement:*`, `/fix:*`) - Code Implementation & Bug Fixes

**When to use**: You need to implement features or fix bugs with focused, targeted changes.

**Available Commands**:

- `/implement:spec-kit-tasks` - Implement features using Agent Orchestra framework
- `/implement:small` - Quick implementation for small tasks bypassing spec-kit
- `/fix:bug-quickly` - Rapid bug fixes without full implementation complexity
- `/fix:import-statements` - Fix broken imports from file moves/renames

**Characteristics**:

- Targeted, specific changes
- Small to medium scope
- Agent coordination for complex tasks
- Quick turnaround for focused work

---

### Quality (`/clean:*`) - Code Quality & Formatting

**When to use**: You want to improve code readability, apply formatting rules, or enhance code structure.

**Available Commands**:

- `/clean:apply-style-rules` - Automated formatting using project's configured formatter
- `/clean:improve-readability` - Manual beautification: naming, structure, comments

**Characteristics**:

- Code improvement without behavior change
- Formatting and style enforcement
- Readability optimization
- Preserves functionality

---

### Documentation (`/docs:*`) - Documentation Management

**When to use**: You need to create, update, or maintain project documentation.

**Available Commands**:

- `/docs:extract-external` - Fetch up-to-date docs from external sources (Context7)
- `/docs:update` - Update existing project documentation intelligently
- `/docs:generate` - Generate comprehensive docs from codebase analysis
- `/docs:changelog` - Manage CHANGELOG.md with version history
- `/docs:api` - Generate and maintain API documentation

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

### System (`/to-do:*`, `/session:*`, `/utility:*`, `/slashcommand:*`, `/subagent:*`, `/prompt:*`) - Meta Operations

**When to use**: You need to manage project metadata, create new commands/agents, or handle system-level operations.

**Available Commands**:

**TODO Management:**

- `/to-do:create` - Capture work items into TODO.md
- `/to-do:convert-to-github-issues` - Create GitHub issues from TODO comments
- `/to-do:find-comments` - Locate all TODO comments in codebase

**Session Management:**

- `/session:start` - Start new session with topic label
- `/session:end` - End current session and optionally archive

**Development:**

- `/slashcommand:create-from-template` - Interactive command creation wizard
- `/subagent:create-from-template` - Interactive agent creation wizard

**Utilities:**

- `/utility:save-artifact-to-markdown` - Save Claude artifacts to organized folders
- `/utility:apply-spec-kit-mods` - Apply cross-repository path modifications
- `/prompt:enhanced` - Enhance prompts with command/agent knowledge

**Characteristics**:

- Project management
- Command system development
- Session tracking
- Artifact organization

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
/spec-kit:specify                      # Create specification
/spec-kit:plan                         # Plan architecture
/spec-kit:tasks                        # Generate task list
/spec-kit:implement                    # Execute implementation
/git:full-workflow                     # Branch, commit, push, PR
```

### "I want to fix a bug quickly"

```bash
/fix:bug-quickly "Issue description"   # Rapid targeted fix
/git:commit                            # Commit the fix
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
/clean:apply-style-rules              # Apply formatting rules
/git:commit                            # Commit cleanup changes
```

### "I want to update my documentation"

```bash
/workflows:run-docs-workflow           # Comprehensive doc workflow
# OR for targeted updates:
/docs:update [target]                  # Update specific docs
/docs:changelog [version]              # Update changelog
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
/spec-kit:specify → /spec-kit:plan → /spec-kit:tasks → /spec-kit:implement → /git:full-workflow
```

**Pre-Release Quality Check:**

```text
/workflows:run-comprehensive-review → /workflows:run-security-audit → /workflows:run-optimization → /git:commit
```

**Documentation Update Cycle:**

```text
/docs:extract-external [libraries] → /docs:generate [type] → /docs:update [target] → /git:commit
```

**Bug Fix Cycle:**

```text
/fix:bug-quickly [issue] → /git:commit → /git:push
```

## Tips for Command Selection

1. **Start Broad, Then Narrow**: Use workflows for initial comprehensive analysis, then atomic commands for specific fixes

2. **Leverage Parallelization**: Workflows run analysts in parallel - significantly faster than sequential atomic commands

3. **Check for Workflows First**: Most common multi-step tasks have optimized workflow commands

4. **Use Git Commands Exclusively**: Never use raw git commands - always use `/git:*` for safety checks

5. **Follow Spec-Kit for Features**: For new features, spec-kit provides structured workflow from idea to implementation

6. **Consult /guru**: When unsure, `/guru` provides context-aware guidance on command selection
