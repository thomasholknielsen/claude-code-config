---
description: "Branch management operations with safety checks and team workflows"
argument-hint: "[branch-name]"
category: "git"
tools: ["Bash", "Read", "Grep"]
complexity: "moderate"
allowed-tools: Bash, Read, Grep
---

# Command: Branch

## Purpose

Creates, manages, and switches git branches with intelligent naming and safety validation.

## Usage

```bash
/git:branch $ARGUMENTS
```

**Arguments**:

- `$1` (branch-name): Branch name (optional, auto-generated from changes if not provided)
- `$2` (--from): Base branch to create from (optional, defaults to current HEAD)
- `$3` (--switch): Switch to branch after creation (optional, default behavior)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "feature/user-authentication"` - Create and switch to feature branch
- `$ARGUMENTS = "hotfix/login-bug --from=main"` - Create hotfix from main branch
- `$ARGUMENTS = ""` - Auto-generate branch name from changes

## Process

1. Parse $ARGUMENTS for branch name and base branch
2. Validate working directory state and check for uncommitted changes
3. Generate intelligent branch name from git diff analysis if not provided
4. Create new feature branch from current HEAD
5. Switch to the new branch and confirm successful creation
6. Report branch creation status and next steps

## Agent Integration

- **Specialist Options**: implementation-strategy-specialist can be spawned for handling git operations and coordination

## Examples

```bash
# Create branch with auto-generated name
/git:branch

# Create branch with specific name
/git:branch $ARGUMENTS
# where $ARGUMENTS = "feature/user-authentication"

# Create hotfix branch
/git:branch $ARGUMENTS
# where $ARGUMENTS = "hotfix/login-bug"
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
