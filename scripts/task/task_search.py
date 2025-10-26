#!/usr/bin/env python
"""Task search and ranking utility for task management commands

Provides testable task search functionality with relevance ranking.
Used by /task:execute, /task:search, and other task management commands.
"""

import json
from pathlib import Path
import re
import sys
from typing import Dict, List, Tuple


def load_tasks(tasks_file: Path) -> List[Dict]:
    """
    Load tasks from markdown file.

    Args:
        tasks_file: Path to tasks.md file

    Returns:
        List of task dictionaries with id, title, status, priority, category, description

    Raises:
        FileNotFoundError: If tasks file doesn't exist
        ValueError: If tasks file is empty or malformed
    """
    if not tasks_file.exists():
        raise FileNotFoundError(f"Tasks file not found: {tasks_file}")

    content = tasks_file.read_text()

    if not content.strip():
        raise ValueError("Tasks file is empty")

    tasks = []
    # Parse markdown format: ## [TASK-XXX] Title
    pattern = r"^##\s+\[TASK-(\d{3})\]\s+(.+?)$"

    for match in re.finditer(pattern, content, re.MULTILINE):
        task_id = f"TASK-{match.group(1)}"
        title = match.group(2).strip()

        # Extract task block until next task or end of file
        start_pos = match.end()
        next_match = re.search(pattern, content[start_pos:])
        end_pos = start_pos + next_match.start() if next_match else len(content)
        task_block = content[start_pos:end_pos]

        # Parse fields
        status_match = re.search(r"\*\*Status\*\*:\s*(\w+)", task_block)
        priority_match = re.search(r"\*\*Priority\*\*:\s*(\w+)", task_block)
        category_match = re.search(r"\*\*Category\*\*:\s*(\w+)", task_block)
        desc_match = re.search(r"\*\*Description\*\*:\s*(.+?)(?=\n\n|\*\*|---)", task_block, re.DOTALL)

        tasks.append(
            {
                "id": task_id,
                "title": title,
                "status": status_match.group(1) if status_match else "unknown",
                "priority": priority_match.group(1) if priority_match else "medium",
                "category": category_match.group(1) if category_match else "unknown",
                "description": desc_match.group(1).strip() if desc_match else "",
            }
        )

    return tasks


def rank_by_relevance(tasks: List[Dict], query: str) -> List[Tuple[Dict, int]]:
    """
    Rank tasks by relevance to search query.

    Scoring algorithm:
    - Exact phrase match in title: 100 points
    - All words match in title: 80 points
    - Most words match in title: 60 points
    - Any word match in title: 40 points
    - Match in description: -20 points (secondary)
    - Priority boost: high/critical +5, medium +2

    Args:
        tasks: List of task dictionaries
        query: Search query string

    Returns:
        List of (task, score) tuples sorted by score descending
    """
    query_lower = query.lower()
    query_words = query_lower.split()

    results = []

    for task in tasks:
        score = 0

        # Title scoring (primary)
        title_lower = task["title"].lower()

        # Exact phrase match
        if query_lower in title_lower:
            score += 100
        else:
            # Word-based matching
            matching_words = sum(1 for word in query_words if word in title_lower)
            total_words = len(query_words)

            if matching_words == total_words:
                score += 80
            elif matching_words > total_words * 0.5:
                score += 60
            elif matching_words > 0:
                score += 40

        # Description scoring (secondary)
        desc_lower = task["description"].lower()
        if query_lower in desc_lower:
            score += 20
        elif any(word in desc_lower for word in query_words):
            score += 10

        # Priority boost
        if task["priority"].lower() in ["critical", "high"]:
            score += 5
        elif task["priority"].lower() == "medium":
            score += 2

        # Only include if some relevance found
        if score > 0:
            results.append((task, score))

    # Sort by score descending
    results.sort(key=lambda x: x[1], reverse=True)
    return results


def search_tasks(
    query: str, tasks_file: Path, limit: int = 5, include_completed: bool = False
) -> List[Tuple[Dict, int]]:
    """
    Search tasks by query string with optional filtering.

    Args:
        query: Search query
        tasks_file: Path to tasks.md file
        limit: Maximum results to return (0 = unlimited)
        include_completed: Include completed tasks in results

    Returns:
        List of (task, score) tuples, ranked by relevance

    Raises:
        FileNotFoundError: If tasks file doesn't exist
        ValueError: If tasks file is empty or malformed
    """
    tasks = load_tasks(tasks_file)

    # Filter by status if not including completed
    if not include_completed:
        tasks = [t for t in tasks if t["status"] != "completed"]

    # Rank by relevance
    results = rank_by_relevance(tasks, query)

    # Apply limit
    if limit > 0:
        results = results[:limit]

    return results


def format_task_row(task: Dict, option: str) -> str:
    """
    Format single task as table row.

    Args:
        task: Task dictionary
        option: Option letter (A-Z)

    Returns:
        Formatted table row
    """
    # Status indicator
    status_map = {
        "completed": "[DONE]",
        "pending": "[ACTIVE]",
        "in-progress": "[ACTIVE]",
        "blocked": "[ACTIVE]",
    }
    status_str = status_map.get(task.get("status", "unknown"), "[NEW]")

    # Priority indicator
    priority_map = {
        "critical": "[!]",
        "high": "[!]",
        "medium": "[*]",
        "low": "-",
    }
    priority_str = priority_map.get(task.get("priority", "medium"), "-")

    # Title with truncation
    title = task.get("title", "Untitled")
    if len(title) > 60:
        title = title[:57] + "..."

    return f"| {option} | {status_str} | {priority_str} | {title} |"


def format_task_table(results: List[Tuple[Dict, int]], show_scores: bool = False) -> str:
    """
    Format search results as markdown table.

    Args:
        results: List of (task, score) tuples from search_tasks()
        show_scores: Include relevance scores in table

    Returns:
        Formatted markdown table
    """
    if not results:
        return "No matching tasks found."

    lines = []
    lines.append("")
    lines.append("| Option | Status | Priority | Task Description |")
    lines.append("|--------|--------|----------|------------------|")

    for i, (task, _) in enumerate(results):
        option = chr(65 + i)  # A, B, C, ...
        lines.append(format_task_row(task, option))

    if show_scores:
        lines.append("")
        lines.append(
            "(Relevance scores: "
            + ", ".join(f"{chr(65 + i)}={int(score)}" for i, (_, score) in enumerate(results))
            + ")"
        )

    return "\n".join(lines)


def validate_tasks_file(tasks_file: Path) -> Tuple[bool, str]:
    """
    Validate tasks file exists and is readable.

    Args:
        tasks_file: Path to tasks.md file

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not tasks_file.exists():
        return False, f"Tasks file not found: {tasks_file}"

    if not tasks_file.is_file():
        return False, f"Not a file: {tasks_file}"

    try:
        content = tasks_file.read_text()
        if not content.strip():
            return False, "Tasks file is empty"

        # Try to load tasks
        load_tasks(tasks_file)
        return True, ""
    except Exception as e:
        return False, f"Error reading tasks file: {e}"


def main():
    """CLI interface for task search utility"""
    if len(sys.argv) < 3:
        print("Usage: task_search.py search <query> <tasks-file> [--limit=5] [--completed]")
        print("       task_search.py validate <tasks-file>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "validate":
        if len(sys.argv) < 3:
            print("Usage: task_search.py validate <tasks-file>")
            sys.exit(1)
        tasks_file = Path(sys.argv[2])
        is_valid, error = validate_tasks_file(tasks_file)
        if is_valid:
            print(json.dumps({"valid": True, "error": ""}))
        else:
            print(json.dumps({"valid": False, "error": error}))
        sys.exit(0 if is_valid else 1)

    elif command == "search":
        if len(sys.argv) < 4:
            print("Usage: task_search.py search <query> <tasks-file> [--limit=5] [--completed]")
            sys.exit(1)

        query = sys.argv[2]
        tasks_file = Path(sys.argv[3])
        limit = 5
        include_completed = False

        # Parse options (skip first 4 args: program, search, query, tasks_file)
        for arg in sys.argv[4:]:
            if arg.startswith("--limit="):
                limit = int(arg.split("=")[1])
            elif arg == "--completed":
                include_completed = True

        try:
            results = search_tasks(query, tasks_file, limit, include_completed)
            output = {
                "query": query,
                "total_results": len(results),
                "results": [
                    {
                        "option": chr(65 + i),
                        "task_id": task["id"],
                        "title": task["title"],
                        "status": task["status"],
                        "priority": task["priority"],
                        "score": int(score),
                    }
                    for i, (task, score) in enumerate(results)
                ],
                "table": format_task_table(results),
            }
            print(json.dumps(output, indent=2))
        except Exception as e:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            sys.exit(1)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
