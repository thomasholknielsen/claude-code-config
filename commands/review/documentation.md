---
description: "Analyze code for documentation quality, comments, and API documentation completeness"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Documentation

## Purpose

Evaluate code changes for documentation quality, comment appropriateness, docstring completeness,
API documentation, and README updates.

## Usage

**Local:** `/review:documentation [feature-branch] [base-branch]`
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

3. **Evaluate against documentation criteria:**
   - Public API documentation completeness (docstrings, JSDoc, etc.)
   - Complex logic explanation (why, not what)
   - Why-not-what comment principle adherence
   - README updates for new features or configuration
   - Configuration documentation
   - Outdated or misleading comments
   - Missing function/class descriptions
   - Parameter and return value documentation
   - Use Context7 MCP for documentation standard best practices (optional)
   - Analyze documentation clarity and accuracy

4. **Report findings with severity and reasoning:**
   - Critical: Missing documentation for public APIs or critical functionality
   - Major: Insufficient documentation hampering understanding or usage
   - Minor: Small documentation gaps or improvements
   - Enhancement: Well-documented, clear code

5. **Include positive observations:**
   - Highlight excellent documentation
   - Acknowledge clear explanatory comments

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key patterns/frameworks used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the documentation gap
  - **Reasoning:** Why this matters (API usability, maintainability, onboarding)
  - **Fix:** Concrete suggestion with documentation example if applicable

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

**Primary Agent:** reviewer - Provides specialized code review guidance for documentation

**Related Agents:**

- documenter - Can generate comprehensive documentation
- research-analysis-specialist - Can research documentation standards

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested documentation

### Path-Specific Triggers

Especially valuable for:

- Public API changes
- New feature implementations
- Configuration changes

## Examples

### Example 1: Local Usage

```bash
/review:documentation feature/auth-api develop
```

**Output:**

```markdown
**High-Level Summary**
This change implements OAuth 2.0 authentication with JWT tokens. Uses Passport.js for
authentication strategies and custom middleware for authorization.

### Critical
- **File:** `src/api/auth.ts:45-80`
  - **Issue:** Public API endpoint `/auth/login` has no documentation explaining parameters or responses
  - **Reasoning:** External developers/teams cannot use API without documentation, blocks adoption
  - **Fix:** Add JSDoc documentation:
    ```typescript
    /**
     * Authenticates user with email and password
     * @route POST /auth/login
     * @param {Object} req.body - Login credentials
     * @param {string} req.body.email - User email address
     * @param {string} req.body.password - User password
     * @returns {Object} Authentication response
     * @returns {string} token - JWT access token
     * @returns {string} refreshToken - Refresh token for renewing access
     * @returns {Object} user - User profile data
     * @throws {401} Invalid credentials
     * @throws {429} Too many login attempts
     */
    export async function login(req: Request, res: Response) { ... }
    ```

- **File:** `README.md` (not updated)
  - **Issue:** README missing documentation for new OAuth authentication feature
  - **Reasoning:** Users won't know new auth system exists or how to configure it
  - **Fix:** Add section to README:
    ```markdown
    ## Authentication

    This API uses OAuth 2.0 with JWT tokens.

    ### Configuration
    Set environment variables:
    - `JWT_SECRET` - Secret key for signing tokens
    - `JWT_EXPIRATION` - Token expiration time (default: 1h)

    ### Usage
    1. Obtain token: `POST /auth/login`
    2. Include in requests: `Authorization: Bearer <token>`
    3. Refresh expired tokens: `POST /auth/refresh`
    ```

### Major
- **File:** `src/middleware/authorize.ts:67-90`
  - **Issue:** Complex permission checking logic with no explanatory comments
  - **Reasoning:** Future maintainers won't understand permission hierarchy, high risk of bugs
  - **Fix:** Add explanatory comment:
    ```typescript
    // Permission hierarchy: admin > manager > user
    // Admins can access all resources
    // Managers can access their team's resources
    // Users can only access their own resources
    function checkPermissions(user: User, resource: Resource): boolean { ... }
    ```

- **File:** `src/services/tokenService.ts:120-145`
  - **Issue:** Function `rotateTokens` has no docstring explaining when/why it's called
  - **Reasoning:** Unclear usage pattern, developers may misuse or duplicate functionality
  - **Fix:** Add docstring:
    ```typescript
    /**
     * Rotates user tokens for enhanced security
     * Called automatically when:
     * - Token is 80% expired
     * - User changes password
     * - Suspicious activity detected
     *
     * @param userId - User ID to rotate tokens for
     * @returns New token pair (access + refresh)
     */
    async function rotateTokens(userId: string) { ... }
    ```

### Minor
- **File:** `src/utils/crypto.ts:34`
  - **Issue:** Comment states "hash password" but code actually hashes with salt
  - **Reasoning:** Misleading comment causes confusion about security implementation
  - **Fix:** Update comment: `// Hash password with bcrypt salt (10 rounds)`

- **File:** `src/config/auth.config.ts:12-20`
  - **Issue:** Configuration options lack inline documentation
  - **Reasoning:** Developers unclear about valid values or impact of options
  - **Fix:** Add inline comments:
    ```typescript
    export const authConfig = {
      // JWT token lifespan (e.g., '1h', '30m', '7d')
      tokenExpiration: '1h',

      // Bcrypt cost factor (10-12 recommended, higher = slower but more secure)
      saltRounds: 10,

      // Maximum failed login attempts before account lockout
      maxLoginAttempts: 5
    };
    ```

**Highlights:**
- Excellent JSDoc documentation for all public utility functions
- Clear README structure with helpful examples
- Good use of explanatory comments for complex algorithms
```

### Example 2: GitHub Actions (Automatic)

Triggered automatically when PR is opened or synchronized. Posts inline comments and summary.

## Integration Points

- **Follows:** Git operations (fetch, diff)
- **Followed by:** `/review:synthesize` (aggregates findings)
- **Part of:** `/workflows:run-comprehensive-review` (orchestrated execution)
- **Related:** Other `/review:*` commands for comprehensive coverage

## Quality Standards

- **Accuracy:** Identify real documentation gaps affecting usability
- **Actionability:** Every issue has concrete documentation suggestion
- **Reasoning:** Explain impact on maintainability and developer experience
- **Positivity:** Include highlights for well-documented code
- **Consistency:** Follow severity definitions strictly
- **Context-awareness:** Understand public vs private APIs, complexity levels
