---
description: "Identify complex code blocks and extract them into well-named functions for better readability"
category: "refactor"
agent: "code-writer"
tools: ["Read", "Edit", "Bash"]
complexity: "moderate"
---

# Extract Functions

I'll identify complex code blocks and extract them into well-named functions for better readability and maintainability.

Arguments: `$ARGUMENTS` - files, directories, or specific code areas to refactor

## What I Look For

**Complex code patterns:**
- Long functions (>20 lines)
- Nested logic blocks
- Repeated code patterns
- Complex conditional statements
- Code with multiple responsibilities

**Magic numbers and strings:**
- Hardcoded values that should be constants
- Configuration values embedded in logic
- Repeated literal values

## Extraction Strategy

**Function extraction:**
- Extract logical units into named functions
- Create meaningful function names that describe purpose
- Maintain parameter clarity and return types
- Preserve existing behavior exactly

**Constant extraction:**
- Replace magic numbers with named constants
- Group related constants together
- Use descriptive naming conventions

## Validation Process

**Behavior preservation:**
- Run existing tests to ensure no breakage
- Verify edge cases still work correctly
- Check that extracted functions handle all input scenarios
- Maintain exact same output for same input

**Code quality improvements:**
- Better readability through clear function names
- Easier testing of individual components
- Reduced cognitive load when reading code
- Improved reusability of extracted logic

Quick, focused function extraction without complex session management.