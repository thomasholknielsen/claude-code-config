# Claude Code Configuration - Command System Project

This file contains **project-specific** configuration for the Claude Code command system project.

## 🎯 Repository Overview

The Claude Code Command System provides development automation through domain analysts, slash commands, cross-platform Python hooks, and MCP integration (Context7, Playwright, Shadcn).

**Core Components**:

- **Domain Analysts**: Specialized agents for research, framework expertise, quality analysis, security, performance, and more
- **Slash Commands**: Atomic commands and orchestrated workflows organized by category (git, docs, workflows, etc.)
- **Hooks**: Python-based automation for logging, notifications, and context management
- **MCP Integration**: External tool access for documentation (Context7), browser automation (Playwright), and UI components (Shadcn)

## 📋 Anti-Drift Principles

**CRITICAL**: Avoid documentation that drifts from reality when the codebase changes.

**Prohibited**:

- ❌ Hard-coded counts ("15 domain analysts", "47 commands")
- ❌ Percentage statistics ("32% reduction after refactoring")
- ❌ Performance timings ("3-5min", "75-85% faster")
- ❌ Timeline estimates ("first week", "30-60 minutes", "1-3 months")
- ❌ Token burn percentages ("burn 90%+ tokens")
- ❌ Specific time comparisons ("5-8min vs 25-35min")

**Preferred**:

- ✅ Structural descriptions ("Multiple domain analysts", "Comprehensive command library")
- ✅ Qualitative improvements ("Significantly faster", "Improved performance")
- ✅ Priority levels ("Critical/High/Medium", "Immediate/Short-term/Long-term")
- ✅ Relative descriptions ("Main thread can parallelize", "Agents run sequentially")

**Rationale**: Statistics become outdated immediately upon system changes. Focus on principles, patterns, and architecture over precise metrics.

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

### Research Analyst (1)

**research-analyst** - Comprehensive sequential research across multiple domains with synthesized findings (uses Context7)

### Domain Analysts (14)

**Framework/Technology:** react-analyst, typescript-analyst, python-analyst, api-analyst
**Quality/Architecture:** quality-analyst, architecture-analyst (opus+ultrathink), refactoring-analyst
**Security/Performance:** security-analyst, performance-analyst
**Testing/Accessibility:** testing-analyst, accessibility-analyst
**Documentation/Data:** documentation-analyst, database-analyst, frontend-analyst

**Pattern**: Conduct comprehensive research → persist detailed findings to `.agent/context/{YYYY-MM-DD}-{topic}-{sessionid}.md` → return concise summary (context elision)

### Agent Coordination

**Main Thread:** Parallelizes Task tools, invokes multiple domain analysts concurrently, runs one slash command at a time

**Slash Commands:** Absorb main thread capabilities (unless restricted), coordinate domain analysts (series/parallel), can daisy-chain ONE other command as final action (no post-processing)

**Domain Analysts:** Must persist findings to `.agent/context/*.md`, cannot invoke other analysts or slash commands reliably

**System:** Changes to CLAUDE.md/commands/agents require Claude Code restart

## 🧠 Model Inheritance

**Default:** `model: inherit` (inherits from main thread)
**Complex reasoning:** `model: opus` + `thinking: ultrathink` (architecture, system design only)

## 📦 File-Persisted Memory

**Required:** All domain analysts persist findings to `.agent/context/{YYYY-MM-DD}-{topic}-{sessionid}.md`

**Naming Pattern**: `{YYYY-MM-DD}-{topic}-{sessionid}.md`

**Example**: `2025-10-05-ui-refactoring-abc123.md`

**Why:** Enables multi-analyst coordination without context pollution

**Session ID**: Agents obtain current session ID via: `python3 ~/.claude/.agents/scripts/session_manager.py current`

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

Use `/workflows:run-comprehensive-review` for multi-perspective reviews with dynamic selection, parallel execution, and unified reporting. 11 atomic review commands available (readability, performance, testing, style, architecture, documentation, observability, security, code, design, synthesize).

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
