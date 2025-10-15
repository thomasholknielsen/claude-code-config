---
description: "Intelligent task triaging and execution with seamless speckit integration"
argument-hint: "[TASK-XXX ...] [--status=state] [--notes=\"text\"] [--complete]"
allowed-tools: Read, Edit, SlashCommand(/speckit:specify), SlashCommand(/development:small), mcp__sequential-thinking__sequentialthinking
---

# Command: Task Execute

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Intelligent task management via three modes (interactive triaging with 0-3 contextual questions + grouping, direct execution by TASK-ID with auto-status updates, quick update for metadata-only changes), read .agent/tasks.md, analyze patterns (priority/origin/category distribution), detect logical groupings (same module/related features/GitHub milestones), present selection with rationale, seamless handover to /speckit:specify or /development:small

**P**urpose: Reduce decision paralysis through smart contextual questions, maximize efficiency via automatic task grouping (related work done together), enable flexible workflows (from exploration to structured speckit), maintain unified task tracking with origin-aware filtering, support seamless transition from triaging to implementation

**E**xpectation: Interactive Mode → 0-3 questions + selected tasks with grouping rationale + implementation path options. Direct Mode → task details display + auto-status to in-progress + metadata updates + handover offer. Quick Update Mode → metadata-only changes + confirmation. All modes preserve history with ISO timestamps

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% task metadata, Accuracy >90% grouping logic, Relevance >85% question contextuality, Efficiency <10s triaging)

## Explicit Constraints

**IN SCOPE**: Task triaging (pattern analysis, contextual questions, grouping detection), direct execution (TASK-ID lookup, status updates, notes), metadata management (auto-status, timestamps), speckit/development handover, origin filtering (adhoc/code-comment/github-issue)
**OUT OF SCOPE**: Task implementation (delegates to /speckit:*or /development:*), duplicate detection/merging, task dependencies/ordering, GitHub sync (status updates don't sync to GitHub), bulk operations (use individual /task:execute calls)

## Purpose

Intelligent task management command that analyzes your task backlog, asks contextual questions to identify relevant work, and seamlessly hands off to implementation workflows.

**Three Modes**:

1. **Interactive Triaging** - Analyzes tasks, asks smart questions, helps you focus
2. **Direct Execution** - Work on specific tasks by ID
3. **Quick Update** - Update status/notes without full display

## Usage

### Mode 1: Interactive Triaging (No arguments)

```bash
/task:execute
```

**Behavior**:

1. Reads all pending/blocked tasks from `.agent/tasks.md`
2. Analyzes patterns (related tasks, priority distribution, origins)
3. Identifies logical groupings (same module, related features, GitHub milestones)
4. Asks 0-3 contextual multiple-choice questions
5. Presents selected task(s) with rationale
6. Offers seamless handover to `/speckit:specify` or `/development:small`

**Question Examples**:

```
Found 15 pending tasks. Let me help you focus:

Q1: What should we prioritize?
A) Critical bugs (2 tasks) - authentication & database issues
B) High-priority features (4 tasks) - OAuth & user management
C) Technical debt (6 tasks) - code comments from recent scan
D) Show me everything

Q2: Which area needs attention?
A) Authentication module (3 related tasks)
B) Database layer (2 tasks)
C) API endpoints (4 tasks)
D) No preference

Q3: Task grouping preference?
A) Work on related tasks together (recommended: 3 auth tasks)
B) One task at a time
```

### Mode 2: Direct Execution (With task IDs)

```bash
/task:execute TASK-XXX [TASK-YYY ...]
```

**Arguments**:

- `TASK-XXX` - One or more task IDs (space-separated)
- `--status=state` - Update status: `pending | in-progress | blocked | completed`
- `--notes="text"` - Add progress note with timestamp
- `--complete` - Shorthand for `--status=completed`

**Behavior**:

- Shows task details immediately
- Auto-sets status to `in-progress` if currently `pending`
- Displays full task information (metadata, description, notes, code context)
- Offers speckit handover for implementation

**Examples**:

```bash
# Start work on single task
/task:execute TASK-001

# Work on multiple related tasks
/task:execute TASK-001 TASK-002 TASK-003

# Mark task complete with note
/task:execute TASK-001 --complete --notes="Tests passing, PR created"

# Update status to blocked
/task:execute TASK-005 --status=blocked --notes="Waiting for API key from DevOps"
```

### Mode 3: Quick Update (Status/Notes only)

```bash
/task:execute TASK-XXX --notes="progress update"
/task:execute TASK-XXX --status=in-progress
```

**Behavior**:

- Updates metadata only
- No full task display
- Quick status/progress tracking

## Process

### Interactive Mode Process

1. **Read Tasks**: Load all pending/blocked tasks from `.agent/tasks.md`

2. **Analyze Task Set**:
   - Count by priority (critical, high, medium, low)
   - Count by origin (github-issue, code-comment, adhoc)
   - Count by category (bug, feature, refactor, docs, test, research, chore)
   - Identify patterns and groupings

3. **Detect Logical Groupings**:
   - **Same Module**: Tasks referencing same file/directory
   - **Related Features**: Tasks with similar descriptions or linked features
   - **GitHub Milestone**: Tasks from same GitHub milestone
   - **Code Comment Clusters**: Multiple TODOs/FIXMEs in same area

4. **Generate Smart Questions** (0-3 based on analysis):
   - **0 questions**: Only 1-2 obvious tasks (go straight to presentation)
   - **1 question**: Clear pattern needs confirmation (e.g., "Focus on critical bugs?")
   - **2 questions**: Need priority + area narrowing
   - **3 questions**: Diverse task set + grouping preference

5. **Present Selected Task(s)**:

   ```
   Selected: Authentication Bug Fix Group (3 tasks)

   [TASK-015] Fix login validation - CRITICAL
   Priority: critical | Origin: github-issue | Category: bug

   [TASK-018] Add session timeout - HIGH
   Priority: high | Origin: code-comment | Location: src/auth/session.ts:67

   [TASK-022] Refactor auth middleware - HIGH
   Priority: high | Origin: code-comment | Location: src/middleware/auth.ts:34

   Rationale: All three tasks touch the authentication system.
   Fixing them together will provide better context and avoid
   rework. Estimated combined effort: 3-4 hours.
   ```

6. **Offer Implementation Path**:

   ```
   Ready to implement? Choose your approach:

   A) Create detailed specification (/speckit:specify) - RECOMMENDED
      Best for: Complex tasks, unclear requirements, need planning

   B) Start small implementation (/development:small)
      Best for: Clear requirements, straightforward changes

   C) Mark as in-progress and work manually
      Best for: Exploratory work, research tasks

   D) Show me different tasks
   ```

### Direct Mode Process

1. **Parse Arguments**: Extract task IDs and options
2. **Read tasks.md**: Load `.agent/tasks.md`
3. **Find Tasks**: Locate specified tasks by ID
4. **Display Details**: Show full task information for each task
5. **Update Metadata**:
   - Auto-set to `in-progress` if currently `pending` (unless different status specified)
   - Add notes if provided
   - Update "Last Updated" timestamp
6. **Save Changes**: Write updated tasks.md
7. **Offer Handover**: Present speckit/development options

## Task Grouping Logic

### Pattern Detection Examples

**Same Module Pattern**:

```
Detected: 3 code-comment tasks in src/services/auth.ts
- TASK-010: Extract validation logic (line 45)
- TASK-015: Add error handling (line 78)
- TASK-020: Improve type safety (line 120)

Grouping rationale: All in same file, can be refactored together efficiently.
```

**Related Features Pattern**:

```
Detected: OAuth Integration Suite (4 tasks)
- TASK-025: Design OAuth flow - PENDING
- TASK-026: Implement OAuth backend - PENDING
- TASK-027: Add OAuth UI components - PENDING
- TASK-028: Write OAuth tests - PENDING

Grouping rationale: Sequential dependencies. Best done in order.
```

**GitHub Milestone Pattern**:

```
Detected: Sprint 5 Critical Bugs (3 tasks)
- TASK-030: Fix checkout race condition (#145) - CRITICAL
- TASK-031: Database connection leak (#148) - CRITICAL
- TASK-032: API timeout handling (#152) - HIGH

Grouping rationale: All tagged for Sprint 5 milestone, team priority.
```

**Priority Clustering Pattern**:

```
Detected: Multiple critical issues requiring immediate attention
- TASK-005: Security vulnerability in auth - CRITICAL
- TASK-012: Data corruption bug - CRITICAL
- TASK-018: API endpoint crash - CRITICAL

Grouping rationale: All critical priority, block other work.
```

## Spec-Kit Integration

### Handover Flow

After task selection, command offers implementation options:

```
Selected task(s) ready for implementation.

Choose your approach:

A) Create specification with /speckit:specify (RECOMMENDED)
   → Detailed requirements gathering
   → Architecture planning
   → Implementation roadmap
   → Best for complex or unclear tasks

B) Start small implementation with /development:small
   → Direct implementation for clear tasks
   → Focused, atomic changes
   → Best for straightforward fixes

C) Manual implementation
   → Mark as in-progress
   → Work directly without framework
   → Best for exploration/research
```

**If user chooses A**:

```
Invoking /speckit:specify with selected task(s)...

[Context passed to speckit:specify]
- Task IDs: TASK-015, TASK-018, TASK-022
- Feature: Authentication system improvements
- Related files: src/auth/*, src/middleware/auth.ts
- Priority: Critical/High
- Estimated scope: 3-4 hours

[Spec-kit takes over from here]
```

**If user chooses B**:

```
Invoking /development:small...

[Context passed to development:small]
- Task IDs: TASK-015
- Scope: Fix login validation
- Files: src/auth/validate.ts
- Priority: Critical

[Development workflow takes over]
```

## Agent Integration

- **No agents required** for basic operation
- **Specialist Options**:
  - code-quality-analyst: Can help prioritize technical debt
  - architecture-analyst: Can advise on grouped refactoring tasks
  - research-codebase-analyst: Can provide context for complex task groups

## Examples

### Example 1: Interactive Triaging (Diverse Tasks)

```bash
/task:execute
# where $ARGUMENTS = ""

# Expected interaction:
→ Analyzing 18 pending tasks...
→
→ Found diverse workload. Let me help you focus:
→
→ Q1: What should we prioritize?
→ A) Critical bugs (2 tasks) - authentication & database
→ B) High-priority features (5 tasks) - OAuth & user management
→ C) Technical debt (8 tasks) - code comments from scan
→ D) Medium priority work (3 tasks) - docs & tests
→
User: B
→
→ Q2: Which feature area?
→ A) OAuth integration (3 related tasks)
→ B) User management (2 tasks)
→ C) All features
→
User: A
→
→ Selected: OAuth Integration Suite (3 tasks)
→
→ [TASK-025] Design OAuth flow - HIGH
→ [TASK-026] Implement OAuth backend - HIGH
→ [TASK-027] Add OAuth UI components - MEDIUM
→
→ Rationale: Sequential implementation recommended.
→ Start with design, then backend, then UI.
→
→ Ready to implement?
→ A) Create specification (/speckit:specify) - RECOMMENDED
→ B) Start implementation (/development:small)
→ C) Mark in-progress manually
→
User: A
→
→ Invoking /speckit:specify for OAuth integration...
```

### Example 2: Interactive Triaging (Focused Priority)

```bash
/task:execute

# Expected interaction:
→ Analyzing 6 pending tasks...
→
→ Q1: Priority focus?
→ A) Critical bug (1 task) - needs immediate attention
→ B) High-priority tasks (3 tasks) - planned for sprint
→ C) All tasks
→
User: A
→
→ Selected: [TASK-015] Security vulnerability in authentication - CRITICAL
→
→ Origin: github-issue (#145)
→ Category: bug
→ Priority: critical
→
→ Description:
→ SQL injection vulnerability in login endpoint allows
→ unauthorized access. Reported by security audit.
→
→ This is a critical security issue requiring immediate attention.
→
→ Ready to implement?
→ A) Create specification (/speckit:specify) - RECOMMENDED
→ B) Start implementation (/development:small)
→ C) Mark in-progress manually
```

### Example 3: Direct Task Execution

```bash
/task:execute TASK-001
# where $ARGUMENTS = "TASK-001"

# Expected behavior:
→ [TASK-001] Fix login validation error
→
→ Status: pending → in-progress (auto-updated)
→ Priority: high
→ Category: bug
→ Origin: adhoc
→ Created: 2025-10-13T10:00:00Z
→ Last Updated: 2025-10-13T16:30:00Z
→
→ Description:
→ Fix validation error when users login with special characters.
→
→ Ready to implement?
→ A) Create specification (/speckit:specify)
→ B) Start implementation (/development:small)
→ C) Continue manually
```

### Example 4: Multiple Tasks Direct

```bash
/task:execute TASK-010 TASK-015 TASK-020
# where $ARGUMENTS = "TASK-010 TASK-015 TASK-020"

# Expected behavior:
→ Selected 3 related tasks:
→
→ [TASK-010] Extract validation logic (code-comment)
→ [TASK-015] Add error handling (code-comment)
→ [TASK-020] Improve type safety (code-comment)
→
→ All tasks in: src/services/auth.ts
→ Auto-grouped for efficient refactoring
→
→ Status updated: pending → in-progress (all 3 tasks)
→
→ Ready to implement?
→ A) Create specification (/speckit:specify) - RECOMMENDED
→ B) Start implementation (/development:small)
→ C) Continue manually
```

### Example 5: Quick Status Update

```bash
/task:execute TASK-001 --notes="Found issue in regex pattern at line 45"

# Expected behavior:
→ TASK-001 updated
→ Note added: "Found issue in regex pattern at line 45" (2025-10-13T16:35:00Z)
```

### Example 6: Mark Complete

```bash
/task:execute TASK-001 --complete --notes="Tests passing, PR #123 created"

# Expected behavior:
→ TASK-001 completed
→ Status: in-progress → completed
→ Completed: 2025-10-13T17:00:00Z
→ Note added: "Tests passing, PR #123 created"
→
→ Great work! Run /task:archive to clean up completed tasks.
```

## Integration Points

- **Follows**: `/task:add`, `/task:scan-project --consolidate`, `/github:convert-issues-to-tasks`
- **Followed by**: `/speckit:specify`, `/development:small`, `/task:archive`
- **Related**: `/github:create-issue-from-task` (create issues from tasks)

## Quality Standards

- **Smart Analysis**: Contextual questions based on actual task patterns
- **Logical Grouping**: Detect related tasks automatically
- **Clear Rationale**: Explain why tasks are grouped
- **Seamless Handover**: Smooth transition to implementation workflows
- **Auto-Status**: Intelligently update status based on context
- **Preserve History**: All notes and updates timestamped

## Output

- Task analysis summary
- Contextual questions (0-3)
- Selected task(s) with details
- Grouping rationale (if applicable)
- Implementation path options
- Handover to speckit or development commands

## Workflow Examples

### Daily Development Workflow

```bash
# Morning: See what's next
/task:execute
# Answer questions: A (critical bugs)
# Choose: A (speckit)

# Work on task
[speckit workflow]

# Update progress
/task:execute TASK-001 --notes="Fixed validation, running tests"

# Complete
/task:execute TASK-001 --complete

# Get next task
/task:execute
```

### Sprint Planning Workflow

```bash
# Import GitHub issues
/github:fetch-issues --milestone=sprint-5
/github:convert-issues-to-tasks --source-file=.agent/github-issues.md

# Review and start work
/task:execute
# Answer: A (GitHub issues)
# Answer: A (speckit)
```

### Technical Debt Workflow

```bash
# Scan codebase
/task:scan-project src/ --types=TODO,FIXME --consolidate

# Triage technical debt
/task:execute
# Answer: C (technical debt)
# Answer: A (authentication module)
# Choose: A (speckit - grouped refactoring)
```

## Best Practices

1. **Use Interactive Mode** - Let the command help you focus
2. **Trust Grouping** - Related tasks are more efficient together
3. **Choose Spec-Kit** - Complex tasks benefit from planning
4. **Update Progress** - Use `--notes` to track work
5. **Complete Promptly** - Mark done when finished, archive regularly
6. **Ask Questions** - Command will guide you with contextual options

## Task Selection Algorithm

**Priority Sorting**:

1. Critical priority tasks first
2. High priority tasks second
3. Within same priority: github-issue > code-comment > adhoc
4. Within same origin: older tasks first (by created date)

**Grouping Detection**:

1. Same file/module (for code-comment origin)
2. Related descriptions (keyword matching)
3. GitHub milestone (for github-issue origin)
4. Category clusters (multiple bugs in same area)

**Question Generation Logic**:

- **0 questions**: ≤2 tasks OR all same priority+origin
- **1 question**: Clear pattern (e.g., all bugs, need priority choice)
- **2 questions**: Mixed priorities + multiple areas
- **3 questions**: Diverse set + grouping opportunity

## Notes on Command Behavior

**Auto-Status Update**:

- First time executing a `pending` task → auto-sets to `in-progress`
- Subsequent executions → keep current status unless explicitly changed
- `--complete` flag → sets to `completed` + adds completion timestamp

**Task Display**:

- Interactive mode: Shows selected tasks with rationale
- Direct mode (task IDs): Shows full task details
- Quick update (with --notes/--status only): Minimal output

**Spec-Kit Context Passing**:
When handing off to `/speckit:specify`, command passes:

- Task IDs
- Task descriptions
- Related files (for code-comment tasks)
- Priority/category information
- Grouping rationale

This context helps speckit generate better specifications aligned with the actual work needed.
