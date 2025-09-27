#!/usr/bin/env python

from datetime import datetime
import json
import re
import sys


input_data = json.load(sys.stdin)
tool_input = input_data.get("tool_input", {})
query = tool_input.get("query", "")
current_year = str(datetime.now().year)
has_year = re.search(r"\b20\d{2}\b", query)
has_temporal = any(word in query.lower() for word in ["latest", "recent", "current", "new", "now", "today"])
should_add_year = not has_year and not has_temporal
modified_query = f"{query} {current_year}" if should_add_year else query
modified_tool_input = {"query": modified_query}
hook_specific_output = {
    "hookEventName": "PreToolUse",
    "modifiedToolInput": modified_tool_input
}
output = {"hookSpecificOutput": hook_specific_output}
print(json.dumps(output))
sys.exit(0)
