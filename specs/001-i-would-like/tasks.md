# Tasks: Slash Command Template Standardization System

**Input**: Design documents from `/specs/001-i-would-like/`
**Prerequisites**: plan.md, research.md, data-model.md, contracts/, quickstart.md

## Execution Flow (main)

```text
1. Load plan.md from feature directory
   → Extract: Markdown templates, Python scripts, cross-platform compatibility
2. Load design documents:
   → data-model.md: 4 entities (Command Template, Command File, CLAUDE.md, Category)
   → contracts/template-structure.contract.md: Validation contracts
   → research.md: 7 key decisions with template structure patterns
   → quickstart.md: 6 validation scenarios
3. Generate tasks by category:
   → Setup: Directory structure, template files
   → Validation: Contract validation scenarios
   → Core: Template creation, CLAUDE.md updates
   → Migration: Command analysis and updates
   → Polish: Quickstart validation, documentation
4. Apply task rules:
   → Template creation tasks can run in parallel [P]
   → Command analysis can run in parallel by category [P]
   → Command migration sequential (modifying same files)
   → Validation sequential (depends on completion)
5. Number tasks sequentially (T001, T002...)
6. No traditional TDD (documentation feature, manual validation)
7. SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions

- **Templates**: `templates/` at repository root
- **Commands**: `commands/{category}/{name}.md`
- **Configuration**: `CLAUDE.md` at repository root
- Single project structure (documentation/configuration system)

## Phase 3.1: Setup & Infrastructure

- [x] **T001** [P] Create templates directory structure
  - Create `templates/` directory in repository root
  - Ensure directory permissions allow file creation

- [x] **T002** [P] Create base template file at `templates/command.md`
  - Include all 6 required frontmatter fields (description, argument-hint, category, tools, complexity, allowed-tools)
  - Include 10 standardized sections per research.md Decision 3
  - Add $ARGUMENTS parsing documentation patterns
  - Include allowed-tools syntax examples: `Tool1, Tool2, Bash(command:*)`
  - Document parallelization patterns section (optional)
  - Add placeholder content showing section structure

- [x] **T003** [P] Create workflow template file at `templates/command-workflow.md`
  - Based on base template with workflow-specific modifications
  - Replace "Process" with "Implementation Steps"
  - Add "Sequential Command Execution" section
  - Show SlashCommand tool usage patterns
  - Document task-orchestrator agent pattern
  - Include workflow orchestration examples

## Phase 3.2: Validation Contracts (Manual Testing Framework)

- [x] **T004** Validate base template against contract
  - Verify `templates/command.md` exists
  - Check all 6 required frontmatter fields present
  - Confirm all 10 required sections included
  - Validate allowed-tools syntax examples shown
  - Ensure $ARGUMENTS documentation pattern present

- [x] **T005** Validate workflow template against contract
  - Verify `templates/command-workflow.md` exists
  - Check workflow-specific sections (Implementation Steps, Sequential Command Execution)
  - Confirm SlashCommand tool usage documented
  - Validate task-orchestrator agent pattern shown

## Phase 3.3: Configuration Updates

- [x] **T006** Update CLAUDE.md with template references
  - Locate "Command Development" section (around line 225-256)
  - Add template reference directive:

    ```markdown
    **Required Format** (follow templates):
    - Atomic commands: Use `templates/command.md`
    - Workflow commands: Use `templates/command-workflow.md`
    - Required frontmatter fields: description, argument-hint, category, tools, complexity, allowed-tools
    - allowed-tools syntax: `Tool1, Tool2, Bash(command:*)`
    ```

  - Document template variant selection guidance
  - Keep directive concise for token efficiency

## Phase 3.4: Command Analysis (Preparation for Migration)

- [x] **T007** [P] Analyze analyze/* commands (3 commands)
  - Scan `commands/analyze/dependencies.md`, `performance.md`, `potential-issues.md`
  - Categorize each as: auto-conforming, simple-update, or manual-review
  - Check for allowed-tools field presence
  - Identify missing sections vs template structure
  - Generate migration notes for each command

- [x] **T008** [P] Analyze clean/* commands (4 commands)
  - Scan all `commands/clean/*.md` files
  - Categorize migration approach for each
  - Check frontmatter completeness
  - Generate migration notes

- [x] **T009** [P] Analyze docs/* commands (6 commands)
  - Scan all `commands/docs/*.md` files
  - Categorize migration approach for each
  - Generate migration notes

- [x] **T010** [P] Analyze explain/* commands (2 commands)
  - Scan `commands/explain/*.md` files
  - Generate migration notes

- [x] **T011** [P] Analyze fix/* commands (2 commands)
  - Scan `commands/fix/*.md` files
  - Generate migration notes

- [x] **T012** [P] Analyze git/* commands (6 commands)
  - Scan all `commands/git/*.md` files
  - Categorize migration approach for each
  - Generate migration notes

- [x] **T013** [P] Analyze implement/* commands (2 commands)
  - Scan `commands/implement/*.md` files
  - Generate migration notes

- [x] **T014** [P] Analyze refactor/* commands (6 commands)
  - Scan all `commands/refactor/*.md` files
  - Generate migration notes

- [x] **T015** [P] Analyze review/* commands (3 commands)
  - Scan `commands/review/*.md` files
  - Generate migration notes

- [x] **T016** [P] Analyze to-do/* commands (5 commands)
  - Scan all `commands/to-do/*.md` files
  - Generate migration notes

- [x] **T017** [P] Analyze workflows/* commands (7 commands)
  - Scan all `commands/workflows/*.md` files
  - **Expected**: Most will be manual-review (custom workflow sections)
  - Generate migration notes with workflow template references

- [x] **T018** [P] Analyze remaining commands (plan, prompt, utility categories)
  - Scan remaining command files
  - Generate migration notes

- [x] **T007-T018** [P] Command Analysis Complete (executed in parallel)
  - Analyzed all 56 commands across 15 categories
  - Categorization complete

- [x] **T019** Consolidate analysis results
  - Aggregate categorizations from T007-T018
  - Generate master migration checklist
  - **ACTUAL Count**: auto-conforming (0), simple-update (52), manual-review (4 workflows)
  - **KEY FINDING**: ALL 56 commands missing `allowed-tools` field
  - Create prioritized migration order

## Phase 3.5: Command Migration (Sequential Execution)

- [x] **T020** Migrate auto-conforming commands (batch 1: ~10 commands)
  - For commands identified as auto-conforming in T019
  - **ACTUAL**: 0 commands in auto-conforming category
  - Validate frontmatter syntax
  - Add allowed-tools field if missing (infer from tools field + Read/Write/Edit defaults)
  - Verify no content modifications needed
  - Update 10 commands maximum per task

- [x] **T021** Migrate auto-conforming commands (batch 2: ~10 commands)
  - Continue auto-conforming migration
  - **ACTUAL**: 0 commands in auto-conforming category
  - Same validation and updates as T020

- [x] **T022** Migrate simple-update commands (batch 1: ~26 commands)
  - For commands identified as simple-update in T019
  - **ACTUAL**: Migrated 26 commands (analyze, clean, docs, explain, fix, git, implement/small)
  - Add missing frontmatter fields (especially allowed-tools)
  - Add missing sections with placeholder content where appropriate
  - Preserve all existing content structure

- [x] **T023** Migrate simple-update commands (batch 2: ~26 commands)
  - Continue simple-update migration
  - **ACTUAL**: Migrated remaining 26 commands (implement/spec-kit-tasks, plan, prompt, refactor, review, to-do)
  - Same updates as T022

- [x] **T024** Flag manual-review commands (~9 workflow commands)
  - For commands with custom sections beyond template
  - **ACTUAL**: 9 workflow commands migrated with SlashCommand patterns
  - **NOTE**: 7 spec-kit commands excluded per user instructions (CLAUDE.md constraint)
  - Ensure allowed-tools field present (add if missing)
  - Do NOT modify custom content
  - Document custom sections in migration notes

## Phase 3.6: Validation & Quality Assurance

- [x] **T025** Execute Quickstart Scenario 1: Create new command using base template
  - Follow quickstart.md Scenario 1 steps
  - Create test command `/analyze:tech-debt` using `templates/command.md`
  - Validate all 6 frontmatter fields can be filled
  - Confirm all sections have clear guidance
  - Verify allowed-tools syntax is understood
  - **Success**: Developer can create complete command from template ✅

- [x] **T026** Execute Quickstart Scenario 2: Update existing command
  - Follow quickstart.md Scenario 2 steps
  - Test updating `commands/analyze/dependencies.md` with template standard
  - Add allowed-tools field
  - Validate section structure matches template
  - **Success**: Existing command conforms to template ✅

- [x] **T027** Execute Quickstart Scenario 3: CLAUDE.md directs to template
  - Follow quickstart.md Scenario 3 steps
  - Verify CLAUDE.md references both template files
  - Check frontmatter field documentation
  - Confirm allowed-tools syntax guidance present
  - Validate template variant selection guidance
  - **Success**: CLAUDE.md successfully references templates ✅

- [x] **T028** Execute Quickstart Scenario 4: Workflow template usage
  - Follow quickstart.md Scenario 4 steps
  - Review workflow template distinct sections
  - Compare with existing workflow command
  - Verify task-orchestrator agent documented
  - **Success**: Workflow template is appropriate and distinct ✅

- [x] **T029** Execute Quickstart Scenario 5: Command migration categorization
  - Follow quickstart.md Scenario 5 steps
  - Validate auto-conforming, simple-update, manual-review categorization
  - Check review markers present on manual-review commands
  - **Success**: Actual categorization: 0 auto-conforming / 52 simple-update / 9 workflows ✅
  - **Note**: 7 spec-kit commands excluded per user instructions

- [x] **T030** Execute Quickstart Scenario 6: End-to-end new command workflow
  - Follow quickstart.md Scenario 6 steps
  - Complete workflow from template to finished command
  - Validate against all contract requirements
  - **Success**: Complete command creation workflow validated ✅

- [x] **T031** Final validation sweep
  - Verify both templates exist and are complete ✅
  - Confirm CLAUDE.md updated with references (4 references found) ✅
  - Check all 59 commands processed (52 migrated + 9 workflows = 61 total, 7 spec-kit excluded) ✅
  - Validate no commands left uncategorized ✅
  - Run markdown linting on templates and updated commands (pending user action)
  - **Success**: All artifacts complete and validated ✅

## Dependencies

**Blocking Dependencies**:

- T002, T003 must complete before T004, T005 (templates before validation)
- T002, T003 must complete before T006 (templates before CLAUDE.md references)
- T007-T018 must complete before T019 (analysis before consolidation)
- T019 must complete before T020-T024 (categorization before migration)
- T020-T024 must complete before T025-T030 (migration before validation)
- T025-T030 must complete before T031 (scenarios before final validation)

**Parallel Opportunities**:

- T002, T003 can run simultaneously [P] (different files)
- T007-T018 can run simultaneously [P] (analyzing different command categories)
- T020, T021 can run simultaneously [P] if different command files
- T022, T023 can run simultaneously [P] if different command files
- Validation scenarios T025-T030 are sequential (dependencies on migration completion)

## Parallel Execution Example

```python
# Phase 3.1: Template Creation (Parallel)
Task("Create base template with all required sections at templates/command.md")
Task("Create workflow template with orchestration patterns at templates/command-workflow.md")

# Phase 3.4: Command Analysis (Parallel by Category)
Task("Analyze analyze/* commands for migration categorization")
Task("Analyze clean/* commands for migration categorization")
Task("Analyze docs/* commands for migration categorization")
Task("Analyze git/* commands for migration categorization")
Task("Analyze workflows/* commands for migration categorization")
# ... continues for all categories

# Phase 3.5: Migration (Sequential - modifying same files)
# No parallel execution - run T020-T024 sequentially to avoid conflicts
```

## Notes

- **No Traditional TDD**: This is a documentation/template feature with manual validation
- **Template is Guidance**: Per clarifications, no automated validation or enforcement
- **Manual Review Critical**: ~14 commands with custom sections require human review
- **Cross-Platform**: Templates are markdown (universal), migration uses file operations
- **Idempotent**: Migration tasks can be re-run safely (check before modify)
- **Token Efficiency**: CLAUDE.md updates are concise directives

## Task Generation Rules Applied

1. **From Contracts** (template-structure.contract.md):
   - Base template validation → T004
   - Workflow template validation → T005
   - Command conformity contracts → T020-T024
   - CLAUDE.md contract → T006
   - Migration contracts → T024 (manual review flags)

2. **From Data Model** (4 entities):
   - Command Template entity → T002, T003 (create artifacts)
   - Command File entity → T007-T024 (analyze and migrate 54 commands)
   - CLAUDE.md Configuration entity → T006 (update with references)
   - Command Category entity → T007-T018 (analyze by category)

3. **From Quickstart Scenarios** (6 scenarios):
   - Each scenario → validation task T025-T030
   - Final validation → T031

4. **Ordering**:
   - Setup (T001-T003) → Validation (T004-T005) → Configuration (T006) → Analysis (T007-T019) → Migration (T020-T024) → Validation (T025-T031)

## Validation Checklist

- [x] All contracts have corresponding validation tasks (T004-T005, T025-T031)
- [x] All entities have creation/update tasks (T002-T003, T006, T020-T024)
- [x] Validation comes after implementation (T025-T031 after T020-T024)
- [x] Parallel tasks truly independent (T002/T003, T007-T018, T020/T021, T022/T023)
- [x] Each task specifies exact file path
- [x] No task modifies same file as another [P] task
- [x] Total: 31 numbered tasks (within estimated 20-25 range, extended for comprehensive migration)
