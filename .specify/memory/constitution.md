# Claude Code Command System Constitution

<!--
SYNC IMPACT REPORT - Constitution Update
Version: 1.0.0 → 2.0.0 (MAJOR)
Date: 2025-10-14

MODIFIED PRINCIPLES:
- Complete restructure from placeholder template to concrete implementation
- Established 7 core principles from 5 generic placeholders
- Added Command System Architecture section
- Added Security & Quality Standards section
- Expanded governance with specific compliance procedures

ADDED SECTIONS:
- Command System Architecture (command categories, atomic design, git constraints)
- Security & Quality Standards (dependency management, code evidence, quality gates)

REMOVED SECTIONS:
- None (all placeholder sections replaced with concrete content)

TEMPLATES REQUIRING UPDATES:
✅ plan-template.md - Constitution Check section references this file
✅ spec-template.md - Functional requirements align with principles
✅ tasks-template.md - Task organization reflects atomic design and user story independence
✅ constitution.md - This command file (self-referential)

FOLLOW-UP TODOS:
- Monitor template usage for 30 days to verify constitution alignment
- Consider adding explicit examples for constitution violations in plan-template.md
-->

## Core Principles

### I. Agent Specialist Framework

**Every analysis must leverage domain specialists with clear responsibility boundaries.**

- Domain analysts conduct comprehensive research and persist findings to `.agent/Session-{name}/context/{agent-name}.md`
- Analysts return concise summaries with task counts to minimize context pollution
- Main thread coordinates parallel analyst invocation for optimal performance
- No overlapping responsibilities between agents

**Rationale**: Specialists provide deep expertise while preserving context efficiency through the research-persist-summarize pattern.

### II. Atomic Command Design

**Every command must have single purpose, clear responsibility, and composable design.**

- Commands follow template-based development (`templates/commands/*.md`)
- One command = one responsibility (no feature creep)
- Commands can delegate to domain analysts but not perform git operations (except `/git/*` commands)
- Slash commands can daisy-chain ONE other command as final action

**Rationale**: Atomic design enables reliable composition, testing, and maintenance while preventing scope creep.

### III. Git Operation Safety (NON-NEGOTIABLE)

**ONLY `/git/*` and `/git-flow/*` commands can perform Git operations.**

- Main thread NEVER performs direct git operations
- Other commands NEVER perform direct git operations
- All git workflows must delegate to `/git:*` or `/git-flow:*` commands
- Git commands follow Conventional Commits with auto-detected types

**Rationale**: Centralized git operations prevent inconsistent states, ensure validation gates, and maintain audit trails.

### IV. Context Management Discipline

**Every session must maintain structured context with incremental updates.**

- All sessions initialized via `session_manager.py start <name> [topic]`
- Context structure: `.agent/Session-{name}/context/session.md` + `{agent-name}.md`
- Domain analysts MUST persist lean, actionable findings (not verbose analysis)
- Main thread updates context file "Main Thread Log" after implementing recommendations

**Rationale**: Structured context enables session continuity, traceability, and prevents context drift across complex multi-step workflows.

### V. Test-First for Feature Development (CONDITIONAL)

**When tests are requested in feature specs, TDD is mandatory.**

- Tests written FIRST → User approved → Tests FAIL → Then implement
- Red-Green-Refactor cycle strictly enforced when tests included
- Tests are OPTIONAL unless explicitly requested in specifications
- Integration tests required for: new contracts, contract changes, inter-service communication

**Rationale**: TDD ensures requirements clarity and prevents regressions, but remains optional to support rapid prototyping when tests aren't needed.

### VI. User Story Independence

**Every user story must be independently testable and deliverable.**

- User stories prioritized (P1, P2, P3) by importance
- Each story = viable MVP increment that delivers standalone value
- Tasks organized by user story to enable parallel development
- Stories can be developed, tested, deployed, and demonstrated independently

**Rationale**: Independent stories enable incremental delivery, parallel team work, and early validation without waiting for full feature completion.

### VII. Cross-Platform Compatibility

**All automation must work across Windows, macOS, and Linux.**

- Python with `pathlib.Path` for all file operations
- `Path.home()` for user directories (never hardcoded paths)
- No platform-specific shell commands in core workflows
- MCP integration via `~/.claude.json` (cross-platform)

**Rationale**: Cross-platform design ensures broad adoption and prevents vendor lock-in.

## Command System Architecture

**Command Categories**: `/git/*`, `/git-flow/*`, `/workflows/*`, `/speckit/*`, `/docs/*`, `/task/*`, `/github/*`, `/system/*`, `/claude/*`, `/lint/*`, `/explain/*`

**Atomic Design Requirements**:
- Single-purpose commands with clear responsibility
- Template compliance (`templates/commands/command.md` or `command.md`)
- Composable design (can be orchestrated by workflows)
- User input via A/B/C/D table format (max 5 choices, "Skip" always included)

**Git Workflow Constraints**:
- Git-Flow (main+develop) with auto-detection
- Conventional Commits format with type prefixes (feat, fix, docs, etc.)
- Branch name validation via pre-tool-use hooks
- Direct push prevention to main/master

**MCP Integration**:
- 7 servers: Context7 (docs), Playwright (browser), fetch (web), markitdown (conversion), terraform (infra), shadcn (UI), sequential-thinking (reasoning)
- Commands delegate to agents for MCP tool usage (security constraint)
- Configuration in `~/.claude.json` (user-local, per-project)

## Security & Quality Standards

**Dependency Management (NON-NEGOTIABLE)**:
- ALWAYS update package.json/requirements.txt when adding imports
- NEVER add import statements without corresponding dependencies
- Check existing libraries before importing new ones

**Code Evidence Protocol**:
- When asked about implementation, SHOW CODE with `file_path:line_number` references
- Provide specific file paths in all recommendations
- Include line ranges for context

**Quality Gates**:
- Run lint/typecheck commands after changes
- Validate builds pass before completion
- Follow existing patterns and conventions
- Clean up temporary debugging code automatically

**Security Protocols**:
- No API keys/secrets in client-side code
- Proper authentication and input validation required
- Row-level database security for multi-tenant systems
- Block commits of `.env`, `*.key`, `credentials.json`

**Intelligent Logging**:
- Automatically add essential logging to understand core application behavior
- Log key decisions, data transformations, and system state changes
- Use appropriate levels (ERROR/WARN/INFO/DEBUG) with relevant context

## Development Workflow

**Session Workflow**:
1. Initialize: `python ~/.claude/scripts/session/session_manager.py start <name> [topic]`
2. Work: Invoke analysts → Read context → Implement → Update context log
3. Archive: `session_manager.py archive` (optional)

**Parallelization Pattern**:
- Main thread spawns multiple concurrent tasks (Task tool)
- Parallel research → Sequential implementation → Parallel QA
- Sub-agents run sequentially in isolated contexts (cannot parallelize)

**Feature Development**:
1. `/speckit:specify` - Create specification
2. `/speckit:plan` - Generate implementation plan
3. `/speckit:tasks` - Create dependency-ordered tasks
4. `/speckit:implement` - Execute implementation

**Daily Workflow**:
- `/task:execute` → work → complete → `/task:archive`
- `/task:scan-project --consolidate` for tech debt discovery
- `/github:fetch-issues --milestone=X` → convert → work for sprint planning

## Governance

**Constitution Authority**:
- This constitution supersedes all other practices and guidelines
- All commands, agents, and workflows MUST comply with these principles
- Violations require explicit justification in `plan.md` Complexity Tracking table

**Amendment Procedure**:
1. Proposal with rationale and impact analysis
2. Version bump decision (MAJOR/MINOR/PATCH semantic versioning)
3. Update constitution via `/speckit:constitution` command
4. Propagate changes to dependent templates (plan, spec, tasks)
5. Update runtime guidance (README.md, CLAUDE.md)
6. Generate Sync Impact Report (HTML comment at top of file)

**Versioning Policy**:
- **MAJOR**: Backward incompatible governance/principle removals or redefinitions
- **MINOR**: New principle/section added or materially expanded guidance
- **PATCH**: Clarifications, wording, typo fixes, non-semantic refinements

**Compliance Review**:
- All PRs/reviews must verify constitution compliance
- `/speckit:analyze` performs cross-artifact consistency checks
- Complexity violations tracked in plan.md with justifications
- Runtime development guidance references this constitution

**Template Synchronization**:
- Plan template Constitution Check section aligns with principles
- Spec template requirements structure reflects user story independence
- Tasks template organization supports atomic design and parallel execution
- Command templates enforce atomic design and git constraints

**Version**: 2.0.0 | **Ratified**: 2025-10-14 | **Last Amended**: 2025-10-14
