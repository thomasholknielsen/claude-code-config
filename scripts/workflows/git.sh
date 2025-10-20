#!/bin/bash

# Workflow: Git
# Purpose: Complete git workflow with intelligent commit grouping
# Creates branch, groups changes into logical commits by type, pushes, and creates PR

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Utility functions
log_error() {
  echo -e "${RED}❌ $1${NC}"
}

log_success() {
  echo -e "${GREEN}✅ $1${NC}"
}

log_info() {
  echo -e "${BLUE}ℹ️  $1${NC}"
}

log_progress() {
  echo -e "${BLUE}✓ $1${NC}"
}

# Detect conventional commit type from file path
detect_type_from_file() {
  local file="$1"

  # Documentation files
  if [[ "$file" =~ \.(md|txt)$ ]] || [[ "$file" =~ ^docs/ ]] || [[ "$file" =~ ^README ]]; then
    echo "docs"
    return
  fi

  # Test files
  if [[ "$file" =~ \.(test|spec)\. ]] || [[ "$file" =~ ^(tests|__tests__)/ ]]; then
    echo "test"
    return
  fi

  # Dependency files
  if [[ "$file" =~ ^(package\.json|yarn\.lock|requirements\.txt|Cargo\.toml|go\.mod|Gemfile|composer\.json)$ ]]; then
    echo "chore"
    return
  fi

  # CI configuration
  if [[ "$file" =~ ^\.github/ ]] || [[ "$file" =~ ^\.gitlab-ci || "$file" =~ ^\.circleci/ ]]; then
    echo "ci"
    return
  fi

  # Build configuration
  if [[ "$file" =~ (webpack|vite|tsconfig|Makefile|build)\.* ]] || [[ "$file" =~ ^(build|dist)/ ]]; then
    echo "build"
    return
  fi

  # Performance files
  if [[ "$file" =~ (perf|optimize|cache|speed) ]]; then
    echo "perf"
    return
  fi

  # Fix/bug keywords
  if [[ "$file" =~ (fix|bug|patch|hotfix) ]]; then
    echo "fix"
    return
  fi

  # Default: refactor for code changes
  echo "refactor"
}

# Detect scope from file paths
detect_scope_from_files() {
  local files="$1"
  local scope=""

  # Try to extract common directory pattern
  for file in $files; do
    if [[ "$file" =~ ^src/([^/]+)/ ]]; then
      scope="${BASH_REMATCH[1]}"
      break
    elif [[ "$file" =~ ^([^/]+)/ ]]; then
      scope="${BASH_REMATCH[1]}"
      # Skip common non-scope directories
      if [[ ! "$scope" =~ ^(\.|__pycache__|node_modules|\.git)$ ]]; then
        break
      fi
    fi
  done

  echo "$scope"
}

# Generate commit message
generate_commit_message() {
  local type="$1"
  local scope="$2"
  local file_count="$3"

  if [ -n "$scope" ] && [ "$scope" != "." ]; then
    echo "${type}(${scope}): apply ${type} changes ($file_count files)"
  else
    echo "${type}: apply changes ($file_count files)"
  fi
}

# Generate PR title from commits
generate_pr_title() {
  local primary_type="$1"
  local scope="$2"

  case "$primary_type" in
    feat) echo "feat: Add new functionality" ;;
    fix) echo "fix: Resolve issues" ;;
    docs) echo "docs: Update documentation" ;;
    test) echo "test: Add test coverage" ;;
    perf) echo "perf: Improve performance" ;;
    refactor) echo "refactor: Code improvements" ;;
    chore) echo "chore: Update dependencies and configuration" ;;
    ci) echo "ci: Update CI/CD configuration" ;;
    build) echo "build: Update build configuration" ;;
    *) echo "chore: Various changes" ;;
  esac
}

# ============================================================================
# STEP 1: Pre-flight Validation
# ============================================================================

log_progress "Checking GitHub CLI installation..."
if ! command -v gh &> /dev/null; then
  log_error "GitHub CLI (gh) not installed"
  echo "Install: https://cli.github.com/"
  exit 1
fi

log_progress "Checking GitHub CLI authentication..."
if ! gh auth status &> /dev/null; then
  log_error "GitHub CLI not authenticated"
  echo "Run: gh auth login"
  exit 1
fi

log_progress "Verifying git repository..."
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  log_error "Not a git repository"
  exit 1
fi

# Check for uncommitted changes
if git diff --quiet && git diff --cached --quiet; then
  log_error "No uncommitted changes to commit"
  echo "Run 'git status' to verify working tree"
  exit 1
fi

log_success "Pre-flight checks passed"

# ============================================================================
# STEP 2: Detect Workflow Mode
# ============================================================================

log_progress "Detecting workflow mode..."

if git branch -a 2>/dev/null | grep -q "develop" && git branch -a | grep -q "main"; then
  MODE="git-flow"
  BASE_BRANCH="develop"
  log_success "Git-Flow mode detected (develop + main)"
else
  MODE="conventional"
  BASE_BRANCH="$(git symbolic-ref --short HEAD)"
  log_success "Conventional mode (single main branch)"
fi

# ============================================================================
# STEP 3: Analyze and Group Changes
# ============================================================================

log_progress "Analyzing uncommitted changes..."

declare -A file_groups
declare -A type_counts
declare -A seen_files
primary_type=""
primary_count=0

# Get all uncommitted files (both staged and unstaged), deduplicated
while IFS= read -r file; do
  # Skip if already seen
  if [ -n "${seen_files[$file]}" ]; then
    continue
  fi
  seen_files[$file]=1

  type=$(detect_type_from_file "$file")

  # Track file count per type
  if [ -z "${type_counts[$type]}" ]; then
    type_counts[$type]=1
  else
    ((type_counts[$type]++))
  fi

  # Track primary type (most common)
  count=${type_counts[$type]}
  if [ "$count" -gt "$primary_count" ]; then
    primary_count=$count
    primary_type=$type
  fi

  # Group files
  if [ -z "${file_groups[$type]}" ]; then
    file_groups[$type]="$file"
  else
    file_groups[$type]+=" $file"
  fi
done < <(
  # Get both unstaged and staged changes, in one stream
  git diff HEAD --name-only 2>/dev/null
  git diff --cached --name-only 2>/dev/null
)

log_success "Grouped changes into ${#file_groups[@]} types"

# ============================================================================
# STEP 4: Create Branch
# ============================================================================

BRANCH_NAME="${1:-}"

if [ -z "$BRANCH_NAME" ]; then
  # Auto-generate from primary type
  if [ "$MODE" = "git-flow" ]; then
    # Git-Flow: feature/<description>
    BRANCH_NAME="feature/${primary_type}-changes"
  else
    # Conventional: <type>/<description>
    BRANCH_NAME="${primary_type}/update"
  fi
fi

# In git-flow mode, convert conventional types to feature/
if [ "$MODE" = "git-flow" ] && [[ "$BRANCH_NAME" =~ ^(feat|fix|docs|test|chore|perf)/ ]]; then
  BRANCH_NAME="feature/${BRANCH_NAME#*/}"
fi

log_progress "Creating branch: $BRANCH_NAME (from $BASE_BRANCH)..."

# Check if branch already exists
if git rev-parse --verify "$BRANCH_NAME" &> /dev/null; then
  log_info "Branch '$BRANCH_NAME' already exists, switching to it..."
  git checkout "$BRANCH_NAME"
else
  if [ "$BASE_BRANCH" = "develop" ] || [ "$BASE_BRANCH" = "main" ]; then
    git checkout -b "$BRANCH_NAME" "$BASE_BRANCH"
  else
    # For conventional mode, branch from current branch
    git checkout -b "$BRANCH_NAME"
  fi
fi

log_success "Created/switched to branch: $BRANCH_NAME"

# ============================================================================
# STEP 5: Create Logical Commits (one per type)
# ============================================================================

log_progress "Creating logical commits..."

commit_count=0
declare -a commit_messages

for type in $(printf '%s\n' "${!file_groups[@]}" | sort); do
  files="${file_groups[$type]}"
  file_count=$(echo "$files" | wc -w)

  scope=$(detect_scope_from_files "$files")
  message=$(generate_commit_message "$type" "$scope" "$file_count")

  # Stage only files of this type
  # shellcheck disable=SC2086
  git add $files

  # Create commit
  git commit -m "$message" > /dev/null 2>&1
  commit_messages+=("$message")
  ((commit_count++))

  log_success "$message"
done

# ============================================================================
# STEP 6: Push with Tracking
# ============================================================================

log_progress "Pushing to remote..."

if git push -u origin "$BRANCH_NAME" > /dev/null 2>&1; then
  total_files=$(git diff "origin/$BRANCH_NAME"...HEAD --name-only 2>/dev/null | wc -l)
  log_success "Pushed to origin/$BRANCH_NAME ($total_files files, $commit_count commits)"
else
  log_error "Failed to push to remote"
  echo "Check network connection and remote permissions"
  exit 1
fi

# ============================================================================
# STEP 7: Create PR with Error Handling
# ============================================================================

log_progress "Creating pull request..."

# Determine PR base branch
PR_BASE="main"
if [ "$MODE" = "git-flow" ]; then
  if [[ "$BRANCH_NAME" =~ ^feature/ ]]; then
    PR_BASE="develop"
  else
    PR_BASE="main"
  fi
fi

# Check if branch exists on remote
if ! git ls-remote --exit-code --heads origin "$BRANCH_NAME" &> /dev/null; then
  log_error "Branch not found on remote: $BRANCH_NAME"
  exit 1
fi

# Check if PR already exists
EXISTING_PR=$(gh pr list --head "$BRANCH_NAME" --json url --jq '.[0].url' 2>/dev/null || echo "")

if [ -n "$EXISTING_PR" ]; then
  log_info "PR already exists: $EXISTING_PR"
  exit 0
fi

# Generate PR title and body
PR_TITLE=$(generate_pr_title "$primary_type" "")
PR_BODY=$(printf "## Changes\n\n")
for msg in "${commit_messages[@]}"; do
  PR_BODY+="- $msg"$'\n'
done
PR_BODY+=$'\n'"## Commits\n\n"
while read -r line; do
  PR_BODY+="- $line"$'\n'
done < <(git log --oneline "origin/${PR_BASE}...${BRANCH_NAME}")

# Attempt PR creation
if PR_URL=$(gh pr create --title "$PR_TITLE" --body "$PR_BODY" --base "$PR_BASE" 2>&1); then
  log_success "PR created: $PR_URL"
  exit 0
else
  log_error "PR creation failed"
  echo ""
  echo "Error: $PR_URL"
  echo ""
  echo "Possible causes:"
  echo "1. GitHub CLI authentication expired - Run: gh auth login"
  echo "2. Insufficient permissions - Check repository access"
  echo "3. Branch protection rules require review"
  echo ""
  echo "Manual PR creation:"
  REPO=$(git config --get remote.origin.url | sed 's/.*://;s/.git$//')
  echo "  1. Visit: https://github.com/$REPO/compare/$PR_BASE...$BRANCH_NAME"
  echo "  2. Or run: gh pr create --web"
  echo ""
  log_success "Branch pushed successfully: $BRANCH_NAME"
  log_success "Created $commit_count logical commits"
  exit 1
fi
