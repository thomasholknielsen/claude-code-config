---
description: "Comprehensive documentation workflow that analyzes, generates, updates, and validates all project documentation"
allowed-tools: Task
---

# Command: Run Docs Workflow

## Purpose

Orchestrates a comprehensive documentation workflow using parallel domain analysis to assess, improve, and validate
all project documentation efficiently.

## Usage

```bash
/workflows:run-docs-workflow
```

## Process

1. **Parallel Analysis Phase** - Launch 3 domain analysts concurrently for comprehensive documentation assessment
2. **Synthesis Phase** - Main thread consolidates findings and generates/updates documentation
3. **Validation Phase** - Verify documentation quality, completeness, and GitHub compatibility

## Agent Integration

- **Primary Agent**: documentation-analyst - Orchestrates parallel documentation analysis and synthesizes improvements
- **Parallel Domain Analysts** (3 concurrent):
  - documentation-analyst - Documentation coverage, quality, and completeness assessment
  - architecture-analyst - System design documentation and technical accuracy validation
  - quality-analyst - Code example accuracy, formatting consistency, and standards compliance

## Implementation Steps

### Phase 1: Parallel Documentation Analysis

```python
# Launch 3 analysts concurrently for comprehensive assessment
Task("documentation-analyst: Analyze documentation coverage, identify gaps, and assess completeness across README, docs/, API docs, and changelog")
Task("architecture-analyst: Review system design documentation accuracy, validate technical diagrams, and ensure architectural consistency")
Task("quality-analyst: Verify code examples work correctly, check formatting standards, and validate GitHub rendering compatibility")

# Each analyst:
# - Burns tokens on comprehensive documentation domain analysis
# - Persists findings to .artifacts/context/{domain}-analysis-{timestamp}.md
# - Returns 2-3 sentence summary to main thread
```

### Phase 2: Main Thread Synthesis & Implementation

```python
# Read all analyst artifacts
Read(.artifacts/context/documentation-analysis-*.md)
Read(.artifacts/context/architecture-analysis-*.md)
Read(.artifacts/context/quality-analysis-*.md)

# Based on consolidated findings:
# 1. Extract external documentation for frameworks/libraries (if gaps identified)
# 2. Generate missing documentation sections
# 3. Update outdated content
# 4. Refresh API documentation
# 5. Update changelog with recent changes
# 6. Apply formatting and style corrections

# Save comprehensive documentation improvements
```

### Phase 3: Validation

```python
# Verify all improvements:
# - Check README links to docs/ work correctly
# - Validate mobile-friendly GitHub rendering
# - Ensure code examples are accurate and runnable
# - Confirm consistent formatting across all docs
```

## Examples

```bash
# Execute complete documentation workflow
/workflows:run-docs-workflow

# Result: Parallel analysis in 3-4 minutes (vs 15-20 minutes sequential)
# Phase 1: 3 analysts run concurrently (documentation, architecture, quality)
# Phase 2: Main thread synthesizes findings and implements improvements
# Phase 3: Validation ensures quality and GitHub compatibility
```

## Integration Points

### **Development Workflow Integration**

- Run after major feature implementation
- Include in pre-commit hooks for documentation updates
- Integrate with CI/CD for automated doc validation
- Schedule regular documentation health checks

### **Quality Assurance & Architecture Compliance**

- Validate all generated/updated documentation
- Ensure GitHub-friendly structure: concise README.md + comprehensive docs/
- Check README links to docs/ sections work correctly
- Verify mobile-friendly GitHub rendering
- Ensure examples work and code samples are accurate
- Maintain consistent style and formatting across README and docs/

### **Team Collaboration**

- Generate onboarding documentation for new team members
- Create handoff documentation for project transfers
- Maintain consistent documentation standards across team
- Support multiple documentation formats and audiences

## Performance Characteristics

**Traditional Sequential Approach:**

- Documentation analysis: 5-7 minutes
- Architecture review: 4-6 minutes
- Quality validation: 4-6 minutes
- Total: 15-20 minutes

**Parallel Analysis Approach:**

- 3 analysts run concurrently: 3-4 minutes
- Main thread synthesis: 1-2 minutes
- Total: 4-6 minutes
- **Performance Gain: 70-75% faster**

## Domain Analyst Outputs

**documentation-analyst** persists to `.artifacts/context/documentation-analysis-{timestamp}.md`:

- Coverage gaps and missing sections
- Outdated content identification
- API documentation completeness assessment
- Changelog update requirements

**architecture-analyst** persists to `.artifacts/context/architecture-analysis-{timestamp}.md`:

- Technical accuracy validation
- System design documentation review
- Diagram and visualization assessment
- Architectural consistency checks

**quality-analyst** persists to `.artifacts/context/quality-analysis-{timestamp}.md`:

- Code example validation results
- Formatting and style compliance
- GitHub rendering compatibility
- Cross-reference link validation
