---
description: Systematic code restructuring with behavior preservation
category: refactoring
tools: Read, Write, Edit, MultiEdit, Glob, Grep, Bash
session: refactor/
---

# Large-Scale Refactoring

I'll systematically restructure large codebases while preserving functionality and improving maintainability across multiple files and modules.

Arguments: `$ARGUMENTS` - files, directories, or refactoring scope

## Session Continuity

**Session files location: `refactor/` in current directory**
- `refactor/plan.md` - Refactoring plan with progress
- `refactor/state.json` - Current state and checkpoints

**Commands:**
- `/refactor` - Start or resume refactoring
- `/refactor status` - Check progress  
- `/refactor new` - Start fresh session

## Refactoring Process

**Analysis Phase:**
- Identify code complexity hotspots and duplication
- Analyze architecture inconsistencies
- Check test coverage for safe refactoring
- Reference `.specify/plan.md` for architectural guidance (if available)
- Create refactoring plan with risk assessment

**Execution Phase:**
- Apply refactorings incrementally with git checkpoints
- Validate functionality after each change
- Update tests and documentation as needed
- Track progress in session files

## Refactoring Categories

**Types of refactoring:**
- **Quick wins**: Variable renames, method extractions
- **Structural**: Pattern applications, dependency improvements  
- **Architectural**: Major reorganizations, module boundaries
- **Performance**: Algorithm optimizations, caching strategies

## Validation Process

**Built-in validation:**
- Test suite validation after each change
- Behavior preservation checks
- Integration point verification
- Performance impact monitoring

## Usage Examples

**Start refactoring:**
```
/refactor                    # Analyze entire project
/refactor src/components/    # Focus on directory
/refactor UserService.ts     # Target single file
```

**Session control:**
```
/refactor resume    # Continue existing session
/refactor status    # Check progress
/refactor new       # Start fresh
```

## Execution Workflow

1. **Setup session** - Load/create state files
2. **Analyze** - Identify refactoring opportunities
3. **Plan** - Create structured refactoring plan
4. **Execute** - Apply changes incrementally
5. **Validate** - Ensure behavior preservation

Perfect session continuity with automatic rollback safety.