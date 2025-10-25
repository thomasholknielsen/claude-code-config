---
description: "Search tasks by query with intelligent relevance ranking"
argument-hint: "<query> [--completed] [--limit=N]"
allowed-tools: Read, SlashCommand(/task:execute)
---

# Command: Task Search

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Search tasks by query with intelligent relevance ranking and display matching results.

**YOU MUST:**
1. ✓ Parse search query from $ARGUMENTS
2. ✓ Load all tasks from `.agent/tasks.md`
3. ✓ Search titles and descriptions for matches
4. ✓ Rank results by relevance (exact phrase > all words > partial)
5. ✓ Display results in table format (A-Z options)

**YOU MUST NOT:**
- ✗ Do nothing silently if tasks exist
- ✗ Skip ranking by relevance
- ✗ Fail to display results

---

## IMPLEMENTATION FLOW

### Step 1: Validate Search Query
Extract and validate search query from $ARGUMENTS (must be non-empty)

### Step 2: Load Tasks
Read `.agent/tasks.md` and parse all task entries

### Step 3: Search & Rank
Calculate relevance score for each task:
- Exact phrase: 100 pts
- All words match: 80 pts
- Partial match: 60 pts

### Step 4: Display Results
Show top N results (default 5) in table format with A-Z options

---

## Purpose

Dedicated task search command for finding specific tasks by query. Complements `/task:execute` by providing focused search functionality separate from task execution.

## User Feedback

| Option | Action | Details |
|--------|--------|---------|
| A | Default workflow | [RECOMMENDED] |
| B | Alternative approach | For different use case |
| C | Skip | Exit without changes |

Your choice (A/B/C)?

## Next Steps

| Option | Action | Command |
|--------|--------|---------|
| 1 | Review output | Check generated content |
| 2 | Iterate or refine | Run command again [RECOMMENDED] |
| 3 | Continue workflow | Proceed to next step |
| 4 | Get help | Use /claude:guru for guidance |

What would you like to do next?


## Usage

```bash
/task:search <query> [--completed] [--limit=N]
```

## Arguments

- `query` (required): Search query
  - Examples: "authentication", "fix bug", "refactor database"
  - Searches across task titles, descriptions, categories
  - Multi-word queries supported (all words must match for high relevance)

- `--completed` (optional): Include completed tasks in results
  - Default: Show only pending/in-progress/blocked tasks
  - Use when looking for finished work or re-running analysis

- `--limit=N` (optional): Maximum results to show
  - Default: 5 results
  - Range: 1-26 (one per letter A-Z)
  - Use --limit=0 for all matching tasks

## Process

1. **Validate tasks.md exists and is readable**
   - Check file exists at `.agent/tasks.md`
   - Verify file is not empty
   - Confirm valid markdown format

2. **Parse search query**
   - Split into words
   - Search against task titles and descriptions
   - Apply relevance ranking algorithm

3. **Rank by relevance**
   - Exact phrase match: 100 points
   - All words match: 80 points
   - Most words match (>50%): 60 points
   - Any word match: 40 points
   - Match in description: +20 points
   - Priority boost: +5 (critical/high), +2 (medium)

4. **Display results**
   - Show table with task options (A-Z)
   - Include status `[ACTIVE]` or `[DONE]`
   - Show priority `[!]` (critical/high) or `[*]` (medium)
   - Truncate long titles to 60 characters

5. **Handle selection**
   - User selects task by letter (A-Z)
   - Execute selected task: `/task:execute TASK-XXX`
   - Or perform other action

## Display Format

```
Search results for "authentication":

## Showing 3 of 15 matches

| Option | Status | Priority | Task Description |
|--------|--------|----------|------------------|
| A | [ACTIVE] | [!] | Fix authentication bug causing login failures... |
| B | [ACTIVE] | [*] | Implement OAuth 2.0 integration |
| C | [DONE] | - | Review authentication code (completed 2025-10-16) |

Actions:
- A-Z: Execute selected task
- Show more: Display next 5 results
- Different search: Try new query
- Skip: Exit

Your choice: _
```

## Examples

### Example 1: Search active tasks

```bash
/task:search authentication

# Output:
# Showing 5 of 8 matches
#
# | Option | Status | Priority | Task Description |
# |--------|--------|----------|------------------|
# | A | [ACTIVE] | [!] | Fix authentication bug... |
# | B | [ACTIVE] | [*] | Implement rate limiting... |
# ...
```

### Example 2: Search including completed

```bash
/task:search refactor --completed

# Output:
# Showing 5 of 12 matches (including completed)
#
# | Option | Status | Priority | Task Description |
# |--------|--------|----------|------------------|
# | A | [DONE] | [*] | Refactor database schema (completed 2025-10-15) |
# | B | [ACTIVE] | - | Refactor API endpoints... |
# ...
```

### Example 3: Increase result limit

```bash
/task:search "performance optimization" --limit=10

# Output:
# Showing 10 of 18 matches
#
# | Option | Status | Priority | Task Description |
# |--------|--------|----------|------------------|
# (displays A-J options)
```

## Error Handling

**Missing tasks.md**:
```
Error: Tasks file not found at .agent/tasks.md

To create first task: /task:add "Task description"
```

**Empty tasks.md**:
```
Error: No tasks found in .agent/tasks.md

To create first task: /task:add "Task description"
```

**No matches found**:
```
No tasks match your query: "xyz nonexistent"

Options:
- Create new task: /task:add "xyz nonexistent"
- Try different search: /task:search "<new-query>"
- Show all tasks: /task:search "*" --limit=0
```

**Invalid query**:
```
Error: Invalid query format

Usage: /task:search <query> [--completed] [--limit=N]
Examples:
- /task:search authentication
- /task:search "multi word query"
- /task:search refactor --completed
```

## Search Ranking Examples

**Query: "authentication bug"**

| Task | Match Type | Score | Ranked |
|------|-----------|-------|--------|
| "Fix authentication bug in login" | Exact phrase match | 100 | 🥇 #1 |
| "Authentication: implement 2FA" | All words match | 80 | 🥈 #2 |
| "Bug: authentication service timeout" | All words match | 80 | 🥈 #2 |
| "Fix login issues" | Partial match (bug) | 40 | 🥉 #3 |
| "Improve authentication" | Partial match | 40 | 🥉 #3 |

## Integration

- **Precedes**: `/task:execute` when user selects a task to run
- **Complements**: `/task:execute` - separate search vs. execute workflows
- **Alternative to**: Using search within execute (for users who prefer dedicated search)

## Related Commands

- `/task:execute` - Execute task with full workflow (includes search)
- `/task:add` - Create new task
- `/task:archive` - Manage completed tasks

## Performance

- Search performance: <100ms for 100+ tasks
- Result limiting: Shows top N matches by relevance
- Pagination: Manual "Show more" for additional results

## Design Philosophy

Atomic design principle: Single responsibility - search only, don't execute. Users can:
- Search multiple times with different queries
- Compare results across searches
- Then execute via `/task:execute TASK-ID`
