#!/usr/bin/env python3
"""
Task Schema Manager
Handles parsing, extracting, and populating task.md sections
Supports 7-section progressive structure with full agent integration
"""

from datetime import datetime
import json
from pathlib import Path
import re
import sys
from typing import Dict, List, Optional


def extract_task_section(tasks_file: Path, task_id: str) -> Optional[str]:
    """
    Extract full task section from tasks.md
    Returns text from ## [TASK-XXX] to next --- separator

    Args:
        tasks_file: Path to .agent/tasks.md
        task_id: Task ID (e.g., "TASK-001")

    Returns:
        Full task section text, or None if not found
    """
    if not tasks_file.exists():
        return None

    content = tasks_file.read_text()

    # Pattern: ## [TASK-XXX] ... to next ---
    pattern = rf"^##\s+\[{re.escape(task_id)}\]\s+.+?(?=^---\s*$)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    return match.group(0) if match else None


def parse_task_metadata(task_section: str) -> Dict[str, str]:
    """
    Parse metadata from task section header

    Args:
        task_section: Full task section text

    Returns:
        Dict with keys: task_id, title, status, priority, category, origin, created, completed
    """
    lines = task_section.split("\n")
    metadata = {}

    # Extract header: ## [TASK-XXX] title
    header_match = re.match(r"^##\s+\[TASK-(\d{3})\]\s+(.+)$", lines[0])
    if header_match:
        metadata["task_id"] = f"TASK-{header_match.group(1)}"
        metadata["title"] = header_match.group(2)

    # Extract metadata fields
    for line in lines[1:]:
        if line.startswith("**Status**"):
            metadata["status"] = line.split(":", 1)[1].strip()
        elif line.startswith("**Priority**"):
            metadata["priority"] = line.split(":", 1)[1].strip()
        elif line.startswith("**Category**"):
            metadata["category"] = line.split(":", 1)[1].strip()
        elif line.startswith("**Origin**"):
            metadata["origin"] = line.split(":", 1)[1].strip()
        elif line.startswith("**Created**"):
            metadata["created"] = line.split(":", 1)[1].strip()
        elif line.startswith("**Completed**"):
            metadata["completed"] = line.split(":", 1)[1].strip()
        elif line.startswith("**Task Details Directory**"):
            metadata["task_dir"] = line.split(":", 1)[1].strip()

    return metadata


def extract_description(task_section: str) -> Optional[str]:
    """
    Extract description from task section
    Tries two patterns:
    1. ### Description section (modern format)
    2. **Description**: inline format (legacy)

    Args:
        task_section: Full task section text

    Returns:
        Description text, or None if not found
    """
    # Try pattern 1: ### Description section
    pattern1 = r"^###\s+Description\s*\n(.*?)(?=^###|\Z)"
    match = re.search(pattern1, task_section, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()

    # Try pattern 2: **Description**: inline format
    pattern2 = r"^\*\*Description\*\*:\s*(.+?)$"
    match = re.search(pattern2, task_section, re.MULTILINE)
    if match:
        return match.group(1).strip()

    return None


def create_7section_template(
    task_id: str,
    title: str,
    description: str,
    task_details_dir: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> str:
    """
    Create 7-section task.md structure template

    Sections:
    1. Header + Metadata
    2. Description
    3. Status Summary
    4. Key Findings
    5. Synthesis & Conclusions
    6. Next Steps
    7. Analysis Details
    8. Main Thread Log

    Args:
        task_id: Task ID (e.g., "TASK-001")
        title: Task title
        description: Task description
        task_details_dir: Optional path to task details directory
        metadata: Optional dict with priority, category, origin, created, completed fields

    Returns:
        Template string with all 7 sections
    """
    # Use provided metadata or defaults
    metadata = metadata or {}
    status = metadata.get("status", "in-progress")
    priority = metadata.get("priority", "[priority]")
    category = metadata.get("category", "[category]")
    origin = metadata.get("origin", "[origin]")
    created = metadata.get("created", datetime.now().isoformat() + "Z")
    completed = metadata.get("completed", "")

    # Build header
    header = f"## [{task_id}] {title}\n\n"
    header += f"**Status**: {status}\n"
    header += f"**Priority**: {priority}\n"
    header += f"**Category**: {category}\n"
    header += f"**Origin**: {origin}\n"
    header += f"**Created**: {created}\n"
    if completed:
        header += f"**Completed**: {completed}\n"
    if task_details_dir:
        header += f"**Task Details Directory**: {task_details_dir}\n"

    template = f"""{header}
---

### Description

{description}

---

### Status Summary

*Populate during execution: Quick status assessment with visual markers*

- [ ] Task setup complete
- [ ] Analysis in progress
- [ ] Findings synthesized
- [ ] Next steps identified

---

### Key Findings

*Populate from agent analysis: 3-5 one-liner findings*

1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

---

### Synthesis & Conclusions

*Populate from agent analysis: Cross-agent insights and resolutions*

**Cross-Agent Consensus**: [What all agents agreed on]

**Critical Issues**: [Most important items from findings]

**Recommendations**: [Actionable next steps]

---

### Next Steps

*Populate from task requirements: Checkboxed action items*

- [ ] Action 1
- [ ] Action 2
- [ ] Action 3

**Blockers**: [Any dependencies or blockers]

---

### Analysis Details

Full analysis saved to:
`{task_details_dir or "[task-directory]"}`

Agent findings:
- `[agent-name].md` - [Agent responsibility]
- `[agent-name].md` - [Agent responsibility]

---

### Main Thread Log

**Session Created**: {datetime.now().isoformat()}Z
**Task Loaded**: [timestamp]
**Task Setup Complete**: [timestamp]
**Agents Invoked**: [agent-names and timestamps]
**Analysis Complete**: [timestamp]
**Sections Populated**: [timestamp]
**Task Status**: in-progress
"""

    return template


def populate_key_findings(findings_text: str) -> str:
    """
    Parse agent findings and create Key Findings section

    Args:
        findings_text: Raw findings from agents

    Returns:
        Formatted Key Findings section
    """
    lines = findings_text.split("\n")
    findings = []

    for line in lines:
        line = line.strip()
        if line and not line.startswith("#") and len(line) > 10:
            # Take first 100 chars of each finding
            finding = line[:100]
            if not finding.endswith("."):
                finding += "."
            findings.append(finding)

    # Limit to top 5
    findings = findings[:5]

    result = "### Key Findings\n\n"
    for i, finding in enumerate(findings, 1):
        result += f"{i}. {finding}\n"

    return result


def update_task_in_file(tasks_file: Path, task_id: str, new_section: str) -> bool:
    """
    Replace task section in tasks.md with updated version

    Args:
        tasks_file: Path to .agent/tasks.md
        task_id: Task ID to update
        new_section: New task section content

    Returns:
        True if update successful, False otherwise
    """
    if not tasks_file.exists():
        return False

    content = tasks_file.read_text()

    # Pattern: ## [TASK-XXX] ... to next ---
    pattern = rf"^##\s+\[{re.escape(task_id)}\]\s+.+?(?=^---\s*$)"

    if re.search(pattern, content, re.MULTILINE | re.DOTALL):
        # Replace task section
        updated = re.sub(pattern, new_section, content, count=1, flags=re.MULTILINE | re.DOTALL)

        tasks_file.write_text(updated)
        return True

    return False


def generate_main_thread_log(
    _task_id: str, agents_invoked: List[str], task_setup_time: str, analysis_complete_time: str
) -> str:
    """
    Generate Main Thread Log section

    Args:
        task_id: Task ID
        agents_invoked: List of agent names
        task_setup_time: ISO timestamp of task setup
        analysis_complete_time: ISO timestamp of analysis completion

    Returns:
        Formatted Main Thread Log section
    """
    now = datetime.now().isoformat()

    agents_str = ", ".join(agents_invoked) if agents_invoked else "none"

    log = f"""### Main Thread Log

**Execution Timeline**:
- Task Created: {datetime.now().isoformat()}Z
- Task Setup: {task_setup_time}
- Agents Invoked: {agents_str}
- Analysis Completed: {analysis_complete_time}
- Last Updated: {now}Z

**Status**: in-progress
**Agents Completed**: {len(agents_invoked)}
"""

    return log


def extract_findings_from_agents(context_dir: str, agent_list: Optional[List[str]] = None) -> str:
    """
    Extract findings from all agent context files in a directory

    Args:
        context_dir: Path to task context directory containing agent .md files
        agent_list: Optional list of specific agents to extract from (all if not provided)

    Returns:
        Concatenated findings from all agent files
    """
    context_path = Path(context_dir)

    if not context_path.exists():
        return ""

    all_findings = []

    # Find all .md files in context directory
    for agent_file in context_path.glob("*.md"):
        # Skip if specific agent list provided and this agent not in it
        if agent_list and agent_file.stem not in agent_list:
            continue

        try:
            content = agent_file.read_text()
            # Extract first 500 chars of findings
            # Look for common sections in agent output
            lines = content.split("\n")

            # Find meaningful content (skip headers, take first substantial section)
            findings = []
            for line in lines:
                if line.strip() and len(line) > 20:
                    findings.append(line.strip())
                    if len(findings) >= 10:  # Limit to first 10 substantial lines
                        break

            if findings:
                agent_name = agent_file.stem
                all_findings.append(f"\n--- {agent_name} ---\n")
                all_findings.extend(findings)

        except Exception:
            # Skip files that can't be read
            continue

    return "\n".join(all_findings)


def write_task_md(file_path: str, content: str) -> bool:
    """
    Write content to task.md file, creating parent directories if needed

    Args:
        file_path: Path where task.md should be written
        content: Complete task.md content

    Returns:
        True if write successful, False otherwise
    """
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: task_schema_manager.py <command> <args>"}))
        sys.exit(1)

    command = sys.argv[1]

    if command == "extract":
        # Extract task section from tasks.md
        # Usage: task_schema_manager.py extract <tasks_file_path> <task_id>
        if len(sys.argv) < 4:
            print(json.dumps({"error": "extract requires <tasks_file_path> and <task_id>"}))
            sys.exit(1)

        tasks_file_path = sys.argv[2].replace("~", str(Path.home()))
        tasks_file = Path(tasks_file_path)
        task_id = sys.argv[3]

        section = extract_task_section(tasks_file, task_id)
        if section:
            print(section)
            sys.exit(0)
        else:
            print(json.dumps({"error": f"Task {task_id} not found"}), file=sys.stderr)
            sys.exit(1)

    elif command == "extract_description":
        # Extract description from task section
        # Usage: task_schema_manager.py extract_description <task_section_text>
        task_section = sys.stdin.read() if len(sys.argv) < 3 else "\n".join(sys.argv[2:])

        description = extract_description(task_section)
        print(description if description else "")
        sys.exit(0)

    elif command == "parse_metadata":
        # Parse metadata from task section
        # Usage: task_schema_manager.py parse_metadata <task_section_text>
        task_section = sys.stdin.read() if len(sys.argv) < 3 else "\n".join(sys.argv[2:])

        metadata = parse_task_metadata(task_section)
        print(json.dumps(metadata))
        sys.exit(0)

    elif command == "populate_key_findings":
        # Populate Key Findings section from agent findings
        # Usage: task_schema_manager.py populate_key_findings <findings_text>
        findings_text = sys.stdin.read() if len(sys.argv) < 3 else "\n".join(sys.argv[2:])

        result = populate_key_findings(findings_text)
        print(result)
        sys.exit(0)

    elif command == "generate_main_thread_log":
        # Generate Main Thread Log section
        # Usage: task_schema_manager.py generate_main_thread_log <task_id> <agents_list> <setup_time> <complete_time>
        if len(sys.argv) < 6:
            print(
                json.dumps(
                    {"error": "generate_main_thread_log requires <task_id> <agents> <setup_time> <complete_time>"}
                )
            )
            sys.exit(1)

        task_id = sys.argv[2]
        agents_str = sys.argv[3]
        agents_list = [a.strip() for a in agents_str.split(",") if a.strip()]
        setup_time = sys.argv[4]
        complete_time = sys.argv[5]

        log = generate_main_thread_log(task_id, agents_list, setup_time, complete_time)
        print(log)
        sys.exit(0)

    elif command == "create_template":
        # Create 7-section template
        # Usage: task_schema_manager.py create_template <task_id> <title> <description> [task_details_dir] [metadata_json]
        if len(sys.argv) < 4:
            print(
                json.dumps(
                    {
                        "error": "create_template requires <task_id> <title> <description> [task_details_dir] [metadata_json]"
                    }
                )
            )
            sys.exit(1)

        task_id = sys.argv[2]
        title = sys.argv[3]
        description = sys.argv[4] if len(sys.argv) > 4 else ""
        task_details_dir = sys.argv[5] if len(sys.argv) > 5 else None

        # Parse metadata JSON if provided
        metadata = None
        if len(sys.argv) > 6:
            try:
                metadata = json.loads(sys.argv[6])
            except json.JSONDecodeError:
                print(json.dumps({"error": f"Invalid JSON in metadata: {sys.argv[6]}"}), file=sys.stderr)
                sys.exit(1)

        template = create_7section_template(task_id, title, description, task_details_dir, metadata)
        print(template)
        sys.exit(0)

    elif command == "update_task_in_file":
        # Update task section in tasks.md file
        # Usage: task_schema_manager.py update_task_in_file <tasks_file_path> <task_id> <new_section>
        if len(sys.argv) < 5:
            print(json.dumps({"error": "update_task_in_file requires <tasks_file_path> <task_id> <new_section>"}))
            sys.exit(1)

        tasks_file_path = sys.argv[2].replace("~", str(Path.home()))
        tasks_file = Path(tasks_file_path)
        task_id = sys.argv[3]
        new_section = "\n".join(sys.argv[4:])

        success = update_task_in_file(tasks_file, task_id, new_section)
        print(json.dumps({"success": success}))
        sys.exit(0 if success else 1)

    elif command == "extract_findings_from_agents":
        # Extract findings from all agent context files
        # Usage: task_schema_manager.py extract_findings_from_agents <context_dir> [agent1,agent2,...]
        if len(sys.argv) < 3:
            print(json.dumps({"error": "extract_findings_from_agents requires <context_dir> [agent_list]"}))
            sys.exit(1)

        context_dir = sys.argv[2].replace("~", str(Path.home()))
        agent_list = None
        if len(sys.argv) > 3:
            agent_list = [a.strip() for a in sys.argv[3].split(",") if a.strip()]

        findings = extract_findings_from_agents(context_dir, agent_list)
        print(findings)
        sys.exit(0)

    elif command == "write_task_md":
        # Write content to task.md file
        # Usage: task_schema_manager.py write_task_md <file_path> <content>
        if len(sys.argv) < 4:
            print(json.dumps({"error": "write_task_md requires <file_path> <content>"}))
            sys.exit(1)

        file_path = sys.argv[2].replace("~", str(Path.home()))
        content = "\n".join(sys.argv[3:])

        success = write_task_md(file_path, content)
        print(json.dumps({"success": success, "file": file_path}))
        sys.exit(0 if success else 1)

    else:
        print(json.dumps({"error": f"Unknown command: {command}"}), file=sys.stderr)
        sys.exit(1)
