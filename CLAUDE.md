# Claude Code Configuration - Command System Project

This file contains **project-specific** configuration for the Claude Code command system project.

## 🎯 Repository Overview

The Claude Code Command System provides development automation through domain analysts, slash commands, cross-platform Python hooks, and MCP integration (Context7, Playwright, Shadcn).

**Core Components**:

- **Domain Analysts**: Specialized agents for research, framework expertise, quality analysis, security, performance, and more
- **Slash Commands**: Atomic commands and orchestrated workflows organized by category (git, docs, workflows, etc.)
- **Hooks**: Python-based automation for logging, notifications, and context management
- **MCP Integration**: External tool access for documentation (Context7), browser automation (Playwright), and UI components (Shadcn)

## 🎨 Frontmatter Standards

**Single Source of Truth**: Frontmatter syntax and structure are defined ONLY in templates.

**CLAUDE.md Role**:

- ✅ Reference templates for frontmatter specifications
- ✅ Explain the distinction between command and agent frontmatter
- ❌ Do NOT duplicate frontmatter YAML examples
- ❌ Do NOT show specific field syntax

**Key Distinction**:

- **Commands** declare permissions via `allowed-tools` frontmatter
- **Agents** declare capabilities via `tools` frontmatter

**Template References**:

- Command frontmatter: See `templates/commands/command.md` and `templates/commands/command-workflow.md`
- Agent frontmatter: See `templates/agents/agent-domain-specialist.md`

## 🏗️ Domain Analyst Framework

### Research Analyst

**research-analyst** - Comprehensive sequential research across multiple domains with synthesized findings (uses Context7)

### Domain Analysts

**Framework/Technology:** react-analyst, typescript-analyst, python-analyst, api-analyst, shadcn-analyst
**Quality/Architecture:** quality-analyst, architecture-analyst (opus+ultrathink), refactoring-analyst
**Security/Performance:** security-analyst, performance-analyst
**Testing/Accessibility:** testing-analyst, accessibility-analyst
**Documentation/Data:** documentation-analyst, database-analyst, frontend-analyst

<<<<<<< Updated upstream
**Pattern**: Conduct comprehensive research → persist lean, actionable findings to `.agent/context/{session-id}/{agent-name}.md` → return concise summary with task counts (context elision)
=======
**Pattern**: Conduct comprehensive research → persist detailed findings to `.agent/context/{session-id}/{agent-name}.md` → return concise summary (context elision)
>>>>>>> Stashed changes

### Agent Coordination

**Main Thread:** Parallelizes Task tools, invokes multiple domain analysts concurrently, runs one slash command at a time

**Slash Commands:** Absorb main thread capabilities (unless restricted), coordinate domain analysts (series/parallel), can daisy-chain ONE other command as final action (no post-processing)

**Domain Analysts:** Must persist lean, actionable findings to `.agent/context/{session-id}/{agent-name}.md`, update incrementally if file exists, cannot invoke other analysts or slash commands reliably

**System:** Changes to CLAUDE.md/commands/agents require Claude Code restart

## 🧠 Model Inheritance

**Default:** `model: inherit` (inherits from main thread)
**Complex reasoning:** `model: opus` + `thinking: ultrathink` (architecture, system design only)

## 📦 Context Management System

<<<<<<< Updated upstream
**Directory Structure**:

```text
.agent/context/
└── {session-id}/
    ├── session.md              # Session metadata and summary
    ├── python-analyst.md       # One file per agent
    ├── security-analyst.md
    └── {agent-name}.md
```

**Required:** All domain analysts persist findings to `.agent/context/{session-id}/{agent-name}.md`
=======
**Required:** All domain analysts persist findings to `.agent/context/{session-id}/{agent-name}.md`

**Path Strategy**: Project-local context storage in `{project_root}/.agent/context/`
- Context files are stored within each project's `.agent/` directory
- Enables project-specific analysis without cross-project pollution
- Session isolation prevents context collision between concurrent analyses

**Naming Pattern**: `{session-id}/{agent-name}.md`

**Example**: `abc123/performance-analyst.md`
>>>>>>> Stashed changes

**Session Commands**:

<<<<<<< Updated upstream
- Get session ID: `python3 ~/.claude/.agent/scripts/session_manager.py current`
- Get context directory: `python3 ~/.claude/.agent/scripts/session_manager.py context_dir`
- Initialize session: `python3 ~/.claude/.agent/scripts/session_manager.py init [topic]`
- List agents invoked: `python3 ~/.claude/.agent/scripts/session_manager.py list_agents`
- Archive session: `python3 ~/.claude/.agent/scripts/session_manager.py archive`

**Lean Context Principle**: Context files must be scannable in <30 seconds - focus on actionable tasks, not verbose analysis

**Why:** Enables multi-analyst coordination, incremental updates, and clean organization without context pollution

**Main Thread Responsibility**: After executing agent recommendations, update context file's "Main Thread Log" section with completion status
=======
**Session ID**: Agents obtain current session ID via: `python3 ~/.claude/.agent/scripts/session_manager.py current`
>>>>>>> Stashed changes

## 🚀 Parallel Research Pattern

**Workflow:** Parallel research (multiple analysts) → Sequential implementation → Parallel QA

**Performance:** Significantly faster than sequential execution through concurrent analyst invocations

## 📁 Command System

**Categories:** analyze, artifact, clean, docs, explain, fix, git, implement, plan, prompt, refactor, review, spec-kit, to-do, workflows

**Atomic Design:** Single-purpose, clear responsibility, composable, template-compliant (use `templates/commands/command.md` or `templates/commands/command-workflow.md`)

**Frontmatter**: See templates for complete specifications

## 🔌 MCP Integration

**Context7:** Library/framework documentation (docs, review, analysis commands)
**Playwright:** Browser automation (design review, testing workflows)

## 🌐 Cross-Platform

All automation uses Python with `pathlib.Path` for Windows/macOS/Linux compatibility. Use `Path.home()` for user directories.

## 🔐 Security & Git Constraints

**CRITICAL:** Only `/git/*` commands perform Git operations. All other agents/commands use SlashCommand tool for Git delegation.

**Git Conventions:** Conventional commit format with auto-detected types from file analysis (feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert)

**Permissions:** Context7/Playwright tools allowed. Block secrets (.env, *.key, credentials). Restrict dangerous operations (rm -rf, sudo). See `settings.json`.

## 📦 Artifact Management

Use `/artifact:save` to capture Claude outputs (plans, reviews, research) in `.artifacts/` with type-based organization.

## 🤖 AI Code Review

Use `/review:code` for comprehensive code review with domain analyst delegation. For multi-perspective reviews, use `/workflows:run-comprehensive-review` with dynamic analyst selection, parallel execution, and unified reporting.

## 📚 Documentation

Docs in `docs/` following Diátaxis framework (tutorials, guides, reference, explanation). Start with `README.md` and `docs/user-guide.md`.

## 🔧 Development Standards

### Markdown Linting

Follow `.markdownlint.yml`: 150-char lines (code: 200), ATX headers with blank lines, fenced code with language tags, asterisk emphasis, 2-space lists, inline HTML allowed. Exceptions in `.markdownlintignore`.

### Command Development

**Templates:** `templates/commands/command.md` (atomic), `templates/commands/command-workflow.md` (orchestration)

**Frontmatter:** See templates for complete specifications and required fields

**Key Requirements:** Single-purpose, clear responsibility, composable design

### Agent Development

**Requirements:** Single responsibility, no overlap, follow domain-analyst pattern, model: inherit (default) or opus (complex reasoning), use SlashCommand for delegation

**Frontmatter:** See `templates/agents/agent-domain-specialist.md` for complete specifications

**Key Requirements:** Clear domain focus, advisory role (analyze and recommend, not execute)

### Spec-Kit Integration

When `.specify/` exists: reference `spec.md` (requirements), `plan.md` (architecture), `tasks.md` (completion), `contracts/` (API compliance)

**Cross-Repository Paths:** Use `~/.claude/.specify/scripts/` and `~/.claude/.specify/templates/` (reapply with `/utility:apply-spec-kit-mods`)

## 🔄 CRUD Operations

### TODO Location Constraint

**CRITICAL:** All TODO operations use `{project_root}/.claude/.todos/TODO.md` ONLY. Prohibited: TODO files elsewhere.

### Creating Commands

1. Use template from `docs/command-template.md`
2. Place in `commands/{category}/{name}.md`
3. Assign to existing domain analyst
4. Include MCP tools if relevant
5. Ensure atomic design

**Reapply Spec-Kit Mods:**

```bash
/utility:apply-spec-kit-mods
```

## 🔄 Workflows

**TODO Management:** Use standardized location `{project_root}/.claude/.todos/TODO.md` via `/to-do:*` commands

**Command/Agent Changes:** Follow templates, maintain atomic design, update CLAUDE.md after changes

## ⚠️ Critical Constraints

**Git Operations:** ONLY `/git/*` commands can perform Git operations
**Cross-Platform:** No hardcoded user paths (use `~/.claude/`)
**Agent Uniqueness:** Each agent has single, unique responsibility
**MCP Integration:** Use Context7/Playwright where appropriate
**Atomic Design:** Keep commands single-purpose
**CLAUDE.md Sync:** Update after creating/modifying/deleting agents or commands

### CLAUDE.md Disambiguation Protocol

**When working with multiple CLAUDE.md files, ALWAYS ask:** "Are you referring to user CLAUDE.md (global patterns in ~/CLAUDE.md) or project CLAUDE.md (project-specific in /Users/thomasholknielsen/.claude/CLAUDE.md)?"

**NO EXCEPTIONS** - applies to reading, editing, referencing, suggesting updates, or ANY mention of CLAUDE.md.

---

**Note:** This configuration provides comprehensive instructions for working with all repository artifacts while maintaining quality, security, and cross-platform compatibility standards.
