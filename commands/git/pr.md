---
description: "Create and manage pull requests with GitHub CLI integration"
argument-hint: "[title]"
allowed-tools: Bash, Read, Grep, mcp__sequential-thinking__sequentialthinking
---

# Command: Pr

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create GitHub PR with workflow mode detection (Git-Flow: feature/*→ develop, release/hotfix/* → main; Conventional: * → main), auto-generate PR title/description from branch file changes (git diff origin/<base>...HEAD), validate gh CLI auth, check for existing PR, execute gh pr create with formatted title/body

**P**urpose: Streamline PR creation with intelligent base branch selection, conventional title formatting (Title Case), comprehensive descriptions from file analysis, avoid duplicates, provide immediate PR URL for team collaboration

**E**xpectation: PR created with auto-detected base branch (develop for features in git-flow, main otherwise), conventional title format `<type>: <Title Case Description>`, comprehensive description with file change summary, PR URL returned, clear error messages with manual fallback

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% PR requirements, Accuracy >90% base branch detection, Relevance >85% conventional format, Efficiency <15s PR creation)

## Purpose

Creates pull requests with auto-generated descriptions and returns the PR URL for immediate access.

## Usage

```bash
/git:pr $ARGUMENTS
```

**Arguments**:

- `$1` (title): PR title (optional, auto-generated from commits if not provided)
- `$2` (--draft): Create as draft PR (optional)
- `$3` (--base): Base branch for PR (optional, auto-detected in git-flow mode, defaults to main)

**$ARGUMENTS Examples**:

**Git-Flow Mode** (base branch auto-detected):

- `$ARGUMENTS = "Add user authentication"` - feature/* → targets develop (auto)
- `$ARGUMENTS = "--draft"` - Draft PR with auto-detected base
- `$ARGUMENTS = "Release v1.2.0"` - release/* → targets main (auto)
- `$ARGUMENTS = "Fix login bug --base=develop"` - Override auto-detection

**Conventional Mode**:

- `$ARGUMENTS = "Add user authentication system"` - PR with custom title (targets main)
- `$ARGUMENTS = "--draft"` - Create draft PR with auto-generated title
- `$ARGUMENTS = "Fix login bug --base=develop"` - PR targeting develop branch

## Process

1. **Detect repository workflow mode and auto-select base branch:**
   - Check if `develop` branch exists: `git branch -a | grep -q "develop"`
   - Check if `main` branch exists: `git branch -a | grep -q "main"`
   - Get current branch name: `git symbolic-ref --short HEAD`
   - **If Git-Flow mode detected (main + develop exist):**
     - `feature/*` → base = `develop` (unless `--base` specified)
     - `release/*` → base = `main` (unless `--base` specified)
     - `hotfix/*` → base = `main` (unless `--base` specified)
   - **Otherwise (Conventional mode):**
     - base = `main` (or `--base` if specified)
2. **Analyze branch file changes for PR context:**
   - Run `git diff origin/<base>...HEAD --name-status` to see all changes in branch
   - Analyze file changes between base and current branch
   - Determine primary type from file analysis (not commits)
   - Extract scope from consistent file paths across branch
   - Never rely on commit messages for type detection
3. **Parse or generate PR title:**
   - If title provided: Extract type, validate, format to Title Case
   - If no title: Auto-generate from branch file changes
   - Format: `<type>: <Title Case Description>`
   - Or with scope: `<type>(<scope>): <Title Case Description>`
   - Validate type is conventional: feat, fix, docs, style, refactor, test, chore, perf, ci, build
4. **Generate PR description:**
   - Summary of file changes (not commit messages)
   - List modified files grouped by type
   - Include test files modified
   - Add conventional type badges
   - Include breaking changes if detected
5. Create pull request using GitHub CLI with formatted title and description to detected base
6. Set appropriate labels, reviewers, and milestones if configured
7. Return PR URL for immediate access and review

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned for handling git operations and coordination

## Examples

### Git-Flow Mode Examples

```bash
# Feature PR (auto-targets develop)
/git:pr
# Current branch: feature/user-auth
# Output: ✓ Git-Flow mode detected
#         ✓ Creating PR: feature/user-auth → develop

# Release PR (auto-targets main)
/git:pr "Release v1.2.0"
# Current branch: release/v1.2.0
# Output: ✓ Git-Flow mode detected
#         ✓ Creating PR: release/v1.2.0 → main

# Hotfix PR (auto-targets main)
/git:pr "Critical security fix"
# Current branch: hotfix/security-patch
# Output: ✓ Git-Flow mode detected
#         ✓ Creating PR: hotfix/security-patch → main

# Override base branch
/git:pr --base=staging
# Output: ✓ Git-Flow mode detected
#         ✓ Creating PR: feature/experiment → staging (override)
```

### Conventional Mode Examples

```bash
# Create PR with auto-generated title and description
/git:pr

# Create PR with custom title
/git:pr "Add user authentication system"

# Create draft PR for work in progress
/git:pr --draft "WIP: Refactor payment processing"

# Target specific base branch
/git:pr "Add payments" --base=develop
```

## Output

- Created PR URL for immediate access
- PR title and description summary
- Assigned reviewers and labels (if configured)
- Next steps for the review process

## Integration Points

- **Follows**: /git:push, development completion
- **Followed by**: Code review process, CI/CD pipeline
- **Related**: /git-flow:feature, /git:commit, /workflows:git

## Type Auto-Detection from Branch Changes

Analyzes `git diff origin/<base>...HEAD --name-status` to determine PR type (same priority as commits):

1. **All documentation files** → `docs:`
2. **All test files** → `test:`
3. **Dependency files** → `chore:`
4. **CI configuration** → `ci:`
5. **Build configuration** → `build:`
6. **New files added** → `feat:`
7. **Files with fix/bug keywords** → `fix:`
8. **Performance files** → `perf:`
9. **Only formatting changes** → `style:`
10. **Default for code modifications** → `refactor:`

**Scope Detection:** Extracts scope from consistent directory patterns across all branch changes.

**Title Case Conversion:** Automatically formats PR titles in Title Case for consistency.

## Implementation Pattern

```bash
# Step 1: Pre-flight checks
if ! command -v gh &> /dev/null; then
  echo "❌ GitHub CLI (gh) not installed. Install: https://cli.github.com/"
  exit 1
fi

if ! gh auth status &> /dev/null; then
  echo "❌ GitHub CLI not authenticated. Run: gh auth login"
  exit 1
fi

# Step 2: Check if branch exists on remote
BRANCH_NAME=$(git symbolic-ref --short HEAD)
if ! git ls-remote --exit-code --heads origin "$BRANCH_NAME" &> /dev/null; then
  echo "❌ Branch not found on remote: $BRANCH_NAME"
  echo "Push branch first: git push -u origin $BRANCH_NAME"
  exit 1
fi

# Step 3: Check if PR already exists
if EXISTING_PR=$(gh pr list --head "$BRANCH_NAME" --json url --jq '.[0].url' 2>/dev/null); then
  if [ -n "$EXISTING_PR" ]; then
    echo "ℹ️  PR already exists: $EXISTING_PR"
    exit 0
  fi
fi

# Step 4: Generate PR title and description
PR_TITLE=$(generate_pr_title_from_branch_changes)
PR_BODY=$(generate_pr_body_from_branch_changes)

# Step 5: Attempt PR creation with comprehensive error handling
if ! PR_URL=$(gh pr create --title "$PR_TITLE" --body "$PR_BODY" 2>&1); then
  echo "❌ PR creation failed"
  echo ""
  echo "Error: $PR_URL"
  echo ""
  echo "Possible causes:"
  echo "1. GitHub CLI authentication expired - Run: gh auth login"
  echo "2. Insufficient permissions - Check repository access"
  echo "3. Branch protection rules require review"
  echo ""
  echo "Manual PR creation:"
  REPO_URL=$(git remote get-url origin | sed 's/.*://;s/.git$//')
  echo "  1. Visit: https://github.com/$REPO_URL/compare/$BRANCH_NAME"
  echo "  2. Or run: gh pr create --web"
  echo ""
  exit 1
fi

echo "✅ PR created: $PR_URL"
```

## Quality Standards

- **Detects workflow mode automatically** - Identifies Git-Flow or Conventional mode
- **Git-Flow aware base branch** - Auto-detects base from branch type in git-flow mode:
  - feature/* → develop
  - release/* → main
  - hotfix/* → main
- **Manual override supported** - Use `--base=<branch>` to override auto-detection
- **Validates GitHub CLI authentication** - Pre-flight check prevents silent failures
- **Verifies branch on remote** - Ensures branch is pushed before PR creation
- **Checks for existing PR** - Avoids duplicate PR creation
- **Enforces conventional PR titles** - Uses type prefixes matching commit conventions
- **Auto-detects type from branch file changes** - Analyzes file diffs, not commit messages
- **Formats titles in Title Case** - Converts descriptions to proper case
- **Comprehensive error handling** - Provides actionable error messages and manual instructions
- Generates descriptive PR titles from file analysis
- Creates comprehensive PR descriptions with change summary
- Includes test plan and verification steps when applicable
- Links related issues and references automatically
- Returns immediate PR URL for team collaboration
- Follows repository PR template when available
- Sets appropriate draft status for work-in-progress
- Groups file changes by conventional type in description

## Error Handling

### GitHub CLI Not Installed

```
❌ GitHub CLI (gh) not installed
Install: https://cli.github.com/
```

### GitHub CLI Not Authenticated

```
❌ GitHub CLI not authenticated
Run: gh auth login
```

### Branch Not on Remote

```
❌ Branch not found on remote: feature/auth
Push branch first: git push -u origin feature/auth
```

### PR Already Exists

```
ℹ️  PR already exists: https://github.com/org/repo/pull/123
```

### PR Creation Failed

```
❌ PR creation failed
Error: gh: authentication token expired

Possible causes:
1. GitHub CLI authentication expired - Run: gh auth login
2. Insufficient permissions - Check repository access
3. Branch protection rules require review

Manual PR creation:
  1. Visit: https://github.com/org/repo/compare/branch-name
  2. Or run: gh pr create --web
```
