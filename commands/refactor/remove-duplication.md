---
description: "Identify and eliminate code duplication by applying DRY principles through function extraction"
category: "refactor"
agent: "code-writer"
tools: ["Grep", "Read", "Edit"]
complexity: "moderate"
---

# Remove Duplication

I'll identify and eliminate code duplication by applying DRY (Don't Repeat Yourself) principles through function extraction, parameterization, and shared utilities.

Arguments: `$ARGUMENTS` - files, modules, or directories to analyze for duplication

## Duplication Detection

**Code pattern analysis:**
- Identical or near-identical code blocks
- Similar logic with minor variations
- Repeated string literals and magic numbers
- Copy-pasted functions with slight modifications

**Structural duplication:**
- Similar class structures with minor differences
- Repeated component patterns
- Duplicate utility functions across modules
- Common error handling patterns

## DRY Strategies

**Function extraction:**
- Extract common logic into shared functions
- Parameterize differences between similar code blocks
- Create utility functions for repeated operations
- Build shared libraries for common functionality

**Configuration-driven approaches:**
- Replace hardcoded values with configuration
- Use data structures to drive similar behaviors
- Create template functions that accept variations
- Build generic handlers for similar cases

## Implementation Process

**Safe refactoring:**
- Verify behavior is identical before extraction
- Test extracted functions thoroughly
- Update all call sites consistently
- Maintain backward compatibility where needed

**Quality improvements:**
- Centralize business logic
- Reduce maintenance burden
- Improve consistency across codebase
- Enable easier testing of shared logic

Focused duplication removal with emphasis on maintainability and safety.