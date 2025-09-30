---
description: "Create and manage pull requests with GitHub CLI integration"
argument-hint: "[title]"
category: "git"
tools: ["Bash", "Read", "Grep"]
complexity: "moderate"
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

1. Parse $ARGUMENTS for title, draft status, and base branch
2. Analyze commit history and changes for PR description generation
3. Generate meaningful PR title and description from commit messages
4. Create pull request using GitHub CLI with proper formatting
5. Set appropriate labels, reviewers, and milestones if configured
6. Return PR URL for immediate access and review

## Agent Integration

- **Specialist Options**: implementation-strategy-specialist can be spawned for handling git operations and coordination

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

## Quality Standards

- Generates descriptive PR titles from commit analysis
- Creates comprehensive PR descriptions with change summary
- Includes test plan and verification steps when applicable
- Links related issues and references automatically
- Returns immediate PR URL for team collaboration
- Follows repository PR template when available
- Sets appropriate draft status for work-in-progress
