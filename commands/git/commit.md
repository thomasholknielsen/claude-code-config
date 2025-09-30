---
description: "Smart commit message generation with quality checks"
argument-hint: "[message]"
category: "git"
tools: ["Bash", "Read", "Grep"]
complexity: "moderate"
---

# Command: Commit

## Purpose

Creates logical, atomic commits with intelligent message generation and quality validation.

## Usage

```bash
/git:commit $ARGUMENTS
```

**Arguments**:

- `$1` (message): Commit message (optional, auto-generated from changes if not provided)
- `$2` (--batch): Create multiple logical commits (optional)
- `$3` (--amend): Amend the last commit (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "feat: add user authentication system"` - Single commit with message
- `$ARGUMENTS = "--batch"` - Multiple logical commits
- `$ARGUMENTS = "Fix typo --amend"` - Amend last commit

## Process


1. **Pre-Commit Linting**: Run `/workflows:lint-and-correct-all` to ensure code quality
   - Auto-fix linting errors across all languages
   - Stage auto-fixed files automatically
   - Report any unfixable issues requiring manual intervention
   - Abort commit if critical linting errors remain
2. Parse $ARGUMENTS for commit message and options
3. Analyze staged and unstaged changes for logical groupings
4. Generate meaningful commit messages based on file modifications
5. Create atomic commits for each logical unit of work
6. Validate commit quality and message clarity
7. Report commit summary and next steps

## Agent Integration

- **Specialist Options**: implementation-strategy-specialist can be spawned for handling git operations and coordination

## Examples

```bash
# Automatic commit with generated messages
/git:commit

# Single commit with custom message
/git:commit $ARGUMENTS
# where $ARGUMENTS = "feat: add user authentication system"

# Batch commits with logical grouping
/git:commit $ARGUMENTS
# where $ARGUMENTS = "--batch"
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

- **Runs automated linting and fixes before commit** - Ensures code style consistency
- **Aborts commit if critical linting errors remain** - Maintains code quality gate
- Creates atomic commits focused on single functionality
- Generates clear, descriptive commit messages following conventions
- Groups related changes logically (features, fixes, refactoring)
- Validates no breaking changes are mixed with features
- Ensures commit messages are under 72 characters for subject line
- Follows semantic commit format when appropriate (feat:, fix:, docs:)
- **Stages auto-fixed files automatically** - Includes linting fixes in commit
