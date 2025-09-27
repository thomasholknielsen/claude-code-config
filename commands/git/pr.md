---
description: "Create and manage pull requests with GitHub CLI integration"
category: "git"
agent: "implementation-orchestrator"
tools: ["Bash", "Read", "Grep"]
complexity: "moderate"
---

# Command: Pr

## Purpose

Creates pull requests with auto-generated descriptions and returns the PR URL for immediate access.

## Usage

```bash
/git:pr [title]
```

**Arguments**: Optional PR title (auto-generated from commits if not provided)

## Process

1. Analyze commit history and changes for PR description generation
2. Generate meaningful PR title and description from commit messages
3. Create pull request using GitHub CLI with proper formatting
4. Set appropriate labels, reviewers, and milestones if configured
5. Return PR URL for immediate access and review

## Agent Integration

- **Primary Agent**: implementation-orchestrator - Handles git operations and coordination

## Examples

```bash
# Create PR with auto-generated title and description
/git:pr

# Create PR with custom title
/git:pr "Add user authentication system"

# Create draft PR for work in progress
/git:pr --draft "WIP: Refactor payment processing"
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
