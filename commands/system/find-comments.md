---
description: "Locate all TODO comments and unfinished work markers in the codebase"
argument-hint: "[arguments]"
allowed-tools: Grep, Read, Write
---

# Command: Find Comments

## Purpose

Locates TODO comments and unfinished work markers throughout the codebase, with optional consolidation to `.agent/tasks.md` for session-based task management.

## Usage

```bash
/system:find-comments $ARGUMENTS
```

**Arguments**:

- `$1` (scope): Search scope (files, directories, or patterns) (optional, default: entire project)
- `$2` (--types): Comment types to find (TODO, FIXME, HACK, NOTE, BUG, OPTIMIZE) (optional, default: all)
- `$3` (--consolidate): Consolidate findings to tasks.md (optional, default: false)
- `$4` (--output): Output format (optional, default: report)
  - `report`: Display findings in console
  - `tasks`: Save to .agent/tasks.md
  - `github`: Prepare for GitHub issue creation
  - `both`: Report + save to tasks.md

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "src/"` - Find comments only in src directory
- `$ARGUMENTS = "--types=TODO,FIXME"` - Find only TODO and FIXME comments
- `$ARGUMENTS = "*.js --consolidate=true"` - Find in JS files and consolidate to tasks.md
- `$ARGUMENTS = "--types=BUG,FIXME --output=github"` - Find bugs and prepare for GitHub
- `$ARGUMENTS = "src/ --output=both"` - Find in src/, display report and save to tasks.md

## Process

1. **Parse Arguments**: Extract search scope and comment types
2. **Search Codebase**: Use Grep to find specified comment types with context
3. **Extract Context**:
   - File path and line number
   - Comment text and description
   - Surrounding code (3 lines before/after)
   - Author from git blame (if available)
4. **Categorize Findings**:
   - By comment type (TODO, FIXME, HACK, NOTE, BUG, OPTIMIZE)
   - By priority (inferred from context)
   - By file/module
5. **Generate Report**: Display findings organized by type and priority
6. **Optional Consolidation**: If `--consolidate=true` or `--output=tasks`:
   - Save findings to `{project_root}/.agent/tasks.md`
   - Format as structured tasks with metadata
   - Link to source file locations
7. **Provide Summary**: Count by type, priority, and file

**⚠️ LOCATION**: Task consolidation saves to `{project_root}/.agent/tasks.md` only.

## Comment Type Mapping

| Comment Type | Inferred Priority | Description |
|-------------|------------------|-------------|
| TODO | Medium | New functionality to implement |
| FIXME | High | Known issues requiring fixes |
| HACK | Medium | Temporary solutions needing cleanup |
| BUG | High | Confirmed bugs in code |
| NOTE | Low | Important information or context |
| OPTIMIZE | Medium | Performance improvements |

## Agent Integration

- **Specialist Options**: quality-analyst can be spawned to analyze comment patterns and prioritize findings

## Examples

### Find All Comments in Source Directory

```bash
/system:find-comments src/

Result:
Found 23 comments in src/

By Type:
- TODO: 12 comments
- FIXME: 5 comments
- HACK: 4 comments
- NOTE: 2 comments

Top Priority:
1. src/auth.ts:45 - [FIXME] Add proper error handling
2. src/api/users.ts:23 - [FIXME] Validate email format
3. src/db/connection.ts:12 - [BUG] Connection pool leak

Run /system:create-github-issue --source=code-comments to create issues
```

### Find and Consolidate to Tasks

```bash
/system:find-comments --types=TODO,FIXME --consolidate=true

Result:
Found 17 TODO/FIXME comments

✓ Consolidated to .agent/tasks.md
✓ Created 17 tasks

Tasks created:
[TASK-012] Fix authentication error handling (src/auth.ts:45)
[TASK-013] Validate email format (src/api/users.ts:23)
[TASK-014] Refactor user service (src/services/user.ts:89)
... (14 more)
```

### Find Bugs and Prepare for GitHub

```bash
/system:find-comments --types=BUG,FIXME --output=github

Result:
Found 8 BUG/FIXME comments

Prepared for GitHub issue creation:
- 3 critical bugs
- 5 high-priority fixes

Next step:
/system:create-github-issue --source=code-comments --comment-types=BUG,FIXME
```

### Find in JavaScript Files with Context

```bash
/system:find-comments "*.js" --output=both

Result:
Found 15 comments in *.js files

✓ Report displayed below
✓ Saved to .agent/tasks.md

Detailed findings:

📝 TODO Comments (8):
─────────────────────────
src/app.js:23
  TODO: Add error boundary for React components
  Context:
    21: function App() {
    22:   return (
    23:     // TODO: Add error boundary for React components
    24:     <div className="app">
    25:       <Router />

src/utils/api.js:45
  TODO: Implement request caching
  Context:
    43: export async function fetchData(url) {
    44:   // TODO: Implement request caching
    45:   const response = await fetch(url);
... (6 more)

🐛 FIXME Comments (5):
─────────────────────────
src/auth.js:67
  FIXME: Handle token expiration properly
  Priority: HIGH
  Author: @username (3 days ago)
... (4 more)

🔧 HACK Comments (2):
─────────────────────────
src/db.js:12
  HACK: Temporary workaround for connection pooling
  Priority: MEDIUM
... (1 more)
```

## Output Formats

### Report Format (Console Display)

Organized by comment type with:

- File location and line number
- Comment text
- Code context
- Priority level
- Author and date (from git blame)

### Tasks Format (.agent/tasks.md)

Structured task entries with:

- Task ID (auto-incremented)
- Status (pending)
- Priority (inferred from comment type)
- Category (mapped from comment type)
- Source location (file:line)
- Description (comment text)
- Code context

### GitHub Format (Preparation)

Groups comments by type with:

- Issue title format
- Issue body with code context
- Suggested labels
- Priority indicators
- Ready for `/system:create-github-issue`

## Integration Points

**Works Well With**:

- `/system:create-github-issue` - Convert found comments to GitHub issues
- `/system:create-task` - Add individual comments as tasks
- `/implement:small` - Implement fixes for found issues
- `/refactor:apply` - Clean up HACK comments

**Typical Workflow**:

```bash
# 1. Find comments in codebase
/system:find-comments src/ --types=TODO,FIXME,HACK

# 2. Consolidate to tasks for session work
/system:find-comments src/ --consolidate=true

# 3. Or convert to GitHub issues for team visibility
/system:create-github-issue --source=code-comments --scope=src/
```

## Output

Provides:

- Total comment count by type
- Detailed findings with context
- Priority assessment
- File/location references
- Optional: Consolidated tasks in .agent/tasks.md
- Recommended next actions

## Best Practices

1. **Run periodically** - Check for accumulated comments during development
2. **Focus by type** - Use `--types` to focus on specific comment types
3. **Consolidate strategically** - Save to tasks.md for session work, GitHub for team work
4. **Review context** - Check surrounding code to understand urgency
5. **Clean up regularly** - Convert comments to tasks/issues, then remove from code
6. **Use with git blame** - Understand when comments were added
7. **Scope appropriately** - Search specific directories to reduce noise

## Comment Discovery vs Task Creation

**Use `/system:find-comments` to**:

- Discover existing comments in codebase
- Get overview of technical debt
- Understand comment distribution
- Prepare for bulk conversion

**Use `/system:create-task` to**:

- Capture new tasks during development
- Add immediate work items
- Create structured tasks manually

**Use together**:

```bash
# Discover existing comments
/system:find-comments --consolidate=true

# Add new tasks as you work
/system:create-task "Refactor authentication module"
```
