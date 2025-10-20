---
description: "<Single clear sentence describing command purpose>"
argument-hint: "[arg1] [--flag=value]"
allowed-tools: Tool1, Tool2, Bash(command:*), Bash(another-cmd:*)
# CRITICAL: Commands NEVER use MCP tools directly. Always delegate to domain analysts with MCP access.
# ❌ Bad: allowed-tools: mcp__context7__get-library-docs
# ✅ Good: Invoke documentation-analyst (which has context7 tools)
# Rationale: Keeps commands focused on orchestration, leverages agent domain expertise
---

# Command: <Action Verb> <Object>

## Purpose

<Single sentence describing the primary function of this command>

## Usage

```
/<category>:<command-name> $ARGUMENTS
```

**Arguments**:

- `$1` (<name>): <Description> (optional/required)
- `$2` (<flag>): <Description> (optional)
- `$3` (<flag>): <Description> (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "value1"` - <Description of what this does>
- `$ARGUMENTS = "value1 --flag=value2"` - <Description with flag>
- `$ARGUMENTS = "--flag-only"` - <Description>

## Process

1. **Step 1**: <Clear action description>

   - <Sub-step or detail>
   - <Sub-step or detail>

2. **Step 2**: <Next action>

   - <Sub-step or detail>

3. **Step 3**: <Final outcome>
   - <Sub-step or detail>

## Agent Integration

- **Specialist Options**: <agent-name> can be spawned to <describe role and coordination>
- **Primary Agent**: <agent-name> - <Role description>
- **Coordination**: <How agent coordinates with other specialists if applicable>

**Coordination Pattern Guidance:**

- **Thread Absorption**: Does this command absorb main thread capabilities, or restrict via `allowed-tools` frontmatter?

  - If unrestricted: Command has full main thread access (can parallelize, invoke agents/commands)
  - If restricted: Document specific tool permissions in `allowed-tools`

- **Agent Usage**: If this command invokes agents:

  - Agents provide advisory recommendations (not direct execution)
  - Agents must persist findings to `.artifacts/context/*.md`
  - Agents cannot reliably invoke slash commands themselves

- **Command Delegation**: If this command invokes other commands:
  - Use SlashCommand tool for delegation
  - Delegation should be final action (no post-processing after)
  - Document daisy-chain pattern if applicable

**Examples of Compliant Patterns:**

```
# Tool restriction example (frontmatter)
allowed-tools: Read, Grep, Bash(ls:*), Bash(git status)

# Agent coordination example
Agent analyzes → saves to .artifacts/context/analysis.md → reports location

# Command delegation example (daisy-chain)
SlashCommand(/next:command $ARGS)
# Command ends here - no post-processing
```

## MCP Availability Checking (If Applicable)

**Use this section if your command or its delegated agents require MCP tools**

### Checking Required MCPs

If your command depends on specific MCPs (via agents), check availability upfront:

```bash
# Example: Check if fetch MCP is available before running research-analyst

# In your command implementation:
if command_requires_mcp("fetch"):
    # Check if MCP is configured
    if not mcp_available("fetch"):
        return "❌ This command requires fetch MCP. Please run /system:setup-mcp to configure it."

# If required MCPs available, proceed
invoke_agent("research-analyst", task)
```

### Handling Agent MCP Failures

If an agent fails due to missing MCPs:

```
# Agent returns error like: "❌ Fetch MCP failed..."
# Show user clear guidance:

"Research failed due to missing external tool.
Run /system:setup-mcp to configure fetch, or proceed with local resources."
```

### Key Pattern

1. **Check upfront**: If MCPs required, verify availability BEFORE starting work
2. **Clear message**: If missing, tell user exactly which MCP is needed and how to fix it
3. **Delegate handling**: Agents handle MCP errors internally
4. **Report to user**: Display agent error messages with setup guidance if needed

### Documentation

If your command delegates to agents that use MCPs:

```markdown
## MCP Dependencies

This command delegates to:
- **research-analyst**: Uses fetch (required), markitdown (optional)
- **security-analyst**: Uses sequential-thinking (required)

If MCPs are unavailable, command will report which MCP failed and suggest setup.
```

## Interactive User Input (Optional)

_Include this section if your command requires interactive user choices_

**When to Use:**

- Command has multiple distinct execution paths
- User needs to choose between 2-5 mutually exclusive options
- Decision significantly impacts what the command will do

**Standard Format (A/B/C/D Table):**

Present options using a Markdown table:

```markdown
## How would you like to proceed?

| Option | Description                                  |
| ------ | -------------------------------------------- |
| A      | <First option description>                   |
| B      | <Second option description>                  |
| C      | <Third option description>                   |
| D      | <Fourth option (optional)>                   |
| Skip   | Exit without making changes (always include) |

Your choice: \_
```

**Implementation Guidelines:**

- Maximum 5 options (A-E), keep choices focused
- Each option must be mutually exclusive (no overlap)
- Always include "Skip" option for exit without changes
- Validate user input (A/B/C/D/Skip, case-insensitive)
- If invalid input, re-prompt once then default to Skip
- Use descriptive option text (not just "Option A")

**Benefits of A/B/C/D Format:**

- Cleaner, more scannable than numbered lists
- Letter-based options more intuitive than complex syntax (e.g., "1,3,5" or "critical+high")
- Consistent with speckit command patterns
- Table format groups related options visually
- Easy to add impact columns or additional context

**Example with Impact Column:**

```markdown
| Option | Description   | Impact              |
| ------ | ------------- | ------------------- |
| A      | Quick fix     | 3 changes, ~5 min   |
| B      | Recommended   | 10 changes, ~15 min |
| C      | Comprehensive | 20 changes, ~30 min |
| Skip   | Exit          | No changes          |

Your choice: \_
```

**Validation Example:**

```
User enters: B
→ Validated: Applying recommended fixes
→ Proceeding with 10 changes...

User enters: xyz
→ Invalid input. Please enter A, B, C, D, or Skip.
→ Your choice: _

(Second invalid input)
→ No valid selection. Defaulting to Skip.
```

## Examples

### Example 1: <Scenario Name>

```
/<category>:<command> $ARGUMENTS
# where $ARGUMENTS = "<specific values>"

# Expected behavior:
→ <What happens>
→ <Result>
```

### Example 2: <Another Scenario>

```
/<category>:<command> $ARGUMENTS
# where $ARGUMENTS = "<different values>"

# Expected behavior:
→ <What happens>
→ <Result>
```

## Parallelization Patterns (Optional)

_Include this section if the command supports parallel execution_

**Use Case**: <When parallel execution is beneficial>

```
# Example parallel task coordination
Task("Parallel task 1 description")
Task("Parallel task 2 description")
Task("Parallel task 3 description")
```

**Coordination Strategy**:

- <How tasks are coordinated>
- <Dependencies between parallel tasks>
- <Result aggregation approach>

## Integration Points

- **Follows**: <Commands that typically run before this one>
- **Followed by**: <Commands that typically run after this one>
- **Related**: <Related commands in the same domain>

## Success Criteria (S-Tier Pattern)

**Command succeeds when** (measurable outcomes):

- [ ] {Specific outcome 1} (e.g., "All linters pass with zero errors")
- [ ] {Specific outcome 2} (e.g., "Context files created for each analyst invoked")
- [ ] {Specific outcome 3} (e.g., "User receives actionable summary with clear next steps")

**Quality Metrics (CARE Framework)**:

- **C**ompleteness: >95% - Command addresses all aspects of user request
- **A**ccuracy: >90% - Outputs are factually correct and verifiable
- **R**elevance: >85% - Results align with user intent and solve stated problem
- **E**fficiency: Optimal - Completes in reasonable time with appropriate resource use

**S-Tier Threshold**: 85+ overall quality score

## Explicit Constraints (S-Tier Pattern)

### Scope Boundaries

**IN SCOPE**:

- {What this command handles}
- {Specific use cases}
- {Supported workflows}

**OUT OF SCOPE**:

- {What this command does NOT handle}
- {Edge cases or limitations}
- {Functionality handled by other commands}

### What NOT to Do

**Anti-Patterns to Avoid**:

- ❌ {Anti-pattern 1 with example} → ✅ {Correct approach}
- ❌ {Anti-pattern 2 with example} → ✅ {Correct approach}
- ❌ {Anti-pattern 3 with example} → ✅ {Correct approach}

### Pre-Execution Checklist

Before running command, verify:

- [ ] Required arguments provided (no placeholders)
- [ ] Session initialized if using context system
- [ ] User intent is clear (ask if ambiguous)
- [ ] Command is appropriate for task (not overengineered)

## Quality Standards

- **Analysis Depth**: Comprehensive examination when delegating to analysts
- **Context Persistence**: All agent findings saved to `.agent/context/{session-id}/`
- **User Communication**: Clear, concise updates with progress indicators
- **Error Handling**: Graceful failures with actionable error messages
- **Success Validation**: Verify command completed successfully before reporting
- **Anti-Pattern Avoidance**: Follow checklist above
- **Quality Threshold**: Achieve 85+ CARE score

## Format Specification (S-Tier Pattern)

**Command Output Structure**:

```json
{
  "status": "success|failure|partial",
  "summary": "1-2 sentence outcome",
  "metrics": {
    "quality_score": 92,
    "care_breakdown": { "C": 95, "A": 90, "R": 88, "E": 95 }
  },
  "details": {
    "analysts_invoked": ["agent-name-1", "agent-name-2"],
    "tasks_completed": 5,
    "tasks_pending": 0,
    "files_modified": ["file1.ts", "file2.ts"],
    "context_files": [".agent/context/{session-id}/agent-name.md"]
  },
  "next_steps": ["Recommended action 1", "Recommended action 2"],
  "execution_time": "2.3s"
}
```

**User-Facing Output** (Markdown):

```markdown
✅ Command Complete: {Summary}

**Quality Score**: 92/100 (CARE: C:95 A:90 R:88 E:95)

**Results**:

- {Key outcome 1}
- {Key outcome 2}
- {Key outcome 3}

**Context Files**: {count} analyst reports in `.agent/context/{session-id}/`

**Next Steps**:

1. {Recommended action 1}
2. {Recommended action 2}
```

## Chain-of-Thought Process (S-Tier Pattern)

**For complex multi-step commands, follow systematic approach**:

### Execution Phases

<execution>
1. **Parse & Validate**: Extract arguments → Validate inputs → Check prerequisites
2. **Invoke Agents** (if applicable): Launch in parallel → Monitor completion → Read context files
3. **Synthesize**: Consolidate findings → Deduplicate → Prioritize by impact
4. **Implement**: Execute changes → Validate results → Update context logs
5. **Report**: Generate summary → Include metrics → Provide next steps
</execution>

**Use sequential-thinking MCP for complex decision trees or multi-branch logic**

### Self-Reflection Before Completion

<reflection>
- [ ] All success criteria met?
- [ ] Quality metrics at 85+ threshold?
- [ ] User receives clear, actionable output?
- [ ] Context files updated (Main Thread Log)?
- [ ] No placeholder values in output?
- [ ] Anti-patterns avoided?
- [ ] Error handling tested?
</reflection>

## Output

**Command Produces**:

- {Primary output (files, analysis, changes)}
- {Feedback to user (summary, metrics, recommendations)}
- {Context artifacts (if agents invoked)}
- {Logs or audit trails (if applicable)}

**User Receives**:

- Clear success/failure indication with quality score
- Summary of what was accomplished
- File references with line numbers where applicable
- Actionable next steps or recommendations
- Execution time and resource usage (if relevant)
