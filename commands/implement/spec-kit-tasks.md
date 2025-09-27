---
description: Implement features using the Agent Orchestra framework with intelligent task coordination
---

# Implement Spec-Kit Tasks - Agent Orchestra Edition

Execute spec-kit implementation using the multi-agent system with orchestrators and specialized workers.

## Architecture

This command leverages the Agent Orchestra framework:
1. **implementation-orchestrator** manages the overall flow
2. **code-writer** generates implementation code
3. **test-writer** creates comprehensive tests
4. **documenter** updates documentation
5. **reviewer** validates quality

## Execution Flow

### With Spec-Kit Context (Primary Mode)
When `.specify/` exists with spec/plan/tasks:
```
1. Delegate to /spec-kit:implement via implementation-orchestrator
2. Follow task-based implementation from tasks.md
3. Validate against spec.md requirements
4. Track progress in agent memory
```

### Without Spec-Kit Context (Fallback)
Direct implementation using Agent Orchestra:
```
1. task-orchestrator analyzes requirements
2. Spawns implementation-orchestrator for code changes
3. Sequential phases:
   - Setup: Dependencies and structure
   - Core: Business logic implementation
   - Testing: Comprehensive test suite
   - Documentation: API and user docs
   - Review: Quality validation
```

## Agent Coordination

### Phase 1: Planning
```
task-orchestrator:
  → Analyze complexity
  → Determine if spec-kit exists
  → Plan execution strategy
  → Spawn implementation-orchestrator
```

### Phase 2: Implementation
```
implementation-orchestrator (sequential):
  1. code-writer → /implement or /refactor:large-scale
  2. code-writer → Business logic
  3. test-writer → Unit and integration tests
  4. documenter → /docs:generate
  5. reviewer → /review:code
```

### Phase 3: Validation
```
Multiple agents in parallel:
  [P] reviewer → /review:code
  [P] reviewer → /review:security
  [P] test-writer → Run test suite
```

## Slash Commands Used

The orchestrator delegates to workers with these commands:
- `/spec-kit:implement` - When spec-kit context exists
- `/refactor:large-scale` - Major restructuring
- `/implement` - Feature implementation
- `/test` - Test execution
- `/docs:generate` - Documentation creation
- `/review:code` - Quality review
- `/review:security` - Security validation

## Progress Tracking

Implementation progress monitored through:
- Phase completion status
- Active worker assignments
- Modified file tracking
- Task dependency resolution

## Usage Examples

### Basic Spec-Kit Implementation
```
User: "/implement:spec-kit-tasks"
→ Detects .specify/tasks.md
→ implementation-orchestrator coordinates
→ Delegates to /spec-kit:implement
→ Follows task breakdown
→ Agent Orchestra coordinates execution
```

### Complex Feature with Spec
```
User: "/implement:spec-kit-tasks payment-integration"
→ Loads payment-integration spec
→ implementation-orchestrator plans phases
→ Multiple code-writer iterations
→ Comprehensive test-writer coverage
→ Full documentation update
```

## Benefits

1. **Intelligent Coordination**: Orchestrators manage complexity
2. **Specialized Workers**: Each agent focuses on one task
3. **Slash Command Reuse**: Leverages existing atomic commands
4. **Progress Tracking**: Memory system maintains state
5. **Quality Built-in**: Automatic testing and review

## Error Handling

If implementation fails:
1. State preserved in memory
2. Can resume from checkpoint
3. bug-fixer agent can be spawned
4. Rollback plan available

## Important Notes

- **NO automatic git operations** - Requires explicit user consent
- Primarily uses spec-kit when available
- Falls back to direct implementation if no spec
- All work tracked in agent memory
- Can be resumed if interrupted

This command represents the evolution of spec-kit implementation: from single-agent to orchestrated multi-agent execution with full slash command integration.