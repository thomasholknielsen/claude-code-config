---
description: "Orchestrate multi-perspective code review with dynamic selection and parallel execution"
allowed-tools: Task, Read, Write, Grep, Glob, WebFetch, WebSearch
github_integration: true
---

# Command: Run Comprehensive Review

## Purpose

Orchestrates comprehensive multi-perspective code review by dynamically selecting applicable review perspectives
based on changed files, executing them in parallel using Task tool, and synthesizing results for unified reporting.

## Usage

```bash
/workflows:run-comprehensive-review [feature-branch] [base-branch]
```

**Arguments:**

- `feature-branch` (optional): Branch to review (defaults to current branch)
- `base-branch` (optional): Base branch to compare against (defaults to `develop` or `main`)

## Process

### Step 1: Git Operations & Context Detection

1. **Fetch latest code:**

   ```bash
   git fetch origin
   ```

2. **Determine branches:**

   - If not provided, detect current branch and default base branch
   - Validate branches exist remotely

3. **Analyze changed files:**

   ```bash
   git diff --name-only --diff-filter=M origin/[base]...origin/[feature]
   ```

4. **File type detection:**

   - Categorize changed files by extension and path
   - Determine applicable review perspectives

### Step 2: Dynamic Review Selection

Based on changed files, select applicable reviews:

**Always Run (Core Reviews):**

- `/review:readability` - All code changes
- `/review:style` - All code changes
- `/review:testing` - All code changes
- `/review:observability` - All code changes
- `/review:documentation` - All code changes

**Conditional Reviews:**

- `/review:performance` - If database, API, or algorithmic code changed
- `/review:architecture` - If services, models, or core business logic changed
- `/review:security` - If auth, API, or sensitive data handling changed
- `/review:design` - If UI components changed (`.jsx`, `.tsx`, `.vue`, etc.)
- `/review:database` - If database schemas, migrations, or ORM models changed
- `/review:api` - If API routes, controllers, or contracts changed
- `/review:frontend-architecture` - If frontend components, state management, or build configs changed

**File Type Matrix:**

```python
file_extensions = {
    # Frontend files - trigger frontend-architecture + design
    '.js/.ts/.jsx/.tsx/.vue': ['readability', 'style', 'testing', 'observability', 'documentation', 'architecture', 'frontend-architecture', 'design'],
    'components/|store/|state/|hooks/|composables/': ['frontend-architecture', 'design', 'performance', 'testing', 'readability'],
    'webpack.config|vite.config|rollup.config': ['frontend-architecture', 'performance'],

    # Database files - trigger database review
    '.sql|migrations/|schema/|prisma/': ['database', 'performance', 'security', 'documentation'],
    'models/|entities/|repositories/': ['database', 'architecture', 'performance', 'testing'],

    # API files - trigger API review
    'routes/|controllers/|api/|handlers/': ['api', 'security', 'performance', 'testing', 'documentation'],
    '.graphql|openapi.yaml|swagger.json': ['api', 'documentation'],
    'middleware/|guards/|interceptors/': ['api', 'security', 'architecture'],

    # Backend code
    '.py/.java/.go/.rs': ['readability', 'style', 'testing', 'observability', 'documentation', 'architecture'],

    # Configuration and dependencies
    'package.json/requirements.txt': ['security', 'documentation'],
    '.yml/.yaml (CI paths)': ['observability', 'architecture', 'documentation'],
}

# Security-critical paths always get deep security review
security_critical_paths = ['auth/', 'api/security/', 'middleware/auth/', 'crypto/', 'password/']

# Performance-critical paths always get deep performance review
performance_critical_paths = ['database/', 'queries/', '.sql', 'api/', 'cache/']

# Database-critical paths always get database review
database_critical_paths = ['migrations/', 'schema/', 'prisma/', 'models/', 'entities/', '.sql']

# API-critical paths always get API review
api_critical_paths = ['routes/', 'controllers/', 'api/', 'endpoints/', 'graphql/', 'openapi']

# Frontend-critical paths always get frontend-architecture review
frontend_critical_paths = ['components/', 'store/', 'state/', 'hooks/', 'composables/', 'pages/', 'views/']
```

### Step 3: Parallel Analysis

Execute selected reviews concurrently using Task tool for maximum speed:

```python
# Phase 1: Parallel Domain Analysis (multiple analysts simultaneously)
Task("quality-analyst: Analyze code quality, complexity, and maintainability issues")
Task("security-analyst: Perform OWASP Top 10 vulnerability assessment and threat modeling")
Task("performance-analyst: Identify bottlenecks, optimization opportunities, and resource usage")
Task("testing-analyst: Assess test coverage, quality, and edge case identification")
Task("accessibility-analyst: Review WCAG compliance and ARIA patterns")
Task("documentation-analyst: Evaluate documentation completeness and quality")

# Conditional analysts based on file types:
Task("database-analyst: Review schema design, query optimization, and migrations") # if database files changed
Task("api-analyst: Analyze API design, contracts, and REST/GraphQL patterns") # if API files changed
Task("frontend-analyst: Evaluate component architecture and state management") # if frontend files changed
Task("react-analyst: Review React patterns, hooks, and component design") # if React files changed
Task("typescript-analyst: Assess type safety and TypeScript best practices") # if TypeScript files changed
Task("python-analyst: Evaluate Pythonic patterns and PEP 8 compliance") # if Python files changed

# Each analyst:
# - Performs comprehensive domain-specific analysis
# - Persists lean, actionable findings to .agent/context/{session-id}/{agent-name}.md
# - Updates incrementally if file exists
# - Returns concise summary with task counts to main thread
```

**Parallelization Benefits:**

**Execution Time:**

- Sequential reviews: significantly longer execution time (multiple reviews × quick parallel analysis each)
- Parallel analysis: much faster concurrent execution (multiple analysts running concurrently)
- **Performance Gain: substantially faster**

### Step 4: Synthesis

Main thread synthesizes all analyst findings:

```python
# Phase 2: Main Thread Synthesis
# Get session context directory
session_id = $(python3 ~/.claude/.agent/scripts/session_manager.py current)
context_dir = .agent/context/${session_id}

# Read all analyst artifacts
Read(${context_dir}/quality-analyst.md)
Read(${context_dir}/security-analyst.md)
Read(${context_dir}/performance-analyst.md)
Read(${context_dir}/testing-analyst.md)
Read(${context_dir}/accessibility-analyst.md)
Read(${context_dir}/documentation-analyst.md)
# ... plus conditional analysts

# Synthesize unified report:
# - Deduplicate overlapping issues
# - Organize by severity (Critical/Major/Minor/Enhancement)
# - Generate high-level summary
# - Compile positive highlights
# - Save to .artifacts/reviews/review-{date}-{feature-branch}.md
```

## Agent Integration

- **Primary Agent**: quality-analyst - Orchestrates parallel domain analysis and synthesizes findings
- **Parallel Domain Analysts** (6-12 concurrent):
  - quality-analyst - Code quality, complexity, maintainability
  - security-analyst - Vulnerability assessment, threat modeling
  - performance-analyst - Bottleneck detection, optimization
  - testing-analyst - Test coverage and quality assessment
  - accessibility-analyst - WCAG compliance evaluation
  - documentation-analyst - Documentation completeness review
  - database-analyst - Schema design, query optimization (conditional)
  - api-analyst - API design and contracts review (conditional)
  - frontend-analyst - Component architecture evaluation (conditional)
  - react-analyst - React patterns analysis (conditional)
  - typescript-analyst - Type safety assessment (conditional)
  - python-analyst - Pythonic patterns evaluation (conditional)
- **Tools:** Task for parallel analysis, Read for synthesis, Write for report generation

## Implementation Steps

### Full Workflow Execution

1. **Git Analysis:**

   ```bash
   git fetch origin
   git diff --name-only --diff-filter=M origin/develop...origin/feature/x
   ```

2. **Dynamic Selection:**

   - Analyze file types: `.ts`, `.tsx`, `.sql`, etc.
   - Check security-critical paths: `auth/`, `api/security/`
   - Check performance-critical paths: `database/`, `queries/`
   - Check database-critical paths: `migrations/`, `schema/`, `prisma/`, `models/`
   - Check API-critical paths: `routes/`, `controllers/`, `api/`, `graphql/`
   - Check frontend-critical paths: `components/`, `store/`, `hooks/`
   - Select applicable reviews: `[readability, performance, testing, security, style, architecture,
     documentation, observability, design, database, api, frontend-architecture]`

3. **Parallel Analysis:**

   ```python
   # Core analysts (always run)
   Task("quality-analyst: Analyze code quality, complexity, and maintainability for feature/x vs develop")
   Task("security-analyst: Perform vulnerability assessment and threat modeling for feature/x vs develop")
   Task("testing-analyst: Assess test coverage and quality for feature/x vs develop")
   Task("accessibility-analyst: Review WCAG compliance for feature/x vs develop")
   Task("documentation-analyst: Evaluate documentation completeness for feature/x vs develop")

   # Conditional analysts (based on changed files)
   Task("performance-analyst: Identify bottlenecks and optimization opportunities for feature/x vs develop")
   Task("architecture-analyst: Review SOLID principles and design patterns for feature/x vs develop")
   Task("frontend-analyst: Evaluate component architecture for feature/x vs develop")

   # Specialized analysts (based on file type detection)
   Task("database-analyst: Review schema design and query optimization for feature/x vs develop")
   Task("api-analyst: Analyze API design and contracts for feature/x vs develop")
   Task("react-analyst: Review React patterns and hooks for feature/x vs develop")

   # All execute simultaneously, persist to .agent/context/{session-id}/, return summaries
   ```

4. **Synthesis:**

   ```python
   # Main thread reads all analyst artifacts from session directory
   Read(.agent/context/${session_id}/quality-analyst.md)
   Read(.agent/context/${session_id}/security-analyst.md)
   # ... etc for all analysts

   # Synthesize unified report
   # - Deduplicate issues
   # - Organize by severity
   # - Generate summary
   ```

5. **Save Results:**

   ```bash
   Write(.artifacts/reviews/review-2025-10-01-feature-x.md)
   ```

## Examples

### Example 1: Full Stack Feature Review

```bash
/workflows:run-comprehensive-review feature/checkout-flow develop
```

**Process:**

1. Git diff detects: `.tsx` (UI), `.ts` (API), `.sql` (queries)
2. Selected reviews: readability, performance, testing, security, style, architecture, documentation,
   observability, design, database, api, frontend-architecture (12 reviews)
3. Parallel execution: All 12 run simultaneously (much faster concurrent execution)
4. Synthesis: Unified report with deduplicated findings
5. Output: Comprehensive report saved to `.artifacts/reviews/`

**Sample Output:**

```markdown
# Comprehensive Code Review Report

## Summary
This change implements a new checkout flow with Stripe payment integration...

## Issues by Severity

### Critical (2 issues)
- N+1 query in order processing (performance + security)
- Missing error handling for payment failures (observability + testing)

### Major (5 issues)
- Insufficient test coverage for payment flows (testing)
- Missing input validation on checkout form (security + readability)
- ...

### Minor (3 issues)
...

## Highlights
- Excellent separation of concerns in service layer (architecture)
- Comprehensive error logging with correlation IDs (observability)
- Well-documented API endpoints (documentation)

## Review Coverage
✓ 8 perspectives analyzed through quick parallel execution
```

### Example 2: Backend API Changes

```bash
/workflows:run-comprehensive-review feature/user-auth main
```

**Process:**

1. Git diff detects: `.py` (API), `.sql` (migrations)
2. Selected reviews: readability, performance, testing, security, style, architecture, documentation,
   observability, database, api (multiple reviews, skips design and frontend-architecture)
3. Security-critical path detected (`auth/`) → Deep security scan
4. Database-critical path detected (`migrations/`) → Deep database review with migration safety analysis
5. API-critical path detected → Deep API design and contract review
6. Parallel execution + synthesis
7. Report generated

## GitHub Integration

### Automated PR Reviews

When integrated with GitHub Actions:

1. Workflow triggers on PR open/sync
2. Runs comprehensive review automatically
3. Posts synthesized report as PR comment
4. Posts inline comments for Critical/Major issues

### Manual Local Review

Run locally before creating PR:

```bash
git checkout feature/my-changes
/workflows:run-comprehensive-review feature/my-changes develop
# Review report before pushing
```

## Integration Points

- **Input:** Git branches (feature vs base)
- **Dependencies:** All `/review:*` commands (atomic + synthesis)
- **Output:** Comprehensive unified report
- **Storage:** `.artifacts/reviews/review-{date}-{branch}.md`
- **Follow-up:**
  - Use `/to-do:create` to capture action items
  - Use `/git:commit` after addressing Critical issues
  - Use `/artifact:save` to preserve report

## Performance Characteristics

**Sequential Review:**

- Reviews execute one after another
- Total time scales linearly with review count
- Single-threaded execution pattern
- Higher developer waiting time

**Parallel Review:**

- Multiple reviews run simultaneously using Task tool
- Execution time approaches slowest review (Amdahl's Law)
- Significantly faster through concurrent execution
- Real-time progress tracking

**Note**: Actual performance depends on system resources, network latency for MCP tools, and codebase complexity.

**Intelligent Selection:**

- Only runs applicable reviews based on changed file types
- Backend changes skip UI reviews (design, frontend-architecture)
- Frontend changes skip database/API reviews
- Database-only changes skip frontend/UI reviews
- API-only changes run API-specific deep reviews
- Additional time savings through smart filtering

## Quality Standards

- **Accuracy:** Only select truly applicable reviews
- **Speed:** Maximize parallelization
- **Completeness:** Cover all relevant perspectives
- **Actionability:** Synthesized report prioritizes by severity
- **Consistency:** Follow review standards across all perspectives
