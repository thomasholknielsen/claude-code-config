---
description: "Intelligent task triaging and execution with seamless speckit integration"
argument-hint: "[TASK-XXX ...] [--status=state] [--notes=\"text\"] [--complete]"
allowed-tools: Read, Edit, SlashCommand(/speckit:specify), SlashCommand(/development:small), mcp__sequential-thinking__sequentialthinking
---

# Command: Task Execute

## EXECUTION FLOW (START HERE)

### Step 1: Determine Mode

**IF no arguments** → Execute **Interactive Mode** (skip Direct Mode)
**IF task-related arguments provided** → Execute **Direct Mode** (skip Interactive Mode)

---

## INTERACTIVE MODE (No Arguments)

**Execute these steps in order:**

1. Read `.agent/tasks.md` - get all pending/blocked tasks
2. Analyze patterns: priority (critical/high/medium/low), origin (github-issue/code-comment/adhoc), category (bug/feature/refactor/docs/test)
3. Detect groupings: same module, related features, GitHub milestone, code comment clusters
4. Ask 0-3 contextual questions based on task diversity
5. Present selected task(s) with grouping rationale
6. Offer implementation path:
   - A) Create specification (`/speckit:specify`) - RECOMMENDED for complex tasks
   - B) Start implementation (`/development:small`) - for clear requirements
   - C) Mark in-progress manually - for exploratory work
   - D) Show different tasks

---

## DIRECT MODE (With Arguments)

**Execute these steps in order:**

### STEP 1: Validate or Create Session

**YOU MUST validate session exists. If not, create one.**

```bash
SESSION=$(python3 ~/.claude/scripts/session/session_manager.py current)
```

**IF SESSION is empty (no active session)**:

Present options in A/B/C table:

```
No active session for current terminal. Would you like to:

| Option | Description | Impact |
|--------|-------------|--------|
| A | Auto-create adhoc session from task ID | ~3s, creates registry file |
| B | Create named session with custom name | ~5s, prompts for name |
| C | Exit and run /session:start manually | 0s, requires manual session setup |
| Skip | Cancel task execution | 0s, no changes |

Your choice: _
```

- **If A selected**: Extract first task ID from arguments, create session: `/session:start "task-{id}" "{task-description}"`. Display: `✓ Created session: Session-task-029-fix-auth`
- **If B selected**: Prompt user for session name, create session with optional topic
- **If C selected**: Exit command with message: "Run `/session:start <name> [topic]` to create session"
- **If Skip selected**: Exit command

**IF SESSION exists**:

Display: `✓ Session active: {SESSION}`

Continue to STEP 2

### STEP 2: Smart Task Resolution Gate

For each argument (excluding `--status`, `--notes`, `--complete`):

**A. Format Check (lazy evaluation)**:

**Check format**: Does it match `TASK-\d{3}` (e.g., TASK-001)?

**IF VALID task ID**:
- Validate task exists in `.agent/tasks.md`
- Continue to STEP 3
- **Skip all search logic** (performance optimization)

**IF INVALID (freeform text)**:
- Continue to STEP 2a (pre-flight validation)

### STEP 2a: Pre-flight Validation

**Before searching, validate tasks.md**:

1. Check `.agent/tasks.md` exists
2. Check file is readable
3. Check file is not empty (>0 tasks)
4. Validate basic markdown structure

**IF validation fails**:
```
Error: Cannot read tasks.md

| Option | Action |
|--------|--------|
| A | Create first task (/task:add) |
| B | Check file permissions |
| Skip | Exit |
```

**IF validation passes**:
- Continue to STEP 2b (search)

### STEP 2b: Smart Task Search

1. Read `.agent/tasks.md` - all pending/in-progress/blocked tasks
2. Search for matches: title, description, category, priority
3. Rank by relevance:
   - Exact phrase match: 100 points
   - All words match: 80 points
   - Most words match (>50%): 60 points
   - Any word match: 40 points
   - Priority boost: +5 (critical/high), +2 (medium)
4. Limit to top 5 results (most relevant first)

### STEP 2c: Enhanced Selection Gate

Display results with visual status indicators:

```
Searching for tasks matching: "<query>"

Showing 5 of 18 matches:

| Option | Status | Priority | Task Description |
|--------|--------|----------|------------------|
| A | [ACTIVE] | [!] | Fix authentication bug causing login failures (GH-123) |
| B | [ACTIVE] | [*] | Implement rate limiting for API endpoints (CODE) |
| C | [DONE] | - | Review authentication code (completed 2025-10-16) |

| Action | Description |
|--------|-------------|
| Show more | Display more matches (13 additional) |
| Search again | Try different search terms |
| Create new | Create new task (/task:add) |
| Show all | See all pending tasks (interactive) |
| Skip | Exit without executing |

Your choice: _
```

**Status Indicators**:
- `[ACTIVE]` = pending/in-progress/blocked
- `[DONE]` = completed (only shown if in default results or "Show all")
- `[NEW]` = recently created

**Priority Indicators**:
- `[!]` = critical or high priority
- `[*]` = medium priority
- `-` = low or normal priority

**Handle selection**:

**IF task selected (A-Z)**:
- **IF pending/in-progress/blocked** → Continue to STEP 3
- **IF completed**:
  ```
  Task TASK-029 is marked complete (2025-10-16).

  | Option | Action |
  |--------|--------|
  | A | Re-run with fresh analysis (full workflow) |
  | B | View previous results only |
  | Skip | Return to task selection |
  ```
  - **If A**: Change status to "pending", proceed to STEP 3 (full STEP 1-7 workflow)
  - **If B**: Display previous results, exit
  - **If Skip**: Return to selection gate

**IF "Show more"**:
- Extend results to next 5-10 matches
- Re-display gate with expanded list
- Pagination support (max 26 tasks per page, A-Z)

**IF "Search again"**:
- Prompt: "Enter new search query: _"
- Return to STEP 2b with new query

**IF "Create new"**:
- Suggest: `/task:add "<current-query>"`
- Exit command

**IF "Show all"**:
- Execute Interactive Mode (show all pending tasks with grouping)

**IF "Skip"**:
- Exit command

**CRITICAL: When Re-Running Completed Tasks**

**YOU MUST execute the full flow, not create ad-hoc analysis.**

When user selects to re-run a completed task:
1. **DO NOT** manually invoke agents
2. **DO NOT** create a fresh "analysis session"
3. **YOU MUST** go through STEP 1 (validate/create session)
4. **YOU MUST** go through STEP 3 (load task)
5. **YOU MUST** go through STEP 4 (setup task directories with setup_task)
6. **YOU MUST** go through STEP 4.5 (validate)
7. **YOU MUST** go through STEP 6 (invoke agents)

This ensures agents save to correct task-specific directory, not session-level context.

### STEP 3: Load and Display Tasks

1. Parse arguments: extract task IDs and options
2. Read `.agent/tasks.md`
3. Find tasks by ID
4. Display full task information

### STEP 4: Create Task Directories

**YOU MUST execute this step. It sets up task directories and context routing.**

For each task ID (process first task in current implementation):

```bash
# Atomic task setup: copy + set + validate in single operation
RESULT=$(python3 ~/.claude/scripts/session/session_manager.py setup_task <TASK-ID> "<full-task-content>")

# Parse JSON result
SESSION=$(echo $RESULT | python3 -c "import sys, json; print(json.load(sys.stdin)['session'])")
TASK_DIR=$(echo $RESULT | python3 -c "import sys, json; print(json.load(sys.stdin)['task_dir'])")
CONTEXT_DIR=$(echo $RESULT | python3 -c "import sys, json; print(json.load(sys.stdin)['context_dir'])")
VALIDATION=$(echo $RESULT | python3 -c "import sys, json; v=json.load(sys.stdin)['validation']; print('PASS' if all(v.values()) else 'FAIL')")
```

Display progress:
- `⏳ Creating task workspace...`
- `✓ Directory created: {TASK_DIR}`
- `✓ Active task set: {TASK_ID}`

**IF VALIDATION fails**:
- Display error: "Task setup validation failed"
- Show diagnostics: task_dir_exists, marker_set, context_valid
- STOP - Do not proceed to STEP 5

### STEP 4.5: MANDATORY VALIDATION GATE

**YOU MUST NOT skip this step. Validation is critical before agent invocation.**

Verify task setup succeeded:

```
✓ Validating task setup...
  ✓ Task directory exists: {TASK_DIR}
  ✓ Active task marker set: .current_task → {TASK_ID}
  ✓ Context routing correct: {CONTEXT_DIR} contains Task-{ID}

✓ Task setup validated - Ready for analysis
```

**IF any validation fails**:
- **DO NOT invoke agents**
- Display clear error message with diagnostics
- Present A/B/C recovery table:
  - A) Retry task setup with fresh session
  - B) View session/task directory structure for debugging
  - C) Exit command
- **STOP execution**

**IF all validations pass**:
- Continue to STEP 5

### STEP 5: Update Task Metadata

1. Auto-set status to `in-progress` if currently `pending` (unless `--status` specified)
2. Add notes if `--notes` provided
3. Update "Last Updated" timestamp
4. Write changes to `tasks.md`

Display progress:
- `⏳ Updating task metadata...`
- `✓ Status: pending → in-progress`

### STEP 5.5: Context Path Preview

**BEFORE invoking agents, show user where files will be saved.**

Display:

```
Agent context files will be saved to:
  📁 {CONTEXT_DIR}

  Where CONTEXT_DIR = .agent/Session-{session}/Task-{id}--{title}/

Files will include:
  - architecture-analyst.md (if invoked)
  - security-analyst.md (if invoked)
  - performance-analyst.md (if invoked)
  - [other agent-name].md files

This creates isolated, task-specific context for all analysis findings.
```

### STEP 6: Invoke Agents (Optional)

**IF task requires analysis**, use Task tool with **explicit context path**:

```
Task(
  subagent_type="<agent-name>",
  prompt="<analysis task>

  **Context File Location**: Save your findings to:
  {CONTEXT_DIR}/<agent-name>.md

  Where CONTEXT_DIR = <absolute-path-from-step-4>

  Do NOT attempt to detect session - use the path provided above."
)
```

### STEP 7: Offer Handover

Present implementation options:
- A) Create specification (`/speckit:specify`) - RECOMMENDED
- B) Start implementation (`/development:small`)
- C) Continue manually

---

## Quick Reference

**Usage**:
```bash
# Interactive mode
/task:execute

# Direct mode (task IDs)
/task:execute TASK-001
/task:execute TASK-001 TASK-002 TASK-003

# Direct mode (search)
/task:execute fix authentication bug

# Status updates
/task:execute TASK-001 --status=blocked --notes="Waiting for API key"
/task:execute TASK-001 --complete --notes="Tests passing, PR created"
```

**Key Features**:
- Smart task search: Use freeform text instead of task IDs
- Intelligent grouping: Detects related tasks automatically
- Session-aware: Requires active named session for context routing
- Seamless handover: Smooth transition to speckit or development workflows

**Integration Points**:
- Follows: `/task:add`, `/task:scan-project`, `/github:convert-issues-to-tasks`
- Followed by: `/speckit:specify`, `/development:small`, `/task:archive`
- Complemented by: `/task:search` (dedicated search without execution)

## Implementation Notes

### CRITICAL: Enforcement Guards

**YOU MUST NOT**:
- Add "run directly without task management" options
- Invoke agents before STEP 4 (task setup)
- Bypass session validation
- Create any options not listed in this specification

**ANY selection that proceeds with a task MUST**:
1. Go through STEP 3 (load task)
2. Go through STEP 4 (atomic task setup)
3. Go through STEP 4.5 (mandatory validation)
4. Then STEP 6 (invoke agents with explicit context paths)

### Performance Optimization

**Lazy Evaluation Pattern** (STEP 2):
- Check format FIRST (is it TASK-XXX?)
- Search ONLY for freeform input
- Result: 100% performance improvement for valid task IDs
- Avoids unnecessary file reads and search operations

### Search Algorithm

**Task Search Utility** (`~/.claude/scripts/task/task_search.py`):
- Extracted for testability
- Reusable by `/task:execute` and `/task:search`
- Supports ranking, filtering, pagination
- Handles edge cases (empty files, corrupted data)
