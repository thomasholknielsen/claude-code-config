---
description: "Automated workflow that creates branch, commits changes, pushes, and creates PR with URL"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand", "Bash", "TodoWrite"]
complexity: "complex"
---

# Command: Run Git Branch Commit And PR

## Purpose

Automates the complete git workflow from current changes to pull request creation with automatic branch, commit, push, and PR generation.

## Usage

```bash
/workflows:run-git-branch-commit-and-pr [branch-name]
```

**Arguments**: Optional branch name (auto-generated if not provided)

## Process

1. Validate current state using git status checks
2. Execute `/git:branch [branch-name]` to create feature branch
3. Execute `/git:commit` to create logical, atomic commits
4. Execute `/git:push` to push branch with tracking setup
5. Execute `/git:pr` to create pull request with auto-generated description
6. Return PR URL for immediate access and team collaboration

## Agent Integration

- **Primary Agent**: task-orchestrator - Coordinates entire git automation workflow
- **Git Commands**: Uses SlashCommand tool to execute `/git:branch`, `/git:commit`, `/git:push`, `/git:pr`
- **Delegation**: All git operations delegated to atomic git commands via SlashCommand

## Examples

```bash
# Automatic workflow with generated branch name
/workflows:run-git-branch-commit-and-pr

# Specify custom branch name
/workflows:run-git-branch-commit-and-pr "feature/user-authentication"

# Quick automation for hotfix
/workflows:run-git-branch-commit-and-pr "hotfix/login-bug"
```

## Output

- Created branch name and commit summary
- Generated commit messages for each logical unit
- Push confirmation with remote tracking
- Pull request URL for immediate review
- Summary of all automated steps completed

## Integration Points

- **Follows**: Code changes, feature development, bug fixes
- **Followed by**: Code review process, CI/CD pipeline
- **Related**: /git:branch, /git:commit, /git:push, /git:pr

## Quality Standards

- Uses existing atomic git commands for all git operations
- Maintains git operation constraints through SlashCommand delegation
- Orchestrates sequential workflow: branch → commit → push → PR
- Provides comprehensive error handling and rollback via atomic commands
- Returns immediate PR URL through `/git:pr` command output
- Respects Agent Orchestra framework git constraints
