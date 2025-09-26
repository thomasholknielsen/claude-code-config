# Code Review

I'll review your code with context-appropriate depth and spec-kit integration.

Arguments: `$ARGUMENTS` - files, directories, or specific areas to review

## Review Modes

**Quick Review (default):**
- General code quality assessment
- Basic bug pattern detection
- Style and convention checking
- Quick improvement suggestions

**Advanced Review (--advanced flag):**
- Deep technical analysis using specialized subagents
- Performance bottleneck identification
- Complex bug pattern analysis
- Architecture and design pattern assessment
- Comprehensive test coverage analysis

**Spec-Kit Integration:**
When `.specify/` folder exists, I'll automatically:
- Validate against feature requirements (`spec.md`)
- Check architectural alignment (`plan.md`)
- Verify task completion criteria (`tasks.md`)
- Validate API contract compliance (`contracts/`)

## Analysis Areas

**Code Quality:**
- Syntax correctness and language compliance
- Error handling and edge cases
- Code completeness and maintainability
- Performance implications

**Architecture:**
- Design pattern usage
- Dependency management
- Module organization
- Separation of concerns

**Security (Basic):**
- Common vulnerability patterns
- Input validation issues
- Authentication flow problems

## Usage Examples

```
/review:code UserService.ts
/review:code src/auth --advanced
/review:code . --advanced --spec-aware
```

Adapts review depth and focus based on your needs and project context.