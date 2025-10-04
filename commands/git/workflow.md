---
description: "Complete Git workflow automation with intelligent branching and team coordination"
argument-hint: "[arguments]"
category: "git"
tools: ["Bash"]
complexity: "moderate"
allowed-tools: Bash
---

# Command: Workflow

## Purpose

Executes git operations for workflow functionality.

## Usage

```bash
/git:workflow $ARGUMENTS
```

**Arguments**:

- `$1` (workflow-type): Specific workflow to execute (optional)
- `$2` (--branch): Target branch for workflow (optional)
- `$3` (--push): Push changes after workflow completion (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "feature-branch --push"` - Complete feature workflow with push
- `$ARGUMENTS = "hotfix main"` - Hotfix workflow for main branch
- `$ARGUMENTS = "--branch=develop"` - Workflow targeting develop branch

## Process

1. Analyze the current state and requirements based on $ARGUMENTS
2. Execute the git workflow operation with specified parameters
3. Coordinate branch management, commits, and team workflows
4. Validate results and provide feedback
5. Update relevant documentation or state

## Agent Integration

- **Specialist Options**: implementation-strategy-specialist can be spawned for handling git operations and coordination

## Examples

```bash
