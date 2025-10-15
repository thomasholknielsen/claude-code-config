---
description: "Push with safety checks, force-push protection, and team coordination"
argument-hint: "[remote] [branch]"
allowed-tools: Bash, mcp__sequential-thinking__sequentialthinking
---

# Command: Push

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Push commits to remote with validation (local branch state, commit history, remote conflicts), set up branch tracking with -u flag (first push), execute git push with safety checks, provide remote branch information

**P**urpose: Safely share local commits with team, establish remote tracking for collaboration, prevent force-push accidents (requires explicit confirmation), coordinate with remote repository state

**E**xpectation: Commits pushed to origin/remote, branch tracking established, clear push status with commit counts, remote branch URL provided, next steps guidance (PR creation if needed)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% push requirements, Accuracy >90% remote sync, Relevance >85% safety checks, Efficiency <10s typical push)

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
- **Related**: /git-flow:feature, /workflows:git

## Quality Standards

- Validates local commits are ready for sharing
- Sets up proper branch tracking for future pulls
- Checks for conflicts with remote before pushing
- Provides clear feedback on push status and next actions
- Never force-pushes without explicit user confirmation
- Ensures remote branch references are correctly established
