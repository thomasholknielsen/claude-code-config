# Comprehensive Repository Refactoring Plan

**Date**: 2025-10-05
**Scope**: Multi-faceted repository cleanup and standardization
**Status**: Planning Complete - Awaiting Approval

## Executive Summary

This plan addresses 7 major refactoring areas across the Claude Code command system repository:

1. **Agent System Enhancement**: Add shadcn-analyst for UI development
2. **Artifact Storage Migration**: Transition from `.artifacts/context/` to `.agent/context/`
3. **Documentation Bloat Reduction**: Remove stats, timelines, and redundant phrases
4. **Frontmatter Standardization**: Remove drift-prone category/complexity fields
5. **Command Enhancement**: Update creation wizard with new requirements
6. **Tool Optimization**: Remove unused SlashCommand tools from agents
7. **Documentation Quality**: Add Mermaid chart guidance

## 1. Agent System Enhancement

### Task: Create shadcn-analyst Agent

**Objective**: Add UI/UX specialist agent for shadcn/ui component development

**Approach**:

- Adapt provided template to repository standards
- Change artifact storage from `.claude/doc/` to `.agent/context/`
- Remove implementation restrictions (agents are advisory)
- Update tool declarations to match repository patterns
- Integrate with existing MCP shadcn tools

**Key Changes from Template**:

```yaml
# Artifact storage path
- .claude/doc/xxxxx.md
+ .agent/context/{YYYY-MM-DD}-{sessiontopic}-{sessionid}.md

# Agent role (agents are advisory, not executors)
- NEVER do actual implementation
+ Provide implementation recommendations (agents are advisory)

# Tool declarations
- tools: [listed individually]
+ tools:
+   - Read
+   - Grep
+   - Glob
+   - mcp__shadcn (all shadcn tools)
```

**Output**: `/Users/thomasholknielsen/.claude/agents/shadcn-analyst.md`

## 2. Artifact Storage Migration

### Current State

```text
.artifacts/context/{domain}-analysis-{timestamp}.md
.artifacts/context/{domain}-{type}-{timestamp}.md
```

### Target State

```text
{project}/.agent/context/{YYYY-MM-DD}-{sessiontopic}-{sessionid}.md
```

### Migration Strategy

**Phase 1**: Update Templates

- Agent template: Update all `.artifacts/context/` references
- Command templates: Update artifact storage examples
- Documentation: Update all path references

**Phase 2**: Update Existing Agents (15 agents)

- python-analyst
- typescript-analyst
- react-analyst
- quality-analyst
- security-analyst
- performance-analyst
- testing-analyst
- accessibility-analyst
- documentation-analyst
- database-analyst
- api-analyst
- frontend-analyst
- architecture-analyst
- refactoring-analyst
- research-analyst

**Phase 3**: Update Both CLAUDE.md Files

- Project CLAUDE.md: File-Persisted Memory section
- User CLAUDE.md: Context Management Strategy section

**Phase 4**: Update Commands Referencing Artifacts

- All workflow commands that read artifact files
- Review commands that reference analysis files
- Documentation commands

**Session ID Management**:

```python
# Agents use this pattern:
python3 ~/.claude/.artifacts/session_manager.py current
# Returns: {sessionid}

# File naming:
{YYYY-MM-DD}-{sessiontopic}-{sessionid}.md
# Example: 2025-10-05-ui-refactoring-abc123.md
```

## 3. Documentation Bloat Reduction

### Anti-Drift Principle

**New Principle for Project CLAUDE.md**:

```markdown
## 📋 Anti-Drift Principles

**CRITICAL**: Avoid documentation that drifts from reality when the codebase changes.

**Prohibited**:
- ❌ Hard-coded counts ("15 domain analysts", "47 commands")
- ❌ Percentage statistics ("32% reduction after refactoring")
- ❌ Performance timings ("3-5min", "75-85% faster")
- ❌ Timeline estimates ("first week", "30-60 minutes", "1-3 months")
- ❌ Token burn percentages ("burn 90%+ tokens")
- ❌ Specific time comparisons ("5-8min vs 25-35min")

**Preferred**:
- ✅ Structural descriptions ("Multiple domain analysts", "Comprehensive command library")
- ✅ Qualitative improvements ("Significantly faster", "Improved performance")
- ✅ Priority levels ("Critical/High/Medium", "Immediate/Short-term/Long-term")
- ✅ Relative descriptions ("Main thread can parallelize", "Agents run sequentially")

**Rationale**: Statistics become outdated immediately upon system changes. Focus on principles, patterns, and architecture over precise metrics.
```

### Template-Only Frontmatter Principle

**New Principle for Project CLAUDE.md**:

```markdown
## 🎨 Frontmatter Standards

**Single Source of Truth**: Frontmatter syntax and structure are defined ONLY in templates.

**CLAUDE.md Role**:
- ✅ Reference templates for frontmatter specifications
- ✅ Explain the distinction between command and agent frontmatter
- ❌ Do NOT duplicate frontmatter YAML examples
- ❌ Do NOT show specific field syntax

**Correct Reference Pattern**:
"Commands use `allowed-tools`, agents use `tools`. See `templates/commands/command.md` and `templates/agents/agent-domain-specialist.md` for complete frontmatter specifications."

**Rationale**: Frontmatter syntax duplicated in CLAUDE.md creates drift when templates are updated. Templates are the authoritative source - CLAUDE.md should only reference them.
```

### Files Requiring Bloat Removal

**Project CLAUDE.md** (`/Users/thomasholknielsen/.claude/CLAUDE.md`):

- Remove System Architecture Stats section (lines 9-34)
- Update Domain Analyst Framework section (remove "burn 90%+ tokens")
- Remove Parallel Research Pattern performance stats (line 107)
- Remove all frontmatter syntax examples (keep only in templates)
- Remove Frontmatter Standards section (reference templates instead)
- Update to say "See templates/commands/ and templates/agents/ for frontmatter specifications"

**User CLAUDE.md** (`/Users/thomasholknielsen/CLAUDE.md`):

- Remove Performance Benefits section stats (lines 299-304)
- Update Context Management Strategy (remove noise/signal percentages)
- Preserve principles but remove specific timing claims

**Command Workflow Template** (`templates/commands/command-workflow.md`):

- Remove performance timing examples (line 141)
- Update with qualitative descriptions

**Agent Template** (`templates/agents/agent-domain-specialist.md`):

- Remove "burn 90%+ tokens" phrases
- Remove timeline sections (lines 168-177)
- Replace with priority-based recommendations

**Documentation Files**:

- README.md: Review for timeline references
- docs/github-automation.md: Remove timing estimates
- docs/output-styles/examples.md: Remove performance claims

## 4. Frontmatter Standardization

### Command Frontmatter Changes

**Remove from Templates**:

```yaml
category: "category-name"        # Remove - derived from file path
complexity: "simple|moderate|complex"  # Remove - causes drift
```

**Keep in Templates**:

```yaml
description: "Single clear sentence"
argument-hint: "[arg1] [--flag]"
allowed-tools: Tool1, Tool2, Bash(cmd:*)
```

**Rationale**:

- `category` is redundant (derived from `commands/{category}/` path)
- `complexity` drifts as commands evolve
- Both fields add maintenance burden without value

### Command Audit Strategy

**Discovery**:

```bash
# Find all commands with category or complexity
Glob: commands/**/*.md
Grep: "^category:|^complexity:" (with -C 3 for context)
```

**Batch Update Approach**:

1. Generate list of all command files
2. For each file, remove category and complexity lines
3. Verify frontmatter is still valid YAML
4. Test one command from each category

**Estimated Scope**: ~47 commands across 13 categories

## 5. Command Enhancement

### Update /slashcommand:create-from-template

**New Requirements to Add**:

1. **Analyst Assignment Prompt**:

   ```markdown
   **Agent Assignment**:
   - Which domain analyst(s) should this command use?
   - Options: {list current analysts}
   - Can suggest need for new analyst if none fit
   ```

2. **MCP Tool Integration Prompt**:

   ```markdown
   **MCP Integration**:
   - Does this command need external documentation? (Context7)
   - Does this command need browser automation? (Playwright)
   - Does this command need shadcn UI tools? (shadcn MCP)
   ```

3. **File Placement Validation**:

- Verify `commands/{category}/{name}.md` path
- Create category directory if new
- Confirm placement before writing

**Updated Process**:

```markdown
1. Select Template Type (atomic/workflow)
2. Collect Specifications:
   - Category (existing or new)
   - Command name (kebab-case)
   - Description
   - Arguments
   - Tools needed → Generate allowed-tools
   - Agent assignment → Add to Agent Integration section
   - MCP integration → Add to frontmatter if needed
3. Generate Command File
4. Confirm creation (show path and usage)
```

**Note**: Remove CLAUDE.md update step (violates anti-drift principle)

## 6. Tool Optimization

### Remove Unused SlashCommand Tool

**Discovery Strategy**:

```bash
# Find agents declaring SlashCommand
Grep: "- SlashCommand" agents/*.md

# Check if they actually use SlashCommand
# Read each agent to verify usage
```

**Expected Findings**:

- Many agents declare SlashCommand but don't use it
- SlashCommand is for commands, not subagents
- Agents should provide recommendations, not invoke commands

**Removal Criteria**:

- Agent doesn't contain instructions to use SlashCommand
- Agent is advisory (doesn't execute workflows)
- Agent focuses on analysis, not orchestration

**Keep SlashCommand For**:

- Agents that explicitly coordinate with /git:* commands
- Workflow agents that daisy-chain commands
- Any agent with documented SlashCommand usage

## 7. Documentation Quality Enhancement

### Add Mermaid Chart Guidance

**Target Commands/Agents**:

- `/docs:generate` - Add Mermaid architecture diagrams
- `/docs:update` - Update Mermaid diagrams when structure changes
- `/docs:api` - Add Mermaid sequence diagrams for API flows
- `/explain:architecture` - Use Mermaid for system architecture
- `documentation-analyst` - Include Mermaid in analysis

**Guidance to Add**:

```markdown
### Mermaid Diagram Integration

Use Mermaid charts to enhance documentation clarity:

**Architecture Diagrams**:

    ```mermaid
    graph TD
        A[Component A] --> B[Component B]
        B --> C[Component C]
    ```

**Sequence Diagrams**:

    ```mermaid
    sequenceDiagram
        Client->>API: Request
        API->>Database: Query
        Database-->>API: Result
        API-->>Client: Response
    ```

**Flowcharts**:

    ```mermaid
    flowchart LR
        Start --> Decision{Condition?}
        Decision -->|Yes| ActionA
        Decision -->|No| ActionB
        ActionA --> End
        ActionB --> End
    ```

**When to Use Mermaid**:

- System architecture overview
- API request/response flows
- Decision trees and logic flows
- Component relationships
- Process workflows
```

## Execution Strategy

### Phase 1: Foundation (No Dependencies)

- ✅ Create refactoring plan (this document)
- Create shadcn-analyst agent
- Add anti-drift principle to project CLAUDE.md

### Phase 2: Template Updates (Low Risk)

- Update command templates (remove category/complexity)
- Update agent template (remove bloat, update artifact paths)
- Add Mermaid guidance to templates

### Phase 3: CLAUDE.md Cleanup (Moderate Risk)

- Update project CLAUDE.md (remove stats, update paths)
- Update user CLAUDE.md (remove performance stats)
- Verify both files still parse correctly

### Phase 4: Mass Updates (High Volume)

- Update all 15 agents (artifact paths, remove bloat)
- Update all ~47 commands (remove frontmatter fields)
- Update documentation files (remove timelines)

### Phase 5: Command Enhancement (Functional Change)

- Update /slashcommand:create with new requirements
- Test command creation wizard
- Document new workflow

### Phase 6: Tool Optimization (Cleanup)

- Audit agents for unused SlashCommand
- Remove SlashCommand from non-using agents
- Verify agents still function correctly

### Phase 7: Documentation Enhancement (Quality)

- Add Mermaid guidance to docs commands
- Add Mermaid guidance to documentation-analyst
- Update relevant command documentation

## Validation Strategy

### Automated Checks

```bash
# Verify no drift-prone stats remain
grep -r "burn \d+%" .
grep -r "\d+-\d+ min" .
grep -r "\d+% faster" .

# Verify artifact path migration
grep -r ".artifacts/context/" .
grep -r ".agent/context/" .

# Verify frontmatter cleanup
grep -r "^category:" commands/
grep -r "^complexity:" commands/

# Verify YAML validity
for file in commands/**/*.md; do
  # Extract and validate frontmatter
done
```

### Manual Verification

- Test /slashcommand:create with new prompts
- Verify one agent from each domain works correctly
- Test one command from each category
- Verify CLAUDE.md files are accurate and complete

## Risk Assessment

### Low Risk

- Adding shadcn-analyst (new, isolated)
- Adding anti-drift principle (documentation only)
- Removing unused tools (no functional impact)

### Medium Risk

- Artifact path migration (requires coordination)
- Frontmatter removal (could break parsing)
- Template updates (affects future commands)

### High Risk

- CLAUDE.md bloat removal (core documentation)
- Mass command updates (high volume changes)

### Mitigation Strategy

- Work on feature branch (`005-simplify-the-claude`)
- Commit after each phase
- Test representative samples
- Keep rollback option available

## Success Criteria

### Functional

- ✅ All commands parse correctly (valid frontmatter)
- ✅ All agents function as expected (artifact storage works)
- ✅ /slashcommand:create wizard includes new prompts
- ✅ No drift-prone statistics in documentation
- ✅ Mermaid guidance added to relevant commands

### Quality

- ✅ CLAUDE.md files are concise and accurate
- ✅ Templates reflect current best practices
- ✅ Documentation uses principles over metrics
- ✅ Agents use consistent artifact storage pattern

### Maintainability

- ✅ Anti-drift principle prevents future bloat
- ✅ Frontmatter is minimal and necessary
- ✅ Artifact paths are consistent across system
- ✅ Commands are properly categorized and documented

## Timeline Estimates

**Phase 1-2**: Quick wins (agent creation, template updates)
**Phase 3**: Moderate effort (CLAUDE.md cleanup)
**Phase 4**: High volume (mass updates to agents/commands)
**Phase 5-7**: Incremental improvements (enhancements and optimization)

**Note**: Actual execution depends on approval and can be parallelized where dependencies allow.

## Open Questions for User

1. **Artifact Storage**: Confirm `.agent/context/{YYYY-MM-DD}-{sessiontopic}-{sessionid}.md` pattern is correct
2. **Session Topic**: How should `{sessiontopic}` be determined? (user input, auto-detect, command name?)
3. **Shadcn Agent**: Should shadcn-analyst be "MUST BE USED" or "Use PROACTIVELY"?
4. **Category Removal**: Any concerns about removing category from command frontmatter?
5. **Stats Removal**: Should we completely remove System Architecture Stats or replace with qualitative descriptions?
6. **Mermaid**: Are there other commands/agents that should include Mermaid guidance?

## Appendix: File Inventory

### Templates (3 files)

- `templates/commands/command.md`
- `templates/commands/command-workflow.md`
- `templates/agents/agent-domain-specialist.md`

### CLAUDE.md Files (2 files)

- `/Users/thomasholknielsen/.claude/CLAUDE.md` (project)
- `/Users/thomasholknielsen/CLAUDE.md` (user/global)

### Agents (15+ files)

- All files in `agents/*.md`

### Commands (~47 files)

- All files in `commands/**/*.md`

### Documentation (5+ files)

- README.md
- docs/github-automation.md
- docs/output-styles/examples.md
- Other docs as discovered

### Target Command for Enhancement (1 file)

- `commands/slashcommand/create-from-template.md`

---

**Plan Status**: ✅ Complete - Updated with Template-Only Frontmatter Principle

**Key Update Based on User Feedback**:
Added "Template-Only Frontmatter Principle" to Section 3. CLAUDE.md files will no longer contain frontmatter syntax examples - these will be maintained exclusively in `templates/commands/` and `templates/agents/` to prevent drift.

**Next Step**: User review and approval to proceed with execution
