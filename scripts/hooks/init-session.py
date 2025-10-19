#!/usr/bin/env python3
"""
Auto-initialize session at conversation start.
This hook runs before the first user prompt in a new conversation.

Updated for TTY-based named sessions with graceful fallback for non-interactive mode.
"""

import os
from pathlib import Path
import subprocess
import sys


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

        # Check if session already exists for current terminal
        result = subprocess.run(["python3", str(session_manager), "current"], capture_output=True, text=True, timeout=5)

        # If session exists, print compact confirmation and exit
        if result.returncode == 0 and result.stdout.strip():
            session_name = result.stdout.strip()
            session_dir = Path.cwd() / ".agent" / f"Session-{session_name}"
            print(f"SessionStart:compact hook success: Session context already exists: {session_dir}", file=sys.stderr)
            return

        # No session exists - need to create one
        # Try to detect if we're in interactive mode (TTY available)
        try:
            os.ttyname(0)
            is_interactive = True
        except (OSError, AttributeError):
            is_interactive = False

        if is_interactive:
            # Interactive mode - try to select existing "adhoc" session first
            result = subprocess.run(
                ["python3", str(session_manager), "select", "adhoc"],
                capture_output=True,
                text=True,
                check=False,
                timeout=5,
            )

            if result.returncode == 0:
                # Successfully linked to existing adhoc session
                print("SessionStart:compact hook success: Linked to existing adhoc session", file=sys.stderr)
            else:
                # adhoc session doesn't exist - try to create it
                result = subprocess.run(
                    ["python3", str(session_manager), "start", "adhoc", "Ad-hoc development session"],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=5,
                )
                if result.returncode == 0:
                    print("SessionStart:compact hook success: Created ad-hoc session", file=sys.stderr)
                else:
                    # Session creation failed - fall back to legacy init
                    subprocess.run(["python3", str(session_manager), "init"], check=False, timeout=5)
        else:
            # Non-interactive mode (hook/script context) - create adhoc session
            # Try to select existing adhoc session first
            result = subprocess.run(
                ["python3", str(session_manager), "select", "adhoc"],
                capture_output=True,
                text=True,
                check=False,
                timeout=5,
            )

            if result.returncode == 0:
                # Successfully linked to existing adhoc session
                session_dir = Path.cwd() / ".agent" / "Session-adhoc"
                print(f"SessionStart:compact hook success: Linked to adhoc session: {session_dir}", file=sys.stderr)
            else:
                # adhoc session doesn't exist - create it
                result = subprocess.run(
                    ["python3", str(session_manager), "start", "adhoc", "Ad-hoc development session"],
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=5,
                )
                if result.returncode == 0:
                    session_dir = Path.cwd() / ".agent" / "Session-adhoc"
                    print(f"SessionStart:compact hook success: Created adhoc session: {session_dir}", file=sys.stderr)
                else:
                    # Session creation failed - print error for debugging
                    print("SessionStart:compact hook error: Failed to create adhoc session", file=sys.stderr)

    except Exception:
        # Silent fail - don't interrupt user workflow
        pass


if __name__ == "__main__":
    main()
