---
description: "Analyze database schema, queries, migrations, and data modeling for optimization and security"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Database

## Purpose

Evaluate database changes for schema design quality, query optimization, migration safety, data security,
and data modeling best practices.

## Usage

**Local:** `/review:database [feature-branch] [base-branch]`
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
   # Focus on: .sql, migrations/, models/, schema/, prisma/, typeorm/, sequelize/
   ```

3. **Parallel Database Analysis:**
   Launch 5 concurrent specialized database review tasks:

   ```python
   # Schema design analysis
   Task("Review schema design for normalization, denormalization trade-offs, index strategy, constraint usage, and data type appropriateness")

   # Query optimization analysis
   Task("Analyze query patterns for N+1 queries, missing indexes, inefficient joins, ORM performance issues, and batch operation opportunities")

   # Migration safety analysis
   Task("Evaluate migration scripts for rollback safety, data integrity preservation, breaking changes, and production deployment risks")

   # Database security analysis
   Task("Assess database security including SQL injection risks, permission models, encryption at rest, sensitive data handling, and audit logging")

   # Data modeling analysis
   Task("Review data modeling for relationship design, cascade behaviors, soft delete patterns, versioning strategy, and referential integrity")
   ```

4. **Evaluate against database criteria:**
   - **Schema Design:** Normalization (1NF-3NF), denormalization decisions, index strategy, constraints, data types
   - **Query Optimization:** N+1 patterns, SELECT N+1, missing indexes, inefficient joins, ORM query analysis
   - **Migration Safety:** Rollback procedures, data preservation, breaking changes, downtime requirements
   - **Database Security:** SQL injection, permission grants, encryption, PII handling, audit trails
   - **Data Modeling:** Relationships (1:1, 1:N, N:M), cascades, soft deletes, versioning, integrity
   - Use Context7 MCP for ORM-specific best practices (Prisma, TypeORM, Sequelize, Django ORM, etc.)

5. **Report findings with severity and reasoning:**
   - Critical: Data loss risks, security vulnerabilities, performance issues causing outages
   - Major: Significant performance degradation, schema design flaws, migration risks
   - Minor: Optimization opportunities, best practice deviations
   - Enhancement: Well-designed schemas and efficient queries

6. **Include positive observations:**
   - Highlight efficient indexing strategies
   - Acknowledge safe migration patterns
   - Recognize good data modeling decisions

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key database patterns/ORMs used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the database problem
  - **Reasoning:** Why this matters (data integrity, performance, security impact)
  - **Fix:** Concrete suggestion with SQL/migration code snippet if applicable

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

**Primary Agent:** reviewer - Provides specialized database review guidance

**Related Agents:**

- research-analysis-specialist - Can research database optimization techniques
- implementation-strategy-specialist - Can suggest schema refactoring strategies

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested fixes

### Path-Specific Triggers

Especially valuable for:

- Migration files (`migrations/`, `alembic/`, `db/migrate/`)
- Schema files (`schema.sql`, `prisma/schema.prisma`, `models/`)
- ORM model files (`models/`, `entities/`)
- Raw SQL query files (`.sql`)

## Examples

### Example 1: Migration Review

```bash
/review:database feature/add-user-preferences main
```

**Output:**

```markdown
**High-Level Summary**
This change adds user preferences table with JSON storage for flexible settings. Uses Prisma with PostgreSQL
JSONB for structured data storage.

### Critical

- **File:** `prisma/migrations/20250101_add_preferences.sql:12-15`
  - **Issue:** Migration adds NOT NULL column without default value to existing table with data
  - **Reasoning:** Will fail on production deployment when existing users have no preference data,
    causing downtime and rollback
  - **Fix:** Add default value or make column nullable initially:
    ```sql
    ALTER TABLE users ADD COLUMN preferences JSONB DEFAULT '{}';
    ```

### Major

- **File:** `prisma/schema.prisma:45-50`
  - **Issue:** Missing index on `userId` foreign key in user_preferences table
  - **Reasoning:** Queries filtering by user will perform full table scan, causing slow response
    times as data grows
  - **Fix:** Add index:
    ```prisma
    model UserPreference {
      userId Int @db.Integer
      @@index([userId])
    }
    ```

- **File:** `migrations/20250101_add_preferences.sql:20-25`
  - **Issue:** No rollback migration provided for destructive schema change
  - **Reasoning:** Cannot safely revert deployment if issues arise, requires manual intervention
  - **Fix:** Create down migration that preserves data before removing columns

### Minor

- **File:** `models/UserPreference.ts:34`
  - **Issue:** Using `VARCHAR(255)` for preference_key when enum would be more appropriate
  - **Reasoning:** Small optimization opportunity and better type safety at database level
  - **Fix:** Define enum type for known preference keys

**Highlights:**
- Excellent use of JSONB for flexible schema evolution
- Proper foreign key constraints with ON DELETE CASCADE
- Well-documented migration with comments explaining intent
```

### Example 2: Query Optimization Review

```bash
/review:database feature/order-dashboard develop
```

**Output:**

```markdown
**High-Level Summary**
This change implements order dashboard with analytics queries. Uses TypeORM with PostgreSQL for data
aggregation and reporting.

### Critical

- **File:** `src/services/OrderService.ts:89-105`
  - **Issue:** N+1 query pattern loading order items in loop for dashboard display
  - **Reasoning:** Dashboard loads 100 orders, triggering 101 queries (1 for orders + 100 for items).
    Causes 5-10 second page load and potential timeout under load
  - **Fix:** Use eager loading with join:
    ```typescript
    const orders = await orderRepository.find({
      relations: ['items', 'customer'],
      where: { status: 'completed' },
      order: { createdAt: 'DESC' },
      take: 100
    });
    ```

### Major

- **File:** `src/queries/analytics.sql:45-60`
  - **Issue:** Missing composite index for dashboard date range query
  - **Reasoning:** Query filters on `created_at >= ? AND created_at <= ? AND status = ?` but only has
    single index on created_at, requiring additional filtering
  - **Fix:** Create composite index:
    ```sql
    CREATE INDEX idx_orders_analytics ON orders(created_at, status) WHERE status IN ('completed', 'cancelled');
    ```

**Highlights:**
- Efficient use of materialized view for complex aggregations
- Proper connection pooling configuration for concurrent dashboard users
- Smart use of partial indexes for frequently queried statuses
```

## Integration Points

- **Input:** Git branches (feature vs base)
- **Dependencies:** Context7 for ORM best practices
- **Output:** Database-specific review findings
- **Related Reviews:** performance, security, architecture
- **Follow-up:**
  - Use `/fix:bug-quickly` for critical migration issues
  - Use `/analyze:performance` for query optimization deep dive

## Quality Standards

- **Accuracy:** Detect ORM-specific antipatterns and framework best practices
- **Safety:** Prioritize data integrity and migration safety
- **Performance:** Focus on query efficiency and indexing strategy
- **Security:** Identify SQL injection and permission issues
- **Completeness:** Cover schema, queries, migrations, modeling, and security

## Database Technology Coverage

**Supported ORMs:**

- Prisma (TypeScript/JavaScript)
- TypeORM (TypeScript/JavaScript)
- Sequelize (JavaScript)
- Django ORM (Python)
- SQLAlchemy (Python)
- Hibernate (Java)
- Entity Framework (C#)

**Supported Databases:**

- PostgreSQL
- MySQL/MariaDB
- SQLite
- MongoDB (document modeling)
- SQL Server
- Oracle

**Framework Integration:**

- Uses Context7 to fetch latest ORM documentation and best practices
- Adapts recommendations based on detected ORM and database type
