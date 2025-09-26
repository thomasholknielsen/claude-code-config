# Agent Memory System

This directory contains the working memory and coordination artifacts for the multi-agent system.

## Directory Structure

```
.specify/agents/
├── context/          # Current execution state
│   ├── task-state.json     # Active task tracking
│   └── worker-states/      # Individual agent states
├── artifacts/        # Shared work products
│   ├── [session-id]/      # Session-specific artifacts
│   └── research/          # Research findings
└── handoffs/        # Agent-to-agent communication
    └── [task-id].md       # Task handoff documents
```

## Purpose

This memory system allows agents to:
1. **Persist state** between operations
2. **Share context** without token bloat
3. **Coordinate** complex multi-phase tasks
4. **Hand off** work between specialized agents

## Usage

### For Orchestrators
- Save task breakdown in `context/task-state.json`
- Track worker progress in `context/worker-states/`
- Store synthesized results in `artifacts/`

### For Workers
- Read task assignments from `handoffs/`
- Save work products to `artifacts/[session-id]/`
- Update status in parent's worker state file

### For Research
- Parallel findings go to `artifacts/research/[session-id]/`
- Synthesis document created after collection
- Sources tracked in `sources.json`

## Integration with Spec-Kit

This agent memory system works alongside spec-kit's feature structure:
- `.specify/features/` - Feature specifications and plans
- `.specify/agents/` - Agent coordination and memory
- `.specify/memory/` - Project constitution and patterns

Agents can read from feature specs when implementing, while maintaining their own working memory here.

## Best Practices

1. **Clean up** old session artifacts regularly
2. **Use descriptive** session and task IDs
3. **Keep artifacts small** - summarize before storing
4. **Version important** decisions in handoff documents
5. **Timestamp** all state changes for debugging

## File Formats

### task-state.json
```json
{
  "task_id": "feature-auth-2025-01-26",
  "complexity": "complex",
  "orchestrator": "implementation-orchestrator",
  "phases": ["setup", "core", "testing"],
  "current_phase": "core",
  "workers_spawned": ["code-writer", "test-writer"],
  "started": "2025-01-26T10:00:00Z",
  "updated": "2025-01-26T10:30:00Z"
}
```

### Handoff Document
```markdown
## Task Handoff: API Implementation
**From**: implementation-orchestrator
**To**: code-writer
**Task**: Implement user authentication endpoints

### Context
- Framework: Express.js
- Auth method: JWT
- Database: PostgreSQL

### Requirements
1. POST /auth/login
2. POST /auth/logout
3. GET /auth/refresh

### Constraints
- Use existing middleware
- Follow project patterns
- Include rate limiting

### Deliverables
- Implemented endpoints
- Updated routes file
- Modified files list
```

## Maintenance

This directory is managed automatically by agents. Manual cleanup may be needed for:
- Sessions older than 7 days
- Failed task artifacts
- Orphaned handoff documents