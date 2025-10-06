---
description: "Create and manage pull requests with GitHub CLI integration"
argument-hint: "[title]"
allowed-tools: Bash, Read, Grep
---

# Command: Pr

## Purpose

Creates pull requests with auto-generated descriptions and returns the PR URL for immediate access.

## Usage

```bash
/git:pr $ARGUMENTS
```

**Arguments**:

- `$1` (title): PR title (optional, auto-generated from commits if not provided)
- `$2` (--draft): Create as draft PR (optional)
- `$3` (--base): Base branch for PR (optional, defaults to main)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "Add user authentication system"` - PR with custom title
- `$ARGUMENTS = "--draft"` - Create draft PR with auto-generated title
- `$ARGUMENTS = "Fix login bug --base=develop"` - PR targeting develop branch

## Process

1. **Analyze branch file changes for PR context:**
   - Run `git diff origin/<base>...HEAD --name-status` to see all changes in branch
   - Analyze file changes between base and current branch
   - Determine primary type from uncommitted file analysis (not commits)
   - Extract scope from consistent file paths across branch
   - Never rely on commit messages for type detection
2. **Parse or generate PR title:**
   - If title provided: Extract type, validate, format to Title Case
   - If no title: Auto-generate from branch file changes
   - Format: `<type>: <Title Case Description>`
   - Or with scope: `<type>(<scope>): <Title Case Description>`
   - Validate type is conventional: feat, fix, docs, style, refactor, test, chore, perf, ci, build
3. **Generate PR description:**
   - Summary of file changes (not commit messages)
   - List modified files grouped by type
   - Include test files modified
   - Add conventional type badges
   - Include breaking changes if detected
4. Create pull request using GitHub CLI with formatted title and description
5. Set appropriate labels, reviewers, and milestones if configured
6. Return PR URL for immediate access and review

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned for handling git operations and coordination

## Examples

```bash
# Create PR with auto-generated title and description
/git:pr

# Create PR with custom title
/git:pr $ARGUMENTS
# where $ARGUMENTS = "Add user authentication system"

# Create draft PR for work in progress
/git:pr $ARGUMENTS
# where $ARGUMENTS = "--draft \"WIP: Refactor payment processing\""
```

## Output

- Created PR URL for immediate access
- PR title and description summary
- Assigned reviewers and labels (if configured)
- Next steps for the review process

## Integration Points

- **Follows**: /git:push, development completion
- **Followed by**: Code review process, CI/CD pipeline
- **Related**: /git:branch, /git:commit, /workflows:run-git-branch-commit-and-pr

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

## Quality Standards

- **Enforces conventional PR titles** - Uses type prefixes matching commit conventions
- **Auto-detects type from branch file changes** - Analyzes file diffs, not commit messages
- **Formats titles in Title Case** - Converts descriptions to proper case
- Generates descriptive PR titles from file analysis
- Creates comprehensive PR descriptions with change summary
- Includes test plan and verification steps when applicable
- Links related issues and references automatically
- Returns immediate PR URL for team collaboration
- Follows repository PR template when available
- Sets appropriate draft status for work-in-progress
- Groups file changes by conventional type in description
