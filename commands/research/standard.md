---
description: "Launch standard research with multi-source verification"
argument-hint: "\"research question\" [--context-dir=path]"
allowed-tools: Task, Bash
---

# Command: Standard Research

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Launch research-web-analyst in standard mode for feature comparisons and moderate complexity topics.

**YOU MUST:**
1. ✓ Get session context directory
2. ✓ Parse research question from $ARGUMENTS
3. ✓ Invoke research-web-analyst with **Research Mode**: standard
4. ✓ Display lean summary to user

**YOU MUST NOT:**
- ✗ Skip mode specification
- ✗ Forget context file path

---

## EXECUTE THIS NOW

**You MUST execute this workflow immediately:**

1. ✓ Get context dir: `python ~/.claude/scripts/session/session_manager.py context_dir`
2. ✓ Extract question from $ARGUMENTS
3. ✓ Invoke research-web-analyst:
   ```
   Task(
     subagent_type="research-web-analyst",
     description="Standard research: {question}",
     prompt="Research Question: {question}

     **Research Mode**: standard

     **Context File Location**: {context_dir}/research-web-analyst.md

     Apply websearch-standard Skill for multi-source verification."
   )
   ```
4. ✓ Display summary to user

---

## USAGE

```bash
/research:standard "What are the differences between GraphQL and REST APIs?"
```

**Arguments:**
- `question` (required): Research question
- `--context-dir` (optional): Override context directory

---

## EXAMPLES

**Example: Feature Comparison**
```bash
/research:standard "GraphQL vs REST API differences"
```

**Output:**
```
## Web Research Analysis Complete

**Research Mode**: standard (manually specified)
**Queries Executed**: 3 query variations
**Sources Consulted**: 8 (6 authoritative)
**Iterations**: 2 (multi-source verification complete)

**Key Finding**: GraphQL uses single endpoint with client-specified queries, reducing over-fetching compared to REST's multiple resource endpoints [1][2][3]

**Tasks Added**:
- 2 Critical recommendations
- 3 Important recommendations
- 1 Enhancement

**Quality Score**: 88/100

**Context File**: .agent/Session-{id}/context/research-web-analyst.md
```

---

## NEXT STEPS

| Step | Action |
|------|--------|
| **A** | Review full analysis ← **Recommended** |
| **B** | Execute recommendations |
| **C** | Deep research for complex follow-up |
| **D** | Quick lookup for simple facts |
