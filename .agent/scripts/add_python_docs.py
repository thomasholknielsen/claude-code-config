#!/usr/bin/env python3
"""Batch add type hints and documentation to Python hook scripts."""

from pathlib import Path


# Add comprehensive documentation to notify.py
notify_py = Path.home() / ".claude" / "scripts" / "hooks" / "notify.py"
notify_content = notify_py.read_text()

# Add type hints to notify.py functions
notify_updated = (
    notify_content.replace("def get_script_dir():", "def get_script_dir() -> Path:")
    .replace(
        '    """Get the directory where this script is located."""',
        '''    """
    Get the directory where this script is located.

    Returns:
        Path: Directory containing this script

    Example:
        >>> script_dir = get_script_dir()
        >>> print(script_dir.exists())
        True
    """''',
    )
    .replace("def detect_os():", "def detect_os() -> str:")
    .replace(
        '    """Detect the operating system and return appropriate identifier."""',
        '''    """
    Detect the operating system and return appropriate identifier.

    Returns:
        str: OS identifier ('macos', 'windows', 'wsl', 'linux', or 'unknown')

    Example:
        >>> os_type = detect_os()
        >>> print(os_type in ['macos', 'windows', 'linux', 'wsl', 'unknown'])
        True
    """''',
    )
    .replace(
        "def run_notification(os_type, script_dir, stdin_data):",
        "def run_notification(os_type: str, script_dir: Path, stdin_data: str) -> None:",
    )
    .replace(
        '    """Run the appropriate notification script based on OS."""',
        '''    """
    Run the appropriate notification script based on OS.

    Args:
        os_type: Operating system identifier
        script_dir: Directory containing notification scripts
        stdin_data: Data to pass to notification script

    Example:
        >>> run_notification('macos', Path('/path/to/scripts'), 'Task completed')
    """''',
    )
    .replace(
        "def _get_notification_command(os_type, script_dir):",
        "def _get_notification_command(os_type: str, script_dir: Path) -> list[str]:",
    )
    .replace(
        '    """Get the appropriate notification command for the OS."""',
        '''    """
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
    """''',
    )
    .replace(
        "def _execute_notification(cmd, stdin_data):",
        "def _execute_notification(cmd: list[str], stdin_data: str) -> None:",
    )
    .replace(
        '    """Execute the notification script and handle errors."""',
        '''    """
    Execute the notification script and handle errors.

    Args:
        cmd: Command array for subprocess.run()
        stdin_data: Data to pass to notification script via stdin

    Raises:
        subprocess.TimeoutExpired: If notification script exceeds timeout (handled internally)
        FileNotFoundError: If notification script not found (handled internally)

    Example:
        >>> _execute_notification(['echo', 'test'], 'data')
    """''',
    )
)

notify_py.write_text(notify_updated)
print(f"✓ Updated {notify_py}")

# Add comprehensive documentation to update-search-year.py
search_py = Path.home() / ".claude" / "scripts" / "hooks" / "update-search-year.py"
search_content = search_py.read_text()

search_updated = search_content.replace("def main():", "def main() -> None:").replace(
    '    """Main entry point for the search year update hook."""',
    '''    """
    Main entry point for the search year update hook.

    Reads JSON from stdin, extracts web search query, and appends current year
    if no year or temporal keywords are present. Outputs modified query to stdout.

    Input JSON format:
        {"tool_input": {"query": "python documentation"}}

    Output JSON format:
        {"hookSpecificOutput": {"hookEventName": "PreToolUse", "modifiedToolInput": {"query": "python documentation 2025"}}}

    Raises:
        json.JSONDecodeError: If input is not valid JSON (handled, error message printed)
        SystemExit: Always exits with 0 on success, 1 on error

    Example:
        >>> # Input: {"tool_input": {"query": "react hooks"}}
        >>> # Output: {"hookSpecificOutput": {"hookEventName": "PreToolUse", "modifiedToolInput": {"query": "react hooks 2025"}}}
        >>> # (assuming current year is 2025 and no temporal keywords present)
    """''',
)

search_py.write_text(search_updated)
print(f"✓ Updated {search_py}")

print("\n✅ All Python hook scripts now have comprehensive type hints and documentation")
