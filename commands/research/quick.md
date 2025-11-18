---
description: "Launch quick research for version lookups and simple definitions"
argument-hint: "\"research question\" [--context-dir=path]"
allowed-tools: Task, Bash
---

# Command: Quick Research

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Launch research-web-analyst in quick mode for fast factual lookups.

**YOU MUST:**
1. ✓ Get session context directory
2. ✓ Parse research question
3. ✓ Invoke research-web-analyst with **Research Mode**: quick
4. ✓ Display concise answer

**YOU MUST NOT:**
- ✗ Use for complex questions (use standard/deep instead)
- ✗ Skip mode specification

---

## EXECUTE THIS NOW

**You MUST execute this workflow immediately:**

1. ✓ Get context dir: `python ~/.claude/scripts/session/session_manager.py context_dir`
2. ✓ Extract question
3. ✓ Invoke research-web-analyst:
   ```
   Task(
     subagent_type="research-web-analyst",
     description="Quick research: {question}",
     prompt="Research Question: {question}

     **Research Mode**: quick

     **Context File Location**: {context_dir}/research-web-analyst.md

     Apply websearch-quick Skill for targeted lookup."
   )
   ```
4. ✓ Display answer

---

## USAGE

```bash
/research:quick "What version of React Router was released in 2025?"
```

**Arguments:**
- `question` (required): Simple factual question
- `--context-dir` (optional): Override context directory

---

## EXAMPLES

**Example: Version Lookup**
```bash
/research:quick "What version of React Router 2025?"
```

**Output:**
```
## Web Research Analysis Complete

**Research Mode**: quick (manually specified)
**Queries Executed**: 1 targeted query
**Sources Verified**: 1 authoritative source
**Iterations**: 1 (single-pass complete)

**Answer**: React Router v7.2.0 was released on March 15, 2025 [1]

**Context File**: .agent/Session-{id}/context/research-web-analyst.md
```

---

## NEXT STEPS

| Step | Action |
|------|--------|
| **A** | Use answer immediately ← **Recommended** |
| **B** | Standard research for more detail |
| **C** | Deep research for comprehensive analysis |
