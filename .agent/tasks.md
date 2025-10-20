# Active Tasks

## [TASK-001] Ensure all configured MCP servers are integrated into the repository

**Status**: completed
**Details**: .agent/Session-chores/TASK-001--ensure-all-configured-mcp-servers-are-integrated-i
**Priority**: medium
**Category**: chore
**Epic**: MCP Integration
**Depends On**: (none)
**Related**: TASK-011, TASK-021
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T10:29:41.271837+00:00
**Last Updated**: 2025-10-19T10:29:41.271837+00:00

**Description**:
Ensure all configured mcpservers{} are integrated into the repos, meaning that relevant commands and subagents and templates are "aware" of all mcps

---

## [TASK-002] Review current workflow commands for comprehensive pre-commit review capability

**Status**: pending
**Priority**: high
**Category**: feature
**Epic**: Pre-Commit Workflow
**Depends On**: (none)
**Related**: TASK-008, TASK-022, TASK-023
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Review current workflow commands for coverage of this already - we need one command to launch a comprehensive review of either the entire repos or the uncommitted changes. The objective is to provide a list of critical issues and discrepancies that we should consider fixing before committing - similar to a PR review.

---

## [TASK-003] Critical review of command template(s) - consider consolidation

**Status**: pending
**Priority**: high
**Category**: refactor
**Epic**: Template Standardization
**Depends On**: (none)
**Related**: TASK-004, TASK-005, TASK-006
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Critical review of command template(s) perhaps consolidate into one?

---

## [TASK-004] Critical review of mermaid template

**Status**: pending
**Priority**: medium
**Category**: chore
**Epic**: Template Standardization
**Depends On**: (none)
**Related**: TASK-003, TASK-005, TASK-006
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Critical review of mermaid template

---

## [TASK-005] Align agents with template

**Status**: pending
**Priority**: medium
**Category**: chore
**Epic**: Template Standardization
**Depends On**: TASK-003
**Related**: TASK-003, TASK-004, TASK-006
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Align agents with template

---

## [TASK-006] Align mermaid with template

**Status**: pending
**Priority**: medium
**Category**: chore
**Epic**: Template Standardization
**Depends On**: TASK-003
**Related**: TASK-003, TASK-004, TASK-005
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Align mermaid with template

---

## [TASK-007] Align commands with template, except speckit

**Status**: pending
**Priority**: medium
**Category**: chore
**Epic**: Template Standardization
**Depends On**: TASK-003
**Related**: TASK-003, TASK-004, TASK-005
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Align commands with template, except speckit

---

## [TASK-008] /workflow:docs starts work without confirmation - should perform detailed analysis and suggest actions

**Status**: pending
**Priority**: high
**Category**: bug
**Epic**: Pre-Commit Workflow
**Depends On**: (none)
**Related**: TASK-002, TASK-022, TASK-023
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
/workflow:docs starts work without confirmation - it should perform a detailed analysis and suggest actions

---

## [TASK-009] When adding tasks - automatically create enhanced prompt and relate to tasks in task.md

**Status**: pending
**Priority**: medium
**Category**: feature
**Epic**: Task Management Enhancement
**Depends On**: (none)
**Related**: TASK-030
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
When adding tasks - automatically create enhanced prompt and relate to tasks in task.md

---

## [TASK-010] Evaluate speckit:implement command's use of subagents - determine if enhancement needed

**Status**: pending
**Priority**: medium
**Category**: research
**Epic**: Speckit Enhancement
**Depends On**: (none)
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
The speckit functions are great and should be changed as little as possible. Some changes have already been applied through speckit:apply-user-settings-fix command. But we should also evaluate if the speckit:implement command makes use of the subagents - does it already do this or should we imply this more directly through the users claude.md file?

---

## [TASK-011] Subagents/commands that depend on MCP tools should handle missing/failing MCP gracefully

**Status**: completed
**Completed**: 2025-10-19T15:09:07.603873
**Details**: .agent/Session-chores/TASK-011--subagentscommands-that-depend-on-mcp-tools-should-
**Priority**: high
**Category**: feature
**Epic**: MCP Integration
**Depends On**: (none)
**Related**: TASK-001, TASK-021
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T12:33:13.301159+00:00

**Description**:
Subagents/commands that depend on mcp tools should be able to handle missing/failing mcp gracefully

---

## [TASK-012] Review commands template from UX perspective and integrate template changes onto existing commands

**Status**: pending
**Priority**: medium
**Category**: refactor
**Epic**: Template Standardization
**Depends On**: TASK-003
**Related**: TASK-003, TASK-004, TASK-005
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Review the commands template from a UX perspective and integrate any template changes onto existing commands

---

## [TASK-013] Apply reasoning for complex tasks - think deeply and sequentially - add to user CLAUDE.md and repo copy

**Status**: pending
**Priority**: medium
**Category**: docs
**Epic**: Documentation
**Depends On**: (none)
**Related**: TASK-024, TASK-027
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Apply reasoning for complex tasks think deeply and sequentially - add this to user claude.md and repos copy

---

## [TASK-014] Review argument hints for commands and include marker for defaults

**Status**: pending
**Priority**: medium
**Category**: refactor
**Epic**: UI/UX
**Depends On**: (none)
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Review argument hints for commands + include marker for defaults

---

## [TASK-015] Use speckit to refactor context management file structure for session and task organization

**Status**: in
**Priority**: high
**Category**: refactor
**Epic**: Context Management
**Depends On**: (none)
**Related**: TASK-019
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Use speckit to refactor the context management file structure to enable session work as well as task work. Proposed structure:

---

## [TASK-016] Ensure /git:commit and workflows handle pre-commit hook failures with auto-fix and recommit

**Status**: pending
**Priority**: high
**Category**: feature
**Epic**: Git Workflow
**Depends On**: (none)
**Related**: TASK-025, TASK-026
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Ensure that when /git:commit tries to commit and precommit hooks fail, then it should resolve these errors, stage the changes again and recommit. This is also true for other workflows that perform commits. Also ensure that every command that performs a commit should review which files should be committed together based on best practice.

---

## [TASK-017] Ensure command and agent templates balance impact with simplicity and maintainability

**Status**: pending
**Priority**: high
**Category**: refactor
**Epic**: Template Standardization
**Depends On**: (none)
**Related**: TASK-003, TASK-004, TASK-005
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Ensure that command and agent template balance impact with simplicity and maintainability. Guiding principles:
- "Simplicity is the ultimate sophistication." – Leonardo da Vinci
- "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away." – Antoine de Saint-Exupéry
- "Less, but better." – Dieter Rams
- "The ability to simplify means to eliminate the unnecessary so that the necessary may speak." – Hans Hofmann

---

## [TASK-018] Add GDPR compliance analyst agent

**Status**: pending
**Priority**: medium
**Category**: feature
**Epic**: Security
**Depends On**: (none)
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Add an agent with expertise in GDPR to ensure that solutions are GDPR compliant

---

## [TASK-019] Review and refactor any command or agent that saves to artifacts directory

**Status**: in
**Priority**: medium
**Category**: refactor
**Epic**: Context Management
**Depends On**: TASK-015
**Related**: TASK-015
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T05:01:49.175447Z

**Description**:
Review and refactor any command or agent that saves to artifacts directory

---

## [TASK-020] Rename /prompt:enhance-prompt to /prompt:enhance

**Status**: completed
**Details**: .agent/Session-chores/TASK-020--rename-promptenhance-prompt-to-promptenhance
**Priority**: low
**Category**: refactor
**Epic**: Misc
**Depends On**: (none)
**Related**: TASK-029
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T09:52:23.328857+00:00
**Last Updated**: 2025-10-19T09:52:23.328857+00:00

**Description**:
Rename /prompt:enhance-prompt to /prompt:enhance

---

## [TASK-021] Review /system:setup-mcp for support for all available MCP servers

**Status**: completed
**Completed**: 2025-10-19T15:09:07.603884
**Priority**: medium
**Category**: feature
**Epic**: MCP Integration
**Depends On**: (none)
**Related**: TASK-001, TASK-011
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Details**: .agent/Session-chores/TASK-021--review-systemsetup-mcp-for-support-for-all-availab
**Last Updated**: 2025-10-19T16:45:00Z

**Description**:
Review /system:setup-mcp for support for all available mcp servers

---

## [TASK-022] Replace command workflows (except git) with single pre-commit workflow for multi-vector review

**Status**: pending
**Priority**: high
**Category**: refactor
**Epic**: Pre-Commit Workflow
**Depends On**: TASK-002
**Related**: TASK-002, TASK-008, TASK-023
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
Replace command workflows (except git) with a single precommit workflow essentially does a multi vector review (replaces a pr review) on a chosen scope

---

## [TASK-023] Pre-commit workflow: conduct thorough analysis of uncommitted changes using parallel tasks

**Status**: pending
**Priority**: medium
**Category**: feature
**Epic**: Pre-Commit Workflow
**Depends On**: TASK-002
**Related**: TASK-002, TASK-008, TASK-022
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
For the precommit workflow. Input for prompt: conduct a thorough analysis of the uncommitted changes using parallel tasks and review if we need to modify or add something

---

## [TASK-024] Enhance review-claude-md command to analyze recent PRs and suggest CLAUDE.md improvements

**Status**: pending
**Priority**: medium
**Category**: feature
**Epic**: Documentation
**Depends On**: (none)
**Related**: TASK-013, TASK-027
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
The review-claude-md command should also have the capability to review last x PRs and suggest improvements to the claude.md
- "Analyze current CLAUDE.md and suggest improvements based on recent issues"
- "What coding patterns should we standardize from recent PRs?"

---

## [TASK-025] Git commit process should evaluate if changes should be added to .gitignore

**Status**: pending
**Priority**: medium
**Category**: feature
**Epic**: Git Workflow
**Depends On**: (none)
**Related**: TASK-016, TASK-026
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
When committing on git the process should also evaluate if any of the changes should be added to gitignore

---

## [TASK-026] Fix GitHub workflow error when Claude bot engages with PRs - add to allowed_bots list

**Status**: pending
**Priority**: high
**Category**: bug
**Epic**: Git Workflow
**Depends On**: (none)
**Related**: TASK-016, TASK-025
**Origin**: adhoc
**Created**: 2025-10-15T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
Fix the issue when claude engages with a pr on github:
Error: Prepare step failed with error: Workflow initiated by non-human actor: claude (type: Bot). Add bot to allowed_bots list or use '*' to allow all bots.

---

## [TASK-027] Document MCP server requirements (Docker Engine, etc.) for complete setup guide

**Status**: pending
**Priority**: medium
**Category**: docs
**Epic**: Documentation
**Depends On**: (none)
**Related**: TASK-013, TASK-024
**Origin**: adhoc
**Created**: 2025-10-16T00:00:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
Docker engine is required for some MCPs to work - there might also be other requirements for other MCPs. This should be documented.

---

## [TASK-028] test haiku 4.5 model for speedy work

**Status**: pending
**Priority**: medium
**Category**: research
**Epic**: Model & Performance
**Depends On**: (none)
**Related**: TASK-031, TASK-032
**Origin**: adhoc
**Created**: 2025-10-16T10:30:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
test haiku 4.5 model for speedy work

---

## [TASK-029] analyze the meaning of life from coding perspective using 2 subagents

**Status**: completed
**Priority**: medium
**Category**: research
**Epic**: Misc
**Depends On**: (none)
**Related**: TASK-020
**Origin**: adhoc
**Created**: 2025-10-16T10:31:00Z
**Completed**: 2025-10-19T07:05:00Z
**Last Updated**: 2025-10-19T07:05:00Z

**Description**:
change name of task:execute to task:implement

---

## [TASK-030] change name of task:execute to task:implement

**Status**: pending
**Priority**: medium
**Category**: refactor
**Epic**: Task Management Enhancement
**Depends On**: (none)
**Related**: TASK-009
**Origin**: adhoc
**Created**: 2025-10-16T10:32:00Z

**Description**:
change name of task:execute to task:implement

---

## [TASK-031] ensure that sequential thinking is applied for complex problems only and evaluate MCP usage

**Status**: pending
**Priority**: high
**Category**: research
**Epic**: Model & Performance
**Depends On**: (none)
**Related**: TASK-028, TASK-032
**Origin**: adhoc
**Created**: 2025-10-16T10:33:00Z

**Description**:
ensure that sequantial thinking is applied for complex problems only and also evaualte how the sequantial thinking mcp is actually utilized, how is depth of thinking controlled etc

---

## [TASK-032] ensure smarter model selection with simple agent template configuration

**Status**: pending
**Priority**: high
**Category**: feature
**Epic**: Model & Performance
**Depends On**: (none)
**Related**: TASK-028, TASK-031
**Origin**: adhoc
**Created**: 2025-10-16T10:41:00Z

**Description**:
ensure smarter model selection - haiku for speed and specific tasks, sonnet for complexity - ensure agent tempalte offer a simple way to manage model and sequential thinking options

---

## [TASK-033] Consider adding "claude skills" as a vector of productivity into the repos

**Status**: pending
**Priority**: medium
**Category**: feature
**Epic**: (none)
**Depends On**: (none)
**Related**: (none)
**Origin**: adhoc
**Created**: 2025-10-19T07:10:00Z

**Description**:
Consider adding "claude skills" as a vector of productivity into the repos

---

## [TASK-034] Update 8 existing agents to use newly-integrated MCP tools

**Status**: completed
**Priority**: medium
**Category**: refactor
**Epic**: MCP Integration
**Depends On**: (none)
**Related**: TASK-001, TASK-011, TASK-021
**Origin**: adhoc
**Created**: 2025-10-19T10:36:14.512216+00:00

**Description**:
Update 8 existing agents to use newly-integrated MCP tools (fetch, markitdown, terraform):

**Fetch MCP (4 agents)**:
- api-docs-analyst
- docs-docusaurus-analyst
- seo-analyst
- research-web-analyst (already has)

**Markitdown MCP (4 agents)**:
- api-docs-analyst
- database-architecture-analyst
- docs-docusaurus-analyst
- research-web-analyst (already has)

**Terraform MCP (4 agents)**:
- infrastructure-cloud-analyst
- infrastructure-devops-analyst
- infrastructure-monitoring-analyst
- infrastructure-network-analyst

Template is already updated (TASK-001), this backfills existing agents.

---
