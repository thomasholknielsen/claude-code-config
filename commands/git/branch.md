---
description: "Branch management operations with safety checks and team workflows"
category: "git"
agent: "implementation-orchestrator"
tools: ["Bash", "Read", "Grep"]
complexity: "moderate"
---

# Command: Branch

## Purpose

Creates, manages, and switches git branches with intelligent naming and safety validation.

## Usage

```bash
/git:branch [branch-name]
```

**Arguments**: Optional branch name (auto-generated from changes if not provided)

## Process

1. Validate working directory state and check for uncommitted changes
2. Generate intelligent branch name from git diff analysis if not provided
3. Create new feature branch from current HEAD
4. Switch to the new branch and confirm successful creation
5. Report branch creation status and next steps

## Agent Integration

- **Primary Agent**: implementation-orchestrator - Handles git operations and coordination

## Examples

```bash
# Create branch with auto-generated name
/git:branch

# Create branch with specific name
/git:branch "feature/user-authentication"

# Create hotfix branch
/git:branch "hotfix/login-bug"
```

## Output

- Created branch name and base commit
- Confirmation of successful branch switch
- Working directory status after branch creation
- Guidance on next steps (commit, push, etc.)

## Integration Points

- **Follows**: Code changes, feature development initiation
- **Followed by**: /git:commit, code modifications
- **Related**: /git:push, /git:pr, /workflows:run-git-branch-commit-and-pr

## Quality Standards

- Validates clean working state before branch creation
- Generates meaningful branch names from file analysis
- Follows repository naming conventions (feature/, hotfix/, etc.)
- Ensures branch creation doesn't conflict with existing branches
- Provides clear feedback on branch status and next actions
