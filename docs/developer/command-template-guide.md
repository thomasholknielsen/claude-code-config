# Command Template Developer Guide

**Updated**: 2025-10-21
**Unified Template**: `templates/commands/command.md`

This guide contains detailed explanations, examples, and best practices for creating Claude Code commands using the unified template.

## Quick Reference

**Template Location**: `templates/commands/command.md`
**Command Directory**: `commands/{category}/{command-name}.md`
**Frontmatter Required**: `allowed-tools: [tool1, tool2, ...]`

## Template Sections Explained

### EXECUTION INSTRUCTIONS (Start Here)

This section tells Claude exactly what to do when the command runs.

**What to include:**
- Clear sentence about the command's purpose
- 3-5 specific actions Claude MUST take (the core steps)
- 2-3 anti-patterns to avoid
- No explanations—just actions

**Example:**
```markdown
## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Run all applicable linters with auto-fix enabled

**YOU MUST:**
1. ✓ Detect project languages (check package.json, pyproject.toml, etc.)
2. ✓ Identify applicable linters for each language
3. ✓ Run linters in parallel with --fix flag
4. ✓ Report results with file paths and line numbers

**YOU MUST NOT:**
- ✗ Skip running all applicable linters
- ✗ Run linters without auto-fix flag
```

### IMPLEMENTATION FLOW

Step-by-step breakdown of what happens.

**Structure:**
- Step 1: [Action]
- Step 2: [Action]
- Step 3: [Outcome]

Each step should be 1-2 sentences maximum. Include bash examples if applicable.

**Example:**
```markdown
## IMPLEMENTATION FLOW

### Step 1: Detect Project Languages
Scan for configuration files (package.json, pyproject.toml, Gemfile, etc.)

### Step 2: Run Language-Specific Linters
For each detected language, execute the appropriate linter with --fix flag

### Step 3: Report Results
Display file paths, line numbers, and what was fixed
```

### Usage

Show how to invoke the command and what arguments it takes.

**Include:**
- Command syntax with $ARGUMENTS placeholder
- Argument definitions (required vs optional)
- Example usage scenarios

### Examples

Concrete usage examples with expected output.

**Best practice:** Show 2-3 different scenarios (simple case, complex case, edge case).

### Agent Integration (CONDITIONAL)

Include only if your command delegates to domain analysts (uses Task tool to invoke agents).

**What to list:**
- Which analysts your command invokes
- What each analyst analyzes
- How results are used

**Example:**
```markdown
## Agent Integration

**Analysts Invoked:**
- security-analyst: Security vulnerability assessment
- performance-analyst: Performance bottleneck detection

**Pattern:** Analysts work in parallel, persist findings to context files, main thread synthesizes and implements changes.
```

### Parallel Orchestration (CONDITIONAL - Workflows Only)

Include only if your command coordinates multiple operations (typically `/workflows/*` commands).

**Structure:**
```
Phase 1: Parallel Analysis (independent concurrent tasks)
├─ Task: Analyst A analyzes domain X
├─ Task: Analyst B analyzes domain Y
└─ Task: Analyst C analyzes domain Z

Phase 2: Sequential Synthesis (main thread merges results)
└─ Consolidate findings, remove duplicates, prioritize by impact

Phase 3: Parallel Implementation (apply fixes concurrently)
├─ Edit file 1
├─ Edit file 2
└─ Run validation
```

**Anti-Pattern (NEVER):**
```
❌ WRONG: Task("Analyst: Fix the issues")
❌ WRONG: Task("Analyst: Apply auto-fixes")

✅ CORRECT: Task("Analyst: Analyze and identify issues")
```

**Key Rule**: Analysts provide *recommendations only*. Main thread implements all changes.

### Error Handling

Common errors and how to handle them.

**Use a table:**

| Error | Cause | Solution |
|-------|-------|----------|
| File not found | User provided invalid path | Validate path upfront, provide clear error message |
| Permission denied | Insufficient access | Check permissions, suggest running as admin/sudo if needed |
| Missing dependency | Tool not installed | Detect missing tool, provide installation instructions |

### Output Format

What Claude shows the user when done.

**Always include:**
- ✓ Clear success/failure indication (emoji or text)
- ✓ 1-2 sentence summary
- ✓ File references with line numbers if applicable
- ✓ What's next (actionable follow-up steps)

**Example:**
```markdown
✅ Linting Complete

**Results:**
- 42 issues fixed in 8 files
- 3 warnings remain in src/utils.ts (lines 12, 45, 89)

**Next Steps:**
1. Review warnings in src/utils.ts
2. Run tests to verify fixes
3. Commit changes: git commit -m "fix: apply linter auto-fixes"
```

### Interactive Prompts (CONDITIONAL)

Include only if command needs user to choose between distinct options (2-4 max).

**Format:** Table with options and outcomes

**Example:**
```markdown
| Option | Description | Outcome |
|--------|-------------|---------|
| A | Commit with default message | Creates commit with conventional format |
| B | Provide custom message | Prompts for message, validates format |
| Skip | Exit without committing | No changes made |

**User Flow:** Show table → Prompt "Your choice: _" → Validate input (A/B or Skip)
```

### Integration Points

Which commands typically run before/after this one.

**Example:**
```markdown
- **Follows**: Usually after `/git:pre-commit-review`
- **Precedes**: Usually before `git push`
- **Related**: `/git:push`, `/workflows:git`

Typical workflow: review → commit → push
```

### Quality Standards

Success criteria—how to know if the command worked.

**Template:**
- ✓ [Criterion 1]
- ✓ [Criterion 2]
- ✓ [Criterion 3]

## Best Practices

### MCP Tool Usage

**NEVER use MCP tools directly in commands:**
```
❌ WRONG: allowed-tools: [mcp__context7__get-library-docs, Bash, Task]
```

**CORRECT: Delegate to domain analysts:**
```
✅ CORRECT:
allowed-tools: [Task, Bash, Read]
Then invoke: Task("documentation-analyst: Analyze X and identify issues")
```

### Workflow Command Patterns

Workflow commands orchestrate multiple operations.

**Good Pattern:**
```markdown
Phase 1: Parallel Analysis
├─ Task: security-analyst (async)
├─ Task: performance-analyst (async)
└─ Task: code-quality-analyst (async)

Phase 2: Sequential Synthesis (waits for all Phase 1)
└─ Main thread: consolidate findings

Phase 3: Parallel Implementation (executes fixes)
├─ Edit file 1
└─ Run validation
```

**Bad Pattern (NEVER):**
```
❌ Invoke one analyst
❌ Wait for completion
❌ Invoke next analyst (sequential—defeats parallelization)
```

### Conditional Sections

Sections marked as CONDITIONAL should be included only if applicable:

- **Agent Integration**: Include only if using Task tool to invoke analysts
- **Parallel Orchestration**: Include only for `/workflows/*` commands
- **Interactive Prompts**: Include only if command needs user choice
- **Explicit Constraints**: Include only if important scope boundaries exist

If not applicable, remove the section entirely (don't leave placeholder).

### Command Size Guidelines

- **Minimal command**: 80-120 lines (simple atomic command)
- **Standard command**: 120-180 lines (typical atomic command with examples)
- **Complex command**: 180-250+ lines (workflow with multiple sections)

## Common Mistakes to Avoid

❌ **Mistake**: Using MCP tools directly in allowed-tools
✅ **Fix**: Delegate to agents instead

❌ **Mistake**: Inventing custom section structures
✅ **Fix**: Follow unified template section order

❌ **Mistake**: "You might want to..." or "Consider..."
✅ **Fix**: "YOU MUST" and "YOU MUST NOT" (be explicit)

❌ **Mistake**: Overly long explanations in template
✅ **Fix**: Point to external documentation for detailed patterns

❌ **Mistake**: Sequential analyst invocation for parallelizable work
✅ **Fix**: Use concurrent Task tool invocations for independent analysis

❌ **Mistake**: Forgetting YAML frontmatter with allowed-tools
✅ **Fix**: Always include: `---\nallowed-tools: [tools]\n---`

## Template Evolution

The unified template is optimized for:
- ✓ Clarity: Explicit "YOU MUST" requirements
- ✓ Consistency: Single template for all command types
- ✓ Token efficiency: Reduced explanatory text
- ✓ Developer experience: Clear patterns without noise

Updates to the template follow this process:
1. Constitution check (principles alignment)
2. Quality review (clarity, token efficiency, best practices)
3. Sample testing (apply to 3 representative commands)
4. Documentation update (update this guide)
5. Deployment (apply to all commands via conformance audit)

## Questions?

- **Template questions**: Review `templates/commands/command.md` comments
- **Examples**: Study existing commands in `commands/{category}/`
- **Best practices**: See sections above or existing conforming commands
- **Changes to template**: Submit via `constitution` amendment process
