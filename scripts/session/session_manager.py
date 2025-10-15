#!/usr/bin/env python3
"""
Session Manager for Claude Code
Cross-platform session ID generation and management with context directory support
"""

from datetime import datetime
from pathlib import Path
import sys
import uuid


# Constants
SESSION_ID_LENGTH = 8  # Length of generated session IDs (first 8 chars of UUID)


def get_session_file():
    """Get path to session file (cross-platform)"""
    claude_dir = Path.home() / ".claude"
    claude_dir.mkdir(exist_ok=True)
    return claude_dir / ".current_session"


def get_context_base_dir():
    """Get base context directory (cross-platform)"""
    context_dir = Path.home() / ".claude" / ".agent" / "context"
    context_dir.mkdir(parents=True, exist_ok=True)
    return context_dir


def get_session_context_dir(session_id):
    """Get context directory for a specific session"""
    session_dir = get_context_base_dir() / session_id
    return session_dir


def generate_session_id():
    """Generate a short, unique session ID"""
    return str(uuid.uuid4())[:SESSION_ID_LENGTH]


def current_session():
    """Get current session ID, create if doesn't exist"""
    session_file = get_session_file()

    if session_file.exists():
        return session_file.read_text().strip()

    # Create new session if none exists
    session_id = generate_session_id()
    session_file.write_text(session_id)
    return session_id


def new_session(topic=None):
    """Create new session with optional topic"""
    session_id = generate_session_id()
    session_file = get_session_file()
    session_file.write_text(session_id)

    if topic:
        print(f"Created new session: {session_id} (topic: {topic})")
    else:
        print(f"Created new session: {session_id}")

    return session_id


def init_session(topic=None):
    """Initialize a new session with context directory and session metadata file"""
    session_id = current_session()
    session_dir = get_session_context_dir(session_id)
    session_dir.mkdir(parents=True, exist_ok=True)

    # Create session.md metadata file
    session_file = session_dir / "session.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not session_file.exists():
        content = f"""# Session: {session_id}

**Started**: {timestamp}
**Topic**: {topic if topic else "General development"}
**Status**: active

## Agents Invoked

## Overview

## Key Artifacts
"""
        session_file.write_text(content)
        print(f"Initialized session context: {session_dir}")
    else:
        print(f"Session context already exists: {session_dir}")

    return str(session_dir)


def get_context_dir():
    """Get context directory path for current session"""
    session_id = current_session()
    session_dir = get_session_context_dir(session_id)
    session_dir.mkdir(parents=True, exist_ok=True)
    return str(session_dir)


def list_agents():
    """List agents that have been invoked in current session"""
    session_id = current_session()
    session_dir = get_session_context_dir(session_id)

    if not session_dir.exists():
        print("No context directory found for current session")
        return []

    # List all .md files except session.md
    agent_files = [f.stem for f in session_dir.glob("*.md") if f.name != "session.md"]

    if agent_files:
        print("Agents invoked in this session:")
        for agent in sorted(agent_files):
            print(f"  - {agent}")
    else:
        print("No agents invoked yet in this session")

    return agent_files


def archive_session():
    """Mark current session as completed"""
    session_id = current_session()
    session_dir = get_session_context_dir(session_id)
    session_file = session_dir / "session.md"

    if session_file.exists():
        content = session_file.read_text()
        # Update status to completed
        content = content.replace("**Status**: active", "**Status**: completed")
        session_file.write_text(content)
        print(f"Session {session_id} marked as completed")
    else:
        print(f"No session metadata found for {session_id}")

    return session_id


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: session_manager.py [current|new [topic]|init [topic]|context_dir|list_agents|archive]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "current":
        print(current_session())
    elif command == "new":
        topic = sys.argv[2] if len(sys.argv) > 2 else None
        new_session(topic)
    elif command == "init":
        topic = sys.argv[2] if len(sys.argv) > 2 else None
        init_session(topic)
    elif command == "context_dir":
        print(get_context_dir())
    elif command == "list_agents":
        list_agents()
    elif command == "archive":
        archive_session()
    else:
        print(f"Unknown command: {command}")
        print("Usage: session_manager.py [current|new [topic]|init [topic]|context_dir|list_agents|archive]")
        sys.exit(1)


if __name__ == "__main__":
    main()
