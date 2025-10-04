---
description: "Analyzes performance bottlenecks and provides optimization recommendations"
argument-hint: "[component] (optional: frontend|backend|database|infrastructure) or [--focus <area>]"
category: "analyze"
tools: ["Bash", "Read", "Grep", "Task"]
complexity: "complex"
allowed-tools: Bash, Read, Grep, Task
---

# Command: Performance

## Purpose

Identifies performance bottlenecks across frontend, backend, and infrastructure with actionable optimization recommendations.

## Usage

```bash
/analyze:performance $ARGUMENTS
```

**Arguments**: Optional component or focus area specification

- `$1` - Component filter (frontend|backend|database|infrastructure)
- `--focus <area>` - Specific performance area to analyze
- No arguments performs comprehensive analysis across all components

### $ARGUMENTS Examples

```bash
# Component-specific analysis
/analyze:performance frontend
/analyze:performance backend
/analyze:performance database
/analyze:performance infrastructure

# Focus area analysis
/analyze:performance --focus memory
/analyze:performance --focus queries
/analyze:performance --focus bundle-size
/analyze:performance --focus rendering

# Component with focus
/analyze:performance backend --focus queries
/analyze:performance frontend --focus bundle-size

# Comprehensive analysis (no arguments)
/analyze:performance
```

## Process

1. **Argument Processing**: Parse $ARGUMENTS to determine analysis scope (component $1 or --focus flag)
2. **Performance Profiling**: Systematically analyze runtime performance, memory usage, and resource consumption patterns
3. **Frontend Performance Analysis**: Evaluate rendering performance, bundle size, loading times, and user interaction responsiveness (if
   $1=frontend or comprehensive)
4. **Backend Performance Assessment**: Analyze API response times, database query efficiency, and server resource utilization (if $1=backend or comprehensive)
5. **Database Optimization Review**: Identify slow queries, missing indexes, and schema optimization opportunities (if $1=database or comprehensive)
6. **Infrastructure Analysis**: Evaluate deployment performance, caching strategies, and CDN optimization (if $1=infrastructure or comprehensive)
7. **Focus Area Deep Dive**: Conduct specialized analysis if --focus specified (memory, queries, bundle-size, etc.)
8. **Benchmark Research**: Research industry performance standards and best practices for comparison
9. **Bottleneck Identification**: Pinpoint critical performance issues and resource constraints within specified scope
10. **Optimization Roadmap**: Create prioritized improvement plan with impact estimates and implementation complexity

## Agent Integration

- **Specialist Available**: research-analysis-specialist can be spawned to conduct comprehensive performance analysis across frontend,
  backend, and infrastructure domains
- **External Research**: Leverages WebSearch and Context7 MCP for current performance optimization best practices and benchmarking standards
- **Multi-Domain Expertise**: Frontend optimization, backend performance, database tuning, and infrastructure scaling

## Parallelization Patterns

Performance analysis benefits significantly from parallel investigation across different system layers:

```text
Main Thread Parallelization Strategy:
1. Spawn research-analysis-specialist for comprehensive performance analysis
2. Simultaneously spawn reviewer for performance-focused code review
3. Optionally spawn implementation-strategy-specialist for optimization planning
4. Coordinate findings into unified performance improvement roadmap
```

### Parallel Performance Investigation

```python
# Example: Multi-domain performance analysis with argument handling
Task(
    agent="research-analysis-specialist",
    task="Performance analysis with scope: $ARGUMENTS",
    context=f"Analyze performance based on arguments: {$ARGUMENTS}. Include frontend, backend, database, and infrastructure performance with industry benchmarking within specified scope"
)

Task(
    agent="reviewer",
    task="Performance-focused code review and optimization identification",
    context="Review code for performance anti-patterns, inefficient algorithms, and resource usage issues"
)

Task(
    agent="implementation-strategy-specialist",
    task="Performance optimization implementation planning",
    context="Create phased optimization roadmap with impact estimates and testing strategies"
)
```

## Examples

### Complete Performance Analysis

```bash
/analyze:performance
# $ARGUMENTS = "" (comprehensive analysis across all components)
```

### Layer-Specific Analysis

```bash
/analyze:performance frontend
# $ARGUMENTS = "frontend", $1 = "frontend"

/analyze:performance backend
# $ARGUMENTS = "backend", $1 = "backend"

/analyze:performance database
# $ARGUMENTS = "database", $1 = "database"

/analyze:performance infrastructure
# $ARGUMENTS = "infrastructure", $1 = "infrastructure"
```

### Focus Area Analysis

```bash
/analyze:performance --focus memory
# $ARGUMENTS = "--focus memory"

/analyze:performance --focus queries
# $ARGUMENTS = "--focus queries"

/analyze:performance --focus bundle-size
# $ARGUMENTS = "--focus bundle-size"
```

### Combined Component and Focus

```bash
/analyze:performance backend --focus queries
# $ARGUMENTS = "backend --focus queries", $1 = "backend"

/analyze:performance frontend --focus bundle-size
# $ARGUMENTS = "frontend --focus bundle-size", $1 = "frontend"
```

### Specialist Task Example

```python
# Performance bottleneck analysis with argument scope
Task(
    agent="research-analysis-specialist",
    task="Analyze application performance with scope: $ARGUMENTS",
    context="""
    Conduct performance analysis based on provided arguments ($ARGUMENTS):
    - If $1 = 'frontend': Focus on bundle size, loading times, rendering performance, user interaction responsiveness
    - If $1 = 'backend': Focus on API response times, memory usage, CPU utilization, concurrent request handling
    - If $1 = 'database': Focus on query performance, index optimization, connection pooling, data access patterns
    - If $1 = 'infrastructure': Focus on deployment performance, caching effectiveness, CDN optimization
    - If --focus specified: Deep dive into specific performance area (memory, queries, bundle-size, etc.)
    - If no arguments: Comprehensive analysis across all system layers

    Include analysis areas based on scope:
    - Frontend: Bundle size, loading times, rendering performance, user interaction responsiveness
    - Backend: API response times, memory usage, CPU utilization, concurrent request handling
    - Database: Query performance, index optimization, connection pooling, data access patterns
    - Infrastructure: Deployment performance, caching effectiveness, CDN optimization

    Research industry benchmarks and best practices for performance comparison.
    Identify critical bottlenecks and provide actionable optimization recommendations.
    Prioritize improvements by performance impact and implementation complexity.
    """
)
```

### Parallel Performance Strategy

```python
# Coordinate parallel performance investigation
performance_tasks = [
    Task(
        agent="research-analysis-specialist",
        task="Full-stack performance analysis",
        context="Frontend, backend, database, and infrastructure performance assessment"
    ),
    Task(
        agent="reviewer",
        task="Performance code review",
        context="Code-level performance issues, algorithms, and resource usage patterns"
    ),
    Task(
        agent="implementation-strategy-specialist",
        task="Optimization implementation strategy",
        context="Phased optimization plan with testing and deployment considerations"
    )
]

# Synthesize into comprehensive performance roadmap
performance_roadmap = coordinate_performance_analysis(performance_tasks)
```
