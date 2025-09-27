---
description: Push with safety checks, force-push protection, and team coordination
category: git
tools: Bash
---

# Git Push with Safety Checks

I'll help you push changes safely with comprehensive validation, team coordination, and protection against destructive operations.

**Pre-Push Safety Protocol:**

Before any push operations, I'll verify:

- All commits are properly formatted and tested
- No sensitive information in commit history
- Branch protection rules compliance
- Team workflow requirements
- Force-push safety measures

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

# Verify we have commits to push
if git diff --quiet origin/$CURRENT_BRANCH 2>/dev/null; then
    echo "No local commits to push"
    exit 0
fi

echo "Commits to be pushed:"
git log --one-line origin/$CURRENT_BRANCH..HEAD 2>/dev/null || git log --one-line HEAD
```

## Standard Push Operations

**Safe Standard Push:**
```bash
CURRENT_BRANCH=$(git branch --show-current)
REMOTE="origin"

# Fetch latest remote state
echo "Fetching latest remote state..."
git fetch $REMOTE

# Check if remote branch exists
if git ls-remote --heads $REMOTE $CURRENT_BRANCH | grep -q $CURRENT_BRANCH; then
    echo "Remote branch exists, checking for conflicts..."

    # Check if we're behind remote
    LOCAL=$(git rev-parse HEAD)
    REMOTE_COMMIT=$(git rev-parse $REMOTE/$CURRENT_BRANCH)
    BASE=$(git merge-base HEAD $REMOTE/$CURRENT_BRANCH)

    if [ "$LOCAL" = "$REMOTE_COMMIT" ]; then
        echo "Branch is up to date with remote"
        exit 0
    elif [ "$LOCAL" = "$BASE" ]; then
        echo "⚠ Local branch is behind remote"
        echo "Run 'git pull' first to merge remote changes"
        exit 1
    elif [ "$REMOTE_COMMIT" = "$BASE" ]; then
        echo "✓ Safe to push (fast-forward)"
    else
        echo "⚠ Branches have diverged"
        echo "Consider pulling and merging remote changes first"
        echo "Or use force-push with lease (if safe)"
        exit 1
    fi
else
    echo "Creating new remote branch..."
fi
```

**Push with Upstream Tracking:**
```bash
# Push and set upstream tracking for new branches
if ! git ls-remote --heads $REMOTE $CURRENT_BRANCH | grep -q $CURRENT_BRANCH; then
    echo "Setting upstream tracking for new branch..."
    git push -u $REMOTE $CURRENT_BRANCH
else
    git push $REMOTE $CURRENT_BRANCH
fi

echo "✓ Successfully pushed to $REMOTE/$CURRENT_BRANCH"
```

## Protected Branch Handling

**Branch Protection Validation:**
```bash
PROTECTED_BRANCHES="main master production release/* hotfix/*"

# Check if pushing to protected branch
for pattern in $PROTECTED_BRANCHES; do
    if [[ "$CURRENT_BRANCH" == $pattern ]]; then
        echo "⚠ CAUTION: Pushing to protected branch '$CURRENT_BRANCH'"

        # Check branch protection rules (if GitHub CLI available)
        if command -v gh &> /dev/null && gh auth status &>/dev/null; then
            echo "Checking branch protection rules..."
            PROTECTION=$(gh api repos/:owner/:repo/branches/$CURRENT_BRANCH/protection 2>/dev/null)
            if [ -n "$PROTECTION" ]; then
                echo "Branch has protection rules enabled"
                echo "Consider using pull request workflow instead"
            fi
        fi

        echo "Continue with direct push? (y/N)"
        read -r response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            echo "Push cancelled. Consider creating a PR instead:"
            echo "gh pr create --title 'Your PR title' --body 'Description'"
            exit 1
        fi
        break
    fi
done
```

## Pre-Push Quality Checks

**Commit Quality Validation:**
```bash
echo "Running pre-push quality checks..."

# Check commit messages
INVALID_COMMITS=$(git log --pretty=format:"%h %s" origin/$CURRENT_BRANCH..HEAD 2>/dev/null | grep -E "^[a-f0-9]+ (WIP|TODO|FIXME|XXX)" || true)
if [ -n "$INVALID_COMMITS" ]; then
    echo "⚠ Found commits with temporary messages:"
    echo "$INVALID_COMMITS"
    echo "Consider amending commit messages before pushing"
    echo "Continue anyway? (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check for large files
LARGE_FILES=$(git diff --cached --name-only | xargs -I {} sh -c 'if [ -f "{}" ]; then du -h "{}" | awk "$1 ~ /[0-9]+[MG]/ {print}"; fi' 2>/dev/null || true)
if [ -n "$LARGE_FILES" ]; then
    echo "⚠ Large files detected:"
    echo "$LARGE_FILES"
    echo "Consider using Git LFS for large files"
fi
```

**Security Scan:**
```bash
# Check for potential secrets
echo "Scanning for potential secrets..."
SECRET_PATTERNS="password|secret|key|token|api_key|private|credential"
POTENTIAL_SECRETS=$(git log --oneline -p origin/$CURRENT_BRANCH..HEAD 2>/dev/null | grep -iE "$SECRET_PATTERNS" | head -5 || true)

if [ -n "$POTENTIAL_SECRETS" ]; then
    echo "⚠ Potential secrets detected in commits:"
    echo "$POTENTIAL_SECRETS"
    echo ""
    echo "NEVER push real secrets to version control!"
    echo "If these are real secrets, abort and clean history"
    echo "Continue only if these are safe examples/placeholders (y/N)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "Push aborted for security"
        exit 1
    fi
fi
```

**Build and Test Validation:**
```bash
# Run tests before pushing (if available)
if [ -f "package.json" ] && grep -q '"test"' package.json; then
    echo "Running tests before push..."
    if ! npm test; then
        echo "❌ Tests failed! Fix tests before pushing"
        exit 1
    fi
    echo "✓ Tests passed"
elif [ -f "Makefile" ] && grep -q "test:" Makefile; then
    echo "Running make test..."
    if ! make test; then
        echo "❌ Tests failed! Fix tests before pushing"
        exit 1
    fi
    echo "✓ Tests passed"
fi

# Run build if available
if [ -f "package.json" ] && grep -q '"build"' package.json; then
    echo "Running build check..."
    if ! npm run build; then
        echo "❌ Build failed! Fix build errors before pushing"
        exit 1
    fi
    echo "✓ Build successful"
fi
```

## Force Push Operations (Use with Extreme Caution)

**Force Push with Lease (Safer):**
```bash
echo "⚠ DANGER: Force push operation requested"
echo "This can overwrite remote history and affect other team members"
echo ""
echo "Force push options:"
echo "1. --force-with-lease (safer, checks remote state)"
echo "2. --force (dangerous, overwrites everything)"
echo "3. Cancel"
echo ""
echo "Choose option (1/2/3): "
read -r choice

case $choice in
    1)
        echo "Using --force-with-lease for safer force push..."
        if git push --force-with-lease $REMOTE $CURRENT_BRANCH; then
            echo "✓ Force push with lease successful"
        else
            echo "❌ Force push failed - remote has changed"
            echo "Someone else has pushed to this branch"
            echo "Fetch and review changes before force pushing"
        fi
        ;;
    2)
        echo "⚠ EXTREME DANGER: This will overwrite remote history!"
        echo "Type 'I UNDERSTAND THE RISKS' to proceed: "
        read -r confirmation
        if [ "$confirmation" = "I UNDERSTAND THE RISKS" ]; then
            git push --force $REMOTE $CURRENT_BRANCH
            echo "Force push completed - notify team members"
        else
            echo "Force push cancelled"
        fi
        ;;
    3)
        echo "Force push cancelled"
        exit 0
        ;;
    *)
        echo "Invalid option, cancelling"
        exit 1
        ;;
esac
```

**Force Push Safety Checklist:**
```bash
echo "Force push safety checklist:"
echo "□ Have you communicated with team members?"
echo "□ Is this a personal/feature branch (not shared)?"
echo "□ Have you backed up important work?"
echo "□ Are you fixing commit history (not overwriting others' work)?"
echo "□ Have you considered alternatives (revert, new commits)?"
echo ""
echo "All checks confirmed? (yes/NO): "
read -r confirmation
if [[ "$confirmation" != "yes" ]]; then
    echo "Force push cancelled for safety"
    exit 1
fi
```

## Multi-Remote Push

**Push to Multiple Remotes:**
```bash
# List all configured remotes
echo "Available remotes:"
git remote -v

# Push to all remotes
echo "Push to all remotes? (y/N): "
read -r response
if [[ "$response" =~ ^[Yy]$ ]]; then
    for remote in $(git remote); do
        echo "Pushing to $remote..."
        if git push $remote $CURRENT_BRANCH; then
            echo "✓ Successfully pushed to $remote"
        else
            echo "❌ Failed to push to $remote"
        fi
    done
fi
```

## Push with Tags

**Push Tags with Commits:**
```bash
# Check for new tags
NEW_TAGS=$(git tag --points-at HEAD)
if [ -n "$NEW_TAGS" ]; then
    echo "New tags to push: $NEW_TAGS"
    echo "Push tags along with commits? (y/N): "
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        git push --tags $REMOTE $CURRENT_BRANCH
        echo "✓ Pushed commits and tags"
    fi
else
    git push $REMOTE $CURRENT_BRANCH
fi
```

## Post-Push Operations

**Success Confirmation:**
```bash
echo "✓ Push completed successfully!"
echo ""
echo "Post-push information:"
echo "Remote URL: $(git remote get-url $REMOTE)"
echo "Branch: $CURRENT_BRANCH"
echo "Commits pushed: $(git rev-list --count origin/$CURRENT_BRANCH..HEAD^ 2>/dev/null || echo 'N/A')"

# Show push result
git log --one-line -5 origin/$CURRENT_BRANCH 2>/dev/null || git log --one-line -5
```

**Team Notification:**
```bash
# If this is a shared branch, suggest notifying team
SHARED_BRANCHES="develop integration staging"
if echo $SHARED_BRANCHES | grep -w $CURRENT_BRANCH > /dev/null; then
    echo ""
    echo "📢 Consider notifying team members about changes to $CURRENT_BRANCH"
    echo "Changes include:"
    git log --one-line origin/$CURRENT_BRANCH..HEAD^ 2>/dev/null || echo "Recent commits"
fi
```

## Integration with .specify/ Context

If `.specify/` folder exists, I'll:
- Validate pushed commits align with feature specifications
- Check task completion status in `tasks.md`
- Ensure implementation matches `plan.md` requirements
- Maintain consistency with project contracts

**Emergency Recovery:**
```bash
# If push causes issues, provide recovery options
echo ""
echo "If this push caused issues, recovery options:"
echo "1. Revert last commit: git revert HEAD"
echo "2. Reset remote branch: git push --force-with-lease origin HEAD~1:$CURRENT_BRANCH"
echo "3. Contact team for coordination"
```

This command provides comprehensive push safety with team coordination, security checks, and protection against destructive operations.