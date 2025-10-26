---
description: "Intelligent command creation with expert consultation and iterative refinement"
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, mcp__sequential-thinking__sequentialthinking
---

# Command: Create Command

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Create new slash commands with expert consultation using a generate-first workflow.

**Claude Code MUST execute this workflow:**
1. ✓ Initialize session context
2. ✓ Invoke command-expert for design consultation and analysis
3. ✓ Read design brief from context file
4. ✓ Auto-generate command file from appropriate template
5. ✓ Present generation summary
6. ✓ Offer iteration options (Edit/Regenerate/Finalize/Cancel)
7. ✓ Update documentation upon finalization

**Claude Code MUST NOT:**
- ✗ Prompt user before generating (generate first, then iterate)
- ✗ Skip documentation updates
- ✗ Fail silently on command generation

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create slash commands via command-expert consultation with generate-first workflow (auto-generate → present summary → iterate → finalize), read design brief from context (.agent/Session-{name}/context/command-expert.md), select template (atomic vs workflow), fill template, update docs/command-decision-guide.md

**P**urpose: Enable rapid high-quality command creation with expert recommendations as smart defaults, enforce command uniqueness validation across all categories, support atomic vs workflow type selection, reduce upfront decision fatigue through show-don't-ask pattern, maintain template compliance

**E**xpectation: New command file (commands/{category}/{name}.md) with frontmatter, process steps, examples from expert brief, documentation updated, context file updated with completion status, restart instructions provided

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% template fields, Accuracy >90% expert recommendations, Relevance >85% uniqueness validation, Efficiency <30s generation)

## Purpose

Creates commands using expert design consultation, generates with smart defaults, and provides iterative refinement options for fast, high-quality command creation.

## User Feedback

| Option | Action | Details |
|--------|--------|---------|
| A | Default workflow | [RECOMMENDED] |
| B | Alternative approach | For different use case |
| C | Skip | Exit without changes |

Your choice (A/B/C)?

## Next Steps

| Option | Action | Command |
|--------|--------|---------|
| 1 | Review output | Check generated content |
| 2 | Iterate or refine | Run command again [RECOMMENDED] |
| 3 | Continue workflow | Proceed to next step |
| 4 | Get help | Use /claude:guru for guidance |

What would you like to do next?

---

## Quality Checklist for Commands

**Every new command MUST meet these criteria before creation:**

### Pre-Generation Checklist

Before generating a command, the command-expert must validate:

- [ ] **Purpose Clarity** (5 pts) - Clear, single-purpose responsibility (not overlapping with existing commands)
- [ ] **Naming Convention** (5 pts) - Follows slash-command format: `/category:command-name` with lowercase
- [ ] **Category Appropriate** (5 pts) - Placed in correct category (claude, docs, git, etc.)
- [ ] **Tool Permissions** (10 pts) - Only requests necessary tools, no over-permissioning
- [ ] **Documentation Complete** (15 pts) - Usage examples, process steps, expected outputs clear
- [ ] **Interactive Pattern** (15 pts) - Includes User Feedback + Next Steps tables
- [ ] **Error Handling** (10 pts) - Clear error messages and recovery paths
- [ ] **Integration Ready** (10 pts) - Compatible with existing command ecosystem
- [ ] **Atomic Design** (10 pts) - Single responsibility, composable with other commands
- [ ] **No Placeholders** (5 pts) - No TODO, dummy data, or incomplete sections

**Subtotal Pre-Generation: 90 points max**

### Post-Generation Auto-Scoring (CARE Metrics)

After command file is generated, calculate CARE score:

- **Completeness** (25 pts): All required frontmatter, sections, examples present
  - Full frontmatter (description, argument-hint, allowed-tools): +10
  - Usage section with examples: +8
  - Error handling documented: +7

- **Accuracy** (25 pts): Content matches recommendations, no errors
  - Frontmatter matches design brief: +10
  - Examples are realistic and runnable: +10
  - Tool permissions match design: +5

- **Relevance** (25 pts): Solves actual user problem, adds value
  - Purpose aligned with use case: +8
  - No duplication with existing commands: +10
  - Clear next-step guidance: +7

- **Efficiency** (15 pts): Generation quality and usability
  - Generated in <30 seconds: +5
  - File is well-formatted: +5
  - Interactive pattern quality: +5

- **Voice Authenticity** (10 pts): User-centric, clear communication
  - Clear, accessible language: +5
  - Helpful tone and guidance: +5

**Total Score: 100 points**

### Quality Gates

**Score Ranges**:
- **85-100**: Excellent - Proceed to finalize
- **75-84**: Good - Minor refinements recommended, can proceed
- **60-74**: Fair - Refinements required before finalization
- **Below 60**: Needs Work - Must iterate on design and regenerate

### Scoring Display

When presenting generation summary, include:

```
=== Quality Assessment ===

CARE Score: 87/100 (Excellent)

Breakdown:
- Completeness: 23/25
- Accuracy: 24/25
- Relevance: 24/25
- Efficiency: 12/15
- Voice Authenticity: 10/10

✓ Command meets quality standards
✓ Ready for finalization
```

**For scores 60-84**:

```
=== Quality Assessment ===

CARE Score: 72/100 (Fair - Refinements Recommended)

Breakdown:
- Completeness: 20/25 (missing error handling example)
- Accuracy: 22/25 (example output needs clarification)
- Relevance: 23/25 (purpose clear, integration could be stronger)
- Efficiency: 12/15
- Voice Authenticity: 9/10

⚠️ Recommendations:
1. Add comprehensive error handling examples
2. Clarify example outputs
3. Strengthen integration guidance

Suggested Action: Edit and regenerate

Proceed anyway? [Y/n]
```

**For scores below 60**:

```
=== Quality Assessment ===

CARE Score: 48/100 (Needs Work)

⚠️ This command does not meet quality standards.

Critical Issues:
- Missing required sections (completeness: 15/25)
- Unclear purpose and overlap with existing commands (relevance: 10/25)
- No error handling or examples (accuracy: 18/25)

Recommended Actions:
1. Return to design phase with command-expert
2. Clarify purpose and differentiate from existing commands
3. Add comprehensive documentation and examples
4. Regenerate after improvements

Abort and return to design? [Y/n]
```

---

## Usage

```bash
/claude:create-command
```

**Arguments**: None (interactive with generate-first workflow)

## Generate-First Workflow

### Philosophy

**Show → Iterate → Finalize** instead of asking permission for every decision upfront. Generate commands with expert recommendations as smart defaults, then allow users to review and refine.

### Process

1. **Initialize Session Context**

   ```bash
   python ~/.claude/scripts/session/session_manager.py current
   python ~/.claude/scripts/session/session_manager.py context_dir
   ```

2. **Invoke Command Expert**

   ```markdown
   Task("command-expert: User wants to create a new command. Please analyze:
        - User's stated requirements and use cases
        - Command uniqueness vs existing commands across all categories
        - Appropriate command type (atomic vs workflow)
        - Recommended naming, category, tool permissions
        - Process step recommendations
        - 2-3 realistic usage examples

        Persist complete design brief to context file for template generation.")
   ```

3. **Read Design Brief**

   ```bash
   Read: {context_dir}/command-expert.md
   ```

4. **Automatically Generate Command**
   - Read unified template: `templates/commands/command.md`
   - Fill template with expert recommendations (no confirmation prompts)
   - Include frontmatter (description, argument-hint, allowed-tools)
   - Add purpose and usage sections
   - Include process steps from expert brief
   - Include examples from expert recommendations
   - Write file: `commands/{category}/{command-name}.md`

4.5. **Calculate CARE Score (NEW - Quality Assurance)**
   - Auto-calculate CARE score (100 points max) based on:
     - Completeness (25): frontmatter, sections, examples
     - Accuracy (25): content matches design brief, realistic examples
     - Relevance (25): solves user problem, no duplication, clear guidance
     - Efficiency (15): generation quality, formatting
     - Voice Authenticity (10): user-centric, clear communication
   - Store score in command generation summary
   - If score < 60: Flag for design review (see Quality Gates section)
   - If score 60-84: Flag as "Fair - Refinements Recommended"
   - If score >= 85: Flag as "Excellent - Ready to Finalize"

5. **Present Generation Summary (WITH QUALITY SCORE)**
   Display what was created:

   ```
   === Command Generated ===

   **Command**: /{category}:{command-name}
   **Type**: {Atomic | Workflow}
   **Location**: commands/{category}/{command-name}.md

   **Specifications Used**:
   - Category: {category}
   - Template: command.md (unified for all commands)

   **Tool Permissions**:
   {list of allowed tools}

   **Process Steps** ({count}):
   1. {step-1}
   2. {step-2}
   3. {step-3}

   **Usage Examples** ({count}):
   /{category}:{command} {example-args}
   # Expected: {outcome}

   **Uniqueness**: {validation-result}

   === NEW: Quality Assessment ===

   **CARE Score**: {score}/100 ({rating})

   **Breakdown**:
   - Completeness: {points}/25 (frontmatter, sections, examples)
   - Accuracy: {points}/25 (content matches design, realistic examples)
   - Relevance: {points}/25 (solves problem, no duplication)
   - Efficiency: {points}/15 (generation quality, formatting)
   - Voice Authenticity: {points}/10 (user-centric, clear communication)

   **Status**: {Excellent | Good | Fair | Needs Work}
   **Recommendation**: {Proceed to finalize | Refinements recommended | Return to design}

   ===
   ```

6. **Offer Iteration Options (Quality-Aware)**

   Based on CARE score, present appropriate options:

   **If CARE Score >= 85 (Excellent)**:
   ```
   What would you like to do?
   (E) Edit specifications and regenerate
   (R) Regenerate with current specs
   (F) Finalize (update documentation and complete) ← RECOMMENDED
   (C) Cancel and delete

   Choice [F]:
   ```

   **If CARE Score 60-84 (Good/Fair)**:
   ```
   What would you like to do?
   (E) Edit specifications and refine (recommended)
   (R) Regenerate with current specs
   (F) Finalize anyway (update documentation and complete)
   (C) Cancel and delete

   ⚠️ Command scored {score}/100. Consider refinements before finalizing.

   Choice [E]:
   ```

   **If CARE Score < 60 (Needs Work)**:
   ```
   ⚠️ Command scored {score}/100 (below quality threshold of 60).

   Required Action: Return to design phase

   (D) Return to design with command-expert (recommended)
   (F) Force finalize anyway (not recommended)
   (C) Cancel and delete

   Choice [D]:
   ```

7. **Handle User Choice**

   **If Edit**:

   ```
   Which aspect would you like to change?
   1. Command name
   2. Command type (atomic vs workflow)
   3. Category
   4. Tool permissions
   5. Process steps
   6. Usage examples
   7. Multiple aspects

   Choice [1-7]:
   ```

   - Collect modifications
   - Regenerate command file with updated specs
   - Return to step 5 (present summary)

   **If Regenerate**:
   - Regenerate command file with same specs
   - Return to step 5 (present summary)

   **If Finalize**:
   - Update docs/command-decision-guide.md
   - Update command-expert context (Main Thread Log)
   - Display completion message
   - End workflow

   **If Cancel**:
   - Delete generated command file
   - Update command-expert context (cancelled)
   - Display cancellation message
   - End workflow

8. **Completion Message** (if finalized)

   ```
   === Command Finalized Successfully ===

   Location: commands/{category}/{command-name}.md
   Type: {Atomic | Workflow}
   Category: {category}
   Documentation: Updated ✓

   Usage:
   /{category}:{command-name} $ARGUMENTS

   The command is now ready to use. Example:
   {first usage example from design brief}

   Next Steps:
   1. Restart Claude Code to register new command
   2. Test command with example arguments
   3. Review generated file for any final adjustments

   To use in another project:
   1. Copy commands/{category}/{command-name}.md to target project
   2. Restart Claude Code in target project

   ===
   ```

## Explicit Constraints

**IN SCOPE**: Command file generation from expert brief, template selection (atomic/workflow), template filling (frontmatter, process, examples), docs/command-decision-guide.md updates, uniqueness validation across categories, iterative spec refinement (edit/regenerate), context file management
**OUT OF SCOPE**: Command implementation logic (delegates to agents/tools), cross-project command distribution, bulk command creation, template structure modifications, command testing (restart required)

## Agent Integration

- **Domain Analysts**: Uses **command-expert** for design consultation and validation
- **Pattern**: Expert consultation → Auto-generate → Iterate → Finalize

## Workflow Diagram

```
User Request
    ↓
Initialize Session Context
    ↓
Invoke command-expert
    ↓
[Command Expert Analysis]
├─ Validate uniqueness across all categories
├─ Recommend command type (atomic vs workflow)
├─ Suggest category, naming, tools
├─ Design process steps
└─ Craft usage examples
    ↓
Read Design Brief
    ↓
Auto-Generate Command (with expert recommendations)
    ↓
Present Summary
    ↓
Offer Iteration Options
    ├─ Edit → Modify specs → Regenerate → Present Summary (loop)
    ├─ Regenerate → Present Summary (loop)
    ├─ Finalize → Update Documentation → Complete
    └─ Cancel → Delete file → End
```

## Benefits of Generate-First Workflow

✅ **Faster Iteration**: No upfront confirmation prompts - just generate and review
✅ **Better UX**: Show don't ask - users see results immediately
✅ **Smart Defaults**: Expert recommendations used as defaults
✅ **Flexible Refinement**: Easy to iterate on any aspect
✅ **Lower Friction**: Reduce decision fatigue with good defaults
✅ **Same Quality**: Expert validation happens upfront
✅ **Learnable**: Users see what good commands look like immediately

## Examples

### Example 1: Quick Generation with Defaults

```text
User: /claude:create-command
User: "I need a command to back up configuration files"

Command: [Initializes session, invokes command-expert]

Command-Expert: [Analyzes and persists design brief]

Command: [Auto-generates system/backup-config.md]

=== Command Generated ===

**Command**: /system:backup-config
**Type**: Atomic (single-purpose operation)
**Location**: commands/system/backup-config.md

**Specifications Used**:
- Category: system
- Type: atomic
- Template: command.md

**Tool Permissions**:
Read, Write, Bash, Glob

**Process Steps** (4):
1. Use Glob to identify configuration files
2. Create timestamped backup directory
3. Copy files to backup location
4. Generate backup manifest

**Usage Examples** (2):
/system:backup-config
# Expected: Backs up default config files to .backups/

/system:backup-config --include="*.env"
# Expected: Includes additional file patterns

**Uniqueness**: ✓ Validated (no overlap)

===

What would you like to do?
(E) Edit specifications and regenerate
(R) Regenerate with current specs
(F) Finalize (update documentation and complete)
(C) Cancel and delete

Choice [F]:

User: F

[Updates documentation, completes]

=== Command Finalized Successfully ===
Location: commands/system/backup-config.md
Type: Atomic
Category: system
Documentation: Updated ✓
===
```

### Example 2: Iteration Before Finalizing

```text
User: /claude:create-command
User: "Create a command to analyze API performance"

Command: [Generates workflows/analyze-api-performance.md automatically]

=== Command Generated ===

**Command**: /workflows:analyze-api-performance
**Type**: Workflow (multi-analyst orchestration)
**Location**: commands/workflows/analyze-api-performance.md

**Specifications Used**:
- Category: workflows
- Type: workflow
- Analysts: performance-analyst, api-rest-analyst

**Process Steps** (3):
1. Launch parallel analysis (performance-analyst, api-rest-analyst)
2. Synthesize findings from context files
3. Generate consolidated performance report

===

Choice [F]: E

Which aspect would you like to change?
1. Command name
2. Command type (atomic vs workflow)
3. Category
4. Tool permissions
5. Process steps
6. Usage examples
7. Multiple aspects

Choice: 5

Current process steps:
1. Launch parallel analysis (performance-analyst, api-rest-analyst)
2. Synthesize findings from context files
3. Generate consolidated performance report

Enter new process steps (one per line, empty line to finish):
User: Launch parallel analysis (performance-analyst, api-rest-analyst, security-analyst)
User: Wait for analyst completion and read context files
User: Identify critical performance bottlenecks
User: Generate prioritized optimization recommendations
User: [empty line]

[Regenerates with updated process steps]

=== Command Generated ===

**Command**: /workflows:analyze-api-performance
**Process Steps** (4):
1. Launch parallel analysis (performance-analyst, api-rest-analyst, security-analyst)
2. Wait for analyst completion and read context files
3. Identify critical performance bottlenecks
4. Generate prioritized optimization recommendations

===

Choice [F]: F

[Finalizes]
===
```

### Example 3: Preventing Overlap

```text
User: /claude:create-command
User: "Create a command to run all linters with auto-fix"

Command: [Invokes command-expert]

Command-Expert: [Detects overlap, provides recommendations]

Command: [Reads design brief showing overlap warning]

=== Command Design Brief ===
Expert Analysis:
- Recommended: Use existing /lint:correct-all
- Uniqueness: ❌ Overlaps with:
  * /lint:correct-all (detects languages, runs linters with auto-fix)
  * /workflows:run-cleanup-workflow (comprehensive cleanup including linting)

The existing /lint:correct-all command already provides:
- Automatic language detection
- Parallel linter execution
- Auto-fix support for all detected languages

===

Continue with command creation? (y/N): N

Command creation cancelled. Use existing commands:
- /lint:correct-all for comprehensive linting
- /workflows:run-cleanup-workflow for full codebase cleanup
```

## Iteration Options Detail

### Edit Specifications

**Available for editing**:

1. **Command name**: Change command name and filename
2. **Command type**: Switch between atomic and workflow
3. **Category**: Change command category
4. **Tool permissions**: Modify allowed-tools list
5. **Process steps**: Update command execution steps
6. **Usage examples**: Modify example scenarios

**Process**:

- Select aspect to edit
- Provide new value(s)
- System regenerates command file
- Present updated summary
- Return to iteration options

### Regenerate

- Useful if template or generation logic updated
- Regenerates file with same specifications
- Preserves all current settings

### Finalize

**Actions performed**:

1. Read docs/command-decision-guide.md
2. Add command to appropriate category section
3. Update command-expert context (Main Thread Log)
4. Display completion message with usage instructions

**Documentation Update**:

```markdown
## {Category} Commands

### /{category}:{command-name}
{description}
**Use when**: {use case}
```

**Command-Expert Context Update**:

```markdown
### {timestamp}
**Completed**: Command finalized - {category}/{command-name}.md
**Specifications Used**: {summary}
**Documentation Updated**: Added to command-decision-guide.md
```

### Cancel

**Actions performed**:

1. Delete generated command file
2. Update command-expert context (cancelled status)
3. Display cancellation message

## Command Name Rules

**Kebab-case format**: lowercase with hyphens

**Good Names**:

- /system:create-todo
- /workflows:run-comprehensive-review
- /system:backup-config
- /github:create-issue

**Bad Names**:

- /system:createTodo (camelCase)
- /system:Create_TODO (mixed case)
- /system:runtests (missing hyphens)
- /SYSTEM:CREATE-TODO (uppercase)

## Template Selection

All commands use the unified template `command.md` which supports:

- Single-purpose atomic operations (most common)
- Multi-analyst coordination patterns (via Task tool)
- Parallel execution and synchronization
- Interactive user feedback and next steps

## Error Handling

### Session Context Not Available

```text
Error: Could not initialize session context.

Solution:
1. Initialize session manually:
   /session:start command-creation "Command creation workflow"

2. Re-run /claude:create-command
```

### Command-Expert Not Available

```text
Error: command-expert not found in agents/ directory.

Solution:
1. Verify command-expert.md exists in agents/ directory
2. Restart Claude Code to load new agents
3. If missing, restore from repository
```

### Template Not Found

```text
Error: templates/commands/{template}.md not found.

Solution:
1. Verify template exists in templates/commands/ directory
2. Check working directory is project root
3. Restore template from repository if missing
```

### Generation Fails

```text
Error: Failed to generate command file.

Solution:
1. Check design brief in .agent/Session-{name}/context/command-expert.md
2. Verify template is valid
3. Check file permissions for commands/ directory
4. Try regenerating with (R) option
```

### Documentation Update Fails

```text
Error: Could not update docs/command-decision-guide.md.

Solution:
1. Manually add command to docs/command-decision-guide.md
2. Find appropriate category section
3. Add entry following existing pattern
```

## Next Steps

After creating your command, here are recommended follow-up actions:

| Option | Action | Command |
|--------|--------|---------|
| A | Test the new command ← Recommended | Restart Claude Code, then: `/{category}:{command-name} [args]` |
| B | Create supporting agent if needed | `/claude:create-agent` |
| C | Update documentation | `/docs:sync --scope=changes` |
| D | Commit the new command | `/git:commit "feat: add {category}:{command-name} command"` |

**Recommended workflow**: Restart Claude Code to register the new command, test it with the examples from the design brief, then commit with `/git:commit`.

---

## Integration Points

**Works Well With**:

- `/claude:create-agent` - Create supporting domain analyst for workflow
- `/docs:sync` - Update documentation after creation
- `/git:commit` - Commit new command file

**Follows Well**:

- Command system planning and design discussions
- Template customization or updates
- Command refactoring initiatives

## Notes

- **Generate-First**: No confirmation prompts before generation
- **Smart Defaults**: Expert recommendations used automatically
- **Fast Iteration**: Easy to try different approaches
- **Flexible**: Can edit any aspect before finalizing
- **Reversible**: Cancel option deletes generated file
- **Session Context**: Uses context for expert coordination
- **Restart Required**: Claude Code must restart to register new command

## See Also

- `templates/commands/command.md` - Atomic command template
- `templates/commands/command.md` - Workflow command template
- `agents/command-expert.md` - Design consultation agent
- `docs/command-decision-guide.md` - Command usage guide
- `CLAUDE.md` - Command system documentation
- `/claude:create-agent` - Agent creation with same workflow
