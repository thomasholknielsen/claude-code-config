#!/usr/bin/env python3
"""
Context Helper for Claude Code
Utility functions for managing agent context files in session directories
"""

from datetime import datetime
from pathlib import Path
import re
import sys


def get_session_id():
    """Get current session ID"""
    session_file = Path.home() / ".claude" / ".current_session"
    if session_file.exists():
        return session_file.read_text().strip()
    return None


def get_context_dir():
    """Get context directory for current session"""
    session_id = get_session_id()
    if not session_id:
        raise RuntimeError("No active session found")

    context_dir = Path.home() / ".claude" / ".agent" / "context" / session_id
    context_dir.mkdir(parents=True, exist_ok=True)
    return context_dir


def get_context_file(agent_name):
    """Get path to context file for a specific agent

    Args:
        agent_name: Name of the agent (e.g., 'python-analyst')

    Returns:
        Path object for the agent's context file
    """
    context_dir = get_context_dir()
    return context_dir / f"{agent_name}.md"


def parse_context_sections(content):
    """Parse markdown content into sections

    Args:
        content: Markdown content string

    Returns:
        Dictionary mapping section names to content
    """
    sections = {}
    current_section = None
    current_content = []

    lines = content.split("\n")

    for line in lines:
        # Check for h1 header (# Header)
        if line.startswith("# ") and not line.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = line[2:].strip()
            current_content = [line]
        else:
            if current_section:
                current_content.append(line)

    # Add last section
    if current_section:
        sections[current_section] = "\n".join(current_content).strip()

    return sections


def read_context(agent_name):
    """Read existing context file and parse into sections

    Args:
        agent_name: Name of the agent

    Returns:
        Dictionary with parsed sections, or None if file doesn't exist
    """
    context_file = get_context_file(agent_name)

    if not context_file.exists():
        return None

    content = context_file.read_text()
    sections = parse_context_sections(content)

    return sections


def extract_metadata(sections):
    """Extract metadata from first section

    Args:
        sections: Dictionary of parsed sections

    Returns:
        Dictionary with metadata fields
    """
    if not sections:
        return {}

    first_section = list(sections.values())[0] if sections else ""
    metadata = {}

    # Extract metadata lines (bold key-value pairs)
    for line in first_section.split("\n"):
        match = re.match(r"\*\*([^*]+)\*\*:\s*(.+)", line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            metadata[key] = value

    return metadata


def update_metadata(sections, updates):
    """Update metadata in first section

    Args:
        sections: Dictionary of parsed sections
        updates: Dictionary of metadata updates

    Returns:
        Updated sections dictionary
    """
    if not sections:
        return sections

    first_section_name = list(sections.keys())[0]
    first_section_content = sections[first_section_name]

    lines = first_section_content.split("\n")
    updated_lines = []

    for line in lines:
        match = re.match(r"\*\*([^*]+)\*\*:\s*(.+)", line)
        if match:
            key = match.group(1).strip()
            if key in updates:
                updated_lines.append(f"**{key}**: {updates[key]}")
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)

    sections[first_section_name] = "\n".join(updated_lines)
    return sections


def write_context(agent_name, sections):
    """Write sections to context file

    Args:
        agent_name: Name of the agent
        sections: Dictionary mapping section names to content
    """
    context_file = get_context_file(agent_name)

    # Build content from sections
    content_parts = []
    for section_name, section_content in sections.items():
        if not section_content.startswith(f"# {section_name}"):
            content_parts.append(f"# {section_name}\n\n{section_content}")
        else:
            content_parts.append(section_content)

    content = "\n\n---\n\n".join(content_parts)
    context_file.write_text(content)


def add_tasks(agent_name, tasks, priority="Important"):
    """Add tasks to actionable tasks section

    Args:
        agent_name: Name of the agent
        tasks: List of task strings
        priority: Priority level (Critical, Important, or Enhancements)
    """
    sections = read_context(agent_name)
    if not sections:
        raise ValueError(f"No context file found for {agent_name}")

    # Find Actionable Tasks section
    if "Actionable Tasks" not in sections:
        sections["Actionable Tasks"] = "## Actionable Tasks\n"

    tasks_content = sections["Actionable Tasks"]

    # Find or create priority subsection
    priority_header = f"### {priority}"
    if priority_header not in tasks_content:
        tasks_content += f"\n{priority_header}\n"

    # Add tasks
    for task in tasks:
        if not task.startswith("- [ ]"):
            task = f"- [ ] {task}"
        tasks_content += f"{task}\n"

    sections["Actionable Tasks"] = tasks_content
    write_context(agent_name, sections)


def mark_task_obsolete(agent_name, task_pattern):
    """Mark tasks matching pattern as obsolete with strikethrough

    Args:
        agent_name: Name of the agent
        task_pattern: Regex pattern or string to match tasks
    """
    sections = read_context(agent_name)
    if not sections or "Actionable Tasks" not in sections:
        return

    tasks_content = sections["Actionable Tasks"]
    lines = tasks_content.split("\n")
    updated_lines = []

    for line in lines:
        if re.search(task_pattern, line) and line.strip().startswith("- [ ]"):
            # Add strikethrough
            task_text = line.strip()[5:].strip()  # Remove "- [ ] "
            updated_lines.append(f"- [x] ~~{task_text}~~")
        else:
            updated_lines.append(line)

    sections["Actionable Tasks"] = "\n".join(updated_lines)
    write_context(agent_name, sections)


def create_initial_context(agent_name, objective, iteration=1):
    """Create initial context file structure

    Args:
        agent_name: Name of the agent
        objective: One-sentence objective
        iteration: Iteration number (default 1)

    Returns:
        Dictionary of initial sections
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sections = {
        f"{agent_name.replace('-', ' ').title()} Analysis": f"""# {agent_name.replace("-", " ").title()} Analysis

**Objective**: {objective}
**Last Updated**: {timestamp}
**Iteration**: {iteration}""",
        "Analysis": """# Analysis

### Findings Category 1
{findings}""",
        "Actionable Tasks": """# Actionable Tasks

### Critical (Do First)

### Important (Do Next)

### Enhancements (Nice to Have)""",
        "Main Thread Log": """# Main Thread Log

""",
    }

    return sections


def add_main_thread_log(agent_name, completed, deferred=None):
    """Add main thread log entry

    Args:
        agent_name: Name of the agent
        completed: List of completed task descriptions
        deferred: Optional list of deferred task descriptions with reasons
    """
    sections = read_context(agent_name)
    if not sections:
        return

    if "Main Thread Log" not in sections:
        sections["Main Thread Log"] = "# Main Thread Log\n"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"\n### {timestamp}\n"

    if completed:
        log_entry += f"**Completed**: {', '.join(completed)}\n"

    if deferred:
        log_entry += f"**Deferred**: {', '.join(deferred)}\n"

    sections["Main Thread Log"] += log_entry
    write_context(agent_name, sections)


def increment_iteration(agent_name):
    """Increment iteration number in context file

    Args:
        agent_name: Name of the agent
    """
    sections = read_context(agent_name)
    if not sections:
        return

    metadata = extract_metadata(sections)
    current_iteration = int(metadata.get("Iteration", "1"))

    updates = {"Iteration": str(current_iteration + 1), "Last Updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    sections = update_metadata(sections, updates)
    write_context(agent_name, sections)


def main():
    """Main entry point for CLI usage"""
    if len(sys.argv) < 2:
        print("Usage: context_helper.py [get_file|read|init] agent_name [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "get_file":
        if len(sys.argv) < 3:
            print("Usage: context_helper.py get_file agent_name")
            sys.exit(1)
        agent_name = sys.argv[2]
        print(get_context_file(agent_name))

    elif command == "read":
        if len(sys.argv) < 3:
            print("Usage: context_helper.py read agent_name")
            sys.exit(1)
        agent_name = sys.argv[2]
        sections = read_context(agent_name)
        if sections:
            for name, content in sections.items():
                print(f"\n{'=' * 60}")
                print(f"SECTION: {name}")
                print(f"{'=' * 60}")
                print(content)
        else:
            print(f"No context file found for {agent_name}")

    elif command == "init":
        if len(sys.argv) < 4:
            print("Usage: context_helper.py init agent_name 'objective'")
            sys.exit(1)
        agent_name = sys.argv[2]
        objective = sys.argv[3]
        sections = create_initial_context(agent_name, objective)
        write_context(agent_name, sections)
        print(f"Initialized context for {agent_name}")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
