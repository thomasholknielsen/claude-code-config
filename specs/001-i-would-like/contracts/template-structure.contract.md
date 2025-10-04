# Contract: Template Structure Validation

**Feature**: 001-i-would-like
**Contract Type**: File Structure Validation
**Date**: 2025-10-03

## Purpose

Defines the validation contract for command template files to ensure they include all required sections and proper frontmatter schema.

## Template File Contracts

### Base Template Contract (`templates/command.md`)

**Required Frontmatter Fields**:

```yaml
---
description: "<single sentence>"
argument-hint: "[arg1] [--flag]"
category: "<category-name>"
tools: ["Tool1", "Tool2"]
complexity: "simple|moderate|complex"
allowed-tools: <permission-syntax>
---
```

**Required Sections** (in order):

1. `# Command: <Action Verb> <Object>`
2. `## Purpose`
3. `## Usage`
4. `## Process`
5. `## Agent Integration`
6. `## Examples`
7. `## Integration Points` (optional)
8. `## Quality Standards` (optional)

**Required Documentation Elements**:

- $ARGUMENTS parsing explanation in Usage section
- Numbered process steps
- Agent specialist identification
- Real usage examples with $ARGUMENTS values
- allowed-tools syntax examples

**Validation Criteria**:

- [ ] File exists at `templates/command.md`
- [ ] Contains valid YAML frontmatter
- [ ] All 6 required frontmatter fields present
- [ ] allowed-tools field includes syntax examples
- [ ] All required section headings present
- [ ] $ARGUMENTS documentation pattern shown
- [ ] Agent Integration section identifies specialist
- [ ] Examples section shows concrete usage

### Workflow Template Contract (`templates/command-workflow.md`)

**Additional/Different Sections**:

- `## Implementation Steps` (replaces Process)
- `## Sequential Command Execution` (workflow-specific)
- Agent: `task-orchestrator` instead of specialized agents

**Validation Criteria**:

- [ ] File exists at `templates/command-workflow.md`
- [ ] Contains valid YAML frontmatter
- [ ] Shows SlashCommand tool usage in Implementation Steps
- [ ] Documents sequential command orchestration
- [ ] Identifies task-orchestrator as primary agent

## Command File Contracts

### Atomic Command Contract

**Applies To**: 47 atomic commands (analyze/*, clean/*, docs/*, etc.)

**Required Conformity**:

```yaml
---
description: "<description>"
argument-hint: "[arguments]"
category: "<category>"
tools: [<tools-list>]
complexity: "simple|moderate|complex"
allowed-tools: <permissions>
---

# Command: <Name>

## Purpose
<single-sentence description>

## Usage
/<category>:<command> $ARGUMENTS

## Process
1. Step 1
2. Step 2
...

## Agent Integration
- **Specialist**: <agent-name>

## Examples
<usage examples with $ARGUMENTS>
```

**Validation Criteria**:

- [ ] Frontmatter valid YAML
- [ ] All 6 required fields present
- [ ] allowed-tools follows syntax: `Tool1, Tool2, Bash(cmd:*)`
- [ ] Purpose is single sentence
- [ ] Usage shows $ARGUMENTS pattern
- [ ] Process has numbered steps
- [ ] Agent Integration identifies specialist
- [ ] Examples show real usage

### Workflow Command Contract

**Applies To**: 7 workflow commands in workflows/* category

**Allowed Variations**:

- Implementation Steps instead of Process
- Sequential Command Execution section showing SlashCommand calls
- task-orchestrator as primary agent

**Validation Criteria**:

- [ ] Frontmatter valid YAML
- [ ] All 6 required fields present
- [ ] allowed-tools field present
- [ ] Shows command orchestration with SlashCommand tool
- [ ] Documents sequential execution strategy

## CLAUDE.md Contract

**Required Template References**:

```markdown
### Command Development

**Required Format** (follow templates):
- Atomic commands: Use `templates/command.md`
- Workflow commands: Use `templates/command-workflow.md`
- Required frontmatter fields: description, argument-hint, category, tools, complexity, allowed-tools
- allowed-tools syntax: `Tool1, Tool2, Bash(command:*)`
```

**Validation Criteria**:

- [ ] CLAUDE.md references both template files
- [ ] Command Development section exists
- [ ] Lists all 6 required frontmatter fields
- [ ] Shows allowed-tools syntax pattern
- [ ] Distinguishes atomic vs workflow templates

## Migration Contracts

### Auto-Conforming Command

**Criteria**:

- Existing frontmatter matches required fields
- Section structure matches template
- No custom sections beyond template

**Contract**:

- [ ] Validate frontmatter syntax
- [ ] Ensure allowed-tools field present with correct syntax
- [ ] No modifications to existing content needed

### Simple-Update Command

**Criteria**:

- Missing some sections but no custom content
- Frontmatter mostly complete

**Contract**:

- [ ] Add missing frontmatter fields (especially allowed-tools)
- [ ] Add missing sections with placeholder content
- [ ] Preserve existing content structure

### Manual-Review Command

**Criteria**:

- Has custom sections not in template
- Complex or non-standard structure
- Workflow command requiring different template

**Contract**:

- [ ] Flag with comment marker: `<!-- MANUAL REVIEW: Custom sections beyond template -->`
- [ ] Do not auto-modify content
- [ ] Ensure frontmatter includes allowed-tools field
- [ ] Document custom sections for review

## Test Scenarios

### Scenario 1: New Command Creation

**Given**: Developer wants to create `/analyze:new-command`
**When**: Uses template at `templates/command.md`
**Then**:

- File includes all required frontmatter
- All required sections present
- allowed-tools syntax correct
- Validates successfully

### Scenario 2: Existing Command Migration (Auto)

**Given**: Existing command `/docs/generate.md` matches template
**When**: Validation script runs
**Then**:

- Frontmatter validated
- allowed-tools field checked
- Marked as auto-conforming
- No manual intervention needed

### Scenario 3: Existing Command Migration (Manual)

**Given**: Workflow command `/workflows/run-comprehensive-review.md` with custom sections
**When**: Validation script runs
**Then**:

- Flagged for manual review
- Comment marker added
- Frontmatter validated
- Custom content preserved

### Scenario 4: CLAUDE.md Update

**Given**: CLAUDE.md needs template reference
**When**: Update applied
**Then**:

- Both template paths referenced
- Syntax rules documented
- Command development directive present
- Validates successfully

## Acceptance Criteria

**Phase 1 Complete When**:

1. Both template files created and validated
2. All contracts documented
3. CLAUDE.md update specification complete
4. Migration categorization rules defined
5. Validation criteria clear and testable
