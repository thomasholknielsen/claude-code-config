---
description: "Orchestrate multi-perspective code review with dynamic selection and parallel execution"
category: "workflows"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Write", "Task", "SlashCommand"]
complexity: "complex"
allowed-tools: SlashCommand(/review:*), Read, Write
github_integration: true
---

# Command: Run Comprehensive Review

## Purpose

Orchestrates comprehensive multi-perspective code review by dynamically selecting applicable review commands
based on changed files, executing them in parallel for speed, and synthesizing results into a unified report.

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

### Step 3: Parallel Execution

Execute selected reviews concurrently using Task tool for maximum speed:

```python
# Pseudo-code for illustration - not directly executable
# Spawn parallel tasks (8-10 simultaneously)
reviews_to_run = determine_applicable_reviews(changed_files)

for review in reviews_to_run:
    Task(
        description=f"Review {review}",
        prompt=f"Run /review:{review} on {feature_branch} vs {base_branch}",
        subagent_type="reviewer"
    )

# Each task returns structured review output to main thread
```

**Parallelization Benefits:**

- Sequential: 30-40 minutes (10 reviews × 3-4 min each)
- Parallel: 3-5 minutes (all reviews simultaneously)
- Speedup: 8-10x faster

### Step 4: Synthesis

Aggregate all review outputs:

```bash
SlashCommand("/review:synthesize [all-review-outputs]")
```

The synthesis command will:

- Deduplicate overlapping issues
- Organize by severity (Critical/Major/Minor/Enhancement)
- Generate high-level summary
- Compile positive highlights
- Format final report

### Step 5: Output & Storage

1. **Display comprehensive report** to console
2. **Optionally save to artifacts:**

   ```bash
   # Save review to .artifacts/reviews/
   Write comprehensive report to .artifacts/reviews/review-{date}-{feature-branch}.md
   ```

## Agent Integration

- **Primary Agent**: reviewer - Orchestrates parallel review execution and synthesis
- **Parallel Subagents**: Multiple reviewer agents execute atomic reviews concurrently
- **Tools:** Task for parallelization, SlashCommand for synthesis

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

3. **Parallel Execution:**

   ```python
   # Core reviews (always run)
   Task("Review readability", "Run /review:readability feature/x develop", "reviewer")
   Task("Review style", "Run /review:style feature/x develop", "reviewer")
   Task("Review testing", "Run /review:testing feature/x develop", "reviewer")
   Task("Review observability", "Run /review:observability feature/x develop", "reviewer")
   Task("Review documentation", "Run /review:documentation feature/x develop", "reviewer")

   # Conditional reviews (based on changed files)
   Task("Review performance", "Run /review:performance feature/x develop", "reviewer")
   Task("Review security", "Run /review:security feature/x develop", "reviewer")
   Task("Review architecture", "Run /review:architecture feature/x develop", "reviewer")
   Task("Review design", "Run /review:design feature/x develop", "reviewer")

   # Specialized reviews (based on file type detection)
   Task("Review database", "Run /review:database feature/x develop", "reviewer")
   Task("Review API", "Run /review:api feature/x develop", "reviewer")
   Task("Review frontend architecture", "Run /review:frontend-architecture feature/x develop", "reviewer")

   # All execute simultaneously, return to main thread
   ```

4. **Synthesis:**

   ```bash
   SlashCommand("/review:synthesize [aggregated-outputs]")
   ```

5. **Save Results:**

   ```bash
   Write report to .artifacts/reviews/review-2025-10-01-feature-x.md
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
3. Parallel execution: All 12 run simultaneously (3-5 minutes)
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
✓ 8 perspectives analyzed in 3.2 minutes
```

### Example 2: Backend API Changes

```bash
/workflows:run-comprehensive-review feature/user-auth main
```

**Process:**

1. Git diff detects: `.py` (API), `.sql` (migrations)
2. Selected reviews: readability, performance, testing, security, style, architecture, documentation,
   observability, database, api (10 reviews, skips design and frontend-architecture)
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

**Traditional Sequential Review:**

- 10 reviews × 3 minutes each = 30 minutes total
- Single-threaded execution
- High developer waiting time

**Optimized Parallel Review:**

- 10 reviews simultaneously = 3-5 minutes total
- Multi-threaded with Task tool
- 85% time reduction
- Real-time progress tracking

**Intelligent Selection:**

- Only runs applicable reviews based on changed file types
- Backend changes skip UI reviews (design, frontend-architecture)
- Frontend changes skip database/API reviews
- Database-only changes skip frontend/UI reviews
- API-only changes run API-specific deep reviews
- Saves additional 20-30% time through smart filtering

## Quality Standards

- **Accuracy:** Only select truly applicable reviews
- **Speed:** Maximize parallelization
- **Completeness:** Cover all relevant perspectives
- **Actionability:** Synthesized report prioritizes by severity
- **Consistency:** Follow review standards across all perspectives
