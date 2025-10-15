# Claude Code Configuration - Global Patterns

This file contains **project-agnostic** patterns and standards that apply across all development projects.

## Core Principles

### Fundamental Rules

- **ONLY** modify what is explicitly requested - no unauthorized changes
- **NEVER** use placeholder values - use proper variables or ask for real values
- **ALWAYS** update dependencies when adding imports
- **DISTINGUISH** questions (provide answers) from code requests (make changes)
- **ASK** for clarification when information is missing - never guess
- **PRESERVE** functional requirements - fix technical issues, not requirements
- **PROVIDE** code evidence when asked about implementation status

### Context Awareness & Safety

**Technology Stack Detection:** Always detect project type using Glob/Grep, find configuration files (package.json, requirements.txt, pom.xml, etc.), understand existing patterns, and adapt approach to detected stack. Check for test/lint/build/typecheck patterns and auto-run after changes.

**Safety Protocols:** Create git checkpoints before destructive operations, validate current state, track modifications, provide rollback options, and run build/test validation.

**Quality Gates:** Before operations, verify builds pass, tests pass, linter passes, and no obvious errors exist.

**Execution Pattern:** Analyze → Plan → Execute incrementally → Validate → Report completion

## Security & Quality Standards

### Critical Security Rules (NON-NEGOTIABLE)

**1. Dependency Management:** ALWAYS update package.json/requirements.txt when adding imports. NEVER add import statements without corresponding dependencies.

**2. No Placeholders:** NEVER use "YOUR_API_KEY", "TODO", or dummy data. Use environment variables or config patterns.

**3. Security Implementation:** NEVER put API keys/secrets in client-side code. ALWAYS implement proper authentication, input validation, and row-level database security.

**4. Code Evidence:** When asked about implementation, SHOW CODE EVIDENCE: "Looking at [filename] (lines X-Y): [code snippet]"

**5. Capability Honesty:** NEVER attempt to generate images/audio or fake implementations. State limitations clearly and suggest proper alternatives.

**6. Intelligent Logging:** AUTOMATICALLY add essential logging to understand core application behavior. Log key decisions, data transformations, and system state changes. Use appropriate levels (ERROR/WARN/INFO/DEBUG) with relevant context.

### Quality Enforcement

**Mandatory Pre-Response Checks:**

- Only change what's requested?
- New imports added to dependencies?
- Any placeholder values present?
- Question vs code request distinction?
- Making assumptions about missing info?
- Security vulnerabilities present?
- Claiming unavailable capabilities?
- Can provide code evidence?

**Emergency Stop Protocol:** If unsure: STOP → ASK → WAIT → Proceed only when certain.

### Code Quality Standards

- Run lint/typecheck commands after changes
- Follow existing patterns and conventions
- Never add comments unless requested
- Check existing libraries before importing new ones
- Remove unused code when making changes
- Clean up temporary debugging code automatically

## Tool & File Operations

### File Operations

- **Search:** Use Glob for file patterns, Grep for content (with regex), rg instead of grep
- **Efficient Operations:** Batch file reads, parallel bash commands, combine related tool calls
- **Never Use:** find (use Glob), cat/head/tail (use Read)
- **Complex Searches:** Use Task tool for multi-step searches

### Tool Usage Optimization

- **Parallel Execution:** Send multiple tool calls in single messages, run bash commands concurrently, launch multiple agents for independent tasks
- **Context Management:** Use specialized agents proactively, pass full context to agents, prefer Task tool for complex searches
- **Performance Tips:** Front-load context gathering, detect project stack first, cache information mentally, validate assumptions early

## Git & Attribution

### Attribution Standards

**NEVER add AI attribution to:**

- Commits (no "Co-authored-by" or Claude signatures)
- Pull requests (no "Generated with Claude Code")
- Issues or any git-related content
- Any code or documentation

All work maintains your full ownership and authenticity. Never modify git config or user credentials.

### Git Workflow

**CRITICAL CONSTRAINT**: All git operations MUST be delegated to `/git:*` slash commands. Main thread and other commands NEVER perform direct git operations.

- **ONLY** commit when explicitly requested by user
- Check `git status` before operations
- Run `git diff` to review changes
- Use clear, concise commit messages
- Follow repository's existing commit style
- Follow existing branch naming patterns
- Never push unless explicitly requested

## Session & Context Management

### Session Workflow

**Every development session must:**

1. Initialize session: `python {claude_config}/scripts/session/session_manager.py init [topic]`
2. Get session ID: `python {claude_config}/scripts/session/session_manager.py current`
3. Get context directory: `python {claude_config}/scripts/session/session_manager.py context_dir`
4. Context structure: `{project}/.agent/context/{session-id}/{agent-name}.md`
5. Update context files incrementally throughout session (main thread + ALL sub-agents)

**Note:** `{claude_config}` = `~/.claude` (macOS/Linux) or `%USERPROFILE%\.claude` (Windows)

### Sub-Agent Coordination

**CRITICAL CONSTRAINT: Sub-Agents Do NOT Make Changes**

**ALL sub-agents are analysis-only** - they conduct comprehensive research and analysis but **DO NOT implement any changes**. Sub-agents:

- ✅ **DO**: Analyze code, research best practices, identify issues, generate actionable task lists, persist lean findings to `.agent/context/{session-id}/{agent-name}.md` files
- ❌ **DO NOT**: Modify code files, create new files, execute implementations, make any changes to the codebase

**Main Thread Responsibilities:**

- Invoke sub-agents for analysis and recommendations
- **MUST implement** all recommended changes from sub-agent analysis
- Read sub-agent context files before continuing work (`.agent/context/{session-id}/{agent-name}.md`)
- **Update context file Main Thread Log** after completing implementation with what was done, deferred, or modified

**Sub-Agent Requirements (ALL AGENTS MUST):**

- Conduct comprehensive analysis within isolated context
- Check if context file exists: `.agent/context/{session-id}/{agent-name}.md`
- If exists: Read, update incrementally (add new findings, mark obsolete with ~~strikethrough~~, increment iteration)
- If new: Create lean structure with Objective, Analysis, Actionable Tasks (Critical/Important/Enhancements), Main Thread Log
- Keep context quickly scannable - focus on actionable tasks, not verbose explanations
- Return concise summary to main thread with task counts (context elision)
- **NEVER modify code files** - only analyze and recommend

### Context File Structure

**Directory**: `{project}/.agent/context/{session-id}/`
**Files**:

- `session.md` - Session metadata, agents invoked, overall summary
- `{agent-name}.md` - One file per agent (e.g., `python-analyst.md`, `security-analyst.md`)

**Agent Context Format** (Lean & Actionable):

- **Objective**: 1-sentence what was analyzed
- **Analysis**: Concise findings with file:line references
- **Actionable Tasks**: Grouped by priority (Critical/Important/Enhancements) in checkbox format
- **Main Thread Log**: Main thread updates with completion status

## Parallelization

### Core Principles

**Key Insight**: Only main thread can parallelize. Subagents run sequentially in isolated contexts.

**Optimal Pattern**: Parallel research → Sequential implementation → Parallel QA

### Parallelization Rules

- Main thread: Spawn multiple concurrent tasks using Task tool
- Parallelize: Independent research, analysis, diagnostics, reviews
- Never parallelize: File editing, dependent tasks, implementation phases, database modifications

### Context Management Pattern

**Problem**: Verbose research output creates context pollution
**Solution**: Subagents conduct comprehensive research, persist to `.agent/context/`, return focused summaries

Use subagents for extensive research work, keep main thread clean for implementation.

**Critical**: Subagents cannot parallelize. Only main thread can use Task tool for parallel execution.

## Universal Documentation Architecture

### Industry-Standard GitHub Repository Structure

Follow standardized GitHub documentation: Root files (README.md, LICENSE, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md, CODEOWNERS) + `/docs` hierarchy organized by audience (user/, developer/, admin/, concepts/) following Diátaxis framework (tutorials, guides, reference, explanation). README.md = front door, docs/ = comprehensive depth. Mobile-friendly rendering, 2-level max depth, underscores in filenames.

### Anti-Drift Principles

Avoid documentation drift when codebase changes. Prohibited: Hard-coded counts, percentage statistics, performance timings, timeline estimates. Preferred: Structural descriptions, qualitative improvements, priority levels, relative descriptions. Focus on principles over precise metrics.

### Industry Standards

Prioritize established patterns: Language conventions (PEP 8, ESLint), frameworks over custom solutions, community best practices, semantic versioning, security practices, accessibility standards (WCAG), API patterns (REST, GraphQL), CI/CD patterns.

## Communication Protocols

### Response Style

- Be concise and direct
- Answer questions without preambles
- Use `file_path:line_number` for code references

### Interactive User Input (Standard Pattern)

When you need the user to make a choice between multiple options, ALWAYS use the A/B/C/D Markdown table format:

**Standard Format:**

```markdown
## How would you like to proceed?

| Option | Description |
|--------|-------------|
| A | <First option description> |
| B | <Second option description> |
| C | <Third option description> |
| D | <Fourth option (optional)> |
| Skip | Exit without making changes (always include) |

Your choice: _
```

**Guidelines:**

- Maximum 5 options (A-E), keep choices focused and distinct
- Each option must be mutually exclusive (no overlap)
- Always include "Skip" option for exit without changes
- Use descriptive text, not just "Option A"
- Optional: Add "Impact" column showing consequences of each choice
- Validate input (A/B/C/D/Skip, case-insensitive)
- Invalid input: re-prompt once, then default to Skip

**Benefits:**

- Cleaner, more scannable than numbered lists or complex syntax
- Letter-based options intuitive and easy to type
- Table format groups related options visually
- Consistent UX across all interactions
- Easy to compare options side-by-side

**Example with Impact:**

```markdown
| Option | Description | Impact |
|--------|-------------|--------|
| A | Quick fix | 3 changes, ~5 min |
| B | Recommended | 10 changes, ~15 min |
| C | Comprehensive | 20 changes, ~30 min |
| Skip | Exit | No changes |

Your choice: _
```

**When NOT to use:**

- Simple yes/no questions (just ask directly)
- Open-ended input (use "Please provide...")
- Single choice with no alternatives (just proceed)

### When Uncertain

- State: "I need clarification on [specific point] before proceeding."
- NEVER guess or make assumptions
- Ask specific questions to get needed information

### Error Handling

- ANALYZE actual error messages/responses
- NEVER assume error causes without evidence
- Ask user to share error details if needed
- Provide specific debugging steps

## Review & Quality Assurance

**Review Types:** Code (syntax, bugs, performance), Security (OWASP, CVEs, secrets), Design (accessibility, responsiveness)

**Priority Levels:**

- **Critical:** Security vulnerabilities (CVSS 7+), breaking bugs, accessibility violations, exposed credentials
- **High:** Performance problems, missing error handling, design violations, auth flaws
- **Medium:** Code complexity, test coverage gaps, style inconsistencies

**Integration:** Work with existing linters/formatters, respect project configs, generate TodoWrite lists, create fix branches, update docs automatically.
