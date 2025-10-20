---
description: "Intelligent task execution with dependency-aware workflow and validation"
argument-hint: "[TASK-XXX ...] [--status=state] [--notes=\"text\"] [--complete] [--validate]"
allowed-tools: Read, Edit, Bash, SlashCommand(/speckit:*), mcp__sequential-thinking__sequentialthinking
---

# Command: Task Execute

## Quick Start

```bash
# Interactive mode - select from pending tasks
/task:execute

# Direct execution - by task ID
/task:execute TASK-001

# Search-based - find matching tasks
/task:execute "fix authentication"
```

## EXECUTION FLOW (START HERE)

### MANDATORY: Read This BEFORE Proceeding

**This command has EXACTLY TWO workflows:**

1. **Interactive Mode** (no arguments) → Show all tasks with dependency info, offer grouping
2. **Direct Mode** (with arguments) → STEP 0 (Dependency Check) → STEP 1 (Smart Task Gate) → STEP 2-10

**NEW**: Dependency awareness at every step - shows blockers, recommends execution order

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

### Step 0: Determine Mode & Pre-Flight Checks

**IF no arguments** → Execute **Interactive Mode** (skip Direct Mode)
**IF task-related arguments provided** → Execute **Direct Mode** (include STEP 0)

---

## DIRECT MODE: STEP 0 - Dependency Check

**BEFORE processing any task, check for dependency blockers:**

### STEP 0a: Load Dependency Graph

```bash
# Parse all tasks and build depends_on graph
# For each TASK-XXX argument:
# - Extract Depends On list
# - Compute Blocked By (reverse dependencies)
# - Check circular dependencies
```

### STEP 0b: Validate Task Dependencies

**For each task to execute:**

1. **Check if all dependencies completed**
   - Get Depends On list
   - Check status of each dependency
   - If any pending/in-progress: FLAG AS BLOCKER

2. **Check if other tasks depend on this**
   - Get Blocked By list
   - Report if completing this unblocks work

3. **Check for circular dependencies**
   - Alert if cycle detected
   - Suggest which relationship to break

### STEP 0c: Display Dependency Analysis

**IF blockers found:**

```
📋 Dependency Analysis for TASK-005

TASK-005: Align agents with template
├─ Status: pending
├─ Depends On: TASK-003 (pending) ⚠️ BLOCKER
└─ Blocked By: TASK-006, TASK-007 (waiting for this)

⚠️ This task cannot start until:
1. TASK-003 - Review command template (pending)

Recommended execution order:
1. TASK-003 - Review command template
2. TASK-005 - Align agents with template
3. TASK-006 - Align mermaid with template
4. TASK-007 - Align commands with template

Continue anyway? [y/N]
```

**IF no blockers:**

```
✓ TASK-005 ready to execute (no blockers)
Ready: Yes (all dependencies completed)
This task unblocks: TASK-006, TASK-007
```

**IF --validate flag:**

```
/task:execute TASK-005 --validate

Validation Report:
- Dependencies: ✓ All completed
- Status: ready
- Epic: Template Standardization
- Priority: medium
- Category: chore

Estimate: 30 min (based on similar tasks)
Ready to start: YES
```

### STEP 0d: Decision Point

**User choice:**

```
| Option | Action |
|--------|--------|
| y | Continue with TASK-005 anyway |
| 1 | Execute TASK-003 first (suggested) |
| 2 | Execute TASK-003 then TASK-005 (batch) |
| --epic | Execute all tasks in epic (ordered) |
| N/Skip | Cancel (no execution) |

Your choice: _
```

**Actions:**
- `y` → Continue to STEP 1 with selected task
- `1` → Change context to TASK-003, re-run STEP 0
- `2` → Add TASK-003 to queue, then TASK-005
- `--epic` → Load epic, sort by dependencies, confirm order
- `N/Skip` → Exit command

---

## INTERACTIVE MODE with Dependency Info

### STEP I2 Enhanced: Display All Tasks (WITH Dependencies)

**New columns added:**

```
Available tasks (showing 10 of X):

| # | Task ID   | Description                                  | Status      | Deps | Ready |
|---|-----------|----------------------------------------------|-------------|------|-------|
| 1 | TASK-015  | Use speckit to refactor context management   | in-progress | 2→   | ✓     |
| 2 | TASK-019  | Review and refactor artifacts directory      | in-progress | ✓1→  | ✓     |
| 3 | TASK-003  | Review command templates                     | pending     | -    | ✓     |
| 4 | TASK-005  | Align agents with template                   | pending     | 3    | ⚠️    |
| 5 | TASK-006  | Align mermaid with template                  | pending     | 3    | ⚠️    |
```

**Column Meanings:**
- `Deps`: Dependencies (shows blockers or "-" if none)
  - `2→` means depends on 2 completed tasks
  - `3` means depends on pending TASK-003
  - `-` means no dependencies
- `Ready`: Execution readiness
  - `✓` = All dependencies completed, ready to start
  - `⚠️` = Blocked (has pending dependencies)
  - `X` = Circular dependency detected

---

### STEP I3 Enhanced: Handle Selection with Dependencies

**After task selection, run STEP 0 (Dependency Check)**

Show dependency info before starting work:

```
You selected: TASK-005

Dependency Check:
├─ Depends On: TASK-003 (pending) ⚠️
├─ Blocked By: TASK-006, TASK-007
└─ Ready: NO

Suggestion: Execute TASK-003 first

Continue? [y/1/N]
- y = Start TASK-005 anyway
- 1 = Switch to TASK-003 first
- N = Cancel
```

---

## INTERACTIVE MODE (No Arguments)

**Execute these concrete steps in order:**

### STEP I0: Session Context Check (Session-Aware Entry Point)

**Execute THIS step FIRST before showing task list:**

```bash
# 1. Check for active session
SESSION=$(python3 ~/.claude/scripts/session/session_manager.py current)

# 2. If session exists, get current task and topic
if [ -n "$SESSION" ]; then
    CURRENT_TASK=$(python3 -c "
from pathlib import Path
import re

session_md = Path('.agent/Session-${SESSION}/session.md').read_text()
match = re.search(r'\*\*Current Task\*\*:\s*(.+)', session_md)
task = match.group(1).strip() if match else '(none)'
print(task if task != '(none)' else '')
    ")

    SESSION_TOPIC=$(grep '**Topic**:' .agent/Session-${SESSION}/session.md | sed 's/\*\*Topic\*\*:\s*//')
fi
```

### STEP I0a: Active Task in Session

**IF SESSION exists AND CURRENT_TASK is set (not empty):**

Display active session context:

```
📋 Active Session: ${SESSION}
Topic: ${SESSION_TOPIC}

⏳ Task in Progress: ${CURRENT_TASK}
${TASK_TITLE}
Status: in-progress
Last Updated: ${TIMESTAMP}

| Option | Action |
|--------|--------|
| Continue | Resume work on current task |
| Complete | Mark task complete, pick new task |
| Switch | Pause current task, select different task |
| Skip | Exit |

Your choice: _
```

**Handle selection:**
- `Continue` → Load CURRENT_TASK, go directly to STEP 7 (Context Path Preview) since setup already done
- `Complete` → Run STEP 10 (mark complete), then continue to STEP I1 (show task list)
- `Switch` → Continue to STEP I1 (show all tasks)
- `Skip` → Exit command

### STEP I0b: Session Without Active Task

**ELIF SESSION exists BUT CURRENT_TASK is empty:**

Display session info with filtering option:

```
📋 Active Session: ${SESSION}
Topic: ${SESSION_TOPIC}
Status: No active task

| Option | Action |
|--------|--------|
| Related | Show tasks related to session topic |
| All | Show all pending tasks |
| Skip | Exit |

Your choice: _
```

**Handle selection:**
- `Related` → Filter tasks by session topic keywords (see Task Filtering below), show filtered list in STEP I1
- `All` → Show all tasks (continue to STEP I1)
- `Skip` → Exit command

**Task Filtering for "Related" Option:**

```python
# Extract topic keywords (ignore common words)
topic_keywords = [w.lower() for w in SESSION_TOPIC.split()
                  if w.lower() not in ['the', 'a', 'an', 'of', 'for', 'to', 'in']]

# Score tasks by relevance
for task in tasks:
    score = 0
    task_text = (task.title + task.description + task.epic).lower()

    # Count keyword matches
    for keyword in topic_keywords:
        if keyword in task_text:
            score += 1

    task.relevance_score = score

# Sort by relevance (highest first), then priority
tasks.sort(key=lambda t: (-t.relevance_score, priority_order[t.priority]))

# Show top 10 most relevant
tasks = tasks[:10]
```

### STEP I0c: No Active Session

**ELSE (no active session):**

Skip directly to STEP I1 (show all tasks normally)

---

### STEP I1: Read All Pending Tasks

```bash
# Read tasks.md and extract all pending/in-progress/blocked tasks
# Use Python for reliable parsing
```

Extract task data:
- Task ID (TASK-XXX)
- Title/description
- Status (pending/in-progress/blocked)
- Priority (if present)

Limit to first 10 tasks for display.

### STEP I2: Display All Tasks (Merged Table Format)

```
Available tasks (showing 4 of 10):

| Option | Task ID   | Description                                              | Status      | Priority |
|--------|-----------|----------------------------------------------------------|-------------|----------|
| A      | TASK-015  | Use speckit to refactor context management               | in-progress | high     |
| B      | TASK-019  | Review and refactor artifacts directory                  | in-progress | medium   |
| C      | TASK-020  | Rename /prompt:enhance-prompt to /prompt:enhance         | pending     | low      |
| D      | TASK-030  | Change name of task:execute to task:implement            | pending     | medium   |
| More   | —         | Show next batch of tasks                                 | —           | —        |
| Search | —         | Search for specific task by keyword                      | —           | —        |
| Skip   | —         | Exit without selecting                                   | —           | —        |

Your choice (A-D, More, Search, or Skip): _
```

### STEP I3: Handle Selection

**IF letter selected (A-D or next available)**:
- Extract corresponding TASK-XXX ID
- Store in variable for Direct Mode
- **Continue to STEP 2** of Direct Mode (session validation)

**IF "More" selected**:
- Load next batch of tasks (up to 4 more)
- Redisplay merged table with A-D letters for new batch
- Previous options: E=More, F=Search, G=Skip
- Wait for selection

**IF "Search" selected**:
- Prompt: "Enter search query: _"
- Execute Direct Mode STEP 1b (Smart Task Search)
- Show search results in merged table format
- Wait for task selection
- **Continue to STEP 2** of Direct Mode

**IF "Skip" selected**:
- Exit command

### STEP I4: Route to Direct Mode Workflow

After task selection in STEP I3, execute the full Direct Mode workflow starting from STEP 2:

1. **STEP 2**: Validate or Create Session
2. **STEP 3**: Load and Display Tasks (load selected task)
3. **STEP 4**: Create Task Directories
4. **STEP 5**: Mandatory Validation Gate
5. **STEP 6**: Update Task Metadata
6. **STEP 7**: Context Path Preview
7. **STEP 8**: Invoke Agents (if needed)
8. **STEP 8.5**: Synthesize Research Findings
9. **STEP 9**: Offer Handover
10. **STEP 10**: Mark Task Complete (optional)

**CRITICAL**: Interactive Mode is just a task picker - all execution logic is in Direct Mode STEP 2-10.

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

### STEP 1c: Enhanced Selection Gate (Merged Table Format)

Display results with visual status indicators in a **single merged table**:

```
Searching for tasks matching: "authentication"

Showing 5 of 18 matches:

| Option   | Task ID   | Status   | Priority | Description                                        |
|----------|-----------|----------|----------|-----------------------------------------------------|
| A        | TASK-012  | [ACTIVE] | [!]      | Fix authentication bug causing login failures      |
| B        | TASK-014  | [ACTIVE] | [*]      | Implement rate limiting for API endpoints          |
| C        | TASK-006  | [DONE]   | -        | Review authentication code (completed 2025-10-16)  |
| More     | —         | —        | —        | Display more matches (13 additional)               |
| Search   | —         | —        | —        | Try different search terms                         |
| Create   | —         | —        | —        | Create new task (/task:add)                        |
| Show all | —         | —        | —        | See all pending tasks (interactive)                |
| Skip     | —         | —        | —        | Exit without executing                             |

Your choice (A-C, More, Search, Create, Show all, or Skip): _
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

  Your choice (A, B, or Skip): _
  ```
  - **If A**: Change status to "pending", proceed to STEP 2 (full STEP 1-2 then STEP 3-10 workflow)
  - **If B**: Display previous results, exit
  - **If Skip**: Return to selection gate

**IF "More" selected**:
- Extend results to next batch of matches
- Re-display merged table with updated A-D letters for new batch
- Pagination support (max 26 tasks per page, A-Z)
- Add options: More, Search, Create, Show all, Skip

**IF "Search" selected**:
- Prompt: "Enter new search query: _"
- Return to STEP 1b with new query

**IF "Create" selected**:
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

Display existing sessions in **merged table format**:

```
Existing sessions found:

| Option | Session       | Topic                              | Started          | Terminals |
|--------|---------------|------------------------------------|------------------|-----------|
| A      | task-029      | analyze meaning of life from c...  | 2025-10-18 19:20 | 1         |
| B      | feature-auth  | Authentication implementation      | 2025-10-17 14:30 | 2         |
| C      | —             | Create new session                 | —                | —         |
| Skip   | —             | Exit without session               | —                | —         |

Your choice (A-C, or Skip): _
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

Present implementation options with workflow guidance:

| Option | Description | Next Steps |
|--------|-------------|-----------|
| A) Specify | Create detailed specification (`/speckit:specify`) - RECOMMENDED | Generates `spec.md` with requirements and acceptance criteria |
| B) Implement | Start implementation workflow (`/speckit:implement`) | Executes tasks from `tasks.md` with progress tracking |
| C) Manual | Continue working manually | Review analysis files in task directory, proceed as needed |
| D) Complete | Mark task complete | Archives analysis to task directory, updates status |

**After Selection**:
- **Option A**: User runs `/speckit:specify` to create specification, then `/speckit:implement` to execute
- **Option B**: User runs `/speckit:implement` directly to begin task execution
- **Option C**: User reviews context files and continues independently
- **Option D**: Task marked complete, context files preserved

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
- Followed by: `/speckit:specify`, `/speckit:implement`, `/task:archive`
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
