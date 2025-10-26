---
description: "Intelligent agent creation with expert consultation and iterative refinement"
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, mcp__sequential-thinking__sequentialthinking
---

# Command: Create Agent

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Create new domain analyst agents with expert consultation using a generate-first workflow.

**Claude Code MUST execute this workflow:**
1. ✓ Initialize session context
2. ✓ Invoke agent-expert for design consultation and analysis
3. ✓ Read design brief from context file
4. ✓ Auto-generate agent file from template with expert recommendations
5. ✓ Present generation summary
6. ✓ Offer iteration options (Edit/Regenerate/Finalize/Cancel)
7. ✓ Update CLAUDE.md upon finalization

**Claude Code MUST NOT:**
- ✗ Prompt user before generating (generate first, then iterate)
- ✗ Skip context file updates
- ✗ Fail silently on agent generation

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create domain analyst agents via agent-expert consultation with generate-first workflow (auto-generate → present summary → iterate → finalize), read design brief from context (.agent/Session-{name}/context/agent-expert.md), fill agent-domain-specialist.md template, update CLAUDE.md Domain Analyst Framework section

**P**urpose: Enable rapid high-quality agent creation with expert recommendations as smart defaults, reduce upfront decision fatigue through show-don't-ask pattern, support iterative refinement (edit specs/regenerate/cancel), enforce domain uniqueness validation, maintain template compliance

**E**xpectation: New agent file (agents/{domain}-analyst.md) with frontmatter, core expertise, methodology, examples from expert brief, CLAUDE.md updated with agent entry, context file updated with completion status, restart instructions provided

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% template fields, Accuracy >90% expert recommendations, Relevance >85% domain validation, Efficiency <30s generation)

## Purpose

Creates agents using expert design consultation, generates with smart defaults, and provides iterative refinement options for fast, high-quality agent creation.

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


## Usage

```bash
/claude:create-agent
```

**Arguments**: None (interactive with generate-first workflow)

## Generate-First Workflow

### Philosophy

**Show → Iterate → Finalize** instead of asking permission for every decision upfront. Generate agents with expert recommendations as smart defaults, then allow users to review and refine.

### Process

1. **Initialize Session Context**

   ```bash
   python ~/.claude/scripts/session/session_manager.py current
   python ~/.claude/scripts/session/session_manager.py context_dir
   ```

2. **Invoke Agent Expert**

   ```markdown
   Task("agent-expert: User wants to create a new agent. Please analyze:
        - User's stated requirements and use cases
        - Domain uniqueness vs existing agents
        - Appropriate agent type (analyst vs specialist vs workflow)
        - Recommended naming, color coding, MCP tools
        - 2-3 realistic usage examples

        Persist complete design brief to context file for template generation.")
   ```

3. **Read Design Brief**

   ```bash
   Read: {context_dir}/agent-expert.md
   ```

4. **Automatically Generate Agent**
   - Read template: `templates/agents/agent-domain-specialist.md`
   - Fill template with expert recommendations (no confirmation prompts)
   - Include frontmatter (name, description with examples, color, model, tools)
   - Add core expertise areas from expert brief
   - Include analysis methodology section
   - Add domain-specific patterns
   - Write file: `agents/{domain}-analyst.md`

5. **Present Generation Summary**
   Display what was created:

   ```
   === Agent Generated ===

   **Agent**: {domain}-analyst
   **Type**: {Domain Analyst | Technical Specialist | Workflow Agent}
   **Location**: agents/{domain}-analyst.md

   **Specifications Used**:
   - Domain: {domain-name}
   - Color: {color}
   - Model: {model}
   - MCP Tools: {tools}

   **Core Expertise** ({count} areas):
   1. {area-1}
   2. {area-2}
   3. {area-3}

   **Usage Examples** ({count}):
   {first-example}

   **Uniqueness**: {validation-result}

   ===
   ```

6. **Offer Iteration Options**

   ```
   What would you like to do?
   (E) Edit specifications and regenerate
   (R) Regenerate with current specs
   (F) Finalize (update CLAUDE.md and complete)
   (C) Cancel and delete

   Choice [F]:
   ```

7. **Handle User Choice**

   **If Edit**:

   ```
   Which aspect would you like to change?
   1. Domain name
   2. Agent type
   3. Color
   4. MCP tools
   5. Core expertise areas
   6. Usage examples
   7. Multiple aspects

   Choice [1-7]:
   ```

   - Collect modifications
   - Regenerate agent file with updated specs
   - Return to step 5 (present summary)

   **If Regenerate**:
   - Regenerate agent file with same specs
   - Return to step 5 (present summary)

   **If Finalize**:
   - Update CLAUDE.md (add to Domain Analyst Framework)
   - Update agent-expert context (Main Thread Log)
   - Display completion message
   - End workflow

   **If Cancel**:
   - Delete generated agent file
   - Update agent-expert context (cancelled)
   - Display cancellation message
   - End workflow

8. **Completion Message** (if finalized)

   ```
   === Agent Finalized Successfully ===

   Location: agents/{domain}-analyst.md
   Type: {Domain Analyst | Technical Specialist | Workflow Agent}
   CLAUDE.md: Updated ✓

   Usage:
   The {domain}-analyst agent is now available. Claude Code will automatically
   suggest this agent when {trigger conditions from examples}.

   You can also invoke explicitly:
   Task("{domain}-analyst: {example task}")

   Next Steps:
   1. Restart Claude Code to load new agent
   2. Test agent invocation with example task
   3. Review generated file for any final adjustments

   To use in another project:
   1. Copy agents/{domain}-analyst.md to target project
   2. Update target project's CLAUDE.md
   3. Restart Claude Code

   ===
   ```

## Explicit Constraints

**IN SCOPE**: Agent file generation from expert brief, template filling (frontmatter, expertise, methodology), CLAUDE.md updates, domain uniqueness validation, iterative spec refinement (edit/regenerate), context file management
**OUT OF SCOPE**: Agent behavior implementation (agents analyze, don't execute), cross-project agent distribution, bulk agent creation, template structure modifications, agent testing/validation (restart required)

## Agent Integration

- **Domain Analysts**: Uses **agent-expert** for design consultation and validation
- **Pattern**: Expert consultation → Auto-generate → Iterate → Finalize

## Workflow Diagram

```
User Request
    ↓
Initialize Session Context
    ↓
Invoke agent-expert
    ↓
[Agent Expert Analysis]
├─ Validate uniqueness
├─ Recommend specifications
├─ Craft usage examples
└─ Persist design brief
    ↓
Read Design Brief
    ↓
Auto-Generate Agent (with expert recommendations)
    ↓
Present Summary
    ↓
Offer Iteration Options
    ├─ Edit → Modify specs → Regenerate → Present Summary (loop)
    ├─ Regenerate → Present Summary (loop)
    ├─ Finalize → Update CLAUDE.md → Complete
    └─ Cancel → Delete file → End
```

## Benefits of Generate-First Workflow

✅ **Faster Iteration**: No upfront confirmation prompts - just generate and review
✅ **Better UX**: Show don't ask - users see results immediately
✅ **Smart Defaults**: Expert recommendations used as defaults
✅ **Flexible Refinement**: Easy to iterate on any aspect
✅ **Lower Friction**: Reduce decision fatigue with good defaults
✅ **Same Quality**: Expert validation happens upfront
✅ **Learnable**: Users see what good agents look like immediately

## Examples

### Example 1: Quick Generation with Defaults

```text
User: /claude:create-agent
User: "I need an agent for Kubernetes analysis"

Command: [Initializes session, invokes agent-expert]

Agent-Expert: [Analyzes and persists design brief]

Command: [Auto-generates kubernetes-analyst.md]

=== Agent Generated ===

**Agent**: kubernetes-analyst
**Type**: Domain Analyst (analysis-only)
**Location**: agents/kubernetes-analyst.md

**Specifications Used**:
- Domain: kubernetes-analyst
- Color: blue (infrastructure category)
- Model: inherit
- MCP Tools: Context7 (for K8s documentation)

**Core Expertise** (3 areas):
1. Pod and container orchestration patterns
2. Helm chart design and deployment strategies
3. Cluster operations and troubleshooting

**Usage Examples** (3):
Task("kubernetes-analyst: Analyze deployment manifests for best practices")

**Uniqueness**: ✓ Validated (no overlap)

===

What would you like to do?
(E) Edit specifications and regenerate
(R) Regenerate with current specs
(F) Finalize (update CLAUDE.md and complete)
(C) Cancel and delete

Choice [F]:

User: F

[Updates CLAUDE.md, completes]

=== Agent Finalized Successfully ===
Location: agents/kubernetes-analyst.md
Type: Domain Analyst
CLAUDE.md: Updated ✓
===
```

### Example 2: Iteration Before Finalizing

```text
User: /claude:create-agent
User: "Create an agent for GraphQL API analysis"

Command: [Generates graphql-api-rest-analyst.md automatically]

=== Agent Generated ===

**Agent**: graphql-api-rest-analyst
**Type**: Domain Analyst
**Location**: agents/graphql-api-rest-analyst.md

**Specifications Used**:
- Domain: graphql-api-rest-analyst
- Color: green
- MCP Tools: Context7

**Core Expertise** (3 areas):
1. GraphQL schema design and validation
2. Query optimization and N+1 detection
3. Resolver performance analysis

===

Choice [F]: E

Which aspect would you like to change?
1. Domain name
2. Agent type
3. Color
4. MCP tools
5. Core expertise areas
6. Usage examples
7. Multiple aspects

Choice: 5

Current expertise areas:
1. GraphQL schema design and validation
2. Query optimization and N+1 detection
3. Resolver performance analysis

Enter new expertise areas (one per line, empty line to finish):
User: GraphQL schema design and federation patterns
User: Query optimization and caching strategies
User: Resolver performance and batching
User: Security and authentication in GraphQL APIs
User: [empty line]

[Regenerates with updated expertise areas]

=== Agent Generated ===

**Agent**: graphql-api-rest-analyst
**Core Expertise** (4 areas):
1. GraphQL schema design and federation patterns
2. Query optimization and caching strategies
3. Resolver performance and batching
4. Security and authentication in GraphQL APIs

===

Choice [F]: F

[Finalizes]
===
```

### Example 3: Preventing Overlap

```text
User: /claude:create-agent
User: "I want to create an agent for Python code quality"

Command: [Invokes agent-expert]

Agent-Expert: [Detects overlap, provides recommendations]

Command: [Reads design brief showing overlap warning]

=== Agent Design Brief ===
Expert Analysis:
- Recommended: Use existing code-python-analyst + code-quality-analyst
- Uniqueness: ⚠️  Overlaps with:
  * code-python-analyst (Python code analysis)
  * code-quality-analyst (code quality assessment)

Recommendation: The combination of code-python-analyst and code-quality-analyst
already covers Python code quality. Consider using existing agents.
===

Continue with agent creation? (y/N): N

Agent creation cancelled. Use existing agents:
- code-python-analyst for Python-specific analysis
- code-quality-analyst for code quality metrics
```

## Iteration Options Detail

### Edit Specifications

**Available for editing**:

1. **Domain name**: Change agent name and filename
2. **Agent type**: Switch between Domain Analyst / Technical Specialist / Workflow Agent
3. **Color**: Change UI color coding
4. **MCP tools**: Add/remove Context7, Playwright, Shadcn
5. **Core expertise areas**: Modify list of expertise domains
6. **Usage examples**: Update example scenarios

**Process**:

- Select aspect to edit
- Provide new value(s)
- System regenerates agent file
- Present updated summary
- Return to iteration options

### Regenerate

- Useful if template or generation logic updated
- Regenerates file with same specifications
- Preserves all current settings

### Finalize

**Actions performed**:

1. Read CLAUDE.md
2. Add agent to appropriate Domain Analyst Framework section
3. Update agent-expert context (Main Thread Log)
4. Display completion message with usage instructions

**CLAUDE.md Update**:

```markdown
**{Category}:** ..., {new-agent}
```

**Agent-Expert Context Update**:

```markdown
### {timestamp}
**Completed**: Agent finalized - {domain}-analyst.md
**Specifications Used**: {summary}
**CLAUDE.md Updated**: Added to {section}
```

### Cancel

**Actions performed**:

1. Delete generated agent file
2. Update agent-expert context (cancelled status)
3. Display cancellation message

## Error Handling

### Session Context Not Available

```text
Error: Could not initialize session context.

Solution:
1. Initialize session manually:
   /session:start agent-creation "Agent creation workflow"

2. Re-run /claude:create-agent
```

### Agent-Expert Not Available

```text
Error: agent-expert not found in agents/ directory.

Solution:
1. Verify agent-expert.md exists in agents/ directory
2. Restart Claude Code to load new agents
3. If missing, restore from repository
```

### Template Not Found

```text
Error: templates/agents/agent-domain-specialist.md not found.

Solution:
1. Verify template exists in templates/agents/ directory
2. Check working directory is project root
3. Restore template from repository if missing
```

### Generation Fails

```text
Error: Failed to generate agent file.

Solution:
1. Check design brief in .agent/Session-{name}/context/agent-expert.md
2. Verify template is valid
3. Check file permissions for agents/ directory
4. Try regenerating with (R) option
```

## Notes

- **Generate-First**: No confirmation prompts before generation
- **Smart Defaults**: Expert recommendations used automatically
- **Fast Iteration**: Easy to try different approaches
- **Flexible**: Can edit any aspect before finalizing
- **Reversible**: Cancel option deletes generated file
- **Session Context**: Uses context for expert coordination
- **Restart Required**: Claude Code must restart to load new agent

## See Also

- `templates/agents/agent-domain-specialist.md` - Template structure
- `agents/agent-expert.md` - Design consultation agent
- `CLAUDE.md` - Domain Analyst Framework documentation
- `/claude:create-command` - Command creation with same workflow
