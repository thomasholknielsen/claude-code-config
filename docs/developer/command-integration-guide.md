# Command Integration Guide

This guide documents how commands work together, their relationships, and integration patterns within the Claude Code Command System.

## Command Workflow Patterns

### Development Workflow Chain

```bash
/analyze:potential-issues → /fix:bug-quickly → /review:code → /git:commit
```text

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
```text

### Feature Development Lifecycle

```bash
/spec-kit:specify → /spec-kit:plan → /implement:spec-kit-tasks → /review:code → /docs:update → /git:pr
```text

**Usage Example:**

```bash
# 1. Define feature requirements
/spec-kit:specify "User authentication system"

# 2. Create implementation plan
/spec-kit:plan

# 3. Implement the feature
/implement:spec-kit-tasks

# 4. Review implementation
/review:code

# 5. Update documentation
/docs:update

# 6. Create pull request
/git:pr "Add user authentication system"
```text

### Code Quality Improvement Chain

```bash
/analyze:performance → /refactor:large-scale → /clean:improve-readability → /review:design → /git:commit
```text

### Documentation Workflow

```bash
/docs:analyze → /docs:generate → /docs:update → /review:design → /git:commit
```yaml

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

```bash
# Analysis → Action → Validation
/analyze:potential-issues → /fix:bug-quickly → /review:code
```yaml

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

```bash
# Problem → Fix → Verify → Commit
/analyze:potential-issues → /fix:bug-quickly → /review:code → /git:commit
```yaml

### Refactor Commands

**Primary Commands:**

- `/refactor:extract-functions` - Function extraction
- `/refactor:remove-duplication` - DRY principle application
- `/refactor:simplify-logic` - Logic simplification
- `/refactor:rename-variables` - Naming improvements
- `/refactor:large-scale` - Major restructuring
- `/refactor:quick` - Quick improvements

**Workflow Integration:**

```bash
# Analysis-driven refactoring
/analyze:codebase → /refactor:large-scale → /review:code → /git:commit

# Quality-driven refactoring
/analyze:potential-issues → /refactor:simplify-logic → /clean:improve-readability
```yaml

### Review Commands

**Primary Commands:**

- `/review:code` - Code quality review
- `/review:security` - Security analysis
- `/review:design` - UI/UX compliance

**Integration as Quality Gates:**

```bash
# Before commits
{any-changes} → /review:code → /git:commit

# Before deployment
{implementation} → /review:security → /review:design → /git:pr
```yaml

### Git Commands

**Primary Commands:**

- `/git:commit` - Commit changes
- `/git:branch` - Branch management
- `/git:merge` - Branch merging
- `/git:push` - Push to remote
- `/git:pr` - Pull request creation
- `/git:workflow` - Complete Git workflows

**Integration as Final Steps:**

```bash
# Individual commits
{changes} → /review:code → /git:commit

# Feature completion
{feature} → /review:code → /git:pr

# Release preparation
{release-changes} → /workflows:run-comprehensive-review → /git:workflow
```yaml

### Documentation Commands

**Primary Commands:**

- `/docs:generate` - Auto-generate documentation
- `/docs:update` - Update existing docs
- `/docs:api` - API documentation
- `/docs:changelog` - Version history
- `/docs:analyze` - Documentation audit
- `/docs:extract-external` - External doc integration

**Integration Patterns:**

```bash
# Feature documentation
/implement:spec-kit-tasks → /docs:api → /docs:update → /git:commit

# Release documentation
/git:workflow → /docs:changelog → /docs:generate → /git:pr
```yaml

### Workflow Commands

**Primary Commands:**

- `/workflows:run-comprehensive-review` - Complete quality check
- `/workflows:run-cleanup-workflow` - Code cleanup
- `/workflows:run-docs-workflow` - Documentation workflow
- `/workflows:run-optimization` - Performance optimization
- `/workflows:run-security-audit` - Security assessment
- `/workflows:run-refactor-workflow` - Refactoring workflow
- `/workflows:run-complete-overhaul` - Full system improvement

**Integration as Orchestrators:**

```bash
# Pre-release workflow
/workflows:run-comprehensive-review → /workflows:run-docs-workflow → /git:workflow

# Maintenance workflow
/workflows:run-cleanup-workflow → /workflows:run-optimization → /git:commit
```text

## Agent Coordination Patterns

### Orchestrator → Worker Delegation

```text
task-orchestrator → code-writer (for implementation)
research-orchestrator → reviewer (for analysis)
implementation-orchestrator → multiple workers (for complex features)
```text

### Parallel Execution Patterns

```bash
# Parallel reviews
/workflows:run-comprehensive-review
├── /review:code (reviewer agent)
├── /review:security (reviewer agent)
└── /review:design (reviewer agent)

# Parallel documentation
/workflows:run-docs-workflow
├── /docs:api (documenter agent)
├── /docs:generate (documenter agent)
└── /docs:update (documenter agent)
```text

### Sequential Coordination

```bash
# Feature implementation chain
1. /spec-kit:specify (implementation-orchestrator)
2. /spec-kit:plan (implementation-orchestrator)
3. /implement:spec-kit-tasks (implementation-orchestrator → code-writer)
4. /review:code (reviewer)
5. /docs:update (documenter)
6. /git:pr (implementation-orchestrator)
```yaml

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

```bash
# ✅ Good
/fix:bug-quickly → /review:code → /git:commit

# ❌ Bad
/fix:bug-quickly → /git:commit
```text

### 2. Use Workflows for Complex Operations

```bash
# ✅ Good
/workflows:run-comprehensive-review

# ❌ Avoid manual coordination
/review:code && /review:security && /review:design
```text

### 3. Follow Logical Sequence

```bash
# ✅ Good sequence
/analyze:potential-issues → /fix:bug-quickly → /review:code → /git:commit

# ❌ Illogical sequence
/git:commit → /fix:bug-quickly → /analyze:potential-issues
```text

### 4. Leverage Agent Orchestration

```bash
# ✅ Use orchestrators for complex tasks
/workflows:run-complete-overhaul

# ❌ Manual worker coordination
/clean:* → /refactor:* → /review:* → /docs:*
```text

## Common Integration Scenarios

### Scenario 1: Bug Fix Workflow

```bash
# Identify and fix critical bug
/analyze:potential-issues "authentication failure"
/fix:bug-quickly "authentication not working"
/review:code
/git:commit "Fix authentication bug"
```text

### Scenario 2: Feature Development

```bash
# Complete feature implementation
/spec-kit:specify "Shopping cart functionality"
/spec-kit:plan
/implement:spec-kit-tasks
/review:code
/docs:api
/git:pr "Add shopping cart feature"
```text

### Scenario 3: Code Quality Improvement

```bash
# Systematic quality improvement
/analyze:codebase
/workflows:run-refactor-workflow
/workflows:run-cleanup-workflow
/review:code
/git:commit "Improve code quality and structure"
```text

### Scenario 4: Release Preparation

```bash
# Prepare for release
/workflows:run-comprehensive-review
/workflows:run-security-audit
/workflows:run-docs-workflow
/git:workflow "release/v2.0.0"
```text

### Scenario 5: Performance Optimization

```bash
# Performance improvement cycle
/analyze:performance
/workflows:run-optimization
/review:code
/docs:update "performance improvements"
/git:commit "Optimize application performance"
```bash

## Troubleshooting Integration Issues

### Command Not Found

1. Verify command category and name
2. Check command file exists in correct directory
3. Validate YAML frontmatter

### Agent Assignment Errors

1. Check agent exists in orchestrators/ or workers/
2. Verify agent has required tools and permissions
3. Review Agent Orchestra Framework documentation

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

```bash
# Conditional refactoring
/analyze:potential-issues → [if complex] → /refactor:large-scale
                         → [if simple] → /refactor:quick
```text

### Parallel Processing

Leverage Agent Orchestra for parallel execution:

```bash
# Parallel quality checks
/workflows:run-comprehensive-review
# Executes /review:code, /review:security, /review:design simultaneously
```yaml

### Context-Aware Integration

Commands adapt based on project context:

```bash
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

- Orchestrators coordinate, workers execute
- Parallel execution for independent tasks
- Sequential execution for dependent tasks
