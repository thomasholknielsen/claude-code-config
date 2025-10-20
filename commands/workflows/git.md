---
description: "Complete git workflow: create branch, logical commits, push, and create PR"
argument-hint: "[branch-name]"
allowed-tools: Bash, Read, Grep, mcp__sequential-thinking__sequentialthinking
---

# Command: Workflow

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Execute complete git workflow - create branch, group changes into logical commits, push, and create PR.

**YOU MUST:**
1. ✓ Auto-detect workflow mode (git-flow vs conventional commits)
2. ✓ Analyze uncommitted changes and group by type (feat/fix/docs/test)
3. ✓ Create branch from appropriate base (develop for git-flow, HEAD for conventional)
4. ✓ Create logical commits (one per type group)
5. ✓ Push with tracking (-u flag)
6. ✓ Create PR with appropriate base branch
7. ✓ Handle errors with clear manual fallback

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Create single monolithic commit (group by type)
- ✗ Skip PR creation

---

## IMPLEMENTATION FLOW

### Step 1: Pre-flight Validation
Check gh CLI auth, validate git repo state

### Step 2: Workflow Detection
Detect git-flow (develop + main) vs conventional (main only)

### Step 3: Analyze Changes
Run git diff HEAD, group files by conventional type (feat/fix/docs/test)

### Step 4: Create Branch
Use provided name or auto-generate from primary type, create from appropriate base

### Step 5: Logical Commits
For each type group: stage files, detect scope, generate conventional message, commit

### Step 6: Push & PR
Push with -u flag, detect base branch, create PR via gh CLI

---

## Framework Structure (S-Tier Pattern)

### CO-STAR Framework (Orchestration)

**C**ontext: Complete git workflow orchestration for Git-Flow and Conventional Commits modes, with intelligent commit grouping by type (feat, fix, docs, test), branch creation from appropriate base (develop for features in git-flow, HEAD for conventional), and GitHub PR creation with error handling

**O**bjective: Auto-detect workflow mode (git-flow vs conventional), analyze uncommitted changes, group files by conventional type, create logical commits (one per type), push with tracking, create PR with appropriate base branch (develop for features, main for others), handle errors gracefully with manual fallback

**S**tyle: Command-line automation with comprehensive validation (gh CLI auth, git repo state), logical commit grouping (feat/fix/docs/test separation), conventional commit messages with scope detection, and detailed error messages with manual instructions

**T**one: Direct, automated, developer-friendly with emphasis on workflow efficiency - clear progress indicators, explicit error messages, actionable fallback instructions

**A**udience: Software engineers requiring streamlined git workflows with automatic commit grouping, branch management, and PR creation - supports both Git-Flow and Conventional Commits patterns

**R**esults: Branch created/switched, logical commits by type pushed to origin with tracking, PR created with auto-detected base branch, or detailed error with manual fallback instructions

## Analysis Methodology

### 1. Pre-flight Validation: Check gh CLI installation and authentication, validate git repo state (no conflicts, clean working tree), ensure current branch up-to-date

### 2. Workflow Detection: Check for develop + main branches (git-flow mode) vs main only (conventional mode), determine base branch (develop for features, HEAD for others)

### 3. Change Analysis: Run git diff HEAD to get uncommitted files, group files by conventional type (feat, fix, docs, test, chore), detect scope from file paths within each group

### 4. Branch Creation: Use provided branch name or auto-generate from primary commit type, create branch from appropriate base (develop in git-flow, HEAD in conventional)

### 5. Logical Commits: For each type group, stage files of that type only, detect scope, generate conventional message, create commit

### 6. Push & PR: Push all commits with -u flag for tracking, detect appropriate PR base branch (develop for feature/*, main for others in git-flow), create PR with gh CLI or provide manual fallback

## Explicit Constraints

**IN SCOPE**: Git workflow orchestration, commit grouping by type, branch creation (git-flow and conventional modes), conventional commit formatting, PR creation with error handling, GitHub CLI integration
**OUT OF SCOPE**: Code implementation (developer responsibility), git repository initialization (git init), git configuration management (git config), merge conflict resolution (manual resolution required)

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% workflow steps, Accuracy >90% commit grouping, Relevance >85% conventional format compliance, Efficiency <30s for typical workflows)

## Purpose

Executes complete git workflow with intelligent commit grouping - creates branch, groups changes into logical commits by type, pushes, and creates PR with comprehensive error handling.

## EXECUTE THIS NOW

**You MUST execute this command immediately using the Bash tool:**

```bash
bash ~/.claude/scripts/workflows/git.sh "$@"
```

Do NOT just describe what should happen - actively run this command using the Bash tool right now.

---

## Implementation

Execute the git workflow automation script with the provided branch name argument (or auto-generate):

```bash
bash ~/.claude/scripts/workflows/git.sh $ARGUMENTS
```

The script handles all workflow steps: pre-flight validation, workflow detection, change analysis, branch creation, logical commits, push with tracking, and PR creation.

## Usage

```bash
/workflows:git $ARGUMENTS
```

**Arguments**:

- `$1` (branch-name): Optional custom branch name. Auto-generates from primary commit type if not provided.

**$ARGUMENTS Examples**:

**Git-Flow Mode** (main + develop branches detected):

- `$ARGUMENTS = "feature/auth"` - Create feature from develop
- `$ARGUMENTS = ""` - Auto-generate feature/ branch from changes

**Conventional Mode** (default):

- `$ARGUMENTS = "feat/auth"` - Custom branch name from HEAD
- `$ARGUMENTS = ""` - Auto-generate branch name from changes

## Process

### 1. Pre-flight Validation

- Check `gh` CLI is installed and authenticated
- Validate git repository state (no conflicts, clean working tree)
- Ensure current branch is up-to-date with remote

### 2. Detect Workflow Mode

- Check if `develop` branch exists: `git branch -a | grep -q "develop"`
- Check if `main` branch exists: `git branch -a | grep -q "main"`
- If both exist: **Git-Flow mode** detected
- Otherwise: **Conventional mode** (default)

### 3. Analyze & Group Changes

- Run `git diff HEAD --name-status` to get all uncommitted files
- Group files by conventional commit type (feat, fix, docs, test, chore, etc.)
- Detect scope from file paths within each type group
- **Result:** Logical commit groups instead of monolithic commit

### 4. Create Branch

- If branch name provided: Use it
- If not provided: Auto-generate from primary commit type
- **Git-Flow mode format**: `feature/<description>` (branches from develop)
- **Conventional mode format**: `<type>/<description>` or `<type>/<scope>/<description>` (branches from HEAD)
- Create and switch to new branch from appropriate base

### 5. Create Logical Commits

**CRITICAL:** Group changes by type and create separate commits

For each type group (feat, fix, docs, test, etc.):

1. Stage only files of this type
2. Detect scope from file paths in group
3. Generate conventional commit message for this type
4. Create commit
5. Report commit created

**Example Output:**

```
✅ feat(auth): implement JWT authentication (12 files)
✅ docs: update authentication documentation (3 files)
✅ test: add authentication test coverage (8 files)
```

### 6. Push with Tracking

- Push all commits to origin with `-u` flag
- Set up branch tracking for future pulls
- Report total files and commits pushed

### 7. Create PR with Error Handling

- **If Git-Flow mode:** Auto-detect base branch:
  - `feature/*` → base = `develop`
  - Other branches → base = `main`
- **If Conventional mode:** base = `main`

- Verify branch exists on remote (push succeeded)
- Check if PR already exists for this branch
- Generate PR title from primary commit type (Title Case)
- Generate PR description from all commits and file changes
- Attempt PR creation with `gh pr create`
- **If fails:** Provide detailed error message and manual instructions

## Implementation Pattern

This command groups files by type and creates logical commits:

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

# Step 2: Analyze and group files by type
declare -A file_groups
while IFS= read -r file; do
  type=$(detect_conventional_type "$file")
  file_groups["$type"]+="$file "
done < <(git diff HEAD --name-only)

# Step 2: Detect workflow mode
if git branch -a | grep -q "develop" && git branch -a | grep -q "main"; then
  MODE="git-flow"
  BASE_BRANCH="develop"  # Feature branches from develop
  echo "✓ Git-Flow mode detected"
else
  MODE="conventional"
  BASE_BRANCH="HEAD"
  echo "✓ Conventional mode"
fi

# Step 3: Create branch
BRANCH_NAME=${1:-$(generate_branch_name_from_primary_type "$MODE")}

# In git-flow mode, convert conventional types to feature/
if [ "$MODE" = "git-flow" ] && [[ "$BRANCH_NAME" =~ ^(feat|fix|docs|test|chore)/ ]]; then
  BRANCH_NAME="feature/${BRANCH_NAME#*/}"
fi

git checkout -b "$BRANCH_NAME" "$BASE_BRANCH"

# Step 4: Create logical commits (one per type)
commit_count=0
for type in "${!file_groups[@]}"; do
  files="${file_groups[$type]}"
  scope=$(detect_scope_from_files "$files")

  # Stage only files of this type
  git add $files

  # Generate message for this type
  message=$(generate_commit_message "$type" "$scope" "$files")

  # Create commit
  git commit -m "$message"
  ((commit_count++))

  echo "✅ $message ($(echo $files | wc -w) files)"
done

# Step 5: Push with tracking
total_files=$(git diff origin/$(git symbolic-ref --short HEAD) --name-only | wc -l)
git push -u origin "$BRANCH_NAME"
echo "✅ Pushed to origin/$BRANCH_NAME ($total_files files, $commit_count commits)"

# Step 6: Create PR with comprehensive error handling
# Check if branch exists on remote
if ! git ls-remote --exit-code --heads origin "$BRANCH_NAME" &> /dev/null; then
  echo "❌ Branch not found on remote: $BRANCH_NAME"
  exit 1
fi

# Check if PR already exists
if EXISTING_PR=$(gh pr list --head "$BRANCH_NAME" --json url --jq '.[0].url' 2>/dev/null); then
  if [ -n "$EXISTING_PR" ]; then
    echo "ℹ️  PR already exists: $EXISTING_PR"
    exit 0
  fi
fi

# Generate PR title and description
PR_TITLE=$(generate_pr_title_from_commits)
PR_BODY=$(generate_pr_body_from_commits)

# Attempt PR creation
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
  echo "✅ Branch pushed successfully: $BRANCH_NAME"
  echo "✅ Created $commit_count logical commits"
  exit 1
fi

echo "✅ PR created: $PR_URL"
```

## Type Detection Priority

Analyzes `git diff HEAD --name-status` to determine type (priority order):

1. **All documentation files** (`*.md`, `docs/**`, `README*`) → `docs:`
2. **All test files** (`*.test.*`, `*.spec.*`, `tests/**`, `__tests__/**`) → `test:`
3. **Dependency files** (`package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`) → `chore:`
4. **CI configuration** (`.github/**`, `.gitlab-ci.yml`, `.circleci/**`) → `ci:`
5. **Build configuration** (`webpack.config.js`, `tsconfig.json`, `Makefile`, `vite.config.*`) → `build:`
6. **New files added** (git status: A) → `feat:`
7. **Files with fix/bug keywords** (path contains "fix", "bug", "patch", "hotfix") → `fix:`
8. **Performance files** (path contains "perf", "optimize", "cache", "speed") → `perf:`
9. **Only formatting changes** (whitespace/semicolons, no logic) → `style:`
10. **Default for code modifications** → `refactor:`

**Scope Detection:** Extracts from consistent directory patterns (e.g., `src/api/` → `api`, `src/auth/` → `auth`)

## Examples

### Example 1: Multi-Type Changes (Auto-branch)

```bash
# Changes:
# - src/auth/*.ts (12 files)
# - docs/api.md (1 file)
# - tests/auth/*.test.ts (8 files)

/workflows:git

# Output:
✓ Checking GitHub CLI authentication...
✓ Analyzing 21 uncommitted files...
✓ Grouped into 3 logical commits

✅ Created branch: feat/authentication-system
✅ feat(auth): implement JWT authentication (12 files)
✅ docs: update API documentation (1 file)
✅ test: add authentication test coverage (8 files)
✅ Pushed to origin/feat/authentication-system (21 files, 3 commits)
✅ PR created: https://github.com/org/repo/pull/123
```

### Example 2: Single-Type Changes (Custom branch)

```bash
# Changes:
# - docs/*.md (5 files)

/workflows:git docs/improve-readme

# Output:
✓ Checking GitHub CLI authentication...
✓ Analyzing 5 uncommitted files...
✓ Grouped into 1 logical commit

✅ Created branch: docs/improve-readme
✅ docs: improve README and documentation (5 files)
✅ Pushed to origin/docs/improve-readme (5 files, 1 commit)
✅ PR created: https://github.com/org/repo/pull/124
```

### Example 3: PR Creation Failure

```bash
/workflows:git feature/payments

# Output:
✓ Checking GitHub CLI authentication...
✓ Analyzing 15 uncommitted files...
✓ Grouped into 2 logical commits

✅ Created branch: feature/payments
✅ feat(api): add payment endpoints (10 files)
✅ test: add payment integration tests (5 files)
✅ Pushed to origin/feature/payments (15 files, 2 commits)
❌ PR creation failed

Error: gh: authentication token expired

Possible causes:
1. GitHub CLI authentication expired - Run: gh auth login
2. Insufficient permissions - Check repository access
3. Branch protection rules require review

Manual PR creation:
  1. Visit: https://github.com/org/repo/compare/feature/payments
  2. Or run: gh pr create --web

✅ Branch pushed successfully: feature/payments
✅ Created 2 logical commits
```

## Integration Points

- **Replaces**: Sequential `/git-flow:feature` → `/git:commit` → `/git:push` → `/git:pr` workflow
- **Follows**: Code implementation, feature completion, bug fixes
- **Followed by**: Code review process, CI/CD pipeline
- **Related**: `/git-flow:feature`, `/git:commit`, `/git:push`, `/git:pr` (atomic commands)

## Quality Standards

- **Detects workflow mode automatically** - Identifies Git-Flow or Conventional mode
- **Git-Flow aware branching** - Creates feature/ branches from develop in git-flow mode
- **Git-Flow aware PR targeting** - Auto-targets develop for features in git-flow mode
- **Groups changes into logical commits** - One commit per conventional type (feat, fix, docs, test)
- **Validates GitHub CLI authentication** - Pre-flight check prevents silent failures
- **Comprehensive error handling** - Provides actionable error messages and manual instructions
- **Verifies branch on remote** - Ensures push succeeded before PR creation
- **Checks for existing PR** - Avoids duplicate PR creation
- **Uses conventional commit format** - All commits follow `<type>(<scope>): <description>`
- **Auto-detects types from files** - Analyzes file changes, not commit history
- **Maintains clean git history** - Logical commits enable easier code review and debugging
- **Returns PR URL immediately** - Provides direct link for team collaboration

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

### No Uncommitted Changes

```
❌ No uncommitted changes to commit
Run 'git status' to verify working tree
```

### Branch Already Exists

```
ℹ️  Branch 'feature/auth' already exists
Switching to existing branch...
```

### PR Already Exists

```
ℹ️  PR already exists: https://github.com/org/repo/pull/123
```

### Push Fails

```
❌ Push failed
Error: [git error message]
Check network connection and remote permissions
```

### PR Creation Fails

```
❌ PR creation failed
Error: [gh error message]

Possible causes:
1. GitHub CLI authentication expired
2. Insufficient permissions
3. Branch protection rules

Manual PR creation:
  1. Visit: https://github.com/org/repo/compare/branch-name
  2. Or run: gh pr create --web

✅ Branch pushed successfully: branch-name
✅ Created N logical commits
```

## Success Criteria

✅ Branch created or switched successfully
✅ Changes grouped into logical commits by type
✅ Each commit follows conventional format
✅ All commits pushed to remote with tracking
✅ PR created successfully OR detailed error with manual instructions
✅ PR URL returned for immediate access
✅ Clean git history with atomic commits

## Notes

- **Logical Commit Grouping**: Creates separate commits for feat/fix/docs/test/chore changes instead of monolithic commits
- **Pre-flight Checks**: Validates `gh` CLI installation and authentication before operations
- **Comprehensive Error Handling**: Provides actionable error messages and manual fallback instructions
- **Idempotent Branch Creation**: Safe to run multiple times, switches to existing branch if present
- **PR Duplicate Detection**: Checks for existing PR before attempting creation
- **Conventional Commit Compliance**: All operations follow conventional commit standards
- **Direct Git Operations**: This command is in `/git` category, authorized for git operations per repository constraint
