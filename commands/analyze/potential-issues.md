---
description: "Analyze codebase to predict potential problems before they impact the project"
argument-hint: "[domain] (optional: security|performance|code-quality) or [--component <name>]"
category: "analyze"
tools: ["Glob", "Read", "Grep", "Bash"]
complexity: "complex"
allowed-tools: Glob, Read, Grep, Bash
---

# Command: Potential Issues

## Purpose

Analyze codebase to predict potential problems before they impact the project, identifying security vulnerabilities, performance bottlenecks,
code quality issues, and architectural risks through comprehensive multi-domain investigation.

## Usage

```bash
/analyze:potential-issues $ARGUMENTS
```

**Arguments**: Optional domain or component specification

- `$1` - Domain filter (security|performance|code-quality)
- `--component <name>` - Component-specific analysis
- No arguments performs comprehensive analysis across all domains

### $ARGUMENTS Examples

```bash
# Domain-specific analysis
/analyze:potential-issues security
/analyze:potential-issues performance
/analyze:potential-issues code-quality

# Component-specific analysis
/analyze:potential-issues --component authentication
/analyze:potential-issues --component database
/analyze:potential-issues --component api

# Comprehensive analysis (no arguments)
/analyze:potential-issues
```

## Process

1. **Argument Processing**: Parse $ARGUMENTS to determine analysis scope (domain filter $1 or --component flag)
2. **Code Quality Analysis**: Systematically scan for code smells, complexity issues, and maintainability problems using Glob and Grep
3. **Security Vulnerability Assessment**: Identify potential security issues, dependency vulnerabilities, and configuration risks
4. **Performance Risk Identification**: Analyze code patterns that could lead to performance problems or resource bottlenecks
5. **Architecture Review**: Evaluate structural issues, coupling problems, and design pattern violations
6. **Dependency Analysis**: Check for outdated packages, security advisories, and compatibility issues
7. **Scope Filtering**: Apply domain or component filters from $ARGUMENTS to focus analysis
8. **Risk Prioritization**: Categorize findings by severity, impact, and implementation complexity
9. **Actionable Recommendations**: Generate specific fixes and improvement strategies with implementation guidance

## Agent Integration

- **Specialist Available**: research-analysis-specialist can be spawned to conduct comprehensive sequential analysis across multiple risk domains
- **Specialist Expertise**: Deep investigation capabilities for code quality, security, performance, and architectural risks
- **Domain Coverage**: Security vulnerabilities, performance bottlenecks, code quality issues, dependency risks, and architectural problems

## Parallelization Patterns

While the specialist conducts comprehensive sequential analysis, the main thread can enable parallel investigation:

```text
Main Thread Parallelization Approach:
1. Spawn research-analysis-specialist for comprehensive issue analysis
2. Simultaneously spawn reviewer for focused security assessment
3. Optionally spawn task-analysis-specialist for implementation complexity evaluation
4. Coordinate findings and create unified risk assessment
```

### Parallel Task Coordination

```python
# Example: Parallel risk analysis coordination with argument handling
Task(
    agent="research-analysis-specialist",
    task="Conduct comprehensive potential issues analysis of codebase with $ARGUMENTS scope",
    context=f"Focus analysis based on arguments: {$ARGUMENTS}. Include security vulnerabilities, performance risks, code quality issues, and architectural problems within specified scope"
)

Task(
    agent="reviewer",
    task="Perform focused security vulnerability assessment",
    context="Concentrate on OWASP Top 10, dependency vulnerabilities, and configuration security"
)

Task(
    agent="task-analysis-specialist",
    task="Evaluate implementation complexity and risk mitigation strategies",
    context="Assess effort required for fixing identified issues and prioritize by impact"
)
```

## Examples

### Basic Potential Issues Analysis

```bash
/analyze:potential-issues
# $ARGUMENTS = "" (comprehensive analysis)
```

### Domain-Specific Analysis

```bash
/analyze:potential-issues security
# $ARGUMENTS = "security", $1 = "security"

/analyze:potential-issues performance
# $ARGUMENTS = "performance", $1 = "performance"

/analyze:potential-issues code-quality
# $ARGUMENTS = "code-quality", $1 = "code-quality"
```

### Component-Specific Analysis

```bash
/analyze:potential-issues --component authentication
# $ARGUMENTS = "--component authentication"

/analyze:potential-issues --component database
# $ARGUMENTS = "--component database"

/analyze:potential-issues --component api
# $ARGUMENTS = "--component api"
```

### Specialist Task Example

```python
# Comprehensive potential issues investigation with argument scope
Task(
    agent="research-analysis-specialist",
    task="Analyze codebase for potential issues with scope: $ARGUMENTS",
    context="""
    Conduct analysis based on provided arguments ($ARGUMENTS):
    - If $1 = 'security': Focus on security vulnerabilities and dependency risks
    - If $1 = 'performance': Focus on performance bottlenecks and resource issues
    - If $1 = 'code-quality': Focus on code quality and maintainability concerns
    - If --component specified: Limit analysis to specified component
    - If no arguments: Comprehensive analysis across all domains

    Include:
    - Security vulnerabilities and dependency risks
    - Performance bottlenecks and resource usage issues
    - Code quality problems and maintainability concerns
    - Architectural risks and design pattern violations
    - Configuration and deployment security issues

    Prioritize findings by severity and provide actionable remediation strategies.
    """
)
```

### Parallel Analysis Coordination

```python
# Main thread coordinates parallel risk assessment
results = [
    Task(
        agent="research-analysis-specialist",
        task="Comprehensive potential issues analysis",
        context="Full codebase security, performance, and quality assessment"
    ),
    Task(
        agent="reviewer",
        task="Security-focused vulnerability assessment",
        context="OWASP compliance and dependency security review"
    )
]

# Synthesize findings into unified risk report
consolidated_assessment = synthesize_risk_findings(results)
```
