#!/bin/bash
"""
macOS helper script for cross-platform user prompt logging.
Handles macOS-specific operations and calls the main Python logging script.
"""

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Path to the main Python logging script
PYTHON_SCRIPT="$SCRIPT_DIR/log-prompt.py"

# Ensure the Python script exists
if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    echo "[ERROR] Python logging script not found: $PYTHON_SCRIPT" >&2
    exit 1
fi

# Ensure the Python script is executable
chmod +x "$PYTHON_SCRIPT" 2>/dev/null

# Create logs directory if it doesn't exist
LOGS_DIR="$HOME/.claude/logs"
if [[ ! -d "$LOGS_DIR" ]]; then
    mkdir -p "$LOGS_DIR" 2>/dev/null || {
        echo "[WARNING] Could not create logs directory: $LOGS_DIR" >&2
        # Continue anyway - the Python script will handle fallback
    }
fi

# Set proper permissions on logs directory (readable/writable by user only)
if [[ -d "$LOGS_DIR" ]]; then
    chmod 700 "$LOGS_DIR" 2>/dev/null
fi

# Run the Python logging script with all stdin data
# Use python3 explicitly to ensure we're using Python 3
if command -v python3 &> /dev/null; then
    python3 "$PYTHON_SCRIPT"
    exit_code=$?
elif command -v python &> /dev/null; then
    # Fallback to 'python' command
    python "$PYTHON_SCRIPT"
    exit_code=$?
else
    echo "[ERROR] Python not found. Please install Python 3." >&2
    exit 1
fi

# Exit with the same code as the Python script
exit $exit_code