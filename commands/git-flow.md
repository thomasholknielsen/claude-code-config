---
description: Streamlined git workflows with intelligent automation
category: git
tools: Bash
---

# Streamlined Git Operations

I'll handle common git workflows efficiently with intelligent automation.

Arguments: `$ARGUMENTS` - operation type or branch/commit details

## Core Operations

**Branch Management:**
- Create and switch to feature branches
- Clean merge and delete completed branches  
- Handle merge conflicts with context
- Sync with remote branches safely

**Commit Workflow:**
- Smart staging of related changes
- Conventional commit message generation
- Batch commits for logical units
- Amend and fixup commit support

**Pull Request Flow:**
- Create PRs with generated descriptions
- Link to issues and reference tickets
- Add appropriate reviewers based on changes
- Update PR status and handle feedback

## Quick Commands

```
/git-flow branch "feature-name"     # Create and switch to feature branch
/git-flow commit "description"      # Smart commit with message
/git-flow pr "title"               # Create PR with description
/git-flow sync                     # Sync with main branch
/git-flow clean                    # Clean merged branches
```

## Intelligent Features

**Context-aware operations:**
- Detect which files to stage based on changes
- Generate commit messages from change patterns
- Suggest appropriate PR reviewers
- Auto-link related issues and tickets

**Safety measures:**
- Backup before destructive operations
- Validate branch state before merging
- Check for conflicts and provide resolution
- Confirm before force operations

Streamlined git workflows without compromising safety or best practices.