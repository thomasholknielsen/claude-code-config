# Active Tasks

## [TASK-001] Ensure all configured MCP servers are integrated into the repository

**Status**: pending
**Priority**: medium
**Category**: chore
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Ensure all configured mcpservers{} are integrated into the repos, meaning that relevant commands and subagents and templates are "aware" of all mcps

---

## [TASK-002] Review current workflow commands for comprehensive pre-commit review capability

**Status**: pending
**Priority**: high
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Review current workflow commands for coverage of this already - we need one command to launch a comprehensive review of either the entire repos or the uncommitted changes. The objective is to provide a list of critical issues and discrepancies that we should consider fixing before committing - similar to a PR review.

---

## [TASK-003] Critical review of command template(s) - consider consolidation

**Status**: pending
**Priority**: high
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Critical review of command template(s) perhaps consolidate into one?

---

## [TASK-004] Critical review of mermaid template

**Status**: pending
**Priority**: medium
**Category**: chore
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Critical review of mermaid template

---

## [TASK-005] Align agents with template

**Status**: pending
**Priority**: medium
**Category**: chore
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Align agents with template

---

## [TASK-006] Align mermaid with template

**Status**: pending
**Priority**: medium
**Category**: chore
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Align mermaid with template

---

## [TASK-007] Align commands with template, except speckit

**Status**: pending
**Priority**: medium
**Category**: chore
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Align commands with template, except speckit

---

## [TASK-008] /workflow:docs starts work without confirmation - should perform detailed analysis and suggest actions

**Status**: pending
**Priority**: high
**Category**: bug
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
/workflow:docs starts work without confirmation - it should perform a detailed analysis and suggest actions

---

## [TASK-009] When adding tasks - automatically create enhanced prompt and relate to tasks in task.md

**Status**: pending
**Priority**: medium
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
When adding tasks - automatically create enhanced prompt and relate to tasks in task.md

---

## [TASK-010] Evaluate speckit:implement command's use of subagents - determine if enhancement needed

**Status**: pending
**Priority**: medium
**Category**: research
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
The speckit functions are great and should be changed as little as possible. Some changes have already been applied through speckit:apply-user-settings-fix command. But we should also evaluate if the speckit:implement command makes use of the subagents - does it already do this or should we imply this more directly through the users claude.md file?

---

## [TASK-011] Subagents/commands that depend on MCP tools should handle missing/failing MCP gracefully

**Status**: pending
**Priority**: high
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Subagents/commands that depend on mcp tools should be able to handle missing/failing mcp gracefully

---

## [TASK-012] Review commands template from UX perspective and integrate template changes onto existing commands

**Status**: pending
**Priority**: medium
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Review the commands template from a UX perspective and integrate any template changes onto existing commands

---

## [TASK-013] Apply reasoning for complex tasks - think deeply and sequentially - add to user CLAUDE.md and repo copy

**Status**: pending
**Priority**: medium
**Category**: docs
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Apply reasoning for complex tasks think deeply and sequentially - add this to user claude.md and repos copy

---

## [TASK-014] Review argument hints for commands and include marker for defaults

**Status**: pending
**Priority**: medium
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Review argument hints for commands + include marker for defaults

---

## [TASK-015] Use speckit to refactor context management file structure for session and task organization

**Status**: in-progress
**Priority**: high
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Use speckit to refactor the context management file structure to enable session work as well as task work. Proposed structure:

```
.agent/
 - tasks.md (list of all tasks)
 - Session-YYYY-MM-DD-{id}/
    - Task-XXX--{TaskTitle}/ (files and context related to tasks)
        - enhanced-prompt
        - analyst-x.md
        - analyst-y.md
        - save-to-markdown.md
    - context/ (unrelated to a task)
        - enhanced-prompt
        - analyst-x.md
        - analyst-y.md
        - save-to-markdown.md
```

On session end, prompt to delete .agent dir.

---

## [TASK-016] Ensure /git:commit and workflows handle pre-commit hook failures with auto-fix and recommit

**Status**: pending
**Priority**: high
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Ensure that when /git:commit tries to commit and precommit hooks fail, then it should resolve these errors, stage the changes again and recommit. This is also true for other workflows that perform commits. Also ensure that every command that performs a commit should review which files should be committed together based on best practice.

---

## [TASK-017] Ensure command and agent templates balance impact with simplicity and maintainability

**Status**: pending
**Priority**: high
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Ensure that command and agent template balance impact with simplicity and maintainability. Guiding principles:
- "Simplicity is the ultimate sophistication." – Leonardo da Vinci
- "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." – Antoine de Saint-Exupéry
- "Less, but better." – Dieter Rams
- "The ability to simplify means to eliminate the unnecessary so that the necessary may speak." – Hans Hofmann

Core principle: "Simplify: take away until only the essential remains."

---

## [TASK-018] Add GDPR compliance analyst agent

**Status**: pending
**Priority**: medium
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Add an agent with expertise in GDPR to ensure that solutions are GDPR compliant

---

## [TASK-019] Review and refactor any command or agent that saves to artifacts directory

**Status**: in-progress
**Priority**: medium
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Review and refactor any command or agent that saves to artifacts directory

---

## [TASK-020] Rename /prompt:enhance-prompt to /prompt:enhance

**Status**: pending
**Priority**: low
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Rename /prompt:enhance-prompt to /prompt:enhance

---

## [TASK-021] Review /system:setup-mcp for support for all available MCP servers

**Status**: pending
**Priority**: medium
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Review /system:setup-mcp for support for all available mcp servers

---

## [TASK-022] Replace command workflows (except git) with single pre-commit workflow for multi-vector review

**Status**: pending
**Priority**: high
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Replace command workflows (except git) with a single precommit workflow essentially does a multi vector review (replaces a pr review) on a chosen scope

---

## [TASK-023] Pre-commit workflow: conduct thorough analysis of uncommitted changes using parallel tasks

**Status**: pending
**Priority**: medium
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
For the precommit workflow. Input for prompt: conduct a thorough analysis of the uncommitted changes using parallel tasks and review if we need to modify or add something

---

## [TASK-024] Enhance review-claude-md command to analyze recent PRs and suggest CLAUDE.md improvements

**Status**: pending
**Priority**: medium
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
The review-claude-md command should also have the capability to review last x PRs and suggest improvements to the claude.md
- "Analyze current CLAUDE.md and suggest improvements based on recent issues"
- "What coding patterns should we standardize from recent PRs?"

---

## [TASK-025] Git commit process should evaluate if changes should be added to .gitignore

**Status**: pending
**Priority**: medium
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
When committing on git the process should also evaluate if any of the changes should be added to gitignore

---

## [TASK-026] Fix GitHub workflow error when Claude bot engages with PRs - add to allowed_bots list

**Status**: pending
**Priority**: high
**Category**: bug
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z

**Description**:
Fix the issue when claude engages with a pr on github:
Error: Prepare step failed with error: Workflow initiated by non-human actor: claude (type: Bot). Add bot to allowed_bots list or use '*' to allow all bots.

---

## [TASK-027] Document MCP server requirements (Docker Engine, etc.) for complete setup guide

**Status**: pending
**Priority**: medium
**Category**: docs
**Origin**: adhoc
**Created**: 2025-10-16T00:00:00Z

**Description**:
Docker engine is required for some MCPs to work - there might also be other requirements for other MCPs. This should be documented.

---

## [TASK-028] test haiku 4.5 model for speedy work

**Status**: pending
**Priority**: medium
**Category**: research
**Origin**: adhoc
**Created**: 2025-10-16T10:30:00Z

**Description**:
test haiku 4.5 model for speedy work

---

## [TASK-029] analyze the meaning of life from coding perspective using 2 subagents

**Status**: completed
**Priority**: medium
**Category**: research
**Origin**: adhoc
**Created**: 2025-10-16T10:31:00Z
**Last Updated**: 2025-10-19T07:05:00Z
**Completed**: 2025-10-19T07:05:00Z
**Details**: .agent/Session-task-029/TASK-029--analyze-the-meaning-of-life-from-coding-perspectiv/

---



## [TASK-030] change name of task:execute to task:implement

**Status**: pending
**Priority**: medium
**Category**: refactor
**Origin**: adhoc
**Created**: 2025-10-16T10:32:00Z

**Description**:
change name of task:execute to task:implement

---

## [TASK-031] ensure that sequential thinking is applied for complex problems only and evaluate MCP usage

**Status**: pending
**Priority**: high
**Category**: research
**Origin**: adhoc
**Created**: 2025-10-16T10:33:00Z

**Description**:
ensure that sequantial thinking is applied for complex problems only and also evaualte how the sequantial thinking mcp is actually utilized, how is depth of thinking controlled etc

---

## [TASK-032] ensure smarter model selection with simple agent template configuration

**Status**: pending
**Priority**: high
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-16T10:41:00Z

**Description**:
ensure smarter model selection - haiku for speed and specific tasks, sonnet for complexity - ensure agent tempalte offer a simple way to manage model and sequential thinking options

---
