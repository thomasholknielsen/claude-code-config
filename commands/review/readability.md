---
description: "Analyze code for readability, naming clarity, and maintainability issues"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Readability

## Purpose

Evaluate code changes for readability-related issues, naming conventions, maintainability concerns,
and adherence to DRY principles.

## Usage

**Local:** `/review:readability [feature-branch] [base-branch]`
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

3. **Evaluate against readability criteria:**
   - Variable/function/class naming clarity and consistency
   - Code structure and logical organization
   - Duplicate code violations (DRY principle)
   - Complex logic requiring simplification
   - Confusing or convoluted code sections
   - Magic numbers and hardcoded values
   - Function/method length and complexity
   - Use Context7 MCP for latest language-specific naming conventions (optional)
   - Analyze in context of surrounding code and usage patterns

4. **Report findings with severity and reasoning:**
   - Critical: Code so unclear it will cause bugs or maintenance disasters
   - Major: Significant readability issues hampering understanding
   - Minor: Small improvements to clarity
   - Enhancement: Well-written, clear code patterns

5. **Include positive observations:**
   - Highlight well-named variables/functions
   - Acknowledge clear code structure

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key patterns/frameworks used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the readability problem
  - **Reasoning:** Why this matters (impact on maintainability, bug risk, team productivity)
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

**Primary Agent:** reviewer - Provides specialized code review guidance for readability

**Related Agents:**

- research-analysis-specialist - Can research readability best practices for specific languages
- implementation-strategy-specialist - Can suggest refactoring strategies

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested fixes

### Path-Specific Triggers

Can be configured to run on all code files or specific paths.

## Examples

### Example 1: Local Usage

```bash
/review:readability feature/user-profile develop
```

**Output:**

```markdown
**High-Level Summary**
This change adds user profile management with avatar uploads. Uses React hooks and TypeScript for type safety.

### Critical
- **File:** `src/components/UserProfile.tsx:89-102`
  - **Issue:** Function `processData` with 5 nested callbacks is incomprehensible
  - **Reasoning:** Deeply nested callbacks create "callback hell" making logic impossible to follow, high bug risk
  - **Fix:** Refactor to async/await: `const result = await fetchUser(); const processed = await processUser(result);`

### Major
- **File:** `src/utils/helpers.ts:34-45`
  - **Issue:** Function named `doStuff` provides no information about its purpose
  - **Reasoning:** Generic names force developers to read implementation, slowing development
  - **Fix:** Rename to `calculateUserAgeFromBirthdate` to clearly convey purpose

- **File:** `src/components/UserProfile.tsx:120-135`
  - **Issue:** Duplicate validation logic appears in 3 different components
  - **Reasoning:** Violates DRY principle, changes require updating 3 locations, high risk of inconsistency
  - **Fix:** Extract to shared validator: `export const validateEmail = (email: string) => { ... }`

### Minor
- **File:** `src/components/Avatar.tsx:23`
  - **Issue:** Magic number `86400` with no explanation
  - **Reasoning:** Unclear what 86400 represents, reduces code clarity
  - **Fix:** Use named constant: `const SECONDS_PER_DAY = 86400;`

**Highlights:**
- Excellent use of descriptive variable names in `calculateSubscriptionPrice`
- Clear component structure with well-separated concerns
```

### Example 2: GitHub Actions (Automatic)

Triggered automatically when PR is opened or synchronized. Posts inline comments and summary.

## Integration Points

- **Follows:** Git operations (fetch, diff)
- **Followed by:** `/review:synthesize` (aggregates findings)
- **Part of:** `/workflows:run-comprehensive-review` (orchestrated execution)
- **Related:** Other `/review:*` commands for comprehensive coverage

## Quality Standards

- **Accuracy:** No false positives (validate issues in context)
- **Actionability:** Every issue has concrete fix suggestion
- **Reasoning:** Explain why each issue matters for maintainability
- **Positivity:** Include highlights for well-written code
- **Consistency:** Follow severity definitions strictly
- **Context-awareness:** Understand surrounding code and project patterns
