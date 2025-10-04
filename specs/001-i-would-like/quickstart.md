# Quickstart: Slash Command Template System

**Feature**: 001-i-would-like
**Date**: 2025-10-03
**Purpose**: Validate template system implementation through end-to-end scenarios

## Prerequisites

- Templates created at `templates/command.md` and `templates/command-workflow.md`
- CLAUDE.md updated with template references
- Access to existing commands in `commands/` directory

## Scenario 1: Create New Atomic Command Using Template

**Goal**: Verify developers can create new commands using the base template

**Steps**:

1. **Copy Base Template**

   ```bash
   # From repository root
   cat templates/command.md
   ```

   **Expected**: See complete template with all required sections and frontmatter

2. **Create New Command File**

   ```bash
   # Example: Create new /analyze:tech-debt command
   mkdir -p commands/analyze
   # Use template as starting point
   ```

3. **Fill Required Frontmatter**

   ```yaml
   ---
   description: "Analyze technical debt and code quality metrics"
   argument-hint: "[path] [--severity=high|medium|low]"
   category: "analyze"
   tools: ["Read", "Grep", "Bash"]
   complexity: "moderate"
   allowed-tools: Bash(cloc:*), Bash(git log:*), Read, Grep
   ---
   ```

4. **Complete Required Sections**
   - Purpose: Single sentence
   - Usage: Show $ARGUMENTS pattern
   - Process: Numbered steps
   - Agent Integration: Identify specialist
   - Examples: Real usage scenarios

5. **Validate Command Structure**

   ```bash
   # Check frontmatter is valid YAML
   head -n 10 commands/analyze/tech-debt.md | grep -A 7 "^---$"

   # Verify required sections exist
   grep "^## " commands/analyze/tech-debt.md
   ```

**Success Criteria**:

- [ ] Template provides complete structure
- [ ] All 6 frontmatter fields present
- [ ] allowed-tools syntax correct
- [ ] All required sections included
- [ ] $ARGUMENTS documented in examples

## Scenario 2: Update Existing Command to Template Standard

**Goal**: Verify existing commands can be updated to conform to template

**Steps**:

1. **Select Test Command**

   ```bash
   # Use commands/analyze/dependencies.md as test case
   cat commands/analyze/dependencies.md
   ```

2. **Validate Current Frontmatter**

   ```bash
   # Extract and check frontmatter
   sed -n '/^---$/,/^---$/p' commands/analyze/dependencies.md
   ```

3. **Check for allowed-tools Field**

   ```bash
   grep "allowed-tools:" commands/analyze/dependencies.md
   ```

   **Expected**: May be missing (needs addition)

4. **Add allowed-tools if Missing**

   ```yaml
   allowed-tools: Bash, Read, Grep, WebFetch
   ```

5. **Verify Section Structure**

   ```bash
   # Check all required sections present
   grep "^## Purpose$\|^## Usage$\|^## Process$\|^## Agent Integration$\|^## Examples$" \
     commands/analyze/dependencies.md
   ```

6. **Validate $ARGUMENTS Documentation**

   ```bash
   # Ensure $ARGUMENTS is explained
   grep "\$ARGUMENTS" commands/analyze/dependencies.md
   ```

**Success Criteria**:

- [ ] allowed-tools field added with correct syntax
- [ ] All required sections present or added
- [ ] $ARGUMENTS pattern documented
- [ ] Agent integration specified
- [ ] Existing content preserved

## Scenario 3: CLAUDE.md Directs to Template

**Goal**: Verify CLAUDE.md successfully references templates for command creation

**Steps**:

1. **Read CLAUDE.md Configuration**

   ```bash
   grep -A 10 "Command Development" CLAUDE.md
   ```

2. **Verify Template References**
   **Expected Output**:

   ```markdown
   ### Command Development

   **Required Format** (follow templates):
   - Atomic commands: Use `templates/command.md`
   - Workflow commands: Use `templates/command-workflow.md`
   ```

3. **Check Frontmatter Field Documentation**

   ```bash
   grep "required frontmatter fields" CLAUDE.md
   ```

   **Expected**: Lists all 6 required fields

4. **Verify allowed-tools Syntax Guidance**

   ```bash
   grep "allowed-tools syntax" CLAUDE.md
   ```

   **Expected**: Shows pattern like `Tool1, Tool2, Bash(command:*)`

5. **Confirm Template Variant Guidance**

   ```bash
   grep "atomic vs workflow" CLAUDE.md
   ```

   **Expected**: Explains when to use each template

**Success Criteria**:

- [ ] CLAUDE.md references both template files
- [ ] Command Development section exists
- [ ] All 6 frontmatter fields listed
- [ ] allowed-tools syntax documented
- [ ] Template variant guidance present

## Scenario 4: Workflow Command Template Usage

**Goal**: Verify workflow template is distinct and appropriate

**Steps**:

1. **Review Workflow Template**

   ```bash
   cat templates/command-workflow.md
   ```

2. **Identify Workflow-Specific Sections**
   **Expected**:
   - Implementation Steps (instead of Process)
   - Sequential Command Execution
   - Shows SlashCommand tool usage

3. **Compare with Existing Workflow**

   ```bash
   # Check existing workflow command
   cat commands/workflows/run-comprehensive-review.md
   ```

4. **Verify task-orchestrator Agent**

   ```bash
   grep "task-orchestrator" templates/command-workflow.md
   ```

   **Expected**: Workflow template uses task-orchestrator, not specialized agents

**Success Criteria**:

- [ ] Workflow template distinct from base template
- [ ] Shows SlashCommand orchestration pattern
- [ ] Uses task-orchestrator agent
- [ ] Implementation Steps section present
- [ ] Sequential execution documented

## Scenario 5: Command Migration Categorization

**Goal**: Verify existing commands are correctly categorized for migration

**Steps**:

1. **Scan Auto-Conforming Commands**

   ```bash
   # Find commands already matching template
   # Example: commands/git/commit.md
   ```

   **Criteria**: Has all frontmatter fields, standard sections

2. **Identify Simple-Update Commands**

   ```bash
   # Find commands missing sections but no custom content
   # Example: commands with missing allowed-tools field
   ```

   **Criteria**: Missing some fields/sections but otherwise standard

3. **Flag Manual-Review Commands**

   ```bash
   # Find commands with custom sections
   # Example: workflow commands, commands with special structure
   ```

   **Criteria**: Has content beyond standard template sections

4. **Test Manual Review Marker**

   ```bash
   # Check for review comment marker
   grep "<!-- MANUAL REVIEW" commands/workflows/*.md
   ```

**Success Criteria**:

- [ ] Auto-conforming commands identified (estimated ~20)
- [ ] Simple-update commands identified (estimated ~20)
- [ ] Manual-review commands flagged (estimated ~14)
- [ ] No commands auto-modified with custom sections
- [ ] Review markers present where needed

## Scenario 6: End-to-End New Command Workflow

**Goal**: Complete workflow from template to finished command

**Steps**:

1. **Start with Template**
   - Copy `templates/command.md` for new command `/refactor:modernize`

2. **Fill Metadata**

   ```yaml
   ---
   description: "Modernize code to use current language features"
   argument-hint: "[path] [--target-version]"
   category: "refactor"
   tools: ["Read", "Edit", "Bash"]
   complexity: "complex"
   allowed-tools: Read, Edit, Bash(npm test:*), Bash(linting:*)
   ---
   ```

3. **Complete All Sections**
   - Purpose: "Modernize legacy code..."
   - Usage: Show $ARGUMENTS examples
   - Process: 5-step workflow
   - Agent Integration: code-writer specialist
   - Examples: 3 real scenarios

4. **Validate Against Contract**
   - Check frontmatter valid YAML
   - Verify all 6 fields present
   - Confirm allowed-tools syntax
   - Ensure all sections complete

5. **Save and Test**

   ```bash
   # Save to commands/refactor/modernize.md
   # Verify file structure
   cat commands/refactor/modernize.md
   ```

**Success Criteria**:

- [ ] Template provides complete starting structure
- [ ] All required elements easily identifiable
- [ ] Developer can complete command without confusion
- [ ] Final command validates successfully
- [ ] Follows all contract requirements

## Validation Checklist

After completing quickstart scenarios, verify:

**Templates**:

- [ ] Base template complete and usable
- [ ] Workflow template distinct and appropriate
- [ ] Both templates have all required sections
- [ ] Examples and patterns clear

**CLAUDE.md**:

- [ ] References both template files
- [ ] Documents required frontmatter fields
- [ ] Shows allowed-tools syntax
- [ ] Explains template selection

**Migration**:

- [ ] Can identify auto-conforming commands
- [ ] Can flag manual-review commands
- [ ] allowed-tools can be added safely
- [ ] Existing content preserved

**End-to-End**:

- [ ] New commands can be created from template
- [ ] Existing commands can be updated
- [ ] Validation criteria clear
- [ ] No ambiguity in requirements

## Notes

- Manual review required for ~14 commands with custom sections
- No automated enforcement (per clarifications)
- Template updates don't propagate to existing commands
- This is a one-time migration effort
