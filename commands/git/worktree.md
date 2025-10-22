---
description: "Manages git worktrees for parallel development with shared repository history"
argument-hint: "[action] [arguments...]"
allowed-tools: Bash, Read, Grep, mcp__sequential-thinking__sequentialthinking
---

# Command: Worktree

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Create and manage git worktrees for parallel development in separate directories.

**YOU MUST:**
1. ✓ Parse action (add/add-multiple/remove/list/prune) from $ARGUMENTS
2. ✓ For add: Create worktree with auto-generated path
3. ✓ For add-multiple: Batch create worktrees in parallel mode
4. ✓ For remove: Delete worktree directory and references
5. ✓ For list: Show all worktrees with status
6. ✓ Display clear status for each worktree

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Remove worktrees without confirmation
- ✗ Skip status reporting

---

## EXECUTE THIS NOW

**You MUST execute this command immediately using the Bash tool:**

1. ✓ Parse action: add | add-multiple | remove | list | prune
2. ✓ For add/add-multiple: Execute `git worktree add <path> [<branch>]`
3. ✓ For remove: Execute `git worktree remove <path>`
4. ✓ For list: Execute `git worktree list --porcelain`
5. ✓ For prune: Execute `git worktree prune`
6. ✓ Report status for each worktree operation

Do NOT just describe what should happen - actively execute git worktree commands NOW using the Bash tool.

---

## IMPLEMENTATION FLOW

### Step 1: Parse Action
Extract action and arguments

### Step 2: Validate Repository
Check git repo status

### Step 3: Execute Action
Add/remove/list worktrees based on action

### Step 4: Manage Paths
Auto-generate or parse directory paths

### Step 5: Report Status
Show all worktrees with mode and status

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create and manage git worktrees for parallel development with actions (add/add-multiple/add-staging/remove/list/prune), auto-generate directory paths, support parallel mode (independent branches) and staging mode (consolidated work), track worktree relationships

**P**urpose: Enable simultaneous work on multiple branches without context switching, support parallel development (multiple PRs) or staging workflows (single PR), maintain shared repository history with independent working directories

**E**xpectation: Worktrees created with proper directory structure (.trees/ paths), clear mode indicators (parallel/staging-parent/staging-child), working status for each worktree, consolidation guidance for staging mode, efficient parallel development support

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% worktree requirements, Accuracy >90% directory structure, Relevance >85% workflow guidance, Efficiency <15s worktree creation)

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
- **Related**: /git:branch, /git:complete, /git:complete

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
