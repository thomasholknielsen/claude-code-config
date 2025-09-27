#!/usr/bin/env python3
"""
Cross-platform user prompt logging for Claude Code hooks.
Logs all user prompts to daily rotating log files.
"""

from datetime import datetime
import json
from pathlib import Path
import sys


def get_script_dir():
    """Get the directory where this script is located."""
    if "__file__" in globals():
        return Path(__file__).parent
    # Fallback to ~/.claude/scripts directory
    return Path.home() / ".claude" / "scripts"


def get_logs_dir():
    """Get the logs directory, creating it if it doesn't exist."""
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


def get_log_filename():
    """Generate log filename for this year."""
    year = datetime.now().strftime("%Y")
    return f"prompt-log-{year}.log"


def sanitize_prompt(prompt_text):
    """Sanitize prompt text for logging (remove sensitive patterns)."""
    # Basic sanitization - remove control characters but keep newlines
    sanitized = "".join(char for char in prompt_text if char.isprintable() or char in "\n\r\t")

    # Limit length to prevent huge log entries
    max_length = 10000
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length] + "... [TRUNCATED]"

    return sanitized


def log_prompt(prompt_text):
    """Log the user prompt to the yearly log file."""
    try:
        logs_dir = get_logs_dir()
        log_file = logs_dir / get_log_filename()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
        sanitized_prompt = sanitize_prompt(prompt_text)

        # Create log entry
        log_entry = f"[{timestamp}] USER PROMPT:\n{sanitized_prompt}\n{'=' * 80}\n\n"

        # Write to log file with UTF-8 encoding
        with log_file.open("a", encoding="utf-8", errors="replace") as f:
            f.write(log_entry)
            f.flush()  # Ensure immediate write

        return True, f"Logged to {log_file}"

    except Exception as e:
        return False, f"Failed to log prompt: {str(e)}"


def parse_hook_input():
    """Parse the input from Claude Code hook."""
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
            elif isinstance(hook_data, dict) and "content" in hook_data:
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
