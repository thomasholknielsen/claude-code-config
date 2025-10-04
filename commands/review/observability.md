---
description: "Analyze code for error handling, logging, monitoring, and observability practices"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Observability

## Purpose

Evaluate code changes for error handling completeness, logging practices, monitoring integration,
tracing capabilities, and overall system observability.

## Usage

**Local:** `/review:observability [feature-branch] [base-branch]`
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

3. **Evaluate against observability criteria:**
   - Error handling completeness and appropriateness
   - Logging at appropriate levels (ERROR, WARN, INFO, DEBUG)
   - Sensitive data in logs (PII, credentials, tokens)
   - Monitoring/metrics integration (Prometheus, Datadog, etc.)
   - Tracing/debugging information (correlation IDs, request IDs)
   - Exception propagation and handling
   - Alerting considerations for critical paths
   - Contextual information in logs
   - Use Context7 MCP for observability framework best practices (optional)
   - Analyze debuggability and troubleshooting readiness

4. **Report findings with severity and reasoning:**
   - Critical: Missing error handling causing crashes or silent failures
   - Major: Insufficient observability hampering debugging or monitoring
   - Minor: Small logging or monitoring improvements
   - Enhancement: Excellent observability practices

5. **Include positive observations:**
   - Highlight robust error handling
   - Acknowledge comprehensive logging

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key patterns/frameworks used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the observability problem
  - **Reasoning:** Why this matters (debugging, monitoring, incident response)
  - **Fix:** Concrete suggestion with logging/error handling example if applicable

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

**Primary Agent:** reviewer - Provides specialized code review guidance for observability

**Related Agents:**

- research-analysis-specialist - Can research observability best practices
- implementation-strategy-specialist - Can suggest error handling strategies

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested improvements

### Path-Specific Triggers

Especially valuable for:

- API endpoints
- Critical business logic
- Infrastructure code
- Error handling paths

## Examples

### Example 1: Local Usage

```bash
/review:observability feature/payment-processing develop
```

**Output:**

```markdown
**High-Level Summary**
This change implements payment processing with Stripe integration. Handles various payment
failure scenarios and webhook processing for async confirmations.

### Critical
- **File:** `src/services/paymentService.ts:89-110`
  - **Issue:** No error handling for Stripe API failures, exceptions propagate uncaught
  - **Reasoning:** Payment failures are common (network issues, API errors) and uncaught
    exceptions crash service, causing revenue loss
  - **Fix:** Add comprehensive error handling:
    ```typescript
    try {
      const charge = await stripe.charges.create({ ... });
      logger.info('Payment succeeded', { chargeId: charge.id, orderId });
    } catch (error) {
      if (error.type === 'StripeCardError') {
        logger.warn('Card declined', { orderId, reason: error.code });
        throw new PaymentDeclinedError(error.message);
      } else if (error.type === 'StripeRateLimitError') {
        logger.error('Stripe rate limit hit', { orderId });
        throw new RateLimitError('Payment system overloaded');
      } else {
        logger.error('Payment failed', { orderId, error: error.message });
        throw new PaymentError('Payment processing failed');
      }
    }
    ```

- **File:** `src/api/webhooks.ts:67-85`
  - **Issue:** Logging payment webhook data including full credit card token (PII exposure)
  - **Reasoning:** Violates PCI compliance, exposes sensitive data in logs, security risk
  - **Fix:** Redact sensitive data:
    ```typescript
    logger.info('Webhook received', {
      event: event.type,
      customerId: event.data.object.customer,
      // Redact sensitive fields
      cardLast4: event.data.object.card.last4,  // ✓ Only last 4 digits
      // ✗ Do NOT log: card.number, card.cvc, full tokens
    });
    ```

### Major
- **File:** `src/services/orderService.ts:120-145`
  - **Issue:** No logging for order state transitions (pending → processing → completed)
  - **Reasoning:** Impossible to debug order issues, no audit trail, customer support blind
  - **Fix:** Add state transition logging:
    ```typescript
    async function updateOrderStatus(orderId: string, newStatus: OrderStatus) {
      const oldStatus = order.status;
      order.status = newStatus;
      await order.save();

      logger.info('Order status changed', {
        orderId,
        oldStatus,
        newStatus,
        userId: order.userId,
        timestamp: new Date().toISOString()
      });

      // Emit metric for monitoring
      metrics.increment('order.status.changed', { status: newStatus });
    }
    ```

- **File:** `src/api/orders.ts:89-105`
  - **Issue:** No request correlation ID for distributed tracing across services
  - **Reasoning:** Multi-service requests impossible to trace end-to-end, debugging nightmares
  - **Fix:** Add correlation ID:
    ```typescript
    app.use((req, res, next) => {
      req.correlationId = req.headers['x-correlation-id'] || uuidv4();
      res.setHeader('x-correlation-id', req.correlationId);

      // Add to all log entries
      logger.child({ correlationId: req.correlationId });
      next();
    });
    ```

- **File:** `src/services/inventoryService.ts:67-80`
  - **Issue:** Silent failure when inventory update fails, no error thrown or logged
  - **Reasoning:** Causes inventory drift, overselling, customer complaints, revenue loss
  - **Fix:** Log and throw error:
    ```typescript
    const result = await updateInventory(productId, quantity);
    if (!result.success) {
      logger.error('Inventory update failed', {
        productId,
        quantity,
        error: result.error
      });
      throw new InventoryError(`Failed to update inventory for ${productId}`);
    }
    ```

### Minor
- **File:** `src/utils/logger.ts:34`
  - **Issue:** Using console.log instead of proper logger
  - **Reasoning:** console.log doesn't support log levels, formatting, or external aggregation
  - **Fix:** Use structured logger: `logger.info('message', { context })`

- **File:** `src/services/emailService.ts:90`
  - **Issue:** Logging at ERROR level for non-critical email send failures
  - **Reasoning:** Clutters error logs, desensitizes team to real errors, should be WARN
  - **Fix:** Change to WARN level: `logger.warn('Email send failed, will retry', { ... })`

**Highlights:**
- Excellent use of structured logging with contextual data throughout
- Proper error classes with specific types (PaymentError, ValidationError, etc.)
- Good monitoring integration with metrics for critical operations
```

### Example 2: GitHub Actions (Automatic)

Triggered automatically when PR is opened or synchronized. Posts inline comments and summary.

## Integration Points

- **Follows:** Git operations (fetch, diff)
- **Followed by:** `/review:synthesize` (aggregates findings)
- **Part of:** `/workflows:run-comprehensive-review` (orchestrated execution)
- **Related:** Other `/review:*` commands for comprehensive coverage

## Quality Standards

- **Accuracy:** Identify real observability gaps affecting operations
- **Actionability:** Every issue has concrete logging/error handling suggestion
- **Reasoning:** Explain impact on debugging, monitoring, and incident response
- **Positivity:** Include highlights for well-instrumented code
- **Consistency:** Follow severity definitions strictly
- **Context-awareness:** Understand criticality and failure modes of code
