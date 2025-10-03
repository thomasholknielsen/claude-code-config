---
description: "Review API design, contracts, endpoints, versioning, and REST/GraphQL best practices"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7", "mcp__playwright__browser_navigate"]
complexity: "moderate"
github_integration: true
---

# Command: Review API

## Purpose

Evaluate API changes for design quality, contract compliance, endpoint security, error handling,
documentation completeness, and performance optimization.

## Usage

**Local:** `/review:api [feature-branch] [base-branch]`
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
   # Focus on: routes/, controllers/, api/, .graphql, openapi.yaml, swagger.json
   ```

3. **Parallel API Analysis:**
   Launch 6 concurrent specialized API review tasks:

   ```python
   # API design principles
   Task("Review API design for RESTful/GraphQL principles, resource modeling, endpoint naming, HTTP method usage, and API consistency")

   # Contract and versioning
   Task("Analyze API contracts including OpenAPI/GraphQL schema validation, versioning strategy, breaking changes, and backward compatibility")

   # Endpoint security
   Task("Assess endpoint security including authentication, authorization, rate limiting, CORS, CSRF protection, and input validation")

   # Error handling and responses
   Task("Evaluate error handling for consistent status codes, error messages, edge cases, validation responses, and retry strategies")

   # API documentation
   Task("Review API documentation including endpoint descriptions, request/response examples, authentication docs, and changelog updates")

   # API performance
   Task("Analyze API performance including caching headers, pagination, bulk operations, response compression, and timeout handling")
   ```

4. **Evaluate against API criteria:**
   - **Design:** RESTful principles, resource naming, HTTP verbs, GraphQL schema design, API consistency
   - **Contracts:** OpenAPI spec, GraphQL schema, versioning, breaking changes, deprecation strategy
   - **Security:** Auth (OAuth, JWT), authz (RBAC, ABAC), rate limiting, CORS, input validation
   - **Errors:** Status codes (2xx, 4xx, 5xx), error messages, validation errors, retry-after headers
   - **Documentation:** Endpoint docs, examples, authentication guide, migration guides, changelog
   - **Performance:** Caching, pagination, bulk ops, compression, N+1 prevention, timeout configuration
   - Use Context7 MCP for framework-specific best practices (Express, FastAPI, Spring, etc.)

5. **Report findings with severity and reasoning:**
   - Critical: Security vulnerabilities, breaking changes without versioning, data exposure
   - Major: Poor API design, missing documentation, performance issues, inconsistent errors
   - Minor: Best practice deviations, documentation gaps, optimization opportunities
   - Enhancement: Well-designed endpoints and robust error handling

6. **Include positive observations:**
   - Highlight consistent API design
   - Acknowledge comprehensive documentation
   - Recognize robust error handling

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this API change delivers for clients
- Engineering approach: REST/GraphQL, authentication method, key patterns

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the API problem
  - **Reasoning:** Why this matters (security, breaking changes, client impact)
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

**Primary Agent:** reviewer - Provides specialized API review guidance

**Related Agents:**

- research-analysis-specialist - Can research API design patterns and standards
- documenter - Can assist with API documentation improvements

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested fixes
- Flags breaking changes prominently

### Path-Specific Triggers

Especially valuable for:

- Route definitions (`routes/`, `routers/`, `endpoints/`)
- Controller/handler files (`controllers/`, `handlers/`, `views/`)
- API schema files (`openapi.yaml`, `swagger.json`, `schema.graphql`)
- API middleware (`middleware/`, `guards/`, `interceptors/`)

## Examples

### Example 1: REST API Design Review

```bash
/review:api feature/user-management-api main
```

**Output:**

```markdown
**High-Level Summary**
This change adds user management REST API with CRUD operations. Uses Express.js with JWT authentication
and OpenAPI 3.0 documentation.

### Critical

- **File:** `src/routes/users.ts:45-52`
  - **Issue:** Endpoint returns user passwords in API response JSON
  - **Reasoning:** Exposes password hashes to API clients, creating security vulnerability even if hashed.
    Violates least privilege principle
  - **Fix:** Exclude sensitive fields from response:
    ```typescript
    const userResponse = {
      id: user.id,
      email: user.email,
      name: user.name,
      // password excluded
    };
    res.json(userResponse);
    ```

- **File:** `src/routes/users.ts:78-85`
  - **Issue:** Breaking change - removed `username` field without API versioning
  - **Reasoning:** Existing API clients expect `username` field, will break on deployment.
    No v2 endpoint or deprecation period
  - **Fix:** Implement API versioning:
    ```typescript
    // v1 endpoint (deprecated)
    router.get('/v1/users/:id', getUserV1);

    // v2 endpoint (new)
    router.get('/v2/users/:id', getUserV2);

    // Add deprecation warning header to v1
    ```

### Major

- **File:** `src/controllers/userController.ts:120-140`
  - **Issue:** No rate limiting on user creation endpoint
  - **Reasoning:** Allows unlimited account creation, enables spam and abuse. Could overwhelm database
  - **Fix:** Add rate limiting middleware:
    ```typescript
    import rateLimit from 'express-rate-limit';

    const createUserLimiter = rateLimit({
      windowMs: 60 * 60 * 1000, // 1 hour
      max: 5, // 5 requests per hour
      message: 'Too many accounts created, please try again later'
    });

    router.post('/users', createUserLimiter, createUser);
    ```

- **File:** `src/routes/users.ts:90-100`
  - **Issue:** Missing pagination for user listing endpoint
  - **Reasoning:** Returns all users in single response, will cause timeouts and memory issues
    as user base grows
  - **Fix:** Implement cursor-based pagination:
    ```typescript
    router.get('/users', async (req, res) => {
      const limit = parseInt(req.query.limit) || 20;
      const cursor = req.query.cursor;

      const users = await User.findMany({
        take: limit + 1,
        cursor: cursor ? { id: cursor } : undefined,
        orderBy: { id: 'asc' }
      });

      const hasMore = users.length > limit;
      const results = hasMore ? users.slice(0, -1) : users;
      const nextCursor = hasMore ? users[limit].id : null;

      res.json({
        data: results,
        pagination: { nextCursor, hasMore }
      });
    });
    ```

- **File:** `openapi.yaml:0`
  - **Issue:** No OpenAPI specification file for new endpoints
  - **Reasoning:** API clients cannot generate SDKs or understand contracts, reduces API discoverability
  - **Fix:** Create OpenAPI spec with request/response schemas

### Minor

- **File:** `src/controllers/userController.ts:45`
  - **Issue:** Inconsistent error response format between endpoints
  - **Reasoning:** Some endpoints return `{ error: "message" }`, others `{ message: "error" }`.
    Confuses API clients
  - **Fix:** Standardize error format:
    ```typescript
    const errorResponse = {
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Invalid email format',
        details: validationErrors
      }
    };
    ```

**Highlights:**
- Excellent use of HTTP status codes (201 for creation, 204 for deletion)
- Proper use of middleware for request validation
- Clean separation of routes, controllers, and services
- Comprehensive input validation with detailed error messages
```

### Example 2: GraphQL API Review

```bash
/review:api feature/graphql-products develop
```

**Output:**

```markdown
**High-Level Summary**
This change adds GraphQL product catalog API with filtering and search. Uses Apollo Server with DataLoader
for N+1 prevention.

### Critical

- **File:** `src/graphql/schema.graphql:45-60`
  - **Issue:** Unbounded list query without pagination
  - **Reasoning:** `products` query returns all products without limit, will cause memory exhaustion
    and timeouts with large catalogs
  - **Fix:** Implement connection-based pagination:
    ```graphql
    type Query {
      products(first: Int!, after: String): ProductConnection!
    }

    type ProductConnection {
      edges: [ProductEdge!]!
      pageInfo: PageInfo!
    }
    ```

### Major

- **File:** `src/graphql/resolvers/product.ts:89-105`
  - **Issue:** N+1 query problem in category resolver
  - **Reasoning:** Fetches category individually for each product, causes severe performance
    degradation with many products
  - **Fix:** Use DataLoader (already in dependencies):
    ```typescript
    const categoryLoader = new DataLoader(async (categoryIds) => {
      const categories = await Category.findByIds(categoryIds);
      return categoryIds.map(id => categories.find(c => c.id === id));
    });

    // In resolver
    category: (product) => categoryLoader.load(product.categoryId)
    ```

- **File:** `src/graphql/schema.graphql:12-20`
  - **Issue:** Missing input validation directives for mutations
  - **Reasoning:** No constraints on string lengths, number ranges, or formats.
    Allows malformed data into database
  - **Fix:** Add validation directives:
    ```graphql
    input CreateProductInput {
      name: String! @length(max: 200)
      price: Float! @range(min: 0)
      sku: String! @pattern(regex: "^[A-Z0-9-]+$")
    }
    ```

**Highlights:**
- Excellent type safety with TypeScript integration
- Proper use of DataLoader pattern for efficient data fetching
- Well-structured schema with clear types and relationships
```

### Example 3: API Gateway Review

```bash
/review:api feature/api-gateway-routes main
```

**Output:**

```markdown
**High-Level Summary**
This change configures API Gateway routes for microservices. Uses Kong with OAuth2 plugin and
rate limiting policies.

### Critical

- **File:** `kong.yaml:67-75`
  - **Issue:** CORS configuration allows all origins (`*`) in production
  - **Reasoning:** Allows any website to make authenticated requests, enabling CSRF attacks
    and credential theft
  - **Fix:** Restrict to allowed origins:
    ```yaml
    cors:
      origins:
        - https://app.example.com
        - https://admin.example.com
      credentials: true
      methods: [GET, POST, PUT, DELETE]
    ```

### Major

- **File:** `kong.yaml:120-135`
  - **Issue:** No timeout configuration for upstream services
  - **Reasoning:** Slow upstream services can cause gateway to hang indefinitely, exhausting
    connections and causing cascading failures
  - **Fix:** Add timeout policies:
    ```yaml
    upstream:
      connect_timeout: 5000
      write_timeout: 60000
      read_timeout: 60000
    ```

**Highlights:**
- Excellent centralized authentication with OAuth2 plugin
- Smart use of rate limiting tiers for different API consumers
- Proper request/response transformation for version compatibility
```

## Integration Points

- **Input:** Git branches (feature vs base)
- **Dependencies:** Context7 for API framework best practices, Playwright for endpoint testing
- **Output:** API-specific review findings
- **Related Reviews:** security, performance, documentation, architecture
- **Follow-up:**
  - Use `/docs:api` to generate/update API documentation
  - Use `/review:security` for deep security audit
  - Use `/fix:bug-quickly` for critical issues

## Quality Standards

- **Design Quality:** Enforce RESTful/GraphQL principles and consistency
- **Contract Compliance:** Validate OpenAPI/GraphQL schemas and versioning
- **Security First:** Prioritize auth, authz, rate limiting, and input validation
- **Performance Aware:** Identify pagination, caching, and N+1 issues
- **Documentation Complete:** Ensure all endpoints are documented with examples

## API Technology Coverage

**Supported Frameworks:**

- Express (Node.js/TypeScript)
- FastAPI (Python)
- Spring Boot (Java)
- ASP.NET Core (C#)
- Django REST Framework (Python)
- Rails API (Ruby)
- NestJS (TypeScript)

**API Styles:**

- REST/RESTful
- GraphQL
- gRPC
- WebSocket APIs

**API Gateways:**

- Kong
- AWS API Gateway
- Azure API Management
- Google Cloud Endpoints
- Nginx

**Standards:**

- OpenAPI 3.0/3.1
- GraphQL Schema Definition Language
- JSON:API
- HAL (Hypertext Application Language)
