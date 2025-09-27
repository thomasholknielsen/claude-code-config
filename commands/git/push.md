---
description: "Push with safety checks, force-push protection, and team coordination"
category: "git"
agent: "implementation-orchestrator"
tools: ["Bash"]
complexity: "moderate"
---

# Command: Push

## Purpose

Safely pushes commits to remote repository with tracking setup and team coordination checks.

## Usage

```bash
/git:push [remote] [branch]
```

**Arguments**: Optional remote and branch names (defaults to origin and current branch)

## Process

1. Validate local branch state and commit history
2. Check remote repository status and conflicts
3. Set up branch tracking if this is the first push
4. Push commits with appropriate flags and safety checks
5. Confirm successful push and provide remote branch information

## Agent Integration

- **Primary Agent**: implementation-orchestrator - Handles git operations and coordination

## Examples

```bash
# Push current branch to origin with tracking
/git:push

# Push specific branch to origin
/git:push origin feature/new-feature

# Push to different remote
/git:push upstream main
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