---
description: "Comprehensive codebase analysis through parallel domain specialist invocations covering all quality perspectives"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch, mcp__sequential-thinking__sequentialthinking
---

# Command: Run Complete Overhaul

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Execute most comprehensive codebase analysis - launch 10+ domain analysts in parallel covering all quality perspectives.

**YOU MUST:**
1. ✓ Establish baseline metrics across all dimensions
2. ✓ Launch 10+ specialist analysts in parallel (security, quality, performance, architecture, refactoring, testing, accessibility, docs, database, frontend)
3. ✓ Read all context files from all analysts
4. ✓ Deduplicate overlapping findings across domains
5. ✓ Generate risk-based roadmap with phased improvement plan
6. ✓ Deliver comprehensive overhaul summary with priorities

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Skip any major analysis domain
- ✗ Provide roadmap without prioritization by risk/impact

---

## IMPLEMENTATION FLOW

### Step 1: Pre-Overhaul Assessment
Baseline metrics: test coverage, security posture, performance, complexity

### Step 2: Parallel Multi-Domain Analysis
Launch 10+ specialists concurrently via Task tool

### Step 3: Read All Context Files
Collect findings from every analyst

### Step 4: Consolidate & Deduplicate
Aggregate all findings, identify overlaps, merge duplicate issues

### Step 5: Generate Roadmap
Create phased plan (Phase 1: Immediate | Phase 2: Short-term | Phase 3: Medium-term)

### Step 6: Report
Deliver comprehensive overhaul summary with priorities

---

## Framework Structure (S-Tier Pattern)

### CO-STAR Framework (Orchestration)

**C**ontext: Most comprehensive codebase analysis workflow launching 10+ domain analysts in parallel to assess every quality dimension (security, code quality, performance, architecture, refactoring, testing, accessibility, documentation, database, frontend) simultaneously

**O**bjective: Execute complete multi-domain parallel analysis, consolidate findings from all perspectives, deduplicate overlapping issues, generate risk-based prioritized roadmap with phased improvement plan (immediate/short-term/medium-term), deliver comprehensive overhaul summary

**S**tyle: Exhaustive multi-perspective assessment with risk-level classification (critical/high/medium/low), CVSS scoring for security, complexity metrics for quality, performance benchmarks, test coverage percentages, and consolidated improvement roadmap

**T**one: Comprehensive, strategic, risk-focused with emphasis on systematic improvement - clear phase definitions, measurable outcomes, actionable priorities

**A**udience: Engineering leadership, technical architects, product managers requiring complete codebase health assessment with prioritized improvement roadmap across all quality dimensions

**R**esults: Consolidated overhaul roadmap with critical findings prioritized by risk/impact, phased improvement plan (Phase 1: immediate, Phase 2: short-term, Phase 3: medium-term), detailed domain-specific reports persisted to .agent/context/{session-id}/

## Analysis Methodology

### 1. Pre-Overhaul Assessment: Baseline current state metrics (test coverage, security posture, performance benchmarks, complexity scores), identify high-risk areas

### 2. Parallel Multi-Domain Analysis: Launch 10+ domain analysts concurrently (security, quality, performance, architecture, refactoring, testing, accessibility, docs, database, frontend)

### 3. Consolidation & Deduplication: Aggregate findings from all domains, deduplicate overlapping issues (e.g., same security vulnerability identified by security-analyst and api-rest-analyst)

### 4. Risk-Based Prioritization: Classify by severity (Critical/High/Medium/Low), calculate impact scores, generate phased improvement roadmap

### 5. Synthesis: Generate comprehensive overhaul summary with phase definitions, measurable outcomes, success criteria per phase

## Explicit Constraints

**IN SCOPE**: Complete multi-domain analysis (security, quality, performance, architecture, refactoring, testing, accessibility, documentation, database, frontend), risk-based prioritization, phased improvement roadmap generation
**OUT OF SCOPE**: Implementation of fixes (main thread or subsequent workflows), architecture redesigns requiring API changes, infrastructure changes (cloud migrations), dependency major version upgrades

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% all domains covered, Accuracy >90% findings validated, Relevance >85% prioritized by impact, Efficiency <60s parallel analysis with 10+ analysts)

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
Task("code-quality-analyst: Analyze code complexity, detect code smells, assess maintainability metrics")
Task("performance-analyst: Identify bottlenecks, analyze optimization opportunities, assess scalability")
Task("architecture-analyst: Evaluate design patterns, assess SOLID compliance, recommend improvements")
Task("refactoring-analyst: Detect technical debt, identify refactoring opportunities, prioritize improvements")
Task("testing-analyst: Assess test coverage, evaluate test quality, identify testing gaps")
Task("frontend-accessibility-analyst: Review WCAG compliance, evaluate ARIA patterns, assess keyboard navigation")
Task("docs-analyst: Assess documentation completeness, evaluate API docs, identify knowledge gaps")
Task("database-analyst: Evaluate schema design, optimize queries, assess indexing strategies")
Task("frontend-analyst: Analyze component architecture, assess state management, optimize bundle size")

# Phase 2: Main thread synthesizes all findings and provides consolidated overhaul roadmap
```

## Agent Integration

- **Primary Agent**: architecture-analyst - Coordinates comprehensive analysis and synthesizes findings
- **Supporting Analysts** (10 parallel analysts):
  - security-analyst - Security vulnerability assessment
  - code-quality-analyst - Code quality and maintainability
  - performance-analyst - Performance and scalability analysis
  - architecture-analyst - Design patterns and SOLID compliance
  - refactoring-analyst - Technical debt and refactoring opportunities
  - testing-analyst - Test coverage and quality evaluation
  - frontend-accessibility-analyst - WCAG compliance and inclusive design
  - docs-analyst - Documentation completeness assessment
  - database-analyst - Schema design and query optimization
  - frontend-analyst - Component architecture and bundle optimization

## Examples

```bash
# Execute complete codebase overhaul analysis
/workflows:run-complete-overhaul
```

**Expected Outcome**: Quick parallel analysis across 10 domains, consolidated improvement roadmap with critical findings and prioritized action items.

**Output Structure**:

```markdown
## Complete Overhaul Analysis Summary

**Analysis Scope**: 10 domain specialists (parallel execution)
**Analysis Time**: Quick concurrent execution
**Overall Risk Level**: High (multiple critical findings)

### Critical Findings (Immediate Action)
1. **Security** - SQL injection in 3 endpoints (CVSS 9.8)
2. **Performance** - N+1 queries causing 400% slowdown
3. **Architecture** - Circular dependencies in 5 modules

### Improvement Roadmap (Prioritized by Impact)
1. **Phase 1** (Immediate): Critical security fixes + performance bottlenecks
2. **Phase 2** (Short-term): Architecture refactoring + code quality improvements
3. **Phase 3** (Medium-term): Testing coverage + documentation + accessibility

**Detailed Reports**:
- `.agent/context/{session-id}/security-analyst.md`
- `.agent/context/{session-id}/performance-analyst.md`
- `.agent/context/{session-id}/architecture-analyst.md`
- [... 7 more domain-specific reports]
```

## Integration Points

- **Domain Analysts**: Leverages all 10 analysts for complete multi-perspective analysis
- **Replaces**: Sequential workflow invocations with parallel analyst execution
- **Performance**: Significantly faster than sequential workflow approach
- **Artifact Outputs**: All analysts persist lean, actionable findings to `.agent/context/{session-id}/`

## Dependencies

**Domain Analysts** (all 10 required):

- architecture-analyst (coordination and synthesis)
- security-analyst (security assessment)
- code-quality-analyst (code quality evaluation)
- performance-analyst (performance analysis)
- refactoring-analyst (technical debt assessment)
- testing-analyst (test quality evaluation)
- frontend-accessibility-analyst (accessibility compliance)
- docs-analyst (documentation assessment)
- database-analyst (data layer optimization)
- frontend-analyst (UI architecture analysis)

## Performance Notes

- **Analysis Speed**: Significantly faster through concurrent execution
- **Parallel Tasks**: Multiple concurrent analyst invocations (most comprehensive workflow)
- **Context Management**: Analysts persist detailed findings to artifacts, return concise summaries
- **Synthesis Quality**: Main thread consolidates findings with risk-based prioritization
