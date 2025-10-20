---
description: "<Single clear sentence describing command purpose>"
argument-hint: "[arg1] [--flag=value]"
allowed-tools: Tool1, Tool2, Bash(command:*), mcp__sequential-thinking__sequentialthinking
# CRITICAL: Commands NEVER use MCP tools directly. Always delegate to domain analysts with MCP access.
# ❌ Bad: allowed-tools: mcp__context7__get-library-docs
# ✅ Good: Invoke documentation-analyst (which has context7 tools)
---

# Command: [Action Verb] [Object]

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** [Single clear sentence explaining core purpose]

**YOU MUST:**
1. ✓ [Specific action 1] (example: "Parse argument from $ARGUMENTS")
2. ✓ [Specific action 2] (example: "Call Python script: python3 ~/.claude/scripts/...")
3. ✓ [Specific action 3] (example: "Display confirmation with results")

**YOU MUST NOT:**
- ✗ [Anti-pattern 1 to avoid] (e.g., "Do nothing silently")
- ✗ [Anti-pattern 2 to avoid] (e.g., "Skip the implementation")
- ✗ [Anti-pattern 3 to avoid] (e.g., "Use placeholder values")

---

## IMPLEMENTATION FLOW

### Step 1: [Action Name]
[Clear description of what to do]

**Example bash command (if applicable):**
```bash
command example here
```

### Step 2: [Next Action]
[Clear description]

**Details:**
- Sub-point 1
- Sub-point 2

### Step 3: [Final Action]
[Outcome or result delivery]

---

## Usage

```bash
/<category>:<command> $ARGUMENTS
```

**Arguments:**

- `arg1` (required): [Description] (e.g., task name, file path)
- `--flag1`: [Description] (optional, default: value)
- `--flag2`: [Description] (optional)

**$ARGUMENTS Examples:**

- `$ARGUMENTS = "value1"` - [Scenario 1 and outcome]
- `$ARGUMENTS = "value1 --flag=value2"` - [Scenario 2 and outcome]
- `$ARGUMENTS = ""` - [Default behavior scenario]

---

## Examples

### Example 1: [Common Use Case]

```bash
/<category>:<command> specific-args

# Expected output:
→ [What happens]
→ [Result confirmation]
```

### Example 2: [Another Use Case]

```bash
/<category>:<command> different-args

# Expected output:
→ [What happens]
→ [Result confirmation]
```

---

## Agent Integration (CONDITIONAL: Include only if command uses agents)

**If this command delegates to domain analysts:**

**Analysts Invoked:**
- [Analyst 1]: [Specific role - what analysis they perform]
- [Analyst 2]: [Specific role - what analysis they perform]

**Pattern:**
1. Analysts conduct independent analysis
2. Persist detailed findings to `.agent/context/{session-id}/{analyst-name}.md`
3. Return concise summary with actionable recommendations
4. Main thread reads context files and implements changes

**Key Constraint:** Analysts provide recommendations only - main thread implements all changes

### FOR WORKFLOW COMMANDS ONLY: Parallel Orchestration

This section applies ONLY to `/workflows/*` commands.

**Parallelization Strategy:**

```
Phase 1: Parallel Analysis (concurrent analyst invocations)
├─ Task: analyst-1 analyzes [domain] → persists findings → returns summary
├─ Task: analyst-2 analyzes [domain] → persists findings → returns summary
└─ Task: analyst-3 analyzes [domain] → persists findings → returns summary

Phase 2: Sequential Synthesis
├─ Main thread reads all context files
├─ Consolidates findings → removes duplicates → prioritizes by impact
└─ Generates unified recommendations

Phase 3: Parallel Implementation
├─ Edit/Bash: Fix issue 1 in file A
├─ Edit/Bash: Fix issue 2 in file B
└─ Bash: Run validation/tests
```

**Forbidden Pattern (NEVER do this):**
```
❌ WRONG: Task("analyst: Fix the issues")
❌ WRONG: Task("analyst: Apply auto-fixes")
✅ CORRECT: Task("analyst: Analyze X and identify issues")
```

---

## Interactive Prompts (CONDITIONAL: Include only if command needs user choice)

_Use this section if command requires interactive user input to choose between distinct execution paths (max 5 options)_

**When to Show This:**
- Command has 2-4 mutually exclusive options
- User decision significantly affects what command does
- Option details need explanation

**Format (A/B/C/D Table):**

| Option | Description | Impact |
|--------|-------------|--------|
| A | [Choice 1 description] | [Effect/outcome] |
| B | [Choice 2 description] | [Effect/outcome] |
| C | [Choice 3 description] | [Effect/outcome] |
| Skip | Exit without making changes | No changes made |

**User Flow:**
```
→ Command displays table above
→ Prompt: "Your choice: _"
→ Validate: A/B/C or Skip (case-insensitive)
→ If valid: Proceed with chosen action
→ If invalid (first time): Re-prompt
→ If invalid (second time): Default to Skip
```

---

## Error Handling

**Common Issues & Solutions:**

| Issue | Example | Solution |
|-------|---------|----------|
| [Error type 1] | User provides invalid input | Validate and re-prompt or default to safe option |
| [Error type 2] | Required file/tool missing | Check prerequisites upfront, provide clear install instructions |
| [Error type 3] | Operation fails | Provide rollback/recovery steps if applicable |

---

## Integration Points

- **Precedes**: [Commands that typically run after this one]
- **Follows**: [Commands that typically run before this one]
- **Related**: [Related commands in same domain or workflow]

**Workflow Example:**
```
/command:step1 → /command:step2 → /command:step3
```

---

## Output Format

**What User Receives:**

- ✓ Clear success/failure indication
- ✓ Summary of what was accomplished
- ✓ File references with line numbers (if applicable)
- ✓ Actionable next steps
- ✓ Execution time (if relevant)

**Example Output Structure:**

```markdown
✅ Command Complete: [Summary in 1-2 sentences]

**Results:**
- [Key outcome 1]
- [Key outcome 2]
- [Key outcome 3]

**Next Steps:**
1. [Suggested action 1]
2. [Suggested action 2]
```

---

## Explicit Constraints (CONDITIONAL: Include only if command has important scope boundaries)

### Scope Boundaries

**IN SCOPE:**
- [What this command handles]
- [Specific use cases]

**OUT OF SCOPE:**
- [What this command does NOT handle]
- [Limitations or edge cases]
- [Functionality handled by other commands]

---

## Quality Standards

**Command succeeds when:**
- ✓ Execution instructions are clear and followed
- ✓ Implementation flow steps are completed in order
- ✓ User receives clear output with next steps
- ✓ No silent failures or missing steps
- ✓ Error handling is graceful with actionable messages

**Quality Threshold:** If command completed all steps and user has clear results, success target met.
