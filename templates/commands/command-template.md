---
# Frontmatter Field Guide:
# - description: Single clear sentence about what this command does (max 80 chars)
#   Example: "Create a conventional commit with smart type detection"
# - argument-hint: Real example showing argument format, not placeholders
#   Example: "TASK-XXX [--status=pending|in_progress|completed]"
#   Example: "FEATURE-NAME [--scope=project|changes]"
# - allowed-tools: Comma-separated tool list, NO brackets, single line
#   Example: Task, Bash, Read, Grep, SlashCommand
#   NEVER include MCP tools directly (mcp__*) - use agents instead
description: "[Single clear sentence describing command purpose - max 80 chars]"
argument-hint: "[Real example: ARGUMENT-FORMAT [--flag=value|option]]"
allowed-tools: Tool1, Tool2, Tool3
---

# Command: [Action Verb] [Object]

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** [Single sentence explaining core purpose]

**Claude Code MUST execute this workflow:**
1. ✓ [Specific action 1 - be explicit]
2. ✓ [Specific action 2 - be explicit]
3. ✓ [Specific action 3 - be explicit]

**Claude Code MUST NOT:**
- ✗ [Anti-pattern 1]
- ✗ [Anti-pattern 2]

---

## MCP TOOL HANDLING RULES

**CRITICAL for Claude Code:**

Claude Code MUST NEVER directly invoke MCP tools (identifiers starting with `mcp__`).

**WRONG:**
```yaml
allowed-tools: mcp__context7__get-library-docs, Task, Bash
```

**CORRECT:**
```yaml
allowed-tools: Task, Bash, Read
# Then delegate MCP operations to agents:
Task("documentation-analyst: Research X and identify key points")
```

**Why**: MCP tools are token-expensive. Delegating to agents (which have MCP access) reduces token waste and improves response quality.

**Valid MCP Delegation Pattern**:
```
Invoke agent with specific analysis request
Agent returns concise findings
You read findings and execute recommended changes
```

---

## VALIDATION & PREREQUISITES

**Before executing, Claude Code MUST validate:**

- [ ] Required arguments are present and have correct format
- [ ] Required files/directories exist and are readable
- [ ] Required tools are available (git, python, etc.)
- [ ] Write permissions exist for target files
- [ ] No conflicting operations in progress

**If any validation fails**: Stop immediately and report clearly what's missing.

**Example validation:**
```bash
# Check git repository exists
git rev-parse --git-dir 2>/dev/null || exit "Not a git repository"

# Check script is executable
test -x ~/.claude/scripts/example.py || exit "Script not found or not executable"
```

---

## IMPLEMENTATION FLOW

### Step 1: [Action Name]
[Clear description of what to do - specific, not generic]

**Example command (if applicable):**
```bash
command-here with-args
```

### Step 2: [Next Action]
[Clear description - what specifically happens]

**Details:**
- Specific detail 1
- Specific detail 2

### Step 3: [Final Action]
[Outcome - what user receives at the end]

---

## USAGE

**Invocation:**
```bash
/<category>:<command> ARGUMENT-FORMAT [--flag=value]
```

**Cross-Platform Note**: Claude Code handles platform differences (Windows/macOS/Linux) automatically. Use forward slashes in paths.

**Arguments:**

| Argument | Required | Description | Example |
|----------|----------|-------------|---------|
| `arg1` | Yes | [What this argument is] | `value` |
| `--flag1` | No | [What this flag does] | `--flag1=xyz` |
| `--flag2` | No | [What this flag does] | `--flag2` |

**$ARGUMENTS Examples:**

- `$ARGUMENTS = "value1"` - [Scenario 1: What happens]
- `$ARGUMENTS = "value1 --flag=value2"` - [Scenario 2: What happens]
- `$ARGUMENTS = ""` - [Default: What happens if empty]

---

## EXAMPLES

**Example 1: [Common Use Case]**

```bash
/<category>:<command> specific-args

# Expected output:
✅ Operation Complete: [Summary]
Results:
- [Outcome 1]
- [Outcome 2]

Next Steps:
1. [Action 1]
2. [Action 2]
```

**Example 2: [Another Use Case]**

```bash
/<category>:<command> different-args

# Expected output:
✅ Operation Complete: [Summary]
Results:
- [Outcome 1]
```

---

## AGENT INTEGRATION (CONDITIONAL: Include only if using agents/Task tool)

**Analysts Invoked:**
- [Analyst Name]: [Specific role and analysis type]
- [Analyst Name]: [Specific role and analysis type]

**Execution Pattern:**
1. Spawn analysts in parallel (using Task tool)
2. Wait for all to complete
3. Read `.agent/context/{session-id}/{analyst-name}.md` files
4. Consolidate findings and prioritize by severity
5. Execute recommended changes (main thread responsibility)

**CRITICAL RULE**: Analysts provide recommendations only. Main thread implements all changes.

---


## INTERACTIVE PROMPTS (CONDITIONAL: Include only for user choice between 2-4 options)

**Use when command needs user to choose between mutually exclusive paths (max 4 mutually exclusive options + Other + Skip):**

### User Feedback Collection Table

Present options in table format with up to 4 mutually exclusive choices, plus "Other" for custom input, plus "Skip" to exit:

| Option | Action | Description | Outcome |
|--------|--------|-------------|---------|
| **A** | [Action name] | [Choice 1 description] | [Result] |
| **B** | [Action name] | **Recommended: [Why]** | [Result] |
| **C** | [Action name] | [Choice 3 description] | [Result] |
| **Other** | Custom | Describe what you want | Execute custom path |
| Skip | Exit | No changes | Exit without modifications |

**CRITICAL RULES for Interactive Prompts:**
1. ✓ Always show exactly ONE "Recommended" option (bold with explanation)
2. ✓ Include "Other" option if custom input makes sense for your command
3. ✓ Always include "Skip" option to exit without changes
4. ✓ Display table BEFORE prompting for input
5. ✓ Present prompt as: `Your choice (A/B/C/Other/Skip): _`
6. ✓ Accept input case-insensitive (a, A, b, B, etc.)
7. ✓ Validate input (first attempt: re-prompt if invalid; second attempt: default to Skip)
8. ✓ After user selects, confirm choice before executing: "Proceeding with Option B..."

### Next Steps Table (ALWAYS REQUIRED)

After completing the command, ALWAYS end with suggested next actions in identical table format:

| Option | Action | Description | Command/Details |
|--------|--------|-------------|-----------------|
| **A** | [Next action] | [Description] | `command` or [steps] |
| **B** | [Next action] | Recommended if: [condition] | `command` or [steps] |
| **C** | [Next action] | [Description] | `command` or [steps] |
| **Other** | Custom | Describe what you need | User specifies |

**CRITICAL RULES for Next Steps:**
1. ✓ Always provide 2-4 concrete next actions (never just 1)
2. ✓ Include specific commands (e.g., `/git:commit "msg"`) or detailed steps
3. ✓ Include "Other" option to allow custom follow-up
4. ✓ Mark one option as "Recommended if: [condition]" for guidance
5. ✓ Tables make it scannable and actionable
6. ✓ Never end command without suggesting what to do next

### Example Pattern

```markdown
## Your Choice

| Option | Action | Description | Outcome |
|--------|--------|-------------|---------|
| **A** | Full workflow | Apply all recommendations | 15-20 min, comprehensive |
| **B** | Critical only | **Recommended: Faster, focuses on critical issues** | 5-10 min |
| **C** | Review plan | Show detailed plan first | Preview before changes |
| **Other** | Custom | Describe specific scope | Targeted approach |
| Skip | Exit | No changes | Exit now |

Your choice (A/B/C/Other/Skip): _

# [After user selection and execution completes]

## Next Steps

| Option | Action | Description | Command |
|--------|--------|-------------|---------|
| **A** | Review changes | Examine what was modified | `git diff` |
| **B** | Commit changes | **Recommended: Create git commit** | `/git:commit "message"` |
| **C** | Push & PR | Create pull request | `/git:push` then `/git:pr "title"` |
| **Other** | Custom | What you need next | Describe your next step |
```

**User Flow:**
1. Display user feedback table with up to 4 mutually exclusive options + Other + Skip
2. Mark ONE option as "**Recommended: ...**" (bold)
3. Prompt: `Your choice (A/B/C/Other/Skip): _`
4. Validate input (case-insensitive): A, B, C, Other, or Skip
5. If invalid (first time): Re-prompt with "Invalid. Choose A/B/C/Other/Skip: _"
6. If invalid (second time): Default to Skip with message "Defaulting to Skip"
7. Confirm choice: "Proceeding with Option B (Critical Only)..."
8. Execute selected path
9. Display "Next Steps" table with 2-4 actionable options
10. End with suggestion: "What would you like to do next? Choose from the table above or describe your next step."

---

## ERROR HANDLING

**Errors that might occur and how to handle them:**

| Error Scenario | Likely Cause | Solution |
|----------------|-------------|----------|
| [Error 1 name] | [Why it happens] | [How to recover or report] |
| [Error 2 name] | [Why it happens] | [How to recover or report] |
| [Error 3 name] | [Why it happens] | [How to recover or report] |

**General Error Handling Rules:**
- Always validate inputs before processing
- Provide clear error messages with actionable next steps
- Never silently fail
- Offer rollback steps if operation is destructive

---

## OUTPUT FORMAT

**Claude Code MUST always provide clear output with these components:**

✅ **Success indicator** - Emoji or explicit text (✅ Complete, ⚠️ Warning, etc.)
✅ **Summary** - 1-2 sentences what was accomplished
✅ **Results** - Bullet list of specific outcomes achieved
✅ **File references** - With line numbers (format: `file:line`)
✅ **User Feedback Table** (if choices needed) - Present options before requesting input
✅ **Next Steps Table** (ALWAYS REQUIRED) - 2-4 actionable options in table format
✅ **Closing suggestion** - Ask what user wants to do next

**Pattern for Commands WITHOUT User Choices:**
```markdown
✅ Command Complete: [1-2 sentence summary]

**Results:**
- [Outcome 1]
- [Outcome 2 - include file:line if relevant]
- [Outcome 3]

## Next Steps

| Option | Action | Description | Command |
|--------|--------|-------------|---------|
| **A** | [Next action] | [Description] | `command` or steps |
| **B** | [Next action] | Recommended if: [condition] | `command` or steps |
| **C** | [Next action] | [Description] | `command` or steps |
| **Other** | Custom | What you need next | Describe your needs |

What would you like to do next? Choose from the table above or describe your next step.
```

**Pattern for Commands WITH User Choices:**
```markdown
## Your Choice

| Option | Action | Description | Outcome |
|--------|--------|-------------|---------|
| **A** | [Choice 1] | [Description] | [Result] |
| **B** | [Choice 2] | **Recommended: [Why]** | [Result] |
| **C** | [Choice 3] | [Description] | [Result] |
| **Other** | Custom | Describe what you want | Custom path |
| Skip | Exit | No changes | Exit now |

Your choice (A/B/C/Other/Skip): _

# [After user selection and execution]

✅ Command Complete: [1-2 sentence summary]

**Results:**
- [Outcome 1 from selected path]
- [Outcome 2]

## Next Steps

| Option | Action | Description | Command |
|--------|--------|-------------|---------|
| **A** | [Next action] | [Description] | `command` |
| **B** | [Next action] | **Recommended:** [Why] | `command` |
| **C** | [Next action] | [Description] | `command` |
| **Other** | Custom | What you need next | Describe |

What would you like to do next?
```

---

## ROBUSTNESS & CONSTRAINTS

**IN SCOPE:**
- [What this command handles]
- [Specific use case 1]
- [Specific use case 2]

**OUT OF SCOPE:**
- [What this command does NOT handle]
- [Limitations or edge cases]
- [Functionality delegated to other commands]

**Atomic Operations:**
- [This command handles/should complete X as atomic unit]
- [If validation fails, nothing is modified]
- [No partial states]

**Cross-Platform Compatibility:**
- Command works on: Windows, macOS, Linux
- Python execution: Use `python` (not `python3`)
- Paths: Use forward slashes `/` (Claude Code translates for platform)
- Shell commands: Use Bash syntax (works cross-platform via WSL/Git Bash on Windows)

---

## INTEGRATION POINTS

- **Follows**: [Commands typically run before this one]
- **Precedes**: [Commands typically run after this one]
- **Related**: [Related commands in same workflow]

**Workflow Example:**
```
/category:step1 → /category:step2 → /category:step3
```

---

## QUALITY STANDARDS

**Command succeeds when:**
- ✓ All validation checks pass before execution
- ✓ Each step in IMPLEMENTATION FLOW completes successfully
- ✓ User receives clear output with results and next steps
- ✓ No silent failures or skipped steps
- ✓ Error messages are clear and actionable
- ✓ All operations are atomic (complete or fail cleanly)
- ✓ Cross-platform compatibility maintained

**Quality Checklist:**
- [ ] Frontmatter fields are filled with real values (not placeholders)
- [ ] Each section has concrete content (not generic templates)
- [ ] Examples are realistic and runnable
- [ ] Validation rules are explicit and checkable
- [ ] Error handling covers foreseeable failures
- [ ] Output format matches the specified example
- [ ] No silent failures or ambiguous instructions
- [ ] User Feedback Table (if present): Shows exactly ONE "Recommended" option
- [ ] User Feedback Table (if present): Includes "Other" option when relevant
- [ ] User Feedback Table (if present): Always includes "Skip" option
- [ ] Next Steps Table (ALWAYS): Provides 2-4 actionable options (never just 1)
- [ ] Next Steps Table (ALWAYS): Includes specific commands (e.g., `/git:commit "msg"`)
- [ ] Next Steps Table (ALWAYS): Includes "Other" option for custom follow-up
- [ ] Ends with clear question: "What would you like to do next?"
