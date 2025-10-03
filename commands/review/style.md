---
description: "Analyze code for style consistency, formatting, and coding standards adherence"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Style

## Purpose

Evaluate code changes for style consistency, formatting standards, naming conventions, and
adherence to project coding standards.

## Usage

**Local:** `/review:style [feature-branch] [base-branch]`
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

3. **Evaluate against style criteria:**
   - Code formatting consistency (indentation, spacing)
   - Import ordering and organization
   - Naming conventions (camelCase, snake_case, PascalCase adherence)
   - Indentation and whitespace consistency
   - Linter/formatter compliance (ESLint, Prettier, Black, etc.)
   - Language-specific idioms and conventions
   - File/folder naming conventions
   - Line length limits
   - Use Context7 MCP for language-specific style guides (optional)
   - Analyze against project's established patterns

4. **Report findings with severity and reasoning:**
   - Critical: Style violations breaking builds or CI pipelines
   - Major: Significant inconsistencies hampering readability
   - Minor: Small style inconsistencies
   - Enhancement: Well-formatted, consistent code

5. **Include positive observations:**
   - Highlight excellent code formatting
   - Acknowledge adherence to style guides

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key patterns/frameworks used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the style violation
  - **Reasoning:** Why this matters (build failures, team consistency, code review friction)
  - **Fix:** Concrete suggestion with formatted code example if applicable

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

**Primary Agent:** reviewer - Provides specialized code review guidance for style

**Related Agents:**

- research-analysis-specialist - Can research style guide best practices
- implementation-strategy-specialist - Can suggest refactoring for style consistency

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested fixes

### Path-Specific Triggers

Runs on all code files to ensure consistency.

## Examples

### Example 1: Local Usage

```bash
/review:style feature/user-dashboard develop
```

**Output:**

```markdown
**High-Level Summary**
This change adds a new user dashboard with analytics widgets. Uses React components and TypeScript for type safety.

### Critical
- **File:** `src/components/Dashboard.tsx:12-20`
  - **Issue:** Mixed single and double quotes violates project ESLint rule
  - **Reasoning:** Breaks CI build with linter errors, blocks merge
  - **Fix:** Run `npm run lint --fix` or manually standardize to double quotes per project config

### Major
- **File:** `src/utils/formatters.ts:45-60`
  - **Issue:** Inconsistent indentation (2 spaces in some places, 4 in others)
  - **Reasoning:** Makes code harder to read, violates team standards, creates unnecessary diff noise
  - **Fix:** Standardize to 2-space indentation per `.editorconfig`:
    ```typescript
    export function formatCurrency(amount: number): string {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
      }).format(amount);
    }
    ```

- **File:** `src/api/userService.ts:89-95`
  - **Issue:** Imports not organized by convention (external, internal, relative)
  - **Reasoning:** Inconsistent import order creates confusion, violates project style guide
  - **Fix:** Reorder imports:
    ```typescript
    // External dependencies
    import { Request, Response } from 'express';
    import axios from 'axios';

    // Internal modules
    import { UserRepository } from '@/repositories/UserRepository';

    // Relative imports
    import { validateUser } from './validators';
    ```

### Minor
- **File:** `src/components/Widget.tsx:34`
  - **Issue:** Line exceeds 120 character limit (145 characters)
  - **Reasoning:** Long lines require horizontal scrolling, minor readability impact
  - **Fix:** Break into multiple lines:
    ```typescript
    const result = await fetchUserData(
      userId,
      options.includeHistory,
      options.includePreferences
    );
    ```

- **File:** `src/utils/helpers.ts:67`
  - **Issue:** Function name uses snake_case instead of camelCase
  - **Reasoning:** Inconsistent with JavaScript/TypeScript conventions, minor but noticeable
  - **Fix:** Rename `calculate_total` to `calculateTotal`

**Highlights:**
- Excellent consistent use of TypeScript types throughout
- Perfect spacing and formatting in React components
- Clean import organization in most files
```

### Example 2: GitHub Actions (Automatic)

Triggered automatically when PR is opened or synchronized. Posts inline comments and summary.

## Integration Points

- **Follows:** Git operations (fetch, diff)
- **Followed by:** `/review:synthesize` (aggregates findings)
- **Part of:** `/workflows:run-comprehensive-review` (orchestrated execution)
- **Related:** Other `/review:*` commands for comprehensive coverage

## Quality Standards

- **Accuracy:** Only flag violations of established project standards
- **Actionability:** Every issue has concrete fix suggestion
- **Reasoning:** Explain why consistency matters for team productivity
- **Positivity:** Include highlights for well-formatted code
- **Consistency:** Follow severity definitions strictly
- **Context-awareness:** Understand project's specific style guide and linter config
