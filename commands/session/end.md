---
description: "End current session and optionally archive context files for future reference"
argument-hint: "[--archive]"
allowed-tools: Bash, Read, Glob, mcp__sequential-thinking__sequentialthinking
---

# Command: End Session

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** End the current session by displaying a summary and providing interactive cleanup options.

**YOU MUST:**
1. ✓ Get current session via `python ~/.claude/scripts/session/session_manager.py current`
2. ✓ Display session summary (started, topic, context files, tasks created)
3. ✓ Present interactive A/B/C cleanup prompt (Delete/Archive/Keep/Skip)
4. ✓ Execute cleanup action based on user choice
5. ✓ Display confirmation of action taken

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Delete session without user confirmation
- ✗ Skip the interactive prompt

---

## IMPLEMENTATION FLOW

### Step 1: Get Current Session
```bash
python ~/.claude/scripts/session/session_manager.py current
```

### Step 2: Build & Display Summary
Show session metadata: name, started timestamp, topic, context file count, task directories

### Step 3: Present Interactive Cleanup Prompt
Show A/B/C table format (Delete/Archive/Keep/Skip options)

### Step 4: Execute Cleanup
Call appropriate cleanup function based on user selection

### Step 5: Confirm Action
Display confirmation with action taken

---

## End Session Options

| Option | Action | Recommendation |
|--------|--------|-----------------|
| **A** | Archive session for future reference | **← Recommended** for preserving analysis history |
| **B** | Delete session completely | When session was temporary or exploratory |
| **C** | Keep session active for later | For work-in-progress needing continuation |

Your choice (A/B/C)?

## Next Steps

| Step | Action | Details |
|------|--------|---------|
| 1 | Review session findings and context | Summarize analysis and decisions made |
| 2 | Archive session metadata if selected | Preserve for future reference or auditing |
| 3 | Create final session summary report | Document outcomes and next steps |
| 4 | Start new session or review archived | Continue work or begin new analysis |

What would you like to do next?

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Display current session summary (session ID, started timestamp, topic, context files created, task directories created), present interactive A/B/C cleanup prompt (Delete/Archive/Keep/Skip), execute cleanup_session(session_id, action) based on user choice, update session.md status field accordingly, confirm final action taken

**P**urpose: Gracefully conclude work sessions with user control over session lifecycle, support three cleanup strategies (atomic delete, archive for reference, keep active), provide clear session summary before cleanup, enable organized session management with explicit user choice

**E**xpectation: Session summary displayed with context file count and task directory count, interactive A/B/C table prompt presented, cleanup action executed based on user choice (delete → directory removed, archive → moved to .agent/archive/, keep → marked completed), confirmation message with action taken and next steps

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% session summary, Accuracy >90% cleanup execution, Relevance >85% prompt clarity, Efficiency <5s operation)

## Purpose

Ends the current session by displaying session summary and providing interactive cleanup options. Supports three cleanup strategies: delete (atomic removal), archive (preserve for reference), or keep (mark completed).

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
/session:end [--archive]
```

## Arguments

- `--archive` (optional, DEPRECATED): Use interactive prompt instead
  - If provided: Automatically selects "Archive" option
  - Recommended: Use interactive prompt for explicit choice

## Process

1. **Read Current Session:**
   - Get session ID via `session_manager.py current`
   - Get session directory via `session_manager.py` using `get_session_dir(session_id)`
   - Read session.md metadata for session details

2. **Display Session Summary:**
   - Session ID
   - Started timestamp (from session.md)
   - Topic (from session.md)
   - Status (from session.md)
   - Context files created (count files in Session-{date}-{id}/context/)
   - Task directories created (count Task-XXX--* subdirectories)
   - List of agents invoked (from session.md or context file listing)

3. **Present Interactive Cleanup Prompt:**
   - Show A/B/C table format with cleanup options:
     * **A (Delete)**: Permanently remove session directory recursively
     * **B (Archive)**: Move Session-{date}-{id}/ to .agent/archive/ and update status to "archived"
     * **C (Keep)**: Mark session.md status as "completed" but leave directory active
     * **Skip**: Exit without cleanup
   - If `--archive` flag provided: Auto-select option B
   - Validate user input (A/B/C/Skip, case-insensitive)

4. **Execute Cleanup Action:**
   - **Delete (A)**: Call `session_manager.cleanup_session(session_id, "delete")`
     * Removes Session-{date}-{id}/ directory recursively
     * Confirmation: "Session {id} deleted. All files removed."
   - **Archive (B)**: Call `session_manager.cleanup_session(session_id, "archive")`
     * Moves to .agent/archive/Session-{date}-{id}/
     * Updates session.md status to "archived"
     * Confirmation: "Session {id} archived to .agent/archive/Session-{date}-{id}/"
   - **Keep (C)**: Call `session_manager.cleanup_session(session_id, "keep")`
     * Updates session.md status to "completed"
     * Leaves directory in .agent/
     * Confirmation: "Session {id} marked as completed (kept active)"
   - **Skip**: No action taken
     * Confirmation: "Session cleanup cancelled. Session remains active."

5. **Next Steps:**
   - Ready to start new session with `/session:start`

## Explicit Constraints

**IN SCOPE**: Session summary display (session ID, timestamps, topic, status, file counts), interactive A/B/C cleanup prompt, cleanup_session() execution (delete/archive/keep), session.md status updates, .current_session preservation, --archive flag backward compatibility
**OUT OF SCOPE**: Automatic cleanup decisions (user must choose), permanent session history tracking (no central registry), session recovery after deletion, cross-session context merging, multi-session cleanup (one at a time)

## Agent Integration

- **Tools**: Bash for session_manager.py execution, Read for session.md parsing, Glob for context file discovery
- **No Domain Analysts**: This is a simple utility command

## Examples

### Example 1: End session with interactive prompt (Delete)

```bash
/session:end

# Output:
# Session Summary:
# - Session ID: a3f8b2c1
# - Started: 2025-10-16 09:23:14
# - Topic: feature-implementation
# - Status: active
# - Context files: 3 (architecture-analyst.md, security-analyst.md, performance-analyst.md)
# - Task directories: 2 (Task-015--refactor-context, Task-022--add-validation)
#
# ## How would you like to handle this session?
#
# | Option | Action | Effect |
# |--------|--------|--------|
# | A | Delete session | Permanently remove Session-2025-10-16-a3f8b2c1/ directory |
# | B | Archive session | Move to .agent/archive/Session-2025-10-16-a3f8b2c1/ |
# | C | Keep session | Mark as completed but leave in .agent/ |
# | Skip | Cancel | No changes, session remains active |
#
# Your choice: A
#
# Session a3f8b2c1 deleted. All files removed.
# Ready to start new session with /session:start
```

### Example 2: End session with --archive flag (Auto-select Archive)

```bash
/session:end --archive

# Output:
# Session Summary:
# - Session ID: d7e4a9f2
# - Started: 2025-10-16 14:45:32
# - Topic: authentication-feature
# - Status: active
# - Context files: 5
# - Task directories: 1
#
# Auto-selecting Archive (--archive flag provided)
#
# Session d7e4a9f2 archived to .agent/archive/Session-2025-10-16-d7e4a9f2/
# Ready to start new session with /session:start
```

### Example 3: End session and keep (Mark completed)

```bash
/session:end

# Output:
# Session Summary:
# - Session ID: 9c2b5f1a
# - Started: 2025-10-16 16:12:08
# - Topic: bug-fix-validation
# - Status: active
# - Context files: 2
# - Task directories: 0
#
# ## How would you like to handle this session?
#
# | Option | Action | Effect |
# |--------|--------|--------|
# | A | Delete session | Permanently remove Session-2025-10-16-9c2b5f1a/ directory |
# | B | Archive session | Move to .agent/archive/Session-2025-10-16-9c2b5f1a/ |
# | C | Keep session | Mark as completed but leave in .agent/ |
# | Skip | Cancel | No changes, session remains active |
#
# Your choice: C
#
# Session 9c2b5f1a marked as completed (kept active)
# Session directory: .agent/Session-2025-10-16-9c2b5f1a/
# Ready to start new session with /session:start
```

### Example 4: End session and skip cleanup

```bash
/session:end

# (After displaying session summary and prompt)
#
# Your choice: Skip
#
# Session cleanup cancelled. Session remains active.
```

## Output

- Session summary with file/directory counts
- Interactive A/B/C cleanup prompt (unless --archive flag)
- Cleanup action confirmation
- Ready status for new session

## Integration Points

- **Follows**: Completed work session with domain analyst coordination and task execution
- **Preceded by**: `/session:start` at beginning of work
- **Related**: All domain analyst commands and `/task:execute` that created session files

## Quality Standards

- User-controlled cleanup (explicit choice required)
- Three lifecycle options: delete (atomic), archive (preserve), keep (reference)
- Clear session summary before cleanup decision
- Safe default (Skip option always available)
- Cross-platform file operations via session_manager.py
- Backward compatible with --archive flag

## Session Lifecycle

**Complete Session Workflow:**

1. **Start:** `/session:start feature-implementation`
2. **Work:** Execute commands, domain analysts create context files, tasks create subdirectories
3. **Review:** Check `.agent/Session-{date}-{id}/` for analyst findings and task artifacts
4. **End:** `/session:end` with interactive cleanup choice
5. **Restart:** `/session:start next-feature`

**Cleanup Strategy Guide:**

- **Delete (Option A)**: Completed, no future reference needed
  - Use when: Session work fully integrated, no historical value
  - Effect: Atomic removal of entire Session-{date}-{id}/ directory
  - Pros: Clean slate, minimal disk usage
  - Cons: Irreversible, loses all session context

- **Archive (Option B)**: Completed, preserve for reference
  - Use when: Session work complete, may need historical reference
  - Effect: Moves to .agent/archive/Session-{date}-{id}/
  - Pros: Organized long-term storage, easy to find by date
  - Cons: Disk usage grows over time

- **Keep (Option C)**: Ongoing reference needed
  - Use when: Session context still relevant, iterative work
  - Effect: Marks session.md status="completed" but leaves in .agent/
  - Pros: Immediate access, no file movement
  - Cons: Active directory grows with completed sessions

## Notes

- Session file (`.current_session`) is preserved (overwritten by next `/session:start`)
- Archive directories maintain Session-{date}-{id}/ naming for uniqueness
- Cleanup actions are atomic (delete all or nothing)
- --archive flag provides backward compatibility with old usage pattern
- Invalid input re-prompts once, then defaults to Skip
