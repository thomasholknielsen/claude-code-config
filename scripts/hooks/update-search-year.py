#!/usr/bin/env python3
"""
Pre-tool-use hook to automatically add current year to web search queries
when no year or temporal keywords are detected.
"""

from datetime import datetime
import json
import re
import sys


def main() -> None:
    """
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
    """
    try:
        # Read and parse JSON input
        try:
            input_data = json.load(sys.stdin)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
            sys.exit(1)

        # Validate input structure
        if not isinstance(input_data, dict):
            print("Error: Input must be a JSON object", file=sys.stderr)
            sys.exit(1)

        # Extract tool input
        tool_input = input_data.get("tool_input")
        if tool_input is None:
            print("Error: Missing 'tool_input' field", file=sys.stderr)
            sys.exit(1)

        if not isinstance(tool_input, dict):
            print("Error: 'tool_input' must be a JSON object", file=sys.stderr)
            sys.exit(1)

        # Extract query
        query = tool_input.get("query", "")
        if not isinstance(query, str):
            print("Error: 'query' must be a string", file=sys.stderr)
            sys.exit(1)

        # Get current year
        current_year = str(datetime.now().year)

        # Check if query already has a year (2000-2099)
        has_year = re.search(r"\b20\d{2}\b", query)

        # Check for temporal keywords
        temporal_keywords = ["latest", "recent", "current", "new", "now", "today"]
        has_temporal = any(word in query.lower() for word in temporal_keywords)

        # Add year only if neither year nor temporal keywords are present
        should_add_year = not has_year and not has_temporal
        modified_query = f"{query} {current_year}" if should_add_year else query

        # Build output
        modified_tool_input = {"query": modified_query}
        hook_specific_output = {"hookEventName": "PreToolUse", "modifiedToolInput": modified_tool_input}
        output = {"hookSpecificOutput": hook_specific_output}

        # Output modified query
        print(json.dumps(output))
        sys.exit(0)

    except Exception as e:
        print(f"Unexpected error in search year update hook: {e}", file=sys.stderr)
        # Pass through original query on error
        try:
            fallback_output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "modifiedToolInput": {"query": query if "query" in locals() else ""},
                }
            }
            print(json.dumps(fallback_output))
        except Exception:
            # If even fallback fails, exit with error
            pass
        sys.exit(1)


if __name__ == "__main__":
    main()
