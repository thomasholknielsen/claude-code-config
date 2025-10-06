#!/usr/bin/env python3
"""
Session Manager for Claude Code
Cross-platform session ID generation and management
"""

from pathlib import Path
import sys
import uuid


def get_session_file():
    """Get path to session file (cross-platform)"""
    claude_dir = Path.home() / ".claude"
    claude_dir.mkdir(exist_ok=True)
    return claude_dir / ".current_session"


def generate_session_id():
    """Generate a short, unique session ID"""
    return str(uuid.uuid4())[:8]


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


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: session_manager.py [current|new [topic]]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "current":
        print(current_session())
    elif command == "new":
        topic = sys.argv[2] if len(sys.argv) > 2 else None
        new_session(topic)
    else:
        print(f"Unknown command: {command}")
        print("Usage: session_manager.py [current|new [topic]]")
        sys.exit(1)


if __name__ == "__main__":
    main()
