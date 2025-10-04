
# Implementation Plan: Slash Command Template Standardization System

**Branch**: `001-i-would-like` | **Date**: 2025-10-03 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-i-would-like/spec.md`

## Execution Flow (/plan command scope)

```text
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file
   (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot,
   `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:

- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary

Create a standardized template system for slash command development in the Claude Code command repository. The template will
define required sections (frontmatter, purpose, usage, process, agent integration, examples) and enforce consistent `allowed-tools`
syntax. Update CLAUDE.md to reference the template, perform one-time migration of 54 existing commands with manual review flags
for custom sections, and optionally provide automated command creation tooling.

## Technical Context

**Language/Version**: Markdown (templates), Python 3.x (scripts - cross-platform compatibility required)
**Primary Dependencies**: Claude Code CLI, existing command structure (54 commands across 15 categories)
**Storage**: File system - markdown template files, command .md files in `commands/` hierarchy
**Testing**: Manual validation against template structure, markdown linting (.markdownlint.yml)
**Target Platform**: macOS and Windows (cross-platform requirements per CLAUDE.md)
**Project Type**: Documentation/Configuration system (single project structure)
**Performance Goals**: Template application must be idempotent, no runtime performance impact
**Constraints**: Template is guidance only (no automated validation per clarifications), manual review required for custom sections,
no auto-propagation of template updates to existing commands
**Scale/Scope**: 54 existing commands, 15 categories, template variants for different command types (base, workflow)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Agent Specialist Framework Compliance

- [x] Appropriate specialized agents identified for this feature
  - `documenter` - Template creation and structure definition (Technical Specialist)
  - `code-writer` - CLAUDE.md updates and script modifications (Technical Specialist)
  - `reviewer` - Command validation and standardization review (Technical Specialist)
- [x] Agent selection strategy documented (parallel vs sequential)
  - Phase 0: Parallel research (template patterns, frontmatter standards)
  - Phase 1: Sequential design (template → CLAUDE.md → validation approach)
  - Implementation: Sequential (template creation → existing command migration)
- [x] All agents provide advisory guidance (not direct execution)
  - Agents recommend approaches, main thread executes
  - Framework roles clearly defined per constitution

### Atomic Command Design Compliance

- [x] Feature produces atomic, single-purpose artifacts
  - Template files define standardized command structure
  - Each template has clear, predictable outcome
- [x] Template variants address different command types
  - Base template for atomic commands
  - Workflow template for orchestration commands
- [x] Integration points documented
  - Templates integrate with CLAUDE.md configuration
  - Commands reference templates for structure

### Specification-Driven Development Compliance

- [x] Spec-kit workflow followed with complete artifacts
  - `spec.md` - User requirements (WHAT/WHY, not HOW)
  - `plan.md` - Technical design and strategy
  - `contracts/` - Validation contracts
  - Clarification session completed (3 questions resolved)
- [x] Requirements are testable and unambiguous
  - Each FR has measurable outcomes
  - Validation scenarios in quickstart.md
- [x] No implementation details in spec
  - Focus on required sections and outcomes, not syntax

### Cross-Platform Compatibility Compliance

- [x] Python-based automation for cross-platform support
  - Template files are markdown (universal)
  - Migration scripts will use pathlib.Path
- [x] User-agnostic paths used
  - Templates referenced as `templates/command.md`
  - No hardcoded user directories
- [x] Works on macOS, Windows, Linux
  - Markdown templates platform-independent
  - Python scripts cross-platform compatible

### MCP Integration Compliance

- [x] MCP opportunities identified
  - N/A for this feature (documentation/template system)
  - No Context7 or Playwright integration needed
- [x] Template documentation includes MCP tool references
  - Base template shows how to document MCP tool usage
  - Examples from existing commands with MCP integration

### Git Operations Constraint Compliance

- [x] Git constraints respected
  - This feature doesn't require Git operations during implementation
  - Branch already created by spec-kit setup script
  - Final commit will use `/git:commit` command

### Quality Standards Compliance

- [x] Command quality requirements will be met
  - Templates ensure atomic design, complete documentation
  - Integration points clearly defined
- [x] System quality requirements addressed
  - Cross-platform markdown templates
  - User-agnostic path references
  - Security constraints respected

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)

```text
# Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure]
```

**Structure Decision**: Option 1 (Single project) - This is a documentation/configuration feature within an existing CLI tool
repository

## Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

## Phase 1: Design & Contracts

*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Generate contract tests** from contracts:
   - One test file per endpoint
   - Assert request/response schemas
   - Tests must fail (no implementation yet)

4. **Extract test scenarios** from user stories:
   - Each story → integration test scenario
   - Quickstart test = story validation steps

5. **Update agent file incrementally** (O(1) operation):
   - Run `.specify/scripts/bash/update-agent-context.sh claude`
     **IMPORTANT**: Execute it exactly as specified above. Do not add or remove any arguments.
   - If exists: Add only NEW tech from current plan
   - Preserve manual additions between markers
   - Update recent changes (keep last 3)
   - Keep under 150 lines for token efficiency
   - Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach

*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:

1. **Template Creation Tasks** (from contracts):
   - Create base template (`templates/command.md`) with all required sections
   - Create workflow template (`templates/command-workflow.md`) with orchestration patterns
   - Validate templates against structure contract

2. **Configuration Tasks**:
   - Update CLAUDE.md with template references in Command Development section
   - Add frontmatter field requirements
   - Document allowed-tools syntax
   - Add template variant selection guidance

3. **Command Analysis Tasks** [P]:
   - Scan all 54 commands for structure conformity
   - Categorize as: auto-conforming, simple-update, or manual-review
   - Generate migration checklist

4. **Command Migration Tasks**:
   - Auto-conforming: Validate frontmatter syntax only (~20 commands)
   - Simple-update: Add missing frontmatter fields, especially allowed-tools (~20 commands)
   - Manual-review: Add review markers for custom sections (~14 commands)

5. **Validation Tasks**:
   - Execute quickstart.md scenarios
   - Verify template usability
   - Confirm CLAUDE.md references work
   - Test new command creation workflow

**Ordering Strategy**:

1. Template creation (blocking - everything depends on this)
2. CLAUDE.md update (can parallel with template)
3. Command analysis [P] (parallel - can scan independently)
4. Command migration (sequential by category for safety)
5. Validation (final step)

**Estimated Output**: 20-25 numbered tasks in tasks.md

**Key Dependencies**:

- Templates must exist before migration begins
- Command analysis must complete before migration
- All migration before validation

**Parallelization Opportunities**:

- Template creation vs CLAUDE.md update [P]
- Command analysis across categories [P]
- Validation scenarios can run in parallel [P]

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation

*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking

*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

## Progress Tracking

*This checklist is updated during execution flow*

**Phase Status**:

- [x] Phase 0: Research complete (/plan command)
  - ✅ research.md created with 7 key decisions
  - ✅ All technical context questions resolved
  - ✅ Template structure patterns analyzed
  - ✅ Migration strategy defined
- [x] Phase 1: Design complete (/plan command)
  - ✅ data-model.md created (4 entities: Template, Command File, CLAUDE.md, Category)
  - ✅ contracts/template-structure.contract.md created
  - ✅ quickstart.md created with 6 validation scenarios
  - ✅ CLAUDE.md updated with template context
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
  - ✅ Task generation strategy documented
  - ✅ Ordering strategy with dependencies defined
  - ✅ Estimated 20-25 tasks
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:

- [x] Initial Constitution Check: PASS
  - All compliance criteria met
  - Agent-first architecture planned
  - Specification-driven approach followed
- [x] Post-Design Constitution Check: PASS
  - Design artifacts complete
  - No constitutional violations
  - Simpler approach confirmed (no automation/validation)
- [x] All NEEDS CLARIFICATION resolved
  - Clarification session completed with 3 questions
  - All research questions answered
- [x] Complexity deviations documented
  - No deviations - straightforward documentation feature

---
*Based on Constitution v2.0.0 - See `.specify/memory/constitution.md`*
