---
description: "Intelligent command creation with expert consultation and iterative refinement"
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Grep, Glob, mcp__sequential-thinking__sequentialthinking
---

# Command: Create Command

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create slash commands via command-expert consultation with generate-first workflow (auto-generate → present summary → iterate → finalize), read design brief from context (.agent/context/{session-id}/command-expert.md), select template (atomic vs workflow), fill template, update docs/command-decision-guide.md

**P**urpose: Enable rapid high-quality command creation with expert recommendations as smart defaults, enforce command uniqueness validation across all categories, support atomic vs workflow type selection, reduce upfront decision fatigue through show-don't-ask pattern, maintain template compliance

**E**xpectation: New command file (commands/{category}/{name}.md) with frontmatter, process steps, examples from expert brief, documentation updated, context file updated with completion status, restart instructions provided

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% template fields, Accuracy >90% expert recommendations, Relevance >85% uniqueness validation, Efficiency <30s generation)

## Purpose

Creates commands using expert design consultation, generates with smart defaults, and provides iterative refinement options for fast, high-quality command creation.

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
   - Select template based on expert recommendation (atomic vs workflow)
   - Read template: `templates/commands/command.md` or `command-workflow.md`
   - Fill template with expert recommendations (no confirmation prompts)
   - Include frontmatter (description, argument-hint, allowed-tools)
   - Add purpose and usage sections
   - Include process steps from expert brief
   - Add agent integration section (if workflow)
   - Include examples from expert recommendations
   - Write file: `commands/{category}/{command-name}.md`

5. **Present Generation Summary**
   Display what was created:

   ```
   === Command Generated ===

   **Command**: /{category}:{command-name}
   **Type**: {Atomic | Workflow}
   **Location**: commands/{category}/{command-name}.md

   **Specifications Used**:
   - Category: {category}
   - Type: {atomic | workflow}
   - Template: {command.md | command-workflow.md}

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

   ===
   ```

6. **Offer Iteration Options**

   ```
   What would you like to do?
   (E) Edit specifications and regenerate
   (R) Regenerate with current specs
   (F) Finalize (update documentation and complete)
   (C) Cancel and delete

   Choice [F]:
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

Commands are automatically generated with the appropriate template based on expert recommendation:

**Atomic Commands** (`command.md`):

- Single-purpose operations
- Direct tool usage
- Quick targeted execution
- CRUD operations

**Workflow Commands** (`command-workflow.md`):

- Multi-analyst coordination
- Parallel execution patterns
- Comprehensive analysis
- Cross-domain synthesis

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
1. Check design brief in .agent/context/{session-id}/command-expert.md
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

## Integration Points

**Works Well With**:

- `/claude:create-agent` - Create supporting domain analyst for workflow
- `/workflows:docs` - Update documentation after creation
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
