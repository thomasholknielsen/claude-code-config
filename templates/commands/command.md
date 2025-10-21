---
description: "<Single clear sentence describing command purpose>"
argument-hint: "[arg1] [--flag=value]"
allowed-tools: Tool1, Tool2, Bash(command:*), mcp__sequential-thinking__sequentialthinking
# Important: Don't use MCP tools directly—delegate to domain analysts with MCP access
---

# Command: [Action Verb] [Object]

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** [Single clear sentence explaining core purpose]

**YOU MUST:**
1. ✓ [Specific action 1]
2. ✓ [Specific action 2]
3. ✓ [Specific action 3]

**YOU MUST NOT:**
- ✗ [Anti-pattern 1]
- ✗ [Anti-pattern 2]

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

**Analysts Invoked:**
- [Analyst 1]: [Role and analysis type]
- [Analyst 2]: [Role and analysis type]

**Pattern:** Analysts analyze independently, persist findings to `.agent/context/{session-id}/`, return summary. Main thread implements changes.

---

## Parallel Orchestration (CONDITIONAL: Workflows only)

*For `/workflows/*` commands coordinating multiple operations:*

```
Phase 1: Parallel Analysis → Phase 2: Synthesis → Phase 3: Parallel Implementation
```

See command-template-guide.md for detailed orchestration patterns.

---

## Interactive Prompts (CONDITIONAL: User choice between 2-4 options)

**Format:** A/B/C table with options and outcomes

| Option | Description | Outcome |
|--------|-------------|---------|
| A | [Choice 1] | [Result] |
| B | [Choice 2] | [Result] |
| Skip | Exit without changes | No changes |

**User Flow:** Display table → Prompt "Your choice: _" → Validate (A/B/C or Skip)

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
