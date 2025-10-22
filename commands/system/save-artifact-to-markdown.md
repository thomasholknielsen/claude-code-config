---
description: "Captures Claude conversation artifacts (plans, reviews, research) and saves them to session/task directories in .agent/Session-{date}-{id}/"
argument-hint: "[type] [--title=\"Custom Title\"]"
allowed-tools: Write, Read, Bash, mcp__sequential-thinking__sequentialthinking
---

# Command: Save Artifact

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Capture Claude conversation artifacts and save them to session/task directories with context-aware organization.

**Claude Code MUST execute this workflow:**
1. ✓ Detect artifact type (plan/review/research/analysis/spec/docs/report)
2. ✓ Get current session context
3. ✓ Determine save location (session-level or task-specific)
4. ✓ Extract artifact content with formatting preserved
5. ✓ Generate filename ({type}-{title-slug}.md)
6. ✓ Add metadata headers (artifact_type, created, session_id)
7. ✓ Display confirmation with full path

**Claude Code MUST NOT:**
- ✗ Lose formatting or structure
- ✗ Save to wrong directory (wrong session)
- ✗ Fail silently on save operation

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Capture Claude conversation artifacts (plans, reviews, research, analysis, specs, docs, reports), auto-detect type from context keywords or use explicit type arg, extract content with formatting preservation, generate filename ({type}-{title-slug}.md), determine save location (current task directory if executing task, else session context/), add metadata headers (artifact_type, created, session_id, task_id, status)

**P**urpose: Preserve valuable Claude outputs in session-organized storage, consolidate all session artifacts in one location, enable atomic session cleanup, support both session-level and task-specific artifacts, provide context-aware file organization

**E**xpectation: Artifact saved to Session-{date}-{id}/context/{type}-{title}.md (session-level) or Session-{date}-{id}/Task-XXX--{title}/{type}-{title}.md (task-level) with metadata headers, original formatting preserved, confirmation message with full path, consolidated with other session context files

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% content preservation, Accuracy >90% type detection, Relevance >85% filename quality, Efficiency <5s save operation)

## Purpose

Captures various types of Claude outputs (plans, reviews, research, analysis, specifications, documentation,
reports) and saves them as organized markdown files in the current session directory (`.agent/Session-{date}-{id}/`) with context-aware organization (session-level or task-specific).

## Usage

```bash
/artifact:save [type] [--title="Custom Title"]
```

## Arguments

- `type` (optional): Artifact type to save
  - `plan` - Planning outputs from plan mode
  - `review` - Code, security, or design review outputs
  - `research` - Research and investigation outputs
  - `analysis` - System analysis and diagnostic outputs
  - `spec` - Feature specifications and requirements
  - `docs` - Generated documentation and guides
  - `report` - Status reports and summaries
  - Auto-detected from conversation context if not specified

- `--title="Custom Title"` (optional): Custom title for filename
  - Auto-generated from content if not specified
  - Converted to kebab-case for filename

## Process

1. **Determine artifact type:**
   - Use explicitly provided `type` argument, OR
   - Auto-detect from conversation context using keywords:
     - "plan mode", "planning" → `plan`
     - "review", "code review", "security review" → `review`
     - "research", "investigation", "analyze options" → `research`
     - "analyze", "analysis", "diagnostic" → `analysis`
     - "specification", "requirements", "spec" → `spec`
     - "documentation", "guide", "readme" → `docs`
     - "report", "summary", "status" → `report`
   - Default to `report` if type cannot be determined

2. **Extract content:**
   - Capture relevant Claude output from current conversation
   - For plan mode: Extract plan content
   - For reviews: Extract review findings and recommendations
   - For research: Extract research findings and conclusions
   - Preserve formatting, code blocks, and structure

3. **Detect current context:**
   - Get current session ID via `session_manager.py current`
   - Check if currently executing a task (task_id in context)
   - Determine if this is session-level or task-level artifact

4. **Determine save location:**
   - If task context active: Use task directory via `session_manager.get_task_dir(session_id, task_id, task_title)`
   - Else: Use session context directory via `session_manager.get_context_dir(session_id)`
   - Directory structure:

     ```text
     .agent/Session-{YYYY-MM-DD}-{session-id}/
     ├── context/                          # Session-level artifacts
     │   ├── plan-feature-design.md
     │   ├── review-security-audit.md
     │   └── research-database-options.md
     └── Task-015--refactor-context/       # Task-specific artifacts
         ├── plan-implementation.md
         ├── review-code-quality.md
         └── analysis-performance.md
     ```

5. **Generate filename:**
   - If `--title` provided: Use custom title
   - Otherwise: Extract meaningful title from content (first heading or summary)
   - Format: `{type}-{title-slug}.md` (no date prefix - session already dated)
   - Example: `plan-authentication-feature.md`

6. **Add metadata headers:**

   ```markdown
   ---
   artifact_type: {type}
   created: {YYYY-MM-DD HH:MM:SS}
   session_id: {session_id}
   task_id: {task_id}  # Optional, only for task-level artifacts
   status: draft
   ---
   ```

7. **Save file:**
   - Write to determined location with atomic write for concurrency safety
   - Report saved location to user
   - Confirm successful save with full path

## Explicit Constraints

**IN SCOPE**: Artifact capture from conversation, type detection (7 types: plan, review, research, analysis, spec, docs, report), content extraction with formatting, filename generation (kebab-case), session/task context detection, save location determination (session context/ vs task subdirectory), metadata headers (type, created, session_id, task_id, status), atomic write for concurrency safety, custom title support
**OUT OF SCOPE**: Artifact versioning/history, content editing/modification, cross-project artifact sharing, binary file storage, automatic artifact generation from code, artifact search/indexing, migration of existing .agent/artifacts/ files (manual)

## Agent Integration

- **Primary Agent**: documenter - Handles artifact capture and organization
- **Tools**: Bash for directory operations, Write for file creation, Read for context analysis

## Examples

### Example 1: Save plan with auto-detection (session-level)

```bash
# After creating a plan in plan mode (Shift+Tab twice)
/artifact:save

# Output: Saved to .agent/Session-2025-10-16-d141362d/context/plan-user-authentication.md
```

### Example 2: Save review with explicit type (session-level)

```bash
# After performing a security review
/artifact:save review

# Output: Saved to .agent/Session-2025-10-16-d141362d/context/review-security-audit.md
```

### Example 3: Save research with custom title (task-level)

```bash
# While executing TASK-015 - After researching database options
/artifact:save research --title="Database Comparison Study"

# Output: Saved to .agent/Session-2025-10-16-d141362d/Task-015--refactor-context/research-database-comparison-study.md
```

### Example 4: Save specification (task-level)

```bash
# While executing TASK-022 - After creating feature specification
/artifact:save spec --title="Payment Integration Spec"

# Output: Saved to .agent/Session-2025-10-16-d141362d/Task-022--payment-feature/spec-payment-integration-spec.md
```

## Output

- Confirmation message with full path to saved artifact
- Artifact saved with:
  - Metadata headers (type, created date, project, status)
  - Original content with preserved formatting
  - Organized in type-specific folder
  - Meaningful, searchable filename

## Integration Points

- **Follows**: Any Claude conversation producing valuable artifacts (plans, reviews, research, etc.)
- **Followed by**: Review saved artifacts, share with team, reference in documentation
- **Related**: `/docs:sync`, `/review:code`, `/analyze:potential-issues`, `/speckit:specify`

## Quality Standards

- Preserves original content structure and formatting
- Adds consistent metadata without disrupting readability
- Creates project-specific storage in `.agent/artifacts/`
- Generates meaningful, searchable, dated filenames
- Maintains artifact organization through logical folder structure
- Auto-detection accuracy for common artifact types
- Supports manual override for edge cases

## Artifact Organization

All Claude-generated artifacts are now organized within session directories for consolidated context management:

**Session-Level Artifacts** (`.agent/Session-{date}-{id}/context/`) - General work products from the session:
- **Plans** - Strategic planning outputs, feature plans, implementation strategies
- **Reviews** - Code quality reviews, security audits, design critiques
- **Research** - Technology investigations, option comparisons, feasibility studies
- **Analysis** - System diagnostics, performance analysis, dependency audits
- **Documentation** - Generated guides, README files, documentation
- **Reports** - Status reports, progress summaries

**Task-Level Artifacts** (`.agent/Session-{date}-{id}/Task-XXX--{title}/`) - Task-specific work products:
- **Specifications** - Feature specs created during task execution
- **Plans** - Task-specific implementation plans
- **Reviews** - Code reviews specific to task changes
- **Analysis** - Performance or quality analysis for task scope

**Benefits of Session-Based Organization:**
- Atomic cleanup (delete entire session directory)
- Clear context boundaries (all session work in one place)
- Task isolation (task-specific artifacts separate from general session work)
- No scattered `.agent/artifacts/` files across different type subdirectories

## Migration Note

Artifacts are now saved to session directories instead of `.agent/artifacts/`. Existing artifacts in `.agent/artifacts/` remain accessible but are not automatically migrated. Manual migration recommended when convenient.
