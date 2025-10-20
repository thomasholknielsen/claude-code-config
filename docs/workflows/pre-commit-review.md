# Pre-Commit Review Workflow

**Comprehensive code analysis with context-aware analyst selection and intelligent fix planning.**

## What It Does

The `/git:pre-commit-review` command analyzes code across multiple quality domains with three scope options:

- **Core 8 Analysts**: Security, performance, quality, architecture, refactoring, documentation, accessibility, UI/UX
- **Conditional Testing**: Added only if your project has test infrastructure
- **File-Type Specialists**: Added based on changed file types (Python, TypeScript, React, etc.)
- **Three Analysis Scopes**: Uncommitted changes (default), full repository, or specific folder
- **Logical Fix Plan**: Generated with dependency-aware execution sequence and effort estimates

Total: **8-20 analysts** depending on scope and project

## Quick Start (3 Modes)

### Mode 1: Uncommitted Changes (Default)

```bash
/git:pre-commit-review
```

Analyzes git diff (staged + unstaged) - ~45-60 seconds

### Mode 2: Full Repository Audit

```bash
/git:pre-commit-review --scope=repo
```

Analyzes all tracked files - ~60-120 seconds

### Mode 3: Specific Folder

```bash
/git:pre-commit-review --scope=folder --path=src/components
```

Analyzes only specified directory - ~30-45 seconds

## Workflow Example

### 1. Run Review

```bash
$ /git:pre-commit-review

Comprehensive Pre-Commit Review Complete

Scope: uncommitted
Analysts Run: 12 (8 core + 1 conditional + 3 file-type)
Analysis Time: 52 seconds

═══════════════════════════════════════════
ISSUES FOUND: 47
  🔴 Critical:  2
  🟠 High:      8
  🟡 Medium:   15
  ⚪ Low:      22

AUTO-FIX AVAILABLE: 15 issues
  • ESLint (JavaScript): 8 issues
  • Ruff (Python): 4 issues
  • Prettier (formatting): 3 issues

FIX PLAN: .agent/pre-commit-fix-plan.md

═══════════════════════════════════════════

| Option | Action | Impact |
|--------|--------|--------|
| A | Review fix plan | Edit before execution |
| B | Auto-fix all (15) | Run linters, show before/after |
| C | Auto-fix critical (2) | Address blockers only |
| D | Show breakdown | All issues by domain |
| E | Commit anyway | Proceed despite issues |
| Skip | Exit | Review later |

Your choice: _
```

### 2. Review Plan (Option A)

```bash
Fix plan saved to: .agent/pre-commit-fix-plan.md

You can:
- Edit the plan in your editor
- View: cat .agent/pre-commit-fix-plan.md
- Proceed with /git:commit when ready
```

Plan shows three logical phases:

```text
Phase 1: Foundation (2-3h)
  - Fix security issue (blocking)
  - Add type hints (enables refactoring)
  - Fix data loss (critical)

Phase 2: Quality (4-5h)
  - Refactor duplicated code
  - Add docstrings
  - Decompose large class

Phase 3: Polish (3-4h)
  - Minor improvements
  - Documentation updates
  - Style fixes
```

### 3. Execute Action

**Option A**: Edit plan, iterate, then commit

**Option B**: Auto-fix all

```text
Fixed 15 issues ✓
Before: 47 issues
After:  32 issues
Ready to commit? YES
```

**Option C**: Auto-fix critical only

```text
Fixed 2 blocking issues
Before: 47 issues
After:  45 issues
Review remaining issues first
```

**Option D**: See detailed breakdown by domain

**Option E**: Proceed to commit

## Common Patterns

### Pattern 1: Quick Fix & Commit

```bash
/git:pre-commit-review  # Option B: auto-fix all
git commit -m "feat: add new feature"
```

### Pattern 2: Plan-Driven Refactoring

```bash
/git:pre-commit-review  # Option A: review plan
# Edit .agent/pre-commit-fix-plan.md to prioritize
# Execute fixes phase-by-phase over multiple commits
```

### Pattern 3: Full Audit

```bash
/git:pre-commit-review --scope=repo
# Review comprehensive fix plan
# Schedule work across team
```

### Pattern 4: Focused Component

```bash
/git:pre-commit-review --scope=folder --path=src/components
# Isolated analysis and fix plan
```

## Analysis Scopes

### Uncommitted (Default)

- **Analyzes**: Staged + unstaged changes (git diff)
- **Use case**: Before committing code
- **Time**: 45-60 seconds
- **Analysts**: 8-12

### Full Repository

- **Analyzes**: All tracked files in repository
- **Use case**: Periodic audit, pre-release review, onboarding
- **Time**: 60-120 seconds
- **Analysts**: 12-18

### Specific Folder

- **Analyzes**: Only specified directory
- **Use case**: Component review, module focus
- **Time**: 30-45 seconds
- **Analysts**: 8-15

## Smart Analyst Selection

### Core 8 (Always)

1. security-analyst
2. performance-analyst
3. code-quality-analyst
4. architecture-analyst
5. refactoring-analyst
6. docs-analyst
7. frontend-accessibility-analyst
8. ui-ux-analyst

### Conditional (Testing Only)

- testing-analyst (if test config exists)

### File-Type Specialists

- Python → code-python-analyst
- TypeScript → code-typescript-analyst
- JavaScript → code-javascript-analyst
- React → frontend-react-analyst
- Next.js → frontend-nextjs-analyst
- GraphQL → api-graphql-analyst
- REST APIs → api-rest-analyst
- Database → database-sql-analyst
- Terraform → infrastructure-terraform-analyst
- Docker/K8s → infrastructure-devops-analyst
- C# → code-csharp-analyst
- Swift → mobile-ios-swift-analyst
- CLI Tools → ui-ux-cli-analyst

## Fix Plan Format

Always saved to `.agent/pre-commit-fix-plan.md`:

- **Phase 1 (Foundation)**: Blockers, security, type system
- **Phase 2 (Quality)**: Performance, refactoring, maintainability
- **Phase 3 (Polish)**: Docs, style, minor improvements

Each phase includes:

- Logical execution sequence
- File:line references
- Effort estimates
- Dependency notes

Example structure:

```markdown
## Phase 1: Foundation (P0 - 2-3h)

- [ ] Fix O(n²) loop - 45 min
      → Blocks performance improvements
- [ ] Add type hints - 1h
      → Enables IDE support for refactoring
- [ ] Fix data loss risk - 30 min
      → Critical for data integrity

## Phase 2: Quality (P1 - 4-5h)
Depends on: Phase 1 complete

[continues...]
```

## Issue Severity

| Level | Meaning | Action |
|-------|---------|--------|
| 🔴 Critical | Blockers, security | Fix before commit |
| 🟠 High | Quality issues | Strongly recommended |
| 🟡 Medium | Improvements | Address soon |
| ⚪ Low | Polish | Nice to have |

## Parameters

```bash
--scope=uncommitted|repo|folder  # Default: uncommitted
--path=<directory>               # For folder scope (e.g., src/components)
--staged-only                     # Only staged files (uncommitted only)
--unstaged-only                   # Only unstaged files (uncommitted only)
--domains=security,performance   # Filter to specific domains
--timeout=600                     # Analysis timeout in seconds
```

## Troubleshooting

### "No uncommitted changes found"

Make changes first: `git add file.ts`

### "Not a git repository"

Run from inside a git project: `cd my-project`

### Analyst unavailable

Shows warning, continues with available analysts

### Takes too long

Large changesets may take longer - all analysts run in parallel

### Fix application fails

Shows which fixes failed - manual review needed

## Next Steps

After review:

1. Review plan in `.agent/pre-commit-fix-plan.md`
2. Choose action: iterate, auto-fix, or commit
3. If auto-fixing: follow with `/git:commit`
4. If iterating: execute phase-by-phase

Before pushing:

- Security issues require manual review
- Test gaps need coverage
- Documentation gaps need updates
- Architectural decisions need discussion

## Performance

- **20-50 files**: 45-60s (10-12 analysts)
- **50-100 files**: 60-90s (12-15 analysts)
- **100+ files**: 90-120s (15-18 analysts)
- **Full repo**: 60-120s (depending on size)

All analysts run **in parallel**.

## See Also

- `/git:commit` - Create conventional commits
- `/git:push` - Push with safety checks
- `/git-flow:*` - Git Flow commands
