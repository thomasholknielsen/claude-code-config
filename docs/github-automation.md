# GitHub Actions Integration for AI Code Review

## Overview

This guide explains how to set up and use the AI Code Review system's GitHub Actions integration for automated pull request reviews.

## Prerequisites

- GitHub repository with Actions enabled
- Anthropic API key for Claude access
- GitHub token with PR comment permissions
- `gh` CLI installed (for local integration)

## Setup

### 1. Add GitHub Secrets

Navigate to your repository settings and add the following secrets:

```text
Settings → Secrets and variables → Actions → New repository secret
```

Required secrets:

- `ANTHROPIC_API_KEY` - Your Anthropic API key for Claude access
- `GITHUB_TOKEN` - Automatically provided by GitHub Actions (no setup needed)

### 2. Copy Workflow File

Copy `.github/workflows/ai-code-review.yml` from this repository to your project:

```bash
mkdir -p .github/workflows
cp /path/to/claude-code-system/.github/workflows/ai-code-review.yml .github/workflows/
```

### 3. Commit and Push

```bash
git add .github/workflows/ai-code-review.yml
git commit -m "feat(ci): add AI code review workflow"
git push
```

## Workflow Components

The GitHub Actions workflow includes 4 jobs:

### 1. Main AI Review Job

**Triggers:** Every PR open or synchronize
**What it does:**

- Analyzes changed files
- Runs applicable review perspectives (readability, performance, testing, security, style, architecture, documentation, observability)
- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings

**File type detection:**

- JavaScript/TypeScript: All perspectives + design
- Python/Java/Go: All perspectives except design
- SQL: Performance, security, readability
- UI files (`.jsx`, `.tsx`, `.vue`): Includes design review

### 2. Deep Security Review

**Triggers:** PRs touching security-critical paths:

- `auth/`
- `api/security/`
- `middleware/auth/`
- `crypto/`
- `password/`

**What it does:**

- Performs OWASP Top 10 security audit
- Checks authentication/authorization
- Validates input sanitization
- Reviews secrets management
- Flags Critical security issues

### 3. Deep Performance Review

**Triggers:** PRs touching performance-critical paths:

- `database/`
- `queries/`
- `.sql` files
- `api/`
- `cache/`

**What it does:**

- Identifies N+1 query patterns
- Checks for missing indexes
- Reviews algorithm complexity
- Analyzes memory usage
- Flags performance bottlenecks

### 4. Enhanced External Contributor Review

**Triggers:** PRs from forked repositories

**What it does:**

- Applies stricter review criteria
- Security vulnerabilities flagged as Critical
- Requires tests for all new code
- Requires documentation for public APIs
- Checks for breaking changes

## Local Integration

### Running Reviews Locally

1. **Run comprehensive review:**

   ```bash
   cd your-project
   /workflows:run-comprehensive-review feature/my-changes develop
   ```

2. **Save output to file:**

   ```bash
   /workflows:run-comprehensive-review feature/my-changes develop > review-output.md
   ```

3. **Post to GitHub PR:**

   ```bash
   python scripts/github-review-integration.py --pr 123 --review review-output.md
   ```

### Prerequisites for Local Integration

**Install GitHub CLI:**

```bash
# macOS
brew install gh

# Windows
winget install GitHub.cli

# Linux
sudo apt install gh  # Ubuntu/Debian
```

**Authenticate:**

```bash
gh auth login
```

### Script Usage

The `github-review-integration.py` script:

- Parses review markdown output
- Extracts issues by severity
- Posts inline comments for Critical/Major
- Generates summary comment with severity counts

```bash
python scripts/github-review-integration.py \
  --pr 123 \
  --review review-output.md \
  --repo owner/repo  # optional, auto-detected
```

## Review Output Format

### PR Summary Comment

```markdown
## 🤖 AI Code Review Summary

**Review completed at:** 2025-10-01 14:30:00 UTC

### Findings Overview
- 🔴 **Critical:** 2 issues
- 🟠 **Major:** 5 issues
- 🟡 **Minor:** 3 issues
- 🟢 **Enhancement:** 2 suggestions

### Highlights
- Excellent separation of concerns in service layer
- Comprehensive error logging with correlation IDs
- Well-documented API endpoints

### Next Steps
1. Address Critical issues immediately (blocking merge)
2. Review Major issues before merge
3. Consider Minor improvements and Enhancements
```

### Inline Comments

For each Critical/Major issue:

```markdown
**Critical**: Missing null check on user input could cause crash

**Reasoning:** Input from external API may be null/undefined, causing TypeError

**Suggested Fix:**
if (!userData) throw new Error('Invalid user data')

---
*Posted by AI Code Review*
```

## Customization

### Adjust File Paths

Edit `.github/workflows/ai-code-review.yml` to match your project structure:

```yaml
security-review:
  if: |
    contains(github.event.pull_request.changed_files, 'your-auth-path/') ||
    contains(github.event.pull_request.changed_files, 'your-security-path/')
```

### Modify Review Criteria

Update the prompts in the workflow file to emphasize specific concerns:

```yaml
prompt: |
  Focus especially on:
  - Database query performance
  - API response times
  - Memory usage patterns
```

### Ignore Certain Files

Add to `paths-ignore` in workflow:

```yaml
on:
  pull_request:
    paths-ignore:
      - '**.md'
      - 'docs/**'
      - '.artifacts/**'
      - 'tests/**'  # Add your patterns
```

## Troubleshooting

### Workflow Not Triggering

**Check:**

- Workflow file is in `.github/workflows/`
- GitHub Actions are enabled for repository
- Branch protection rules aren't blocking Actions

### Review Comments Not Posting

**Check:**

- `ANTHROPIC_API_KEY` secret is set correctly
- GitHub token has PR write permissions
- Check Actions logs for error messages

### Rate Limiting

**Symptoms:** API errors, timeouts
**Solutions:**

- Reduce review frequency (only on specific paths)
- Add rate limiting to workflow
- Use caching for repeated reviews

### False Positives

**Solutions:**

- Refine prompts in workflow file
- Add project-specific context to prompts
- Use `.reviewignore` file (custom implementation)

## Performance Optimization

### Reduce API Costs

1. **Run only on specific paths:**

   ```yaml
   paths:
     - 'src/**'
     - 'api/**'
   ```

2. **Skip certain file types:**

   ```yaml
   paths-ignore:
     - '**.test.js'
     - '**.spec.ts'
   ```

3. **Use caching:**

   ```yaml
   - uses: actions/cache@v3
     with:
       path: ~/.review-cache
       key: review-${{ github.sha }}
   ```

### Speed Up Reviews

- Parallel jobs run simultaneously (4 jobs max)
- Each job completes in 2-5 minutes
- Total workflow time: ~5-7 minutes

## Best Practices

### When to Use

✅ **Use for:**

- All PRs (basic review)
- Security-critical changes (deep security scan)
- Performance-critical changes (deep performance scan)
- External contributions (enhanced review)

❌ **Skip for:**

- Documentation-only PRs
- Configuration changes
- Test file updates (unless logic changed)

### Review Workflow

1. **Developer**: Create PR
2. **AI Review**: Runs automatically within 5 minutes
3. **Developer**: Address Critical/Major issues
4. **Human Reviewer**: Focus on high-level design and business logic
5. **Merge**: After AI + human approval

### Integration with Human Reviews

AI reviews **complement** human reviews:

- **AI handles:** Mechanical checks (formatting, common patterns, obvious bugs)
- **Humans handle:** Business logic, design decisions, architecture trade-offs

## Examples

### Example 1: Full Stack Feature

**PR:** Adding user authentication with JWT

**AI Review Results:**

- ✓ Detected: Missing rate limiting (Security - Critical)
- ✓ Detected: N+1 query in user lookup (Performance - Major)
- ✓ Detected: Missing tests for auth failures (Testing - Major)
- ✓ Highlighted: Good use of bcrypt for passwords (Enhancement)

**Outcome:** Developer fixed Critical/Major issues, PR approved

### Example 2: Backend API Changes

**PR:** Optimizing database queries

**AI Review Results:**

- ✓ Deep performance scan triggered (database/ path)
- ✓ Detected: Missing index on frequently queried column (Major)
- ✓ Detected: Potential memory leak in loop (Critical)
- ✓ Highlighted: Excellent use of connection pooling (Enhancement)

**Outcome:** Critical issue fixed, index added, PR approved

### Example 3: External Contributor

**PR:** Community feature contribution

**AI Review Results:**

- ✓ Enhanced review applied (stricter criteria)
- ✓ Detected: Missing tests (Major - required for external PRs)
- ✓ Detected: No API documentation (Major)
- ✓ Approved: Security checks passed

**Outcome:** Contributor added tests + docs, PR approved

## Additional Resources

- [Anthropic Claude Code Action Documentation](https://github.com/anthropics/claude-code-action)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [Repository: Typical Workflows](./typical-workflows.md)

## Support

For issues or questions:

1. Check Actions logs in GitHub UI
2. Review troubleshooting section above
3. Test locally with `/workflows:run-comprehensive-review`
4. Verify secrets and permissions
