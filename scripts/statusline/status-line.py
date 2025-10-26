#!/usr/bin/env python
"""
Claude Code Context Monitor
Real-time context usage monitoring with visual indicators and session analytics
"""

import json
import os
import platform
from pathlib import Path
import re
import subprocess
import sys
from typing import Optional, Dict, Any


# Terminal capability detection
def supports_unicode() -> bool:
    """Check if terminal supports Unicode/emoji rendering via actual test."""
    # First: check encoding
    try:
        encoding = sys.stdout.encoding or ''
        # UTF-8 encoding explicitly supports Unicode
        if encoding.lower() in ('utf-8', 'utf8'):
            return True
        # Windows cp1252 (charmap) explicitly cannot render Unicode
        if 'cp' in encoding.lower() or 'iso' in encoding.lower():
            return False
    except Exception:
        pass

    # Second: try to actually render a test emoji
    test_emoji = '🔵'  # Blue circle - simple, common emoji
    try:
        # Try to encode the test emoji to stdout encoding
        test_str = f"test{test_emoji}test"
        test_str.encode(sys.stdout.encoding or 'utf-8')
        # If we get here, encoding succeeded - emoji will render
        return True
    except (UnicodeEncodeError, UnicodeDecodeError, AttributeError):
        # Encoding failed - emoji won't render
        return False

    # Third: fallback to terminal detection
    if platform.system() == 'Windows':
        # Check for known modern terminals
        term_program = os.environ.get('TERM_PROGRAM', '')
        term_emulator = os.environ.get('TERM', '')

        if term_program in ['WindowsTerminal', 'ConEmu']:
            return True
        if 'mintty' in term_emulator:  # Git Bash, Cygwin
            return True
        if 'ANSICON' in os.environ:
            return True
        return False

    # Unix/Linux/macOS: check environment
    if os.environ.get('PYTHONIOENCODING', '').lower() == 'utf-8':
        return True
    if os.environ.get('LANG', '').lower().endswith('utf-8'):
        return True

    return True


UNICODE_SUPPORTED = supports_unicode()


# Emoji definitions with ASCII fallback
EMOJI = {
    'status_unknown': '🔵' if UNICODE_SUPPORTED else '[?]',
    'critical': '🚨' if UNICODE_SUPPORTED else '[!]',
    'high': '🔴' if UNICODE_SUPPORTED else '[X]',
    'medium': '🟠' if UNICODE_SUPPORTED else '[~]',
    'warning': '🟡' if UNICODE_SUPPORTED else '[*]',
    'ok': '🟢' if UNICODE_SUPPORTED else '[OK]',
    'directory': '📁' if UNICODE_SUPPORTED else 'DIR',
    'context': '🧠' if UNICODE_SUPPORTED else 'CTX',
    'cost': '💰' if UNICODE_SUPPORTED else '$',
    'duration': '⏱' if UNICODE_SUPPORTED else 'T',
    'lines': '📝' if UNICODE_SUPPORTED else 'L',
    # Git Flow icons
    'git_feature': '🌿' if UNICODE_SUPPORTED else '[*]',
    'git_release': '🚀' if UNICODE_SUPPORTED else '[~]',
    'git_hotfix': '🔥' if UNICODE_SUPPORTED else '[!]',
    'git_develop': '🔀' if UNICODE_SUPPORTED else '[+]',
    'git_main': '🏠' if UNICODE_SUPPORTED else '[M]',
    'git_default': '📁' if UNICODE_SUPPORTED else 'GIT',
    'git_target': '🎯' if UNICODE_SUPPORTED else '>>',
    'git_ahead': '↑' if UNICODE_SUPPORTED else '^',
    'git_behind': '↓' if UNICODE_SUPPORTED else 'v',
    'git_modified': '●' if UNICODE_SUPPORTED else '*',
    'git_added': '✚' if UNICODE_SUPPORTED else '+',
    'git_deleted': '✖' if UNICODE_SUPPORTED else 'x',
}


def parse_context_from_transcript(transcript_path: str) -> Optional[Dict[str, Any]]:
    """Parse context usage from transcript file with cache tracking and system message parsing."""
    if not transcript_path:
        # Try to find transcript in common locations
        transcript_path = find_transcript_file()
        if not transcript_path:
            return None

    transcript_path_obj = Path(transcript_path)
    if not transcript_path_obj.exists():
        return None

    try:
        with transcript_path_obj.open(encoding='utf-8') as f:
            lines = f.readlines()

        # Check last 15 lines for context information
        recent_lines = lines[-15:] if len(lines) > 15 else lines

        for line in reversed(recent_lines):
            try:
                data = json.loads(line.strip())

                # Method 1: Parse usage tokens from assistant messages (most accurate)
                if data.get("type") == "assistant":
                    message = data.get("message", {})
                    usage = message.get("usage", {})

                    if usage:
                        input_tokens = usage.get("input_tokens", 0)
                        cache_read = usage.get("cache_read_input_tokens", 0)
                        cache_creation = usage.get("cache_creation_input_tokens", 0)

                        # Total tokens for percentage calculation
                        total_tokens = input_tokens + cache_read + cache_creation
                        if total_tokens > 0:
                            percent_used = min(100, (total_tokens / 200000) * 100)
                            return {
                                "percent": percent_used,
                                "tokens": total_tokens,
                                "input_tokens": input_tokens,
                                "cache_read": cache_read,
                                "cache_creation": cache_creation,
                                "cache_total": cache_read + cache_creation,
                                "method": "usage",
                                "warning": None
                            }

                # Method 2: Parse system context warnings (backup + alerts)
                elif data.get("type") == "system_message":
                    content = data.get("content", "")

                    # Check for auto-compact warning
                    match = re.search(r"Context left until auto-compact: (\d+)%", content)
                    if match:
                        percent_left = int(match.group(1))
                        return {
                            "percent": 100 - percent_left,
                            "tokens": None,
                            "method": "system",
                            "warning": "auto-compact"
                        }

                    # Check for "Context low" warning
                    match = re.search(r"Context low \((\d+)% remaining\)", content)
                    if match:
                        percent_left = int(match.group(1))
                        return {
                            "percent": 100 - percent_left,
                            "tokens": None,
                            "method": "system",
                            "warning": "low"
                        }

            except (json.JSONDecodeError, KeyError, ValueError):
                continue

        return None

    except (FileNotFoundError, PermissionError, IOError):
        return None


def find_transcript_file() -> Optional[str]:
    """Find transcript file in common Claude Code locations."""
    try:
        home = Path.home()
        common_paths = [
            home / ".claude" / "transcript.jsonl",
            home / ".claude" / "sessions" / "current" / "transcript.jsonl",
            Path.cwd() / ".claude" / "transcript.jsonl",
        ]

        for path in common_paths:
            if path.exists():
                return str(path)
    except Exception:
        pass
    return None


def get_context_display(context_info: Optional[Dict[str, Any]]) -> str:
    """Generate context display with progress bar, cache info, and alerts."""
    if not context_info:
        return f"{EMOJI['status_unknown']} ???"

    percent = context_info.get("percent", 0)
    warning = context_info.get("warning")
    cache_total = context_info.get("cache_total", 0)

    # Color and icon based on usage level
    if percent >= 95:
        icon, color = EMOJI['critical'], "\033[31;1m"  # Critical red
        alert = "CRIT"
    elif percent >= 90:
        icon, color = EMOJI['high'], "\033[31m"  # Red
        alert = "HIGH"
    elif percent >= 75:
        icon, color = EMOJI['medium'], "\033[91m"  # Light red
        alert = ""
    elif percent >= 50:
        icon, color = EMOJI['warning'], "\033[33m"  # Yellow
        alert = ""
    else:
        icon, color = EMOJI['ok'], "\033[32m"  # Green
        alert = ""

    # Create progress bar (ASCII fallback if needed)
    segments = 8
    filled = int((percent / 100) * segments)
    if UNICODE_SUPPORTED:
        bar = "█" * filled + "▁" * (segments - filled)
    else:
        bar = "=" * filled + "-" * (segments - filled)

    # Build cache info if available with color indicating efficiency
    cache_str = ""
    if cache_total > 0:
        cache_kb = cache_total / 1000
        # Color cache efficiency: higher cache = better reuse (cyan/bright)
        cache_color = "\033[36m"  # Cyan for cache hits (efficient)
        cache_str = f" {cache_color}(cache:{cache_kb:.0f}k)\033[0m"

    # Special warnings override normal alert
    if warning == "auto-compact":
        alert = "AUTO-COMPACT!"
        color = "\033[31m"  # Red for auto-compact
    elif warning == "low":
        alert = "LOW!"
        color = "\033[31m"  # Red for low

    reset = "\033[0m"
    alert_str = f" {alert}" if alert else ""

    return f"{icon}{color}{bar}{reset} {percent:.0f}%{cache_str}{alert_str}"


def get_directory_display(workspace_data: Dict[str, Any]) -> str:
    """Get directory display name with cross-platform path handling."""
    current_dir = workspace_data.get("current_dir", "")
    project_dir = workspace_data.get("project_dir", "")

    try:
        if current_dir and project_dir:
            current_path = Path(current_dir)
            project_path = Path(project_dir)

            # Check if current_dir is within project_dir (cross-platform)
            try:
                rel_path = current_path.relative_to(project_path)
                return str(rel_path) or project_path.name
            except ValueError:
                # current_dir is not relative to project_dir
                return current_path.name

        if project_dir:
            return Path(project_dir).name
        if current_dir:
            return Path(current_dir).name
    except Exception:
        pass

    return "unknown"


def get_session_metrics(cost_data: Optional[Dict[str, Any]]) -> str:
    """Get session metrics display."""
    if not cost_data:
        return ""

    metrics = []

    # Cost
    cost_usd = cost_data.get("total_cost_usd", 0)
    if cost_usd > 0:
        if cost_usd >= 0.10:
            cost_color = "\033[31m"  # Red for expensive
        elif cost_usd >= 0.05:
            cost_color = "\033[33m"  # Yellow for moderate
        else:
            cost_color = "\033[32m"  # Green for cheap

        cost_str = f"{cost_usd * 100:.0f}¢" if cost_usd < 0.01 else f"{cost_usd:.3f}"
        metrics.append(f"{cost_color}{EMOJI['cost']}{cost_str}\033[0m")

    # Duration
    duration_ms = cost_data.get("total_duration_ms", 0)
    if duration_ms > 0:
        minutes = duration_ms / 60000
        duration_color = "\033[33m" if minutes >= 30 else "\033[32m"
        duration_str = f"{duration_ms // 1000}s" if minutes < 1 else f"{minutes:.0f}m"
        metrics.append(f"{duration_color}{EMOJI['duration']} {duration_str}\033[0m")

    return f" \033[90m|\033[0m {' '.join(metrics)}" if metrics else ""


def get_git_flow_status() -> str:
    """Get Git Flow branch status with sync and change indicators."""
    try:
        # Check if in a git repository
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            capture_output=True,
            text=True,
            timeout=1
        )
        if result.returncode != 0:
            return ""  # Not a git repo

        # Get current branch
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            timeout=1
        )
        branch = result.stdout.strip()
        if not branch:
            return ""  # Detached HEAD

        # Determine branch type and get icon
        icon = EMOJI['git_default']
        target = ""

        if branch.startswith("feature/"):
            icon = EMOJI['git_feature']
            target = "develop"
        elif branch.startswith("release/"):
            icon = EMOJI['git_release']
            target = "main"
        elif branch.startswith("hotfix/"):
            icon = EMOJI['git_hotfix']
            target = "main+develop"
        elif branch == "develop":
            icon = EMOJI['git_develop']
        elif branch in ("main", "master"):
            icon = EMOJI['git_main']

        # Get commits ahead/behind
        sync_info = ""
        ahead = 0
        behind = 0

        try:
            ahead_result = subprocess.run(
                ["git", "rev-list", "--count", "@{u}..HEAD"],
                capture_output=True,
                text=True,
                timeout=1
            )
            ahead = int(ahead_result.stdout.strip()) if ahead_result.returncode == 0 else 0
        except (ValueError, subprocess.TimeoutExpired):
            pass

        try:
            behind_result = subprocess.run(
                ["git", "rev-list", "--count", "HEAD..@{u}"],
                capture_output=True,
                text=True,
                timeout=1
            )
            behind = int(behind_result.stdout.strip()) if behind_result.returncode == 0 else 0
        except (ValueError, subprocess.TimeoutExpired):
            pass

        # Format sync status with color-coding based on state
        if ahead > 0 and behind > 0:
            # Diverged: red (conflict state)
            sync_color = "\033[31m"  # Red
            sync_info = f"{sync_color}[DIVERGED:+{ahead}/-{behind}]\033[0m"
        elif ahead > 0:
            # Ahead: green (ready to push)
            sync_color = "\033[32m"  # Green
            sync_info = f"{sync_color}[AHEAD:+{ahead}]\033[0m"
        elif behind > 0:
            # Behind: yellow (needs pull)
            sync_color = "\033[33m"  # Yellow
            sync_info = f"{sync_color}[BEHIND:-{behind}]\033[0m"
        else:
            # In sync: green (good state)
            sync_color = "\033[32m"  # Green
            sync_info = f"{sync_color}[IN-SYNC]\033[0m"

        # Format output with colored branch name
        branch_info = f"{icon} {sync_color}{branch}\033[0m{sync_info}"

        if target:
            branch_info = f"{branch_info} {EMOJI['git_target']} {target}"

        return f" | {branch_info}"

    except Exception:
        return ""  # Silent fail for any git operations


def main() -> None:
    try:
        # Debug: log that script was called (Windows path)
        debug_log = Path.home() / '.claude' / 'statusline-debug.log'
        try:
            with debug_log.open('a', encoding='utf-8') as f:
                f.write('Status line script called\n')
        except Exception:
            pass  # Silent fail on debug logging

        # Read JSON input from Claude Code
        data = json.load(sys.stdin)

        # Extract information
        model_name = data.get("model", {}).get("display_name", "Claude")
        workspace = data.get("workspace", {})
        transcript_path = data.get("transcript_path", "")
        cost_data = data.get("cost", {})

        # Parse context usage
        context_info = parse_context_from_transcript(transcript_path)

        # Build status components
        context_display = get_context_display(context_info)
        directory = get_directory_display(workspace)
        session_metrics = get_session_metrics(cost_data)

        # Model display with context-aware coloring
        if context_info:
            percent = context_info.get("percent", 0)
            if percent >= 90:
                model_color = "\033[31m"  # Red
            elif percent >= 75:
                model_color = "\033[33m"  # Yellow
            else:
                model_color = "\033[32m"  # Green

            model_display = f"{model_color}[{model_name}]\033[0m"
        else:
            model_display = f"\033[94m[{model_name}]\033[0m"

        # Get Git Flow status (if in a git repo)
        git_flow_status = get_git_flow_status()

        # Combine all components in order: Model + Context | Git | Metrics
        # Include context display if available (shows progress bar and cache info)
        context_part = f" {EMOJI['context']} {context_display}" if context_display else ""

        # Build final status line with reordered components
        # Order: [Model] Context | Git | Metrics
        status_line = f"{model_display}{context_part}{git_flow_status}{session_metrics}"

        print(status_line)

    except Exception as e:
        # Fallback display with full error message (safe encoding)
        error_msg = str(e)
        # Encode to ASCII with backslashreplace to avoid charmap errors
        try:
            error_msg_safe = error_msg.encode('ascii', 'backslashreplace').decode('ascii')
        except Exception:
            error_msg_safe = "Unknown error"

        if len(error_msg_safe) > 50:
            error_msg_safe = error_msg_safe[:47] + "..."
        print(f"\033[94m[Claude]\033[0m \033[93m{EMOJI['directory']} {Path.cwd().name}\033[0m {EMOJI['context']} \033[31m[Error: {error_msg_safe}]\033[0m")


if __name__ == "__main__":
    main()
