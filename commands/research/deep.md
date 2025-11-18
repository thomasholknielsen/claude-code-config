---
description: "Launch deep research with problem decomposition and evidence synthesis"
argument-hint: "\"research question\" [--context-dir=path]"
allowed-tools: Task, Bash
---

# Command: Deep Research

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Launch deep-researcher agent (minimal Skill-based agent) for complex architecture decisions and multi-domain synthesis questions.

**YOU MUST:**
1. ✓ Get current session context directory
2. ✓ Parse research question from $ARGUMENTS
3. ✓ Invoke deep-researcher agent (forces websearch-deep Skill loading)
4. ✓ Provide explicit context file path to agent
5. ✓ Display lean summary to user when complete

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Use research-web-analyst (use deep-researcher instead)
- ✗ Forget to provide context file path

---

## EXECUTE THIS NOW

**You MUST execute this research workflow immediately using the Task tool:**

1. ✓ Get session context directory: `python ~/.claude/scripts/session/session_manager.py context_dir`
2. ✓ Extract research question from $ARGUMENTS (first quoted string or all arguments)
3. ✓ Invoke deep-researcher agent:
   ```
   Task(
     subagent_type="deep-researcher",
     description="Deep research: {question}",
     prompt="Research Question: {question}

     **Context File Location**: Save your findings to:
     {context_dir}/deep-researcher.md

     Load websearch-deep Skill immediately and follow all instructions from the Skill."
   )
   ```
4. ✓ Display agent's lean summary to user
5. ✓ Report context file location for detailed findings

Do NOT just describe what should happen - actively execute this research workflow NOW using the Task tool.

---

## IMPLEMENTATION FLOW

### Step 1: Get Session Context Directory

Get current session's context directory for file persistence:
```bash
CONTEXT_DIR=$(python ~/.claude/scripts/session/session_manager.py context_dir)
```

### Step 2: Parse Research Question

Extract research question from $ARGUMENTS:
- If quoted string: Use quoted content
- If multiple args: Combine all arguments
- If empty: Ask user for question

### Step 3: Invoke Research Agent

Launch deep-researcher with:
- **Context File Location**: {context_dir}/deep-researcher.md
- **Question**: User's research question

Agent will:
1. Load Skill("websearch-deep") IMMEDIATELY (minimal agent forces Skill usage)
2. Follow Skill's Phase 1: Decompose into 3-5 sub-questions
3. Follow Skill's Phase 2: Generate 15-25 query variations
4. Execute WebSearch with advanced operators per Skill guidance
5. Follow Skill's Phase 3: Synthesize with evidence ranking
6. Follow Skill's Phase 4: Format with numbered citations
7. Follow Skill's Phase 5: Structured output
8. Follow Skill's Phase 6: Validate completeness (max 5 iterations)
9. Return lean summary to main thread

### Step 4: Display Results

Show user:
- Research mode used (deep)
- Sub-questions analyzed
- Sources consulted count
- Key finding with citation
- Context file location for full analysis

---

## USAGE

**Invocation:**
```bash
/research:deep "What's the best architecture for integrating Salesforce with SQL Server in 2025?"
```

**Cross-Platform Note**: Claude Code handles platform differences automatically.

**Arguments:**

| Argument | Required | Description | Example |
|----------|----------|-------------|---------|
| `question` | Yes | Research question (can be quoted or unquoted) | "best architecture for X" |
| `--context-dir` | No | Override context directory path | --context-dir=.agent/custom |

**$ARGUMENTS Examples:**

- `$ARGUMENTS = "\"What's best architecture for X?\""` - Quoted question
- `$ARGUMENTS = "best practices for microservices"` - Unquoted question
- `$ARGUMENTS = ""` - Ask user for question

---

## EXAMPLES

**Example 1: Architecture Decision**

```bash
/research:deep "What's the best architecture for integrating Salesforce with SQL Server in 2025?"
```

**Process:**
1. Get context dir: `.agent/Session-2025-11-02-abc123/context/`
2. Invoke agent with deep mode
3. Agent decomposes into 5 sub-questions:
   - Salesforce integration capabilities (2025)?
   - SQL Server integration patterns?
   - Middleware options?
   - Security considerations?
   - Scalability factors?
4. Agent generates 25 queries (5 per sub-question)
5. Agent synthesizes from 18 sources
6. Agent iterates 3 times for completeness
7. Display summary to user

**Output:**
```
## Web Research Analysis Complete

**Research Mode**: deep (manually specified)
**Sub-Questions Analyzed**: 5
**Queries Executed**: 25 queries across 5 sub-questions
**Sources Consulted**: 18 (12 authoritative, 15 recent)
**Iterations**: 3 (completeness validated, gaps filled)

**Key Finding**: MuleSoft Anypoint Platform recommended for enterprise-scale Salesforce-SQL Server integration due to native connectors, real-time sync capabilities, and proven scalability [1][2][3]

**Tasks Added**:
- 3 Critical recommendations (immediate action)
- 5 Important recommendations (high priority)
- 2 Enhancements (nice-to-have)

**Quality Score**: 92/100 (CARE: C:95 A:92 R:90 E:90)

**Context File**: .agent/Session-2025-11-02-abc123/context/deep-researcher.md
```

---

**Example 2: Technology Selection**

```bash
/research:deep "Should we use microservices or monolith architecture for our e-commerce platform?"
```

**Process:**
1. Get context dir
2. Invoke agent with deep mode
3. Agent decomposes into 5 sub-questions:
   - Scalability characteristics?
   - Team size implications?
   - Transaction patterns?
   - Deployment complexity?
   - E-commerce case studies?
4. Agent synthesizes evidence with pros/cons analysis
5. Display summary with recommended approach

---

## FRAMEWORK STRUCTURE (S-TIER PATTERN)

### APE Framework (Command Orchestration)

**A**ction: Launch deep-researcher agent (minimal Skill-based agent) for complex research questions, provide explicit context file path, pass question to agent

**P**urpose: Enable ChatGPT-style deep research by forcing websearch-deep Skill loading (agent has NO built-in methodology). Skill provides problem decomposition (3-5 sub-questions), multi-query generation (15-25 total searches), evidence synthesis (credibility/freshness/relevance ranking), numbered citations, iterative refinement (max 5 iterations), keeping main thread context clean (agent returns lean 5K token summary)

**E**xpectation: Agent loads websearch-deep Skill immediately, follows ALL Skill instructions, completes deep research workflow, returns lean summary with sub-question count, source count, iteration count, key finding with citations, tasks by priority (Critical/Important/Enhancements), quality score (CARE metrics), context file reference for full analysis

## EXPLICIT CONSTRAINTS

**IN SCOPE**: Launching deep-researcher agent, providing context file path, parsing research question, displaying lean summary

**OUT OF SCOPE**: Executing research directly (agent responsibility), implementing recommendations (user/main thread responsibility), modifying Skill behavior (edit websearch-deep Skill)

## NEXT STEPS

After deep research completes, consider:

| Step | Action | Details |
|------|--------|---------|
| **A** | Review full analysis | Read context file for complete findings with evidence table and synthesis ← **Recommended** |
| **B** | Execute recommendations | Implement critical tasks identified in research |
| **C** | Standard research | Use `/research:standard` for simpler follow-up questions |
| **D** | Quick lookup | Use `/research:quick` for version checks or doc links |

What would you like to do next?

---

## TROUBLESHOOTING

**Issue 1: Session not found**
- Start a session: `/session:start research "Deep research session"`
- Or let agent create default session

**Issue 2: Agent returns minimal findings**
- Question may be too simple for deep mode
- Try `/research:standard` or `/research:auto` instead

**Issue 3: Too many sources, overwhelming**
- Deep mode designed for complex questions
- Use `/research:standard` for moderate complexity
- Use `/research:quick` for simple lookups

## INTEGRATION POINTS

- **Session Management**: Uses current session's context directory
- **Research Agent**: Delegates to deep-researcher (minimal Skill-based agent)
- **WebSearch Skills**: Agent loads websearch-deep Skill immediately (forced by minimal agent design)
- **Context Files**: Persists to `.agent/Session-{name}/context/deep-researcher.md`
