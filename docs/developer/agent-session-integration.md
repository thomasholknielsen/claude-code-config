# Agent Session Integration

## Problem: Cross-Process Session Detection

Agents run in **separate Claude processes** with different process trees, so they cannot detect the parent session via GPPID (grandparent process ID).

### Symptom

```bash
# Agent tries to get current session
python3 session_manager.py current
# Returns empty - agent's GPPID is different from main thread
```

## Solution: Environment Variable Fallback

The session manager now supports `CLAUDE_SESSION` environment variable for cross-process session sharing.

### Implementation

**Main Thread Responsibility** (before invoking agents):

```bash
# 1. Get current session
SESSION=$(python3 ~/.claude/scripts/session/session_manager.py current)

# 2. Export for child processes
export CLAUDE_SESSION="$SESSION"

# 3. Now invoke agents - they'll inherit CLAUDE_SESSION
```

**Agent Behavior**:

- Agents automatically check `CLAUDE_SESSION` environment variable first
- Falls back to GPPID detection if env var not set
- No changes needed to agent code

### Agent Prompt Pattern

When invoking agents from commands, include this setup:

1. Get current session:

   ```bash
   SESSION=$(python3 ~/.claude/scripts/session/session_manager.py current)
   export CLAUDE_SESSION="$SESSION"
   ```

2. Invoke agent with Task tool:

   ```python
   Task(subagent_type="<agent-name>", prompt="...")
   ```

3. Agent will automatically use CLAUDE_SESSION for context routing

## Command Integration

### `/task:execute` Command

Already includes session check at step 1:

1. **Check Active Session** (REQUIRED):
   - Call: `python3 ~/.claude/scripts/session/session_manager.py current`
   - If empty: Prompt user to start/link session
   - If exists: Export CLAUDE_SESSION before invoking agents

### Workflow Commands

Any command that invokes agents should:

1. Check for active session first
2. Export CLAUDE_SESSION before agent invocation
3. Agents will inherit the environment variable

## Testing

```bash
# Terminal 1: Start session
/session:start test-session "Test"

# Verify session
python3 ~/.claude/scripts/session/session_manager.py current
# Output: test-session

# Export for testing
export CLAUDE_SESSION="test-session"

# Now agents will detect the session
python3 ~/.claude/scripts/session/session_manager.py context_dir
# Output: .agent/Session-test-session/context
```

## Architecture

```text
Main Thread (GPPID: 12345)
  - Session detected via GPPID → "my-session"
  - Export CLAUDE_SESSION="my-session"
  - Spawn Agent (GPPID: 67890 - different!)
    - Check CLAUDE_SESSION env var → "my-session" ✅
    - Fall back to GPPID → different, no match ❌
    - Uses env var session for context routing
```

## Migration Path

### Current State (Broken)

- Agents can't detect parent session
- Fall back to creating legacy UUID sessions
- Context files go to wrong directories

### Fixed State

- Main thread exports CLAUDE_SESSION
- Agents detect session via env var
- Context files route correctly to session/task directories

## Related

- `/session:start` - Creates named session
- `/session:select` - Links terminal to session
- `session_manager.py current` - Gets active session
- Task-aware routing (`copy_task`, `set_task`)
