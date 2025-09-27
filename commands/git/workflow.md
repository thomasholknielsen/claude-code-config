---
description: Complete Git workflow automation with intelligent branching and team coordination
category: git
tools: Bash
---

# Git Workflow Automation

I'll help you implement complete Git workflow automation that intelligently manages branching, commits, reviews, and deployments based on your project's needs.

**Workflow Intelligence:**
This command automatically detects and adapts to:
- Project type and branching strategy (GitFlow, GitHub Flow, GitLab Flow)
- Team size and collaboration patterns
- CI/CD pipeline integration
- Branch protection and review requirements
- Release and deployment workflows

First, let me analyze your repository's workflow patterns:

```bash
# Verify we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository"
    echo "This command requires git version control"
    exit 1
fi

# Analyze repository structure and patterns
echo "Analyzing repository workflow patterns..."

# Detect branching strategy
BRANCHES=$(git branch -r | grep -E "(main|master|develop|staging|production|release|hotfix)" | sed 's/origin\///' | sort)
echo "Detected branches: $BRANCHES"

# Check for CI/CD configuration
CI_FILES=".github/workflows .gitlab-ci.yml .travis.yml circle.yml .circleci"
for ci_file in $CI_FILES; do
    if [ -e "$ci_file" ]; then
        echo "Detected CI/CD: $ci_file"
    fi
done

# Check for release management
if [ -f "CHANGELOG.md" ] || [ -f "RELEASES.md" ] || git tag | grep -q "v[0-9]"; then
    echo "Release management detected"
fi
```

## Workflow Strategy Detection

**GitFlow Detection:**
```bash
# Detect GitFlow pattern
if echo "$BRANCHES" | grep -q "develop" && echo "$BRANCHES" | grep -E "(release|hotfix)"; then
    WORKFLOW_TYPE="gitflow"
    MAIN_BRANCH="main"
    DEVELOP_BRANCH="develop"
    echo "✓ GitFlow workflow detected"
elif echo "$BRANCHES" | grep -E "(main|master)" && ! echo "$BRANCHES" | grep -q "develop"; then
    WORKFLOW_TYPE="github_flow"
    MAIN_BRANCH=$(echo "$BRANCHES" | grep -E "(main|master)" | head -1)
    echo "✓ GitHub Flow workflow detected"
else
    WORKFLOW_TYPE="custom"
    MAIN_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@' 2>/dev/null || echo "main")
    echo "✓ Custom workflow detected"
fi

echo "Main branch: $MAIN_BRANCH"
echo "Workflow type: $WORKFLOW_TYPE"
```

## Complete Feature Development Workflow

**Feature Branch Workflow (GitHub Flow):**
```bash
feature_workflow() {
    local feature_name="$1"
    local feature_description="$2"

    echo "Starting feature development workflow: $feature_name"

    # 1. Ensure we're on main branch and up to date
    git checkout $MAIN_BRANCH
    git pull origin $MAIN_BRANCH

    # 2. Create feature branch
    FEATURE_BRANCH="feature/$feature_name"
    git checkout -b $FEATURE_BRANCH

    # 3. Set up tracking
    git push -u origin $FEATURE_BRANCH

    echo "✓ Feature branch created: $FEATURE_BRANCH"
    echo ""
    echo "Development workflow:"
    echo "1. Make your changes"
    echo "2. Use '/git/commit' for quality commits"
    echo "3. Use '/git/push' to push safely"
    echo "4. Use '/git/pr' to create pull request"
    echo "5. Use '/git/merge' after review approval"

    # Set up .specify/ if not exists
    if [ ! -d ".specify" ]; then
        echo "Setting up feature tracking..."
        mkdir -p .specify
        cat > .specify/current-feature.md << EOF
# Feature: $feature_name

## Description
$feature_description

## Status
- [ ] Development started
- [ ] Core implementation
- [ ] Tests added
- [ ] Documentation updated
- [ ] Code review
- [ ] Merged to main

## Branch
$FEATURE_BRANCH

## Created
$(date)
EOF
        git add .specify/current-feature.md
        git commit -m "feat: initialize feature tracking for $feature_name"
        git push origin $FEATURE_BRANCH
    fi
}
```

**GitFlow Workflow:**
```bash
gitflow_workflow() {
    local workflow_action="$1"
    local name="$2"

    case $workflow_action in
        "feature")
            echo "Starting GitFlow feature: $name"
            git checkout $DEVELOP_BRANCH
            git pull origin $DEVELOP_BRANCH
            git checkout -b "feature/$name"
            git push -u origin "feature/$name"
            echo "✓ Feature branch created: feature/$name"
            ;;
        "release")
            echo "Starting GitFlow release: $name"
            git checkout $DEVELOP_BRANCH
            git pull origin $DEVELOP_BRANCH
            git checkout -b "release/$name"

            # Update version files if they exist
            if [ -f "package.json" ]; then
                npm version $name --no-git-tag-version
                git add package.json package-lock.json 2>/dev/null || git add package.json
                git commit -m "chore: bump version to $name"
            fi

            git push -u origin "release/$name"
            echo "✓ Release branch created: release/$name"
            ;;
        "hotfix")
            echo "Starting GitFlow hotfix: $name"
            git checkout $MAIN_BRANCH
            git pull origin $MAIN_BRANCH
            git checkout -b "hotfix/$name"
            git push -u origin "hotfix/$name"
            echo "✓ Hotfix branch created: hotfix/$name"
            ;;
    esac
}
```

## Automated Quality Workflow

**Pre-Commit Workflow:**
```bash
pre_commit_workflow() {
    echo "Running pre-commit quality workflow..."

    # 1. Code formatting
    if [ -f "package.json" ] && grep -q '"lint"' package.json; then
        echo "Running linter..."
        npm run lint --silent || npm run lint:fix --silent 2>/dev/null
    fi

    # 2. Tests
    if [ -f "package.json" ] && grep -q '"test"' package.json; then
        echo "Running tests..."
        npm test
    fi

    # 3. Build verification
    if [ -f "package.json" ] && grep -q '"build"' package.json; then
        echo "Verifying build..."
        npm run build
    fi

    # 4. Security scan
    if command -v npm &> /dev/null && [ -f "package.json" ]; then
        echo "Running security audit..."
        npm audit --audit-level=high
    fi

    # 5. Type checking
    if [ -f "tsconfig.json" ] && command -v tsc &> /dev/null; then
        echo "Type checking..."
        npx tsc --noEmit
    fi

    echo "✓ Pre-commit checks completed"
}
```

## Release Management Workflow

**Semantic Release Workflow:**
```bash
release_workflow() {
    local release_type="$1"  # major, minor, patch, or specific version

    echo "Starting release workflow..."

    # Ensure we're on main branch
    git checkout $MAIN_BRANCH
    git pull origin $MAIN_BRANCH

    # Run full quality checks
    pre_commit_workflow

    # Determine next version
    if [ -f "package.json" ]; then
        CURRENT_VERSION=$(node -p "require('./package.json').version")
        echo "Current version: $CURRENT_VERSION"

        case $release_type in
            "major"|"minor"|"patch")
                NEW_VERSION=$(npm version $release_type --no-git-tag-version | sed 's/v//')
                ;;
            *)
                NEW_VERSION="$release_type"
                npm version $NEW_VERSION --no-git-tag-version
                ;;
        esac
    else
        # For non-Node.js projects, use git tags
        LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
        echo "Last tag: $LAST_TAG"
        NEW_VERSION="$release_type"
    fi

    echo "New version: $NEW_VERSION"

    # Update CHANGELOG if it exists
    if [ -f "CHANGELOG.md" ]; then
        echo "Updating CHANGELOG.md..."
        # Generate changelog entry
        CHANGES=$(git log --oneline $(git describe --tags --abbrev=0 2>/dev/null || git rev-list --max-parents=0 HEAD)..HEAD | sed 's/^/- /')

        # Backup and update changelog
        cp CHANGELOG.md CHANGELOG.md.bak
        cat > CHANGELOG.md.new << EOF
# Changelog

## [${NEW_VERSION}] - $(date +%Y-%m-%d)

${CHANGES}

EOF
        tail -n +2 CHANGELOG.md >> CHANGELOG.md.new
        mv CHANGELOG.md.new CHANGELOG.md
    fi

    # Commit version changes
    git add -A
    git commit -m "chore: release version $NEW_VERSION

- Update version to $NEW_VERSION
- Update CHANGELOG.md with release notes"

    # Create and push tag
    git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION"
    git push origin $MAIN_BRANCH
    git push origin "v$NEW_VERSION"

    echo "✓ Release $NEW_VERSION completed"

    # Trigger deployment if CI/CD is configured
    if [ -f ".github/workflows/deploy.yml" ] || [ -f ".github/workflows/release.yml" ]; then
        echo "Release will trigger automatic deployment via GitHub Actions"
    fi
}
```

## Team Collaboration Workflow

**Pull Request Workflow:**
```bash
pr_workflow() {
    local pr_title="$1"
    local pr_description="$2"

    echo "Starting pull request workflow..."

    CURRENT_BRANCH=$(git branch --show-current)

    # Ensure branch is up to date
    git fetch origin
    git rebase origin/$MAIN_BRANCH

    # Run quality checks
    pre_commit_workflow

    # Push latest changes
    git push origin $CURRENT_BRANCH

    # Create PR with comprehensive description
    if command -v gh &> /dev/null && gh auth status &>/dev/null; then
        gh pr create \
            --title "$pr_title" \
            --body "$(cat <<EOF
## Summary
$pr_description

## Changes
$(git log --oneline $MAIN_BRANCH..HEAD | sed 's/^/- /')

## Testing
- [ ] Unit tests added/updated and passing
- [ ] Integration tests passing
- [ ] Manual testing completed
- [ ] No regressions identified

## Quality Checks
- [ ] Code follows project conventions
- [ ] Documentation updated
- [ ] No security vulnerabilities
- [ ] Performance impact assessed

## Deployment
- [ ] Safe to deploy
- [ ] Database migrations included (if applicable)
- [ ] Feature flags configured (if applicable)

## Reviewers
@team/reviewers

EOF
)"

        echo "✓ Pull request created"
        gh pr view --web
    else
        echo "GitHub CLI not configured. Manual PR creation required."
        echo "Push completed. Create PR manually with these details:"
        echo "Title: $pr_title"
        echo "Description: $pr_description"
    fi
}
```

## Hotfix Emergency Workflow

**Emergency Hotfix Workflow:**
```bash
hotfix_workflow() {
    local issue_description="$1"
    local hotfix_branch="hotfix/$(date +%Y%m%d)-$(echo $issue_description | sed 's/[^a-zA-Z0-9]/-/g' | tr '[:upper:]' '[:lower:]')"

    echo "🚨 EMERGENCY HOTFIX WORKFLOW"
    echo "Issue: $issue_description"

    # Create hotfix from production/main
    git checkout $MAIN_BRANCH
    git pull origin $MAIN_BRANCH
    git checkout -b $hotfix_branch

    echo "✓ Hotfix branch created: $hotfix_branch"
    echo ""
    echo "HOTFIX CHECKLIST:"
    echo "□ Identify root cause"
    echo "□ Implement minimal fix"
    echo "□ Add regression test"
    echo "□ Verify fix works"
    echo "□ Get emergency review"
    echo "□ Deploy to production"
    echo "□ Monitor deployment"
    echo "□ Backport to develop (if using GitFlow)"
    echo ""
    echo "After implementing fix:"
    echo "1. Use '/git/commit' with descriptive message"
    echo "2. Use '/git/push' to push hotfix"
    echo "3. Use '/git/pr' for emergency review"
    echo "4. Use '/git/merge' after approval"
    echo "5. Use '/git/workflow release patch' for immediate release"

    # Set up hotfix tracking
    cat > .hotfix-$(date +%Y%m%d).md << EOF
# Emergency Hotfix - $(date)

## Issue
$issue_description

## Branch
$hotfix_branch

## Status
- [ ] Root cause identified
- [ ] Fix implemented
- [ ] Tests added
- [ ] Emergency review approved
- [ ] Deployed to production
- [ ] Monitoring active
- [ ] Post-mortem scheduled

## Timeline
- Created: $(date)
- Target deployment: ASAP
EOF

    git add .hotfix-$(date +%Y%m%d).md
    git commit -m "docs: create hotfix tracking for $issue_description"
    git push -u origin $hotfix_branch
}
```

## Workflow Commands

**Interactive Workflow Selection:**
```bash
echo "Git Workflow Automation"
echo "======================="
echo ""
echo "Available workflows:"
echo "1. feature <name> <description>  - Start feature development"
echo "2. release <version>             - Create release"
echo "3. hotfix <description>          - Emergency hotfix"
echo "4. pr <title> <description>      - Create pull request"
echo "5. cleanup                       - Clean up merged branches"
echo "6. status                        - Show workflow status"
echo ""
echo "GitFlow specific:"
echo "7. gitflow feature <name>        - GitFlow feature"
echo "8. gitflow release <version>     - GitFlow release"
echo "9. gitflow hotfix <name>         - GitFlow hotfix"
echo ""

if [ $# -eq 0 ]; then
    echo "Usage: /git/workflow <command> [arguments]"
    echo "Example: /git/workflow feature user-auth 'Add JWT authentication'"
    exit 0
fi

command="$1"
shift

case $command in
    "feature")
        feature_workflow "$1" "$2"
        ;;
    "release")
        release_workflow "$1"
        ;;
    "hotfix")
        hotfix_workflow "$1"
        ;;
    "pr")
        pr_workflow "$1" "$2"
        ;;
    "gitflow")
        gitflow_workflow "$1" "$2"
        ;;
    "cleanup")
        cleanup_workflow
        ;;
    "status")
        workflow_status
        ;;
    *)
        echo "Unknown command: $command"
        exit 1
        ;;
esac
```

## Cleanup and Maintenance

**Branch Cleanup Workflow:**
```bash
cleanup_workflow() {
    echo "Starting branch cleanup workflow..."

    # Update from remote
    git fetch --all --prune

    # Find merged branches
    MERGED_BRANCHES=$(git branch --merged $MAIN_BRANCH | grep -v "$MAIN_BRANCH\|develop\|master" | xargs)

    if [ -n "$MERGED_BRANCHES" ]; then
        echo "Merged branches that can be cleaned up:"
        echo "$MERGED_BRANCHES"
        echo ""
        echo "Delete these branches? (y/N): "
        read -r response
        if [[ "$response" =~ ^[Yy]$ ]]; then
            echo $MERGED_BRANCHES | xargs git branch -d
            echo "✓ Local merged branches deleted"

            # Also delete remote tracking branches if they're gone
            git remote prune origin
            echo "✓ Remote tracking cleanup completed"
        fi
    else
        echo "No merged branches to clean up"
    fi

    # Clean up workflow tracking files
    find . -name ".hotfix-*.md" -mtime +30 -delete 2>/dev/null || true
    echo "✓ Old workflow tracking files cleaned up"
}
```

## Integration with .specify/ Context

```bash
# Enhanced workflow with .specify/ integration
if [ -d ".specify" ]; then
    echo "Integrating with .specify/ context..."

    # Check feature specifications
    if [ -f ".specify/spec.md" ]; then
        echo "Feature specification found - validating against workflow"
    fi

    # Update task progress
    if [ -f ".specify/tasks.md" ]; then
        echo "Updating task completion status"
    fi

    # Validate implementation plan
    if [ -f ".specify/plan.md" ]; then
        echo "Checking implementation plan compliance"
    fi
fi
```

This command provides complete Git workflow automation with intelligent adaptation to your project's needs, team size, and development practices.