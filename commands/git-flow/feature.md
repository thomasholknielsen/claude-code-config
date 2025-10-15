---
description: "Create a new Git Flow feature branch from develop with proper naming and tracking"
argument-hint: "<feature-name>"
allowed-tools: Bash(git:*), mcp__sequential-thinking__sequentialthinking
---

# Git Flow Feature Branch

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create Git Flow feature branch from develop with validation (git repo check, feature name validation, uncommitted changes detection), switch to develop, pull latest, create feature/<name> branch, set up remote tracking with -u flag

**P**urpose: Enforce Git Flow branching strategy with proper feature branch creation from develop (not main), maintain clean working directory, ensure remote tracking for collaboration, follow kebab-case naming conventions

**E**xpectation: New feature branch created with pattern `feature/<descriptive-name>`, tracking origin/feature/<name>, clean working directory, develop synced with remote, clear next steps for feature development workflow

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% git-flow requirements, Accuracy >90% branch setup, Relevance >85% naming compliance, Efficiency <10s branch creation)

Create new feature branch: **$ARGUMENTS**

## Current Repository State

- Current branch: !`git branch --show-current`
- Git status: !`git status --porcelain`
- Develop branch status: !`git log develop..origin/develop --oneline 2>/dev/null | head -5 || echo "No remote tracking for develop"`

## Task

Create a Git Flow feature branch following these steps:

### 1. Pre-Flight Validation

- **Check git repository**: Verify we're in a valid git repository
- **Validate feature name**: Ensure `$ARGUMENTS` is provided and follows naming conventions:
  - ✅ Valid: `user-authentication`, `payment-integration`, `dashboard-redesign`
  - ❌ Invalid: `feat1`, `My_Feature`, empty name
- **Check for uncommitted changes**:
  - If changes exist, warn user and ask to commit/stash first
  - OR offer to stash changes automatically
- **Verify develop branch exists**: Ensure `develop` branch is present

### 2. Create Feature Branch

Execute the following workflow:

```bash
# Switch to develop branch
git checkout develop

# Pull latest changes from remote
git pull origin develop

# Create feature branch with Git Flow naming convention
git checkout -b feature/$ARGUMENTS

# Set up remote tracking
git push -u origin feature/$ARGUMENTS
```

### 3. Provide Status Report

After successful creation, display:

```
✓ Switched to develop branch
✓ Pulled latest changes from origin/develop
✓ Created branch: feature/$ARGUMENTS
✓ Set up remote tracking: origin/feature/$ARGUMENTS
✓ Pushed branch to remote

🌿 Feature Branch Ready

Branch: feature/$ARGUMENTS
Base: develop
Status: Clean working directory

🎯 Next Steps:
1. Start implementing your feature
2. Make commits using conventional format:
   git commit -m "feat: your changes"
3. Push changes regularly: git push
4. When complete, use /finish to merge back to develop

💡 Git Flow Tips:
- Keep commits atomic and well-described
- Push frequently to avoid conflicts
- Use conventional commit format (feat:, fix:, etc.)
- Test thoroughly before finishing
```

### 4. Error Handling

Handle these scenarios gracefully:

**Uncommitted Changes:**

```
⚠️  You have uncommitted changes:
M  src/file1.js
M  src/file2.js

Options:
1. Commit changes first
2. Stash changes: git stash
3. Discard changes: git checkout .

What would you like to do? [1/2/3]
```

**Feature Name Not Provided:**

```
❌ Feature name is required

Usage: /feature <feature-name>

Examples:
  /feature user-profile-page
  /feature api-v2-integration
  /feature payment-gateway

Feature names should:
- Be descriptive and concise
- Use kebab-case (lowercase-with-hyphens)
- Describe what the feature does
```

**Branch Already Exists:**

```
❌ Branch feature/$ARGUMENTS already exists

Existing feature branches:
  feature/user-authentication
  feature/payment-gateway
  feature/$ARGUMENTS ← This one

Options:
1. Switch to existing branch: git checkout feature/$ARGUMENTS
2. Use a different feature name
3. Delete existing and recreate (destructive!)
```

**Develop Behind Remote:**

```
⚠️  Local develop is behind origin/develop by 5 commits

✓ Pulling latest changes...
✓ Develop is now up to date
✓ Ready to create feature branch
```

**No Develop Branch:**

```
❌ Develop branch not found

Git Flow requires a 'develop' branch. Create it with:
  git checkout -b develop
  git push -u origin develop

Or initialize Git Flow:
  git flow init
```

## Git Flow Context

This command is part of the Git Flow branching strategy:

- **main**: Production-ready code (protected)
- **develop**: Integration branch for features (protected)
- **feature/***: New features (you are here)
- **release/***: Release preparation
- **hotfix/***: Emergency production fixes

Feature branches:

- Branch from: `develop`
- Merge back to: `develop`
- Naming convention: `feature/<descriptive-name>`
- Lifecycle: Short to medium term

## Environment Variables

This command respects:

- `GIT_FLOW_DEVELOP_BRANCH`: Develop branch name (default: "develop")
- `GIT_FLOW_PREFIX_FEATURE`: Feature prefix (default: "feature/")

## Related Commands

- `/finish` - Complete and merge feature branch to develop
- `/flow-status` - Check current Git Flow status
- `/release <version>` - Create release branch from develop
- `/hotfix <name>` - Create hotfix branch from main

## Best Practices

**DO:**

- ✅ Use descriptive feature names
- ✅ Keep feature scope focused and small
- ✅ Push to remote regularly
- ✅ Test your changes before finishing
- ✅ Use conventional commit messages

**DON'T:**

- ❌ Create features directly from main
- ❌ Use generic names like "feature1"
- ❌ Let feature branches live too long
- ❌ Mix multiple unrelated features
- ❌ Skip testing before merging
