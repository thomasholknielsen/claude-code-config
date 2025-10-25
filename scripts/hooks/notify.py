#!/usr/bin/env python
"""
Cross-platform notification wrapper for Claude Code hooks.
Detects the operating system and routes to the appropriate notification script.
"""

from pathlib import Path
import platform
import subprocess
import sys
from typing import List


# Constants
NOTIFICATION_TIMEOUT_SECONDS = 30  # Maximum time to wait for notification script


def get_script_dir() -> Path:
    """
    Get the directory where this script is located.

    Returns:
        Path: Directory containing this script

    Example:
        >>> script_dir = get_script_dir()
        >>> print(script_dir.exists())
        True
    """
    # Handle case where __file__ is not defined (when using exec())
    if "__file__" in globals():
        return Path(__file__).parent
    # Fallback to ~/.claude/scripts directory
    return Path.home() / ".claude" / "scripts"


def detect_os() -> str:
    """
    Detect the operating system and return appropriate identifier.

    Returns:
        str: OS identifier ('macos', 'windows', 'wsl', 'linux', or 'unknown')

    Example:
        >>> os_type = detect_os()
        >>> print(os_type in ['macos', 'windows', 'linux', 'wsl', 'unknown'])
        True
    """
    system = platform.system().lower()

    if system == "darwin":
        return "macos"
    if system == "windows":
        return "windows"
    if system == "linux":
        # Check if running in WSL (treat as Windows)
        try:
            with Path("/proc/version").open() as f:
                if "microsoft" in f.read().lower():
                    return "wsl"
        except (FileNotFoundError, PermissionError):
            pass
        return "linux"
    return "unknown"


def run_notification(os_type: str, script_dir: Path, stdin_data: str) -> None:
    """
    Run the appropriate notification script based on OS.

    Args:
        os_type: Operating system identifier
        script_dir: Directory containing notification scripts
        stdin_data: Data to pass to notification script

    Example:
        >>> run_notification('macos', Path('/path/to/scripts'), 'Task completed')
    """
    # Early return for unsupported OS
    if os_type not in ["macos", "windows", "wsl"]:
        print(f"Claude Code notification: Task completed (OS: {os_type} - notifications not supported)")
        return

    # Determine command based on OS
    cmd = _get_notification_command(os_type, script_dir)

    # Execute notification script
    _execute_notification(cmd, stdin_data)


def _get_notification_command(os_type: str, script_dir: Path) -> List[str]:
    """
    Get the appropriate notification command for the OS.

    Args:
        os_type: Operating system identifier
        script_dir: Directory containing notification scripts

    Returns:
        list[str]: Command array for subprocess.run()

    Example:
        >>> cmd = _get_notification_command('macos', Path('/scripts'))
        >>> print(cmd[0])
        'bash'
    """
    if os_type == "macos":
        script_path = script_dir / "notify-macos.sh"
        return ["bash", str(script_path)]

    # Windows or WSL
    script_path = script_dir / "notify-windows.ps1"
    return ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "RemoteSigned", "-File", str(script_path)]


def _execute_notification(cmd: List[str], stdin_data: str) -> None:
    """
    Execute the notification script and handle errors.

    Args:
        cmd: Command array for subprocess.run()
        stdin_data: Data to pass to notification script via stdin

    Raises:
        subprocess.TimeoutExpired: If notification script exceeds timeout (handled internally)
        FileNotFoundError: If notification script not found (handled internally)

    Example:
        >>> _execute_notification(['echo', 'test'], 'data')
    """
    try:
        result = subprocess.run(
            cmd, input=stdin_data, text=True, capture_output=True, timeout=NOTIFICATION_TIMEOUT_SECONDS
        )

        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)

    except subprocess.TimeoutExpired:
        print("Notification script timed out", file=sys.stderr)
    except FileNotFoundError:
        print(f"Notification script not found: {cmd[0]}", file=sys.stderr)
        print("Claude Code notification: Task completed")
    except Exception as e:
        print(f"Error running notification: {e}", file=sys.stderr)
        print("Claude Code notification: Task completed")


def main():
    """Main function to handle cross-platform notifications."""
    # Read stdin data
    stdin_data = sys.stdin.read()

    # Detect OS and get script directory
    os_type = detect_os()
    script_dir = get_script_dir()

    # Run appropriate notification
    run_notification(os_type, script_dir, stdin_data)


if __name__ == "__main__":
    main()
