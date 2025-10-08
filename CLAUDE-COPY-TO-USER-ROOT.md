# Claude Code Configuration - Global Patterns

This file contains **project-agnostic** patterns and standards that apply across all development projects.

## 🎯 Core Principles

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

## 🛡️ Security & Quality Standards

### Critical Security Rules (NON-NEGOTIABLE)
**1. Dependency Management:** ALWAYS update package.json/requirements.txt when adding imports. NEVER add import statements without corresponding dependencies.

**2. No Placeholders:** NEVER use "YOUR_API_KEY", "TODO", or dummy data. Use environment variables or config patterns.

**3. Security Implementation:** NEVER put API keys/secrets in client-side code. ALWAYS implement proper authentication, input validation, and row-level database security.

**4. Code Evidence:** When asked about implementation, SHOW CODE EVIDENCE: "Looking at [filename] (lines X-Y): [code snippet]"

**5. Capability Honesty:** NEVER attempt to generate images/audio or fake implementations. State limitations clearly and suggest proper alternatives.

**6. Intelligent Logging:** AUTOMATICALLY add essential logging to understand core application behavior. Log key decisions, data transformations, and system state changes. Use appropriate levels (ERROR/WARN/INFO/DEBUG) with relevant context.

### Quality Enforcement
**Mandatory Pre-Response Checks:**
- Am I only changing what was explicitly requested?
- Are all new imports added to dependency files?
- Are there any placeholder values needing real implementation?
- Is this a question needing an answer, not code changes?
- Am I making assumptions about missing information?
- Are there security vulnerabilities in suggested code?
- Am I claiming capabilities I don't have?
- Can I provide code evidence for implementation claims?

**Emergency Stop Protocol:** If unsure about ANY aspect: STOP → ASK → WAIT → Proceed only when 100% certain.

### Code Quality Standards
- Run lint/typecheck commands after changes
- Follow existing patterns and conventions
- Never add comments unless requested
- Check existing libraries before importing new ones
- Remove unused code when making changes
- Clean up temporary debugging code automatically

## 🛠️ Tool & File Operations

### File Operations
- **Search:** Use Glob for file patterns (`**/*.ts`, `src/**/*.js`), Grep for content (with regex), rg instead of grep
- **Efficient Operations:** Batch file reads in single messages, run bash commands in parallel, combine related tool calls
- **Never Use:** find (use Glob), cat/head/tail (use Read)
- **Complex Searches:** Use Task tool for multi-step searches to reduce context

### Tool Usage Optimization
- **Parallel Execution:** Send multiple tool calls in single messages, run bash commands concurrently, launch multiple agents for independent tasks
- **Context Management:** Use specialized agents proactively, pass full context to agents, prefer Task tool for complex searches
- **Performance Tips:** Front-load context gathering, detect project stack first, cache information mentally, validate assumptions early

## 🔀 Git & Attribution

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

## 🧠 Session & Context Management

### Session Workflow
**Every development session must:**
1. Initialize session: `python3 ~/.claude/.agent/scripts/session_manager.py init [topic]`
2. Get session ID: `python3 ~/.claude/.agent/scripts/session_manager.py current`
3. Get context directory: `python3 ~/.claude/.agent/scripts/session_manager.py context_dir`
4. Context structure: `{project}/.agent/context/{session-id}/{agent-name}.md`
5. Update context files incrementally throughout session (main thread + ALL sub-agents)

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
- Keep context scannable in <30 seconds - focus on actionable tasks, not verbose explanations
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

### Sub-Agent Registry
**When to Consult Each Agent:**
- **python-analyst**: All tasks involving Python code analysis, type hints, or PEP 8 compliance MUST consult this agent
- **typescript-analyst**: All tasks involving TypeScript code, generics, or type safety MUST consult this agent
- **react-analyst**: All tasks involving React components, hooks, or state management MUST consult this agent
- **frontend-analyst**: All tasks involving UI components, bundle optimization, or frontend architecture MUST consult this agent
- **security-analyst**: All tasks involving security vulnerabilities, authentication, or OWASP compliance MUST consult this agent
- **database-analyst**: All tasks involving database schema, queries, or data optimization MUST consult this agent
- **api-analyst**: All tasks involving API design, REST/GraphQL endpoints, or API contracts MUST consult this agent
- **accessibility-analyst**: All tasks involving WCAG compliance, ARIA patterns, or accessible UI MUST consult this agent
- **architecture-analyst**: All tasks involving system design, SOLID principles, or architectural decisions MUST consult this agent
- **quality-analyst**: All tasks involving code quality assessment, complexity analysis, or maintainability MUST consult this agent
- **testing-analyst**: All tasks involving test coverage, test strategies, or quality assurance MUST consult this agent
- **performance-analyst**: All tasks involving performance optimization, bottlenecks, or profiling MUST consult this agent
- **refactoring-analyst**: All tasks involving code refactoring, technical debt, or code smell detection MUST consult this agent
- **documentation-analyst**: All tasks involving documentation creation, API docs, or knowledge gaps MUST consult this agent
- **shadcn-analyst**: All tasks involving shadcn/ui components or UI implementation MUST consult this agent
- **research-analyst**: All tasks requiring multi-domain research or comprehensive analysis MUST consult this agent

## 📚 Universal Documentation Architecture

### Industry-Standard GitHub Repository Structure
**ALWAYS follow this standardized documentation architecture based on open-source best practices:**

#### Root-Level Documentation (GitHub Special Files)
These files are recognized by GitHub and provide special functionality:

**Essential Files:**
- **README.md** - Primary entry point, concise project overview, quick start
- **LICENSE** - Legal license terms (required for open source)
- **CHANGELOG.md** - Version history and release notes
- **CONTRIBUTING.md** - Contribution guidelines (shows in GitHub issue page)
- **SECURITY.md** - Security vulnerability reporting instructions

**Additional Standard Files:**
- **CODE_OF_CONDUCT.md** - Community behavior guidelines
- **AUTHORS** - Legal contributors for copyright purposes
- **CONTRIBUTORS** - Recognition of all contributors
- **ACKNOWLEDGMENTS.md** - Attribution for used libraries/work
- **CODEOWNERS** - GitHub automatic review assignments

#### Hierarchical Documentation in `/docs` Folder
Organized by audience and following Diátaxis framework (tutorials, guides, reference, explanation):

**Hierarchical docs/ Structure (Audience-Based):**
```
docs/
├── user/ (getting-started/, tutorials/, guides/)
├── developer/ (api-reference/, contributing/, architecture/)
├── admin/ (configuration/, deployment/)
└── concepts/ (architecture.md, design-principles.md, glossary.md)
```

**Documentation Rules:**
1. **README.md** = front door with links to docs/
2. **docs/** = comprehensive, hierarchical, audience-organized
3. **Mobile-friendly** GitHub rendering
4. **2-level max depth** to prevent confusion
5. **Underscores** in filenames, **_index.md** in directories
6. **Diátaxis framework** (tutorials, guides, reference, explanation)

### Anti-Drift Principles

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

### Industry Standards
**Always prioritize established patterns:** Language conventions (PEP 8, ESLint), established frameworks over custom solutions, community best practices, semantic versioning, standard security practices, accessibility standards (WCAG), established API patterns (REST, GraphQL), standard deployment and CI/CD patterns.


## 💬 Communication Protocols

### Response Style
- Be concise and direct (1-4 lines unless detail requested)
- Answer questions directly without unnecessary preambles
- Show code/commands without lengthy explanations
- Use `file_path:line_number` format when referencing code locations
- One word answers are best when appropriate (e.g., "Yes", "4", "ls")

### When Uncertain
- State: "I need clarification on [specific point] before proceeding."
- NEVER guess or make assumptions
- Ask specific questions to get needed information

### Error Handling
- ANALYZE actual error messages/responses
- NEVER assume error causes without evidence
- Ask user to share error details if needed
- Provide specific debugging steps

## 🔍 Review & Quality Assurance

**Review Types:** Code (syntax, bugs, performance), Security (OWASP, CVEs, secrets), Design (accessibility, responsiveness)

**Priority Levels:**
- **Critical:** Security vulnerabilities (CVSS 7+), breaking bugs, accessibility violations, exposed credentials
- **High:** Performance problems, missing error handling, design violations, auth flaws
- **Medium:** Code complexity, test coverage gaps, style inconsistencies

**Integration:** Work with existing linters/formatters, respect project configs, generate TodoWrite lists, create fix branches, update docs automatically.

## 🚀 Parallelization

### Core Architecture
**Key Insight**: Only the main Claude Code thread can parallelize. Subagents run sequentially in isolated contexts.

**Optimal Pattern**: Parallel research → Sequential implementation → Parallel QA

### Main Thread Capabilities
- Spawn up to **10 concurrent tasks** using Task tool
- Parallelize independent research, analysis, diagnostics, and reviews
- **Never** parallelize: file editing, dependent tasks, implementation phases, database modifications

### Comprehensive Example
```markdown
# Feature Development: User Authentication

## Research Phase (Parallel - 4 tasks)
Task("Research authentication best practices and security requirements")
Task("Analyze existing auth patterns in codebase")
Task("Investigate performance and scalability implications")
Task("Explore testing strategies and validation approaches")

## Implementation Phase (Sequential)
1. Create auth models based on research
2. Implement JWT service (depends on models)
3. Add middleware integration (depends on service)
4. Test and validate implementation

## Quality Phase (Parallel - 3 tasks)
Task("Perform security vulnerability assessment")
Task("Review code quality and maintainability")
Task("Validate test coverage and edge cases")
```

### Context Management
**Problem**: Verbose research output creates context pollution
**Solution**: Subagents conduct comprehensive research, persist to `.agent/context/`, return focused summaries

Use subagents for extensive research work, keep main thread clean for implementation.

### Best Practices
1. **Default to parallelization** for independent research/analysis
2. **Batch related research** when possible
3. **Respect 10-task limit** (Claude Code maximum)
4. **Separate domains** to avoid overlap
5. **Sequential implementation** one file at a time

**Critical**: Subagents cannot parallelize. Only main thread can use Task tool for parallel execution.

## ⚠️ CLAUDE.md Disambiguation Protocol

**CRITICAL: When working in ANY project with multiple CLAUDE.md files:**

### File Types
- **User/Global CLAUDE.md** (`~/CLAUDE.md`) - Universal patterns for all projects
- **Project CLAUDE.md** (`{project}/.claude/CLAUDE.md`) - Project-specific configuration

### Mandatory Protocol
**ALWAYS ask for clarification:** *"Are you referring to user CLAUDE.md (global) or project CLAUDE.md (project-specific)?"*

**Applies to ALL actions:** Reading, editing, referencing, or suggesting updates to CLAUDE.md files.

### Enforcement Rules
- **NEVER assume** which file is meant
- **NEVER edit** without explicit clarification
- **ALWAYS ask** which file before ANY action
- **NO EXCEPTIONS** - this protocol is universal

These global patterns apply across all projects while allowing project-specific customizations.
