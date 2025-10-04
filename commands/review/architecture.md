---
description: "Analyze code for architectural design, SOLID principles, and system design patterns"
category: "review"
agent: "reviewer"
tools: ["Grep", "Glob", "Bash", "Read", "Context7"]
complexity: "moderate"
github_integration: true
---

# Command: Review Architecture

## Purpose

Evaluate code changes for architectural design quality, SOLID principles adherence, design patterns
appropriateness, coupling/cohesion concerns, and system design decisions.

## Usage

**Local:** `/review:architecture [feature-branch] [base-branch]`
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

3. **Parallel Architecture Analysis:**
   Launch concurrent specialized architecture review tasks:

   ```python
   # SOLID principles evaluation
   Task("Review SOLID principles adherence: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion")

   # Design patterns and structure
   Task("Analyze design pattern appropriateness (Factory, Strategy, Observer, etc.), module coupling/cohesion, and separation of concerns")

   # System boundaries and dependencies
   Task("Evaluate layer/boundary violations, dependency direction, circular dependencies, and integration with existing architecture")

   # Data model architecture
   Task("Review data model design for entity relationships, domain modeling, repository patterns, aggregate boundaries, and ORM mapping strategies")

   # Service architecture
   Task("Assess service layer design, API boundaries, microservices communication patterns, and event-driven architecture if applicable")
   ```

4. **Evaluate against architecture criteria:**
   - Single Responsibility Principle (SRP) adherence
   - Open/Closed Principle compliance
   - Liskov Substitution Principle violations
   - Interface Segregation violations
   - Dependency Inversion implementation
   - Design pattern appropriateness (Factory, Strategy, Observer, etc.)
   - Module coupling and cohesion
   - Separation of concerns
   - Layer/boundary violations
   - Dependency direction and circular dependencies
   - Data model architecture (entity relationships, domain modeling, repository patterns)
   - Service architecture (API boundaries, microservices patterns, event-driven design)
   - Use Context7 MCP for architectural pattern best practices
   - Analyze fit within existing system architecture

5. **Report findings with severity and reasoning:**
   - Critical: Architectural violations breaking system integrity or maintainability
   - Major: Significant design issues creating technical debt
   - Minor: Small architectural improvements
   - Enhancement: Well-designed, maintainable architecture

6. **Include positive observations:**
   - Highlight excellent architectural decisions
   - Acknowledge proper use of design patterns

## Output Format

**High-Level Summary** (2-3 sentences)

- Product impact: What this change delivers for users
- Engineering approach: Key patterns/frameworks used

### Critical

- **File:** `path/to/file.ext:45-52`
  - **Issue:** Clear, concise description of the architectural problem
  - **Reasoning:** Why this matters (maintainability, scalability, technical debt)
  - **Fix:** Concrete suggestion with architectural improvement if applicable

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

**Primary Agent:** reviewer - Provides specialized code review guidance for architecture

**Related Agents:**

- research-analysis-specialist - Can research architectural patterns
- implementation-strategy-specialist - Can suggest refactoring strategies

## GitHub Integration

### Automated Posting

When run via GitHub Actions:

- Posts inline comments for Critical/Major issues
- Posts summary comment with all findings
- Includes reasoning and suggested architectural improvements

### Path-Specific Triggers

Especially valuable for:

- New feature implementations
- Service layer changes
- Infrastructure code

## Examples

### Example 1: Local Usage

```bash
/review:architecture feature/notification-system develop
```

**Output:**

```markdown
**High-Level Summary**
This change implements a multi-channel notification system (email, SMS, push). Uses Strategy
pattern for channel abstraction and Factory for channel creation.

### Critical
- **File:** `src/services/NotificationService.ts:45-120`
  - **Issue:** Service violates SRP by handling notification creation, delivery, logging, and retry logic
  - **Reasoning:** God class becomes unmaintainable, hard to test, changes in one responsibility break others
  - **Fix:** Split into focused classes:
    ```typescript
    class NotificationService {
      constructor(
        private factory: NotificationChannelFactory,
        private sender: NotificationSender,
        private logger: NotificationLogger
      ) {}
    }
    ```

- **File:** `src/api/controllers/NotificationController.ts:89-100`
  - **Issue:** Controller directly instantiates database repositories, violating Dependency Inversion
  - **Reasoning:** Tight coupling prevents testing, makes changes brittle, violates SOLID principles
  - **Fix:** Use dependency injection:
    ```typescript
    constructor(
      private notificationRepo: INotificationRepository,
      private userRepo: IUserRepository
    ) {}
    ```

### Major
- **File:** `src/services/EmailService.ts:67-85`
  - **Issue:** Circular dependency between EmailService ↔ UserService
  - **Reasoning:** Creates fragile coupling, can cause initialization issues, hard to reason about flow
  - **Fix:** Introduce EventBus to decouple:
    ```typescript
    // EmailService emits events
    eventBus.emit('user.updated', userId);

    // UserService subscribes
    eventBus.on('user.updated', (userId) => { ... });
    ```

- **File:** `src/models/User.ts:120-150`
  - **Issue:** User model contains business logic for notifications (violates separation of concerns)
  - **Reasoning:** Models should be data containers, business logic belongs in services, violates layered architecture
  - **Fix:** Move logic to NotificationService:
    ```typescript
    class NotificationService {
      async notifyUser(user: User, message: string) {
        // Business logic here
      }
    }
    ```

- **File:** `src/services/NotificationFactory.ts:34-50`
  - **Issue:** Factory uses string switching instead of polymorphism
  - **Reasoning:** Violates Open/Closed Principle, requires modification for new channels
  - **Fix:** Use strategy registry:
    ```typescript
    class ChannelRegistry {
      private channels = new Map<string, INotificationChannel>();

      register(type: string, channel: INotificationChannel) {
        this.channels.set(type, channel);
      }

      get(type: string): INotificationChannel {
        return this.channels.get(type);
      }
    }
    ```

### Minor
- **File:** `src/interfaces/INotificationChannel.ts:12-18`
  - **Issue:** Interface has unused method `getMetadata()` violating Interface Segregation
  - **Reasoning:** Clients shouldn't depend on methods they don't use
  - **Fix:** Split into separate interfaces:
    ```typescript
    interface INotificationChannel {
      send(message: Message): Promise<void>;
    }

    interface IChannelMetadata {
      getMetadata(): ChannelMetadata;
    }
    ```

**Highlights:**
- Excellent use of Strategy pattern for channel abstraction
- Clean separation between domain and infrastructure layers
- Proper dependency injection throughout service layer
```

### Example 2: GitHub Actions (Automatic)

Triggered automatically when PR is opened or synchronized. Posts inline comments and summary.

## Integration Points

- **Follows:** Git operations (fetch, diff)
- **Followed by:** `/review:synthesize` (aggregates findings)
- **Part of:** `/workflows:run-comprehensive-review` (orchestrated execution)
- **Related:** Other `/review:*` commands for comprehensive coverage

## Quality Standards

- **Accuracy:** Identify real architectural issues, not nitpicks
- **Actionability:** Every issue has concrete refactoring suggestion
- **Reasoning:** Explain long-term impact on maintainability and scalability
- **Positivity:** Include highlights for well-architected code
- **Consistency:** Follow severity definitions strictly
- **Context-awareness:** Understand existing system architecture and constraints
