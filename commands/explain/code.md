---
description: "Provide clear code explanations with context-appropriate depth"
argument-hint: "[target] [--depth=<level>] [--focus=<aspect>] [--include-examples]"
allowed-tools: Read, Grep, Glob
---

# Command: Code

## Purpose

Provides clear code explanations with context-appropriate depth, helping understand functionality, purpose, and implementation details.

## Usage

```bash
/explain:code $ARGUMENTS
```

**Arguments**:

- `$1` (target): Specific code element (file, function, class, line range) (optional)
- `$2` (--depth): Explanation depth (brief, detailed, comprehensive) (optional)
- `$3` (--focus): Explanation focus (logic, purpose, patterns, performance) (optional)
- `$4` (--include-examples): Include usage examples and test cases (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "src/auth.js --depth=detailed"` - Detailed explanation of auth module
- `$ARGUMENTS = "getUserById --focus=logic"` - Focus on function logic
- `$ARGUMENTS = "utils/ --depth=comprehensive --include-examples"` - Full explanation with examples

## Process

1. **Parallel Code Analysis**: Use Task() to examine different aspects of the code:

   ```python
   Task("analyze-structure", "Break down code structure, classes, functions, and their relationships"),
   Task("analyze-logic", "Trace execution flow and understand algorithmic approaches"),
   Task("analyze-context", "Understand code purpose within larger system and business domain")
   ```

2. **Context Understanding**: Build comprehensive picture of code purpose based on $ARGUMENTS target:
   - Identify the problem the code solves
   - Understand business logic and domain concepts
   - Map relationships with other system components
   - Analyze input/output patterns and data transformations

3. **Implementation Analysis**: Explain how the code works:
   - Break down complex algorithms into understandable steps
   - Explain design patterns and architectural choices
   - Identify key variables, data structures, and their purposes
   - Trace execution flow through different code paths

4. **Quality Assessment**: Evaluate code characteristics:
   - Assess readability, maintainability, and performance
   - Identify potential issues or improvement opportunities
   - Explain trade-offs in implementation decisions
   - Highlight best practices or anti-patterns

5. **Explanation Generation**: Create clear, accessible explanations:
   - Use appropriate technical depth for the audience
   - Provide concrete examples and usage scenarios
   - Include visual aids like flowcharts where helpful
   - Suggest related code or documentation to explore

## Agent Integration

- **Specialist Options**: documenter specialist can be spawned for creating clear, contextual code explanations tailored to audience needs

## Parallelization Patterns

**Multi-Level Analysis**: Simultaneously analyze code at different levels (syntax, logic, architecture) to provide comprehensive understanding.

**Context Enrichment**: Run parallel analysis of related code, tests, and documentation to provide fuller context for explanations.

## Examples

```bash
# Explain specific function
/explain:code $ARGUMENTS
# where $ARGUMENTS = "getUserById --depth=detailed"

# Focus on algorithmic logic
/explain:code $ARGUMENTS
# where $ARGUMENTS = "sorting-algorithm.js --focus=logic"

# Comprehensive explanation with examples
/explain:code $ARGUMENTS
# where $ARGUMENTS = "auth-service.py --depth=comprehensive --include-examples"
