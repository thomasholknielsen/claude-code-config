---
description: "Launch research with automatic mode detection"
argument-hint: "\"research question\" [--context-dir=path]"
allowed-tools: Task, Bash
---

# Command: Auto Research

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Launch research-web-analyst with automatic mode detection based on question complexity.

**YOU MUST:**
1. ✓ Get session context directory
2. ✓ Parse research question
3. ✓ Invoke research-web-analyst with **Research Mode**: auto (or omit for auto-detection)
4. ✓ Display summary with detected mode

**YOU MUST NOT:**
- ✗ Force a specific mode (let agent auto-detect)

---

## EXECUTE THIS NOW

**You MUST execute this workflow immediately:**

1. ✓ Get context dir: `python ~/.claude/scripts/session/session_manager.py context_dir`
2. ✓ Extract question
3. ✓ Invoke research-web-analyst:
   ```
   Task(
     subagent_type="research-web-analyst",
     description="Auto research: {question}",
     prompt="Research Question: {question}

     **Research Mode**: auto

     **Context File Location**: {context_dir}/research-web-analyst.md"
   )
   ```
4. ✓ Display summary

---

## USAGE

```bash
/research:auto "Compare GraphQL and REST APIs"
```

**Arguments:**
- `question` (required): Research question (any complexity)
- `--context-dir` (optional): Override context directory

---

## EXAMPLES

**Example: Auto-Detected Standard Mode**
```bash
/research:auto "Compare GraphQL and REST APIs"
```

**Output:**
```
## Web Research Analysis Complete

**Research Mode**: standard (auto-detected: feature comparison, moderate complexity)
**Detection Signals**: "compare" keyword, feature comparison pattern
**Override Available**: Use /research:deep for comprehensive analysis

**Queries Executed**: 3 query variations
**Sources Consulted**: 8 (6 authoritative)
...
```

---

**Example: Auto-Detected Deep Mode**
```bash
/research:auto "What's the best architecture for integrating Salesforce with SQL Server?"
```

**Output:**
```
## Web Research Analysis Complete

**Research Mode**: deep (auto-detected: architecture + integration keywords, multi-domain synthesis)
**Detection Signals**: "architecture", "integration", requires cross-domain synthesis
...
```

---

## NEXT STEPS

| Step | Action |
|------|--------|
| **A** | Review results ← **Recommended** |
| **B** | Override with specific mode if needed |
| **C** | Execute recommendations |
