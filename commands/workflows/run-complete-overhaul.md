---
description: "Comprehensive codebase analysis through parallel domain specialist invocations covering all quality perspectives"
allowed-tools: Task
---

# Command: Run Complete Overhaul

## Purpose

Execute comprehensive codebase analysis by launching all domain analysts in parallel to assess security, quality, performance, architecture, testing, accessibility, and documentation from every perspective simultaneously.

## Usage

```bash
/workflows:run-complete-overhaul
```

## Process

1. **Launch Comprehensive Parallel Analysis**: Invoke all domain analysts simultaneously for complete coverage
2. **Synthesis Phase**: Collect and consolidate findings from all perspectives
3. **Prioritized Roadmap**: Generate unified improvement plan with risk-based prioritization

## Implementation Pattern

This workflow launches all domain analysts in parallel using Task tool (most comprehensive analysis):

```python
# Phase 1: Parallel Multi-Domain Analysis (10+ analysts concurrently)
Task("security-analyst: Conduct OWASP Top 10 assessment, identify vulnerabilities, assess threat landscape")
Task("quality-analyst: Analyze code complexity, detect code smells, assess maintainability metrics")
Task("performance-analyst: Identify bottlenecks, analyze optimization opportunities, assess scalability")
Task("architecture-analyst: Evaluate design patterns, assess SOLID compliance, recommend improvements")
Task("refactoring-analyst: Detect technical debt, identify refactoring opportunities, prioritize improvements")
Task("testing-analyst: Assess test coverage, evaluate test quality, identify testing gaps")
Task("accessibility-analyst: Review WCAG compliance, evaluate ARIA patterns, assess keyboard navigation")
Task("documentation-analyst: Assess documentation completeness, evaluate API docs, identify knowledge gaps")
Task("database-analyst: Evaluate schema design, optimize queries, assess indexing strategies")
Task("frontend-analyst: Analyze component architecture, assess state management, optimize bundle size")

# Phase 2: Main thread synthesizes all findings and provides consolidated overhaul roadmap
```

## Agent Integration

- **Primary Agent**: architecture-analyst - Coordinates comprehensive analysis and synthesizes findings
- **Supporting Analysts** (10 parallel analysts):
  - security-analyst - Security vulnerability assessment
  - quality-analyst - Code quality and maintainability
  - performance-analyst - Performance and scalability analysis
  - architecture-analyst - Design patterns and SOLID compliance
  - refactoring-analyst - Technical debt and refactoring opportunities
  - testing-analyst - Test coverage and quality evaluation
  - accessibility-analyst - WCAG compliance and inclusive design
  - documentation-analyst - Documentation completeness assessment
  - database-analyst - Schema design and query optimization
  - frontend-analyst - Component architecture and bundle optimization

## Examples

```bash
# Execute complete codebase overhaul analysis
/workflows:run-complete-overhaul
```

**Expected Outcome**: Parallel analysis across 10 domains (5-8 minutes), consolidated improvement roadmap with critical findings and prioritized action items.

**Output Structure**:

```markdown
## Complete Overhaul Analysis Summary

**Analysis Scope**: 10 domain specialists (parallel execution)
**Analysis Time**: 5-8 minutes
**Overall Risk Level**: High (multiple critical findings)

### Critical Findings (Immediate Action)
1. **Security** - SQL injection in 3 endpoints (CVSS 9.8)
2. **Performance** - N+1 queries causing 400% slowdown
3. **Architecture** - Circular dependencies in 5 modules

### Improvement Roadmap (Prioritized by Impact)
1. **Phase 1** (0-2 weeks): Critical security fixes + performance bottlenecks
2. **Phase 2** (2-6 weeks): Architecture refactoring + code quality improvements
3. **Phase 3** (1-3 months): Testing coverage + documentation + accessibility

**Detailed Reports**:
- `.artifacts/context/security-assessment-*.md`
- `.artifacts/context/performance-analysis-*.md`
- `.artifacts/context/architecture-analysis-*.md`
- [... 7 more domain-specific reports]
```

## Integration Points

- **Domain Analysts**: Leverages all 10 analysts for complete multi-perspective analysis
- **Replaces**: Sequential workflow invocations with parallel analyst execution
- **Performance**: 75-85% faster than sequential workflow approach
- **Artifact Outputs**: All analysts persist detailed findings to `.artifacts/context/`

## Dependencies

**Domain Analysts** (all 10 required):

- architecture-analyst (coordination and synthesis)
- security-analyst (security assessment)
- quality-analyst (code quality evaluation)
- performance-analyst (performance analysis)
- refactoring-analyst (technical debt assessment)
- testing-analyst (test quality evaluation)
- accessibility-analyst (accessibility compliance)
- documentation-analyst (documentation assessment)
- database-analyst (data layer optimization)
- frontend-analyst (UI architecture analysis)

## Performance Notes

- **Analysis Speed**: 75-85% faster than sequential approach (5-8 min vs 30-45 min)
- **Parallel Tasks**: 10 concurrent analyst invocations (most comprehensive workflow)
- **Context Management**: Analysts persist detailed findings to artifacts, return concise summaries
- **Synthesis Quality**: Main thread consolidates findings with risk-based prioritization
