# Master Task List - Claude Code System

**Version**: 2.0 (Value-Based Prioritization)
**Last Updated**: 2025-10-25
**Format**: Impact/Effort scoring - higher ratio = higher priority

---

## Value Scoring System

Each task scored by:
- **Impact** (1-10): Scope, user benefit, blockers unblocked
- **Effort** (1-10): Time required, complexity
- **Value** = Impact / Effort (higher = better ROI)

---

## Active Tasks

### TASK-602: Improve slash command usage in CLAUDE.md and command recommendations

**Status**: completed
**Priority**: medium
**Category**: chore
**Epic**: Command System Improvement
**Depends On**: (none)
**Related**: TASK-101
**Origin**: adhoc
**Created**: 2025-10-25T20:35:00Z
**Last Updated**: 2025-10-25T23:30:00Z
**Completed**: 2025-10-25T23:30:00Z
**Details**: `.agent/Session-command-recommendations/Task-602--improve-slash-command-usage`
**Impact**: 6 | **Effort**: 5 | **Value**: 1.2

**Description**:
Review CLAUDE.md files (user and project) to ensure they recommend using slash commands for relevant tasks. Audit existing commands to verify they utilize other slash commands effectively in their "Next Steps" sections and final recommendations. Identify gaps and update recommendations to guide users toward appropriate slash commands.

**Subtasks**:
- [x] Review user CLAUDE.md (~/CLAUDE.md) for slash command recommendations
- [x] Review project CLAUDE.md (.claude/CLAUDE.md) for slash command recommendations
- [x] Audit commands/*/commands to verify "Next Steps" reference relevant slash commands
- [x] Identify commands with missing or ineffective recommendations
- [x] Update CLAUDE.md files with better slash command guidance
- [x] Update command "Next Steps" sections with cross-command references

**Implementation Results**:

1. **User CLAUDE.md** - Added "Slash Command Workflows" section with 5 workflow examples
   - Brainstorm→Capture→Execute, Bug Fix, Feature Implementation, Documentation, Code Review
   - Command Selection Guide table (8 major command categories)
   - Critical rules about git operation delegation
   - ~100 lines of workflow documentation

2. **Project CLAUDE.md** - Added "Implementing Commands by Domain" guidance
   - Maps domain analysts to implementing slash commands
   - Shows recommended command chains (task→speckit→git) for each domain
   - Covers API, Database, Frontend, Code Quality, Security, Infrastructure, Documentation, Research, Testing, Performance

3. **prompt:enhance Command** - Fixed directory pattern issue
   - Replaced 16 `.artifacts/prompts/` references with session-aware paths
   - Aligned with save-artifact-to-markdown pattern
   - Now saves to `.agent/Session-{name}/context/prompt-enhanced-{slug}.md`

4. **Command Audit** - Verified slash command usage
   - 45/45 commands have Next Steps sections (100% coverage)
   - 45/45 commands reference slash commands in workflows
   - Documented cross-reference analysis in analysis.md
   - Identified enhancement opportunities for 5-10 commands

---

---

## Completed and Archived Tasks

**Archive Location**: `.agent/tasks-archive.md`

**Archived Tasks** (4 total):
- TASK-101: Apply interactive pattern to 35 commands ✓
- TASK-301: Integrate quality checklist into command creation ✓
- TASK-401: Review existing documentation for drift ✓
- TASK-501: Add GDPR compliance analyst agent ✓

**Archive Date**: 2025-10-25T20:20:00Z

---

## System Status

**Status**: ✅ All recommended tasks completed - system ready for production use

**Last Update**: 2025-10-25
**Format**: Value = Impact / Effort (ROI-based prioritization)
**Total Completed**: 4 system improvement tasks
**Total Value Delivered**: 3.83 (Impact/Effort sum)

---

## Next Steps

To view completed task details and history:
```bash
cat .agent/tasks-archive.md
```

To start new work:
```bash
/task:add "New task description"
```

To view task execution options:
```bash
/task:help
```
