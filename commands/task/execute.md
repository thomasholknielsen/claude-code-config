---
description: "Intelligent task triaging and execution with seamless speckit integration"
argument-hint: "[TASK-XXX ...] [--status=state] [--notes=\"text\"] [--complete]"
allowed-tools: Read, Edit, SlashCommand(/speckit:specify), SlashCommand(/development:small), mcp__sequential-thinking__sequentialthinking
---

# Command: Task Execute

## EXECUTION FLOW (START HERE)

### MANDATORY: Read This BEFORE Proceeding

**This command has EXACTLY TWO workflows:**

1. **Interactive Mode** (no arguments) → Show all tasks, offer grouping
2. **Direct Mode** (with arguments) → STEP 1 (Smart Task Gate) → STEP 2 (Session) → STEP 3-10

**YOU MUST NOT**:
- ✗ Invoke agents directly (bypass STEP 4 task setup)
- ✗ Create "run analysis" options not in specification
- ✗ Skip STEP 1 Smart Task Resolution Gate for freeform input
- ✗ Improvise any workflow not explicitly defined below

**IF user provides freeform text** (not TASK-XXX):
1. Go to STEP 1 (Smart Task Resolution Gate)
2. Search tasks.md for matches
3. Show enhanced selection table
4. Wait for user selection
5. **DO NOT** directly invoke agents or create ad-hoc analysis

**Violating these constraints breaks task-aware context routing.**

---

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

### STEP 1: Smart Task Resolution Gate

For each argument (excluding `--status`, `--notes`, `--complete`):

**A. Format Check (lazy evaluation)**:

**Check format**: Does it match `TASK-\d{3}` (e.g., TASK-001)?

**IF VALID task ID**:
- Validate task exists in `.agent/tasks.md`
- Continue to STEP 2
- **Skip all search logic** (performance optimization)

**IF INVALID (freeform text)**:
- Continue to STEP 1a (pre-flight validation)

### STEP 1a: Pre-flight Validation

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
- Continue to STEP 1b (search)

### STEP 1b: Smart Task Search

1. Read `.agent/tasks.md` - all pending/in-progress/blocked tasks
2. Search for matches: title, description, category, priority
3. Rank by relevance:
   - Exact phrase match: 100 points
   - All words match: 80 points
   - Most words match (>50%): 60 points
   - Any word match: 40 points
   - Priority boost: +5 (critical/high), +2 (medium)
4. Limit to top 5 results (most relevant first)

### STEP 1c: Enhanced Selection Gate

Display results with visual status indicators in **two-table format**:

**Table 1** (task results - NO "Option" column):

```
Searching for tasks matching: "<query>"

Showing 5 of 18 matches:

| Status   | Priority | Task Description                                                |
|----------|----------|-----------------------------------------------------------------|
| [ACTIVE] | [!]      | Fix authentication bug causing login failures (GH-123)          |
| [ACTIVE] | [*]      | Implement rate limiting for API endpoints (CODE)                |
| [DONE]   | -        | Review authentication code (completed 2025-10-16)               |
```

**Table 2** (actions - WITH "Option" column for letter selection):

```
| Option       | Description                       |
|--------------|-----------------------------------|
| A            | Execute first task (start work)   |
| B            | Execute second task (start work)  |
| C            | Execute third task (start work)   |
| Show more    | Display more matches (13 additional) |
| Search again | Try different search terms        |
| Create new   | Create new task (/task:add)       |
| Show all     | See all pending tasks (interactive) |
| Skip         | Exit without executing            |

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
- **IF pending/in-progress/blocked** → Continue to STEP 2
- **IF completed**:
  ```
  Task TASK-029 is marked complete (2025-10-16).

  | Option | Action |
  |--------|--------|
  | A | Re-run with fresh analysis (full workflow) |
  | B | View previous results only |
  | Skip | Return to task selection |
  ```
  - **If A**: Change status to "pending", proceed to STEP 2 (full STEP 1-2 then STEP 3-10 workflow)
  - **If B**: Display previous results, exit
  - **If Skip**: Return to selection gate

**IF "Show more"**:
- Extend results to next 5-10 matches
- Re-display gate with expanded list
- Pagination support (max 26 tasks per page, A-Z)

**IF "Search again"**:
- Prompt: "Enter new search query: _"
- Return to STEP 1b with new query

**IF "Create new"**:
- Suggest: `/task:add "<current-query>"`
- Exit command

**IF "Show all"**:
- Execute Interactive Mode (show all pending tasks with grouping)

**IF "Skip"**:
- Exit command

### Anti-Patterns (DO NOT DO THIS)

❌ **WRONG**: "Perfect. Let me invoke two subagents for analysis..."
✅ **CORRECT**: Show the enhanced selection gate with task options

❌ **WRONG**: Creating off-spec option: "B) Run analysis directly without task management"
✅ **CORRECT**: Only show options from specification (Show more/Search again/Create/Show all/Skip)

❌ **WRONG**: Bypassing search: "I'll just run the analysis in the current session"
✅ **CORRECT**: Execute STEP 1b search, show results, wait for selection

❌ **WRONG**: "I see the input is not a task ID, so I'll search and then directly invoke agents"
✅ **CORRECT**: "I see the input is not a task ID, so I'll show the Smart Task Resolution Gate and wait for user to select a task"

**CRITICAL: When Re-Running Completed Tasks**

**YOU MUST execute the full flow, not create ad-hoc analysis.**

When user selects to re-run a completed task:
1. **DO NOT** manually invoke agents
2. **DO NOT** create a fresh "analysis session"
3. **YOU MUST** go through STEP 2 (validate/create session)
4. **YOU MUST** go through STEP 3 (load task)
5. **YOU MUST** go through STEP 4 (setup task directories with setup_task)
6. **YOU MUST** go through STEP 5 (validate)
7. **YOU MUST** go through STEP 8 (invoke agents)

This ensures agents save to correct task-specific directory, not session-level context.

### STEP 2: Validate or Create Session

**YOU MUST validate session exists. If not, create one.**

```bash
SESSION=$(python3 ~/.claude/scripts/session/session_manager.py current)
```

**IF SESSION is empty (no active session for current terminal)**:

Check for existing active sessions:

```bash
SESSIONS_JSON=$(python3 ~/.claude/scripts/session/session_manager.py list)
SESSION_COUNT=$(echo $SESSIONS_JSON | python3 -c "import sys, json; print(json.load(sys.stdin)['count'])")
```

**IF SESSION_COUNT > 0 (existing sessions found)**:

Display existing sessions in **two-table format** (per user requirement):

**Table 1** (existing sessions list - NO "Option" column):

```
Existing sessions found:

| Session | Topic | Started | Terminals |
|---------|-------|---------|-----------|
| task-029 | analyze meaning of life from coding... | 2025-10-18 19:20 | 1 |
| feature-auth | Authentication implementation | 2025-10-17 14:30 | 2 |
```

**Table 2** (actions - WITH "Option" column for letter selection):

```
| Option | Description |
|--------|-------------|
| A | Link to session task-029 |
| B | Link to session feature-auth |
| C | Create new session |
| Skip | Exit |

Your choice: _
```

**Handle selection**:

- **If A/B/etc selected (link to existing)**: Link to selected session using `python3 ~/.claude/scripts/session/session_manager.py select "<session-name>"`. Display: `✓ Linked to session: <session-name>`
- **If C selected (new session)**: Go to "Create New Session" flow below
- **If Skip selected**: Exit command

**ELIF SESSION_COUNT == 0 (no existing sessions)**:

Present session creation options:

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

**Create New Session Flow** (for both paths):

- **If A selected**: Extract first task ID from arguments, create session using `python3 ~/.claude/scripts/session/session_manager.py start "task-{id}" "{task-description}"`. Display: `✓ Created session: task-029`
- **If B selected**: Prompt user for session name, create session with optional topic
- **If C selected**: Exit command with message: "Run `/session:start <name> [topic]` to create session"
- **If Skip selected**: Exit command

**IF SESSION exists (terminal already linked)**:

Display: `✓ Session active: {SESSION}`

Continue to STEP 3

### STEP 3: Load and Display Tasks

**YOU MUST execute this step to extract full task content for STEP 4.**

For each task ID:

1. **Read `.agent/tasks.md`** and extract the **full markdown section** for the task
2. **Extract task section** from `## [TASK-XXX]` header to next `## [TASK-` or EOF:
   ```bash
   # This captures ALL task content including:
   # - ## [TASK-029] {title}
   # - **Status**: pending
   # - **Priority**: medium
   # - **Description**: ...
   # - **Notes**: ... (if exists)
   ```
3. **Store in variable** `FULL_TASK_CONTENT` for use in STEP 4
4. **Display task summary**:
   ```
   ⏺ Loading TASK-029...

   Task: analyze the meaning of life from coding perspective using 2 subagents
   Status: pending → will be set to in-progress
   Priority: medium
   Category: research
   ```

**CRITICAL**: The `FULL_TASK_CONTENT` variable MUST contain the complete markdown section including the `## [TASK-XXX] {title}` header. This is required for proper title extraction in STEP 4.

### STEP 4: Create Task Directories

**YOU MUST execute this step. It sets up task directories and context routing.**

For each task ID (process first task in current implementation):

```bash
# Atomic task setup: copy + set + validate in single operation
# CRITICAL: Pass FULL_TASK_CONTENT from STEP 3 (not just description)
RESULT=$(python3 ~/.claude/scripts/session/session_manager.py setup_task <TASK-ID> "$FULL_TASK_CONTENT")

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

### STEP 5: MANDATORY VALIDATION GATE

**YOU MUST NOT skip this step. Validation is critical before agent invocation.**

Verify task setup succeeded:

```
✓ Validating task setup...
  ✓ Task directory exists: {TASK_DIR}
  ✓ Active task marker set: session.env:CURRENT_TASK → {TASK_ID}
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
- Continue to STEP 6

### STEP 6: Update Task Metadata (Both Files)

**CRITICAL**: Update both tasks.md AND task.md to keep status synchronized.

1. Auto-set status to `in-progress` if currently `pending` (unless `--status` specified)
2. Add **Details** field pointing to task directory path (if not already present)
3. Add notes if `--notes` provided
4. Update "Last Updated" timestamp
5. **Write changes to tasks.md** (master file in `.agent/tasks.md`)
6. **Sync changes to task.md** (task directory copy in `{TASK_DIR}/task.md`)

**Implementation**:

```python
# Read current tasks.md
tasks_md_content = Path('.agent/tasks.md').read_text()

# Get task directory relative path from STEP 4
# Example: .agent/Session-task-029/Task-029--analyze-the-meaning-of-life-from-coding-perspectiv
task_dir_relative = TASK_DIR.replace(str(Path.cwd()) + '/', '')

# Find task section by ID and update fields
# Update: **Status**: pending → in-progress
# Add/Update: **Details**: {task_dir_relative} (placed after Status field)
# Update: **Last Updated**: {current_timestamp}
# Add: **Notes**: {notes} (if --notes provided)

# Pattern for adding Details field:
# Find line with **Status**:
# Insert **Details**: line immediately after it (if not exists)

# Write to tasks.md
Path('.agent/tasks.md').write_text(updated_content)

# CRITICAL: Sync same changes to task.md in task directory
task_md_path = Path(TASK_DIR) / 'task.md'
task_md_content = task_md_path.read_text()

# Apply same updates to task.md content
# (same status, same Details field, same timestamp, same notes)

# Write to task.md
task_md_path.write_text(updated_task_md_content)
```

Display progress:
- `⏳ Updating task metadata...`
- `✓ Status: pending → in-progress (synced to both files)`
- `✓ Details: {task_dir_relative}`
- `✓ Timestamp updated: {timestamp}`

### STEP 7: Context Path Preview

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

### STEP 8: Invoke Agents (Optional)

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

### STEP 8.5: Synthesize Research Findings to task.md

**CRITICAL**: Execute this step AFTER agents complete to append research synthesis to task.md.

**Purpose**: task.md should contain a synthesized summary of research findings, not just the task definition.

**Implementation**:

1. **Read agent response summaries** from STEP 8 (from Task tool results)
2. **Extract key insights**:
   - Main conclusions from each agent
   - Critical findings or recommendations
   - Cross-agent patterns or conflicts
3. **Synthesize findings** into concise summary (3-5 bullet points)
4. **Append to task.md** in task directory:

```markdown
## Research Findings

**Analysis Completed**: {timestamp}

**Key Insights**:
- {Insight 1 from agent A}
- {Insight 2 from agent B}
- {Cross-agent observation}

**Recommendations**:
- {Action item 1}
- {Action item 2}

**Full Analysis**:
- See {TASK_DIR}/research-codebase-analyst.md (17KB)
- See {TASK_DIR}/research-web-analyst.md (17KB)

**Conclusion**: {2-3 sentence synthesis of overall findings}
```

**Example**:

```markdown
## Research Findings

**Analysis Completed**: 2025-10-18T17:30:00Z

**Key Insights**:
- Codebase analyst: Architecture as clarity of purpose, technical debt as regrets
- Web analyst: Meaning is created not discovered, achievement ≠ fulfillment
- Both emphasize: Systematic problem-solving and maintainability = sustainability

**Recommendations**:
- Apply DRY principle to reduce conceptual debt
- Align work with personal values for meaning
- Build maintainable systems with clear purpose

**Full Analysis**:
- See TASK-029--analyze-the-meaning-of-life/research-codebase-analyst.md (17KB)
- See TASK-029--analyze-the-meaning-of-life/research-web-analyst.md (17KB)

**Conclusion**: Both perspectives converge on deliberate creation of meaning through systematic, maintainable work aligned with clear purpose and values.
```

Display progress:
- `⏳ Synthesizing research findings...`
- `✓ Research summary appended to task.md`

### STEP 9: Offer Handover

Present implementation options:
- A) Create specification (`/speckit:specify`) - RECOMMENDED
- B) Start implementation (`/development:small`)
- C) Continue manually

### STEP 10: Mark Task Complete (Optional)

**Execute this step when analysis/research is complete and user selects completion.**

1. **Check if task should be marked complete**:
   - User selected option "C) Mark task complete" from handover menu
   - OR `--complete` flag was provided in arguments
   - OR agents completed all analysis and no further work needed

2. **Update tasks.md** (master file):
   ```python
   # Read current tasks.md
   tasks_md_content = Path('.agent/tasks.md').read_text()

   # Find task section by ID and update fields:
   **Status**: in-progress → completed
   **Completed**: {current_timestamp}
   **Last Updated**: {current_timestamp}
   # Preserve **Details**: field (historical record of where work was done)
   # Preserve **Notes**: field with agent summaries

   # Write to tasks.md
   Path('.agent/tasks.md').write_text(updated_content)
   ```

3. **Sync completion status to task.md** (task directory copy):
   ```python
   # CRITICAL: Apply same updates to task.md in task directory
   task_md_path = Path(TASK_DIR) / 'task.md'
   task_md_content = task_md_path.read_text()

   # Update same fields:
   **Status**: in-progress → completed
   **Completed**: {current_timestamp}
   **Last Updated**: {current_timestamp}
   # Preserve **Details**: field (historical record)

   # Write to task.md
   task_md_path.write_text(updated_task_md_content)
   ```

4. **Display completion**:
   ```
   ✓ Task TASK-029 marked complete

   Analysis saved to:
   📁 {TASK_DIR}/
   ├── task.md
   ├── research-codebase-analyst.md
   └── research-web-analyst.md
   ```

**CRITICAL**: Use regex replacement to avoid duplicate "Last Updated" prefixes. Ensure status change is atomic and timestamp format is ISO 8601.

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
3. Go through STEP 5 (mandatory validation)
4. Then STEP 8 (invoke agents with explicit context paths)

### Performance Optimization

**Lazy Evaluation Pattern** (STEP 1):
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
