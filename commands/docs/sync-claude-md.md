---
description: "Automatically synchronizes CLAUDE.md with current agent and command structure"
category: "docs"
agent: "documenter"
tools: ["Write", "Read", "Bash"]
complexity: "simple"
---

# Command: Sync CLAUDE.md

## Purpose
Ensures CLAUDE.md stays current with the actual state of agents and commands by scanning the repository and updating statistics automatically.

## Usage
```
/docs:sync-claude-md
```

**Arguments**: None - automatically detects repository structure

## Process
1. Scan agents directory and categorize by orchestrators/workers
2. Scan commands directory and count by category
3. Parse agent metadata from YAML frontmatter
4. Update CLAUDE.md with current counts and descriptions
5. Preserve existing category descriptions and structure

## Agent Integration
- **Primary Agent**: documenter - Handles documentation updates and file management

## Examples
```bash
# Sync after adding new agent
/docs:sync-claude-md

# Sync after creating new commands
/docs:sync-claude-md

# Verify counts are accurate
/docs:sync-claude-md
```

## Output
- Updated CLAUDE.md with current statistics
- Console report of changes made
- Preserved existing structure and descriptions

## Integration Points
- **Follows**: Agent creation, command creation, repository changes
- **Followed by**: Git operations, documentation reviews
- **Related**: /git:commit (to include updated CLAUDE.md)

## Automation Features
- Cross-platform Python implementation
- Git hook integration available
- Automatic detection of relevant changes
- Fallback parsing when PyYAML unavailable

## Quality Standards
- Preserves existing CLAUDE.md structure
- Updates only statistical information
- Maintains category descriptions and explanations
- Handles parsing errors gracefully
- Provides clear feedback on changes made

## Hook Integration
Automatic synchronization available via git hooks:
- Pre-commit: Updates CLAUDE.md before committing changes to agents/commands
- Post-merge: Updates CLAUDE.md after pulling remote changes
- Manual trigger: Can be run independently anytime

This ensures CLAUDE.md always reflects the current repository state without manual intervention.