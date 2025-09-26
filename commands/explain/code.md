# Explain Code

I'll provide clear code explanations with context-appropriate depth.

Arguments: `$ARGUMENTS` - file path, function name, or code concept to explain

## Explanation Modes

**Quick Mode (default):**
- What the code does
- Key concepts and patterns
- Basic usage examples

**Senior Context Mode (--senior flag):**
- Why this approach was chosen over alternatives
- Trade-offs and architectural decisions made
- Performance implications and considerations
- Maintenance and scalability factors
- Business context and constraints that influenced decisions
- Common pitfalls junior developers miss
- Edge cases that frequently cause issues in production

## Analysis Tools

I'll analyze using native tools:
- **Read tool** to examine code structure and patterns
- **Grep tool** to find related implementations and usage
- **Glob tool** to understand broader codebase context

## Usage Examples

```
/explain:code UserService.ts
/explain:code authentication --senior
/explain:code "payment processing logic" --senior
```

Adapts explanation depth to your needs - from quick understanding to senior-level architectural insights.