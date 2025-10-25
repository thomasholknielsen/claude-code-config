#!/usr/bin/env python
import json
import subprocess
import sys


try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
command = tool_input.get("command", "")

# Only validate git push commands
if tool_name != "Bash" or "git push" not in command:
    sys.exit(0)

# Get current branch
try:
    current_branch = subprocess.check_output(
        ["git", "branch", "--show-current"], stderr=subprocess.DEVNULL, text=True
    ).strip()
except subprocess.CalledProcessError:
    current_branch = ""

# Check if pushing to main or develop
push_cmd = command
is_force_push = "--force" in push_cmd or "-f" in push_cmd

# Check if command or current branch targets protected branches
targets_protected = "origin main" in push_cmd or "origin develop" in push_cmd or current_branch in ["main", "develop"]

# Block direct push to main/develop (unless force push which is already dangerous)
if (
    targets_protected
    and not is_force_push
    and (current_branch in ["main", "develop"] or "origin main" in push_cmd or "origin develop" in push_cmd)
):
    reason = f"""❌ Direct push to main/develop is not allowed!

Protected branches:
  - main (production)
  - develop (integration)

Git Flow workflow:
  1. Create a feature branch:
     /git-flow:feature <name>

  2. Make your changes and commit

  3. Push feature branch:
     git push origin feature/<name>

  4. Create pull request:
     /git:pr

  5. After approval, merge with:
     /git-flow:finish

For releases:
  /git-flow:release <version> → PR → /git-flow:finish

For hotfixes:
  /git-flow:hotfix <name> → PR → /git-flow:finish

Current branch: {current_branch}

💡 Use feature/release/hotfix branches instead of pushing directly to main/develop."""

    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    print(json.dumps(output))
    sys.exit(0)

# Allow the command
sys.exit(0)
