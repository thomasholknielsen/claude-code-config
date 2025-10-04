---
description: "Controlled merge operations with conflict resolution and safety checks"
argument-hint: "[arguments]"
category: "git"
tools: ["Bash"]
complexity: "moderate"
allowed-tools: Bash
---

# Command: Merge

## Purpose

Executes git operations for merge functionality.

## Usage

```bash
/git:merge $ARGUMENTS
```

**Arguments**:

- `$1` (branch): Branch to merge (optional, defaults to current branch)
- `$2` (--strategy): Merge strategy (merge, squash, rebase) (optional)
- `$3` (--no-ff): Force merge commit even for fast-forward (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "feature/auth"` - Merge feature branch
- `$ARGUMENTS = "develop --strategy=squash"` - Squash merge develop branch
- `$ARGUMENTS = "hotfix/bug --no-ff"` - Force merge commit for hotfix

## Process

1. Parse $ARGUMENTS for merge branch and strategy
2. Analyze the current state and merge requirements
3. Execute the git merge operation with conflict resolution
4. Validate results and provide feedback
5. Update relevant documentation or state

## Agent Integration

- **Specialist Options**: implementation-strategy-specialist can be spawned for handling git operations and coordination

## Examples

```bash
