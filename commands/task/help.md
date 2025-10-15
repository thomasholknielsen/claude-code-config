---
description: "Guide to using the unified task management system"
argument-hint: ""
allowed-tools: Read, mcp__sequential-thinking__sequentialthinking
---

# Command: Task Help

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Provide comprehensive task management guidance covering three origins (adhoc/code-comment/github-issue), five core commands (/task:add, /task:scan-project, /task:execute, /task:archive, /task:help), three GitHub integration commands, quick start scenarios (capture/discovery/work), workflow patterns (daily/sprint/tech-debt), best practices, command reference tables

**P**urpose: Enable users to understand unified task system through clear documentation, reduce learning curve via scenario-based examples, support multiple workflows (adhoc capture, code scanning, GitHub integration), provide quick reference for command syntax, clarify GitHub sync behavior (manual, not automatic)

**E**xpectation: Comprehensive guide with three-origin explanation, command reference tables, quick start scenarios, workflow examples (daily/sprint/tech-debt), GitHub integration patterns (read-only/import/export), FAQ section, storage locations, best practices, getting started steps

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% feature coverage, Accuracy >90% command syntax, Relevance >85% scenario examples, Efficiency <30s quick reference scan)

## Explicit Constraints

**IN SCOPE**: Documentation (system overview, command reference, workflow examples), quick start scenarios (adhoc/code-comment/github-issue), GitHub integration patterns (three patterns: read-only, import, export), FAQ section, best practices
**OUT OF SCOPE**: Command implementation details, system troubleshooting, migration from old systems (separate guide), advanced customization, performance tuning

## Purpose

Provides comprehensive guidance on using the unified task management system for capturing, organizing, and tracking work items from multiple sources.

## Usage

```bash
/task:help
```

## Task Management System Overview

The task management system provides a unified way to capture, organize, and track all work items regardless of their origin.

### Three Task Origins

Every task has an **origin** that indicates where it came from:

1. **adhoc** - Tasks you create manually during work
2. **code-comment** - Tasks extracted from TODO/FIXME/HACK/BUG comments in code
3. **github-issue** - Tasks imported from GitHub issues

### Core Commands

```bash
# 📝 Capture & Discovery
/task:add "description" [--priority] [--category]     # Add adhoc task
/task:scan-project [scope] [--types] [--consolidate]         # Find code comments

# 📋 Organization & Management
/task:execute                                        # Interactive triaging
/task:execute TASK-001 [TASK-002 ...]              # Work on specific tasks
/task:execute TASK-001 [--notes] [--complete]      # Update task progress
/task:archive [--completed-before]                    # Archive completed tasks

# 🐙 GitHub Integration
/github:fetch-issues [--filter] [--milestone]                # Fetch issues to context
/github:convert-issues-to-tasks [--filter] [--source-file]             # Convert issues to tasks
/github:create-issue-from-task TASK-001 [--labels]                    # Create issue from task
```

## Quick Start Guide

### Scenario 1: Capture Adhoc Tasks During Work

```bash
# Found a bug while working
/task:add "Fix login validation error" --priority=high --category=bug

# Idea for new feature
/task:add "Add dark mode toggle" --category=feature

# Technical debt to address later
/task:add "Refactor authentication module" --priority=medium --category=refactor
```

**Result**: Tasks saved to `.agent/tasks.md` with origin `adhoc`

---

### Scenario 2: Discover Technical Debt in Code

```bash
# Scan codebase for TODO/FIXME comments
/task:scan-project src/ --types=TODO,FIXME

# Review findings, then consolidate to tasks
/task:scan-project src/ --types=TODO,FIXME --consolidate

# Now they're tracked in .agent/tasks.md with origin `code-comment`
```

**Result**: Code comments converted to tasks with source file locations

---

### Scenario 3: Work on GitHub Issues

```bash
# Fetch your assigned issues (saved to .agent/github-issues.md)
/github:fetch-issues --filter=assigned

# Review issues, then import specific ones to tasks
/github:convert-issues-to-tasks --filter="milestone:v2.0 AND label:bug"

# Or import from the fetched file
/github:convert-issues-to-tasks --source-file=.agent/github-issues.md

# Now work on tasks locally, create issues when ready
/github:create-issue-from-task TASK-005 --labels=bug,urgent
```

**Result**: GitHub issues available for reference, imported ones become tasks

---

## Task File Structure

### Location: `.agent/tasks.md`

All tasks are stored in a single file with this structure:

```markdown
## [TASK-001] Fix login validation error

**Status**: pending
**Priority**: high
**Category**: bug
**Origin**: adhoc
**Created**: 2025-10-13T10:30:00Z

**Description**:
Add validation for special characters in username field.

---

## [TASK-002] Refactor user service (TODO)

**Status**: pending
**Priority**: medium
**Category**: refactor
**Origin**: code-comment
**Source Location**: src/services/user.ts:89
**Created**: 2025-10-13T11:00:00Z

**Description**:
Extract authentication logic into separate service.

**Code Context**:
```typescript
// TODO: Refactor - extract auth logic
export class UserService {
  async login(credentials) { ... }
}
```

---

## [TASK-003] Database connection leak (#125)

**Status**: in-progress
**Priority**: critical
**Category**: bug
**Origin**: github-issue
**GitHub Issue**: <https://github.com/org/repo/issues/125>
**Created**: 2025-10-13T12:00:00Z

**Description**:
Connection pool not releasing connections properly under high load.

---

```

### Task Metadata

- **Status**: `pending | in-progress | completed | blocked`
- **Priority**: `low | medium | high | critical`
- **Category**: `bug | feature | refactor | docs | test | research | chore`
- **Origin**: `adhoc | code-comment | github-issue`

---

## Typical Workflows

### Daily Development Workflow

```bash
# Morning: Check what's on your plate
/task:execute --status=pending,in-progress

# Start working on a task
/task:execute TASK-001 --status=in-progress

# Discover new work while coding
/task:add "Add error handling for API timeout"
/task:scan-project src/api/ --consolidate

# End of day: Archive completed work
/task:archive
```

---

### Sprint Planning Workflow

```bash
# Fetch GitHub issues for upcoming sprint
/github:fetch-issues --milestone=v2.0

# Review and import prioritized issues
/github:convert-issues-to-tasks --filter="milestone:v2.0 AND priority:high"

# List all tasks for sprint
/task:execute --priority=high,critical

# Break down complex tasks (add subtasks as new tasks)
/task:add "Design OAuth integration UI" --category=feature
/task:add "Implement OAuth backend" --category=feature
```

---

### Technical Debt Cleanup Workflow

```bash
# Find all technical debt markers
/task:scan-project --types=TODO,FIXME,HACK --consolidate

# List code-comment tasks
/task:execute --origin=code-comment

# Work through them systematically
/task:execute TASK-010 --status=in-progress
# ... implement fix ...
/task:execute TASK-010 --status=completed

# Create GitHub issues for remaining items
/github:create-issue-from-task --origin=code-comment --labels=tech-debt
```

---

## GitHub Integration Patterns

### Pattern 1: Issues → Session Context (Read-Only)

```bash
# Fetch issues for reference during work
/github:fetch-issues --filter=assigned

# Issues saved to .agent/github-issues.md
# Available for reference, not tracked as tasks
```

**Use when**: You want issue context without committing to work on them yet

---

### Pattern 2: Issues → Tasks (Import for Work)

```bash
# Fetch and review
/github:fetch-issues --milestone=v2.0

# Import specific ones as tasks
/github:convert-issues-to-tasks --filter="label:bug AND milestone:v2.0"

# Now they're in .agent/tasks.md with origin: github-issue
# Work on them locally, status stays separate from GitHub
```

**Use when**: You've decided to work on specific issues this session

---

### Pattern 3: Tasks → Issues (Export Work)

```bash
# Created local tasks during work
/task:add "Discovered critical security issue"

# Ready to share with team
/github:create-issue-from-task TASK-001 --labels=security,critical

# Task updated with GitHub issue link
```

**Use when**: Local work needs team visibility or discussion

---

## Best Practices

### 1. **Capture Immediately**

Don't wait - capture tasks as soon as you think of them:

```bash
/task:add "Idea: Add user preference for theme"
```

### 2. **Origin-Specific Workflows**

- **adhoc**: Quick capture, refine later
- **code-comment**: Review before converting, add context
- **github-issue**: Import selectively, don't sync everything

### 3. **Regular Cleanup**

```bash
# Weekly: Archive completed tasks
/task:archive --completed-before=7d

# Monthly: Convert stale tasks to GitHub issues or delete
/task:execute --status=pending --created-before=30d
```

### 4. **Meaningful Descriptions**

Good: "Fix validation error in login form for special characters"
Bad: "Fix login"

### 5. **Use Categories and Priorities**

Helps with filtering and planning:

```bash
/task:execute --category=bug --priority=high
/task:execute --category=feature --status=pending
```

### 6. **GitHub Sync is Manual**

Task status does NOT automatically sync to GitHub. This is intentional:

- Work on tasks locally
- Update GitHub when reaching milestones
- Use `/github:create-issue-from-task` to share specific tasks

---

## Command Reference

### Task Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `/task:add` | Create adhoc task | `/task:add "Fix bug" --priority=high` |
| `/task:scan-project` | Find code comments | `/task:scan-project src/ --consolidate` |
| `/task:execute` | Triage/work on tasks | `/task:execute` (interactive) or `/task:execute TASK-001` |
| `/task:archive` | Archive completed | `/task:archive` |
| `/task:help` | This guide | `/task:help` |

### GitHub Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `/github:fetch-issues` | Fetch issues to context | `/github:fetch-issues --filter=assigned` |
| `/github:convert-issues-to-tasks` | Convert issues to tasks | `/github:convert-issues-to-tasks --filter="milestone:v2.0"` |
| `/github:create-issue-from-task` | Create issue from task | `/github:create-issue-from-task TASK-001 --labels=bug` |

---

## Storage Locations

```
.agent/
├── tasks.md              # All active tasks
├── tasks-archive.md      # Archived completed tasks
└── github-issues.md      # Fetched GitHub issues (reference only)
```

---

## FAQ

**Q: When should I use `/github:fetch-issues` vs `/github:convert-issues-to-tasks`?**

A: Use `/github:fetch-issues` to pull issues into session context for reference. Use `/github:convert-issues-to-tasks` when you've decided to work on specific issues and want them as trackable tasks.

---

**Q: Do task status updates sync to GitHub automatically?**

A: No. This is intentional. Update tasks locally, then manually use `/github:create-issue-from-task` or update GitHub directly when appropriate.

---

**Q: What happens to code comments after I convert them to tasks?**

A: The comments remain in your code. You can remove them manually or create a PR to replace them with task/issue references.

---

**Q: Can I have tasks without GitHub issues?**

A: Absolutely! Most tasks will be adhoc or code-comment origin. GitHub integration is optional for team collaboration.

---

**Q: How do I handle subtasks?**

A: Create separate tasks with descriptive names. Use task descriptions to link related tasks:

```bash
/task:add "OAuth integration - UI design" --category=feature
/task:add "OAuth integration - Backend implementation" --category=feature
/task:add "OAuth integration - Testing" --category=test
```

---

## Getting Started

1. **Capture your first task**:

   ```bash
   /task:add "Learn task management system"
   ```

2. **Find some technical debt**:

   ```bash
   /task:scan-project src/ --types=TODO --consolidate
   ```

3. **List what you've got**:

   ```bash
   /task:execute
   ```

4. **Start working**:

   ```bash
   /task:execute TASK-001 --status=in-progress
   ```

That's it! You're using the unified task management system.

## Related Documentation

- [Task Management Migration Guide](../../docs/user/task-management-migration.md) - Migrating from old commands
- [User Guide](../../docs/user/user-guide.md) - Complete system documentation
- [CLAUDE.md](../../CLAUDE.md) - Task management patterns and constraints
