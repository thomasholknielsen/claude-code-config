---
description: "Push with safety checks, force-push protection, and team coordination"
argument-hint: "[remote] [branch]"
allowed-tools: Bash
---

# Command: Push

## Purpose

Safely pushes commits to remote repository with tracking setup and team coordination checks.

## Usage

```bash
/git:push $ARGUMENTS
```

**Arguments**:

- `$1` (remote): Remote repository name (optional, defaults to origin)
- `$2` (branch): Branch name to push (optional, defaults to current branch)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "origin feature/auth"` - Push feature branch to origin
- `$ARGUMENTS = "upstream main"` - Push main branch to upstream
- `$ARGUMENTS = ""` - Push current branch to origin (default)

## Process

1. Parse $ARGUMENTS for remote and branch parameters
2. Validate local branch state and commit history
3. Check remote repository status and conflicts
4. Set up branch tracking if this is the first push
5. Push commits with appropriate flags and safety checks
6. Confirm successful push and provide remote branch information

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned for handling git operations and coordination

## Examples

```bash
# Push current branch to origin with tracking
/git:push

# Push specific branch to origin
/git:push $ARGUMENTS
# where $ARGUMENTS = "origin feature/new-feature"

# Push to different remote
/git:push $ARGUMENTS
# where $ARGUMENTS = "upstream main"
```

## Output

- Push status and number of commits pushed
- Remote branch URL and tracking information
- Confirmation of successful remote update
- Next steps guidance (PR creation, collaboration)

## Integration Points

- **Follows**: /git:commit, local development completion
- **Followed by**: /git:pr, team collaboration
- **Related**: /git:branch, /workflows:run-git-branch-commit-and-pr

## Quality Standards

- Validates local commits are ready for sharing
- Sets up proper branch tracking for future pulls
- Checks for conflicts with remote before pushing
- Provides clear feedback on push status and next actions
- Never force-pushes without explicit user confirmation
- Ensures remote branch references are correctly established
