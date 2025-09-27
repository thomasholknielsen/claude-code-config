---
description: "Execute comprehensive refactoring workflow by orchestrating atomic refactor commands in optimal sequence"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand", "Read", "Write"]
complexity: "complex"
---

# Run Refactor Workflow

I'll execute a comprehensive refactoring workflow by orchestrating atomic refactor commands in optimal sequence for maximum code improvement.

Arguments: `$ARGUMENTS` - files, directories, or scope with optional skip flags

## Refactoring Orchestration

I'll run refactoring commands in this strategic order:

**Phase 1: Foundation Cleanup**
1. `/refactor:remove-duplication` - Eliminate code duplication first to avoid refactoring the same logic multiple times
2. `/refactor:extract-functions` - Break down complex functions into manageable pieces

**Phase 2: Code Clarity**
3. `/refactor:rename-variables` - Improve naming after structure is clear
4. `/refactor:simplify-logic` - Simplify logic now that functions are well-organized

**Phase 3: Final Polish**
5. `/format:apply-style-rules` - Apply consistent formatting
6. `/format:improve-readability` - Final manual beautification

**Phase 4: Validation**
7. `/test:all` - Ensure all refactoring preserved functionality
8. `/review:code` - Final quality assessment

## Execution Strategy

**Scope handling:**
- No arguments: Analyze and refactor entire project
- File/directory arguments: Focus refactoring on specified scope
- Multiple arguments: Process each scope systematically

**Skip functionality:**
- `--skip-duplication` - Skip duplication removal
- `--skip-extraction` - Skip function extraction
- `--skip-naming` - Skip variable renaming
- `--skip-logic` - Skip logic simplification
- `--skip-format` - Skip formatting steps
- `--skip-test` - Skip testing validation

**Intelligent execution:**
- Analyze codebase first to determine which refactorings will be most beneficial
- Skip steps that aren't relevant (e.g., no duplication found)
- Provide progress updates and reasoning for each step
- Create git checkpoints between major phases

## Smart Sequencing Logic

**Why this order works:**
1. **Remove duplication first** - Prevents refactoring the same code multiple times
2. **Extract functions next** - Establishes proper code structure before renaming
3. **Rename variables** - Clearer after function boundaries are established
4. **Simplify logic** - Easier to see logic patterns after extraction and naming
5. **Format and polish** - Final cleanup after all structural changes
6. **Test and validate** - Ensure everything still works

## Safety Measures

**Incremental validation:**
- Run tests after each major phase
- Create git commits between phases for rollback safety
- Validate each step before proceeding to next
- Stop execution if any step introduces failures

**Progress tracking:**
- TodoWrite integration to track workflow progress
- Clear reporting of what each phase accomplished
- Summary of all improvements made
- Recommendations for follow-up work

## Usage Examples

```
/workflows:run-refactor-workflow              # Full project refactoring
/workflows:run-refactor-workflow src/         # Scope to src directory
/workflows:run-refactor-workflow --skip-test  # Skip final testing
/workflows:run-refactor-workflow UserService.ts --skip-format  # Single file, skip formatting
```

## Expected Outcomes

**Code quality improvements:**
- Eliminated duplication across codebase
- Better function organization and size
- Clear, descriptive variable and function names
- Simplified, readable logic flow
- Consistent formatting and style

**Maintainability gains:**
- Easier to understand code structure
- Reduced cognitive load for developers
- Better testability through function extraction
- Improved code reusability

Systematic refactoring workflow that transforms messy code into clean, maintainable architecture.