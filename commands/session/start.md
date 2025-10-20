---
description: "Create new project-local session with user-chosen name and optional topic"
argument-hint: "<session-name> [topic]"
allowed-tools: [Bash]
model: inherit
---

# Command: /session:start

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Create a named session in the current project and link the current terminal via TTY detection.

**YOU MUST:**
1. ✓ Parse session-name and optional topic from $ARGUMENTS
2. ✓ Validate session name format (lowercase alphanumeric + hyphens only)
3. ✓ Call Python script: `python3 ~/.claude/scripts/session/session_manager.py start <name> [topic]`
4. ✓ Display confirmation with session name, directory path, and terminal
5. ✓ Inform user that all domain analysts will use this session directory

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Just report what would happen
- ✗ Skip calling the Python script

---

## IMPLEMENTATION FLOW

### Step 1: Parse Arguments
Extract session-name (required) and optional topic from $ARGUMENTS

### Step 2: Validate Format
- Lowercase alphanumeric + hyphens only
- Max 50 characters
- Must be unique in `.agent/.sessions`

### Step 3: Execute Session Creation
```bash
python3 ~/.claude/scripts/session/session_manager.py start <name> [topic]
```

### Step 4: Display Confirmation
Show session name, directory path, and terminal identifier

---

## User Story & Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create new project-local session with user-chosen name via session_manager.py, create Session-{name}/ directory structure with context/ subdirectory and session.env metadata file, link current terminal via TTY detection, optionally label with topic, display session confirmation, inform user all domain analysts will use this session directory

**P**urpose: Enable concurrent session isolation - multiple sessions in same project with separate context directories, support TTY-based terminal linking for multi-terminal workflows, provide human-readable named sessions (not UUIDs), establish clean session boundaries for parallel feature development with strict isolation

**E**xpectation: Named session created and active, Session-{name}/ directory created with context/ subdirectory and session.env (4 fields), current terminal linked via TTY, registry updated with atomic write, confirmation with session name + directory path + optional topic, clear notification that analysts will write to Session-{name}/context/{agent}.md

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% session setup, Accuracy >90% ID generation, Relevance >85% topic labeling, Efficiency <2s creation)

## Purpose

Creates a new named session in the current project and links the current terminal via TTY detection. All domain analyst work in this session will use the session directory for context file organization.

## Usage

```bash
/session:start <session-name> [topic]
```

## Arguments

- `session-name` (required): User-chosen session name
  - Examples: "feature-auth", "bug-validation", "refactor-db"
  - Must be lowercase alphanumeric + hyphens only
  - Max 50 characters
  - Must be unique within project
- `topic` (optional): Human-readable description
  - Examples: "Authentication feature implementation", "Fix validation bug"
  - Stored in session metadata for reference

## Process

1. **Parse Arguments:**
   - Extract session name from `$ARGUMENTS`
   - Extract optional topic
   - If no arguments: prompt interactively

2. **Create Session:**
   - Call `python3 ~/.claude/scripts/session/session_manager.py start <session-name> [topic]`
   - This function:
     * Validates session name format (lowercase alphanumeric + hyphens)
     * Checks uniqueness in `.agent/.sessions` registry
     * Detects current TTY via `os.ttyname(0)`
     * Creates `.agent/Session-{name}/` directory
     * Creates `.agent/Session-{name}/context/` subdirectory
     * Generates `session.env` file with 4 fields:
       - SESSION_ID={name}
       - SESSION_START_DATETIME={ISO 8601 timestamp}
       - SESSION_TOPIC={topic}
       - SESSION_STATUS=active
     * Updates `.agent/.sessions` registry with atomic write
     * Links current TTY to session

3. **Display Session Information:**
   - Show session name
   - Show session directory path
   - Show topic if provided
   - Show linked terminal (TTY)
   - Confirm session is active

4. **Inform User:**
   - All subsequent domain analyst context files will use this session directory
   - Context file pattern: `.agent/Session-{name}/context/{agent-name}.md`
   - Task-specific context: `.agent/Session-{name}/Task-XXX--{title}/{agent-name}.md`
   - Multiple terminals can link to this session via `/session:select`

## Explicit Constraints

**IN SCOPE**: Named session creation, Session-{name}/ directory creation, context/ subdirectory creation, session.env metadata file generation (4 fields only), .agent/.sessions registry management, TTY-based terminal linking, optional topic labeling, session activation confirmation, session name validation, uniqueness checking, atomic registry writes
**OUT OF SCOPE**: Multi-terminal linking (use /session:select), session archiving (use /session:end), analyst context file creation (analysts handle), task subdirectory creation (handled by /task:execute), cross-project session sharing, UUID-based session IDs (legacy), .current_session file management (TTY-based now)

## Error Handling

1. **Session name already exists**:
   ```
   Error: Session 'feature-auth' already exists

   Use /session:select to link to existing session, or choose a different name.
   Available sessions: feature-auth, bug-fix, refactor-db
   ```

2. **Invalid session name**:
   ```
   Error: Invalid session name 'Feature_Auth'

   Session names must be lowercase alphanumeric + hyphens only.
   Valid examples: feature-auth, bug-validation, refactor-db
   ```

3. **Non-interactive mode (TTY detection failed)**:
   ```
   Error: Cannot create session in non-interactive mode (TTY detection failed)

   This command requires an interactive terminal.
   ```

## Examples

### Example 1: Create session with topic

```bash
/session:start feature-auth "Authentication feature implementation"

# Output:
# Created session: feature-auth
# Topic: Authentication feature implementation
# Terminal: ttys001 linked
# Context: .agent/Session-feature-auth/context/
```

### Example 2: Create session without topic

```bash
/session:start bug-validation

# Output:
# Created session: bug-validation
# Terminal: ttys001 linked
# Context: .agent/Session-bug-validation/context/
```

### Example 3: Interactive creation (no arguments)

```bash
/session:start

# Shows session name suggestions (generated from optional topic prompt):
# Session Name Suggestions:
#
# | Option | Session Name | Type | Description |
# |--------|--------------|------|-------------|
# | A | `auth-feature-impl` | Direct | Straightforward (18 chars) |
# | B | `implement-auth-feature` | Contextual | With action context (22 chars) |
# | C | `auth-feature` | Abstract | Domain-based (12 chars) |
# | Custom | [enter your own] | Manual | Provide custom name |
# | Skip | Cancel | - | Exit without creating |
#
# Your choice: A
# Enter topic (optional): Authentication feature implementation
#
# Output:
# ✓ Created session: auth-feature-impl
# Topic: Authentication feature implementation
# Terminal: ttys001 linked
# Context: .agent/Session-auth-feature-impl/context/
```

## Output

- Confirmation message with session name
- Topic if provided
- Linked terminal (TTY identifier)
- Session directory path
- Active session status

## Integration Points

- **Precedes**: Any work requiring domain analyst coordination with context file tracking
- **Followed by**: `/session:end` when work is complete, or `/session:select` from other terminals
- **Related**: All domain analyst commands that persist findings to `.agent/Session-{name}/context/`

## Quality Standards

- Validates session names (lowercase alphanumeric + hyphens)
- Ensures uniqueness within project
- Atomic registry writes (concurrency-safe)
- TTY-based terminal linking (cross-platform)
- Provides clear confirmation of session activation
- Cross-platform compatibility via Python stdlib

## Session Workflow

**Typical Usage Pattern:**

1. Start new session: `/session:start feature-auth "Authentication feature"`
2. Execute commands using domain analysts (they auto-detect session via TTY)
3. Domain analysts create context files in session directory
4. Optionally link more terminals: `/session:select` from other terminals
5. Complete work
6. End session: `/session:end` (with cleanup options)

**TTY-Based Session Detection:**

All domain analysts automatically use the current session directory via TTY lookup:

- `python3 ~/.claude/scripts/session/session_manager.py current` returns session name for current terminal
- `python3 ~/.claude/scripts/session/session_manager.py context_dir` returns context directory (task-aware routing)
- Context files: `.agent/Session-{name}/context/{agent-name}.md`
- Task-specific files: `.agent/Session-{name}/Task-XXX--{title}/{agent-name}.md`
- No manual session tracking needed - TTY-based detection is automatic

## Session Isolation Validation (T023)

After creating session, the system validates:
- Registry tracks session separately from other sessions
- Session directory is independent (`.agent/Session-{name}/`)
- TTY is linked only to this session (not others)
- No context cross-contamination between sessions

## Related Commands

- `/session:select` - Link current terminal to existing session
- `/session:list` - Show all active sessions
- `/session:info` - Show current session details
- `/session:end` - End session with cleanup options
