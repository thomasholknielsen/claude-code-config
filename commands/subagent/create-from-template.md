---
description: "Interactive agent creation wizard using standardized agent templates"
argument-hint: ""
allowed-tools: Read, Write, Edit
---

# Command: Create From Template

## Purpose

Guides users through interactive agent creation using the standardized agent template, ensuring consistency and best practices.

## Usage

```bash
/subagent:create-from-template
```

**Arguments**: None (fully interactive)

## Process

1. **Read Template**: Load `templates/agents/agent-domain-specialist.md`
2. **Interactive Prompts**: Collect agent specifications:
   - Domain name (e.g., "devops", "kubernetes", "ios")
   - Expertise areas (3-5 specific knowledge areas)
   - Analysis focus (what this analyst examines)
   - MCP tool requirements (Context7? Playwright? Neither?)
   - Color for UI (green, blue, purple, orange, yellow)
   - Model (inherit or opus for complex reasoning)
3. **Generate Agent File**: Create `agents/{domain}-analyst.md` from template
4. **Update CLAUDE.md**: Add new agent to Domain Analyst Framework section
5. **Confirm Creation**: Display agent file path and usage instructions

## Agent Integration

- **Domain Analysts**: Uses quality-analyst for validation of generated agent file
- **Pattern**: Template-based generation with validation

## Examples

### Example Interaction

```
User: /subagent:create-from-template
