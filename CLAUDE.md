# Claude Code Configuration - Command System Project

**Scope**: Project-specific configuration for Claude Code command system

## Core Components

- **Domain Analysts**: Specialized agents for research, framework expertise, quality, security, performance
- **Slash Commands**: Atomic commands and workflows (git, docs, workflows categories)
- **Hooks**: Python automation for logging, notifications, context management
- **MCP Integration**: External tools (Context7, Playwright, Shadcn)

## System Topology

**Execution Hierarchy**:

```text
User Request
    ↓
Main Thread (parallelizes Task tools, runs slash commands sequentially)
    ├─→ Domain Analysts (parallel research, persist to .agent/context/)
    ├─→ Slash Commands (orchestrate workflows, delegate to analysts)
    └─→ Direct Operations (file ops, bash commands, git via /git:*)
```

**Component Relationships**:

- **Main Thread** → **Domain Analysts**: Spawns parallel analysis tasks, reads context files
- **Slash Commands** → **Domain Analysts**: Delegates specialized analysis (series/parallel)
- **Domain Analysts** → **Context Files**: Persists findings to `.agent/context/{session-id}/{agent-name}.md`
- **All Components** → **MCP Servers**: Access external tools (Context7, Playwright, Terraform, etc.)
- **Git Operations**: Exclusively handled by `/git:*` and `/git-flow:*` commands

**Data Flow**:

1. User request → Main Thread analyzes → Spawns domain analysts (parallel)
2. Analysts research → Persist to context files → Return concise summary
3. Main Thread reads context → Implements recommendations → Updates context logs
4. Slash commands orchestrate → Delegate to analysts → Execute final actions

## Component Interaction Patterns

### Agent Coordination Pattern

**Parallel Research**: Main thread spawns multiple domain analysts concurrently, each analyzing different aspects (security + performance + quality). Analysts work in isolated contexts, cannot parallelize internally.

**Context Persistence**: Every analyst MUST persist findings to `.agent/context/{session-id}/{agent-name}.md` (lean, actionable format). Incremental updates use strikethrough for obsolete items, increment iteration count.

**Context Elision**: Analysts return concise summaries with task counts to main thread, keeping main context clean. Full analysis details remain in context files.

### MCP Server Integration Pattern

**Tool Access**: All components can invoke MCP tools (Context7 for docs, Playwright for browser automation, Terraform for IaC). Commands delegate to analysts for complex MCP operations.

**Data Retrieval**: Context7 resolves library IDs → fetches docs. Playwright navigates → takes snapshots → evaluates. Terraform searches providers/modules → retrieves specs.

### Session Lifecycle Pattern

**Initialization**: `python ~/.claude/scripts/session/session_manager.py start <name> [topic]` → Creates session with name → Establishes context directory

**Execution**: Domain analysts invoked → Create/update context files → Return summaries → Main thread implements → Updates "Main Thread Log"

**Completion**: Context files preserve full analysis history, session metadata tracks agents invoked and overall summary

### Git Operation Pattern

**Strict Delegation**: ALL git operations routed through `/git:*` or `/git-flow:*` commands. No direct git calls from main thread, other commands, or analysts.

**Workflow Detection**: System auto-detects Conventional Commits (single main, type-prefixed branches) vs Git-Flow (main+develop, workflow branches)

## Critical Constraints

**Git Operations**: ONLY `/git/*` and `/git-flow/*` commands perform Git operations
**Cross-Platform**: No hardcoded user paths (use `~/.claude/`)
**Agent Uniqueness**: Each agent has single, unique responsibility
**MCP Integration**: Use Context7/Playwright where appropriate
**Atomic Design**: Keep commands single-purpose
**CLAUDE.md Sync**: Update after creating/modifying/deleting agents or commands

### CLAUDE.md Disambiguation

**Rule**: ALWAYS ask which CLAUDE.md (user `~/CLAUDE.md` vs project `~/.claude/CLAUDE.md`)
**Dual System**: `CLAUDE-GLOBAL.md` (repo) syncs with `~/CLAUDE.md` (installed)
**Update Protocol**: Sync both files when changing global patterns
**Sync Command**: Use `/claude:apply-config-to-user-claude-md` to merge CLAUDE-GLOBAL.md updates into ~/CLAUDE.md with intelligent conflict detection

## Frontmatter Standards

- Frontmatter syntax defined in templates only (single source of truth)
- Commands use `allowed-tools` frontmatter, agents use `tools` frontmatter
- Reference templates: `templates/commands/*.md`, `templates/agents/*.md`
- Do NOT duplicate YAML examples or field syntax in CLAUDE.md

## Domain Analyst Framework

### Domain Analysts

| Domain | Analysts |
|--------|----------|
| **API** | api-rest-analyst, api-graphql-analyst, api-docs-analyst |
| **Database** | database-analyst, database-sql-analyst, database-nosql-analyst, database-architecture-analyst |
| **Frontend** | frontend-analyst, frontend-react-analyst, frontend-nextjs-analyst, frontend-accessibility-analyst, frontend-shadcn-analyst |
| **Code Quality** | code-python-analyst, code-typescript-analyst, code-javascript-analyst, code-csharp-analyst, code-quality-analyst |
| **Infrastructure** | infrastructure-terraform-analyst, infrastructure-cloud-analyst, infrastructure-network-analyst, infrastructure-devops-analyst, infrastructure-monitoring-analyst |
| **Mobile** | mobile-react-native-analyst, mobile-flutter-analyst, mobile-ios-swift-analyst |
| **Research** | research-codebase-analyst, research-web-analyst |
| **Documentation** | docs-analyst (multi-perspective: IA, content quality, user journey, semantic coherence), docs-docusaurus-analyst |
| **UI/UX** | ui-ux-analyst, ui-ux-cli-analyst |
| **Visualization** | mermaid-analyst |
| **Compliance** | compliance-analyst |
| **Standalone** | architecture-analyst, security-analyst, performance-analyst, testing-analyst, refactoring-analyst, debugger-analyst, seo-analyst, product-roadmap-analyst |
| **Engineering** | prompt-analyst |
| **Meta** | agent-expert, command-expert, git-flow-analyst |

**Pattern**: Conduct comprehensive research → persist lean, actionable findings to `.agent/context/{session-id}/{agent-name}.md` → return concise summary with task counts

**Total**: 45 agents (42 domain analysts + 3 meta agents: agent-expert, command-expert, git-flow-analyst)

### Agent Coordination

- **Main Thread**: Parallelizes Task tools, invokes multiple domain analysts concurrently, runs one slash command at a time
- **Slash Commands**: Absorb main thread capabilities (unless restricted), coordinate domain analysts (series/parallel), can daisy-chain ONE other command as final action (no post-processing)
- **Domain Analysts**: Must persist lean, actionable findings using explicit context file path provided in prompts, update incrementally if file exists, cannot invoke other analysts or slash commands reliably
- **System**: Changes to CLAUDE.md/commands/agents require Claude Code restart

**Explicit Path Passing Pattern** (CRITICAL for cross-process session detection):

Agents run in separate Claude processes and **cannot detect sessions via GPPID**. All commands that invoke agents MUST:

1. Get context directory: `CONTEXT_DIR=$(python ~/.claude/scripts/session/session_manager.py context_dir)`
2. Pass explicit path in agent prompt:

```python
Task(
  subagent_type="<agent-name>",
  prompt="<analysis task>

  **Context File Location**: Save your findings to:
  {CONTEXT_DIR}/<agent-name>.md

  Do NOT attempt to detect session - use the path provided above."
)
```

Agents will use the provided path instead of trying to detect sessions themselves. This pattern solves cross-process detection issues and avoids environment variable collisions in multi-terminal scenarios.

## Model Inheritance

**Default**: `model: inherit` (inherits from main thread)
**Complex reasoning**: `model: opus` + `thinking: ultrathink` (architecture, system design only)

## Context Management System

**Directory Structure**: Hierarchical session-based organization

```text
.agent/
├── Session-{YYYY-MM-DD}-{session-id}/    # Active sessions
│   ├── session.md                         # Session metadata
│   ├── context/                           # Session-level analyst context
│   │   ├── architecture-analyst.md
│   │   ├── security-analyst.md
│   │   └── {agent-name}.md
│   └── Task-XXX--{title}/                 # Task-specific subdirectories
│       ├── plan-implementation.md
│       ├── analysis-performance.md
│       └── {agent-name}.md
└── archive/                               # Archived sessions
    └── Session-{YYYY-MM-DD}-{session-id}/
```

**Context File Routing**:

- **Session-level context**: `.agent/Session-{name}/context/{agent-name}.md` (general analysis)
- **Task-level context**: `.agent/Session-{name}/Task-XXX--{title}/{agent-name}.md` (task-specific)

**Required**: All commands invoking agents MUST provide explicit context file paths in prompts (agents cannot detect sessions from separate processes)

**Session Commands**: `python ~/.claude/scripts/session/session_manager.py [current|start <name> [topic]|select <name>|list|context_dir|list_agents|copy_task|set_task|clear_task|setup_task]`

**Session Lifecycle**:

1. **Start**: `/session:start [topic]` → Creates Session-{date}-{id}/ with context/ subdirectory
2. **Work**: Analysts write to context/, tasks create Task-XXX--{title}/ subdirectories
3. **End**: `/session:end` → Interactive cleanup (Delete/Archive/Keep)

**Lean Context Principle**: Context files must be quickly scannable - focus on actionable tasks, not verbose analysis

**Main Thread Responsibility**: After executing agent recommendations, update context file's "Main Thread Log" section with completion status

**Migration**: Use `python ~/.claude/scripts/session/migration_helper.py` to migrate legacy `.agent/context/` files to hierarchical structure

## Parallel Research Pattern

**Workflow**: Parallel research (multiple analysts) → Sequential implementation → Parallel QA

**Performance**: Significantly faster than sequential execution through concurrent analyst invocations

## Command System

**Organization**: Commands organized in `commands/` directory by category (claude, docs, explain, git, git-flow, github, lint, prompt, speckit, system, task, workflows)

**Atomic Design**: Single-purpose, clear responsibility, composable, template-compliant

**Discovery**: Use file explorer or `ls commands/*/` to discover available commands. Each command file contains purpose, usage, and examples.

## MCP Integration

**Configuration**: `~/.claude.json` (per-project user-local)

| Server | Purpose | Type |
|--------|---------|------|
| fetch | Web content fetching | Python/uvx |
| context7 | Library/framework docs | HTTP+API |
| markitdown | Document to Markdown | Docker |
| terraform | Terraform registry/docs | Docker |
| playwright | Browser automation/testing | npm |
| shadcn | shadcn/ui components | HTTP |
| sequential-thinking | Multi-step reasoning | npm |

**Critical Constraint**: Commands delegate to agents for MCP tool usage

**Setup**: See [MCP User Setup](MCP-USER-SETUP.md) and [MCP Configuration Guide](docs/user/mcp-configuration-guide.md)

## Cross-Platform

All automation uses Python with `pathlib.Path` for Windows/macOS/Linux compatibility. Use `Path.home()` for user directories.

### Python Execution Standards

**Critical**: Use `python` instead of `python3` in all cross-platform examples and documentation:

- **Windows**: Uses `python` command (not `python3`)
- **macOS/Linux**: Both `python` and `python3` typically work, but `python` is preferred for consistency
- **Documentation/Examples**: ALWAYS use `python` for cross-platform compatibility
- **Shebang lines**: Use `#!/usr/bin/env python` for maximum portability

**Examples**:

```bash
# Correct (cross-platform)
python ~/.claude/scripts/session/session_manager.py start feature-auth "Authentication implementation"
python scripts/validate_commands.py --help

# Incorrect (Windows incompatible)
python3 ~/.claude/scripts/session/session_manager.py start feature-auth "Authentication implementation"
python3 scripts/validate_commands.py --help
```

**When platform-specific dispatch is needed**: Use conditional logic in code:

```python
import subprocess
import platform

cmd = ['python', 'script.py']  # Use 'python' as base
if platform.system() == 'Windows':
    # Windows-specific adjustments if needed
    pass
else:
    # Unix-specific adjustments if needed
    pass

result = subprocess.run(cmd, capture_output=True, text=True)
```

## Hooks & Infrastructure

**Statusline**: Real-time context monitoring, session metrics, color-coded alerts (`scripts/statusline/status-line.py`)

**Hooks** (configured in `settings.json`):

- `init-session.py` - SessionStart: Initializes session context and logging
- `log-prompt.py` - UserPromptSubmit: Logs user prompts to session log file
- `notify.py` - Stop: Sends notifications when operations complete
- `validate-branch-name.py` - PreToolUse (git checkout): Enforces Git-Flow branch naming conventions
- `prevent-direct-push.py` - PreToolUse (git push): Prevents direct pushes to protected branches
- `update-search-year.py` - PreToolUse (WebSearch): Updates search queries with current year

**Integration**: Git-Flow hooks reference `/git-flow:*` commands for guidance

## Security & Git Constraints

**Git Workflows**: Conventional Commits (single main, type-prefixed branches) or Git-Flow (main+develop, workflow branches) with auto-detection

**Git Conventions**: Conventional commit format with auto-detected types (feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert)

**Permissions**: Context7/Playwright allowed. Block secrets (.env, *.key, credentials). Restrict dangerous operations (rm -rf, sudo)

## Documentation

Docs in `docs/` following Diátaxis framework (tutorials, guides, reference, explanation).

### Documentation Workflow

**Command**: `/workflows:docs [--scope=changes|project]`

**Multi-Perspective Analysis Pattern**: Single enhanced docs-analyst invoked 4 times in parallel with different objectives to analyze documentation from multiple perspectives simultaneously:

1. **Information Architecture** - Structure, navigation, taxonomy, findability
2. **Content Quality & Reality Alignment** - Cross-reference with codebase, validate entity references, detect mismatches
3. **User Journey Validation** - Test onboarding paths, validate tutorials, check learning progression
4. **Semantic Coherence** - Terminology consistency, conceptual model accuracy, mental model clarity

Plus architecture-analyst (technical accuracy) and code-quality-analyst (code examples) = 6 concurrent analyses.

**Scope Modes**:

- `--scope=changes` (default) - Analyze docs related to uncommitted git changes (fast, 30-60s, iterative)
- `--scope=project` - Analyze all documentation (comprehensive, 4-6min, audit)

**Categorization**: Findings grouped as FUNDAMENTAL (reality mismatches), STRUCTURAL (architecture/IA), SURFACE (polish).

**Benefits**: Catches fundamental issues (non-existent entity references, conceptual conflicts, broken onboarding paths) that traditional completeness checks miss.

## Development Standards

### Markdown Linting

Follow `.markdownlint.yml`: 150-char lines (code: 200), ATX headers with blank lines, fenced code with language tags, asterisk emphasis, 2-space lists, inline HTML allowed. Exceptions in `.markdownlintignore`.

### Command Development

**Template**: `templates/commands/command.md` (unified template for all commands - atomic and workflow)

**EXECUTE THIS NOW Pattern**: Commands MUST include explicit "EXECUTE THIS NOW" sections after "EXECUTION INSTRUCTIONS" to prevent silent failures. This section tells Claude to actually invoke tools instead of just describing the workflow.

**When to use "EXECUTE THIS NOW"**:

- ✅ Workflow commands orchestrating multiple tools (workflows/*, pre-commit-review)
- ✅ Commands with bash scripts to execute (/workflows:git, git commands)
- ✅ Commands that historically had silent failures (/task:archive, /workflows:*)
- ✅ Commands delegating to external tools (gh CLI, git, ruff, etc.)
- ✅ Commands launching parallel analysts (Task tool invocations)

**Pattern Structure**:

```markdown
## EXECUTE THIS NOW

**You MUST execute this [workflow] immediately using the [Tool] tool:**

1. [Explicit action with specific tool command]
2. [Explicit action with specific tool command]
...

Do NOT just describe what should happen - actively execute [NOW/immediately] using the [Tool].
```

**Requirements**: Single-purpose, clear responsibility, composable design

**Interactive Pattern** (MANDATORY):

All commands must implement the interactive pattern for consistent UX:

1. **User Feedback Table** (when command has multiple execution paths):
   - Present options as A/B/C table
   - Exactly ONE option marked as "← Recommended" (bold with explanation)
   - Include "Other" for custom input
   - Include "Skip" for optional decisions
   - Max 4 lettered options (A/B/C plus Other)

2. **Next Steps Table** (ALWAYS required):
   - 2-4 specific actionable next steps
   - Include exact commands, not vague descriptions
   - Mark ONE option as recommended for typical workflow
   - Always close with: "What would you like to do next?"

3. **Quality Gate**:
   - User Feedback table (if present): Exactly ONE "Recommended"
   - Next Steps table: Always present with specific commands
   - Pattern must be scannable in <5 seconds

**References**:
- Full guide: `specs/002-consolidate-command-templates/INTERACTIVE_PATTERN_GUIDE.md`
- Examples: `/docs:sync.md`, `/git:complete.md`
- Developer guide: `docs/developer/command-integration-guide.md`

**Creating Commands**: Use template from `templates/commands/*.md`, place in `commands/{category}/{name}.md`, implement interactive pattern (User Feedback + Next Steps), include MCP tools if relevant, ensure atomic design, add "EXECUTE THIS NOW" section after EXECUTION INSTRUCTIONS. Update CLAUDE.md after changes.

### Agent Development

**Requirements**: Single responsibility, no overlap, domain-analyst pattern, model: inherit (default) or opus (complex reasoning), SlashCommand delegation

**Focus**: Advisory role (analyze and recommend, not execute)

### Spec-Kit Integration

When `.specify/` exists: reference `spec.md` (requirements), `plan.md` (architecture), `tasks.md` (completion), `contracts/` (API compliance)

**Cross-Repository Paths**: `~/.claude/.specify/scripts/` and `~/.claude/.specify/templates/`

## Task Management System

**Architecture**: Unified task management via `/task:*` commands with origin tagging (adhoc, code-comment, github-issue)

**Storage**: Tasks stored in `{project_root}/.agent/tasks.md` (active) and `tasks-archive.md` (completed)

**GitHub Integration**: Bidirectional sync with GitHub issues via `/github:*` commands for team collaboration
