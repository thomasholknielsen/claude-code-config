#!/usr/bin/env python3
"""
Auto-initialize session at conversation start.
This hook runs before the first user prompt in a new conversation.
"""

from pathlib import Path
import subprocess


def main():
    """Initialize session automatically if not already active."""
    try:
        # Get project root (current working directory)
        Path.cwd()

        # Check if session manager exists
        session_manager = Path.home() / ".claude" / "scripts" / "session" / "session_manager.py"

        if not session_manager.exists():
            # Silent fail - session management is optional
            return

        # Check if session already exists
        result = subprocess.run(["python3", str(session_manager), "current"], capture_output=True, text=True, timeout=5)

        # If session exists, do nothing
        if result.returncode == 0 and result.stdout.strip():
            return

        # Initialize new session
        subprocess.run(
            ["python3", str(session_manager), "init"],
            check=False,  # Don't fail if initialization fails
            timeout=5,
        )

    except Exception:
        # Silent fail - don't interrupt user workflow
        pass


if __name__ == "__main__":
    main()
