# Research: Slash Command Template Standardization

**Feature**: 001-i-would-like
**Date**: 2025-10-03

## Research Questions

Based on Technical Context and specification requirements, investigate:

1. **Template Structure Patterns**: What are standard patterns for command documentation templates?
2. **Frontmatter Standards**: Best practices for YAML frontmatter in markdown documentation
3. **Command Categorization**: Analysis of existing 54 commands for common patterns
4. **Template Variants**: Identifying command types requiring specialized templates

## Decision 1: Template Structure Pattern

**Decision**: Use hierarchical markdown template with YAML frontmatter + standardized sections

**Rationale**:

- Existing commands already use YAML frontmatter (description, category, tools, complexity)
- Markdown provides human-readable structure while remaining machine-parsable
- Hierarchical sections (## Purpose, ## Usage, ## Process) align with existing command documentation
- YAML frontmatter enables metadata extraction for tooling without breaking readability

**Alternatives Considered**:

- JSON schema: Rejected - less human-friendly, harder to maintain
- Plain text format: Rejected - no structured metadata extraction
- Custom DSL: Rejected - adds complexity, learning curve

**Evidence from Existing Commands**:
From analysis of `/git/commit.md`, `/docs/generate.md`, `/review/code.md`:

- All use `---` delimited YAML frontmatter
- Common frontmatter fields: description, argument-hint, category, tools, complexity
- Sections present: Purpose, Usage, Process, Agent Integration, Examples, Integration Points, Quality Standards
- `$ARGUMENTS` pattern for parameter documentation
- Parallelization patterns documented where applicable

## Decision 2: Required Frontmatter Fields

**Decision**: Standardize on 6 required fields + 1 optional field

**Required**:

1. `description`: Single-sentence command purpose
2. `argument-hint`: Parameter guidance for CLI
3. `category`: Command category (analyze, docs, git, etc.)
4. `tools`: Claude Code tools used (array format)
5. `complexity`: simple | moderate | complex
6. `allowed-tools`: Permission specification (NEW - per user requirement)

**Optional**:

- Additional metadata as needed by specific command types

**Rationale**:

- Existing commands already use first 5 fields consistently
- `allowed-tools` requirement explicit in specification
- Keeps frontmatter focused on essential metadata
- Extensible for future needs

**Syntax for allowed-tools** (per user specification):

```yaml
allowed-tools: Bash(git checkout --branch:*), Bash(git add:*), Read, Write, Edit
```

## Decision 3: Template Section Structure

**Decision**: 10 standardized sections for base template

**Sections**:

1. **Frontmatter** (YAML) - Metadata
2. **Command**: Title with action verb + object pattern
3. **Purpose**: Single-sentence description
4. **Usage**: Syntax with $ARGUMENTS explanation
5. **Process**: Numbered steps showing workflow
6. **Agent Integration**: Primary agent and specialist coordination
7. **Examples**: Real usage scenarios with $ARGUMENTS values
8. **Parallelization Patterns** (optional): Task() coordination when applicable
9. **Integration Points**: Related commands (Follows, Followed by, Related)
10. **Quality Standards**: Success criteria and validation

**Rationale**:

- Derived from analysis of well-documented existing commands
- Covers functional (Purpose, Usage, Process), integration (Agent, Integration Points), and quality (Examples, Standards) aspects
- Agent Integration section critical for Agent Specialist Framework
- Parallelization patterns section addresses complex commands like `/review:code`, `/implement:small`

**Supporting Evidence**:

- `/review/code.md`: Has parallelization patterns with Task() examples
- `/implement/small.md`: Documents 3-phase approach with parallel research
- `/git/commit.md`: Shows integration points and quality standards clearly
- `/analyze/dependencies.md`: Demonstrates $ARGUMENTS parsing documentation

## Decision 4: Template Variants

**Decision**: Create 2 template variants

**Variants**:

1. **Base Template** (`templates/command.md`): Standard atomic command structure
2. **Workflow Template** (`templates/command-workflow.md`): For workflow orchestration commands

**Workflow Template Additions**:

- **Sequential Command Execution** section showing SlashCommand() calls
- **Implementation Steps** detailing orchestration logic
- Different agent: `task-orchestrator` vs specialized agents

**Rationale**:

- Clarification session confirmed need for template variants for different command types
- Workflow commands (e.g., `/workflows:run-comprehensive-review`) have different structure than atomic commands
- Workflows orchestrate other commands rather than performing direct work
- Approximately 7 workflow commands vs 47 atomic commands

**Evidence**:

- `/workflows/run-comprehensive-review.md` shows distinct pattern:
  - Lists commands being orchestrated
  - Shows sequential execution with SlashCommand tool
  - Uses `task-orchestrator` agent vs specialized agents
  - Has "Implementation Steps" instead of "Process"

## Decision 5: CLAUDE.md Integration Approach

**Decision**: Add template reference directive in "Command Development" section

**Integration Point**:

```markdown
### Command Development

**Required Format** (follow `templates/command.md` for atomic commands, `templates/command-workflow.md` for workflows):
- Use base template for single-purpose atomic operations
- Use workflow template for commands that orchestrate other slash commands
- All commands must include required frontmatter fields
- Follow `allowed-tools` syntax: `Tool1, Tool2, Bash(command:*)`
```

**Rationale**:

- CLAUDE.md already has "Command Development" section
- Directive is clear and actionable
- References both template variants
- Includes critical syntax requirements
- Minimal token overhead

**Alternative Rejected**:

- Separate TEMPLATES.md file: Adds indirection, Claude might not discover it

## Decision 6: Command Migration Strategy

**Decision**: Manual review-based migration with categorization

**Categories for Review**:

1. **Auto-conforming**: Commands already matching template structure (estimated ~20)
2. **Simple updates**: Missing sections but no custom content (estimated ~20)
3. **Manual review**: Custom sections beyond template (estimated ~14 workflows + edge cases)

**Process**:

1. Scan all 54 commands for structure conformity
2. Categorize each command
3. Auto-conforming: Validate frontmatter syntax only
4. Simple updates: Add missing sections with placeholder guidance
5. Manual review: Flag with comment markers for human review

**Rationale**:

- Clarification session confirmed: flag custom sections for manual review
- Preserves valuable custom content in workflow commands
- Balances automation (efficiency) with safety (preserve intent)
- Respects principle: template is guidance, not enforcement

## Decision 7: Command Creation Automation (OPTIONAL)

**Decision**: Defer to post-MVP implementation

**Rationale**:

- Marked as optional (FR-008 SHOULD vs MUST)
- Core value is in template + CLAUDE.md reference
- Creation automation adds complexity without critical value
- Can be added later if adoption shows need

**If Implemented Later**:

- Slash command: `/create:command [category] [name]`
- Prompts for: description, arguments, complexity
- Generates file from template with pre-filled frontmatter
- Opens in editor for completion

## Research Summary

**All Technical Context questions resolved**:

- ✅ Template structure: YAML frontmatter + hierarchical markdown sections
- ✅ Frontmatter standards: 6 required fields + allowed-tools syntax
- ✅ Template variants: Base + Workflow templates
- ✅ CLAUDE.md integration: Directive in Command Development section
- ✅ Migration strategy: Categorized manual review approach
- ✅ Command creation: Deferred as optional

**No NEEDS CLARIFICATION markers remain**

**Ready to proceed to Phase 1: Design & Contracts**
