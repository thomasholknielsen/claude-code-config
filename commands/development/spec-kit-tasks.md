---
description: "Implement features using the Agent Orchestra framework with intelligent task coordination"
argument-hint: "[arguments]"
allowed-tools: Task, TodoWrite
---

# Command: Spec Kit Tasks

## Purpose

Implements features using the Agent Orchestra framework with intelligent task coordination, executing implementation plans by processing and
executing all tasks defined in tasks.md.

## Usage

```bash
/implement:spec-kit-tasks $ARGUMENTS
```

**Arguments**:

- `$1` (feature-name): Specific feature or task set to implement (optional)
- `$2` (--parallel-research): Enable parallel research phase (optional, default)
- `$3` (--sequential-only): Force sequential implementation without parallel research (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "user-dashboard"` - Implement user dashboard feature
- `$ARGUMENTS = "--sequential-only"` - Skip parallel research phase
- `$ARGUMENTS = "authentication-system --parallel-research"` - Full parallel research for auth system

## Process

### Phase 1: Parallel Research (Information Gathering)

1. **Parse Arguments**: Extract feature name and execution mode from $ARGUMENTS
2. **Concurrent Information Gathering**: Launch parallel Task() agents to gather context:
   - Codebase architecture analysis
   - Existing patterns and conventions discovery
   - Dependency and integration requirements research
   - Design system and UI component inventory
   - Test coverage and quality standards assessment

### Phase 2: Implementation Planning

1. **Synthesis and Planning**: Consolidate research findings into implementation strategy
2. **Task Dependency Analysis**: Review tasks.md and identify execution order
3. **Resource Allocation**: Determine which specialist agents are needed

### Phase 3: Sequential Implementation

1. **Coordinated Execution**: Execute tasks in dependency order using specialist agents
2. **Quality Validation**: Run tests, linting, and verification after each major milestone
3. **Integration Testing**: Ensure all components work together correctly
4. **Documentation Updates**: Update relevant documentation to reflect changes

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned to coordinate feature implementation with parallel research and
  sequential execution
- **Research Phase**: Spawns multiple Task() agents in parallel for comprehensive context gathering
- **Implementation Phase**: Delegates to quality-analyst, testing-analyst, documenter as needed
- **Quality Assurance**: Coordinates with reviewer for validation and quality checks

## Examples

### Complex Feature Implementation

```bash
# User: "/implement:spec-kit-tasks $ARGUMENTS"
# where $ARGUMENTS = "user-dashboard-feature"

# Phase 1: Parallel Research
# → architecture-analyst launches parallel research:
#   → Task("Analyze existing authentication patterns")
#   → Task("Research UI component library usage")
#   → Task("Identify database schema requirements")
#   → Task("Review testing conventions and coverage")
#   → Task("Analyze build and deployment pipeline")

# Phase 2: Planning
# → Synthesizes research findings
# → Reviews tasks.md for implementation order
# → Creates execution strategy with dependencies

# Phase 3: Sequential Implementation
# → Spawns quality-analyst for core functionality
# → Spawns testing-analyst for comprehensive test coverage
# → Spawns documenter for API documentation
# → Coordinates integration testing
# → Validates against spec.md requirements
```

### Multi-Component Feature

```bash
# User: "/implement:spec-kit-tasks $ARGUMENTS"
# where $ARGUMENTS = "user-dashboard-feature"

# Parallel Research Phase
# → Task("Analyze existing dashboard components")
# → Task("Research user data access patterns")
# → Task("Identify shared state management approach")
# → Task("Review responsive design requirements")
# → Task("Assess performance optimization needs")

# Implementation Coordination
# → Backend API development (quality-analyst)
# → Frontend components (quality-analyst + UI patterns)
# → Database migrations (quality-analyst + schema validation)
# → Unit and integration tests (testing-analyst)
# → API documentation (documenter)
# → User guide updates (documenter)
```
