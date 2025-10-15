---
description: "Start a new session with optional topic label for context file organization"
argument-hint: "[topic]"
allowed-tools: Bash, mcp__sequential-thinking__sequentialthinking
---

# Command: Start Session

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create new 8-character UUID session ID via session_manager.py, overwrite .current_session file, optionally label with topic for human reference (not in filenames), display session ID + topic confirmation, inform user all domain analysts will use this session ID for context files

**P**urpose: Enable organized context file tracking across domain analyst work, support session-based workflow separation (feature work, bug fixes, refactoring), provide human-readable topic labels while maintaining unique ID, establish clean session boundaries for parallel work streams

**E**xpectation: New session ID created and active, .current_session file updated, confirmation with session ID + optional topic, clear notification that analysts will use this session for context (.agent/context/{YYYY-MM-DD}-{topic}-{sessionid}.md)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% session setup, Accuracy >90% ID generation, Relevance >85% topic labeling, Efficiency <2s creation)

## Purpose

Creates a new session ID and optionally labels it with a topic for organized context file tracking. All domain analyst work in this session will use the new session ID for context file naming.

## Usage

```bash
/session:start [topic]
```

## Arguments

- `topic` (optional): Descriptive label for this session's work
  - Examples: "authentication-feature", "bug-fix-api", "refactoring-cleanup"
  - Used for human-readable reference only (not in filenames)
  - Session ID remains the unique identifier

## Process

1. **Generate New Session ID:**
   - Call `session_manager.py new [topic]` to create 8-character UUID
   - Overwrites `.current_session` file

2. **Display Session Information:**
   - Show new session ID
   - Show topic label if provided
   - Confirm session is active

3. **Inform User:**
   - All subsequent domain analyst context files will use this session ID
   - Context file pattern: `.agent/context/{YYYY-MM-DD}-{topic}-{sessionid}.md`

## Explicit Constraints

**IN SCOPE**: Session ID generation (8-char UUID), .current_session file management, optional topic labeling, session activation confirmation, context file path notification
**OUT OF SCOPE**: Session history tracking, multi-session management (only 1 active session), session archiving (use /session:end), context file creation (analysts handle), session persistence across restarts

## Agent Integration

- **Tools**: Bash for session_manager.py execution
- **No Domain Analysts**: This is a simple utility command

## Examples

### Example 1: Start session without topic

```bash
/session:start

# Output:
# Created new session: a3f8b2c1
# Session is now active.
# Domain analysts will use this session ID for context files.
```

### Example 2: Start session with topic

```bash
/session:start authentication-feature

# Output:
# Created new session: d7e4a9f2 (topic: authentication-feature)
# Session is now active.
# Domain analysts will use this session ID for context files.
```

### Example 3: Start session for bug fix

```bash
/session:start bug-fix-payment-validation

# Output:
# Created new session: 9c2b5f1a (topic: bug-fix-payment-validation)
# Session is now active.
# Domain analysts will use this session ID for context files.
```

## Output

- Confirmation message with session ID
- Topic label if provided
- Active session status

## Integration Points

- **Precedes**: Any work requiring domain analyst coordination with context file tracking
- **Followed by**: `/session:end` when work is complete
- **Related**: All domain analyst commands that persist findings to `.agent/context/`

## Quality Standards

- Generates unique 8-character session IDs
- Overwrites previous session cleanly
- Maintains session state in `.current_session` file
- Provides clear confirmation of session activation
- Cross-platform compatibility via Python script

## Session Workflow

**Typical Usage Pattern:**

1. Start new session: `/session:start feature-name`
2. Execute commands using domain analysts (they read session ID automatically)
3. Domain analysts create context files with session ID
4. Complete work
5. End session: `/session:end` (optional cleanup)

**Session ID Usage:**

All domain analysts automatically use the current session ID when creating context files:

- `python3 ~/.claude/scripts/session/session_manager.py current` returns active session ID
- Context files: `.agent/context/2025-10-06-{topic}-{sessionid}.md`
- No manual session ID tracking needed
