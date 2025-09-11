---
description: Orchestrated cleanup workflow that runs multiple cleanup commands in sequence
category: workflow
tools: TodoWrite, Bash
argument-hint: [scope] [--skip-step1,step2]
---

# Orchestrated Cleanup Workflow

I'll execute a comprehensive cleanup workflow by orchestrating your existing slash commands in the optimal sequence.

Arguments: `$ARGUMENTS` - optional scope (files/directories) and skip flags

## Cleanup Orchestration

I'll run your cleanup commands in this strategic order:

**Phase 1: Safety & Preparation**
1. Create git checkpoint for rollback safety
2. Analyze scope and create execution plan

**Phase 2: Code Quality Foundation** 
3. `/fix-imports` - Resolve broken import statements
4. `/format` - Standardize code formatting

**Phase 3: Code Quality Analysis**
5. `/review` - Comprehensive code review with security analysis
6. `/refactor` - Structural improvements and optimization

**Phase 4: Project Cleanup**
7. `/cleanproject` - Remove development artifacts and temporary files

**Phase 5: Validation**
8. `/test` - Run test suite to ensure everything works
9. Final validation and status report

## Execution Strategy

**Scope handling:**
- No arguments: Full project cleanup
- File/directory arguments: Scope cleanup to specified paths
- Multiple arguments: Process each scope sequentially

**Skip functionality:**
- `--skip-imports` - Skip import fixing
- `--skip-format` - Skip code formatting  
- `--skip-review` - Skip code review
- `--skip-refactor` - Skip refactoring
- `--skip-clean` - Skip project artifact cleanup
- `--skip-test` - Skip final testing

**Error handling:**
- Stop execution on command failures
- Report which step failed and provide recovery options
- Maintain git checkpoint for safe rollback

## Implementation Process

I'll execute this workflow with full transparency:

1. **Parse arguments** to determine scope and skip flags
2. **Create todo list** tracking each orchestration step
3. **Execute commands sequentially** with progress updates
4. **Handle failures gracefully** with clear error reporting
5. **Provide summary** of what was accomplished

Each step will be marked as in-progress during execution and completed when finished.

## Safety Guarantees

**Rollback safety:**
- Git checkpoint created before any changes
- Each command runs with its own safety mechanisms
- Clear recovery instructions if issues occur

**Scope respect:**
- Commands receive appropriate scope arguments
- No unintended changes outside specified scope
- Consistent argument passing to sub-commands

**Progress transparency:**
- Todo list shows current step and progress
- Clear reporting of what each command accomplished
- Summary of entire workflow results

## Example Usage

**Full project cleanup:**
```
/cleanup
```

**Scoped cleanup:**
```
/cleanup src/components/
/cleanup UserService.ts Header.tsx
```

**Skip specific steps:**
```
/cleanup --skip-refactor
/cleanup src/ --skip-test,review
```

## Workflow Benefits

This orchestrated approach ensures:
- **Consistent execution order** - Dependencies handled correctly
- **Safety first** - Git checkpoint and error handling
- **Flexible scope** - Target specific areas or entire project  
- **Progress tracking** - Clear visibility into workflow progress
- **Time efficiency** - One command for complete cleanup

Perfect for transitioning from "working state" to "clean, production-ready code" in a single command.