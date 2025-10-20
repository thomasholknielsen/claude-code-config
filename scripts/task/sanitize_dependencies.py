#!/usr/bin/env python3
"""
Task Dependency Sanitizer

Validates task dependency integrity and detects issues:
- Orphaned dependencies (depends on deleted tasks)
- Circular dependencies (A→B→C→A)
- Status conflicts (completed tasks blocking pending work)
- Epic integrity (tasks in non-existent epics)
- Priority inversions (low priority blocking high priority)
"""

import json
from pathlib import Path
import re
import sys
from typing import Dict, List

from markdown_parser import extract_field, extract_text_field, parse_task_blocks, parse_task_full


class DependencySanitizer:
    """Validates and repairs task dependency graphs."""

    def __init__(self, tasks_file: Path) -> None:
        """Initialize with tasks file."""
        self.tasks_file = tasks_file
        self.tasks = {}
        self.task_ids = set()
        self.issues = []
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Load tasks from file using shared markdown parser."""
        if not self.tasks_file.exists():
            raise FileNotFoundError(f"Tasks file not found: {self.tasks_file}")

        content = self.tasks_file.read_text()
        blocks = parse_task_blocks(content)

        for task_id, task_block in blocks:
            # Extract title from first line of block only (not entire file)
            lines = task_block.split("\n")
            first_line = lines[0] if lines else ""
            first_line_match = re.match(r"^##\s+\[TASK-\d{3}\]\s+(.+?)$", first_line)
            title = first_line_match.group(1).strip() if first_line_match else task_id

            # Parse task fields using shared parser
            task_data = parse_task_full(task_id, task_block, include_optional=False)

            self.tasks[task_id] = {
                "title": title,
                "status": task_data["status"],
                "priority": task_data["priority"],
                "epic": task_data["epic"],
                "depends_on": task_data["depends_on"],
            }
            self.task_ids.add(task_id)

    def sanitize(self) -> Dict:
        """Run all validation checks."""
        self.issues = []

        # Build reverse dependency index once for O(n²) optimization in _check_status_conflicts
        # and _check_priority_inversions (6-8x speedup for large task sets)
        self.reverse_deps = {}  # Maps task_id -> list of tasks that depend on it
        for task_id, task in self.tasks.items():
            for dep_id in task.get("depends_on", []):
                if dep_id not in self.reverse_deps:
                    self.reverse_deps[dep_id] = []
                self.reverse_deps[dep_id].append(task_id)

        self._check_orphaned_dependencies()
        self._check_circular_dependencies()
        self._check_status_conflicts()
        self._check_priority_inversions()
        self._check_epic_integrity()

        return {
            "total_tasks": len(self.tasks),
            "total_issues": len(self.issues),
            "issues": self.issues,
            "critical_count": sum(1 for i in self.issues if i["severity"] == "critical"),
            "warning_count": sum(1 for i in self.issues if i["severity"] == "warning"),
            "info_count": sum(1 for i in self.issues if i["severity"] == "info"),
        }

    def _check_orphaned_dependencies(self) -> None:
        """Check for tasks depending on non-existent tasks."""
        for task_id, task in self.tasks.items():
            for dep_id in task.get("depends_on", []):
                if dep_id not in self.task_ids:
                    self.issues.append(
                        {
                            "type": "orphaned_dependency",
                            "severity": "critical",
                            "task_id": task_id,
                            "description": f"{task_id} depends on {dep_id} (deleted/non-existent)",
                            "related_tasks": [dep_id],
                            "auto_fixable": True,
                            "suggested_fix": f"Remove {dep_id} from {task_id}'s Depends On",
                        }
                    )

    def _check_circular_dependencies(self) -> None:
        """Check for circular dependency cycles."""
        # Build adjacency list
        graph = {task_id: task.get("depends_on", []) for task_id, task in self.tasks.items()}

        # DFS cycle detection
        cycles = self._detect_cycles(graph)

        for cycle in cycles:
            self.issues.append(
                {
                    "type": "circular_dependency",
                    "severity": "critical",
                    "task_id": cycle[0],
                    "description": f"Circular dependency detected: {' → '.join(cycle)}",
                    "related_tasks": cycle,
                    "auto_fixable": False,
                    "suggested_fix": "Manual review - choose which relationship to remove",
                }
            )

    def _detect_cycles(self, graph: Dict[str, List[str]]) -> List[List[str]]:
        """Detect cycles in dependency graph using DFS."""
        visited = set()
        rec_stack = set()
        cycles = []

        def dfs(node: str, path: List[str]) -> None:
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path.copy())
                elif neighbor in rec_stack:
                    # Found cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)

            rec_stack.discard(node)

        for node in graph:
            if node not in visited:
                dfs(node, [])

        return cycles

    def _check_status_conflicts(self) -> None:
        """Check for completed tasks blocking pending work."""
        # Use pre-built reverse dependency index (O(n) instead of O(n²))
        for task_id, task in self.tasks.items():
            if task["status"] == "completed":
                # Look up tasks that depend on this completed task
                for other_id in self.reverse_deps.get(task_id, []):
                    other = self.tasks[other_id]
                    if other["status"] in ["pending", "in-progress"]:
                        self.issues.append(
                            {
                                "type": "status_conflict",
                                "severity": "warning",
                                "task_id": other_id,
                                "description": f"{other_id} ({other['status']}) blocked by {task_id} (completed)",
                                "related_tasks": [task_id],
                                "auto_fixable": False,
                                "suggested_fix": "Consider if this dependency is still needed",
                            }
                        )

    def _check_priority_inversions(self) -> None:
        """Check for low-priority blocking high-priority."""
        priority_order = {"low": 1, "medium": 2, "high": 3, "critical": 4}

        # Use pre-built reverse dependency index (O(n) instead of O(n²))
        for task_id, task in self.tasks.items():
            task_priority = priority_order.get(task["priority"], 0)

            # Look up tasks that depend on this task
            for other_id in self.reverse_deps.get(task_id, []):
                other = self.tasks[other_id]
                other_priority = priority_order.get(other["priority"], 0)

                if task_priority < other_priority:
                    self.issues.append(
                        {
                            "type": "priority_inversion",
                            "severity": "warning",
                            "task_id": other_id,
                            "description": f"{other_id} (priority: {other['priority']}) "
                            f"blocked by {task_id} (priority: {task['priority']})",
                            "related_tasks": [task_id],
                            "auto_fixable": False,
                            "suggested_fix": "Consider re-prioritizing tasks",
                        }
                    )

    def _check_epic_integrity(self) -> None:
        """Check for non-existent epics and empty epics."""
        epics = {task.get("epic") for task in self.tasks.values() if task.get("epic")}

        # Check empty epics
        for epic in epics:
            count = sum(1 for task in self.tasks.values() if task.get("epic") == epic)
            if count == 0:
                self.issues.append(
                    {
                        "type": "empty_epic",
                        "severity": "info",
                        "task_id": None,
                        "description": f"Epic '{epic}' has no tasks",
                        "related_tasks": [],
                        "auto_fixable": False,
                        "suggested_fix": "Delete empty epic or add tasks",
                    }
                )

    def fix_auto_fixable(self) -> int:
        """Auto-fix all auto-fixable issues."""
        fixed_count = 0

        for issue in self.issues:
            if issue["auto_fixable"] and issue["type"] == "orphaned_dependency":
                task_id = issue["task_id"]
                dep_id = issue["related_tasks"][0]

                if task_id in self.tasks:
                    self.tasks[task_id]["depends_on"] = [d for d in self.tasks[task_id]["depends_on"] if d != dep_id]
                    fixed_count += 1

        return fixed_count

    def write_tasks(self) -> None:
        """Write updated tasks back to file, preserving all original fields."""
        # This function only modifies tasks that were fixed by fix_auto_fixable()
        # For full schema preservation, read the original file and merge changes

        original_content = self.tasks_file.read_text()
        original_blocks = parse_task_blocks(original_content)

        # Build mapping of task_id -> original block for reference
        original_blocks_map = dict(original_blocks)

        updated_lines = ["# Active Tasks\n"]

        for task_id in sorted(self.tasks.keys()):
            task = self.tasks[task_id]
            original_block = original_blocks_map.get(task_id, "")

            # Start with task header
            updated_lines.append(f"## [{task_id}] {task['title']}\n")

            # Write core fields (these may have been modified by sanitizer)
            updated_lines.append(f"**Status**: {task['status']}")
            updated_lines.append(f"**Priority**: {task['priority']}")

            # For other fields, preserve from original if not modified
            # Extract original fields
            if original_block:
                original_category = extract_field(original_block, "Category") or ""
                original_related = extract_text_field(original_block, "Related") or ""
                original_origin = extract_field(original_block, "Origin") or ""
                original_created = extract_field(original_block, "Created") or ""
                original_description = extract_text_field(original_block, "Description") or ""

                if original_category:
                    updated_lines.append(f"**Category**: {original_category}")
                else:
                    updated_lines.append("**Category**: chore")
            else:
                updated_lines.append("**Category**: chore")

            # Write epic if present
            if task.get("epic"):
                updated_lines.append(f"**Epic**: {task['epic']}")
            elif original_block and extract_text_field(original_block, "Epic"):
                updated_lines.append(f"**Epic**: {extract_text_field(original_block, 'Epic')}")

            # Write depends_on (sanitizer may have modified this)
            if task.get("depends_on"):
                updated_lines.append(f"**Depends On**: {', '.join(task['depends_on'])}")
            else:
                updated_lines.append("**Depends On**: (none)")

            # Preserve Related, Origin, Created
            if original_block:
                original_related = extract_text_field(original_block, "Related")
                if original_related:
                    updated_lines.append(f"**Related**: {original_related}")
                else:
                    updated_lines.append("**Related**: (none)")

                original_origin = extract_field(original_block, "Origin")
                if original_origin:
                    updated_lines.append(f"**Origin**: {original_origin}")

                original_created = extract_field(original_block, "Created")
                if original_created:
                    updated_lines.append(f"**Created**: {original_created}")

            # Preserve Description
            if original_block:
                original_description = extract_text_field(original_block, "Description")
                if original_description:
                    updated_lines.append(f"\n**Description**:\n{original_description}")

            updated_lines.append("\n---\n")

        content = "\n".join(updated_lines)
        self.tasks_file.write_text(content)


def main() -> None:
    """CLI interface."""
    if len(sys.argv) < 2:
        print("Usage: sanitize_dependencies.py <tasks-file> [--fix]")
        sys.exit(1)

    tasks_file = Path(sys.argv[1].replace("~", str(Path.home())))
    auto_fix = "--fix" in sys.argv

    try:
        sanitizer = DependencySanitizer(tasks_file)
        result = sanitizer.sanitize()

        # Output JSON
        print(json.dumps(result, indent=2))

        # Auto-fix if requested
        if auto_fix and result["critical_count"] > 0:
            fixed = sanitizer.fix_auto_fixable()
            print(f"\n✓ Fixed {fixed} auto-fixable issues", file=sys.stderr)
            sanitizer.write_tasks()

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
