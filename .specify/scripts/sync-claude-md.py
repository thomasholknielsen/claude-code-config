#!/usr/bin/env python3
"""
Repository-specific script to synchronize CLAUDE.md with current agent and command structure.

This script is specific to the Claude Code Command System repository and should NOT be
used as a global slash command. It scans the repository structure and updates CLAUDE.md
with current counts and metadata.

Usage:
    python .specify/scripts/sync-claude-md.py

    Or from git hooks:
    python .specify/scripts/sync-claude-md.py --quiet
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple

def parse_yaml_frontmatter(content: str) -> Dict[str, str]:
    """Parse YAML frontmatter from markdown files."""
    try:
        import yaml
        if content.startswith('---\n'):
            end = content.find('\n---\n', 4)
            if end != -1:
                frontmatter = content[4:end]
                return yaml.safe_load(frontmatter) or {}
    except ImportError:
        # Fallback parsing without PyYAML
        pass

    # Simple regex-based parsing as fallback
    frontmatter = {}
    if content.startswith('---\n'):
        end = content.find('\n---\n', 4)
        if end != -1:
            fm_content = content[4:end]
            for line in fm_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip().strip('"\'')

    return frontmatter

def scan_agents() -> Tuple[Dict[str, List[str]], int]:
    """Scan agents directory and categorize."""
    agents_dir = Path('agents')
    if not agents_dir.exists():
        return {'orchestrators': [], 'workers': []}, 0

    agents = {'orchestrators': [], 'workers': []}
    total_count = 0

    # Scan orchestrators
    orchestrators_dir = agents_dir / 'orchestrators'
    if orchestrators_dir.exists():
        for file in orchestrators_dir.glob('*.md'):
            if file.name != 'README.md':
                agents['orchestrators'].append(file.stem)
                total_count += 1

    # Scan workers
    workers_dir = agents_dir / 'workers'
    if workers_dir.exists():
        for file in workers_dir.glob('*.md'):
            if file.name != 'README.md':
                agents['workers'].append(file.stem)
                total_count += 1

    return agents, total_count

def scan_commands() -> Tuple[Dict[str, int], int]:
    """Scan commands directory and count by category."""
    commands_dir = Path('commands')
    if not commands_dir.exists():
        return {}, 0

    categories = {}
    total_count = 0

    for category_dir in commands_dir.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('.'):
            count = len([f for f in category_dir.glob('*.md') if f.name != 'README.md'])
            if count > 0:
                categories[category_dir.name] = count
                total_count += count

    return categories, total_count

def update_claude_md(agents: Dict[str, List[str]], agent_count: int,
                    commands: Dict[str, int], command_count: int) -> bool:
    """Update CLAUDE.md with current statistics."""
    claude_md = Path('CLAUDE.md')
    if not claude_md.exists():
        print(f"Error: {claude_md} not found")
        return False

    content = claude_md.read_text()
    original_content = content

    # Update agent counts
    # Pattern: **8 Agents**: 3 orchestrators + 5 workers
    agent_pattern = r'\*\*\d+ Agents\*\*: \d+ orchestrators \+ \d+ workers'
    orchestrator_count = len(agents['orchestrators'])
    worker_count = len(agents['workers'])
    new_agent_text = f"**{agent_count} Agents**: {orchestrator_count} orchestrators + {worker_count} workers"
    content = re.sub(agent_pattern, new_agent_text, content)

    # Update command counts
    # Pattern: **48 Commands**: Atomic operations organized across 12 categories
    command_pattern = r'\*\*\d+ Commands\*\*: Atomic operations organized across \d+ categories'
    category_count = len(commands)
    new_command_text = f"**{command_count} Commands**: Atomic operations organized across {category_count} categories"
    content = re.sub(command_pattern, new_command_text, content)

    # Update command structure section if it exists
    # Look for the command categories structure
    categories_pattern = r'```\ncommands/\n(.*?)\n```'
    if re.search(categories_pattern, content, re.DOTALL):
        # Build new categories structure
        categories_lines = []
        for category, count in sorted(commands.items()):
            spacing = ' ' * (12 - len(category))  # Align to 12 characters
            categories_lines.append(f"├── {category}/{spacing} # {count} commands")

        categories_text = "commands/\n" + "\n".join(categories_lines)
        new_categories = f"```\n{categories_text}\n```"
        content = re.sub(categories_pattern, new_categories, content, flags=re.DOTALL)

    # Update actual command categories if the section exists
    # Pattern: ### Actual Command Categories (48 total)
    if "### Actual Command Categories" in content:
        actual_pattern = r'### Actual Command Categories \(\d+ total\)'
        new_actual_text = f"### Actual Command Categories ({command_count} total)"
        content = re.sub(actual_pattern, new_actual_text, content)

    # Write back if changed
    if content != original_content:
        claude_md.write_text(content)
        return True

    return False

def main():
    """Main synchronization function."""
    quiet = '--quiet' in sys.argv

    if not quiet:
        print("Synchronizing CLAUDE.md with repository structure...")

    # Scan repository
    agents, agent_count = scan_agents()
    commands, command_count = scan_commands()

    if not quiet:
        print(f"Found {agent_count} agents:")
        print(f"  - {len(agents['orchestrators'])} orchestrators: {', '.join(agents['orchestrators'])}")
        print(f"  - {len(agents['workers'])} workers: {', '.join(agents['workers'])}")
        print(f"Found {command_count} commands across {len(commands)} categories:")
        for category, count in sorted(commands.items()):
            print(f"  - {category}: {count} commands")

    # Update CLAUDE.md
    updated = update_claude_md(agents, agent_count, commands, command_count)

    if updated:
        if not quiet:
            print("✓ CLAUDE.md updated successfully")
    else:
        if not quiet:
            print("✓ CLAUDE.md already up to date")

    return 0 if updated else 1

if __name__ == '__main__':
    # Ensure we're in the repository root
    if not Path('.git').exists():
        print("Error: Must be run from repository root")
        sys.exit(1)

    sys.exit(main())