---
description: "Merge changes from multiple worktrees into a single feature branch with intelligent conflict resolution"
allowed-tools: Bash, Read, Grep, TodoWrite, mcp__sequential-thinking__sequentialthinking
---

# Command: Worktree Consolidate

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Merge multiple worktree branches into single feature branch with modes (interactive selection, batch branches, staging mode), create safety checkpoints (backup/ branches), detect conflicts, provide guided resolution (manual/ours/theirs/skip/abort), validate merged state

**P**urpose: Consolidate parallel development work into unified branch for single PR, support parallel mode (multiple PRs → one PR) and staging mode (staging parent + children → consolidated), maintain safe rollback capability

**E**xpectation: All selected worktree branches merged into target branch, automatic backup created (backup/consolidate-{timestamp}), conflicts detected with resolution guidance, consolidation summary with total commits/files, next steps for commit/push/PR

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% merge operations, Accuracy >90% conflict detection, Relevance >85% resolution guidance, Efficiency <30s for typical consolidation)

## Purpose

Merges changes from multiple worktrees into a single feature branch with intelligent conflict detection and guided resolution.

## Usage

```bash
/git:worktree-consolidate [arguments...]
```

**Arguments**:

- No arguments: Interactive mode - list available worktrees and select which to consolidate
- `[branch1] [branch2] [branch3...]`: Merge specific branches from worktrees
- `--staging [staging-branch]`: Consolidate all child worktrees of a staging branch
- `--into [target-branch]`: Specify target branch (default: current branch)

## Process

### Interactive Mode

1. Validate current branch is clean (no uncommitted changes)
2. List all available worktrees with change summaries
3. Prompt user to select worktrees for consolidation
4. Create safety checkpoint (backup branch)
5. Merge each selected worktree branch sequentially
6. Detect conflicts and provide resolution guidance
7. Validate merged state after each merge
8. Report consolidation summary and next steps

### Batch Mode (Specified Branches)

1. Validate current branch state and check for uncommitted changes
2. Verify all specified branches exist in worktrees
3. Create safety checkpoint with timestamp
4. For each branch sequentially:
   - Show diff summary of incoming changes
   - Attempt merge with conflict detection
   - If conflicts: pause and provide resolution workflow
   - If clean: validate and continue to next branch
5. Report final consolidation status

### Staging Mode Consolidation

1. Validate staging branch exists and is parent of child worktrees
2. Identify all child worktrees associated with staging branch
3. Create consolidated feature branch from staging branch
4. Merge all child branches into consolidated branch
5. Provide conflict resolution for each child branch
6. Report staging consolidation results

## Agent Integration

- **Primary Agent**: implementation-orchestrator - Handles sequential merge coordination and conflict resolution

## Examples

### Interactive Consolidation

```bash
# Interactive mode: select worktrees to merge
/git:worktree-consolidate

# Output shows:
# Available worktrees:
# [1] .trees/auth (feature/auth) - 5 commits, 12 files changed
# [2] .trees/payments (feature/payments) - 3 commits, 8 files changed
# [3] .trees/header (bugfix/header) - 1 commit, 2 files changed
#
# Select worktrees to consolidate (comma-separated): 1,2
```

### Batch Consolidation

```bash
# Merge specific branches into current branch
/git:worktree-consolidate feature/auth feature/payments

# Merge into specific target branch
/git:worktree-consolidate feature/auth feature/payments --into feature/combined
```

### Staging Mode Consolidation

```bash
# Consolidate all child worktrees from staging branch
/git:worktree-consolidate --staging integration-q4

# This merges:
# - integration-q4-auth
# - integration-q4-payments
# - integration-q4-header
# Into: integration-q4 (or new consolidated branch)
```

## Output

### Pre-Merge Information

- List of worktrees to be consolidated
- Change summaries for each branch (commits, files, impact)
- Safety checkpoint branch name
- Estimated merge complexity

### During Merge

- Progress indicator for each branch being merged
- Conflict detection notifications
- Guided conflict resolution steps
- Validation results after each merge

### Post-Merge Summary

- List of successfully merged branches
- Conflict resolution summary
- Total commits consolidated
- Total files changed
- Next steps guidance (commit, push, PR)

## Conflict Resolution Workflow

When conflicts are detected:

1. **Pause Merge Process**: Stop before conflicting merge
2. **Conflict Analysis**: Show conflicting files and change types
3. **Resolution Options**:
   - **Manual**: Provide instructions to resolve conflicts manually
   - **Ours**: Accept current branch changes
   - **Theirs**: Accept incoming branch changes
   - **Skip**: Skip this branch and continue with others
   - **Abort**: Rollback to safety checkpoint
4. **Validation**: After resolution, validate merged state
5. **Continue**: Proceed to next branch in queue

### Example Conflict Resolution

```text
# Conflict detected during merge of feature/auth
⚠️  Merge conflict detected in 3 files:
  - src/auth/login.js (both modified)
  - src/auth/session.js (both modified)
  - config/auth.json (both modified)

Resolution options:
  [m] Manual resolution - Open files and resolve conflicts
  [o] Accept ours - Keep current branch changes
  [t] Accept theirs - Accept incoming branch changes
  [s] Skip - Skip this branch, continue with others
  [a] Abort - Rollback to checkpoint: backup/consolidate-2025-09-30-1430

Select option:
```

## Safety Features

### Automatic Checkpoints

- Creates backup branch before starting: `backup/consolidate-{timestamp}`
- Can rollback to checkpoint at any time
- Checkpoint preserved until user manually deletes

### Validation Checks

- **Pre-merge**: Clean working directory, valid branches
- **During merge**: File conflicts, semantic conflicts
- **Post-merge**: Build validation, test validation (if configured)

### Rollback Support

```bash
# If consolidation fails or user aborts
git reset --hard backup/consolidate-2025-09-30-1430
```

## Integration Points

- **Follows**: /git:worktree (add-multiple or add-staging)
- **Followed by**: /git:commit, /git:push, /git:pr
- **Related**: /git:merge, /git:branch, /workflows:git

## Quality Standards

- Validates all branches exist before starting consolidation
- Creates safety checkpoints for rollback capability
- Provides clear conflict detection and resolution guidance
- Validates merged state after each branch integration
- Supports both parallel and staging mode worktree patterns
- Preserves commit history and maintains clean merge structure
- Provides detailed consolidation summary with next steps
- Handles edge cases (empty branches, already merged, diverged histories)

## Best Practices

1. **Always Review Changes First**: Use `/git:worktree list` to understand what will be merged
2. **Clean State**: Ensure current branch has no uncommitted changes
3. **Test After Merge**: Run tests after consolidation before pushing
4. **Preserve Checkpoints**: Don't delete backup branches until PR is merged
5. **Incremental Consolidation**: Start with 2-3 worktrees, then add more as needed

## Common Scenarios

### Scenario 1: Parallel Feature Development → Single PR

```bash
# Created parallel worktrees
/git:worktree add-multiple feature/auth feature/payments feature/ui

# Work completed in all worktrees, now consolidate
git checkout -b feature/combined-release
/git:worktree-consolidate feature/auth feature/payments feature/ui

# Result: All changes in feature/combined-release, ready for single PR
```

### Scenario 2: Staging Branch Integration

```bash
# Created staging structure
/git:worktree add-staging integration-q4 auth payments ui

# All child worktrees complete, consolidate into staging
git checkout integration-q4
/git:worktree-consolidate --staging integration-q4

# Result: All child changes merged into integration-q4
```

### Scenario 3: Selective Consolidation with Conflicts

```bash
# Some worktrees ready, others still in progress
/git:worktree-consolidate feature/auth feature/payments

# Conflict in feature/payments
# Choose [s] to skip, consolidate feature/auth only
# Later, return and merge feature/payments when conflicts resolved
```
