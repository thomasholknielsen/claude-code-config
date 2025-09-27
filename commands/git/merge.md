---
description: Controlled merge operations with conflict resolution and safety checks
category: git
tools: Bash
---

# Git Merge Management

I'll help you perform safe, controlled merge operations with comprehensive conflict resolution and team workflow integration.

**Pre-Merge Safety Protocol:**
Before any merge operations, I'll verify:
- Both branches are up to date with their remotes
- Working directory is clean
- No conflicting changes that could cause data loss
- Branch protection rules and merge policies
- Required status checks and approvals

First, let me assess the current repository state:

```bash
# Verify we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository"
    echo "This command requires git version control"
    exit 1
fi

# Check current branch and status
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"
git status --porcelain

# Verify clean working directory
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "Error: Working directory not clean"
    echo "Commit or stash changes before merging"
    git status --short
    exit 1
fi
```

## Merge Strategies

**Fast-Forward Merge (Default):**
```bash
TARGET_BRANCH="feature/branch-name"

# Update both branches from remote
git fetch origin

# Switch to target branch and verify it's current
git checkout $TARGET_BRANCH
git pull origin $TARGET_BRANCH

# Switch back and attempt fast-forward merge
git checkout $CURRENT_BRANCH
git pull origin $CURRENT_BRANCH

# Check if fast-forward is possible
if git merge-base --is-ancestor $CURRENT_BRANCH $TARGET_BRANCH; then
    echo "Fast-forward merge possible"
    git merge $TARGET_BRANCH
else
    echo "Fast-forward not possible, branches have diverged"
    echo "Consider using --no-ff or rebase strategy"
fi
```

**No-Fast-Forward Merge (Preserve History):**
```bash
# Create explicit merge commit even when fast-forward is possible
git merge --no-ff $TARGET_BRANCH -m "Merge $TARGET_BRANCH into $CURRENT_BRANCH

Merge includes:
- Feature implementation
- Test coverage
- Documentation updates"
```

**Squash Merge (Clean History):**
```bash
# Squash all commits from feature branch into single commit
git merge --squash $TARGET_BRANCH

# Review the squashed changes
git diff --cached

# Create meaningful commit message
git commit -m "feat: implement user authentication system

- Add login/logout functionality
- Implement JWT token management
- Add password reset flow
- Include comprehensive test coverage

Squashed from $TARGET_BRANCH"
```

## Pre-Merge Analysis

**Conflict Detection:**
```bash
# Check for potential conflicts before merging
echo "Analyzing potential conflicts..."
git merge-tree $(git merge-base $CURRENT_BRANCH $TARGET_BRANCH) $CURRENT_BRANCH $TARGET_BRANCH > /dev/null

if [ $? -eq 0 ]; then
    echo "✓ No conflicts detected"
else
    echo "⚠ Potential conflicts found"
    echo "Files that may conflict:"
    git diff --name-only $CURRENT_BRANCH $TARGET_BRANCH
fi
```

**Impact Assessment:**
```bash
# Show what will be merged
echo "Changes to be merged from $TARGET_BRANCH:"
git log --oneline $CURRENT_BRANCH..$TARGET_BRANCH
echo ""
echo "Files affected:"
git diff --stat $CURRENT_BRANCH..$TARGET_BRANCH
echo ""
echo "Detailed changes:"
git diff $CURRENT_BRANCH..$TARGET_BRANCH
```

## Conflict Resolution

**Automatic Conflict Detection:**
```bash
# Attempt merge and handle conflicts
if ! git merge $TARGET_BRANCH; then
    echo "Merge conflicts detected!"
    echo "Conflicted files:"
    git status --porcelain | grep "^UU\|^AA\|^DD"

    echo ""
    echo "Conflict resolution options:"
    echo "1. Manual resolution: Edit files, then 'git add' and 'git commit'"
    echo "2. Abort merge: git merge --abort"
    echo "3. Use ours: git checkout --ours ."
    echo "4. Use theirs: git checkout --theirs ."
fi
```

**Interactive Conflict Resolution:**
```bash
# Show conflicts in detail
git status
echo ""
echo "Conflict markers in files:"
git diff --name-only --diff-filter=U | while read file; do
    echo "=== $file ==="
    grep -n "<<<<<<< \|======= \|>>>>>>> " "$file" || true
    echo ""
done
```

**Merge Tools Integration:**
```bash
# Use configured merge tool
if git config merge.tool >/dev/null 2>&1; then
    echo "Opening merge tool: $(git config merge.tool)"
    git mergetool
else
    echo "No merge tool configured. Available options:"
    echo "- VS Code: git config merge.tool vscode"
    echo "- Vim: git config merge.tool vimdiff"
    echo "- Meld: git config merge.tool meld"
fi
```

## Advanced Merge Operations

**Partial Merge (Specific Files):**
```bash
# Merge only specific files from another branch
git checkout $TARGET_BRANCH -- path/to/specific/file.js path/to/another/file.css

# Stage the changes
git add path/to/specific/file.js path/to/another/file.css

# Commit with explanation
git commit -m "merge: cherry-pick specific files from $TARGET_BRANCH

Only merged:
- path/to/specific/file.js - New functionality
- path/to/another/file.css - Updated styles"
```

**Three-Way Merge with Custom Base:**
```bash
# Find common ancestor
MERGE_BASE=$(git merge-base $CURRENT_BRANCH $TARGET_BRANCH)
echo "Common ancestor: $MERGE_BASE"

# Perform three-way merge with explicit base
git merge -s recursive -X ours $TARGET_BRANCH
```

**Octopus Merge (Multiple Branches):**
```bash
# Merge multiple branches simultaneously (use with caution)
git merge branch1 branch2 branch3
```

## Branch-Specific Merge Policies

**Production Branch Protection:**
```bash
PROTECTED_BRANCHES="main master production"
TARGET_BRANCH_TO_MERGE="feature/new-feature"

if echo $PROTECTED_BRANCHES | grep -w $CURRENT_BRANCH > /dev/null; then
    echo "⚠ Merging into protected branch: $CURRENT_BRANCH"

    # Check for required approvals (if GitHub CLI available)
    if command -v gh &> /dev/null && gh auth status &>/dev/null; then
        echo "Checking branch protection rules..."
        gh api repos/:owner/:repo/branches/$CURRENT_BRANCH/protection 2>/dev/null || echo "No protection rules found"
    fi

    echo "Continue with merge? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "Merge cancelled"
        exit 1
    fi
fi
```

**Release Branch Workflow:**
```bash
# Merge into release branch with version tagging
if [[ $CURRENT_BRANCH == release/* ]]; then
    echo "Merging into release branch"

    # Perform merge
    git merge --no-ff $TARGET_BRANCH -m "Merge $TARGET_BRANCH into $CURRENT_BRANCH for release"

    # Extract version from branch name
    VERSION=$(echo $CURRENT_BRANCH | sed 's/release\///')

    # Create version tag
    git tag -a "v$VERSION" -m "Release version $VERSION"
    echo "Created tag: v$VERSION"
fi
```

## Post-Merge Operations

**Automatic Cleanup:**
```bash
# After successful merge, offer to clean up
echo "Merge completed successfully!"
echo ""
echo "Post-merge cleanup options:"
echo "1. Delete merged branch locally: git branch -d $TARGET_BRANCH"
echo "2. Delete merged branch remotely: git push origin --delete $TARGET_BRANCH"
echo "3. Push merged changes: git push origin $CURRENT_BRANCH"
echo ""
echo "Perform cleanup? (y/N)"
read -r response
if [[ "$response" =~ ^[Yy]$ ]]; then
    # Delete local branch if it was merged
    git branch -d $TARGET_BRANCH 2>/dev/null && echo "Deleted local branch: $TARGET_BRANCH"

    # Push the merge
    git push origin $CURRENT_BRANCH && echo "Pushed merged changes"
fi
```

**Merge Verification:**
```bash
# Verify merge integrity
echo "Verifying merge integrity..."

# Check that all commits from target branch are included
MISSING_COMMITS=$(git log $TARGET_BRANCH --not $CURRENT_BRANCH --oneline)
if [ -z "$MISSING_COMMITS" ]; then
    echo "✓ All commits successfully merged"
else
    echo "⚠ Some commits may not have been merged:"
    echo "$MISSING_COMMITS"
fi

# Run tests if test command exists
if [ -f "package.json" ] && grep -q '"test"' package.json; then
    echo "Running tests to verify merge..."
    npm test
elif [ -f "Makefile" ] && grep -q "test:" Makefile; then
    make test
fi
```

## Emergency Recovery

**Abort Merge:**
```bash
# Cancel merge in progress
git merge --abort
echo "Merge aborted, repository restored to pre-merge state"
```

**Undo Completed Merge:**
```bash
# Find the merge commit
MERGE_COMMIT=$(git log --merges -1 --pretty=format:"%H")
echo "Last merge commit: $MERGE_COMMIT"

# Reset to before merge (use with caution)
echo "This will undo the last merge. Continue? (y/N)"
read -r response
if [[ "$response" =~ ^[Yy]$ ]]; then
    git reset --hard HEAD~1
    echo "Merge undone. Repository reset to pre-merge state."
fi
```

## Integration with .specify/ Context

If `.specify/` folder exists, I'll:
- Validate merge against feature specifications in `spec.md`
- Check implementation completeness per `plan.md`
- Ensure all tasks in `tasks.md` are completed
- Maintain consistency with project contracts

**Quality Assurance:**
Before completing any merge:
1. All tests must pass
2. Build must succeed
3. No linting errors
4. Security checks pass
5. Documentation is updated

**Team Workflow Integration:**
- Respects branch protection rules
- Validates required status checks
- Follows merge commit conventions
- Integrates with CI/CD pipelines
- Maintains audit trail

This command provides comprehensive merge management with safety checks, conflict resolution, and team workflow compliance.