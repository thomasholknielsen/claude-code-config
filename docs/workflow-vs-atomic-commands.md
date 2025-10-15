# Workflow vs Atomic Commands: A Comprehensive Guide

## Philosophy

The command system follows a **complementary architecture** where workflows and atomic commands serve different but related purposes:

- **Workflows**: Orchestrated multi-step processes for comprehensive operations
- **Atomic Commands**: Single-purpose, targeted operations for specific tasks

Both are essential, and understanding when to use each maximizes productivity.

## Core Differences

| Aspect | Workflows | Atomic Commands |
|--------|-----------|-----------------|
| **Scope** | Multi-domain, comprehensive | Single-domain, focused |
| **Execution** | Parallel domain analysts | Direct operation |
| **Speed** | Significantly faster (parallelization) | Linear execution |
| **Control** | Automated within parameters | Full manual control |
| **Output** | Consolidated reports | Immediate targeted results |
| **Use Case** | Broad analysis/operations | Surgical interventions |

## Architecture Pattern

### Workflows: Three-Phase Pattern

All workflow commands follow this pattern:

```text
Phase 1: Parallel Analysis
├─ Task(analyst1: comprehensive domain analysis)
├─ Task(analyst2: comprehensive domain analysis)
└─ Task(analyst3: comprehensive domain analysis)

Phase 2: Main Thread Synthesis
├─ Read all analyst artifacts (.agent/context/*.md)
├─ Consolidate findings
└─ Implement changes OR generate consolidated report

Phase 3: Validation
├─ Verify improvements
└─ Confirm quality metrics
```

**Key Characteristic**: Workflows can use `Task, Read, Write, Edit, Grep, Glob, WebFetch, WebSearch` tools, making them self-contained.

### Atomic Commands: Direct Execution

Atomic commands execute immediately with focused scope:

```text
Command Invocation
├─ Validate parameters
├─ Execute single operation
└─ Return immediate results
```

**Key Characteristic**: Single responsibility, immediate feedback, chainable for custom workflows.

## Performance Characteristics

### Parallelization Advantage

**Workflows leverage parallel execution**:

```text
Sequential (Atomic Commands):
├─ Analyst 1: 3-5 min
├─ Analyst 2: 3-5 min
└─ Analyst 3: 3-5 min
Total: Linear accumulation

Parallel (Workflows):
├─ Analyst 1: 3-5 min ┐
├─ Analyst 2: 3-5 min ├─ Concurrent
└─ Analyst 3: 3-5 min ┘
Total: Approaches slowest analyst (Amdahl's Law)
```

**Performance Gain**: Workflows are significantly faster through concurrent execution.

## When to Use Each

### Use Workflows When

1. **Comprehensive Analysis Needed**
   - You want multiple perspectives (security + performance + quality)
   - You need cross-domain insights
   - You want to discover issues you didn't know existed

2. **Speed Matters**
   - Parallel execution provides substantial time savings
   - You have multiple independent analysis tasks
   - You want results faster than sequential operations

3. **Automated Decision-Making Acceptable**
   - You trust the system to make reasonable decisions
   - You want recommendations, not just raw data
   - You're willing to review consolidated findings

4. **Pre-Release Quality Gates**
   - Comprehensive QA before deployment
   - Security audits across all layers
   - Performance optimization across stack

5. **Periodic Health Checks**
   - Regular codebase assessment
   - Documentation validation
   - Technical debt identification

### Use Atomic Commands When

1. **Surgical Precision Required**
   - You know exactly what needs fixing
   - You want to change one specific thing
   - You need granular control over operations

2. **Iterative Development**
   - You're actively coding and need quick feedback
   - You want to test one change at a time
   - You're building custom sequences

3. **Learning and Exploration**
   - You want to understand each step
   - You're experimenting with approaches
   - You need detailed intermediate results

4. **Custom Workflow Construction**
   - Standard workflows don't fit your use case
   - You want to chain commands in unique ways
   - You need conditional logic between steps

5. **Targeted Operations**
   - Git operations (commit, push, branch)
   - Specific documentation updates
   - Quick bug fixes
   - Import statement repairs

## Complementary Usage Patterns

### Pattern 1: Workflow → Atomic (Analysis → Implementation)

```bash
# Comprehensive analysis with workflow
/workflows:run-comprehensive-review

# Review findings in .artifacts/
# Then apply specific fixes with atomic commands
/fix:bug-quickly "SQL injection in user search"
/clean:apply-style-rules
/git:commit
```

**When**: You want comprehensive analysis but manual control over fixes.

---

### Pattern 2: Atomic → Workflow (Development → Validation)

```bash
# Develop feature with atomic commands
/implement:small "Add user authentication endpoint"
/workflows:docs

# Comprehensive validation with workflow
/workflows:run-security-audit
/workflows:run-comprehensive-review
```

**When**: You're actively developing and want thorough QA at the end.

---

### Pattern 3: Workflow → Workflow (Staged Operations)

```bash
# Stage 1: Analyze and optimize
/workflows:run-complete-overhaul

# Stage 2: Security focus
/workflows:run-security-audit

# Stage 3: Documentation update
/workflows:docs

# Stage 4: Commit everything
/git:commit
```

**When**: You want multiple comprehensive passes with different focuses.

---

### Pattern 4: Atomic → Atomic (Custom Workflow)

```bash
# Custom git workflow
/git:branch "feature/new-dashboard"
/implement:small "Create dashboard component"
/clean:apply-style-rules
/git:commit
/git:push
/git:pr "Add user dashboard feature"
```

**When**: You want complete manual control over each step.

## Real-World Scenarios

### Scenario 1: "I inherited a codebase and need to understand it"

**Recommended Approach**:

```bash
# Start with comprehensive analysis
/workflows:run-complete-overhaul          # Get full picture
/explain:architecture                     # Understand structure
/guru "What are the most critical areas?"  # Get guidance

# Then dive into specifics
/explain:code [specific_component]        # Understand details
```

**Why**: Workflows provide broad overview, atomic commands allow deep dives.

---

### Scenario 2: "I'm actively developing a new feature"

**Recommended Approach**:

```bash
# Use speckit workflow for structure
/speckit:specify
/speckit:plan
/speckit:tasks

# Use atomic commands for implementation
/implement:small [each task]              # Iterative development
/fix:bug-quickly [issues found]           # Quick fixes

# Use workflow for final validation
/workflows:run-comprehensive-review       # QA before merge
```

**Why**: Spec-kit provides structure, atomic commands enable iteration, workflow validates quality.

---

### Scenario 3: "Release is tomorrow and I need to ensure quality"

**Recommended Approach**:

```bash
# Parallel comprehensive checks
/workflows:run-security-audit             # Security validation
/workflows:run-optimization               # Performance check
/workflows:run-comprehensive-review       # Code quality

# Use findings to apply specific fixes
/fix:bug-quickly [critical issues]
/clean:apply-style-rules

# Final validation
/workflows:run-lint-and-correct-all
/git:commit
```

**Why**: Time pressure requires parallel workflows for speed, atomic commands for targeted fixes.

---

### Scenario 4: "I need to refactor a complex module"

**Recommended Approach**:

```bash
# Comprehensive refactoring analysis
/workflows:run-refactor-workflow          # Get refactoring plan

# Review consolidated findings
# Then decide: implement automatically or manually?

# Option A: Let workflow implement
# (workflow already did implementation in Phase 2)

# Option B: Manual targeted refactoring
/clean:improve-readability [module]       # Specific improvements
/fix:import-statements [after moving files]
```

**Why**: Workflow identifies opportunities, you choose implementation approach.

## Decision Framework

Use this framework to decide between workflows and atomic commands:

```text
Question 1: Do I know exactly what needs to be done?
├─ YES → Consider atomic commands
└─ NO → Use workflows for discovery

Question 2: Do I need multiple perspectives?
├─ YES → Use workflows for parallel analysis
└─ NO → Atomic command may suffice

Question 3: Is speed critical?
├─ YES → Use workflows for parallelization
└─ NO → Either approach works

Question 4: Do I want automated implementation?
├─ YES → Workflows can implement changes
└─ NO → Use workflows for analysis, atomic for manual fixes

Question 5: Am I building a custom sequence?
├─ YES → Chain atomic commands
└─ NO → Check if workflow exists for your use case
```

## Migration from Deprecated Commands

Three commands were deprecated in favor of workflow approaches:

### `/review:code` → `/workflows:run-comprehensive-review`

**Old Approach** (Single-perspective):

```bash
/review:code src/
```

**New Approach** (Multi-perspective with dynamic selection):

```bash
/workflows:run-comprehensive-review
# Analyzes file types and selects relevant analysts dynamically
# Provides consolidated report from multiple perspectives
```

**Why**: Workflows provide richer analysis through parallel domain experts.

---

### `/refactor:apply` → `/workflows:run-refactor-workflow`

**Old Approach** (Limited patterns):

```bash
/refactor:apply src/ --pattern=extract-function
```

**New Approach** (Comprehensive refactoring):

```bash
/workflows:run-refactor-workflow
# Parallel analysis: refactoring + quality + architecture analysts
# Comprehensive refactoring plan with multiple dimensions
```

**Why**: Workflows identify more opportunities through multi-domain analysis.

---

### `/refactor:large-scale` → `/workflows:run-refactor-workflow`

**Old Approach** (Separate command for scale):

```bash
/refactor:large-scale --target=src/
```

**New Approach** (Unified workflow handles all scales):

```bash
/workflows:run-refactor-workflow
# Handles both small and large refactoring
# Scales analysis based on codebase size
```

**Why**: Single unified workflow eliminates redundancy and provides consistent approach.

## Best Practices

### 1. Start with Workflows for Discovery

Don't assume you know all issues. Run comprehensive workflows to discover problems you didn't anticipate.

### 2. Use Atomic Commands for Precision

When you know exactly what to fix, atomic commands provide surgical precision.

### 3. Leverage Parallel Execution

Workflows running 3-5 analysts in parallel are significantly faster than sequential atomic commands.

### 4. Trust Workflows for Routine QA

Pre-release checks, periodic audits, and health checks benefit from automated workflow execution.

### 5. Build Custom Sequences When Needed

Standard workflows don't cover every use case. Chain atomic commands for custom flows.

### 6. Review Workflow Outputs

Workflows generate consolidated reports in `.artifacts/`. Review these before making decisions.

### 7. Combine Approaches Liberally

Don't limit yourself to one or the other. Use workflows for analysis, atomic for implementation, then workflows for validation.

## Command Catalog Quick Reference

### Available Workflows (8 total)

- `/workflows:run-comprehensive-review` - Multi-perspective code review
- `/workflows:run-refactor-workflow` - Comprehensive refactoring
- `/workflows:run-cleanup-workflow` - Quality and readability cleanup
- `/workflows:run-complete-overhaul` - Full codebase analysis
- `/workflows:docs` - Idempotent documentation workflow
- `/workflows:run-optimization` - Performance optimization
- `/workflows:run-security-audit` - Security assessment
- `/workflows:run-lint-and-correct-all` - Language detection and linting

### Complementary Atomic Commands by Category

- **Git**: commit, branch, merge, push, pr, worktree, full-workflow
- **Spec-Kit**: specify, plan, clarify, tasks, analyze, implement, constitution
- **Development**: implement:small, implement:speckit-tasks, fix:bug-quickly, fix:import-statements
- **Quality**: clean:apply-style-rules, clean:improve-readability
- **Documentation**: docs:extract-external, docs:update, docs:generate, docs:changelog, docs:api
- **Explain**: explain:code, explain:architecture, guru
- **System**: to-do:*, session:*, slashcommand:*, subagent:*, utility:*, prompt:*

## Conclusion

Workflows and atomic commands form a **complementary system**:

- **Workflows** excel at comprehensive, multi-domain operations with parallel execution
- **Atomic commands** excel at targeted, precise operations with full manual control

The most effective approach often combines both:

1. Use workflows for discovery and comprehensive analysis
2. Use atomic commands for targeted implementation and custom sequences
3. Use workflows again for validation and quality assurance

Understanding this complementary relationship unlocks the full power of the command system.
