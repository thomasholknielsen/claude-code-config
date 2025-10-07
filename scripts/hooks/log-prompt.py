#!/usr/bin/env python3
"""
Cross-platform user prompt logging for Claude Code hooks.
Logs all user prompts to daily rotating log files.
"""

from datetime import datetime
import json
from pathlib import Path
import sys


# Constants
MAX_LOG_LINES = 15  # Maximum number of lines to include in log preview
SEPARATOR_WIDTH = 80  # Width of separator line in log output


def get_script_dir() -> Path:
    """
    Get the directory where this script is located.

    Returns:
        Path: Directory containing this script

    Example:
        >>> script_dir = get_script_dir()
        >>> print(script_dir)
        PosixPath('/Users/username/.claude/scripts')
    """
    if "__file__" in globals():
        return Path(__file__).parent
    # Fallback to ~/.claude/scripts directory
    return Path.home() / ".claude" / "scripts"


def get_logs_dir() -> Path:
    """
    Get the logs directory, creating it if it doesn't exist.

    Returns:
        Path: Logs directory path (~/.claude/logs or fallback)

    Raises:
        PermissionError: If directory cannot be created (handled internally with fallback)

    Example:
        >>> logs_dir = get_logs_dir()
        >>> print(logs_dir.exists())
        True
    """
    logs_dir = Path.home() / ".claude" / "logs"

    # Create directory if it doesn't exist
    try:
        logs_dir.mkdir(parents=True, exist_ok=True)
        return logs_dir
    except PermissionError:
        # Fallback to a subdirectory in the script directory
        fallback_dir = get_script_dir() / "logs"
        fallback_dir.mkdir(parents=True, exist_ok=True)
        return fallback_dir


def get_log_filename() -> str:
    """
    Generate log filename for this year.

    Returns:
        str: Log filename in format "prompt-log-YYYY.log"

    Example:
        >>> filename = get_log_filename()
        >>> print(filename)
        'prompt-log-2025.log'
    """
    year = datetime.now().strftime("%Y")
    return f"prompt-log-{year}.log"


def sanitize_prompt(prompt_text: str) -> str:
    """
    Sanitize prompt text for logging (only first MAX_LOG_LINES lines).

    Args:
        prompt_text: Raw user prompt text to sanitize

    Returns:
        str: Sanitized text with only printable characters and newlines, truncated to MAX_LOG_LINES

    Example:
        >>> sanitize_prompt("Hello\\x00World\\nLine2")
        'HelloWorld\\nLine2'
        >>> long_prompt = "\\n".join([f"Line {i}" for i in range(20)])
        >>> result = sanitize_prompt(long_prompt)
        >>> "TRUNCATED" in result
        True
    """
    # Basic sanitization - remove control characters but keep newlines
    sanitized = "".join(char for char in prompt_text if char.isprintable() or char in "\n\r\t")

    # Limit to first MAX_LOG_LINES lines to prevent huge log entries
    lines = sanitized.split("\n")
    if len(lines) > MAX_LOG_LINES:
        sanitized = "\n".join(lines[:MAX_LOG_LINES]) + f"\n... [TRUNCATED - showing first {MAX_LOG_LINES} lines only]"
    else:
        sanitized = "\n".join(lines)

    return sanitized


def log_prompt(prompt_text: str) -> tuple[bool, str]:
    """
    Log the user prompt to the yearly log file.

    Args:
        prompt_text: User prompt text to log

    Returns:
        tuple[bool, str]: Success status and message (True, "Logged to...") or (False, "Failed...")

    Example:
        >>> success, message = log_prompt("Test prompt")
        >>> print(success)
        True
        >>> "Logged to" in message
        True
    """
    try:
        logs_dir = get_logs_dir()
        log_file = logs_dir / get_log_filename()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
        sanitized_prompt = sanitize_prompt(prompt_text)

        # Create log entry
        log_entry = f"[{timestamp}] USER PROMPT:\n{sanitized_prompt}\n{'=' * SEPARATOR_WIDTH}\n\n"

        # Write to log file with UTF-8 encoding
        with log_file.open("a", encoding="utf-8", errors="replace") as f:
            f.write(log_entry)
            # Context manager handles flush on close

        return True, f"Logged to {log_file}"

    except Exception as e:
        return False, f"Failed to log prompt: {str(e)}"


def parse_hook_input() -> tuple[str | None, str | None]:
    """
    Parse the input from Claude Code hook.

    Returns:
        tuple[str | None, str | None]: Parsed prompt text and error message (one will be None)

    Example:
        >>> # With JSON input: {"prompt": "Hello world"}
        >>> prompt, error = parse_hook_input()
        >>> print(prompt)
        'Hello world'
        >>> print(error)
        None
    """
    try:
        # Read all stdin
        input_data = sys.stdin.read().strip()

        if not input_data:
            return None, "No input data received"

        # Try to parse as JSON first (structured hook data)
        try:
            hook_data = json.loads(input_data)
            if isinstance(hook_data, dict) and "prompt" in hook_data:
                return hook_data["prompt"], None
            if isinstance(hook_data, dict) and "content" in hook_data:
                return hook_data["content"], None
            # If it's JSON but doesn't have expected structure, use the raw JSON
            return input_data, None
        except json.JSONDecodeError:
            # Not JSON, treat as raw prompt text
            return input_data, None

    except Exception as e:
        return None, f"Error parsing input: {str(e)}"


def main():
    """Main function to handle user prompt logging."""
    # Parse the hook input
    prompt_text, error = parse_hook_input()

    if error:
        print(f"[ERROR] {error}", file=sys.stderr)
        return 1

    if prompt_text is None:
        print("[ERROR] No prompt text found in input", file=sys.stderr)
        return 1

    # Log the prompt
    success, message = log_prompt(prompt_text)

    if success:
        print(f"[INFO] Prompt logged successfully: {message}")
        return 0

    print(f"[ERROR] {message}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
