#!/bin/bash
# ~/.claude/scripts/hooks/notify-smart.sh
# Smart notification script for Claude Code hooks

# Read hook input data from standard input
INPUT=$(cat)

# Get current session directory name (hooks run in the same directory as the session)
SESSION_DIR=$(basename "$(pwd)")

# Extract transcript_path from the input
TRANSCRIPT_PATH=$(echo "$INPUT" | jq -r '.transcript_path // empty')

# Default message
DEFAULT_MSG="Task completed successfully"

# Try to get the latest assistant message if transcript exists
if [ -f "$TRANSCRIPT_PATH" ] && [ -n "$TRANSCRIPT_PATH" ]; then
    # Extract assistant messages from the last 10 lines and get the latest one
    # Remove newlines and limit to 60 characters
    MSG=$(tail -10 "$TRANSCRIPT_PATH" 2>/dev/null | \
          jq -r 'select(.message.role == "assistant") | .message.content[0].text // empty' 2>/dev/null | \
          tail -1 | \
          tr '\n' ' ' | \
          sed 's/[[:space:]]\+/ /g' | \
          cut -c1-60)

    # Clean up the message and add ellipsis if truncated
    if [ -n "$MSG" ] && [ ${#MSG} -eq 60 ]; then
        MSG="${MSG}..."
    fi

    # Use default if no message was retrieved
    MSG=${MSG:-$DEFAULT_MSG}
else
    MSG=$DEFAULT_MSG
fi

# Configuration: Choose notification method
# Set to "terminal-notifier" or "osascript"
NOTIFICATION_METHOD="terminal-notifier"

# Display notification based on chosen method
if [ "$NOTIFICATION_METHOD" = "osascript" ]; then
    # Native macOS notification
    osascript -e "display notification \"$MSG\" with title \"✅ Claude Code ($SESSION_DIR)\" sound name \"Glass\""
else
    # Terminal-notifier (fallback)
    if command -v terminal-notifier > /dev/null 2>&1; then
        terminal-notifier -message "$MSG" -title "✅ Claude Code ($SESSION_DIR)" -sound Glass -activate 'com.microsoft.VSCode'
    else
        # Fallback to osascript if terminal-notifier not available
        osascript -e "display notification \"$MSG\" with title \"✅ Claude Code ($SESSION_DIR)\" sound name \"Glass\""
    fi
fi
