---
description: Quick implementation for small tasks bypassing spec-kit, using focused Agent Orchestra coordination
---

# Implement Small - Rapid Task Execution

Fast-track implementation for simple tasks that don't need the full spec-kit workflow. Perfect for quick fixes, small features, and minor enhancements.

## When to Use

Use `/implement:small` for:
- Single file modifications
- Simple feature additions (< 100 lines)
- Quick bug fixes
- Minor refactoring
- Small utility functions
- Simple API endpoints
- Basic UI components

## Architecture

Streamlined Agent Orchestra flow:
1. **task-orchestrator** evaluates simplicity
2. **Single worker** execution (no orchestrator overhead)
3. **Optional test/review** based on need

## Execution Flow

### Direct Implementation
```
1. task-orchestrator analyzes request
2. Confirms task is "small" (single worker capable)
3. Spawns ONE specialized worker:
   - code-writer for new features
   - bug-fixer for fixes
   - code-writer for refactoring
4. Optional: Quick test with test-writer
5. Optional: Fast review with reviewer
```

### No Spec-Kit
- Bypasses `.specify/` entirely
- No spec.md, plan.md, or tasks.md
- Direct code generation
- Minimal overhead

## Agent Selection Logic

```
if (task.type === "bug_fix"):
    spawn bug-fixer with /fix:bug-quickly
elif (task.type === "new_feature"):
    spawn code-writer with /implement
elif (task.type === "refactor"):
    spawn code-writer with /refactor:quick
elif (task.type === "test"):
    spawn test-writer directly
elif (task.type === "docs"):
    spawn documenter with /docs:update
```

## Examples

### Quick Bug Fix
```
User: "/implement:small fix login error message"
→ task-orchestrator identifies as bug
→ Spawns bug-fixer
→ Fix applied directly
→ Done in one step
```

### Small Feature
```
User: "/implement:small add email validation helper"
→ task-orchestrator identifies as feature
→ Spawns code-writer
→ Creates validation function
→ Optionally spawns test-writer
```

### Minor Refactor
```
User: "/implement:small extract duplicate code in utils.js"
→ task-orchestrator identifies as refactor
→ Spawns code-writer with /refactor:extract-functions
→ Code cleaned up
→ Done
```

## Slash Commands Used

Direct delegation to focused commands:
- `/fix:bug-quickly` - Rapid bug fixes
- `/refactor:quick` - Fast refactoring
- `/implement` - Simple features
- `/test` - Quick tests
- `/clean:improve-readability` - Code cleanup

## Benefits

1. **Speed**: No orchestrator overhead for simple tasks
2. **Simplicity**: Direct worker execution
3. **Efficiency**: Minimal token usage
4. **Focus**: One worker, one task
5. **Clarity**: No complex coordination

## Comparison

| Aspect | /implement:spec-kit-tasks | /implement:small |
|--------|---------------------------|------------------|
| Complexity | Complex features | Simple tasks |
| Agents | Multiple orchestrated | Single worker |
| Spec-kit | Required/beneficial | Bypassed |
| Memory | Full tracking | Minimal |
| Time | Thorough process | Quick execution |
| Testing | Comprehensive | Optional |
| Review | Full validation | Quick check |

## Thresholds

Task is "small" if:
- Affects ≤ 3 files
- Adds ≤ 100 lines of code
- Takes ≤ 1 worker to complete
- Has clear, focused scope
- Doesn't need complex coordination

## Escalation

If task grows beyond "small":
```
1. task-orchestrator detects complexity
2. Suggests using /implement:spec-kit-tasks
3. Can upgrade mid-task if needed
4. Preserves any work done
```

## Memory Usage

Lightweight tracking:
```json
{
  "task_type": "small",
  "worker": "code-writer",
  "status": "complete",
  "files": ["utils.js"],
  "duration": "2min"
}
```

## Error Handling

Simple approach:
1. If worker fails → spawn bug-fixer
2. If still fails → suggest spec-kit approach
3. Always preserve attempted changes

## Important Notes

- **NO automatic git operations** - User controls commits
- **NO spec-kit overhead** - Direct execution
- **Single responsibility** - One worker per task
- **Fast feedback** - Results in minutes, not hours

Perfect for when you need something done quickly without the ceremony of a full implementation workflow. Think of it as the "quick fix" mode of the Agent Orchestra system.