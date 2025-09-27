#!/usr/bin/env python3
"""
Cross-platform notification wrapper for Claude Code hooks.
Detects the operating system and routes to the appropriate notification script.
"""

from pathlib import Path
import platform
import subprocess
import sys


def get_script_dir():
    """Get the directory where this script is located."""
    # Handle case where __file__ is not defined (when using exec())
    if "__file__" in globals():
        return Path(__file__).parent
    # Fallback to ~/.claude/scripts directory
    return Path.home() / ".claude" / "scripts"


def detect_os():
    """Detect the operating system and return appropriate identifier."""
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


def run_notification(os_type, script_dir, stdin_data):
    """Run the appropriate notification script based on OS."""

    if os_type == "macos":
        # Use bash to run the macOS shell script
        script_path = script_dir / "notify-macos.sh"
        cmd = ["bash", str(script_path)]

    elif os_type in ["windows", "wsl"]:
        # Use PowerShell to run the Windows script
        script_path = script_dir / "notify-windows.ps1"
        cmd = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script_path)]

    else:
        # Unsupported OS - just print to console
        print(f"Claude Code notification: Task completed (OS: {os_type} - notifications not supported)")
        return

    try:
        # Run the appropriate script with stdin data
        result = subprocess.run(cmd, input=stdin_data, text=True, capture_output=True, timeout=30)

        # Print any output from the script
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)

    except subprocess.TimeoutExpired:
        print("Notification script timed out", file=sys.stderr)
    except FileNotFoundError:
        print(f"Notification script not found: {cmd[0]}", file=sys.stderr)
        # Fallback: just print to console
        print("Claude Code notification: Task completed")
    except Exception as e:
        print(f"Error running notification: {e}", file=sys.stderr)
        # Fallback: just print to console
        print("Claude Code notification: Task completed")


def main():
    """Main function to handle cross-platform notifications."""
    # Debug: Print that the hook was triggered
    print("[DEBUG] Claude Code stop hook triggered!", flush=True)

    # Read stdin data
    stdin_data = sys.stdin.read()

    # Debug: Print input data
    print(f"[DEBUG] Hook input data: {stdin_data[:100]}{'...' if len(stdin_data) > 100 else ''}", flush=True)

    # Detect OS
    os_type = detect_os()
    print(f"[DEBUG] Detected OS: {os_type}", flush=True)

    # Get script directory
    script_dir = get_script_dir()
    print(f"[DEBUG] Script directory: {script_dir}", flush=True)

    # Run appropriate notification
    print("[DEBUG] Running notification script...", flush=True)
    run_notification(os_type, script_dir, stdin_data)
    print("[DEBUG] Notification script completed!", flush=True)


if __name__ == "__main__":
    main()
