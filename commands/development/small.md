---
description: "Quick implementation for small tasks bypassing spec-kit, using focused Agent Specialist Framework coordination"
argument-hint: "[arguments]"
allowed-tools: Task, TodoWrite
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

1. **Domain Analysis**: Invoke appropriate domain analysts for implementation guidance (quality-analyst, testing-analyst, language-specific analysts)
2. **Quality Check**: Quick validation of functionality and integration
3. **Minimal Documentation**: Update only essential documentation if needed

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned to coordinate small task implementation with minimal overhead
- **Research Phase**: Launches focused Task() agents for rapid context gathering
- **Domain Analysis**: Invokes domain analysts for implementation guidance:
  - quality-analyst - for code quality assessment
  - testing-analyst - for test strategy recommendations
  - Language-specific analysts (python-analyst, typescript-analyst, react-analyst) based on context
- **Validation**: Minimal quality checks appropriate for small task scope

## Examples

### Quick Bug Fix

```bash
# User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "fix login error message"

# Rapid Research Phase
# → architecture-analyst launches:
#   → Task("Find existing error message patterns")
#   → Task("Locate login-related code structure")
#   → Task("Check testing conventions for error cases")

# Direct Implementation
# → Identifies as bug fix
# → Invokes quality-analyst for code analysis
# → Fix applied with proper error handling
# → Quick validation test
```

### Small Feature Addition

```bash
# User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "add email validation helper"

# Focused Research Phase
# → Task("Analyze existing validation utilities")
# → Task("Review email validation requirements")
# → Task("Check testing patterns for utilities")

# Implementation
# → Invokes quality-analyst for utility function design
# → Invokes testing-analyst for validation test strategy
# → Updates utility exports and documentation
```

### Minor Refactoring

```bash
# User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "extract duplicate code in utils.js"

# Quick Analysis
# → Task("Identify duplication patterns in utils.js")
# → Task("Review existing extraction conventions")

# Refactor Execution
# → Invokes refactoring-analyst for refactoring strategy
# → Applies DRY principles
# → Updates imports and references
# → Validates functionality preserved
```

### API Endpoint Addition

```bash
# User: "/implement:small $ARGUMENTS"
# where $ARGUMENTS = "add GET /api/user/profile endpoint"

# Research Phase
# → Task("Analyze existing API patterns and middleware")
# → Task("Review authentication requirements")
# → Task("Check API testing conventions")
# → Task("Identify database query patterns")

# Implementation
# → Invokes api-analyst for endpoint design analysis
# → Invokes testing-analyst for API test strategy
# → Updates API documentation
# → Validates with integration test
```
