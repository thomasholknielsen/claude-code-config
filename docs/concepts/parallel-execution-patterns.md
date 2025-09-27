# Parallel Execution Patterns with [P] Markers

This guide explains how to effectively use parallel execution patterns in the Agent Orchestra Framework to dramatically speed up complex workflows.

## Overview

The `[P]` marker system enables orchestrators to spawn multiple worker
agents simultaneously, reducing execution time for independent tasks from sequential processing to parallel processing.

**Key Benefits:**

- **3-5x faster** execution for complex workflows
- Better resource utilization across multiple agents
- Improved throughput for independent operations
- Maintained sequential safety for dependent operations

## Core Principles

### When to Use Parallel Execution

✅ **Always Use Parallel For:**

- Independent code reviews (security, quality, design)
- Separate file analysis or modification
- Different types of testing (unit, integration, performance)
- Research across different domains
- Documentation generation for different components

❌ **Never Use Parallel For:**

- Editing the same file
- Sequential dependencies (API → tests that use API)
- Shared state modifications
- Database schema changes that affect each other

### [P] Marker Syntax

```markdown
# Single parallel task
[P] Task description → agent-type with tools

# Multiple parallel tasks
[P] Task A → agent-type-1 with tools
[P] Task B → agent-type-2 with tools
[P] Task C → agent-type-3 with tools
```yaml

## Orchestrator-Specific Patterns

### Task Orchestrator Patterns

The task-orchestrator should **prioritize parallel execution** whenever possible:

#### Standard Code Review (5 agents parallel)

```markdown
[P] Code Quality Review → reviewer with /review:code
[P] Security Scan → reviewer with /review:security
[P] Performance Analysis → reviewer with /analyze:performance
[P] Design Review → reviewer with /review:design
[P] Dependencies Check → Task with /analyze:dependencies
```text

#### Multi-Component Implementation (4 agents parallel)

```markdown
[P] Component A → code-writer with specific scope
[P] Component B → code-writer with specific scope
[P] Utilities → code-writer with helper functions
[P] Tests → test-writer for all components
```text

#### Comprehensive Analysis (6+ agents parallel)

```markdown
[P] Existing Code Analysis → research-orchestrator
[P] External Best Practices → research-orchestrator with WebSearch
[P] Security Requirements → Task with /review:security
[P] Performance Requirements → Task with /analyze:performance
[P] Architecture Impact → Task with /explain:architecture
[P] Documentation Analysis → Task with /docs:analyze
```yaml

### Research Orchestrator Patterns

The research-orchestrator should **maximize parallel agents** for information gathering:

#### Standard Feature Research (9 agents parallel)

```markdown
# Core Implementation Research
[P] Similar implementations in codebase → Glob + Grep
[P] External best practices → WebSearch + Context7
[P] Security considerations → /review:security + WebSearch
[P] Performance implications → /analyze:performance + benchmarks
[P] Framework-specific patterns → Context7 docs

# Supporting Research
[P] Testing strategies → WebSearch + existing tests
[P] Documentation examples → /docs:analyze
[P] Error handling patterns → Grep error handling
[P] Configuration requirements → Glob config files
```text

#### Deep Bug Investigation (10 agents parallel)

```markdown
# Primary Investigation
[P] Error log analysis → Grep error patterns
[P] Code path tracing → specific modules/functions
[P] Recent changes review → git log + git blame
[P] Similar issues search → WebSearch + GitHub issues
[P] Environment analysis → config + dependencies
[P] Test failure patterns → Grep test outputs

# Secondary Investigation
[P] Performance metrics at failure → /analyze:performance
[P] Security implications → /review:security
[P] Database state analysis → Grep database logs
[P] External service issues → WebSearch service status
```yaml

### Implementation Orchestrator Patterns

The implementation-orchestrator uses **hybrid approach** - sequential for dependencies, parallel for independent validation:

#### Feature Development with Parallel Reviews

```markdown
Phase 1: Core Implementation (Sequential - File Dependencies)
  1. Data models → code-writer
  2. Business logic → code-writer (depends on models)
  3. API endpoints → code-writer (depends on business logic)

Phase 2: Testing & Documentation (Parallel - Independent)
  [P] Unit tests → test-writer
  [P] Integration tests → test-writer
  [P] Documentation → documenter
  [P] API documentation → documenter with /docs:api

Phase 3: Quality Assurance (Parallel - Independent Reviews)
  [P] Code review → reviewer with /review:code
  [P] Security review → reviewer with /review:security
  [P] Design review → reviewer with /review:design
  [P] Performance analysis → Task with /analyze:performance
  [P] Final cleanup → Task with /clean:improve-readability
```text

## Workflow Examples

### Example 1: Feature Implementation (Hybrid Pattern)

**Task**: "Implement user authentication with JWT"

**Optimal Execution**:

```markdown
Phase 1: Parallel Research (4 agents, ~2 minutes)
  [P] JWT best practices → research-orchestrator with WebSearch
  [P] Security requirements → Task with /review:security
  [P] Existing auth patterns → research-orchestrator with codebase
  [P] Performance considerations → Task with /analyze:performance

Phase 2: Sequential Implementation (3 steps, ~5 minutes)
  1. Auth models → code-writer
  2. JWT service → code-writer (depends on models)
  3. Auth middleware → code-writer (depends on service)

Phase 3: Parallel Testing & Review (5 agents, ~3 minutes)
  [P] Unit tests → test-writer
  [P] Integration tests → test-writer
  [P] Security review → reviewer with /review:security
  [P] Code review → reviewer with /review:code
  [P] Documentation → documenter
```text

**Performance Gain**: ~10 minutes parallel vs ~20 minutes sequential (50% faster)

### Example 2: Bug Investigation (Maximum Parallel)

**Task**: "Database connection timeouts in production"

**Optimal Execution**:

```markdown
Parallel Investigation (8 agents, ~3 minutes)
  [P] Database logs analysis → Grep + specific patterns
  [P] Connection pool analysis → code analysis
  [P] Recent deployment changes → git history
  [P] Similar timeout issues → WebSearch + GitHub
  [P] Database performance metrics → monitoring analysis
  [P] Network connectivity → infrastructure analysis
  [P] Application performance → /analyze:performance
  [P] Error correlation → log pattern analysis
```text

**Performance Gain**: ~3 minutes parallel vs ~24 minutes sequential (87% faster)

### Example 3: Code Review (Standard Parallel)

**Task**: "Review pull request with 15 file changes"

**Optimal Execution**:

```markdown
Parallel Review (6 agents, ~4 minutes)
  [P] Code quality & style → reviewer with /review:code
  [P] Security vulnerabilities → reviewer with /review:security
  [P] Performance impact → reviewer with /analyze:performance
  [P] Design patterns → reviewer with /review:design
  [P] Test coverage → test-writer with coverage analysis
  [P] Documentation updates → documenter with /docs:analyze
```yaml

**Performance Gain**: ~4 minutes parallel vs ~18 minutes sequential (78% faster)

## Best Practices

### 1. Maximize Parallel Opportunities

- **Default to parallel** unless dependencies exist
- Look for independent subtasks within complex operations
- Split reviews by concern (security, performance, quality)
- Separate research by domain or information source

### 2. Optimal Agent Counts

- **Simple tasks**: 1-3 agents parallel
- **Moderate tasks**: 3-6 agents parallel
- **Complex tasks**: 5-10 agents parallel
- **Research tasks**: 10+ agents parallel (research-orchestrator specialty)

### 3. Clear Task Boundaries

```markdown
# Good - Specific, non-overlapping
[P] Security vulnerabilities in auth module → reviewer with /review:security
[P] Performance bottlenecks in API layer → Task with /analyze:performance

# Bad - Overlapping scope
[P] Overall security review → reviewer
[P] General code review → reviewer
```text

### 4. Tool Assignment Strategy

- Give each parallel agent **specific tools** for their domain
- Avoid generic tool assignments that create overlap
- Use slash commands to focus agent scope

### 5. Dependency Management

```markdown
# Correct - Sequential when dependent
1. Create API endpoints → code-writer
2. Write tests that use those endpoints → test-writer

# Incorrect - Parallel when dependent
[P] Create API endpoints → code-writer
[P] Write tests for endpoints → test-writer  # Will fail - endpoints don't exist yet
```yaml

## Performance Metrics

Based on typical workflow analysis:

| Task Type | Sequential Time | Parallel Time | Improvement |
|-----------|----------------|---------------|-------------|
| Code Review | 15-20 min | 4-6 min | 70-75% faster |
| Bug Investigation | 20-30 min | 3-5 min | 80-85% faster |
| Feature Research | 25-35 min | 5-8 min | 75-80% faster |
| Complex Implementation | 45-60 min | 15-25 min | 60-65% faster |

## Common Anti-Patterns

### ❌ Sequential When Parallel Possible

```markdown
# Bad
1. Security review → reviewer
2. Code review → reviewer
3. Performance review → reviewer

# Good
[P] Security review → reviewer with /review:security
[P] Code review → reviewer with /review:code
[P] Performance review → reviewer with /analyze:performance
```text

### ❌ Parallel When Dependencies Exist

```markdown
# Bad
[P] Create database schema → code-writer
[P] Create models using schema → code-writer

# Good
1. Create database schema → code-writer
2. Create models using schema → code-writer (depends on 1)
```text

### ❌ Vague Task Boundaries

```markdown
# Bad
[P] Review the code → reviewer
[P] Check for issues → reviewer

# Good
[P] Security vulnerabilities → reviewer with /review:security
[P] Code quality & patterns → reviewer with /review:code
```

## Integration with Commands

Many workflow commands can leverage parallel execution:

- `/workflows:run-comprehensive-review` → 5-8 parallel reviewers
- `/analyze:*` commands → parallel analysis across different domains
- `/review:*` commands → parallel reviews by concern type
- `/implement:*` commands → parallel implementation + testing + documentation

## Cross-Platform Considerations

All parallel execution patterns work identically across:

- **Windows**: Full parallel agent support
- **macOS**: Full parallel agent support
- **Linux**: Full parallel agent support

The Agent Orchestra Framework handles platform differences transparently, ensuring consistent parallel execution performance across all environments.

---

Remember: **Parallel execution is your secret weapon for dramatically faster workflows**. Default to parallel patterns whenever tasks are independent,
and
watch your development velocity soar!
