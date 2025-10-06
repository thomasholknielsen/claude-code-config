---
description: "Complete git workflow: create branch, commit changes, push, and create PR in one command"
argument-hint: "[branch-name]"
allowed-tools: Bash(git:*), Bash(gh:*), Read, Write
---

# Command: Git Full Workflow

## Purpose

Executes the complete git workflow from uncommitted changes to pull request creation, automating branch creation, commits, push, and PR generation in a single atomic operation.

## Usage

```bash
/git:full-workflow [branch-name]
```

**Arguments**:

- `[branch-name]` (optional): Custom branch name. If not provided, auto-generates from commit type/scope

## Process

1. **Validate State**: Check git status and ensure repository is in clean state
2. **Analyze Changes**: Detect commit type from uncommitted files (feat/fix/docs/etc.)
3. **Create Branch**: Generate branch name from commit type and create feature branch
4. **Create Commits**: Generate conventional commit messages and commit changes
5. **Push Branch**: Push to remote with upstream tracking
6. **Create PR**: Generate PR title/description and create pull request
7. **Return URL**: Provide PR URL for immediate access

## Implementation Pattern

This command performs all git operations directly (only /git:* commands can do git operations):

```bash
# Step 1: Validate and analyze
git status
git diff --name-status

# Step 2: Create branch (if not provided)
BRANCH_NAME=${1:-"auto-generated-from-commit-type"}
git checkout -b "$BRANCH_NAME"

# Step 3: Commit changes
git add .
git commit -m "$(generate_commit_message)"

# Step 4: Push with tracking
git push -u origin "$BRANCH_NAME"

# Step 5: Create PR
gh pr create --title "PR Title" --body "PR Description"
```

## Agent Integration

- **Primary Agent**: N/A - Direct git operations (no agent needed)
- **Git Operations**: All operations performed directly via Bash tool
- **Constraint Compliance**: This command is in /git category, authorized for git operations

## Examples

### Auto-generated branch name

```bash
/git:full-workflow

# Output:
# ✅ Created branch: feat/user-authentication
# ✅ Committed: feat(auth): implement JWT authentication
# ✅ Pushed to origin/feat/user-authentication
# ✅ PR created: https://github.com/org/repo/pull/123
```

### Custom branch name

```bash
/git:full-workflow feature/custom-name

# Output:
# ✅ Created branch: feature/custom-name
# ✅ Committed: feat: custom feature implementation
# ✅ Pushed to origin/feature/custom-name
# ✅ PR created: https://github.com/org/repo/pull/124
```

## Integration Points

- **Replaces**: Sequential /git:branch → /git:commit → /git:push → /git:pr pattern
- **Used by**: /workflows:run-git-branch-commit-and-pr (invokes this as ONE command)
- **Follows**: Code implementation, feature completion, bug fixes
- **Followed by**: Code review, CI/CD pipeline

## Quality Standards

- Validates git state before operations
- Uses conventional commit format
- Handles errors gracefully with rollback capability
- Returns PR URL for immediate access
- Maintains git history integrity
- Respects repository git constraints (only /git:* can do git ops)

## Error Handling

- **Dirty working tree**: Aborts if uncommitted changes conflict
- **Branch exists**: Switches to existing branch or creates unique name
- **Push fails**: Provides remediation steps
- **PR creation fails**: Returns commit hash and manual PR creation instructions
