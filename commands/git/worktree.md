---
description: "Manages git worktrees for parallel development with shared repository history"
argument-hint: "[action] [arguments...]"
allowed-tools: Bash, Read, Grep
---

# Command: Worktree

## Purpose

Creates and manages git worktrees to enable parallel development of multiple branches in separate directories.

## Usage

```bash
/git:worktree $ARGUMENTS
```

**Arguments**:

- `$1` (action): add, add-multiple, add-staging, remove, list, or prune (default: list)
- For `add`: `$2` (branch-name), `$3` (path) - Single worktree creation
- For `add-multiple`: `$2..$N` (branch names) - Batch parallel worktrees
- For `add-staging`: `$2` (staging-branch), `$3..$N` (feature names) - Staging branch + children
- For `remove`: `$2` (path) - Remove specific worktree
- For `list`: No additional arguments - Show all worktrees with mode indicators
- For `prune`: No additional arguments - Clean stale references

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "add feature/auth ../wt-auth"` - Single worktree
- `$ARGUMENTS = "add-multiple feature/auth feature/payments"` - Multiple parallel worktrees
- `$ARGUMENTS = "add-staging integration feature/auth feature/payments"` - Staging workflow
- `$ARGUMENTS = "remove ../wt-auth"` - Remove worktree
- `$ARGUMENTS = "list"` - Show all worktrees

## Process

### Single Worktree (add)

1. Validate repository state and check for existing worktrees
2. Parse $ARGUMENTS to determine action and parameters
3. Execute specified worktree operation with safety checks
4. Create worktree directory and branch association
5. Update worktree tracking and provide status confirmation
6. Report worktree state and provide next steps guidance

### Parallel Mode (add-multiple)

1. Validate repository state for batch operations
2. Loop through each branch name with validation
3. Auto-generate directory paths (.trees/{branch-suffix}/)
4. Create independent worktrees for parallel development
5. Report all created worktrees with individual PR guidance

### Staging Mode (add-staging)

1. Create integration branch from current HEAD
2. Create base worktree for staging branch
3. Loop through feature names creating child worktrees
4. Each child branches from the staging branch
5. Report staging structure with consolidation workflow guidance

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned for handling git worktree operations and directory coordination

## Examples

### Basic Operations

```bash
# List all worktrees with mode indicators
/git:worktree $ARGUMENTS
# where $ARGUMENTS = "list"

# Single worktree creation (existing functionality)
/git:worktree $ARGUMENTS
# where $ARGUMENTS = "add feature/api-improvements ../api-work"

# Remove worktree
/git:worktree $ARGUMENTS
# where $ARGUMENTS = "remove ../api-work"

# Prune stale worktree references
/git:worktree $ARGUMENTS
# where $ARGUMENTS = "prune"
```

### Parallel Mode: Independent Branches → Multiple PRs (Default)

```bash
# Create multiple independent worktrees for parallel development
/git:worktree $ARGUMENTS
# where $ARGUMENTS = "add-multiple feature/auth feature/payments bugfix/header"

# Creates:
# ../wt-auth/     (feature/auth branch)
# ../wt-payments/ (feature/payments branch)
# ../wt-header/   (bugfix/header branch)
# Each worktree independent → separate PRs

# List shows parallel mode worktrees
/git:worktree list
# [parallel] ../wt-auth (feature/auth)
# [parallel] ../wt-payments (feature/payments)
# [parallel] ../wt-header (bugfix/header)
```

### Staging Mode: Consolidated Work → Single PR

```bash
# Create staging branch + multiple child worktrees
/git:worktree $ARGUMENTS
# where $ARGUMENTS = "add-staging integration-q4 feature/auth feature/payments bugfix/header"

# Creates:
# integration-q4 branch (staging branch)
# ../wt-integration/      (integration-q4 base)
# ../wt-integration-auth/ (integration-q4-auth branch)
# ../wt-integration-pay/  (integration-q4-payments branch)
# ../wt-integration-head/ (integration-q4-header branch)
# All child worktrees branch from integration-q4

# List shows staging structure
/git:worktree list
# [staging-parent] ../wt-integration (integration-q4)
# [staging-child]  ../wt-integration-auth (integration-q4-auth)
# [staging-child]  ../wt-integration-pay (integration-q4-payments)
# [staging-child]  ../wt-integration-head (integration-q4-header)
```

### Workflow Decision Guide

```bash
# Use Parallel Mode when:
# ✅ Changes are logically separate
# ✅ Want clean history and atomic PRs
# ✅ Need independent code review cycles
/git:worktree add-multiple feature/login feature/dashboard feature/api

# Use Staging Mode when:
# ✅ Experimenting with related changes
# ✅ Want to consolidate before review
# ✅ Prefer single bundled PR over multiple small ones
/git:worktree add-staging experiment-2024q4 feature/ui-refresh feature/new-flow feature/analytics
```

### Parallel Mode: Independent Branches → Multiple PRs (Default)

```bash
# Create multiple independent worktrees for parallel development
/git:worktree add-multiple feature/auth feature/payments bugfix/header

# Creates:
# ../wt-auth/     (feature/auth branch)
# ../wt-payments/ (feature/payments branch)
# ../wt-header/   (bugfix/header branch)
# Each worktree independent → separate PRs

# List shows parallel mode worktrees
/git:worktree list
# [parallel] ../wt-auth (feature/auth)
# [parallel] ../wt-payments (feature/payments)
# [parallel] ../wt-header (bugfix/header)
```

### Staging Mode: Consolidated Work → Single PR

```bash
# Create staging branch + multiple child worktrees
/git:worktree add-staging integration-q4 feature/auth feature/payments bugfix/header

# Creates:
# integration-q4 branch (staging branch)
# ../wt-integration/      (integration-q4 base)
# ../wt-integration-auth/ (integration-q4-auth branch)
# ../wt-integration-pay/  (integration-q4-payments branch)
# ../wt-integration-head/ (integration-q4-header branch)
# All child worktrees branch from integration-q4

# List shows staging structure
/git:worktree list
# [staging-parent] ../wt-integration (integration-q4)
# [staging-child]  ../wt-integration-auth (integration-q4-auth)
# [staging-child]  ../wt-integration-pay (integration-q4-payments)
# [staging-child]  ../wt-integration-head (integration-q4-header)
```

### Workflow Decision Guide

```bash
# Use Parallel Mode when:
# ✅ Changes are logically separate
# ✅ Want clean history and atomic PRs
# ✅ Need independent code review cycles
/git:worktree add-multiple feature/login feature/dashboard feature/api

# Use Staging Mode when:
# ✅ Experimenting with related changes
# ✅ Want to consolidate before review
# ✅ Prefer single bundled PR over multiple small ones
/git:worktree add-staging experiment-2024q4 feature/ui-refresh feature/new-flow feature/analytics
```

### Parallel Mode: Independent Branches → Multiple PRs (Default)

```bash
# Create multiple independent worktrees for parallel development
/git:worktree add-multiple feature/auth feature/payments bugfix/header

# Creates:
# .trees/auth/     (feature/auth branch)
# .trees/payments/ (feature/payments branch)
# .trees/header/   (bugfix/header branch)
# Each worktree independent → separate PRs

# List shows parallel mode worktrees
/git:worktree list
# [parallel] .trees/auth (feature/auth)
# [parallel] .trees/payments (feature/payments)
# [parallel] .trees/header (bugfix/header)
```

### Staging Mode: Consolidated Work → Single PR

```bash
# Create staging branch + multiple child worktrees
/git:worktree add-staging integration-q4 feature/auth feature/payments bugfix/header

# Creates:
# integration-q4 branch (staging branch)
# .trees/integration/      (integration-q4 base)
# .trees/integration-auth/ (integration-q4-auth branch)
# .trees/integration-pay/  (integration-q4-payments branch)
# .trees/integration-head/ (integration-q4-header branch)
# All child worktrees branch from integration-q4

# List shows staging structure
/git:worktree list
# [staging-parent] .trees/integration (integration-q4)
# [staging-child]  .trees/integration-auth (integration-q4-auth)
# [staging-child]  .trees/integration-pay (integration-q4-payments)
# [staging-child]  .trees/integration-head (integration-q4-header)
```

### Workflow Decision Guide

```bash
# Use Parallel Mode when:
# ✅ Changes are logically separate
# ✅ Want clean history and atomic PRs
# ✅ Need independent code review cycles
/git:worktree add-multiple feature/login feature/dashboard feature/api

# Use Staging Mode when:
# ✅ Experimenting with related changes
# ✅ Want to consolidate before review
# ✅ Prefer single bundled PR over multiple small ones
/git:worktree add-staging experiment-2024q4 feature/ui-refresh feature/new-flow feature/analytics
```

## Output

### For All Operations

- Current worktrees list with paths, branches, and mode indicators
- Confirmation of worktree creation/removal operations
- Working directory status for each worktree

### For Parallel Mode (add-multiple)

- List of all created independent worktrees
- Individual branch → PR workflow guidance for each
- Status dashboard showing parallel development progress
- Directory structure overview for easy navigation

### For Staging Mode (add-staging)

- Staging branch structure with parent/child relationships
- Consolidation workflow guidance (merge/rebase helpers)
- Child worktree integration status
- Single PR preparation guidance after consolidation

## Integration Points

- **Follows**: Repository setup, feature planning
- **Followed by**: /git:commit, /git:push, parallel development workflows
- **Related**: /git:branch, /git:workflow, /git:full-workflow

## Quality Standards

### General Operations

- Validates repository state before all worktree operations

- Ensures proper directory structure and permissions
- Prevents conflicts between worktree branches
- Provides clear feedback on worktree status and location
- Handles cleanup of stale worktree references automatically

### Parallel Mode (add-multiple)

- Auto-generates sensible directory names (.trees/{branch-suffix}/)
- Validates branch names don't conflict with existing worktrees
- Each worktree maintains independence for clean parallel development
- Provides status tracking across all parallel worktrees
- Warns about potential merge conflicts before creation

### Staging Mode (add-staging)

- Creates proper parent/child relationship hierarchy
- Validates staging branch name doesn't conflict with existing branches
- Auto-prefixes child branches to maintain clear association
- Tracks worktree relationships for consolidation workflow
- Prevents mixing of staging and parallel modes without explicit cleanup
- Provides merge/rebase conflict detection between child worktrees

### Cross-Mode Safety

- Clearly identifies worktree modes in all status outputs
- Prevents accidental mode mixing within same directory structure
- Validates workspace cleanliness before batch operations
- Maintains consistent naming conventions across both modes
