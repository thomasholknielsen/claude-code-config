---
description: Smart feature implementation with session continuity
category: development  
tools: Read, Write, Edit, MultiEdit, Glob, Grep, Bash
session: implement/
---

# Smart Implementation Engine

I'll implement features from any source, adapting them to your project's architecture and patterns.

Arguments: `$ARGUMENTS` - URLs, paths, or descriptions to implement

## Session Continuity

**Session files location: `implement/` in current directory**
- `implement/plan.md` - Implementation plan and progress  
- `implement/state.json` - Session state

**Workflow:**
1. Check for existing session in `implement/`
2. If exists: Resume from checkpoint
3. If new: Analyze source and project, create plan
4. Execute implementation incrementally

## Implementation Process

**Analysis Phase:**
- Detect source type (URL/local/description)
- Map to project architecture and patterns
- Identify dependencies and integration points
- Create implementation plan in `implement/plan.md`

**Execution Phase:**
- Transform source to match project conventions
- Implement incrementally with progress tracking
- Update tests and validate integration
- Create git commits at logical checkpoints

**Validation Phase:**
- Run lint/test commands
- Verify no regressions
- Check integration points
- Update documentation

## Validation Commands

**Deep validation options:**
- `/implement finish` - Complete with full validation
- `/implement verify` - Deep verification against requirements  
- `/implement complete` - Ensure 100% feature completeness
- `/implement enhance` - Refine and optimize implementation

**Validation includes:**
- Source vs implementation comparison
- Comprehensive testing and fixes
- Integration point verification
- Performance and security checks
- Complete documentation updates

## Session Management

**Resume commands:**
- `/implement` or `/implement resume` - Continue from checkpoint
- `/implement status` - Check progress
- `/implement new [source]` - Start fresh implementation

## Usage Examples

**Start implementation:**
```
/implement https://github.com/user/feature
/implement ./legacy-code/auth-system/
/implement "payment processing like Stripe"
```

**Session control:**
```
/implement resume       # Continue existing session
/implement status       # Check progress
/implement new [source] # Start fresh
```

## Execution Workflow

1. **Setup session** - Load/create state files
2. **Analyze** - Understand source and target
3. **Plan** - Create implementation plan
4. **Execute** - Implement with progress tracking
5. **Validate** - Test and verify integration

Perfect session continuity maintained across all interactions.