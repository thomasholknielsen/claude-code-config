---
description: "Analyze code for performance bottlenecks, inefficiencies, and optimization opportunities"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Performance

## Purpose

Evaluate code changes for performance-related issues, bottlenecks, inefficient algorithms, memory
problems, and optimization opportunities.

## Usage

**Local:** `/review:performance [feature-branch] [base-branch]`
**GitHub:** Automatically triggered by AI Code Review workflow on PR open/sync

## Process

1. **Fetch latest code:**

   ```bash
   git fetch origin
   git checkout origin/[feature-branch]
   ```

2. **Compute diff:**

   ```bash
   git diff --name-only --diff-filter=M origin/[base-branch]...origin/[feature-branch]
   # Skip files with no actual diff hunks
   ```

3. **Parallel Performance Analysis:**
   Launch concurrent specialized performance review tasks:

   ```python
   # Algorithmic efficiency
   Task("Analyze algorithms for complexity issues, inefficient loops (O(n²) when O(n) possible), and unnecessary computations")

   # Database and ORM performance
   Task("Review database access patterns for N+1 queries, missing indexes, inefficient joins, ORM antipatterns (Prisma, TypeORM, Sequelize, Django ORM), and batch operation opportunities")

   # Memory and resource management
   Task("Evaluate memory usage for leaks, excessive allocations, large data structures in memory, and resource cleanup patterns")

   # Caching and I/O optimization
   Task("Assess caching strategies, blocking I/O in hot paths, and opportunities for async operations or result memoization")

   # Frontend performance (if applicable)
   Task("Analyze frontend performance for re-render optimization, bundle size, lazy loading, image optimization, and virtual scrolling")
   ```

4. **Evaluate against performance criteria:**
   - N+1 query patterns in database access (ORM-specific detection)
   - Inefficient loops or algorithms (O(n²) when O(n) possible)
   - Memory leaks or excessive allocations
   - Missing caching opportunities
   - Database query optimization needs (index usage, join efficiency)
   - Unnecessary computations or redundant operations
   - Blocking I/O in hot paths
   - Large data structures in memory
   - ORM antipatterns (SELECT N+1, missing eager loading, lazy loading issues)
   - Use Context7 MCP for ORM-specific performance best practices
   - Analyze in context of expected data volumes and usage patterns

5. **Report findings with severity and reasoning:**
   - Critical: Performance issues causing timeouts, crashes, or system failure
   - Major: Significant performance degradation under load
   - Minor: Small optimization opportunities
   - Enhancement: Well-optimized code patterns

6. **Include positive observations:**
   - Highlight efficient algorithms
   - Acknowledge good caching strategies

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key patterns/frameworks used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the performance problem
  - **Reasoning:** Why this matters (impact on users, scale, resource usage)
  - **Fix:** Concrete suggestion with code snippet if applicable

### Major

[Same structure as Critical]

### Minor

[Same structure as Critical]

### Enhancement

[Positive patterns and optional improvements]

**Highlights:**

- Positive observation 1
- Positive observation 2

## Agent Integration

**Primary Agent:** reviewer - Provides specialized code review guidance for performance

**Related Agents:**

- research-analysis-specialist - Can research performance optimization techniques
- implementation-strategy-specialist - Can suggest refactoring for performance

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested fixes

### Path-Specific Triggers

Especially valuable for:

- Database query files (`.sql`, `queries/`, `database/`)
- API endpoints
- Data processing pipelines

## Examples

### Example 1: Local Usage

```bash
/review:performance feature/order-processing develop
```

**Output:**

```markdown
**High-Level Summary**
This change implements bulk order processing with payment integration. Uses database
transactions and async operations for throughput.

### Critical
- **File:** `src/services/orderService.ts:67-85`
  - **Issue:** N+1 query pattern loading order items in loop
  - **Reasoning:** For orders with 100 items, generates 101 database queries causing 5-10
    second delays and potential timeout
  - **Fix:** Use batch query:
    `const items = await OrderItem.findAll({ where: { orderId: { [Op.in]: orderIds } } });`

- **File:** `src/api/orders.ts:120-140`
  - **Issue:** Loading entire user history into memory before filtering
  - **Reasoning:** Users with 10K+ orders will cause OOM errors, crashes production
  - **Fix:** Filter at database level: `WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY) LIMIT 100`

### Major
- **File:** `src/utils/calculator.ts:45-60`
  - **Issue:** O(n²) nested loop for duplicate detection on large datasets
  - **Reasoning:** Processing 1000 items takes 1M iterations (30+ seconds), unacceptable UX
  - **Fix:** Use Set for O(n) performance:
    `const seen = new Set(); items.forEach(i => { if (seen.has(i.id)) { ... } seen.add(i.id); })`

- **File:** `src/services/cache.ts:89-95`
  - **Issue:** Missing cache for expensive API calls repeated on every request
  - **Reasoning:** External API calls take 200-500ms each, multiplied across requests causes slow response times
  - **Fix:** Add Redis cache with 5-minute TTL: `const cached = await redis.get(key); if (cached) return cached;`

### Minor
- **File:** `src/components/OrderList.tsx:34-40`
  - **Issue:** Re-computing totals on every render instead of memoization
  - **Reasoning:** Causes unnecessary CPU cycles, minor impact but preventable
  - **Fix:** Use useMemo: `const total = useMemo(() => orders.reduce((sum, o) => sum + o.amount, 0), [orders]);`

**Highlights:**
- Excellent use of database indexes on `orders.user_id` and `orders.status`
- Proper connection pooling prevents database connection exhaustion
- Smart use of pagination to limit result sets
```

### Example 2: GitHub Actions (Automatic)

Triggered automatically when PR is opened or synchronized. Posts inline comments and summary.

## Integration Points

- **Follows:** Git operations (fetch, diff)
- **Followed by:** `/review:synthesize` (aggregates findings)
- **Part of:** `/workflows:run-comprehensive-review` (orchestrated execution)
- **Related:** Other `/review:*` commands for comprehensive coverage

## Quality Standards

- **Accuracy:** No false positives (consider actual usage patterns and data volumes)
- **Actionability:** Every issue has concrete optimization suggestion
- **Reasoning:** Explain performance impact with scale estimates
- **Positivity:** Include highlights for well-optimized code
- **Consistency:** Follow severity definitions strictly
- **Context-awareness:** Understand expected load and data volumes
