---
description: Create and manage pull requests with GitHub CLI integration
category: git
tools: Bash
---

# Git Pull Request Management

I'll help you create, manage, and review pull requests using GitHub CLI with comprehensive quality checks.

**Pre-PR Quality Validation:**
Before creating any pull request, I'll verify:
- All changes are committed and pushed
- Build passes (if build command exists)
- Tests pass (if test command exists)
- Linter passes (if lint command exists)
- Branch is up to date with base branch

First, let me verify GitHub CLI setup and repository state:

```bash
# Verify GitHub CLI is installed and authenticated
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) not found"
    echo "Install from: https://cli.github.com"
    exit 1
fi

# Verify authentication
if ! gh auth status &>/dev/null; then
    echo "Error: Not authenticated with GitHub"
    echo "Run: gh auth login"
    exit 1
fi

# Verify we're in a git repository with GitHub remote
if ! git remote -v | grep -q github.com; then
    echo "Error: No GitHub remote found"
    echo "This command requires a GitHub repository"
    exit 1
fi

# Check current branch and status
echo "Current branch and status:"
git branch --show-current
git status --porcelain
```

**Pull Request Operations:**

## Create New Pull Request

I'll analyze your current branch and create a comprehensive PR:

```bash
# Get current branch info
CURRENT_BRANCH=$(git branch --show-current)
BASE_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')

# Check if branch is ahead of base
if ! git log $BASE_BRANCH..HEAD --oneline | grep -q .; then
    echo "Error: No commits ahead of $BASE_BRANCH"
    echo "Nothing to create PR for"
    exit 1
fi

# Show commits that will be included
echo "Commits to be included in PR:"
git log $BASE_BRANCH..HEAD --oneline --reverse
```

**Smart PR Analysis:**
I'll analyze your commits to determine:
1. PR type (feature, bugfix, hotfix, documentation, etc.)
2. Scope and impact of changes
3. Dependencies and breaking changes
4. Test coverage requirements
5. Documentation updates needed

Based on the analysis, I'll create a professional PR with:
- **Title**: Clear, descriptive following conventional format
- **Description**: Summary, changes, testing, breaking changes
- **Labels**: Automatically applied based on change analysis
- **Reviewers**: Suggested based on CODEOWNERS or team structure
- **Milestone**: Aligned with project roadmap if detected

```bash
# Create PR with comprehensive description
gh pr create \
  --title "feat(scope): clear description of changes" \
  --body "$(cat <<'EOF'
## Summary
Brief description of what this PR accomplishes.

## Changes
- Bullet point list of specific changes
- Focus on what and why, not how

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests passing
- [ ] Manual testing completed

## Breaking Changes
None / [List any breaking changes]

## Documentation
- [ ] Code comments updated
- [ ] README updated if needed
- [ ] API docs updated if needed

## Checklist
- [ ] Code follows project conventions
- [ ] Tests added for new functionality
- [ ] Documentation updated
- [ ] No merge conflicts
EOF
)"
```

## Manage Existing Pull Requests

**List PRs:**
```bash
# Show all PRs for this repository
gh pr list --state all

# Show PRs assigned to you
gh pr list --assignee @me

# Show PRs by specific author
gh pr list --author username
```

**View PR Details:**
```bash
# Show detailed PR information
gh pr view [PR_NUMBER] --web

# Show PR diff
gh pr diff [PR_NUMBER]

# Show PR checks/status
gh pr checks [PR_NUMBER]
```

**Update PR:**
```bash
# Update PR title and description
gh pr edit [PR_NUMBER] --title "new title" --body "new description"

# Add reviewers
gh pr edit [PR_NUMBER] --add-reviewer username1,username2

# Add labels
gh pr edit [PR_NUMBER] --add-label "enhancement,needs-review"
```

**PR Reviews:**
```bash
# Request review from specific users
gh pr review [PR_NUMBER] --request-changes --body "Review comments"

# Approve PR
gh pr review [PR_NUMBER] --approve --body "LGTM!"

# Add general comment
gh pr comment [PR_NUMBER] --body "Comment text"
```

**Merge PR:**
```bash
# Merge with different strategies
gh pr merge [PR_NUMBER] --merge    # Create merge commit
gh pr merge [PR_NUMBER] --squash   # Squash and merge
gh pr merge [PR_NUMBER] --rebase   # Rebase and merge

# Auto-merge when checks pass
gh pr merge [PR_NUMBER] --auto --squash
```

**Close/Reopen PR:**
```bash
# Close PR without merging
gh pr close [PR_NUMBER]

# Reopen closed PR
gh pr reopen [PR_NUMBER]
```

## Draft PR Workflow

For work-in-progress features:
```bash
# Create draft PR
gh pr create --draft --title "WIP: feature description"

# Convert draft to ready for review
gh pr ready [PR_NUMBER]

# Convert back to draft
gh pr edit [PR_NUMBER] --draft
```

## Cross-Fork PR Management

For contributing to external repositories:
```bash
# Create PR from fork to upstream
gh pr create --repo upstream-owner/repo-name \
  --head your-username:feature-branch \
  --base main
```

**Integration with .specify/ Context:**
If `.specify/` folder exists, I'll:
- Reference `spec.md` for feature requirements validation
- Check `plan.md` for architectural compliance
- Validate against `tasks.md` completion criteria
- Include relevant context in PR description

**Quality Assurance:**
Before PR creation, I'll run:
1. Code quality checks (linting, formatting)
2. Test suite validation
3. Build verification
4. Security scan if configured
5. Documentation completeness check

**Error Handling:**
If PR creation fails:
- Check for merge conflicts with base branch
- Verify all commits are pushed
- Ensure branch protection rules are met
- Validate required status checks
- Handle rate limiting gracefully

**Important Security Notes:**
- Never expose sensitive information in PR descriptions
- Follow repository's security and contribution guidelines
- Respect branch protection rules and required reviews
- Maintain clean commit history

This command provides comprehensive GitHub PR workflow management while maintaining security and quality standards.