#!/usr/bin/env python3
"""
Session Manager for Claude Code
Cross-platform session ID generation and management with context directory support
"""

from datetime import datetime
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


# Constants
SESSION_ID_LENGTH = 8  # Length of generated session IDs (first 8 chars of UUID)


# Terminal Identification (T001 - Updated for non-TTY contexts)


def get_terminal_identifier():
    """
    Get stable terminal identifier using grandparent process PID.

    Works in both TTY and non-TTY contexts (Claude Code Bash execution).
    Cross-platform: macOS, Linux, WSL, Git Bash on Windows.

    Returns:
        str: Terminal identifier (e.g., "claude-86258") or None if detection fails

    Platform Examples:
        - macOS: "claude-86258" (Claude Code process PID)
        - Linux: "claude-12345"
        - Windows (Git Bash): "claude-67890"

    Example:
        >>> identifier = get_terminal_identifier()
        >>> print(identifier)  # "claude-86258"
    """
    try:
        # Get parent process ID
        ppid = os.getppid()

        # Defensive validation - ensure ppid is valid
        if not str(ppid).isdigit():
            return None

        # Use ps command to get grandparent PID (Claude Code process)
        # This is stable across all commands in same terminal session
        result = subprocess.run(["ps", "-p", str(ppid), "-o", "ppid="], capture_output=True, text=True, timeout=1)

        if result.returncode == 0:
            gppid = result.stdout.strip()
            if gppid:
                return f"claude-{gppid}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        # ps command not available or timeout
        pass

    return None


# Sessions Registry Functions (T004)


def load_sessions_registry():
    """
    Load sessions registry from project-local .agent/.sessions file.

    Returns:
        dict: Registry structure with "sessions" key, or empty structure if doesn't exist

    Format:
        {
          "sessions": {
            "feature-auth": {
              "topic": "Authentication feature implementation",
              "started": "2025-10-16T14:30:00",
              "status": "active",
              "terminals": ["ttys001", "ttys003"]
            }
          }
        }

    Example:
        >>> registry = load_sessions_registry()
        >>> sessions = registry["sessions"]
    """
    registry_path = Path.cwd() / ".agent" / ".sessions"

    if not registry_path.exists():
        # Return empty registry structure
        return {"sessions": {}}

    try:
        with registry_path.open() as f:
            registry = json.load(f)
            # Ensure sessions key exists
            if "sessions" not in registry:
                registry["sessions"] = {}
            return registry
    except (json.JSONDecodeError, OSError) as e:
        # Corrupted registry - return empty structure
        print(f"Warning: Could not load sessions registry: {e}")
        return {"sessions": {}}


def save_sessions_registry(registry):
    """
    Save sessions registry to project-local .agent/.sessions file with atomic write.

    Args:
        registry: dict with "sessions" key containing session metadata

    Example:
        >>> registry = load_sessions_registry()
        >>> registry["sessions"]["new-feature"] = {...}
        >>> save_sessions_registry(registry)
    """
    registry_path = Path.cwd() / ".agent" / ".sessions"

    # Ensure .agent directory exists
    registry_path.parent.mkdir(parents=True, exist_ok=True)

    # Serialize to JSON with pretty printing
    content = json.dumps(registry, indent=2)

    # Write atomically (temp file + rename)
    atomic_write(registry_path, content)


# Helper Functions


def sanitize_task_title(title, max_length=50):
    """
    Sanitize task title for safe directory naming.

    Args:
        title: Raw task title string
        max_length: Maximum length of sanitized title (default: 50)

    Returns:
        Sanitized title (lowercase, alphanumeric + hyphens only)

    Example:
        "Fix login validation error!" -> "fix-login-validation-error"
    """
    if not title:
        return ""

    # Remove special characters except hyphens and alphanumeric
    sanitized = re.sub(r"[^a-zA-Z0-9\s-]", "", title)

    # Convert spaces to hyphens
    sanitized = sanitized.replace(" ", "-")

    # Convert to lowercase
    sanitized = sanitized.lower()

    # Remove consecutive hyphens
    sanitized = re.sub(r"-+", "-", sanitized)

    # Strip leading/trailing hyphens
    sanitized = sanitized.strip("-")

    # Truncate to max_length
    return sanitized[:max_length]


def atomic_write(target_path, content):
    """
    Write content to target_path atomically using temp file + rename.

    Args:
        target_path: Path object or string for target file
        content: String content to write

    Raises:
        OSError: If write operation fails
    """
    target_path = Path(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # Create temp file in same directory as target
    temp_fd, temp_path = tempfile.mkstemp(dir=target_path.parent, text=True)

    try:
        # Write content to temp file using file descriptor
        with os.fdopen(temp_fd, "w") as f:
            f.write(content)

        # Atomic rename (POSIX standard, works on Windows/macOS/Linux)
        Path(temp_path).replace(target_path)
    except Exception:
        # Clean up temp file on error
        Path(temp_path).unlink(missing_ok=True)
        raise


def get_session_file():
    """Get path to session file (cross-platform)"""
    claude_dir = Path.home() / ".claude"
    claude_dir.mkdir(exist_ok=True)
    return claude_dir / ".current_session"


def get_context_base_dir():
    """
    Get base .agent directory (project-local).

    Updated for T005: Changed from user-global (~/.claude/.agent) to project-local.

    Returns:
        Path: Project-local .agent directory (Path.cwd() / ".agent")
    """
    agent_dir = Path.cwd() / ".agent"
    agent_dir.mkdir(parents=True, exist_ok=True)
    return agent_dir


# Core Session Operations (T006-T015 - Phase 2 Foundational)


def create_session(session_name, topic=""):
    """
    Create new session and link current terminal (T006).

    Args:
        session_name: User-chosen session name (e.g., "feature-auth")
        topic: Optional human-readable description

    Returns:
        str: Session name (same as input)

    Raises:
        ValueError: If session name is invalid or already exists
        RuntimeError: If TTY detection fails (non-interactive mode)

    Example:
        >>> create_session("feature-auth", "Authentication feature")
        "feature-auth"
    """
    # Validate session name (T017)
    if not session_name:
        raise ValueError("Session name cannot be empty")

    if not re.match(r"^[a-z0-9-]+$", session_name):
        raise ValueError(
            f"Invalid session name '{session_name}'. "
            "Must be lowercase alphanumeric + hyphens only (e.g., 'feature-auth')"
        )

    if len(session_name) > 50:
        raise ValueError(f"Session name too long (max 50 chars): {session_name}")

    # Check uniqueness (T017)
    registry = load_sessions_registry()
    if session_name in registry["sessions"]:
        raise ValueError(f"Session '{session_name}' already exists")

    # Get terminal identifier (T021)
    terminal_id = get_terminal_identifier()
    if terminal_id is None:
        raise RuntimeError("Cannot detect terminal identifier")

    # Create session directory structure (T019)
    session_dir = Path.cwd() / ".agent" / f"Session-{session_name}"
    session_dir.mkdir(parents=True, exist_ok=True)
    (session_dir / "context").mkdir(exist_ok=True)

    # Create session.md metadata file (consolidates session.env + session.md)
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # ISO 8601 format
    session_md_content = f"""# Session: {session_name}

**Started**: {timestamp}
**Topic**: {topic if topic else "(no topic)"}
**Status**: active
**Current Task**: (none)
"""
    atomic_write(session_dir / "session.md", session_md_content)

    # Add to registry with atomic write (T020)
    registry["sessions"][session_name] = {
        "topic": topic,
        "started": timestamp,
        "status": "active",
        "terminals": [terminal_id],
    }
    save_sessions_registry(registry)

    print(f"Created session: {session_name}")
    if topic:
        print(f"Topic: {topic}")

    return session_name


def get_session_for_terminal():
    """
    Find which session current terminal is linked to (T007).

    Returns:
        str | None: Session name if terminal is linked, None otherwise

    Example:
        >>> get_session_for_terminal()
        "feature-auth"  # or None
    """
    terminal_id = get_terminal_identifier()
    if terminal_id is None:
        return None

    registry = load_sessions_registry()

    # Terminal-based session lookup (T021)
    for session_name, session_data in registry["sessions"].items():
        if terminal_id in session_data.get("terminals", []):
            return session_name

    return None


def select_session(session_name):
    """
    Link current terminal to existing session (T008).

    Args:
        session_name: Session name to link to

    Raises:
        ValueError: If session doesn't exist
        RuntimeError: If terminal detection fails

    Example:
        >>> select_session("feature-auth")
    """
    terminal_id = get_terminal_identifier()
    if terminal_id is None:
        raise RuntimeError("Cannot detect terminal identifier")

    registry = load_sessions_registry()

    if session_name not in registry["sessions"]:
        raise ValueError(f"Session '{session_name}' not found")

    # Add terminal ID to session's terminals list (T025 - duplicate check)
    session = registry["sessions"][session_name]
    if terminal_id not in session["terminals"]:
        session["terminals"].append(terminal_id)
        print(f"Linked terminal to session: {session_name}")
    else:
        print(f"Terminal already linked to session: {session_name}")

    save_sessions_registry(registry)


def copy_task_to_session(task_id, task_content):
    """
    Copy task entity to session task directory (T011).

    Args:
        task_id: Task ID (e.g., "TASK-015")
        task_content: Full task markdown section from tasks.md

    Returns:
        Path: Path to created task.md file

    Raises:
        ValueError: If task_id doesn't match pattern TASK-\\d{3}
        RuntimeError: If no active session for current terminal

    Example:
        >>> content = "## TASK-015: Implement auth\n..."
        >>> copy_task_to_session("TASK-015", content)
        Path('.agent/Session-feature-auth/Task-015--implement-auth/task.md')
    """
    # Validate task_id format
    if not re.match(r"^TASK-\d{3}$", task_id):
        raise ValueError(f"Invalid task_id '{task_id}'. Must match TASK-XXX pattern (e.g., TASK-015)")

    session_name = get_session_for_terminal()
    if session_name is None:
        raise RuntimeError("No active session for current terminal")

    # Extract task title from content (T039)
    title_match = re.search(r"^##\s+\[TASK-\d{3}\]\s+(.+)$", task_content, re.MULTILINE)
    task_title = title_match.group(1) if title_match else "untitled"

    # Create task directory (T040)
    session_dir = Path.cwd() / ".agent" / f"Session-{session_name}"
    sanitized_title = sanitize_task_title(task_title)
    task_dir_name = f"{task_id}--{sanitized_title}" if sanitized_title else task_id
    task_dir = session_dir / task_dir_name
    task_dir.mkdir(parents=True, exist_ok=True)

    # Write task.md file (T041)
    task_file = task_dir / "task.md"
    atomic_write(task_file, task_content)

    return task_file


def set_current_task(task_id):
    """
    Set active task for current session (T012).

    Updates **Current Task** field in session.md.

    Args:
        task_id: Task ID to set as active

    Raises:
        RuntimeError: If no active session for current terminal

    Example:
        >>> set_current_task("TASK-015")
    """
    session_name = get_session_for_terminal()
    if session_name is None:
        raise RuntimeError("No active session for current terminal")

    session_dir = Path.cwd() / ".agent" / f"Session-{session_name}"
    session_md = session_dir / "session.md"

    # Read session.md content
    if not session_md.exists():
        # Restore from registry if session.md missing
        registry = load_sessions_registry()
        if session_name in registry["sessions"]:
            session_data = registry["sessions"][session_name]
            timestamp = session_data.get("started", datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
            content = f"""# Session: {session_name}

**Started**: {timestamp}
**Topic**: {session_data.get("topic", "(no topic)")}
**Status**: {session_data.get("status", "active")}
**Current Task**: {task_id}
"""
            atomic_write(session_md, content)
            return
        raise RuntimeError(f"Session {session_name} not found in registry")

    content = session_md.read_text()

    # Update **Current Task** field
    updated_content = re.sub(r"(\*\*Current Task\*\*:)\s*.*", f"\\1 {task_id}", content)

    # Write atomically
    atomic_write(session_md, updated_content)


def get_current_task():
    """
    Get active task ID for current session (T013).

    Reads from **Current Task** field in session.md.

    Returns:
        str | None: Task ID if task is active, None otherwise

    Example:
        >>> get_current_task()
        "TASK-015"  # or None
    """
    session_name = get_session_for_terminal()
    if session_name is None:
        return None

    session_dir = Path.cwd() / ".agent" / f"Session-{session_name}"
    session_md = session_dir / "session.md"

    if not session_md.exists():
        return None

    content = session_md.read_text()

    # Extract **Current Task** field
    task_match = re.search(r"\*\*Current Task\*\*:\s*(.+)", content)
    if task_match:
        task_value = task_match.group(1).strip()
        # Return None if value is "(none)" or empty
        if task_value and task_value != "(none)":
            return task_value

    return None


# New Session Management Functions


def get_session_dir(session_name):
    """
    Get session directory path (T010 - updated for named sessions).

    Args:
        session_name: User-chosen session name (e.g., "feature-auth")

    Returns:
        Path: Absolute path to .agent/Session-{name}/

    Example:
        >>> get_session_dir("feature-auth")
        Path('/path/to/project/.agent/Session-feature-auth')
    """
    session_dir = Path.cwd() / ".agent" / f"Session-{session_name}"
    session_dir.mkdir(parents=True, exist_ok=True)
    return session_dir


def get_task_dir(session_name, task_id, task_title):
    """
    Get task subdirectory within session (T015 - updated to use sanitized titles).

    Args:
        session_name: User-chosen session name
        task_id: Task identifier matching pattern TASK-XXX (e.g., TASK-015)
        task_title: Human-readable task description (will be sanitized)

    Returns:
        Path: Absolute path to .agent/Session-{name}/Task-{XXX}--{sanitized-title}/

    Raises:
        ValueError: If task_id doesn't match TASK-XXX pattern

    Example:
        >>> get_task_dir("feature-auth", "TASK-015", "Implement authentication")
        Path('.agent/Session-feature-auth/Task-015--implement-authentication')
    """
    # Validate task_id format
    if not re.match(r"^TASK-\d{3}$", task_id):
        raise ValueError(f"Invalid task_id format: {task_id}. Must match TASK-XXX pattern.")

    # Get session directory
    session_dir = get_session_dir(session_name)

    # Sanitize task title for directory naming (T015)
    sanitized_title = sanitize_task_title(task_title)

    # Construct task directory name
    task_dir_name = f"{task_id}--{sanitized_title}" if sanitized_title else task_id

    # Create task subdirectory
    task_dir = session_dir / task_dir_name
    task_dir.mkdir(parents=True, exist_ok=True)

    return task_dir


def get_context_dir_new(session_id, task_id=None):
    """
    Get context directory for analyst files (session-level or task-level).

    Args:
        session_id: 8-character session ID
        task_id: Optional task ID if context is task-specific

    Returns:
        Path: Session/context/ if task_id=None, else Session/Task-XXX--{title}/

    Raises:
        ValueError: If session directory doesn't exist
        FileNotFoundError: If task_id provided but task not found
    """
    if task_id is None:
        # Session-level context
        session_dir = get_session_dir(session_id)
        context_dir = session_dir / "context"
        context_dir.mkdir(parents=True, exist_ok=True)
        return context_dir
    # Task-level context - need to find task directory
    session_dir = get_session_dir(session_id)

    # Search for task directory matching task_id pattern
    task_pattern = f"{task_id}--*"
    matching_dirs = list(session_dir.glob(task_pattern))

    if matching_dirs:
        return matching_dirs[0]  # Return first match
    # Task directory doesn't exist yet - this is an error
    raise FileNotFoundError(f"Task directory not found for {task_id} in session {session_id}")


def get_session_metadata(session_id):
    """
    Read session.md metadata file.

    Args:
        session_id: 8-character session ID

    Returns:
        dict: Parsed session metadata with session_id, started, topic, status,
              agents_invoked, key_artifacts

    Raises:
        FileNotFoundError: If session.md doesn't exist
    """
    session_dir = get_session_dir(session_id)
    session_file = session_dir / "session.md"

    if not session_file.exists():
        raise FileNotFoundError(f"No session metadata found for {session_id}")

    # Read and parse session.md
    content = session_file.read_text()

    # Basic metadata extraction (simple regex-based parsing)
    metadata = {
        "session_id": session_id,
        "started": None,
        "topic": None,
        "status": "active",
        "agents_invoked": [],
        "key_artifacts": [],
    }

    # Extract started timestamp
    started_match = re.search(r"\*\*Started\*\*:\s*(.+)", content)
    if started_match:
        metadata["started"] = started_match.group(1).strip()

    # Extract topic
    topic_match = re.search(r"\*\*Topic\*\*:\s*(.+)", content)
    if topic_match:
        metadata["topic"] = topic_match.group(1).strip()

    # Extract status
    status_match = re.search(r"\*\*Status\*\*:\s*(.+)", content)
    if status_match:
        metadata["status"] = status_match.group(1).strip()

    return metadata


def update_session_metadata(session_id, updates):
    """
    Update session.md metadata.

    Args:
        session_id: 8-character session ID
        updates: dict with fields to update (e.g., {"status": "completed"})

    Raises:
        FileNotFoundError: If session.md doesn't exist
    """
    session_dir = get_session_dir(session_id)
    session_file = session_dir / "session.md"

    if not session_file.exists():
        raise FileNotFoundError(f"No session metadata found for {session_id}")

    # Read existing content
    content = session_file.read_text()

    # Update fields
    for key, value in updates.items():
        if key == "status":
            # Update status field
            content = re.sub(r"(\*\*Status\*\*:)\s*\w+", f"\\1 {value}", content)

    # Write atomically
    atomic_write(session_file, content)


def migrate_legacy_contexts():
    """
    Migrate old .agent/context/{date}-{topic}-{id}.md files to new structure.

    Returns:
        dict: Migration statistics {"migrated": int, "skipped": int, "errors": int}
    """
    stats = {"migrated": 0, "skipped": 0, "errors": 0}

    # Get legacy context directory
    legacy_dir = get_context_base_dir()

    if not legacy_dir.exists():
        return stats

    # Scan for old-format files (pattern: YYYY-MM-DD-topic-sessionid.md)
    legacy_files = [f for f in legacy_dir.glob("*.md") if f.is_file()]

    for legacy_file in legacy_files:
        try:
            # Parse filename to extract components
            filename = legacy_file.stem

            # Try to match pattern: YYYY-MM-DD-topic-sessionid
            # Example: 2025-10-13-auth-feature-abc456
            match = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)-([0-9a-f]{8})", filename)

            if not match:
                print(f"Skipping (invalid format): {legacy_file.name}")
                stats["skipped"] += 1
                continue

            date_str, topic, session_id = match.groups()

            # Create new session directory
            session_dir = get_session_dir(session_id)
            context_dir = session_dir / "context"
            context_dir.mkdir(parents=True, exist_ok=True)

            # Create session.md if doesn't exist
            session_file = session_dir / "session.md"
            if not session_file.exists():
                session_content = f"""# Session: {session_id}

**Started**: {date_str} 00:00:00
**Topic**: {topic}
**Status**: archived
**Current Task**: (none)
"""
                atomic_write(session_file, session_content)

            # Move file to new structure
            # Infer agent name from content or use topic as filename
            new_file = context_dir / f"{topic}.md"

            # Copy content
            content = legacy_file.read_text()
            atomic_write(new_file, content)

            print(f"Migrated: {legacy_file.name} → {session_dir.name}/context/{new_file.name}")
            stats["migrated"] += 1

        except Exception as e:
            print(f"Error migrating {legacy_file.name}: {e}")
            stats["errors"] += 1

    return stats


def archive_session_new(session_id):
    """
    Move session directory to archive/.

    Args:
        session_id: 8-character session ID

    Returns:
        Path: Path to archived session directory

    Raises:
        FileNotFoundError: If session directory doesn't exist
    """
    session_dir = get_session_dir(session_id)

    if not session_dir.exists():
        raise FileNotFoundError(f"Session directory not found: {session_id}")

    # Create archive directory (project-local per T005)
    archive_dir = Path.cwd() / ".agent" / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Move session to archive
    archived_path = archive_dir / session_dir.name
    session_dir.rename(archived_path)

    # Update session.md status
    session_file = archived_path / "session.md"
    if session_file.exists():
        update_session_metadata(session_id, {"status": "archived"})

    return archived_path


def cleanup_session(session_name, action):
    """
    Handle session cleanup (T009).

    Args:
        session_name: Session name to clean up
        action: Cleanup action ("delete", "archive", or "keep")

    Returns:
        bool: True if successful, False otherwise

    Raises:
        ValueError: If action is invalid
        FileNotFoundError: If session directory doesn't exist
    """
    if action not in ["delete", "archive", "keep"]:
        raise ValueError(f"Invalid action: {action}. Must be 'delete', 'archive', or 'keep'.")

    try:
        session_dir = get_session_dir(session_name)

        if not session_dir.exists():
            raise FileNotFoundError(f"Session directory not found: {session_name}")

        registry = load_sessions_registry()

        if action == "delete":
            # Remove session directory and registry entry (T054)
            shutil.rmtree(session_dir)
            if session_name in registry["sessions"]:
                del registry["sessions"][session_name]
                save_sessions_registry(registry)
            print(f"Deleted session: {session_name}")
            return True

        if action == "archive":
            # Move to archive/ and update status (T055)
            archive_dir = Path.cwd() / ".agent" / "archive"
            archive_dir.mkdir(parents=True, exist_ok=True)
            archived_path = archive_dir / f"Session-{session_name}"
            session_dir.rename(archived_path)

            # Update registry status
            if session_name in registry["sessions"]:
                registry["sessions"][session_name]["status"] = "archived"
                save_sessions_registry(registry)

            print(f"Archived session to: {archived_path}")
            return True

        if action == "keep":
            # Just update status to completed (T056)
            if session_name in registry["sessions"]:
                registry["sessions"][session_name]["status"] = "completed"
                save_sessions_registry(registry)

            print(f"Session {session_name} marked as completed (kept active)")
            return True

    except Exception as e:
        print(f"Error during cleanup: {e}")
        return False


def get_context_dir():
    """
    Get context directory with task-aware routing (T014).

    Returns:
        str: Path to task directory if task active, else session context/ directory

    Raises:
        RuntimeError: If no active session for current terminal

    Example:
        >>> get_context_dir()
        # Task active: ".agent/Session-feature-auth/Task-015--implement-auth"
        # No task: ".agent/Session-feature-auth/context"
    """
    session_name = get_session_for_terminal()
    if session_name is None:
        raise RuntimeError("No active session for current terminal")

    session_dir = get_session_dir(session_name)

    # Task-aware routing logic (T014, T043)
    task_id = get_current_task()

    if task_id:
        # Task is active - route to task directory
        # Find task directory matching task_id pattern (T045)
        task_pattern = f"{task_id}--*"
        matching_dirs = list(session_dir.glob(task_pattern))

        if matching_dirs:
            return str(matching_dirs[0])  # Return first matching task directory
        # Task marker exists but directory missing - fall back to session context
        # (Could also raise FileNotFoundError, but graceful fallback is more robust)
        print(f"Warning: Task directory not found for {task_id}, using session context")
        context_dir = session_dir / "context"
        context_dir.mkdir(parents=True, exist_ok=True)
        return str(context_dir)
    # No active task - route to session context/
    context_dir = session_dir / "context"
    context_dir.mkdir(parents=True, exist_ok=True)
    return str(context_dir)


def setup_task_atomic(task_id, task_content):
    """
    Atomic task setup: copy task, set active, validate all operations.

    Combines copy_task + set_task + get_context_dir with transactional safety.
    All operations succeed or all fail together (rollback on error).

    Args:
        task_id: Task ID matching pattern TASK-\\d{3}
        task_content: Full task markdown content

    Returns:
        dict: {
            "session": "feature-auth",
            "task_id": "TASK-029",
            "task_dir": "/absolute/path/to/Task-029--fix-auth",
            "context_dir": "/absolute/path/to/Task-029--fix-auth",
            "validation": {
                "task_dir_exists": true,
                "marker_set": true,
                "context_valid": true
            }
        }

    Raises:
        ValueError: If task_id invalid or operations fail
        RuntimeError: If no active session
    """
    # Validate task_id format
    if not re.match(r"^TASK-\d{3}$", task_id):
        raise ValueError(f"Invalid task_id '{task_id}'. Must match TASK-XXX pattern (e.g., TASK-001)")

    # Get active session
    session_name = get_session_for_terminal()
    if session_name is None:
        raise RuntimeError("No active session for current terminal")

    session_dir = get_session_dir(session_name)

    try:
        # Step 1: Copy task to session
        task_file = copy_task_to_session(task_id, task_content)
        task_dir = task_file.parent

        # Step 2: Set active task marker
        set_current_task(task_id)

        # Step 3: Get context directory (should route to task directory now)
        context_dir = get_context_dir()

        # Step 4: Validate all operations succeeded
        validation = {
            "task_dir_exists": task_dir.exists(),
            "marker_set": get_current_task() == task_id,
            "context_valid": Path(context_dir).exists() and task_id in context_dir,
        }

        # All validations must pass
        if not all(validation.values()):
            raise ValueError(f"Task setup validation failed: {validation}")

        # Return complete state as JSON
        return {
            "session": session_name,
            "task_id": task_id,
            "task_dir": str(task_dir),
            "context_dir": str(context_dir),
            "validation": validation,
        }

    except Exception as e:
        # Rollback: clear **Current Task** field in session.md if it was set
        import contextlib

        with contextlib.suppress(Exception):
            session_md = session_dir / "session.md"
            if session_md.exists():
                content = session_md.read_text()
                updated = re.sub(r"(\*\*Current Task\*\*:)\s*.*", r"\1 (none)", content)
                atomic_write(session_md, updated)

        raise ValueError(f"Task setup failed: {e}") from e


def list_agents():
    """List agents that have been invoked in current session"""
    session_name = get_session_for_terminal()
    if session_name is None:
        print("No active session for current terminal")
        return []

    context_dir = get_context_dir_new(session_name)

    if not context_dir.exists():
        print("No context directory found for current session")
        return []

    # List all .md files except session.md
    agent_files = [f.stem for f in context_dir.glob("*.md") if f.name != "session.md"]

    if agent_files:
        print("Agents invoked in this session:")
        for agent in sorted(agent_files):
            print(f"  - {agent}")
    else:
        print("No agents invoked yet in this session")

    return agent_files


def list_sessions():
    """
    List all active sessions with metadata (new command for improved UX).

    Returns:
        dict: JSON structure with list of active sessions
        {
            "sessions": [
                {"name": "task-work", "topic": "...", "started": "...", "terminals": [...]},
                ...
            ]
        }
    """
    registry = load_sessions_registry()

    sessions_list = []
    for session_name, session_data in registry["sessions"].items():
        if session_data.get("status") == "active":
            sessions_list.append(
                {
                    "name": session_name,
                    "topic": session_data.get("topic", ""),
                    "started": session_data.get("started", ""),
                    "terminals": session_data.get("terminals", []),
                    "terminal_count": len(session_data.get("terminals", [])),
                }
            )

    return {
        "sessions": sessions_list,
        "count": len(sessions_list),
    }


def main():
    """Main entry point (T022 - updated CLI support)"""
    if len(sys.argv) < 2:
        print("Usage: session_manager.py [current|start <name> [topic]|select <name>|list|context_dir")
        print("|copy_task <task-id> <content>|set_task <task-id>|clear_task|setup_task <task-id> <content>")
        print("|list_agents]")
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "current":
            # Get current session name for terminal
            session_name = get_session_for_terminal()
            if session_name:
                print(session_name)
            else:
                print("")  # Empty string if not linked

        elif command == "start":
            # Create and start new session
            if len(sys.argv) < 3:
                print("Error: session name required")
                print("Usage: session_manager.py start <name> [topic]")
                sys.exit(1)

            session_name = sys.argv[2]
            topic = sys.argv[3] if len(sys.argv) > 3 else ""
            create_session(session_name, topic)

        elif command == "select":
            # Link current terminal to existing session
            if len(sys.argv) < 3:
                print("Error: session name required")
                print("Usage: session_manager.py select <name>")
                sys.exit(1)

            session_name = sys.argv[2]
            select_session(session_name)

        elif command == "context_dir":
            # Get context directory path (task-aware routing)
            print(get_context_dir())

        elif command == "list":
            # List all active sessions
            result = list_sessions()
            print(json.dumps(result, indent=2))

        elif command == "list_agents":
            # List agents invoked in current session
            list_agents()

        elif command == "copy_task":
            # Copy task entity to session task directory
            if len(sys.argv) < 4:
                print("Error: task_id and task_content required")
                print("Usage: session_manager.py copy_task <task-id> <task-content>")
                sys.exit(1)

            task_id = sys.argv[2]
            task_content = sys.argv[3]
            task_file = copy_task_to_session(task_id, task_content)
            print(f"Task copied to: {task_file}")

        elif command == "set_task":
            # Set active task for current session
            if len(sys.argv) < 3:
                print("Error: task_id required")
                print("Usage: session_manager.py set_task <task-id>")
                sys.exit(1)

            task_id = sys.argv[2]
            set_current_task(task_id)
            print(f"Active task set: {task_id}")

        elif command == "clear_task":
            # Clear active task marker
            session_name = get_session_for_terminal()
            if session_name:
                session_dir = get_session_dir(session_name)
                session_md = session_dir / "session.md"
                if session_md.exists():
                    content = session_md.read_text()
                    updated = re.sub(r"(\*\*Current Task\*\*:)\s*.*", r"\1 (none)", content)
                    atomic_write(session_md, updated)
                    print("Active task cleared")
                else:
                    print("No session.md file found")
            else:
                print("Error: No active session for current terminal")
                sys.exit(1)

        elif command == "setup_task":
            # Atomic task setup with validation
            if len(sys.argv) < 4:
                print("Error: task_id and task_content required")
                print("Usage: session_manager.py setup_task <task-id> <task-content>")
                sys.exit(1)

            task_id = sys.argv[2]
            task_content = sys.argv[3]
            result = setup_task_atomic(task_id, task_content)
            print(json.dumps(result, indent=2))

        else:
            print(f"Unknown command: {command}")
            print("Usage: session_manager.py [current|start <name> [topic]|select <name>|list|context_dir")
            print("|copy_task <task-id> <content>|set_task <task-id>|clear_task|setup_task <task-id> <content>")
            print("|list_agents]")
            sys.exit(1)

    except (ValueError, RuntimeError, FileNotFoundError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
