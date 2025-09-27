---
description: "Smart commit message generation with quality checks"
category: "git"
agent: "implementation-orchestrator"
tools: ["Bash", "Read", "Grep"]
complexity: "moderate"
---

# Command: Commit

## Purpose

Creates logical, atomic commits with intelligent message generation and quality validation.

## Usage

```bash
/git:commit [message]
```

**Arguments**: Optional commit message (auto-generated from changes if not provided)

## Process

1. Analyze staged and unstaged changes for logical groupings
2. Generate meaningful commit messages based on file modifications
3. Create atomic commits for each logical unit of work
4. Validate commit quality and message clarity
5. Report commit summary and next steps

## Agent Integration

- **Primary Agent**: implementation-orchestrator - Handles git operations and coordination

## Examples

```bash
# Automatic commit with generated messages
/git:commit

# Single commit with custom message
/git:commit "feat: add user authentication system"

# Batch commits with logical grouping
/git:commit --batch
```

## Output

- Generated commit messages for each logical unit
- Commit hashes and summaries
- Files included in each commit
- Guidance on next steps (push, PR creation, etc.)

## Integration Points

- **Follows**: /git:branch, code modifications
- **Followed by**: /git:push, /git:pr
- **Related**: /workflows:run-git-branch-commit-and-pr

## Quality Standards

- Creates atomic commits focused on single functionality
- Generates clear, descriptive commit messages following conventions
- Groups related changes logically (features, fixes, refactoring)
- Validates no breaking changes are mixed with features
- Ensures commit messages are under 72 characters for subject line
- Follows semantic commit format when appropriate (feat:, fix:, docs:)