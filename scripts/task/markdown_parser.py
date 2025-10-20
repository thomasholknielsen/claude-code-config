#!/usr/bin/env python3
"""Shared markdown parser for task markdown files.

Provides utilities for parsing and extracting task metadata from markdown format.
Single source of truth for markdown parsing logic to prevent duplication.
"""

import re
from typing import Dict, List, Optional, Tuple


def parse_task_blocks(content: str) -> List[Tuple[str, str]]:
    """Extract task ID and task block from markdown content.

    Args:
        content: Full markdown file content

    Returns:
        List of (task_id, task_block) tuples

    Raises:
        ValueError: If content is not a string
    """
    # Input validation
    if not isinstance(content, str):
        raise ValueError(f"Expected string content, got {type(content).__name__}")

    if not content:
        return []

    pattern = r"^##\s+\[TASK-(\d{3})\]\s+(.+?)$"
    blocks = []

    for match in re.finditer(pattern, content, re.MULTILINE):
        task_id = f"TASK-{match.group(1)}"

        # Extract task block until next task
        start_pos = match.end()
        next_match = re.search(pattern, content[start_pos:])
        end_pos = start_pos + next_match.start() if next_match else len(content)
        task_block = content[start_pos:end_pos]

        blocks.append((task_id, task_block))

    return blocks


def extract_field(task_block: str, field_name: str, multiline: bool = False) -> Optional[str]:
    """Extract a single field from task block.

    Args:
        task_block: Task markdown block
        field_name: Name of field (e.g., "Status", "Priority")
        multiline: If True, allow content spanning multiple lines

    Returns:
        Field value or None if not found
    """
    if multiline:
        pattern = rf"\*\*{field_name}\*\*:\s*(.+?)(?=\n\n|\*\*|---)"
        match = re.search(pattern, task_block, re.DOTALL)
    else:
        pattern = rf"\*\*{field_name}\*\*:\s*(\w+)"
        match = re.search(pattern, task_block)

    return match.group(1).strip() if match else None


def extract_text_field(task_block: str, field_name: str) -> Optional[str]:
    """Extract a text field (can contain spaces and multiple words).

    Args:
        task_block: Task markdown block
        field_name: Name of field (e.g., "Epic", "Description")

    Returns:
        Field value or None if not found
    """
    pattern = rf"\*\*{field_name}\*\*:\s*(.+?)(?:\n|\*\*)"
    match = re.search(pattern, task_block)
    return match.group(1).strip() if match else None


def parse_depends_on(task_block: str) -> List[str]:
    """Parse the "Depends On" field into list of task IDs.

    Args:
        task_block: Task markdown block

    Returns:
        List of task IDs or empty list
    """
    depends_text = extract_text_field(task_block, "Depends On")

    if not depends_text or depends_text == "(none)":
        return []

    return [t.strip() for t in depends_text.split(",")]


def parse_task_full(task_id: str, task_block: str, include_optional: bool = False) -> Dict:
    """Parse complete task from markdown block.

    Args:
        task_id: Task ID (e.g., "TASK-001")
        task_block: Task markdown block
        include_optional: If True, include optional fields like category, description

    Returns:
        Dictionary with parsed task data
    """
    task_data = {
        "id": task_id,
        "status": extract_field(task_block, "Status") or "pending",
        "priority": extract_field(task_block, "Priority") or "medium",
        "epic": extract_text_field(task_block, "Epic"),
        "depends_on": parse_depends_on(task_block),
    }

    if include_optional:
        task_data["category"] = extract_field(task_block, "Category") or "chore"
        task_data["description"] = extract_text_field(task_block, "Description") or ""

    return task_data
