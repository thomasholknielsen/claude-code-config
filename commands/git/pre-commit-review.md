---
description: "Comprehensive pre-commit review across multiple analysis domains"
argument-hint: "[--scope=uncommitted|repo|folder] [--path=<directory>] [--staged-only|--unstaged-only] [--domains=...] [--timeout=300]"
allowed-tools: Task, Bash, Read, Grep
---

# Command: /git:pre-commit-review

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Execute comprehensive multi-domain code review using dynamic analyst selection based on file types.

**YOU MUST:**
1. ✓ Parse scope (uncommitted/repo/folder) and path from $ARGUMENTS
2. ✓ Detect changed files and categorize by type
3. ✓ Dynamically select applicable analysts (8-20 based on files)
4. ✓ Launch analysts in parallel via Task tool
5. ✓ Read all context files and consolidate findings
6. ✓ Generate prioritized fix plan with execution order

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Run all analysts (only applicable ones)
- ✗ Skip fix plan prioritization

---

## EXECUTE THIS NOW

**You MUST execute this command immediately using the Task tool for parallel analysis:**

1. ✓ Parse scope from arguments (default: uncommitted files)
2. ✓ Get current session context: `python ~/.claude/scripts/session/session_manager.py context_dir`
3. ✓ Detect changed files: `git diff HEAD --name-only` or by scope
4. ✓ Categorize files by type and determine applicable analysts
5. ✓ Launch 8-20 analysts in parallel concurrently via Task tool
6. ✓ Each analyst writes findings to `.agent/context/{session-id}/{analyst-name}.md`
7. ✓ Consolidate findings, deduplicate overlaps, prioritize by severity
8. ✓ Generate prioritized fix plan with execution order

Do NOT just describe what should happen - actively execute this parallel code review NOW using the Task tool.

---

## IMPLEMENTATION FLOW

### Step 1: Parse Scope & Path
Extract scope (default: uncommitted) and path

### Step 2: Detect Changed Files
Analyze file types and paths

### Step 3: Select Analysts
Match file types to applicable analysts (8-20 based on context)

### Step 4: Launch Parallel Analysis
Invoke selected analysts concurrently via Task

### Step 5: Consolidate Findings
Read context files, deduplicate, prioritize by impact

### Step 6: Generate Fix Plan
Create logical execution sequence with effort estimates

---

## Purpose

Execute comprehensive analysis of code changes (uncommitted, full repo, or specific folder) across multiple quality domains (security, performance, code quality, architecture, testing, refactoring, documentation, accessibility, UX) with smart analyst selection based on file types and project configuration. Generate prioritized fix plan with logical execution sequence.

## Framework Structure (RISEN Pattern)

**R**ole: Multi-domain code review specialist with expertise across 8+ core domains and 15+ file-type specialists

**I**nstructions: Analyze code changes by: (1) detecting scope and files, (2) selecting relevant analysts (8-20 based on context), (3) spawning in parallel, (4) aggregating findings, (5) generating prioritized fix plan, (6) presenting action options

**S**teps: Follow Process section below with clear execution phases

**E**nd Goal: Deliver comprehensive review with issue counts, logical fix plan, and actionable next steps in 45-90 seconds

**N**arrowing: Support three analysis scopes - uncommitted changes (default), full repository, or specific directory; generate fix plans with logical execution order and effort estimates

## Smart Analyst Selection

### Core 8 Analysts (Always Run)
1. **security-analyst** - Vulnerabilities, auth, secrets, encryption
2. **performance-analyst** - Bottlenecks, optimization, memory leaks
3. **code-quality-analyst** - Complexity, SOLID, code smells
4. **architecture-analyst** - Design patterns, coupling, modularity
5. **refactoring-analyst** - Technical debt, duplication
6. **docs-analyst** - Documentation completeness, accuracy
7. **frontend-accessibility-analyst** - WCAG, a11y compliance
8. **ui-ux-analyst** - User interface, developer experience

### Conditional Testing Analyst
- **testing-analyst**: ONLY if project has test infrastructure
  - Check: `package.json` with test scripts
  - Check: `pytest.ini`, `setup.cfg`, `jest.config.js`, `vitest.config.ts`
  - Check: `phpunit.xml`, `.rspec`, test targets in `Makefile`
  - If none found: Skip testing-analyst (save time)

### File-Type Conditional Analysts

| File Pattern | Analyst | Reason |
|------|------|--------|
| `*.py` | code-python-analyst | PEP 8, Python patterns |
| `*.ts, *.tsx` | code-typescript-analyst | Type safety, TypeScript idioms |
| `*.js, *.jsx` | code-javascript-analyst | ES6+ patterns |
| `*.cs` | code-csharp-analyst | C# patterns, .NET |
| React imports + `*.tsx, *.jsx` | frontend-react-analyst | Hooks, Suspense, React 18+ |
| `app/`, `pages/` dirs | frontend-nextjs-analyst | App Router, Server Components |
| `*.sql`, `migrations/` | database-analyst, database-sql-analyst | Schema, queries |
| `*.tf` | infrastructure-terraform-analyst | IaC, providers |
| `Dockerfile`, `k8s/`, `*.yaml` | infrastructure-devops-analyst | Containers, orchestration |
| `components/`, `ui/` | ui-ux-analyst | Component architecture |
| `*.swift` | mobile-ios-swift-analyst | SwiftUI, UIKit |
| `*.kt` | mobile-react-native-analyst | Kotlin patterns |
| `*.dart` | mobile-flutter-analyst | Flutter, Dart |
| GraphQL schema/resolvers | api-graphql-analyst | Schema design, N+1 |
| REST routes/controllers | api-rest-analyst | Endpoint design |
| CLI tools, terminal UI | ui-ux-cli-analyst | Terminal UX, command patterns |

## Parameter Handling

| Parameter | Default | Behavior |
|-----------|---------|----------|
| `--scope` | uncommitted | Analysis scope: `uncommitted` (git diff), `repo` (all tracked files), or `folder` (specific directory) |
| `--path` | . | Directory path for `--scope=folder` (e.g., `src/components`) |
| `--staged-only` | false | Analyze only staged files (uncommitted scope only) |
| `--unstaged-only` | false | Analyze only unstaged files (uncommitted scope only) |
| `--domains` | auto-detect | Filter to specific domains (comma-separated) |
| `--timeout` | 300s | Max time for analysis |

## Error Handling

| Scenario | Action |
|----------|--------|
| Not a git repo | Stop: "Not a git repository" |
| No uncommitted changes (uncommitted scope) | Stop: "No uncommitted changes found" |
| Invalid parameters | Stop with validation error |
| Analyst unavailable (MCP error) | ⚠️ Warning, continue with available analysts |
| Analyst timeout | Report timeout, continue with others |
| Fix plan generation fails | Show summary anyway, skip plan |

## Process

1. Verify git repository and scope: Execute `git rev-parse --git-dir` to confirm git repository, parse `--scope` parameter (default: uncommitted), IF scope=uncommitted: execute `git status --porcelain` to check for changes and stop if none found, IF scope=repo or folder: skip uncommitted check (analyze all files), display error and stop if not a git repository

2. Detect files based on scope: Parse `--scope` parameter, IF scope=uncommitted: execute `git diff --cached --name-only` for staged files and `git diff --name-only` for unstaged files, handle `--staged-only` and `--unstaged-only` parameters, IF scope=repo: execute `git ls-files` to get all tracked files, IF scope=folder: extract `--path` parameter and execute `git ls-files` filtered to specified path, combine and deduplicate file list for analysis

3. Build analyst list: Start with core 8 analysts (security, performance, code-quality, architecture, refactoring, docs, accessibility, ui-ux), check for test configuration files (package.json test scripts, pytest.ini, jest.config.js, phpunit.xml, .rspec) and add testing-analyst if found, detect file extensions in analyzed files and add file-type specialists (*.py→code-python, *.ts/tsx→code-typescript, *.js/jsx→code-javascript, *.cs→code-csharp, React files→frontend-react, Next.js→frontend-nextjs, *.sql/migrations→database-sql, *.tf→infrastructure-terraform, Docker/k8s→infrastructure-devops, GraphQL→api-graphql, REST→api-rest, *.swift→mobile-ios-swift, *.kt→mobile-react-native, *.dart→mobile-flutter, CLI tools→ui-ux-cli), apply domain filter if `--domains` parameter provided, display analyst selection summary

4. Get session context directory: Execute `python ~/.claude/scripts/session/session_manager.py context_dir` to get session context path, then create pre-commit-review subdirectory: `mkdir -p $CONTEXT_DIR/pre-commit-review`. This ensures analysts save findings to the correct location.

4a. Spawn analysts in parallel: Determine diff command based on scope: IF scope=uncommitted: `git diff HEAD --`, IF scope=repo: `git diff $(git hash-object -t tree /dev/null) HEAD`, IF scope=folder: add path filter to diff command

4b. Invoke each analyst with explicit context file path: For each selected analyst:
- Use Task tool with subagent_type="<analyst-name>"
- Include explicit context file path in prompt using the `$CONTEXT_DIR` value obtained in step 4:
```
Task(
  subagent_type="security-analyst",
  prompt="Analyze the following git diff...

**Context File Location**: Save your findings to:
${CONTEXT_DIR}/pre-commit-review/security-analyst.md

Do NOT attempt to detect session - use the path provided above.
"
)
```
- Request: (1) issues by severity (critical/high/medium/low), (2) file:line references for each issue, (3) fixable issues identifiable by linters (ESLint, Ruff, Prettier), (4) actionable recommendations
- Wait for all analysts to complete with timeout handling per `--timeout` parameter

5. Aggregate results: Collect all analyst responses from context files located at `${CONTEXT_DIR}/pre-commit-review/{analyst-name}.md`, count issues by severity (critical/high/medium/low), identify fixable issues (linters: ESLint, Ruff, Prettier), group by domain, calculate totals and percentages, handle timeouts by continuing with available results and tracking which analysts were skipped

5.5. Generate fix plan (NEW): Create logical 3-phase execution plan based on aggregated issues, Phase 1 (Foundation): security vulnerabilities, critical bugs, data loss risks, type system foundations (~estimate total time), Phase 2 (Quality): performance optimizations, refactoring, code quality improvements (~estimate total time), Phase 3 (Polish): documentation gaps, minor issues, style improvements (~estimate total time), For each phase list issues with file:line references and individual effort estimates, calculate total effort across phases, save plan to file: `.agent/pre-commit-fix-plan.md`, display plan file path and statistics to user

6. Display comprehensive summary: Output scope (uncommitted/repo/folder), analysts run count (N core + X conditional + Y file-type), analysis time, file counts analyzed, total issues by severity (🔴🟠🟡⚪), auto-fix availability with linter names, display fix plan location (.agent/pre-commit-fix-plan.md), display action table with 6 options: (A) Review fix plan at .agent/pre-commit-fix-plan.md, (B) Auto-fix all available issues, (C) Auto-fix critical only, (D) Show detailed breakdown, (E) Commit anyway, (Skip) Exit and review later

7. Execute user's selected action: Prompt for choice (A/B/C/D/E/Skip), execute selected: (A) Display message with plan file path and options ("Edit the plan in your editor", "View the plan: cat .agent/pre-commit-fix-plan.md", "Proceed with /git:commit when ready"), (B) run eslint --fix, ruff check --fix, prettier --write for detected file types, show before/after issue counts and confirmation, (C) run linters on critical files only, show results, (D) display all issues organized by domain with file:line references and descriptions, (E) display commit message with note about running review before push, (Skip) display review later message

## Testing Scenarios

1. ✅ Uncommitted changes (default) - Completes in 45-60s with 10-12 analysts
2. ✅ Full repository audit - Completes in 60-120s with 12-18 analysts
3. ✅ Specific folder analysis - Completes in 30-45s with focused analysts
4. ✅ Python project - Detects .py files, adds code-python-analyst
5. ✅ React project - Detects React, adds frontend-react-analyst
6. ✅ No test config - testing-analyst automatically skipped
7. ✅ Fix plan file saved - Always saves to .agent/pre-commit-fix-plan.md
8. ✅ Large changeset (100+ files) - Completes within timeout with aggregation

## Quality Standards (CARE)

**Target**: 85+ score

- **Completeness**: >95% analysis domain coverage (8-20 analysts)
- **Accuracy**: >90% relevant issue detection
- **Relevance**: >85% actionable findings with fix plans
- **Efficiency**: <90 seconds for typical changesets

## Explicit Constraints

**IN SCOPE**:
- Analysis of three scopes: uncommitted, full repository, specific folder
- Smart analyst selection (8-20 based on context)
- File-type detection for specialized analysts
- Result aggregation and summary
- Logical 3-phase fix plan generation with effort estimates
- Always save fix plan to file
- Interactive user selection for next actions

**OUT OF SCOPE**:
- Session persistence beyond context files
- Git modification beyond running git diff/status/ls-files
- Merge conflict resolution
- Commit creation (use `/git:commit`)
- Push to remote (use `/git:push`)

## Example Usage

**Default (uncommitted changes)**:
```bash
/git:pre-commit-review
→ Analyzes uncommitted changes
→ Generates fix plan with phases
→ Shows options: review plan, auto-fix, commit, etc.
```

**Full repository audit**:
```bash
/git:pre-commit-review --scope=repo
→ Analyzes all tracked files
→ Comprehensive fix plan
→ Full codebase health check
```

**Specific folder**:
```bash
/git:pre-commit-review --scope=folder --path=src/components
→ Analyzes src/components/ only
→ Focused fix plan for component directory
```

**Security-focused full audit**:
```bash
/git:pre-commit-review --scope=repo --domains=security,performance
→ Full-repo security + performance audit only
→ Targeted fix plan
```
