---
description: Rapid bug fixes without full implementation session complexity  
category: debugging
tools: Read, Edit, MultiEdit, Bash
---

# Quick Bug Fix

I'll rapidly identify and fix bugs without full implementation session complexity.

Arguments: `$ARGUMENTS` - bug description, error message, or file with issue

## Fix Categories

**Common Issues:**
- Import/export errors and missing dependencies
- Type errors and null/undefined issues
- Logic errors and off-by-one mistakes
- Configuration and environment problems

**Runtime Errors:**
- Exception handling and error boundaries
- Async/await timing and promise issues
- Memory leaks and resource cleanup
- API integration and network failures

**UI/UX Issues:**
- Layout problems and responsive design
- State management and component lifecycle
- Event handling and user interaction
- Performance and rendering issues

## Fix Process

**Rapid diagnosis:**
- Analyze error messages and stack traces
- Identify root cause from symptoms
- Check related code for similar patterns
- Validate fix scope and impact

**Targeted solution:**
- Apply minimal change to resolve issue
- Test fix in isolation
- Verify no regressions introduced
- Update related documentation if needed

**Quick validation:**
- Run affected tests immediately
- Check integration points
- Validate error resolution
- Confirm expected behavior restored

## Smart Detection

**Error pattern matching:**
- Common JavaScript/TypeScript errors
- Framework-specific issues (React, Vue, etc.)
- Database connection and query problems
- Build and deployment failures

**Context-aware fixes:**
- Consider project conventions and patterns
- Maintain code style consistency
- Preserve existing functionality
- Follow established error handling
- Check `.specify/` for feature-specific requirements and constraints

## Usage Examples

```
/quick-fix "undefined is not a function"
/quick-fix src/components/UserCard.tsx
/quick-fix "API returning 500 error"
/quick-fix "tests failing after merge"
```

Fast, focused bug resolution without session overhead or complex analysis.