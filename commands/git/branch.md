---
description: Branch management operations with safety checks and team workflows
category: git
tools: Bash
---

# Git Branch Management

I'll help you create, switch, manage, and clean up branches with comprehensive safety checks and team workflow integration.

**Pre-Operation Safety Checks:**
Before any branch operations, I'll verify:
- Working directory is clean (no uncommitted changes)
- Current branch state and remote tracking
- Potential conflicts with team workflows
- Branch protection rules and policies

First, let me check the current repository state:

```bash
# Verify we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository"
    echo "This command requires git version control"
    exit 1
fi

# Show current branch status
echo "Current branch information:"
git branch --show-current
git status --porcelain

# Check for uncommitted changes
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "Warning: Uncommitted changes detected"
    echo "Consider committing or stashing changes before branch operations"
    git status --short
fi
```

## Branch Creation

**Create New Feature Branch:**
```bash
# Get base branch (usually main/master)
BASE_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@' 2>/dev/null || echo "main")

# Ensure base branch is up to date
echo "Updating base branch: $BASE_BRANCH"
git fetch origin
git checkout $BASE_BRANCH
git pull origin $BASE_BRANCH

# Create and switch to new branch
BRANCH_NAME="feature/your-feature-name"
git checkout -b $BRANCH_NAME
git push -u origin $BRANCH_NAME

echo "Created and switched to branch: $BRANCH_NAME"
echo "Tracking remote: origin/$BRANCH_NAME"
```

**Smart Branch Naming:**
I'll suggest branch names based on:
- **Feature branches**: `feature/user-authentication`, `feature/payment-integration`
- **Bug fixes**: `bugfix/login-timeout`, `hotfix/security-patch`
- **Documentation**: `docs/api-updates`, `docs/readme-improvements`
- **Refactoring**: `refactor/user-service`, `refactor/database-layer`
- **Experimental**: `experiment/new-framework`, `spike/performance-test`

## Branch Navigation

**Switch Between Branches:**
```bash
# List all branches (local and remote)
git branch -a

# Switch to existing branch
git checkout branch-name

# Switch with safety check for uncommitted changes
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "Uncommitted changes detected. Options:"
    echo "1. Commit changes: git add . && git commit -m 'WIP: save progress'"
    echo "2. Stash changes: git stash push -m 'WIP: temporary stash'"
    echo "3. Force switch (loses changes): git checkout --force branch-name"
    exit 1
else
    git checkout branch-name
fi
```

**Recent Branch Navigation:**
```bash
# Switch to previous branch
git checkout -

# Show recent branches
git for-each-ref --sort=-committerdate refs/heads/ --format='%(refname:short) %(committerdate:relative)'
```

## Branch Information and Analysis

**Branch Status:**
```bash
# Show current branch with tracking info
git status -b --porcelain

# Show branch relationships
git show-branch --all

# Compare with base branch
git log --oneline $BASE_BRANCH..HEAD
git diff --stat $BASE_BRANCH..HEAD
```

**Branch History:**
```bash
# Show commits unique to this branch
git log --oneline --graph --decorate $BASE_BRANCH..HEAD

# Show files changed in this branch
git diff --name-status $BASE_BRANCH..HEAD

# Show branch creation point
git merge-base $BASE_BRANCH HEAD
```

## Remote Branch Management

**Sync with Remote:**
```bash
# Fetch all remote branches
git fetch --all --prune

# List remote branches
git branch -r

# Track remote branch locally
git checkout --track origin/remote-branch-name

# Update current branch from remote
git pull origin $(git branch --show-current)
```

**Push Branch with Safety:**
```bash
CURRENT_BRANCH=$(git branch --show-current)

# Check if branch exists on remote
if git ls-remote --heads origin $CURRENT_BRANCH | grep -q $CURRENT_BRANCH; then
    echo "Branch exists on remote, updating..."
    git push origin $CURRENT_BRANCH
else
    echo "Creating new remote branch..."
    git push -u origin $CURRENT_BRANCH
fi
```

## Branch Cleanup

**Delete Local Branches:**
```bash
# List merged branches (safe to delete)
git branch --merged | grep -v "$(git branch --show-current)" | grep -v "main\|master\|develop"

# Delete merged branch
git branch -d branch-name

# Force delete unmerged branch (use with caution)
git branch -D branch-name
```

**Delete Remote Branches:**
```bash
# Delete remote branch
git push origin --delete branch-name

# Prune deleted remote branches locally
git remote prune origin
```

**Automated Cleanup:**
```bash
# Clean up merged branches (interactive)
echo "Merged branches that can be safely deleted:"
MERGED_BRANCHES=$(git branch --merged | grep -v "$(git branch --show-current)" | grep -v "main\|master\|develop" | xargs)

if [ -n "$MERGED_BRANCHES" ]; then
    echo $MERGED_BRANCHES
    echo "Delete these branches? (y/N)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        echo $MERGED_BRANCHES | xargs git branch -d
        echo "Deleted merged branches"
    fi
else
    echo "No merged branches to clean up"
fi
```

## Branch Protection and Team Workflows

**Check Branch Protection:**
```bash
# Check if GitHub CLI is available for protection rules
if command -v gh &> /dev/null && gh auth status &>/dev/null; then
    echo "Branch protection rules:"
    gh api repos/:owner/:repo/branches/$(git branch --show-current)/protection 2>/dev/null || echo "No protection rules found"
fi
```

**Pre-Push Validation:**
```bash
# Validate before pushing to protected branches
CURRENT_BRANCH=$(git branch --show-current)
PROTECTED_BRANCHES="main master develop production"

if echo $PROTECTED_BRANCHES | grep -w $CURRENT_BRANCH > /dev/null; then
    echo "Warning: Pushing to protected branch '$CURRENT_BRANCH'"
    echo "Consider creating a feature branch and PR instead"
    echo "Continue? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "Push cancelled"
        exit 1
    fi
fi
```

## Advanced Branch Operations

**Branch Comparison:**
```bash
# Compare two branches
git diff branch1..branch2
git log --oneline branch1..branch2

# Find common ancestor
git merge-base branch1 branch2

# Show divergence point
git show-branch branch1 branch2
```

**Branch Renaming:**
```bash
# Rename current branch
OLD_NAME=$(git branch --show-current)
NEW_NAME="feature/new-name"

git branch -m $OLD_NAME $NEW_NAME

# Update remote tracking
if git ls-remote --heads origin $OLD_NAME | grep -q $OLD_NAME; then
    git push origin :$OLD_NAME  # Delete old remote branch
    git push -u origin $NEW_NAME  # Push new branch
fi
```

**Cherry-pick Between Branches:**
```bash
# Cherry-pick specific commit to current branch
git cherry-pick commit-hash

# Cherry-pick range of commits
git cherry-pick commit1..commit2
```

## Integration with .specify/ Context

If `.specify/` folder exists, I'll:
- Create branch names aligned with current feature work
- Reference `spec.md` for branch naming conventions
- Check `plan.md` for implementation phases
- Validate branch strategy against project architecture

**Error Handling and Recovery:**

**Recover from Failed Operations:**
```bash
# Undo last branch operation
git reflog  # Find the commit you want to return to
git reset --hard HEAD@{n}  # Replace n with reflog entry

# Recover deleted branch
git reflog --all | grep "branch-name"
git checkout -b branch-name commit-hash
```

**Conflict Resolution:**
```bash
# If branch operations create conflicts
git status  # Check conflicted files
# Edit files to resolve conflicts
git add resolved-files
git commit  # Complete the operation
```

**Team Workflow Integration:**
- Respects branch naming conventions
- Checks for required status checks
- Validates against CODEOWNERS
- Follows merge policies
- Integrates with CI/CD pipelines

This command provides comprehensive branch management while maintaining team workflow compliance and repository safety.