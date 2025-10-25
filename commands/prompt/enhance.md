---
description: "Transform prompts using S-tier frameworks and proven enhancement patterns"
argument-hint: "\"user prompt text\" [--framework=risen|costar|ape|auto] [--mode=quick|complete] | TASK-XXX | --from-tasks"
allowed-tools: Read, Write, Edit, Grep, Glob, TodoWrite, mcp__sequential-thinking__sequentialthinking
---

# Command: Enhance Prompt

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**YOU MUST:**
1. ✓ Parse input from $ARGUMENTS
2. ✓ Execute core operation
3. ✓ Generate or update required outputs
4. ✓ Report status and results

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Skip required operations
- ✗ Leave work incomplete

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Transform vague user prompts into clear, well-articulated user requests using proven frameworks (RISEN for technical, CO-STAR for production, APE for general), convert to user voice (first-person, outcome-focused), apply enhancement patterns (specificity, constraints, format, role, context, execution strategy), detect delegation intent, validate Voice Authenticity (>90%), calculate CARE+V metrics (baseline → enhanced), present A/B/Skip table (Quick 70-80/100, Complete 85-92/100), **INVOKE Write tool to save file to .artifacts/prompts/ (MANDATORY - command fails without this)**, integrate with task system (Mode 2/3), recommend domain analysts

**P**urpose: Help users articulate their needs clearly to Claude (NOT create AI task lists), systematically improve prompt quality from F/D-tier to B/S-tier (85-92 score), reduce ambiguity through structured frameworks, maintain user voice authenticity (no implementation steps), suggest optimal execution patterns (parallel analysts for multi-domain), persist enhanced prompts for reusability, integrate with unified task management system

**E**xpectation: Enhanced prompt in pure user voice ("I need X because Y, please achieve Z") NOT task voice ("Action: Do X, Steps: 1, 2, 3"), quality improvement delta (e.g., 35/100 → 88/100, D → S-Tier), Voice Authenticity score >90%, **file created with Write tool** and saved to .artifacts/prompts/{date}-{slug}.md (verify file exists!), task entry updated (Mode 2/3), analyst recommendations (max 3 lines), no implementation leakage (validated against anti-patterns)

## Quality Standards (CARE+V)

**Target**: 85+ overall (Completeness >95% framework elements, Accuracy >90% framework selection, Relevance >85% enhancement patterns, Efficiency <15s transformation, Voice >90% user authenticity)

**Voice Authenticity Dimension**:

- **90-100**: Pure user voice, natural request, clear outcomes
- **70-89**: Mostly user voice but some imperative leakage
- **50-69**: Mixed user/implementation voice (❌ FAIL)
- **<50**: Task manager voice, implementation-focused (❌ CRITICAL FAIL)

## Purpose

**Enhances user communication to Claude, NOT implementation plans for bots.**

Transforms vague user requests into clear, well-articulated user requests using proven frameworks (RISEN, CO-STAR, APE). The output is always in **user voice** ("I need X because Y, please achieve Z"), never in task manager voice ("Action: Do X, Steps: 1, 2, 3"). The enhanced prompt helps the user communicate their intent, context, and success criteria more effectively to their AI assistant.

Supports three modes: standalone prompt enhancement (Mode 1), single task enhancement with task.md integration (Mode 2), and batch processing of all tasks without prompts (Mode 3). Auto-saves all enhanced prompts to `.artifacts/prompts/` for version control and reusability.

## Usage

```
/prompt:enhance $ARGUMENTS
```

**Usage Modes**:

1. **Mode 1 - Standalone Prompt Enhancement**: `"user prompt text" [--framework] [--mode]`
2. **Mode 2 - Single Task Enhancement**: `TASK-XXX [--framework] [--mode]`
3. **Mode 3 - Batch Task Processing**: `--from-tasks [--framework] [--mode]`

**Arguments**:

- `$1` (prompt OR task-id OR --from-tasks):
  - Raw user prompt to enhance (Mode 1)
  - TASK-XXX to enhance task description (Mode 2)
  - --from-tasks to batch process all tasks without prompts (Mode 3)
- `$2` (--framework): Framework to apply - risen, costar, ape, or auto for automatic selection (optional, defaults to auto)
- `$3` (--mode): Enhancement mode - quick, complete (optional, defaults to complete)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "Fix the login bug"` - Mode 1: Basic prompt with auto framework
- `$ARGUMENTS = "TASK-042"` - Mode 2: Enhance specific task description
- `$ARGUMENTS = "--from-tasks"` - Mode 3: Batch enhance all tasks without prompts
- `$ARGUMENTS = "Write API docs --framework=costar"` - Mode 1: Specific framework selection
- `$ARGUMENTS = "TASK-015 --mode=quick"` - Mode 2: Quick enhancement for task

## Process

0. **Detect Usage Mode**
   - If `$1` matches `TASK-\d+` pattern → **Mode 2** (Single Task)
     - Read `.agent/tasks.md`
     - Extract task description from matched task entry
     - Use task description as prompt input
   - If `$1` is `--from-tasks` → **Mode 3** (Batch Processing)
     - Read `.agent/tasks.md`
     - Find all tasks without `**Prompt**:` field
     - Process each task description sequentially
   - Else → **Mode 1** (Standalone Prompt)
     - Use `$1` as raw prompt input

1. **Analyze Input Prompt & Detect User Intent**
   - Parse prompt and extract parameters ($1, $2 flags)
   - **Delegation Detection** - Determine if user wants:
     - **Execution intent** (TRANSFORM): Imperative verbs ("fix", "add"), problem statements ("X is broken"), outcome desires ("I need X") → Enhance to user voice
     - **Guidance intent** (MINIMAL/SKIP): Questions ("How should I..."), meta-requests ("What's best way..."), asking for implementation plan → Skip or minimal enhancement
     - **Ambiguous**: Ask user "Would you like me to (A) implement this, or (B) provide guidance for you to implement?"
   - Evaluate current prompt quality using CARE+V metrics (Completeness, Accuracy, Relevance, Efficiency, Voice)
   - Calculate baseline quality score (0-100 scale)
   - Identify specific weaknesses (vagueness, missing context, unclear expectations, implementation leakage)

2. **Present Enhancement Options**
   - If `--mode` flag not provided, present A/B/Skip table with enhancement levels
   - Show clear descriptions with expected quality outcomes
   - If `--mode` flag provided, proceed directly to that enhancement level

3. **Framework Selection**
   - If `--framework=auto` (default), recommend optimal framework based on use case:
     - **RISEN**: Technical/complex tasks, debugging, architecture decisions
     - **CO-STAR**: Production systems, documentation, user-facing content
     - **APE**: General purpose, quick tasks, simple requests (80% of cases)
   - If specific framework requested, use that framework
   - Explain why the framework was selected

4. **Apply Transformation Patterns**
   - Based on selected mode (quick/complete):
     - **Quick**: 3 core patterns (specificity + constraints + format)
     - **Complete**: 6 patterns (quick patterns + role + context + execution strategy)

   **Available Patterns**:
   - **Specificity**: Add concrete details, examples, scope boundaries
   - **Constraints**: Add boundaries, requirements, don'ts
   - **Format Specification**: Define output structure (JSON, table, list)
   - **Role Assignment**: Define expertise level and perspective (Complete mode)
   - **Context Injection**: Add relevant background, dependencies (Complete mode)
   - **Execution Strategy**: Recommend parallel tasks and domain analysts when applicable (Complete mode)

4.5 **Convert to User Voice**

- **CRITICAL**: Transform any imperative commands into user requests
- Replace "Do X", "Implement Y" → "Please do X", "I need Y"
- Add first-person context: "I'm experiencing...", "This is needed for..."
- Frame as outcomes not steps: "After this, I should be able to..." NOT "Step 3: Configure..."
- Include rationale: "This is important because..."
- **Remove implementation HOW**, focus on outcome WHAT
- **Litmus test**: Could a human project manager understand this request and know what success looks like?

5. **Generate Enhanced Prompt**
   - Apply selected framework structure to user voice prompt
   - Validate against CARE+V metrics (including Voice Authenticity)
   - **Anti-Pattern Check**: Detect implementation leakage:
     - ❌ Numbered "Steps: 1, 2, 3" (use bullets instead)
     - ❌ File operation commands ("Open X.md", "Edit line Y")
     - ❌ Missing user voice indicators ("I need", "Please")
     - ❌ Technical HOW without business WHY
   - Calculate quality score improvement delta

6. **Save Enhanced Prompt** (All Modes) - CRITICAL REQUIREMENT

   **⚠️ WARNING: This step is MANDATORY. You MUST invoke the Write tool. The command fails if no file is created.**

   Execute these actions in order:

   a) **Create directory**:

      ```bash
      mkdir -p .artifacts/prompts
      ```

   b) **Generate filename**:
      - Format: `2025-10-15-{first-3-5-words-from-prompt}.md`
      - Lowercase, replace spaces with hyphens, max 40 chars total
      - Example: "/workflow:docs starts work" → `2025-10-15-workflow-docs-starts-work.md`

   c) **Invoke Write tool** (THIS IS NOT OPTIONAL):

      ```
      Write(
        file_path: ".artifacts/prompts/{YYYY-MM-DD}-{topic-slug}.md",
        content: "<!-- Original: \"{original_prompt}\" -->\n\n{enhanced_prompt}"
      )
      ```

      **You must actually call the Write tool here. Do not skip this.**

   d) **Store filepath for later display**:

      ```
      filepath = ".artifacts/prompts/{YYYY-MM-DD}-{topic-slug}.md"
      ```

7. **Present Results** (AFTER Write completes)

   **BEFORE displaying results, verify**: Did you actually call Write tool in step 6c? If NO, STOP and go back to step 6c.

   **OUTPUT ORDER** (critical for terminal UX):
     1. Show separator line: `---`
     2. Display enhanced prompt IN FULL (complete text, not truncated)
     3. Show separator line: `---`
     4. Show file path: `📁 Saved to: {filepath}` + task indicator if Mode 2/3
     5. Present refinement table with 1-3 context-specific improvement options

   **Important**:
   - Enhanced prompt must be fully visible for easy copying from terminal
   - File path must be the actual path where Write tool saved the file
   - Suggest domain analysts if task benefits from specialized expertise (max 3 lines)
   - Recommend parallel execution when multiple independent subtasks exist (max 2 lines)
   - Keep additional output concise and actionable

8. **Update Task Entry** (Mode 2 & 3 Only)
   - Open `.agent/tasks.md` for editing
   - Find task entry by TASK-XXX ID
   - Add `**Prompt**: {filepath}` field after `**Created**` timestamp
   - Save updated tasks.md file

## Agent Integration

- **Specialist Options**: prompt-analyst can be spawned for complex prompt engineering analysis or advanced meta-prompting patterns
- **Analysis Tools**: Read, Grep, Glob for discovering available commands and agents to suggest in enhanced prompts
- **Coordination**: If prompt involves multiple domains (e.g., "optimize and secure my app"), recommend spawning specialized analysts in the enhanced prompt
- **Domain Analyst Mapping**: Automatically suggest relevant domain analysts based on task type:
  - **Code tasks** → code-typescript-analyst, code-python-analyst, code-javascript-analyst, code-csharp-analyst
  - **Security tasks** → security-analyst
  - **Performance tasks** → performance-analyst
  - **Database tasks** → database-analyst, database-sql-analyst, database-nosql-analyst
  - **Frontend tasks** → frontend-react-analyst, frontend-nextjs-analyst, frontend-accessibility-analyst
  - **Architecture tasks** → architecture-analyst
  - **Testing tasks** → testing-analyst
  - **Multi-domain tasks** → Suggest parallel execution of multiple analysts

## Interactive User Input

*Include this section when `--mode` flag is NOT provided*

After analyzing the input prompt, present enhancement options:

```markdown
## How would you like to enhance this prompt?

**Current Quality**: X/100 (Missing: [specific weaknesses])

| Option | Description | Expected Score |
|--------|-------------|----------------|
| A | **Quick** - Add specifics, constraints, output format | 70-80/100 |
| B | **Complete** - Quick + role, context, examples | 85-92/100 |
| Skip | Exit without changes | No change |

Your choice: _
```

**Validation**:

- Accept A, B, or Skip (case-insensitive)
- Invalid input: re-prompt once, then default to Skip
- Execute selected enhancement level

## Framework Structures

### RISEN Framework

Best for: Technical tasks, debugging, architecture decisions

**Core Components**:

- **R**ole: Define expertise and perspective
- **I**nstructions: Clear, actionable steps
- **E**nd goal: Explicit success criteria
- **N**arrowing: Key constraints

**Quick Mode Example** (User Voice):

```
Original: "Fix the login bug"

Enhanced (RISEN-Quick):
I'm experiencing a login functionality issue that needs investigation and resolution.

**What I need**:
- Reproduce the bug with specific test cases to confirm the issue
- Examine the authentication flow (frontend → API → database) and error logs
- Identify root cause and implement a fix with proper error handling
- Add regression tests to prevent recurrence

**Success looks like**: Users can log in reliably with clear error messages when
credentials are invalid.

**Constraints**: Focus on login only, maintain security protocols, ensure backward
compatibility with existing sessions.
```

**Complete Mode Example** (User Voice with RISEN):

```
Original: "Fix the login bug"

Enhanced (RISEN-Complete):
I need you to act as a senior full-stack engineer with authentication systems expertise
to investigate and resolve a login issue through systematic debugging.

**The problem**: Users are experiencing login failures with unclear error messages.

**What I need you to do**:
- Reproduce the issue with specific test cases for different user types (email/social logins)
- Examine the complete authentication flow (frontend → API → database) and error logs
- Identify the root cause and implement a fix with proper error handling
- Write regression tests to prevent this from recurring

**Success criteria**: All user types (email/password and social logins) can log in reliably
with clear, helpful error messages when credentials are invalid.

**Important constraints**: Focus on login functionality only (not broader auth), maintain
security protocols, ensure backward compatibility with existing user sessions.
```

### CO-STAR Framework

Best for: Production systems, documentation, user-facing content

**Core Components**:

- **C**ontext: Background and environment
- **O**bjective: Clear goal statement
- **A**udience: Who will consume this
- **R**esults: Expected output format

**Quick Mode Example** (User Voice):

```
Original: "Write API docs"

Enhanced (CO-STAR-Quick):
I need to create comprehensive, developer-friendly API documentation for our REST API
to reduce support tickets caused by incomplete documentation.

**What I need**:
- Document all endpoints, authentication methods, error codes, and rate limiting
- Include runnable code examples in JavaScript, Python, and cURL
- Create an OpenAPI 3.0 spec for programmatic access
- Build an interactive reference (Swagger/ReDoc style)
- Add a getting started guide and common use case examples

**Success looks like**: Developers can integrate with our API without contacting support
for basic questions about endpoints or authentication.
```

**Complete Mode Example** (User Voice with CO-STAR):

```
Original: "Write API docs"

Enhanced (CO-STAR-Complete):
I need comprehensive, developer-friendly API documentation for our e-commerce REST API.
We have 50+ endpoints, but current documentation is incomplete and causing support tickets
from third-party integrators.

**Target audience**: Third-party developers ranging from junior to senior level who are
integrating their systems with our API.

**What needs to be documented**:
- Complete OpenAPI 3.0 spec (YAML format) for all 50+ endpoints
- Interactive reference interface (Swagger UI or ReDoc)
- Getting started guide that walks through authentication flow
- Real-world use case examples covering orders, payments, and webhooks
- Comprehensive error code reference table

**Style requirements**: Technical but accessible (avoid jargon where possible), follow
OpenAPI 3.0 standards, include runnable code examples in JavaScript, Python, and cURL.

**Success looks like**: Developers can integrate with our API by following the docs alone,
without needing to contact our support team for clarification.
```

### APE Framework

Best for: General purpose, quick tasks (80% of use cases)

**Components**:

- **A**ction: What to do (specific scope)
- **P**urpose: Why it matters (measurable goal)
- **E**xpectation: Success criteria (deliverables)

## User Feedback

| Option | Mode | Details |
|--------|------|---------|
| **A** | Quick | Fast enhancement - add specifics, constraints, format | **← Recommended** for most use cases |
| **B** | Complete | Comprehensive - Quick + role, context, examples | For complex multi-domain tasks |
| **C** | Skip | Exit without enhancement | When prompt is already well-formed |

Your choice (A/B/C)?

## Next Steps

| Option | Action | Command |
|--------|--------|---------|
| 1 | Review enhanced prompt quality | Saved to `.artifacts/prompts/` directory |
| 2 | Iterate on specific weaknesses | Run `/prompt:enhance` again with clarifications |
| 3 | Execute the enhanced prompt | Use directly in `/task:execute` or as task description ← Recommended |
| 4 | Batch enhance similar tasks | Use `/prompt:enhance --from-tasks` for all pending tasks |

What would you like to do next?

---

**Quick Mode Example** (User Voice):

```
Original: "Optimize database queries"

Enhanced (APE-Quick):
I need to optimize the 5 slowest database queries in our user management module to
meet SLA requirements during peak traffic.

**Current situation**: Query response times are 2-3 seconds, causing timeout issues.
Focus on N+1 problems and missing indexes first.

**Target**: <500ms response time for 95th percentile

**What I need**:
- Analysis with query execution plans showing bottlenecks
- Index additions or query refactoring recommendations
- Before/after performance metrics to validate improvements
- Database migration files with rollback capability
```

**Complete Mode Example** (User Voice):

```
Original: "Optimize database queries"

Enhanced (APE-Complete):
I need to analyze and optimize the 5 slowest database queries in our user management
module to meet SLA requirements and improve user experience during peak traffic periods.

**The problem**: Query response times are currently 2-3 seconds, causing timeouts and
user frustration. This started after our user base grew beyond 100k users.

**What I need you to do**:
- Identify the slow queries and generate execution plans to understand bottlenecks
- Focus on N+1 query problems and missing indexes as primary culprits
- Refactor queries or add indexes to achieve <500ms response time (95th percentile)
- Provide before/after performance metrics to validate the improvements
- Create database migration files with proper rollback procedures

**Important constraints**: Use read replicas for any analytics queries, maintain
existing API contracts (don't change query result structures).

**Success criteria**: User management pages load smoothly even during peak traffic,
no timeout errors, SLA compliance restored.
```

## Examples

### Example 1: Quick Enhancement (Auto Framework)

```
/prompt:enhance "Fix the login bug"

→ Analyzing: Missing specifics, context, success criteria
→ Framework: APE (simple debugging task)
→ Applying Quick mode

---

**Enhanced Prompt** (copy and use):

I'm experiencing a login functionality issue that needs investigation and resolution.

**What I need**:
- Reproduce the bug with specific test cases to confirm the issue
- Examine the authentication flow (frontend → API → database) and error logs
- Identify the root cause and implement a fix with proper error handling
- Add regression tests to prevent recurrence

**Success criteria**: Login works reliably with clear error messages when credentials
are invalid.

**Important constraints**: Focus on login only, maintain security protocols, ensure
backward compatibility with existing user sessions.

---
📁 Saved to: .artifacts/prompts/2025-10-15-fix-the-login-bug.md

## Refine further?

| Option | Refinement |
|--------|------------|
| A | Specify which login method is failing (email/password, OAuth, SSO) |
| B | Add timeline/urgency context (blocking users now vs ongoing issue) |
| C | Include tech stack details (React/Node, Django, etc.) |
| Skip | Use this prompt as-is |

Your choice: _
```

### Example 2: Complete Enhancement (Explicit Framework)

```
/prompt:enhance "Write API docs --framework=costar --mode=complete"

→ Analyzing: Missing audience, deliverables, context
→ Framework: CO-STAR (user specified)
→ Applying Complete mode

---

**Enhanced Prompt** (copy and use):

**Context**: E-commerce REST API with 50+ endpoints, current docs incomplete causing support tickets

**Objective**: Create comprehensive, developer-friendly API documentation

**Audience**: Third-party developers (junior-senior) integrating our API

**Results**:
- OpenAPI 3.0 spec (YAML)
- Interactive reference (Swagger/ReDoc)
- Getting started guide with auth flow
- Use case examples (orders, payments, webhooks)
- Error code reference table

**Style**: Technical but accessible, OpenAPI 3.0 standard, runnable code examples in JavaScript/Python/cURL

---
📁 Saved to: .artifacts/prompts/2025-10-15-write-api-docs.md

## Refine further?

| Option | Refinement |
|--------|------------|
| A | Specify which 5-10 endpoints are highest priority |
| B | Add versioning strategy (v2 vs v3 documentation) |
| C | Include timeline constraints (docs needed by when?) |
| Skip | Use this prompt as-is |

Your choice: _
```

### Example 3: Interactive Mode Selection

```
/prompt:enhance "Add user authentication to my app"

→ Analyzing: Missing architecture, requirements, scope
→ Framework: RISEN (multi-phase feature implementation)

## How would you like to enhance this prompt?

**Current Quality**: 35/100 (Missing: architecture details, security requirements, scope)

| Option | Description | Expected Score |
|--------|-------------|----------------|
| A | **Quick** - Add specifics, constraints, output format | 70-78/100 |
| B | **Complete** - Quick + role, context, examples | 85-90/100 |
| Skip | Exit without changes | No change |

Your choice: _

# User selects: B

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**YOU MUST:**
1. ✓ Parse input from $ARGUMENTS
2. ✓ Execute core operation
3. ✓ Generate or update required outputs
4. ✓ Report status and results

**YOU MUST NOT:**
- ✗ Do nothing silently
- ✗ Skip required operations
- ✗ Leave work incomplete

---

→ Applying Complete mode

---

**Enhanced Prompt** (copy and use):

**Role**: Act as senior security engineer with auth systems, OAuth 2.0, and session management expertise

**Instructions**: Design and implement secure user authentication system covering registration, login, session management, and password security

**Steps**:
1. Identify auth requirements (email/password, social logins, MFA, password reset)
2. Choose auth strategy (JWT vs sessions, OAuth providers, token refresh)
3. Implement security (bcrypt hashing, HTTPS, CSRF protection, rate limiting)
4. Build user flows (registration → verification → login → session → logout)
5. Add testing (unit, integration, security penetration)

**End Goal**: Production-ready auth with email/password + 2 social providers (Google, GitHub), OWASP compliance, security audit pass

**Constraints**: Auth only (not authorization), use established libraries (Passport.js, NextAuth, Django Allauth), modern browsers, GDPR compliance

**Context**: Existing web app with user profiles, needs auth before adding payment features

---
📁 Saved to: .artifacts/prompts/2025-10-15-add-user-authentication.md | ✅ Updated [TASK-042]

## Refine further?

| Option | Refinement |
|--------|------------|
| A | Specify tech stack (React/Node, Django, Next.js, etc.) |
| B | Define which social providers (Google, GitHub, others?) |
| C | Add compliance requirements (GDPR, SOC2, specific regulations) |
| Skip | Use this prompt as-is |

Your choice: _
```

### Example 4: Multi-Domain Task with Parallel Execution

```
/prompt:enhance "Improve my e-commerce app" --mode=complete

→ Analyzing: Vague scope, missing domains, no specific goals
→ Framework: RISEN (complex multi-domain task)
→ Applying Complete mode

---

**Enhanced Prompt** (copy and use):

**Role**: Act as full-stack engineering lead with e-commerce platform expertise

**Instructions**: Conduct comprehensive improvement analysis across security, performance, and user experience domains for e-commerce application

**Analysis Areas**:
1. **Security**: Authentication flows, payment handling, data protection (OWASP Top 10)
2. **Performance**: Page load times, database queries, API latency, caching strategies
3. **Frontend**: Accessibility (WCAG 2.1), mobile responsiveness, conversion funnel optimization
4. **Architecture**: Code organization, scalability patterns, technical debt

**Deliverables**:
- Security audit report with vulnerability findings and remediation priorities
- Performance analysis with specific bottlenecks and optimization recommendations
- Frontend accessibility compliance report with WCAG gap analysis
- Architecture review with refactoring roadmap

**Success Criteria**:
- Zero critical security vulnerabilities
- <2s page load time on 3G connection
- WCAG 2.1 AA compliance
- Scalable to 10x current traffic

**Constraints**: Maintain backward compatibility, minimize deployment downtime, prioritize high-impact quick wins

---
📁 Saved to: .artifacts/prompts/2025-10-15-improve-my-ecommerce-app.md

## Refine further?

| Option | Refinement |
|--------|------------|
| A | Prioritize domains (start with security only, then performance, etc.) |
| B | Add budget constraints (time/resources available for improvements) |
| C | Define current pain points (most critical issues to address first) |
| Skip | Use this prompt as-is |

Your choice: _
```

### Example 5: Single Task Enhancement (Mode 2)

```
/prompt:enhance TASK-042

→ Reading .agent/tasks.md
→ Found [TASK-042] Add user authentication to my app
→ Framework: RISEN (multi-phase feature)
→ Applying Complete mode (default)

---

**Enhanced Prompt** (copy and use):

**Role**: Act as senior security engineer with auth systems, OAuth 2.0, and session management expertise

**Instructions**: Design and implement secure user authentication system covering registration, login, session management, and password security

**Steps**:
1. Identify auth requirements (email/password, social logins, MFA, password reset)
2. Choose auth strategy (JWT vs sessions, OAuth providers, token refresh)
3. Implement security (bcrypt hashing, HTTPS, CSRF protection, rate limiting)
4. Build user flows (registration → verification → login → session → logout)
5. Add testing (unit, integration, security penetration)

**End Goal**: Production-ready auth with email/password + 2 social providers (Google, GitHub), OWASP compliance, security audit pass

**Constraints**: Auth only (not authorization), use established libraries (Passport.js, NextAuth, Django Allauth), modern browsers, GDPR compliance

**Context**: Existing web app with user profiles, needs auth before adding payment features

---
📁 Saved to: .artifacts/prompts/2025-10-15-add-user-authentication.md | ✅ Updated [TASK-042]

## Refine further?

| Option | Refinement |
|--------|------------|
| A | Specify tech stack details |
| B | Add social provider requirements |
| C | Include compliance needs (GDPR, SOC2) |
| Skip | Use this prompt as-is |

Your choice: _
```

### Example 6: Batch Task Processing (Mode 3)

```
/prompt:enhance --from-tasks

→ Reading .agent/tasks.md
→ Found 3 tasks without enhanced prompts: TASK-015, TASK-023, TASK-042
→ Processing tasks sequentially...

Processing [TASK-015] "Optimize database queries"...
→ Framework: APE (performance task)

---

**Enhanced Prompt** (copy and use):

**Action**: Analyze and optimize 5 slowest database queries in user management module
- Focus on N+1 problems and missing indexes
- Target <500ms response time (currently 2-3s)

**Purpose**: Meet SLA requirements and improve user experience during peak traffic

**Expectation**:
- Identify queries with execution plans
- Add indexes or refactor queries
- Validate with before/after metrics
- Document in migration files with rollback

**Constraints**: Use read replicas for analytics, maintain existing API contracts

---
📁 Saved to: .artifacts/prompts/2025-10-15-optimize-database-queries.md | ✅ Updated [TASK-015]

---

Processing [TASK-023] "Fix login validation error"...
→ Framework: APE (debugging task)

---

**Enhanced Prompt** (copy and use):

I need to investigate and fix a login validation error that occurs when users enter special characters in their username.

**What I need**:
- Reproduce the bug with test cases using special characters (e.g., @, +, .)
- Check validation rules in both frontend and backend
- Identify where validation breaks (client/server/database layer)
- Implement fix with proper escaping/encoding
- Add regression tests to prevent recurrence

**Success criteria**: Users can login with any valid email characters, and receive clear error messages when input is invalid.

**Important constraints**: Maintain security (prevent SQL injection), ensure backward compatibility with existing users.

---
📁 Saved to: .artifacts/prompts/2025-10-15-fix-login-validation.md | ✅ Updated [TASK-023]

---

[TASK-042 saved to: .artifacts/prompts/2025-10-15-add-user-authentication.md | ✅ Updated [TASK-042]]

---

✅ **Batch processing complete**: Enhanced 3 tasks, saved 3 prompts, updated .agent/tasks.md
```

## User Voice vs Task Voice (Critical Distinction)

**This command transforms vague user requests into clear user requests, NOT into AI implementation tasks.**

| Aspect | User Voice ✅ (CORRECT) | Task Voice ❌ (WRONG) |
|--------|------------------------|----------------------|
| **Audience** | Main thread Claude (user's assistant) | Implementation bot (fictional) |
| **Tone** | First-person requests ("I need...") | Imperative commands ("Do X") |
| **Structure** | What + Why + Success criteria | How + Steps: 1, 2, 3 |
| **Example** | "I need login fixed because users can't access. Please investigate auth flow and resolve with tests." | "Action: Fix login. Steps: 1. Open auth.ts 2. Debug flow 3. Add tests" |
| **Litmus Test** | Could a human PM understand this? | Sounds like a Jira ticket? |

**Key Principle**: Enhanced prompts help users **articulate their needs clearly**, not tell AI **how to implement**.

## Explicit Constraints

**IN SCOPE**: Prompt analysis (CARE+V metrics, weaknesses), framework selection (RISEN/CO-STAR/APE), user voice transformation, quality scoring (0-100, F/D/C/B/A/S tiers), interactive mode selection (Quick/Complete/Skip), analyst/parallelization recommendations, prompt saving (.artifacts/prompts/), task integration (Mode 2 & 3), delegation detection

**OUT OF SCOPE**: AI implementation task creation, numbered step-by-step instructions, file operation commands, actual task implementation, agent invocation (recommends, doesn't spawn), project-specific context injection (user must provide)

## Parallelization Patterns

**Not applicable for command execution** - This command operates sequentially as a single analysis and transformation task.

**However**, enhanced prompts actively recommend parallel execution strategies:

- **Multi-domain tasks**: Suggest spawning multiple domain analysts concurrently
- **Independent subtasks**: Recommend Task tool for parallel execution
- **Complex analysis**: Suggest security-analyst + performance-analyst + architecture-analyst in parallel

**Example Output**:

```
🔀 **Parallel execution**: Spawn these analysts concurrently using Task tool:
   - security-analyst (OWASP compliance review)
   - performance-analyst (optimization opportunities)
   - architecture-analyst (system design validation)

   Task tool usage: Send single message with three Task tool calls for maximum efficiency
```

## Integration Points

- **Follows**: User's initial unclear or vague request, `/task:add` (adhoc task creation), `/task:scan-project` (code comments)
- **Followed by**: Execution of the enhanced prompt (often involves `/claude:guru` for command recommendations)
- **Related**:
  - `/claude:guru` (command recommendations & guidance)
  - `/task:execute` (task management & triage)
  - `/task:add` (adhoc task creation)
  - `/github:convert-issues-to-tasks` (GitHub issue import)
  - speckit commands (structured feature development)

## Task Integration

**Workflow Pattern**: Tasks → Enhanced Prompts → Execution

**Task Format with Prompt Reference**:

```markdown
## [TASK-042] Add user authentication to my app

**Status**: pending
**Priority**: high
**Category**: feature
**Origin**: adhoc
**Created**: 2025-10-15T10:30:00Z
**Prompt**: .artifacts/prompts/2025-10-15-add-user-authentication.md

**Description**:
Design and implement secure user authentication system...
```

**Benefits**:

- **Reusability**: Enhanced prompts stored in version control
- **Consistency**: Same prompt across multiple iterations
- **Collaboration**: Team members can review and improve prompts
- **History**: Track how prompts evolved over time
- **Quick Access**: File path in task for easy reference

**Batch Processing Benefits** (Mode 3):

- Process multiple tasks in single command
- Standardize prompt quality across backlog
- Prepare tasks before sprint planning
- Auto-save all prompts for team review

**Example Workflow**:

```bash
# 1. Capture tasks during brainstorming
/task:add "Add user authentication" --priority=high --category=feature
/task:add "Optimize database queries" --priority=medium --category=refactor
/task:add "Fix login validation" --priority=high --category=bug

# 2. Batch enhance all tasks
/prompt:enhance --from-tasks

# 3. Execute tasks with enhanced prompts
/task:execute TASK-042  # Uses enhanced prompt automatically
```

## Quality Standards

- Transforms prompts using proven frameworks (RISEN, CO-STAR, APE) based on use case
- Applies measurable enhancement patterns (Specificity, Constraints, Format, Role, Context, Execution Strategy)
- Calculates quality scores using CARE metrics (Completeness, Accuracy, Relevance, Efficiency)
- Provides concise before/after comparison with tier labels (F/D/C/B/A/S-Tier)
- Offers interactive mode selection (Quick/Complete) with clear tradeoffs
- Places enhanced prompt at bottom of output for easy terminal copying
- **Recommends parallel execution** when multiple independent subtasks exist
- **Suggests domain analysts** based on task type for specialized expertise
- Optionally suggests clarification questions for quick iteration
- Maintains atomic design - focuses on prompt enhancement only (delegates command discovery to `/claude:guru`)

## Output

**Output Structure** (Optimized for Terminal Usage):

1. **Brief Analysis** (1-2 lines): What's missing from the original prompt
2. **Framework Selection** (if auto): Why this framework was chosen
3. **Enhancement Options** (if --mode not provided): A/B/Skip table
4. **Enhanced Prompt** (ALWAYS AT BOTTOM): The improved prompt ready to use

**After Enhanced Prompt**:

5. **File Path** (Line 1): `📁 Saved to: {filepath}` + `| ✅ Updated [TASK-XXX]` (Mode 2 & 3 only)

6. **Improvement Options** (A/B/C Table):

```markdown
## Refine further?

| Option | Refinement |
|--------|------------|
| A | [Context-specific improvement 1] |
| B | [Context-specific improvement 2] |
| C | [Context-specific improvement 3] |
| Skip | Use this prompt as-is |

Your choice: _
```

**Example Output**:

```
---

I need the /workflow:docs command to require confirmation before starting work...

[rest of enhanced prompt]

---
📁 Saved to: .artifacts/prompts/2025-10-15-workflow-docs-confirmation.md

## Refine further?

| Option | Refinement |
|--------|------------|
| A | Add specific scope options (quick vs complete audit) |
| B | Include cancellation/rollback strategy |
| C | Specify acceptance criteria for "confirmation works" |
| Skip | Use this prompt as-is |

Your choice: _
```

**Rationale**: Enhanced prompt appears last for easy terminal copying. File path shown immediately for quick access. A/B/C table provides 1-3 contextual improvement suggestions based on what's still unclear or could be more specific. User can iterate or use as-is.

## Anti-Patterns Avoided

**Common mistakes this command prevents**:

- ❌ **Vagueness** (insufficient context) → ✅ Adds context, scope, constraints
- ❌ **Over-complexity** (too many instructions) → ✅ Uses structured frameworks for clarity
- ❌ **Missing evaluation** (no success criteria) → ✅ Defines explicit end goals and validation
- ❌ **Generic roles** ("helpful assistant") → ✅ Assigns specific expertise levels
- ❌ **Unclear outputs** (no format specified) → ✅ Defines concrete deliverables and structure
- ❌ **No constraints** (unrealistic scope) → ✅ Adds boundaries and narrowing criteria

**Implementation Leakage Anti-Patterns** (Voice Authenticity):

- ❌ **Numbered steps** ("Steps: 1. Do X, 2. Do Y") → ✅ User requests with bullets ("What I need: ...")
- ❌ **File operation commands** ("Open X.md", "Edit line 42") → ✅ Outcome descriptions ("I need X to behave like Y")
- ❌ **Missing user voice** (no "I need", "Please") → ✅ First-person user requests
- ❌ **Technical HOW without business WHY** → ✅ Rationale included ("This is needed because...")
- ❌ **Task manager tone** ("Action: Implement X") → ✅ User communication ("I need X implemented because Y")
