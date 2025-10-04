---
description: "Quick implementation for small tasks bypassing spec-kit, using focused Agent Specialist Framework coordination"
argument-hint: "[arguments]"
category: "implement"
tools: ["Task", "SlashCommand", "TodoWrite"]
complexity: "moderate"
allowed-tools: Task, SlashCommand, TodoWrite
---

# Command: Small

## Purpose

Quick implementation for small tasks bypassing spec-kit, using focused Agent Specialist Framework coordination with streamlined research and rapid execution.

## Usage

```bash
/implement:small $ARGUMENTS
```

**Arguments**:

- `$1` (task-description): Brief description of small task to implement
- `$2` (--type): Task type hint (bug, feature, refactor, test) (optional)
- `$3` (--scope): Scope limitation for small task (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "fix login error message"` - Simple bug fix task
- `$ARGUMENTS = "add email validation helper --type=feature"` - Small feature addition
- `$ARGUMENTS = "extract duplicate code in utils.js --type=refactor"` - Minor refactoring task

## Process

### Phase 1: Rapid Parallel Research (Focused Context Gathering)

1. **Parse Task Description**: Extract task details and type hints from $ARGUMENTS
2. **Targeted Information Gathering**: Launch focused Task() agents for essential context:
   - Relevant code patterns and existing implementations
   - Dependencies and integration points
   - Testing requirements and conventions
   - Documentation standards

### Phase 2: Quick Planning

1. **Fast Strategy Formation**: Synthesize research into implementation approach
2. **Resource Determination**: Identify which specialist agent is most appropriate
3. **Scope Validation**: Ensure task remains within "small" complexity bounds

### Phase 3: Direct Implementation

1. **Specialist Execution**: Delegate to appropriate execution specialist (code-writer, bug-fixer, test-writer)
2. **Quality Check**: Quick validation of functionality and integration
3. **Minimal Documentation**: Update only essential documentation if needed

## Agent Integration

- **Specialist Options**: implementation-strategy-specialist can be spawned to coordinate small task implementation with minimal overhead
- **Research Phase**: Launches focused Task() agents for rapid context gathering
- **Execution Phase**: Delegates to single specialist (code-writer, bug-fixer, or test-writer)
- **Validation**: Minimal quality checks appropriate for small task scope

## Examples

### Quick Bug Fix

```yaml
User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "fix login error message"

# Rapid Research Phase
→ implementation-strategy-specialist launches:
  → Task("Find existing error message patterns")
  → Task("Locate login-related code structure")
  → Task("Check testing conventions for error cases")

# Direct Implementation
→ Identifies as bug fix
→ Spawns bug-fixer with context
→ Fix applied with proper error handling
→ Quick validation test
```

### Small Feature Addition

```yaml
User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "add email validation helper"

# Focused Research Phase
→ Task("Analyze existing validation utilities")
→ Task("Review email validation requirements")
→ Task("Check testing patterns for utilities")

# Implementation
→ Spawns code-writer for utility function
→ Spawns test-writer for validation tests
→ Updates utility exports and documentation
```

### Minor Refactoring

```yaml
User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "extract duplicate code in utils.js"

# Quick Analysis
→ Task("Identify duplication patterns in utils.js")
→ Task("Review existing extraction conventions")

# Refactor Execution
→ Spawns code-writer with /refactor:extract-functions
→ Applies DRY principles
→ Updates imports and references
→ Validates functionality preserved
```

### API Endpoint Addition

```yaml
User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "add GET /api/user/profile endpoint"

# Research Phase
→ Task("Analyze existing API patterns and middleware")
→ Task("Review authentication requirements")
→ Task("Check API testing conventions")
→ Task("Identify database query patterns")

# Implementation
→ Spawns code-writer for endpoint implementation
→ Spawns test-writer for API tests
→ Updates API documentation
→ Validates with integration test
```
