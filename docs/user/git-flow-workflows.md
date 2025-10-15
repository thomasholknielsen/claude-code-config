# Git-Flow Complete Workflows

This guide provides step-by-step workflows for all git-flow operations with complete command sequences.

## Table of Contents

- [Feature Development](#feature-development)
- [Release Process](#release-process)
- [Hotfix Emergency Fix](#hotfix-emergency-fix)
- [Complete Feature Cycle](#complete-feature-cycle)
- [Multiple Parallel Features](#multiple-parallel-features)
- [Long-Running Features](#long-running-features)

## Feature Development

### Standard Feature Workflow

Complete cycle from feature creation to merge to develop.

```bash
# Step 1: Create feature branch from develop
/git-flow:feature user-authentication

# Output:
#  Git-Flow mode detected
#  Created branch: feature/user-authentication from develop

# Step 2: Make your changes
# (Edit files in your editor)

# Step 3: Commit changes (creates logical commits by type)
/git:commit

# Output:
#  Analyzing 15 uncommitted files...
#  Grouped into 3 logical commits
#  feat(auth): implement JWT authentication (10 files)
#  test: add authentication tests (4 files)
#  docs: update authentication documentation (1 file)

# Step 4: Push to remote
/git:push

# Output:
#  Pushed to origin/feature/user-authentication

# Step 5: Create PR to develop
/git:pr

# Output:
#  Git-Flow mode detected
#  Auto-detected base: develop (feature branch)
#  PR created: https://github.com/org/repo/pull/123

# Step 6: After PR review and merge
# Branch automatically deleted by GitHub
# Feature is now in develop, ready for next release
```

### Fast Feature Workflow (Single Command)

Use `/workflows:git` for complete workflow in one command:

```bash
# Complete workflow: branch ’ commit ’ push ’ PR
/workflows:git feature/user-authentication

# Output:
#  Git-Flow mode detected
#  Created branch: feature/user-authentication from develop
#  feat(auth): implement JWT authentication (10 files)
#  test: add authentication tests (4 files)
#  docs: update authentication documentation (1 file)
#  Pushed to origin/feature/user-authentication (15 files, 3 commits)
#  PR created: https://github.com/org/repo/pull/123
```

## Release Process

### Complete Release Workflow

From preparing release to production deployment.

```bash
# Prerequisites:
# - Multiple features merged to develop
# - Develop branch is stable
# - Ready to cut a release

# Step 1: Create release branch (auto-detects version or specify)
/git-flow:release 1.2.0

# Output:
#  Git-Flow mode detected
#  Current branch: develop
#  Creating release v1.2.0...
#  Created branch: release/v1.2.0 from develop
#  Updated package.json to 1.2.0
#  Generated CHANGELOG.md:
#    - 8 features
#    - 5 bug fixes
#    - 2 documentation updates
#  Pushed to origin/release/v1.2.0
#  PR created: https://github.com/org/repo/pull/124
#
# =Ý Next Steps:
# 1. Review PR and merge to main
# 2. After merge, run: /git-flow:finish

# Step 2: Review and merge PR
# (Team reviews PR, approves, merges via GitHub interface)

# Step 3: Complete release (tag, merge back to develop, cleanup)
/git-flow:finish

# Output:
#  Git-Flow mode detected
#  Detected branch type: release
#  Version: v1.2.0
#  Verified merge to main:  merged
#
# =Ý Finishing release/v1.2.0...
#  Switched to main
#  Created tag: v1.2.0
#  Pushed tag to origin
#  Merged to develop (--no-ff)
#  Deleted branch: release/v1.2.0 (local + remote)
#
# <‰ Release v1.2.0 complete!
#
# =Ê Summary:
# - Tag: v1.2.0 on main
# - Develop: merged with release changes
# - Branch: deleted (release/v1.2.0)
# - Status: ready for next development cycle

# Step 4: Verify deployment
# Production CI/CD deploys main branch with tag v1.2.0
```

### Auto-Detected Version Release

Let the system determine version bump from commits:

```bash
# Analyze commits since last release and suggest version
/git-flow:release

# Output:
#  Analyzing commits since v1.1.0...
#  Found: 5 feat commits, 3 fix commits, 0 BREAKING CHANGE
#  Suggested version: v1.2.0 (MINOR bump)
#
# Create release v1.2.0? [Y/n]
```

## Hotfix Emergency Fix

### Complete Hotfix Workflow

For critical production bugs requiring immediate fix.

```bash
# Scenario: Critical bug discovered in production

# Step 1: Create hotfix branch from main
/git-flow:hotfix critical-security-patch

# Output:
#  Git-Flow mode detected
#  Current production: v1.2.0
#  Hotfix version: v1.2.1 (PATCH bump)
#  Created branch: hotfix/critical-security-patch from main
#   CRITICAL HOTFIX - This is a production emergency!
#
# =Ý Next Steps:
# 1. Implement MINIMAL fix for the critical issue
# 2. Test thoroughly
# 3. Commit and push
# 4. Create emergency PR
# 5. After merge, run: /git-flow:finish

# Step 2: Implement fix
# (Make minimal changes to fix the issue)

# Step 3: Commit and push
/git:commit

# Output:
#  fix(security): patch critical vulnerability

/git:push

# Output:
#  Pushed to origin/hotfix/critical-security-patch

# Step 4: Create emergency PR
/git:pr

# Output:
#  PR created with 'hotfix' label: https://github.com/org/repo/pull/125

# Step 5: After fast-track approval and merge to main
/git-flow:finish

# Output:
#  Detected branch type: hotfix
#  Version: v1.2.1
#  Created tag: v1.2.1 on main
#  Merged to develop (--no-ff)
#  Deleted branch: hotfix/critical-security-patch
#
# =% Hotfix v1.2.1 complete!
#   Deploy to production immediately!
```

## Complete Feature Cycle

End-to-end feature development with quality gates.

```bash
# Full cycle with testing and review

# 1. Start feature
/git-flow:feature payment-integration

# 2. Develop and test locally
# (Implement feature, write tests)

# 3. Run quality checks
/workflows:run-lint-and-correct-all

# 4. Commit with proper messages
/git:commit

# 5. Push and create PR
/git:push
/git:pr

# 6. After PR approval and merge
# Feature is in develop, ready for next release
```

## Multiple Parallel Features

Working on multiple features simultaneously.

```bash
# Feature 1: Authentication
/git-flow:feature user-authentication
# (work on authentication)
/git:commit
/git:push

# Feature 2: Payment gateway (switch features)
/git-flow:feature payment-gateway
# (work on payments)
/git:commit
/git:push

# Feature 3: Dashboard (another feature)
/git-flow:feature dashboard-redesign
# (work on dashboard)
/git:commit
/git:push

# All three features can be developed in parallel
# Each merges to develop independently via PR
```

## Long-Running Features

Managing features that take multiple days/weeks.

```bash
# Start long-running feature
/git-flow:feature mobile-app

# Day 1: Initial implementation
# (work on feature)
/git:commit
/git:push

# Day 5: Sync with latest develop changes
git fetch origin develop
git merge origin/develop
# (resolve any conflicts)
/git:commit
/git:push

# Day 10: Continue development
# (more work)
/git:commit
/git:push

# Day 15: Final testing and PR
/git:pr

# After review and approval, merge to develop
```

## Git-Flow Status

Check current Git-Flow state anytime.

```bash
# Display comprehensive status
/git-flow:status

# Output shows:
# - Current branch type and info
# - Sync status with remote
# - Working directory state
# - Commit history
# - Merge targets
# - Version information
# - Active branches (features/releases/hotfixes)
# - Recommendations for next steps
```

## Best Practices

### Feature Development

1. **Keep features small and focused** - Easier to review and merge
2. **Sync with develop regularly** - Prevent merge conflicts
3. **Write tests before pushing** - Ensure quality
4. **Use conventional commits** - Better changelog generation
5. **Create PR early** - Get feedback sooner

### Release Management

1. **Stabilize develop before release** - Merge all ready features
2. **Review CHANGELOG carefully** - Ensure accuracy
3. **Test release branch thoroughly** - Production readiness
4. **Use semantic versioning** - Clear version bumps
5. **Complete finish workflow** - Tag and merge back to develop

### Hotfix Protocol

1. **Verify it's truly critical** - Use hotfix only for emergencies
2. **Make minimal changes** - Focus only on the fix
3. **Test extensively** - Don't break production further
4. **Fast-track review** - Speed without sacrificing quality
5. **Deploy and monitor** - Watch for issues post-deployment
6. **Complete finish workflow** - Ensure hotfix reaches develop

## Workflow Comparison

### Atomic vs Workflow Commands

**Atomic Approach** (step-by-step control):

```bash
/git-flow:feature my-feature
# (make changes)
/git:commit
/git:push
/git:pr
```

**Workflow Approach** (single command):

```bash
# Creates branch, commits, pushes, creates PR
/workflows:git feature/my-feature
```

**Use atomic when**:

- You need fine-grained control
- Testing between steps
- Multiple commit cycles

**Use workflow when**:

- Feature is complete and ready
- Want speed and efficiency
- Standard flow without variations

## Troubleshooting

### Branch conflicts with develop

```bash
# On your feature branch
git fetch origin develop
git merge origin/develop
# (resolve conflicts)
/git:commit
/git:push
```

### Forgot to create feature branch

```bash
# Stash your changes
git stash

# Create proper feature branch
/git-flow:feature my-feature

# Apply your changes
git stash pop

# Continue normally
/git:commit
```

### Release branch needs bug fix

```bash
# On release branch
# (fix bugs)
/git:commit
/git:push

# Update PR
# After approval, complete release
/git-flow:finish
```

### Hotfix during active release

```bash
# Hotfix takes priority
/git-flow:hotfix critical-issue

# (fix and deploy)
/git-flow:finish

# Return to release branch
git checkout release/v1.2.0

# Merge hotfix changes if needed
git merge main
```

## Integration with CI/CD

### Automated Testing

```yaml
# Example GitHub Actions workflow
on:
  pull_request:
    branches: [develop, main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: npm test
```

### Automated Deployment

```yaml
# Deploy on tag creation (release/hotfix)
on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: ./deploy.sh
```

## Related Commands

- `/git:commit` - Smart commit generation
- `/git:push` - Safe push with validation
- `/git:pr` - PR creation with auto-detection
- `/git:worktree` - Parallel development
- `/workflows:git` - Complete git workflow
- `/git-flow:feature` - Feature branch creation
- `/git-flow:release` - Release branch creation
- `/git-flow:hotfix` - Hotfix branch creation
- `/git-flow:finish` - Complete branch workflow
- `/git-flow:status` - Git-Flow status display
