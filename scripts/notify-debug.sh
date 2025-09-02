#!/bin/bash
# Debug version of the notification script

# Log to file for debugging
DEBUG_LOG="/tmp/claude-hook-debug.log"
echo "$(date): Hook triggered" >> "$DEBUG_LOG"

# Read hook input data from standard input
INPUT=$(cat)
echo "$(date): Input received: $INPUT" >> "$DEBUG_LOG"

# Get current session directory name
SESSION_DIR=$(basename "$(pwd)")
echo "$(date): Session dir: $SESSION_DIR" >> "$DEBUG_LOG"

# Send a simple notification
terminal-notifier -message "Stop hook triggered in $SESSION_DIR" -title "🔍 Debug Hook" -sound Glass
echo "$(date): Notification sent" >> "$DEBUG_LOG"