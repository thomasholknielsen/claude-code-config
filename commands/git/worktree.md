---
description: "Manages git worktrees for parallel development with shared repository history"
category: "git"
agent: "implementation-orchestrator"
tools: ["Bash", "Read", "Grep"]
complexity: "moderate"
---

# Command: Worktree

## Purpose

Creates and manages git worktrees to enable parallel development of multiple branches in separate directories.

## Usage

```bash
/git:worktree [action] [branch-name] [path]
```

**Arguments**:

- `action`: add, remove, list, or prune (default: list)
- `branch-name`: Branch to checkout in new worktree (for add action)
- `path`: Directory path for new worktree (for add action)

## Process

1. Validate repository state and check for existing worktrees
2. Execute specified worktree operation with safety checks
3. Create or manage worktree directories and branch associations
4. Update worktree tracking and provide status confirmation
5. Report worktree state and provide next steps guidance

## Agent Integration

- **Primary Agent**: implementation-orchestrator - Handles git worktree operations and directory coordination

## Examples

```bash
# List all worktrees
/git:worktree

# Add new worktree with existing branch
/git:worktree add feature/api-improvements ../api-work

# Add new worktree with new branch
/git:worktree add -b feature/new-component ../component-work

# Remove worktree
/git:worktree remove ../api-work

# Prune stale worktree references
/git:worktree prune
```

## Output

- Current worktrees list with paths and associated branches
- Confirmation of worktree creation/removal operations
- Working directory status for each worktree
- Guidance on switching between worktrees and managing parallel work

## Integration Points

- **Follows**: Repository setup, feature planning
- **Followed by**: /git:commit, /git:push, parallel development workflows
- **Related**: /git:branch, /git:workflow, /workflows:run-git-branch-commit-and-pr

## Quality Standards

- Validates repository state before worktree operations
- Ensures proper directory structure and permissions
- Prevents conflicts between worktree branches
- Provides clear feedback on worktree status and location
- Handles cleanup of stale worktree references automatically
