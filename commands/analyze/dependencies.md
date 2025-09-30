---
description: "Analyze project dependencies for security vulnerabilities, updates, and optimization opportunities"
argument-hint: "[--focus security|updates|compatibility] or [--manager npm|pip|composer]"
category: "analyze"
tools: ["Bash", "Read", "Grep", "WebFetch"]
complexity: "moderate"
---

# Command: Dependencies

## Purpose

Analyze project dependencies for security vulnerabilities, available updates, compatibility issues, and optimization opportunities through
comprehensive dependency ecosystem investigation.

## Usage

```bash
/analyze:dependencies $ARGUMENTS
```

**Arguments**: Optional focus area or package manager specification

- `--focus <area>` - Analysis focus (security|updates|compatibility)
- `--manager <type>` - Package manager (npm|pip|composer|maven|gradle)
- Multiple flags can be combined
- No arguments performs comprehensive analysis across all aspects

### $ARGUMENTS Examples

```bash
# Focus area analysis
/analyze:dependencies --focus security
/analyze:dependencies --focus updates
/analyze:dependencies --focus compatibility

# Package manager specific
/analyze:dependencies --manager npm
/analyze:dependencies --manager pip
/analyze:dependencies --manager composer

# Combined flags
/analyze:dependencies --focus security --manager npm
/analyze:dependencies --focus updates --manager pip

# Comprehensive analysis (no arguments)
/analyze:dependencies
```

## Process

1. **Argument Processing**: Parse $ARGUMENTS to determine analysis focus (--focus flag) and package manager scope (--manager flag)
2. **Dependency Discovery**: Scan package.json, requirements.txt, Gemfile, pom.xml, and other dependency files across the project (filtered
   by --manager if specified)
3. **Security Vulnerability Assessment**: Check dependencies against known CVE databases and security advisories (prioritized if --focus security)
4. **Version Analysis**: Identify outdated packages, available updates, and breaking change implications (prioritized if --focus updates)
5. **Compatibility Evaluation**: Assess dependency conflicts, peer dependency issues, and version compatibility (prioritized if --focus compatibility)
6. **License Compliance Review**: Verify license compatibility and identify potential legal issues
7. **Performance Impact Analysis**: Evaluate bundle size, load time, and resource usage implications
8. **Scope Filtering**: Apply focus and manager filters from $ARGUMENTS to prioritize relevant analysis areas
9. **Optimization Recommendations**: Suggest dependency consolidation, alternatives, and update strategies within specified scope
10. **Risk Assessment**: Prioritize findings by security severity, maintenance urgency, and business impact

## Agent Integration

- **Specialist Available**: research-analysis-specialist can be spawned to conduct systematic dependency ecosystem analysis with external research capabilities
- **External Research**: Leverages WebSearch and Context7 MCP for current security advisories and best practices
- **Comprehensive Coverage**: Security vulnerabilities, version compatibility, license compliance, and performance optimization

## Parallelization Patterns

Dependency analysis can benefit from parallel investigation across different aspects:

```text
Main Thread Parallelization Strategy:
1. Spawn research-analysis-specialist for comprehensive dependency analysis
2. Simultaneously spawn reviewer for security-focused vulnerability assessment
3. Optionally spawn implementation-strategy-specialist for update planning
4. Coordinate findings into unified dependency report
```

### Parallel Investigation Coordination

```python
# Example: Multi-faceted dependency analysis with argument handling
Task(
    agent="research-analysis-specialist",
    task="Dependency ecosystem analysis with scope: $ARGUMENTS",
    context=f"Analyze dependencies based on arguments: {$ARGUMENTS}. Include security, updates, compatibility, and optimization opportunities within specified scope"
)

Task(
    agent="reviewer",
    task="Security-focused dependency vulnerability assessment",
    context="Focus on CVE analysis, security advisories, and vulnerability impact assessment"
)

Task(
    agent="implementation-strategy-specialist",
    task="Dependency update strategy planning",
    context="Create safe update roadmap considering breaking changes and testing requirements"
)
```

## Examples

### Complete Dependency Analysis

```bash
/analyze:dependencies
# $ARGUMENTS = "" (comprehensive analysis across all aspects)
```

### Security-Focused Analysis

```bash
/analyze:dependencies --focus security
# $ARGUMENTS = "--focus security"
```

### Update Planning Analysis

```bash
/analyze:dependencies --focus updates
# $ARGUMENTS = "--focus updates"

/analyze:dependencies --focus compatibility
# $ARGUMENTS = "--focus compatibility"
```

### Package Manager Specific

```bash
/analyze:dependencies --manager npm
# $ARGUMENTS = "--manager npm"

/analyze:dependencies --manager pip
# $ARGUMENTS = "--manager pip"

/analyze:dependencies --manager composer
# $ARGUMENTS = "--manager composer"
```

### Combined Focus and Manager

```bash
/analyze:dependencies --focus security --manager npm
# $ARGUMENTS = "--focus security --manager npm"

/analyze:dependencies --focus updates --manager pip
# $ARGUMENTS = "--focus updates --manager pip"
```

### Specialist Task Example

```python
# Dependency ecosystem analysis with argument scope
Task(
    agent="research-analysis-specialist",
    task="Analyze project dependencies with scope: $ARGUMENTS",
    context="""
    Conduct dependency analysis based on provided arguments ($ARGUMENTS):
    - If --focus security: Prioritize security vulnerability assessment using CVE databases
    - If --focus updates: Prioritize available updates and compatibility implications
    - If --focus compatibility: Prioritize dependency conflicts and version compatibility
    - If --manager specified: Limit analysis to specific package manager ecosystem
    - If no arguments: Comprehensive analysis across all aspects

    Include analysis areas based on scope:
    - Security vulnerability assessment using CVE databases
    - Available updates and compatibility implications
    - License compliance and legal risk evaluation
    - Performance impact of current dependency choices
    - Bundle size optimization opportunities
    - Alternative package recommendations

    Research external sources for current security advisories and best practices.
    Filter package managers if --manager flag specified (npm, pip, composer, maven, gradle).
    Prioritize findings by security severity and business impact.
    """
)
```

### Parallel Analysis Strategy

```python
# Coordinate parallel dependency investigation
analysis_tasks = [
    Task(
        agent="research-analysis-specialist",
        task="Full dependency ecosystem analysis",
        context="Security, updates, compatibility, performance, and license analysis"
    ),
    Task(
        agent="reviewer",
        task="Security vulnerability deep dive",
        context="CVE analysis, exploit research, and security impact assessment"
    ),
    Task(
        agent="implementation-strategy-specialist",
        task="Update implementation planning",
        context="Safe update strategies, testing requirements, and rollback plans"
    )
]

# Synthesize into unified dependency report
dependency_report = coordinate_dependency_analysis(analysis_tasks)
```
