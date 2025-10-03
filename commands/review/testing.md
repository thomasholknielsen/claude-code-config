---
description: "Analyze code for test coverage, edge cases, and test quality"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Testing

## Purpose

Evaluate code changes for test coverage completeness, edge case handling, test quality, and testing
best practices adherence.

## Usage

**Local:** `/review:testing [feature-branch] [base-branch]`
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

3. **Evaluate against testing criteria:**
   - Unit test coverage for new code paths
   - Edge case testing (null, empty, boundary values)
   - Integration test completeness for end-to-end flows
   - Mock/stub quality and appropriateness
   - Test naming clarity and descriptiveness
   - Assertion meaningfulness and specificity
   - Test isolation and independence
   - Test performance (avoid slow tests)
   - Use Context7 MCP for testing framework best practices (optional)
   - Analyze test coverage in relation to code complexity

4. **Report findings with severity and reasoning:**
   - Critical: Missing tests for critical functionality or security checks
   - Major: Insufficient coverage for important paths or edge cases
   - Minor: Small gaps in test coverage or test quality improvements
   - Enhancement: Well-written, comprehensive tests

5. **Include positive observations:**
   - Highlight thorough test coverage
   - Acknowledge well-designed test cases

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key patterns/frameworks used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the testing gap
  - **Reasoning:** Why this matters (risk of bugs, user impact, data integrity)
  - **Fix:** Concrete suggestion with test case example if applicable

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

**Primary Agent:** reviewer - Provides specialized code review guidance for testing

**Related Agents:**

- test-writer - Can generate comprehensive test suites
- research-analysis-specialist - Can research testing strategies

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested test cases

### Path-Specific Triggers

Especially valuable for:

- New feature implementations
- Bug fixes (should have regression tests)
- Critical business logic

## Examples

### Example 1: Local Usage

```bash
/review:testing feature/payment-gateway develop
```

**Output:**

```markdown
**High-Level Summary**
This change integrates Stripe payment processing with refund capability. Uses async payment
confirmation and webhook handling.

### Critical
- **File:** `src/services/paymentService.ts:89-120`
  - **Issue:** No tests for payment failure scenarios (declined cards, insufficient funds)
  - **Reasoning:** Payment failures are common (5-15% of attempts) and must handle gracefully to prevent revenue loss
  - **Fix:** Add tests:
    ```typescript
    test('handles declined card gracefully', async () => {
      mockStripe.charges.create.mockRejectedValue(new Error('card_declined'));
      await expect(processPayment(order)).rejects.toThrow('Payment declined');
      expect(order.status).toBe('payment_failed');
    });
    ```

- **File:** `src/services/refundService.ts:45-67`
  - **Issue:** No tests for partial refund edge cases (refund > original amount)
  - **Reasoning:** Financial bugs cause legal/compliance issues and customer disputes
  - **Fix:** Add boundary tests:
    ```typescript
    test('rejects refund exceeding original amount', async () => {
      const order = { amount: 100 };
      await expect(refund(order, 150)).rejects.toThrow('Refund exceeds payment');
    });
    ```

### Major
- **File:** `src/api/checkout.ts:120-150`
  - **Issue:** Missing integration test for complete checkout flow (cart → payment → confirmation)
  - **Reasoning:** Individual unit tests exist but no end-to-end validation, critical path untested
  - **Fix:** Add integration test:
    ```typescript
    test('complete checkout flow', async () => {
      const cart = await createCart([item1, item2]);
      const payment = await processPayment(cart, cardToken);
      expect(payment.status).toBe('succeeded');
      const order = await confirmOrder(payment.id);
      expect(order.status).toBe('confirmed');
    });
    ```

- **File:** `src/utils/validator.ts:34-50`
  - **Issue:** Test only checks valid emails, missing invalid email tests
  - **Reasoning:** Validators must prove they reject bad input, not just accept good input
  - **Fix:** Add negative tests:
    ```typescript
    test.each(['invalid', '@test.com', 'test@', 'test..@test.com'])(
      'rejects invalid email: %s',
      (email) => expect(validateEmail(email)).toBe(false)
    );
    ```

### Minor
- **File:** `tests/paymentService.test.ts:78`
  - **Issue:** Test name `test('it works')` is not descriptive
  - **Reasoning:** Unclear test names make failures hard to diagnose
  - **Fix:** Rename to: `test('processes successful payment and updates order status')`

**Highlights:**
- Excellent use of test fixtures for consistent test data
- Comprehensive mock setup prevents external API calls in tests
- Good test isolation - each test is independent
```

### Example 2: GitHub Actions (Automatic)

Triggered automatically when PR is opened or synchronized. Posts inline comments and summary.

## Integration Points

- **Follows:** Git operations (fetch, diff)
- **Followed by:** `/review:synthesize` (aggregates findings)
- **Part of:** `/workflows:run-comprehensive-review` (orchestrated execution)
- **Related:** Other `/review:*` commands for comprehensive coverage

## Quality Standards

- **Accuracy:** Identify real gaps, not cosmetic test additions
- **Actionability:** Every issue has concrete test case suggestion
- **Reasoning:** Explain risk of insufficient testing with real scenarios
- **Positivity:** Include highlights for well-tested code
- **Consistency:** Follow severity definitions strictly
- **Context-awareness:** Understand criticality of code being tested
