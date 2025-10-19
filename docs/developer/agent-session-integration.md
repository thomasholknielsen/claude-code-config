# Agent Session Integration

## Problem: Cross-Process Session Detection

Agents run in **separate Claude processes** with different process trees, so they cannot detect the parent session via GPPID (grandparent process ID).

### Symptom

```bash
# Agent tries to get current session from parent GPPID
python3 session_manager.py current
# Returns empty - agent's GPPID is different from main thread
```

## Solution: Explicit Path Passing

Agents receive context file paths explicitly in the prompt, avoiding environment variable collisions and multi-terminal issues.

### Implementation

**Main Thread Responsibility** (before invoking agents):

```bash
# 1. Get context directory for current session
CONTEXT_DIR=$(python3 ~/.claude/scripts/session/session_manager.py context_dir)

# 2. Pass explicit path in agent prompt (no environment variable needed)
# 3. Agent writes findings to the provided path
```

**Agent Behavior**:

- Agents receive context file path in the prompt
- Write findings to the provided location
- No need to detect session or use environment variables

### Agent Prompt Pattern

When invoking agents from commands, use this pattern:

```python
CONTEXT_DIR=$(python3 ~/.claude/scripts/session/session_manager.py context_dir)

Task(
  subagent_type="<agent-name>",
  prompt="<analysis task>

  **Context File Location**: Save your findings to:
  {CONTEXT_DIR}/<agent-name>.md

  Do NOT attempt to detect session - use the path provided above."
)
```

**Key Points**:

- Get context directory once in main thread
- Pass absolute path to agent
- Agent writes directly to provided location
- No environment variable needed

## Command Integration

### `/task:execute` Command

Already includes session context setup:

1. **Check Active Session** (REQUIRED):
   - Call: `python3 ~/.claude/scripts/session/session_manager.py context_dir`
   - If empty: Prompt user to start/link session
   - If exists: Pass path to agent in prompt

### Workflow Commands

Any command that invokes agents should:

1. Check for active session: `python3 ~/.claude/scripts/session/session_manager.py context_dir`
2. Pass explicit path in agent prompt
3. Agents write to provided location directly

## Testing

```bash
# Terminal 1: Start session
/session:start test-session "Test"

# Verify session context path
python3 ~/.claude/scripts/session/session_manager.py context_dir
# Output: /path/to/project/.agent/Session-test-session/context

# Pass this path to agents in prompts
# Agent will write findings to: /path/to/project/.agent/Session-test-session/context/<agent-name>.md
```

## Architecture

```text
Main Thread
  - Get context dir: .agent/Session-{name}/context
  - Spawn Agent with prompt containing path
    - Receives explicit path: {CONTEXT_DIR}/<agent-name>.md
    - Writes findings to exact location
    - No GPPID detection needed ✅
    - No environment variables needed ✅
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
