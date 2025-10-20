---
description: "Capture adhoc tasks with smart metadata inference from noisy input"
argument-hint: "\"noisy task description\" [--priority=level] [--category=type] [--epic=name] [--depends=TASK-XXX]"
allowed-tools: Read, Write, Edit, Bash(python3:*), Bash(git:status), mcp__sequential-thinking__sequentialthinking
---

# Command: Task Add

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Capture noisy task descriptions with smart metadata inference (dependencies, epic, priority, category).

**YOU MUST:**
1. ✓ Parse task description and optional override flags from $ARGUMENTS
2. ✓ Run TaskAnalyzer for 10-phase semantic analysis
3. ✓ Display inferred metadata with confidence scores
4. ✓ Allow user to override any inferred field
5. ✓ Auto-generate TASK-ID and create entry in tasks.md
6. ✓ Report success with new TASK-ID

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Implement or execute the task (capture only)
- ✗ Skip the inference display
- ✗ Make code changes

---

## IMPLEMENTATION FLOW

### Step 1: Parse Input
Extract task description and optional flags (--priority, --category, --epic, --depends)

### Step 2: Load Existing Tasks
Read `.agent/tasks.md` and find highest TASK-ID for auto-increment

### Step 3: Run TaskAnalyzer
Execute 10-phase semantic analysis on input

### Step 4: Display Inference Results
Show inferred metadata with confidence scores and reasoning

### Step 5: Create Task Entry
Auto-increment TASK-ID and create formatted entry with inferred/overridden values

### Step 6: Save & Report
Append to tasks.md and report success

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Capture adhoc work items with SMART METADATA INFERENCE: accept noisy user input → run TaskAnalyzer (10-phase semantic analysis) → infer dependencies/epic/priority/category → display inference results with confidence scores → allow optional flag overrides → generate auto-incremented TASK-XXX ID → create standardized entry with new schema (Depends On, Related, Epic fields)

**P**urpose: Zero-friction task capture from messy descriptions, intelligent extraction of dependencies and relationships, maintain unified task system with origin tracking (adhoc vs code-comment vs github-issue), enable dependency-aware workflows, prevent context loss from mental notes

**E**xpectation: New task entry in .agent/tasks.md with TASK-ID, inferred metadata (depends_on, epic, priority, category), confidence scores displayed, reasoning shown, user can override if needed, NO implementation/execution, strict capture-only operation

## Quick Start

```bash
# Add a task with smart inference
/task:add "Fix authentication bug that's blocking new users from signup"

# Add with priority override
/task:add "Refactor widget system" --priority=high
```

## Quality Standards (CARE)

**Target**: 90+ overall (Completeness >98% metadata fields, Inference Accuracy >85% dependencies/epic, Reasoning Clarity >90%, Efficiency <5s capture with smart inference)

## Purpose

Captures adhoc work items and ideas with SMART METADATA INFERENCE into the unified task management system at `.agent/tasks.md`. Analyzes noisy input to automatically detect dependencies, epic assignments, priority, and categories.

**⚠️ STRICT CONSTRAINT: This command MUST NOT implement, code, or execute any tasks. It only captures task descriptions with smart inference.**

## Usage

```bash
/task:add "noisy task description [hints]" [--priority=level] [--category=type] [--epic=name] [--depends=TASK-XXX]
```

**Arguments**:

- `$1` (task-description): Noisy description of work (can include [BLOCKER], temporal hints, task refs, required)
- `--priority`: Override inferred priority: `low | medium | high | critical` (optional)
- `--category`: Override inferred category: `bug | feature | refactor | docs | test | research | chore` (optional)
- `--epic`: Override inferred epic: Epic name (optional)
- `--depends`: Override inferred dependencies: `TASK-XXX,TASK-YYY` comma-separated (optional)

**Input Examples**:

- `"fix the auth validation thing [BLOCKER] we need this before template work"` - Smart inference detects: [BLOCKER], priority=critical, related tasks
- `"after we finish context refactor, align agents with template"` - Smart inference detects: "after" hint, temporal dependency on context refactor
- `"refactor the database layer --priority=high"` - Inference + explicit override
- `"related to template standardization - update examples"` - Epic detection from keywords

## Smart Inference Pipeline (10 Phases)

The command uses TaskAnalyzer to automatically extract from noisy input:

1. **Extract Explicit References**: Find TASK-XXX and #issue references
2. **Parse Hint Patterns**: Detect [BLOCKER], [URGENT], after/before, related to, etc.
3. **Extract Keywords**: Tokenize and filter stopwords
4. **Semantic Matching**: Find related existing tasks
5. **Detect Epic**: From keywords and task context
6. **Infer Priority**: From [BLOCKER]/[URGENT] or task relationships
7. **Detect Category**: From language patterns (fix→bug, add→feature)
8. **Infer Dependencies**: From temporal hints, explicit refs, phrases
9. **Calculate Confidence**: Score each inference (0.0-1.0)
10. **Generate Reasoning**: Explain decisions to user

## Process

**FORBIDDEN ACTIONS**: Implementing features, executing tasks, creating files other than tasks.md, making code changes

**ALLOWED ACTIONS ONLY**:

1. **Call TaskAnalyzer**: Load tasks.md → run 10-phase analysis on input
2. **Display Inferred Metadata**: Show inferred values with confidence scores and reasoning
3. **Allow Overrides**: User can override any field with flags
4. **Read Existing File**: Read `{project_root}/.agent/tasks.md` (create if doesn't exist)
5. **Generate Task ID**: Auto-increment from highest existing TASK-XXX number
6. **Tag Origin**: Set origin to `adhoc`
7. **Create Task Entry**: Use new schema with Depends On, Related, Epic fields
8. **Save File**: Write updated tasks.md
9. **Report Success**: Confirm task captured with inferred metadata
10. **STOP IMMEDIATELY** - No further actions permitted

## Task Format

All adhoc tasks use this ENHANCED standardized format with dependency tracking:

```markdown
## [TASK-001] Fix login validation error

**Status**: pending
**Priority**: high
**Category**: bug
**Epic**: Security
**Depends On**: (none)
**Related**: TASK-010
**Origin**: adhoc
**Created**: 2025-10-13T10:30:00Z

**Description**:
Fix the validation error that occurs when users attempt to login with special characters in their username.

---
```

**Metadata Fields**:

- **Status**: Always `pending` for new tasks
- **Priority**: `low | medium | high | critical` (inferred from [BLOCKER]/[URGENT] or defaults to medium)
- **Category**: `bug | feature | refactor | docs | test | research | chore` (inferred from language patterns)
- **Epic**: Epic name (inferred from keywords and task context, can be None)
- **Depends On**: Comma-separated TASK-XXX IDs (inferred from temporal hints, explicit refs, phrases)
- **Related**: Comma-separated TASK-XXX IDs (semantically related, not strict dependencies)
- **Origin**: Always `adhoc` (user-created task)
- **Created**: ISO 8601 timestamp (UTC)

**Confidence Metadata** (shown during creation, not stored):

```
✓ Created TASK-051: Fix auth validation

Inferred Metadata:
├─ Priority: critical [confidence: 0.99]
│  (Detected: [BLOCKER] marker)
├─ Epic: Security [confidence: 0.85]
│  (Inferred from: security-related keywords)
├─ Depends On: (none) [confidence: 1.00]
├─ Category: bug [confidence: 0.92]
│  (Detected: "fix" + "validation" keywords)
└─ Related: TASK-010 [confidence: 0.87]
   (Similar: authentication validation task)

Reasoning:
- Priority elevated to 'critical' due to [BLOCKER] marker
- Category inferred as 'bug' from language patterns
- Inferred epic from security-related keywords
- No dependencies detected (this blocks others, doesn't depend)
- Related task found: similar validation work
```

## Explicit Constraints

**IN SCOPE**: Task capture with smart inference (TaskAnalyzer 10-phase analysis), description parsing, dependency extraction, epic detection, ID generation, metadata tagging with origin=adhoc, file write to .agent/tasks.md, confidence scoring, reasoning display, allow flag overrides
**OUT OF SCOPE**: Task implementation/execution (FORBIDDEN), code changes, file creation beyond tasks.md, task analysis/breakdown, agent invocation, GitHub integration (use /github:create-issue-from-task)

## Integration with TaskAnalyzer

This command MUST use `scripts/task/task_analyzer.py` module:

```bash
# Internal step in /task:add
python3 ~/.claude/scripts/task/task_analyzer.py analyze ~/.claude/.agent/tasks.md "user_input"

# Returns JSON:
{
    "depends_on": ["TASK-015"],
    "epic": "Context Management",
    "priority": "critical",
    "category": "bug",
    "confidence": {
        "epic": 0.85,
        "depends_on": 0.90,
        "priority": 0.99,
        "category": 0.92,
        "overall": 0.91
    },
    "reasoning": [
        "Priority elevated to 'critical' due to [BLOCKER] marker",
        "Found temporal relationship: 'after'",
        "Inferred epic from similar tasks: Context Management",
        ...
    ],
    "related": ["TASK-010"],
    "explicit_issues": ["#123"]
}
```

## Examples

### Example 1: Noisy Input with [BLOCKER] Hint

```bash
/task:add "fix the auth validation thing [BLOCKER] we need this before template work"

System processes (smart inference):
1. Extracts [BLOCKER] → priority=critical
2. Keywords: auth, validation → finds TASK-016 (auth-related)
3. Context: "before template work" → related to Template Standardization epic
4. Category: "fix" + "validation" → bug

✓ Created TASK-051: Fix auth validation thing

Inferred Metadata:
├─ Priority: critical [confidence: 0.99]
│  (Detected: [BLOCKER] marker)
├─ Epic: (none detected) [confidence: 0.50]
│  (Suggestion: Link to security-related epic?)
├─ Depends On: (none) [confidence: 1.00]
│  (This is a blocker, doesn't depend on others)
├─ Category: bug [confidence: 0.92]
│  (Pattern: "fix" + "validation" keywords)
└─ Related: TASK-016 [confidence: 0.87]
   (Similar: authentication tasks)

Reasoning:
- Priority elevated to 'critical' due to [BLOCKER] marker
- Category inferred as 'bug' from language patterns
- This is a blocking task (doesn't depend on others)
- Related task found: TASK-016 (auth-related)
```

### Example 2: Temporal Hint with "after"

```bash
/task:add "after we finish context refactor, align agents with template structure"

System processes (smart inference):
1. Keyword: "context refactor" → finds TASK-015
2. Temporal: "after" → depends on TASK-015
3. Keywords: align, agents, template → suggests epic Template Standardization
4. Category: "align" + "template" → refactor or feature

✓ Created TASK-052: Align agents with template structure

Inferred Metadata:
├─ Priority: medium [confidence: 0.60]
│  (No explicit hints, default to medium)
├─ Epic: Template Standardization [confidence: 0.88]
│  (Inferred from: similar tasks context)
├─ Depends On: TASK-015 [confidence: 0.90]
│  (Found temporal reference: "after")
├─ Category: feature [confidence: 0.76]
│  (Pattern: "align", "structure" keywords)
└─ Related: TASK-005, TASK-006 [confidence: 0.83]
   (Same epic: Template Standardization tasks)

Reasoning:
- Found temporal relationship: 'after' → depends on TASK-015
- Inferred epic from similar tasks: Template Standardization
- Category inferred from language patterns
- Related tasks found in same epic
```

### Example 3: Explicit Override

```bash
/task:add "refactor database layer after auth work" --priority=high --epic="Performance"

System processes (smart inference + overrides):
1. Keywords: refactor, database, layer → suggests "refactor" category
2. Temporal: "after" → depends on auth tasks (TASK-010)
3. Smart inference: epic=database, priority=medium
4. FLAGS OVERRIDE: --priority=high, --epic=Performance

✓ Created TASK-053: Refactor database layer

Inferred Metadata:
├─ Priority: high [OVERRIDDEN by flag]
│  (Smart: medium, User override: high)
├─ Epic: Performance [OVERRIDDEN by flag]
│  (Smart: (none), User override: Performance)
├─ Depends On: TASK-010 [confidence: 0.85]
│  (Detected: "after auth work")
├─ Category: refactor [confidence: 0.89]
│  (Pattern: "refactor", "database" keywords)
└─ Related: TASK-009, TASK-011 [confidence: 0.78]

Reasoning:
- Found temporal relationship: 'after' → depends on TASK-010
- Category inferred as 'refactor' from language patterns
- Priority overridden by user flag (smart: medium → high)
- Epic overridden by user flag (smart: (none) → Performance)
```

### Example 4: Complex Noisy Input

```bash
/task:add "[URGENT] related to MCP integration - sanitize task dependencies for TASK-001 and TASK-011"

System processes (smart inference):
1. Extracts [URGENT] → priority=high
2. Keywords: MCP, integration, sanitize → related to TASK-001, TASK-011
3. Explicit TASK refs: TASK-001, TASK-011
4. Category: "sanitize" + "dependencies" → chore or refactor
5. Epic: MCP Integration (from keywords)

✓ Created TASK-054: Sanitize task dependencies

Inferred Metadata:
├─ Priority: high [confidence: 0.99]
│  (Detected: [URGENT] marker)
├─ Epic: MCP Integration [confidence: 0.81]
│  (Inferred from: keywords + task context)
├─ Depends On: (none) [confidence: 1.00]
│  (This improves others, doesn't depend)
├─ Category: chore [confidence: 0.83]
│  (Pattern: "sanitize", "dependencies" keywords)
└─ Related: TASK-001, TASK-011 [confidence: 0.92]
   (Explicit mention + semantic match)

Reasoning:
- Priority set to 'high' due to [URGENT] marker
- Explicit task references: TASK-001, TASK-011 → related
- Inferred epic from keywords: MCP Integration
- Category inferred as 'chore' from language patterns
```

## Integration Points

- **Follows**: Brainstorming, code review, bug discovery
- **Followed by**: `/task:execute` (triage and work on tasks)
- **Related**: `/task:scan-project` (code comments), `/github:convert-issues-to-tasks` (GitHub issues)

## Quality Standards

- Keep task description concise and actionable
- Use clear, descriptive titles
- Set priority when impact is known
- Categorize for better organization
- No breakdown or detailed planning (unless requested)
- ISO 8601 timestamps (UTC)
- Auto-incrementing task IDs
- Origin always tagged as `adhoc`

## Output

- Updated `{project_root}/.agent/tasks.md` with new task entry
- Task ID assignment (auto-incremented)
- Confirmation message with task details
- Brief validation of metadata

## Workflow Examples

### Quick Capture During Development

```bash
# Found a bug while coding
/task:add "Fix null pointer in user service --priority=high --category=bug"

# Idea for improvement
/task:add "Add caching to API responses --category=feature"

# Technical debt discovered
/task:add "Remove deprecated authentication code --category=refactor"
```

### Sprint Planning

```bash
# Capture sprint backlog items
/task:add "Implement user registration --priority=high --category=feature"
/task:add "Add password reset flow --priority=high --category=feature"
/task:add "Update user documentation --priority=medium --category=docs"
/task:add "Add integration tests --priority=medium --category=test"
```

### Research Phase

```bash
# Research tasks before implementation
/task:add "Research microservices patterns --category=research"
/task:add "Evaluate authentication libraries --priority=high --category=research"
/task:add "Performance benchmarking comparison --category=research"
```

## Best Practices

1. **Capture Immediately** - Don't wait, capture tasks as you think of them
2. **Keep Descriptions Concise** - One clear sentence is sufficient
3. **Use Priority Wisely** - Reserve `critical` for urgent blockers
4. **Categorize Consistently** - Helps with filtering and organization
5. **Review Regularly** - Check tasks at start of each session (`/task:execute`)
6. **Update Status** - Use `/task:execute` when starting work
7. **Convert to Issues** - Use `/github:create-issue-from-task` for team visibility

## Task vs GitHub Issue

**Use `/task:add` for**:

- Personal work items during development
- Quick capture of ideas and bugs
- Session-specific tasks
- Items not ready for team visibility
- Research and exploration

**Use `/github:create` for**:

- Team-visible work items
- Official project backlog
- Issues requiring discussion
- Work spanning multiple sessions

**Convert adhoc tasks to GitHub issues** when ready for team collaboration.

## Adhoc Task Benefits

**Why origin=adhoc?**

1. **Distinguishes from code comments** - Can filter by origin
2. **Separate from GitHub issues** - Local work vs team work
3. **Flexible workflow** - Convert to issues or archive as needed
4. **Quick capture** - No GitHub authentication required
5. **Private brainstorming** - Ideas stay local until ready

**Workflow Pattern**:

```
Idea/Bug → /task:add (adhoc) → Work locally → /github:create (team visibility)
```
