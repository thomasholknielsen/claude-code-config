#!/bin/sh
# ~/.claude/scripts/notify-cross-platform.sh
# Cross-platform notification script that detects OS and routes to appropriate handler

# Detect the operating system
OS="unknown"
if [ "$(uname)" = "Darwin" ]; then
    OS="macos"
elif [ "$(uname -s | grep -i 'MINGW\|MSYS\|CYGWIN')" != "" ] || [ "$OS" = "Windows_NT" ]; then
    OS="windows"
elif [ "$(uname)" = "Linux" ]; then
    # Check if running in WSL
    if grep -q Microsoft /proc/version 2>/dev/null; then
        OS="wsl"
    else
        OS="linux"
    fi
fi

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Route to appropriate platform-specific script
case "$OS" in
    macos)
        # Use the existing macOS script
        exec bash "$SCRIPT_DIR/notify-smart.sh"
        ;;
    windows)
        # On native Windows (Git Bash, MSYS2, etc.), use PowerShell
        # Read stdin and pass it to PowerShell script
        INPUT=$(cat)
        echo "$INPUT" | powershell.exe -ExecutionPolicy Bypass -File "$SCRIPT_DIR/notify-smart.ps1"
        ;;
    wsl)
        # In WSL, try to use Windows notifications via PowerShell
        INPUT=$(cat)
        # Convert WSL path to Windows path for the script
        WIN_SCRIPT_PATH=$(wslpath -w "$SCRIPT_DIR/notify-smart.ps1" 2>/dev/null || echo "$SCRIPT_DIR/notify-smart.ps1")
        echo "$INPUT" | powershell.exe -ExecutionPolicy Bypass -File "$WIN_SCRIPT_PATH"
        ;;
    linux)
        # Native Linux - use notify-send if available
        INPUT=$(cat)
        SESSION_DIR=$(basename "$(pwd)")
        
        # Try to extract message from input (similar to macOS script)
        if command -v jq >/dev/null 2>&1; then
            TRANSCRIPT_PATH=$(echo "$INPUT" | jq -r '.transcript_path // empty')
            if [ -f "$TRANSCRIPT_PATH" ] && [ -n "$TRANSCRIPT_PATH" ]; then
                MSG=$(tail -10 "$TRANSCRIPT_PATH" 2>/dev/null | \
                      jq -r 'select(.message.role == "assistant") | .message.content[0].text // empty' 2>/dev/null | \
                      tail -1 | \
                      tr '\n' ' ' | \
                      sed 's/[[:space:]]\+/ /g' | \
                      cut -c1-60)
                if [ -n "$MSG" ] && [ ${#MSG} -eq 60 ]; then
                    MSG="${MSG}..."
                fi
            fi
        fi
        
        MSG=${MSG:-"Task completed successfully"}
        
        # Use notify-send for Linux desktop notifications
        if command -v notify-send >/dev/null 2>&1; then
            notify-send "✅ Claude Code ($SESSION_DIR)" "$MSG"
        else
            # Fallback to console output if no notification system
            echo "✅ Claude Code ($SESSION_DIR): $MSG"
        fi
        ;;
    *)
        # Unknown OS - just echo to console
        echo "Claude Code notification: Task completed (OS: $OS)"
        ;;
esac