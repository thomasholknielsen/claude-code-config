---
description: "Orchestrate comprehensive code, security, and design review using parallel specialized agents"
category: "workflows"
agent: "task-orchestrator"
tools: ["SlashCommand", "Read", "Write"]
complexity: "complex"
---

# Full Review Command

Orchestrate comprehensive code, security, and design review on $ARGUMENTS using parallel specialized agents for maximum efficiency.

## Orchestrated Review Process

This command coordinates all three review workflows simultaneously for comprehensive quality assurance.

### 1. Initial Analysis
- Detect project type and technology stack
- Identify relevant files and components
- Determine which review types are applicable
- Prepare scope for each specialized reviewer

### 2. Parallel Review Execution

Launch three specialized review agents **in parallel**:

#### 🔧 Code Review Branch
- **Agent**: code-reviewer-advanced
- **Focus**: Syntax, bugs, performance, style, completeness
- **Output**: Code quality report with prioritized issues

#### 🔒 Security Review Branch
- **Agent**: security-scanner
- **Focus**: OWASP vulnerabilities, secrets, CVEs, configurations
- **Output**: Security assessment with severity ratings

#### 🎨 Design Review Branch (if frontend code present)
- **Agent**: ui-compliance-checker
- **Focus**: Design system, accessibility, responsiveness, UX
- **Output**: UI/UX compliance report with visual issues

### 3. Cross-Analysis Integration

After parallel reviews complete, perform intelligent analysis:
- **Correlation**: Identify related issues across review types
- **Deduplication**: Merge overlapping findings
- **Impact Analysis**: Assess combined effect of issues
- **Dependency Mapping**: Find fix order dependencies

### 4. Unified Prioritization

Create master priority list considering:
- **Severity**: Critical > High > Medium > Low
- **Type Weight**:
  - Security Critical = Top Priority
  - Accessibility Violations = High Priority (legal)
  - Bugs = High Priority
  - Performance = Medium Priority
  - Style = Lower Priority
- **Fix Complexity**: Quick wins vs. major refactors
- **Business Impact**: User-facing vs. internal

### 5. Generate Comprehensive Report

```markdown
## 📊 FULL REVIEW REPORT

### Executive Summary
- Total Issues: X (Critical: X, High: X, Medium: X, Low: X)
- Security Risk: [Low/Medium/High/Critical]
- Code Quality: [A/B/C/D/F]
- Design Compliance: X%
- Immediate Actions Required: [Yes/No]

### 🚨 Critical Issues (Fix Immediately)
[Merged critical findings from all reviews]

### 🔴 High Priority Issues
[Security vulnerabilities, bugs, accessibility violations]

### 🟡 Medium Priority Issues
[Performance, important refactoring, design inconsistencies]

### 🔵 Low Priority Issues
[Style, minor improvements, nice-to-haves]

### 📈 Metrics Dashboard
#### Code Quality
- Complexity Hotspots: [List]
- Test Coverage: X%
- Technical Debt: [Hours]

#### Security Posture
- OWASP Coverage: X/10
- CVE Count: X
- Secrets Found: X

#### Design Compliance
- Accessibility Score: X/100
- Design System: X% compliant
- Responsive Issues: X

### ✅ Positive Findings
[Good practices observed across all reviews]

### 🔄 Fix Sequencing
[Ordered list considering dependencies]
1. [Critical security fix]
2. [Breaking bug fix]
3. [Accessibility violation]
...

### 📋 Action Plan
#### Immediate (Today)
- [ ] Fix critical security vulnerabilities
- [ ] Patch breaking bugs

#### Short-term (This Week)
- [ ] Address high-priority issues
- [ ] Update dependencies with CVEs

#### Long-term (This Sprint)
- [ ] Refactor complexity hotspots
- [ ] Improve test coverage
- [ ] Enhance design consistency
```

### 6. Create Integrated Todo List

Generate a TodoWrite list that:
- Groups related fixes together
- Orders by true priority
- Estimates effort for each item
- Includes verification steps
- Links to specific review details

### 7. Continuous Improvement Tracking

Document patterns for future reviews:
- Common issue types found
- False positive patterns
- Project-specific considerations
- Team velocity on fixes

## Command Variations

```bash
# Full review of entire project
/full-review .

# Full review of specific module
/full-review src/api

# Focus on changes only
/full-review "git diff HEAD~1"

# Quick review (parallel but less deep)
/full-review . --quick

# With visual screenshots
/full-review . --visual
```

## Review Coordination

The full review intelligently coordinates:
- **Parallel Execution**: All reviews run simultaneously
- **Resource Sharing**: Reviews share project analysis
- **Conflict Resolution**: Handles overlapping findings
- **Smart Aggregation**: Combines insights intelligently

## Integration Benefits

Running all reviews together provides:
- **Holistic View**: See how issues interconnect
- **Time Efficiency**: Parallel execution saves time
- **Better Prioritization**: Cross-domain priority weighting
- **Reduced Context Switching**: One report to act on
- **Comprehensive Coverage**: Nothing falls through cracks

## Best Practices

1. **Run Regularly**: Before major releases or PR merges
2. **Act on Criticals**: Always fix critical issues immediately
3. **Track Progress**: Use todos to manage remediation
4. **Learn Patterns**: Use findings to prevent future issues
5. **Customize Thresholds**: Adjust severity based on project needs

## Output Handling

The full review will:
- Generate a single, comprehensive report
- Create an actionable todo list
- Provide specific fix recommendations
- Include all necessary context for fixes
- Track remediation progress

Remember: The full review is your quality gate. Use it to ensure code is secure, functional, and user-friendly before shipping. The parallel execution makes it fast enough to run frequently without blocking development flow.