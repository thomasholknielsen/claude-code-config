---
description: "Find code comments (TODO, FIXME, HACK, BUG) and optionally consolidate to tasks"
argument-hint: "[path] [--types=TODO,FIXME] [--consolidate]"
allowed-tools: Read, Grep, Glob, Write, Edit, mcp__sequential-thinking__sequentialthinking
---

# Command: Task Scan Project

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Scan codebase for TODO/FIXME/HACK/BUG comments and optionally consolidate them into tasks.md.

**YOU MUST:**
1. ✓ Parse path, comment types, and --consolidate flag from $ARGUMENTS
2. ✓ Use Grep to search for code comments (TODO, FIXME, HACK, BUG, NOTE, OPTIMIZE)
3. ✓ Extract file location, line number, comment text, and surrounding code
4. ✓ Infer priority & category from comment type
5. ✓ Display organized findings by type and file
6. ✓ If --consolidate: Convert to tasks with origin=code-comment and add to tasks.md

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Modify code files (only analyze)
- ✗ Skip reporting found comments

---

## IMPLEMENTATION FLOW

### Step 1: Parse Arguments
Extract path (default: current dir), comment types (default: TODO,FIXME,HACK,BUG,NOTE,OPTIMIZE), and --consolidate flag

### Step 2: Search Code Comments
Use Grep to find comment patterns matching specified types

### Step 3: Extract Metadata
For each match: file path, line number, comment type, text, surrounding code context

### Step 4: Infer Metadata
Map comment type to priority and category

### Step 5: Display Findings
Show organized by type and file

### Step 6: Consolidate (if --consolidate)
Create task entries in tasks.md with origin=code-comment

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Discover code comments (TODO, FIXME, HACK, BUG, NOTE, OPTIMIZE) via Grep search with path scoping + type filtering, parse comment context (file:line, text, surrounding code), infer priority/category from comment type (FIXME/BUG→high, TODO→medium, NOTE→low), display organized results by type, optionally consolidate to .agent/tasks.md with origin=code-comment

**P**urpose: Surface hidden technical debt from code comments, enable systematic tracking of informal TODOs, support sprint planning from discovered work, provide code context for implementation, distinguish code-derived tasks via origin tagging, preserve source location for easy navigation

**E**xpectation: Without --consolidate → organized findings list (type/file/line/text) + summary count. With --consolidate → new tasks in .agent/tasks.md (origin=code-comment, file:line metadata, code context snippet, inferred priority/category) + task IDs + confirmation

## Quick Start

```bash
# Scan for TODO/FIXME comments
/task:scan-project

# Scan and consolidate to tasks.md
/task:scan-project --consolidate

# Search specific path
/task:scan-project src/ --types=TODO,FIXME,HACK
```

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% comment detection, Accuracy >90% context extraction, Relevance >85% priority inference, Efficiency <15s typical scan)

## Explicit Constraints

**IN SCOPE**: Code comment discovery (Grep-based search), type filtering (TODO/FIXME/HACK/BUG/NOTE/OPTIMIZE), priority/category inference, context extraction (file:line + surrounding code), optional consolidation to tasks.md with origin=code-comment, path scoping
**OUT OF SCOPE**: Comment modification/deletion (comments stay in code), duplicate detection, comment formatting/linting, multi-language comment syntax beyond standard patterns, GitHub issue creation (use /github:create-issue-from-task after consolidation)

## Purpose

Discovers TODO, FIXME, HACK, BUG, and other code comments in the codebase and optionally consolidates them into the unified task management system with origin tagging.

## Usage

```bash
/task:scan-project $ARGUMENTS
```

**Arguments**:

- `$1` (path): Directory or file path to scan (optional, default: current directory)
- `--types`: Comma-separated comment types to find (optional, default: `TODO,FIXME,HACK,BUG`)
- `--consolidate`: Convert found comments to tasks in `.agent/tasks.md` (optional flag)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - Scan current directory for all comment types, show results only
- `$ARGUMENTS = "src/"` - Scan src/ directory only
- `$ARGUMENTS = "--types=TODO,FIXME"` - Find only TODO and FIXME comments
- `$ARGUMENTS = "src/ --types=TODO,FIXME --consolidate"` - Scan and convert to tasks
- `$ARGUMENTS = "--consolidate"` - Scan entire codebase and convert to tasks

## Process

1. **Parse Arguments**: Extract path, types, and consolidate flag
2. **Default Types**: If not specified, use `TODO,FIXME,HACK,BUG,NOTE,OPTIMIZE`
3. **Search Code Comments**: Use Grep to find comment patterns
4. **Parse Comment Context**: Extract file location, line number, comment text, surrounding code
5. **Infer Priority**: Map comment types to default priorities
6. **Display Results**: Show organized findings by type and file
7. **Consolidate (if --consolidate)**: Convert to tasks with origin `code-comment`
8. **Save to tasks.md (if --consolidate)**: Add tasks with proper metadata
9. **Report Summary**: Show count of findings and actions taken

## Comment Type Mapping

**Priority Inference**:

- **FIXME** → `high` (broken code, bugs)
- **BUG** → `high` (known bugs)
- **HACK** → `high` (technical debt requiring attention)
- **TODO** → `medium` (planned improvements)
- **OPTIMIZE** → `medium` (performance improvements)
- **NOTE** → `low` (informational comments)

**Category Inference**:

- **FIXME** → `bug` (fix broken code)
- **BUG** → `bug` (known bugs)
- **HACK** → `refactor` (technical debt)
- **TODO** → `feature` (new functionality) or `refactor` (improvements)
- **OPTIMIZE** → `refactor` (performance)
- **NOTE** → `docs` (informational)

## Task Format for Code Comments

When consolidating with `--consolidate`, tasks include source location:

```markdown
## [TASK-005] Refactor user authentication (TODO)

**Status**: pending
**Priority**: medium
**Category**: refactor
**Origin**: code-comment
**Source Location**: src/services/auth.ts:45
**Created**: 2025-10-13T14:30:00Z

**Description**:
Extract authentication logic into separate service for better testability.

**Code Context**:
```typescript
// TODO: Refactor - extract auth logic into separate service
export class UserService {
  async login(credentials) {
    // Authentication logic here
  }
}
```

---

```

**Metadata Fields**:

- **Status**: Always `pending` for new tasks
- **Priority**: Inferred from comment type (can be adjusted later)
- **Category**: Inferred from comment type
- **Origin**: Always `code-comment` (distinguishes from adhoc and github-issue)
- **Source Location**: `file:line` for easy navigation
- **Created**: ISO 8601 timestamp (UTC)
- **Code Context**: Surrounding code snippet for reference

## Agent Integration

- **No agents required** - Direct Grep-based search
- **Specialist Options**: code-quality-analyst can help prioritize if many findings

## Examples

### Example 1: Scan Current Directory (Display Only)

```bash
/task:scan
# where $ARGUMENTS = ""

# Expected behavior:
→ Scanning current directory for TODO,FIXME,HACK,BUG,NOTE,OPTIMIZE...
→
→ Found 15 code comments:
→
→ FIXME (3):
→   src/services/user.ts:45 - Fix null pointer exception
→   src/api/auth.ts:89 - Handle timeout properly
→   src/utils/validator.ts:123 - Validation logic broken for edge case
→
→ TODO (8):
→   src/services/auth.ts:34 - Extract to separate service
→   src/components/Profile.tsx:56 - Add loading state
→   ...
→
→ HACK (2):
→   src/database/connection.ts:78 - Temporary fix for connection leak
→   src/api/middleware.ts:91 - Workaround for CORS issue
→
→ BUG (2):
→   src/services/payment.ts:145 - Race condition in checkout
→   src/utils/cache.ts:67 - Cache invalidation not working
→
→ Use --consolidate to convert these to tasks
```

### Example 2: Scan Specific Directory with Types

```bash
/task:scan "src/services/ --types=FIXME,BUG"
# where $ARGUMENTS = "src/services/ --types=FIXME,BUG"

# Expected behavior:
→ Scanning src/services/ for FIXME,BUG...
→
→ Found 5 code comments:
→
→ FIXME (3):
→   src/services/user.ts:45 - Fix null pointer exception
→   src/services/auth.ts:89 - Handle timeout properly
→   src/services/payment.ts:156 - Currency conversion error
→
→ BUG (2):
→   src/services/payment.ts:145 - Race condition in checkout
→   src/services/notification.ts:234 - Email not sending
```

### Example 3: Scan and Consolidate to Tasks

```bash
/task:scan "src/ --types=FIXME,TODO --consolidate"
# where $ARGUMENTS = "src/ --types=FIXME,TODO --consolidate"

# Expected behavior:
→ Scanning src/ for FIXME,TODO...
→ Found 11 code comments
→ Consolidating to .agent/tasks.md with origin=code-comment...
→
→ Created tasks:
→ [TASK-010] Fix null pointer exception (FIXME) - src/services/user.ts:45
→ [TASK-011] Handle timeout properly (FIXME) - src/services/auth.ts:89
→ [TASK-012] Extract to separate service (TODO) - src/services/auth.ts:34
→ [TASK-013] Add loading state (TODO) - src/components/Profile.tsx:56
→ ...
→
→ ✓ 11 tasks added to .agent/tasks.md
→ Use /task:execute to review and work on them
```

### Example 4: Full Codebase Technical Debt Scan

```bash
/task:scan "--types=HACK --consolidate"
# where $ARGUMENTS = "--types=HACK --consolidate"

# Expected behavior:
→ Scanning current directory for HACK...
→ Found 7 code comments
→ Consolidating to .agent/tasks.md with origin=code-comment...
→
→ Created tasks:
→ [TASK-020] Temporary fix for connection leak (HACK) - src/database/connection.ts:78
→ [TASK-021] Workaround for CORS issue (HACK) - src/api/middleware.ts:91
→ ...
→
→ ✓ 7 technical debt items added to .agent/tasks.md
→ Priority: high (HACK comments indicate technical debt)
```

## Integration Points

- **Follows**: Code reviews, refactoring sessions, technical debt audits
- **Followed by**: `/task:execute` (review and work on tasks), `/github:create-issue-from-task`
- **Related**: `/task:add` (adhoc tasks), `/github:convert-issues-to-tasks` (GitHub issues)

## Quality Standards

- **Accurate Search**: Find all comment patterns reliably
- **Context Preservation**: Include surrounding code for clarity
- **Smart Priority**: Infer sensible defaults from comment type
- **Source Tracking**: Always include file:line for navigation
- **No Code Modification**: Comments remain in source files
- **Optional Conversion**: User controls consolidation with flag
- **Origin Tagging**: Always tag as `code-comment`

## Output

**Without --consolidate**:

- Organized list of findings by comment type
- File locations with line numbers
- Comment text preview
- Summary count

**With --consolidate**:

- Updated `.agent/tasks.md` with new tasks
- Task IDs for each converted comment
- Source location preservation
- Confirmation message with count

## Workflow Examples

### Technical Debt Discovery

```bash
# Find all technical debt markers
/task:scan-project --types=TODO,FIXME,HACK

# Review findings, then consolidate
/task:scan-project --types=TODO,FIXME,HACK --consolidate

# Now they're tracked in tasks.md - use execute to triage and work on them
/task:execute
```

### Sprint Planning from Code Comments

```bash
# Find all TODO comments
/task:scan-project --types=TODO --consolidate

# Review and prioritize using interactive triaging
/task:execute

# Update specific task priorities
/task:execute TASK-010 --priority=high

# Create GitHub issues for team
/github:create-issue-from-task TASK-010 TASK-011 TASK-012 --labels=tech-debt
```

### Bug Discovery Workflow

```bash
# Find all bug markers
/task:scan-project --types=FIXME,BUG --consolidate

# Review critical bugs using interactive triaging
/task:execute
# (Answer questions to focus on high priority bugs)

# Start working on specific bug
/task:execute TASK-015
```

## Best Practices

1. **Scan Before Sprint Planning** - Discover technical debt early
2. **Use Specific Paths** - Scan targeted directories for faster results
3. **Filter by Type** - Focus on specific comment types (FIXME for bugs, HACK for debt)
4. **Review Before Consolidate** - Run without `--consolidate` first to review findings
5. **Update Code Comments** - Mark comments as resolved or create task references
6. **Regular Scans** - Run periodically to catch new technical debt
7. **Consolidate Strategically** - Not every TODO needs to be a task immediately

## Code Comment Guidelines

**Good Comments for Scanning**:

```typescript
// TODO: Add validation for email format
// FIXME: Null pointer exception when user is undefined
// HACK: Temporary workaround for API timeout issue
// BUG: Race condition in concurrent requests
// OPTIMIZE: Cache this query result for better performance
```

**Poor Comments** (won't scan well):

```typescript
// todo add validation (inconsistent casing)
// need to fix this (no type marker)
// this is broken (vague, no context)
```

## Comment Type Usage

**Use FIXME for**:

- Broken code that needs fixing
- Known bugs requiring attention
- Code that doesn't work as intended

**Use TODO for**:

- Planned improvements
- Missing features
- Code that works but needs enhancement

**Use HACK for**:

- Temporary workarounds
- Technical debt
- Code that needs refactoring

**Use BUG for**:

- Confirmed bugs
- Reproducible issues
- Known defects

## After Consolidation

**Next Steps**:

1. Review tasks: `/task:execute` (interactive triaging)
2. Update priorities: `/task:execute TASK-XXX --priority=high`
3. Work on tasks: `/task:execute TASK-XXX` (auto-sets to in-progress)
4. Update code: Remove or update comment when fixed
5. Complete task: `/task:execute TASK-XXX --complete`
6. Optional: Create GitHub issues for team visibility

**Comment Management**:

- Keep comments in code until resolved
- Add task reference in comment: `// TODO: Refactor this (TASK-025)`
- Remove comment when task is completed
- Or replace with task/issue reference
