# Command Integration Guide

This guide documents how commands work together, their relationships, and integration patterns within the Claude Code Command System.

## Command Workflow Patterns

### Development Workflow Chain

```text
/analyze:potential-issues → /fix:bug-quickly → /review:code → /git:commit
```

**Usage Example:**

```bash
# 1. Identify issues
/analyze:potential-issues

# 2. Fix found problems
/fix:bug-quickly "authentication error"

# 3. Review the fixes
/review:code

# 4. Commit the changes
/git:commit "Fix authentication error"
```

### Feature Development Lifecycle

```text
/speckit:specify → /speckit:plan → /implement:speckit-tasks → /review:code → /workflows:docs → /git:pr
```

**Usage Example:**

```bash
# 1. Define feature requirements
/speckit:specify "User authentication system"

# 2. Create implementation plan
/speckit:plan

# 3. Implement the feature
/implement:speckit-tasks

# 4. Review implementation
/review:code

# 5. Update documentation
/workflows:docs

# 6. Create pull request
/git:pr "Add user authentication system"
```

### Code Quality Improvement Chain

```text
/analyze:performance → /refactor:large-scale → /clean:improve-readability → /review:design → /git:commit
```

### Documentation Workflow

```text
/workflows:docs → /review:design → /git:commit
```

## Command Categories and Relationships

### Analysis Commands

**Primary Commands:**

- `/analyze:codebase` - Entry point for understanding existing code
- `/analyze:dependencies` - Security and update analysis
- `/analyze:potential-issues` - Problem identification

**Typically Followed By:**

- Fix commands (`/fix:*`)
- Refactor commands (`/refactor:*`)
- Documentation commands (`/docs:*`)

**Integration Pattern:**

```text
# Analysis → Action → Validation
/analyze:potential-issues → /fix:bug-quickly → /review:code
```

### Fix Commands

**Primary Commands:**

- `/fix:bug-quickly` - Rapid issue resolution
- `/fix:import-statements` - Import/dependency fixes

**Typically Preceded By:**

- Analysis commands (`/analyze:*`)
- Review commands (`/review:*`)

**Typically Followed By:**

- Review commands (`/review:*`)
- Git commands (`/git:*`)

**Integration Pattern:**

```text
# Problem → Fix → Verify → Commit
/analyze:potential-issues → /fix:bug-quickly → /review:code → /git:commit
```

### Refactor Commands

**Primary Commands:**

- `/refactor:extract-functions` - Function extraction
- `/refactor:remove-duplication` - DRY principle application
- `/refactor:simplify-logic` - Logic simplification
- `/refactor:rename-variables` - Naming improvements
- `/refactor:large-scale` - Major restructuring
- `/refactor:quick` - Quick improvements

**Workflow Integration:**

```text
# Analysis-driven refactoring
/analyze:codebase → /refactor:large-scale → /review:code → /git:commit

# Quality-driven refactoring
/analyze:potential-issues → /refactor:simplify-logic → /clean:improve-readability
```

### Review Commands

**Primary Commands:**

- `/review:code` - Code quality review
- `/review:security` - Security analysis
- `/review:design` - UI/UX compliance

**Integration as Quality Gates:**

```text
# Before commits
{any-changes} → /review:code → /git:commit

# Before deployment
{implementation} → /review:security → /review:design → /git:pr
```

### Git Commands

**Primary Commands:**

- `/git:commit` - Commit changes
- `/git:branch` - Branch management
- `/git:merge` - Branch merging
- `/git:push` - Push to remote
- `/git:pr` - Pull request creation
- `/workflows:git` - Complete Git workflows

**Integration as Final Steps:**

```text
# Individual commits
{changes} → /review:code → /git:commit

# Feature completion
{feature} → /review:code → /git:pr

# Release preparation
{release-changes} → /workflows:run-comprehensive-review → /workflows:git
```

### Documentation Commands

**Primary Commands:**

- `/workflows:docs` - Idempotent documentation workflow (CRUD operations)
- `/docs:changelog` - Manual CHANGELOG.md management (Keep a Changelog v1.1.0)

**Integration Patterns:**

```text
# Feature documentation
/implement:speckit-tasks → /workflows:docs → /git:commit

# Release documentation
/workflows:git → /docs:changelog → /workflows:docs → /git:pr
```

### Workflow Commands

**Primary Commands:**

- `/workflows:run-comprehensive-review` - Complete quality check
- `/workflows:run-cleanup-workflow` - Code cleanup
- `/workflows:docs` - Idempotent documentation workflow
- `/workflows:run-optimization` - Performance optimization
- `/workflows:run-security-audit` - Security assessment
- `/workflows:run-refactor-workflow` - Refactoring workflow
- `/workflows:run-complete-overhaul` - Full system improvement

**Integration as Orchestrators:**

```text
# Pre-release workflow
/workflows:run-comprehensive-review → /workflows:docs → /workflows:git

# Maintenance workflow
/workflows:run-cleanup-workflow → /workflows:run-optimization → /git:commit
```

## Agent Coordination Patterns

### Orchestrator → Worker Delegation

```text
task-analysis-specialist → code-writer (for implementation)
research-analysis-specialist → reviewer (for analysis)
implementation-strategy-specialist → multiple execution specialists (for complex features)
```

### Parallel Execution Patterns

```text
# Parallel reviews
/workflows:run-comprehensive-review
├── /review:code (reviewer agent)
├── /review:security (reviewer agent)
└── /review:design (reviewer agent)

# Parallel documentation
/workflows:docs
└── Documentation analysts (parallel CRUD assessment)
```

### Sequential Coordination

```text
# Feature implementation chain
1. /speckit:specify (implementation-strategy-specialist)
2. /speckit:plan (implementation-strategy-specialist)
3. /implement:speckit-tasks (implementation-strategy-specialist → code-writer)
4. /review:code (reviewer)
5. /workflows:docs (documentation analysts)
6. /git:pr (implementation-strategy-specialist)
```

## Command Dependency Matrix

| Command Category | Depends On | Enables | Best Used With |
|------------------|------------|---------|----------------|
| `analyze/*` | None (entry points) | `fix/*`, `refactor/*` | `review/*`, `docs/*` |
| `fix/*` | `analyze/*` | `review/*`, `git/*` | `review:code` |
| `refactor/*` | `analyze/*` | `clean/*`, `review/*` | `review:code`, `git:commit` |
| `clean/*` | `refactor/*` | `review/*`, `git/*` | `review:design` |
| `review/*` | Any changes | `git/*` | Before all commits |
| `git/*` | `review/*` | Deployment | After validation |
| `docs/*` | Implementation | `review:design`, `git/*` | `workflows:run-docs-workflow` |
| `workflows/*` | Multiple commands | Quality assurance | Major operations |

## Integration Best Practices

### 1. Always Review Before Commit

```text
# ✅ Good
/fix:bug-quickly → /review:code → /git:commit

# ❌ Bad
/fix:bug-quickly → /git:commit
```

### 2. Use Workflows for Complex Operations

```text
# ✅ Good
/workflows:run-comprehensive-review

# ❌ Avoid manual coordination
/review:code && /review:security && /review:design
```

### 3. Follow Logical Sequence

```text
# ✅ Good sequence
/analyze:potential-issues → /fix:bug-quickly → /review:code → /git:commit

# ❌ Illogical sequence
/git:commit → /fix:bug-quickly → /analyze:potential-issues
```

### 4. Leverage Agent Orchestration

```text
# ✅ Use analysis specialists for complex tasks
/workflows:run-complete-overhaul

# ❌ Manual execution specialist coordination
/clean:* → /refactor:* → /review:* → /docs:*
```

## Common Integration Scenarios

### Scenario 1: Bug Fix Workflow

```bash
# Identify and fix critical bug
/analyze:potential-issues "authentication failure"
/fix:bug-quickly "authentication not working"
/review:code
/git:commit "Fix authentication bug"
```

### Scenario 2: Feature Development

```bash
# Complete feature implementation
/speckit:specify "Shopping cart functionality"
/speckit:plan
/implement:speckit-tasks
/review:code
/docs:api
/git:pr "Add shopping cart feature"
```

### Scenario 3: Code Quality Improvement

```bash
# Systematic quality improvement
/analyze:codebase
/workflows:run-refactor-workflow
/workflows:run-cleanup-workflow
/review:code
/git:commit "Improve code quality and structure"
```

### Scenario 4: Release Preparation

```bash
# Prepare for release
/workflows:run-comprehensive-review
/workflows:run-security-audit
/workflows:docs
/workflows:git "release/v2.0.0"
```

### Scenario 5: Performance Optimization

```bash
# Performance improvement cycle
/analyze:performance
/workflows:run-optimization
/review:code
/workflows:docs
/git:commit "Optimize application performance"
```

## Troubleshooting Integration Issues

### Command Not Found

1. Verify command category and name
2. Check command file exists in correct directory
3. Validate YAML frontmatter

### Agent Assignment Errors

1. Check agent exists in analysis-specialists/ or execution-specialists/
2. Verify agent has required tools and permissions
3. Review Agent Specialist Framework documentation

### Workflow Failures

1. Check dependencies are satisfied
2. Verify file permissions and access
3. Review security constraints (especially Git operations)
4. Check cross-platform compatibility

### Integration Conflicts

1. Review command sequence logic
2. Check for circular dependencies
3. Verify agent coordination patterns
4. Test on different platforms

## Advanced Integration Patterns

### Conditional Command Chains

Commands can be conditionally chained based on analysis results:

```text
# Conditional refactoring
/analyze:potential-issues → [if complex] → /refactor:large-scale
                         → [if simple] → /refactor:quick
```

### Parallel Processing

Leverage Agent Orchestra for parallel execution:

```text
# Parallel quality checks
/workflows:run-comprehensive-review
# Executes /review:code, /review:security, /review:design simultaneously
```

### Context-Aware Integration

Commands adapt based on project context:

```text
# React project
/analyze:codebase → [detects React] → /review:design [includes React patterns]

# Node.js project
/analyze:dependencies → [detects Node] → /review:security [includes npm audit]
```

This integration guide ensures commands work together effectively, creating powerful automation workflows while
maintaining the Agent Orchestra coordination patterns.

## Quick Reference

### Most Common Chains

1. **Analysis → Fix → Review → Commit**
2. **Specify → Plan → Implement → Review → Document → PR**
3. **Analyze → Refactor → Clean → Review → Commit**
4. **Workflow → Review → Git**

### Quality Gates

- Always `/review:*` before `/git:*`
- Use `/workflows:*` for complex operations
- Follow dependency chains for best results

### Agent Patterns

- Analysis specialists coordinate, execution specialists execute
- Parallel execution for independent tasks
- Sequential execution for dependent tasks
