---
description: "End current session and optionally archive context files for future reference"
argument-hint: "[--archive]"
allowed-tools: Bash, Read, Glob
---

# Command: End Session

## Purpose

Ends the current session by displaying session summary and optionally archiving context files. Prepares for starting a new session with clean context.

## Usage

```bash
/session:end [--archive]
```

## Arguments

- `--archive` (optional): Move context files to organized archive
  - Archives to: `.agent/context/archive/{YYYY-MM-DD}-{sessionid}/`
  - Preserves all context files created during this session
  - Default: Context files remain in `.agent/context/` (rotated by creation date)

## Process

1. **Read Current Session:**
   - Get session ID from `.current_session`
   - Display current session ID and duration

2. **List Session Context Files:**
   - Find all `.agent/context/*-{sessionid}.md` files
   - Display count and total size
   - List context file topics created during session

3. **Archive (if --archive flag):**
   - Create archive directory: `.agent/context/archive/{YYYY-MM-DD}-{sessionid}/`
   - Move all session context files to archive
   - Display archive location

4. **Session Summary:**
   - Session ID
   - Context files created
   - Archive status
   - Ready for new session

5. **Cleanup:**
   - Session file remains (will be overwritten by next `/session:start`)
   - User can start new session immediately

## Agent Integration

- **Tools**: Bash for file operations, Read for session file, Glob for finding context files
- **No Domain Analysts**: This is a simple utility command

## Examples

### Example 1: End session without archiving

```bash
/session:end

# Output:
# Session a3f8b2c1 ended.
# Context files created: 3
#   - 2025-10-06-cleanup-quality-a3f8b2c1.md
#   - 2025-10-06-cleanup-readability-a3f8b2c1.md
#   - 2025-10-06-security-audit-a3f8b2c1.md
#
# Context files remain in .agent/context/ for reference.
# Ready to start new session with /session:start
```

### Example 2: End session with archiving

```bash
/session:end --archive

# Output:
# Session d7e4a9f2 ended.
# Context files created: 5
#   - 2025-10-06-authentication-design-d7e4a9f2.md
#   - 2025-10-06-security-review-d7e4a9f2.md
#   - 2025-10-06-api-analysis-d7e4a9f2.md
#   - 2025-10-06-database-schema-d7e4a9f2.md
#   - 2025-10-06-testing-strategy-d7e4a9f2.md
#
# Archived to: .agent/context/archive/2025-10-06-d7e4a9f2/
# Ready to start new session with /session:start
```

### Example 3: End session with no context files

```bash
/session:end

# Output:
# Session 9c2b5f1a ended.
# No context files created during this session.
# Ready to start new session with /session:start
```

## Output

- Session ID and summary
- List of context files created
- Archive location (if --archive used)
- Ready status for new session

## Integration Points

- **Follows**: Completed work session with domain analyst coordination
- **Preceded by**: `/session:start` at beginning of work
- **Related**: All domain analyst commands that created context files

## Quality Standards

- Non-destructive by default (files remain for reference)
- Optional archiving for organized long-term storage
- Clear summary of session work
- Maintains context file integrity
- Cross-platform file operations

## Session Lifecycle

**Complete Session Workflow:**

1. **Start:** `/session:start feature-implementation`
2. **Work:** Execute commands, domain analysts create context files
3. **Review:** Check `.agent/context/` for analyst findings
4. **End:** `/session:end` or `/session:end --archive`
5. **Restart:** `/session:start next-feature`

**Context File Management:**

- **No Archive**: Files stay in `.agent/context/` indefinitely
  - Good for: Ongoing reference, recent work
  - Cleanup: Manual review and deletion when needed

- **With Archive**: Files moved to timestamped archive
  - Good for: Completed features, long-term storage
  - Organization: Easy to find historical analysis by date/session

## Notes

- Session file (`.current_session`) is not deleted, just ready for next session
- Archive directories use date + session ID for unique naming
- Context files use session ID in filename for easy identification
- Archiving is optional - only use when session work is truly complete
