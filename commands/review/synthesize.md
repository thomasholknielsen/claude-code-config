---
description: "Aggregate multiple review outputs into a unified, deduplicated report organized by severity"
category: "review"
agent: "reviewer"
tools: ["Read", "Write"]
complexity: "moderate"
github_integration: true
---

# Command: Synthesize Review

## Purpose

Aggregates multiple atomic review outputs into a comprehensive, unified report with deduplication,
severity-based organization, high-level summary, and positive highlights.

## Usage

**Local:** `/review:synthesize [review-output-1] [review-output-2] ...`
**Note:** Typically called by `/workflows:run-comprehensive-review` after parallel review execution

## Process

1. **Parse multiple review outputs:**
   - Accept output from all atomic review commands (readability, performance, testing, style,
     architecture, documentation, observability, security)
   - Extract issues, severity levels, file locations, and suggestions
   - Extract positive highlights from each review

2. **Deduplicate overlapping issues:**
   - Identify issues flagged by multiple reviews (same file and line range)
   - Example: Missing input validation flagged by both `/review:security` and `/review:testing`
   - Keep the issue with more detailed reasoning and concrete fix suggestion
   - Preserve context from all perspectives that flagged the issue

3. **Organize by severity:**
   - Critical → Major → Minor → Enhancement
   - Within each severity, group by file for readability
   - Maintain file:line-range format for easy navigation

4. **Generate high-level summary:**
   - Product impact: What this change delivers for users (2-3 sentences)
   - Engineering approach: Key patterns/frameworks used
   - Overall assessment: Strengths and areas for improvement

5. **Compile positive highlights:**
   - Aggregate 2-3 most significant positive patterns from all reviews
   - Balance critical feedback with recognition of good practices
   - Highlight well-implemented aspects across different perspectives

6. **Add reasoning:**
   - Ensure all issues include reasoning explaining why they matter
   - Provide concrete, actionable fix suggestions
   - Maintain professional, concise tone

7. **Format final report:**
   - Clean markdown output
   - Easy to scan structure
   - Ready for GitHub posting or local review

## Output Format

```markdown
# Comprehensive Code Review Report

## Summary
[2-3 sentences describing product impact and engineering approach]

**Overall Assessment:**
[1-2 sentences on code quality, strengths, and primary concerns]

## Issues by Severity

### Critical
- **File:** `path/to/file.ext:line-range`
  - **Perspective:** [Which review(s) flagged this]
  - **Issue:** [Clear description]
  - **Reasoning:** [Why this matters]
  - **Fix:** [Concrete suggestion]

### Major
[Same structure]

### Minor
[Same structure]

### Enhancement
[Positive patterns and optional improvements]

## Highlights
- [Positive observation 1 from across all reviews]
- [Positive observation 2 from across all reviews]
- [Positive observation 3 from across all reviews]

## Review Coverage
- ✓ Readability
- ✓ Performance
- ✓ Testing
- ✓ Style
- ✓ Architecture
- ✓ Documentation
- ✓ Observability
- ✓ Security

**Total Issues:** X Critical, Y Major, Z Minor, W Enhancements
```

## Agent Integration

**Primary Agent:** reviewer - Synthesizes findings from multiple review perspectives

**Related Agents:**

- implementation-strategy-specialist - Can suggest prioritization and execution order for fixes

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts summary as top-level PR comment
- Links to individual perspective comments
- Includes severity counts and highlights

## Examples

### Example: Synthesizing Multiple Reviews

```bash
# Typically called by workflow, but can be manual:
/review:synthesize \
  --readability-output=readability-results.md \
  --performance-output=performance-results.md \
  --testing-output=testing-results.md \
  --security-output=security-results.md
```

**Output:**

```markdown
# Comprehensive Code Review Report

## Summary
This change implements a user authentication system with JWT tokens and OAuth 2.0 integration.
Uses Passport.js for authentication strategies, bcrypt for password hashing, and Redis for
token storage.

**Overall Assessment:**
Code is well-structured with good separation of concerns and comprehensive error handling.
Primary concerns are missing test coverage for authentication flows and N+1 query pattern
in user lookup. Security practices are generally sound with one critical issue requiring
immediate attention.

## Issues by Severity

### Critical (2 issues)

- **File:** `src/services/authService.ts:89-110`
  - **Perspective:** Security, Observability
  - **Issue:** No error handling for JWT signing failures, exposes internal errors to clients
  - **Reasoning:** Unhandled exceptions expose stack traces with sensitive information
    (database paths, internal IPs) and crash the authentication service
  - **Fix:**
    ```typescript
    try {
      const token = jwt.sign(payload, process.env.JWT_SECRET);
      logger.info('Token created', { userId: payload.userId });
      return token;
    } catch (error) {
      logger.error('JWT signing failed', { userId: payload.userId, error: error.message });
      throw new AuthError('Authentication failed');
    }
    ```

- **File:** `src/api/auth.ts:67-85`
  - **Perspective:** Performance, Security
  - **Issue:** N+1 query pattern loading user permissions in loop, plus missing rate limiting
  - **Reasoning:** Authentication endpoint called on every request; N+1 pattern causes slow
    response times (5-10s for users with many roles), and missing rate limiting enables
    brute force attacks
  - **Fix:**
    ```typescript
    // Fix N+1 with batch query
    const permissions = await Permission.findAll({
      where: { userId: { [Op.in]: userIds } },
      include: [Role]
    });

    // Add rate limiting
    const limiter = rateLimit({
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 5, // 5 attempts
      message: 'Too many login attempts'
    });
    router.post('/login', limiter, loginHandler);
    ```

### Major (3 issues)

- **File:** `src/services/authService.ts:120-150`
  - **Perspective:** Testing, Architecture
  - **Issue:** No tests for authentication failure scenarios (wrong password, expired token)
    and service violates SRP by handling auth + token management + logging
  - **Reasoning:** Authentication failures are common user scenarios that must work correctly;
    missing tests risk bugs. God class becomes unmaintainable.
  - **Fix:**
    ```typescript
    // Add tests
    test('rejects invalid password', async () => {
      await expect(authenticate('user@test.com', 'wrong')).rejects.toThrow('Invalid credentials');
    });

    // Split responsibilities
    class AuthService {
      constructor(
        private tokenManager: TokenManager,
        private userRepo: UserRepository,
        private logger: Logger
      ) {}
    }
    ```

- **File:** `src/api/auth.ts:45-60`
  - **Perspective:** Documentation, Readability
  - **Issue:** Public API endpoint has no documentation and uses generic variable name `data`
  - **Reasoning:** External teams cannot use API without docs; generic names force code
    reading
  - **Fix:**
    ```typescript
    /**
     * Authenticates user with email and password
     * @route POST /auth/login
     * @param {string} req.body.email - User email
     * @param {string} req.body.password - User password
     * @returns {Object} Auth response with token
     */
    export async function login(req: Request, res: Response) {
      const credentials = req.body; // Rename from 'data' to 'credentials'
      ...
    }
    ```

- **File:** `src/middleware/authorize.ts:67-90`
  - **Perspective:** Observability, Documentation
  - **Issue:** No logging for authorization denials and complex permission logic has no
    explanatory comments
  - **Reasoning:** Impossible to debug why users can't access resources; future maintainers
    won't understand permission hierarchy
  - **Fix:**
    ```typescript
    // Permission hierarchy: admin > manager > user
    // Admins can access all resources
    // Managers can access their team's resources
    if (!hasPermission(user, resource)) {
      logger.warn('Authorization denied', {
        userId: user.id,
        resourceId: resource.id,
        requiredPermission: resource.permission
      });
      throw new ForbiddenError('Access denied');
    }
    ```

### Minor (2 issues)

- **File:** `src/utils/crypto.ts:34`
  - **Perspective:** Style
  - **Issue:** Inconsistent indentation (2 spaces vs 4 spaces)
  - **Reasoning:** Minor readability impact, violates team standards
  - **Fix:** Standardize to 2-space indentation per `.editorconfig`

- **File:** `src/services/tokenService.ts:90`
  - **Perspective:** Observability
  - **Issue:** Using console.log instead of proper logger
  - **Reasoning:** Doesn't support log levels or external aggregation
  - **Fix:** Use structured logger: `logger.info('Token refreshed', { userId })`

### Enhancement (2 suggestions)

- **File:** `src/services/authService.ts:overall`
  - **Perspective:** Architecture, Security
  - **Enhancement:** Excellent use of dependency injection throughout service layer and proper
    bcrypt salt rounds (10) for password hashing
  - **Impact:** Makes code testable and maintains good security practices

- **File:** `src/middleware/*.ts:overall`
  - **Perspective:** Readability, Style
  - **Enhancement:** Consistent naming conventions and clean separation of concerns across all
    middleware
  - **Impact:** Easy to understand and maintain

## Highlights
- **Excellent security practices:** Proper bcrypt password hashing with appropriate salt rounds,
  secure JWT implementation (except noted error handling)
- **Clean architecture:** Good use of dependency injection, separation of concerns in service
  layer, proper middleware organization
- **Well-structured code:** Consistent naming conventions, clear function responsibilities,
  TypeScript types used effectively

## Review Coverage
- ✓ Readability
- ✓ Performance
- ✓ Testing
- ✓ Style
- ✓ Architecture
- ✓ Documentation
- ✓ Observability
- ✓ Security

**Total Issues:** 2 Critical, 3 Major, 2 Minor, 2 Enhancements
**Recommendation:** Address Critical issues before merge. Major issues should be fixed or have tracking tickets created.
```

## Integration Points

- **Follows:** All atomic `/review:*` commands
- **Part of:** `/workflows:run-comprehensive-review` (final synthesis step)
- **Followed by:** Optional save to `.artifacts/reviews/` or post to GitHub PR

## Quality Standards

- **Deduplication:** No redundant issues from multiple perspectives
- **Clarity:** Easy to scan, well-organized report
- **Actionability:** All issues have concrete fix suggestions
- **Balance:** Criticism balanced with positive highlights
- **Completeness:** Coverage of all review perspectives documented
- **Professional tone:** Constructive, helpful feedback
