---
description: "Context-aware intelligent assistant that analyzes your project and provides command suggestions, helpful prompts, and workflow guidance"
argument-hint: "[topic]"
allowed-tools: Read, Glob, Grep, Bash(git:*), Bash(ls:*), Bash(find:*), Task, mcp__sequential-thinking__sequentialthinking
---

# Command: Guru

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Provide intelligent context-aware development guidance in two modes (smart suggestions or deep topic guidance).

**Claude Code MUST execute this workflow:**
1. ✓ Analyze current project state (git status, file changes, project type)
2. ✓ Detect execution mode (no args = smart suggestions, with topic = deep guidance)
3. ✓ Provide 3-5 relevant command suggestions with rationale
4. ✓ For smart mode: offer helpful prompts and quick workflow
5. ✓ For deep mode: comprehensive topic guidance with best practices
6. ✓ Always provide actionable, context-specific recommendations

**Claude Code MUST NOT:**
- ✗ Execute suggested commands (only recommend)
- ✗ Skip context analysis
- ✗ Provide generic guidance without project analysis

---

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Provide intelligent development assistance via dual-mode operation (no args → smart suggestions from git/project analysis, with topic → deep guidance), analyze current context (git status, file changes, project type), suggest 3-5 relevant commands with rationale, offer helpful prompts, deliver comprehensive topic guidance (workflows, best practices, examples)

**P**urpose: Reduce cognitive load in choosing appropriate commands/workflows, provide educational context-aware guidance, accelerate development velocity through actionable recommendations, support learning through topic deep-dives (git, git-flow, testing, performance)

**E**xpectation: Smart Suggestion Mode → 3-5 command suggestions + helpful prompts + quick workflow. Deep Guidance Mode → comprehensive topic guide + workflow sequences + best practices + command references + pro tips

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% context factors, Accuracy >90% command suggestions, Relevance >85% to current situation, Efficiency <10s analysis)

## Purpose

Your intelligent development assistant that provides context-aware guidance in two modes:

**Without Arguments** (`/claude:guru`):

- Analyzes current project state and git status
- Suggests relevant commands for your situation
- Provides helpful prompt examples
- Offers quick tactical recommendations

**With Topic** (`/claude:guru <topic>`):

- Deep-dive guidance on specific areas (git, git-flow, testing, performance, etc.)
- Detailed workflow explanations and best practices
- Topic-specific command references
- Educational content and examples

## User Feedback

| Option | Action | Details |
|--------|--------|---------|
| A | Default workflow | [RECOMMENDED] |
| B | Alternative approach | For different use case |
| C | Skip | Exit without changes |

Your choice (A/B/C)?

## Next Steps

| Option | Action | Command |
|--------|--------|---------|
| 1 | Review output | Check generated content |
| 2 | Iterate or refine | Run command again [RECOMMENDED] |
| 3 | Continue workflow | Proceed to next step |
| 4 | Get help | Use /claude:guru for guidance |

What would you like to do next?


## Usage

```bash
/claude:guru              # Smart suggestions based on current context
/claude:guru [topic]      # Deep guidance on specific topic
```

**Arguments**:

- `topic` (optional): Specific area for detailed guidance (e.g., "git", "git-flow", "testing", "refactoring", "performance", "documentation")

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - Context-based command suggestions and helpful prompts
- `$ARGUMENTS = "git"` - Git workflow guidance based on current branch and changes
- `$ARGUMENTS = "git-flow"` - Git-Flow workflow comprehensive guide
- `$ARGUMENTS = "testing"` - Testing strategy recommendations
- `$ARGUMENTS = "performance"` - Performance optimization detailed guidance

## Process

### Mode Selection

**If `$ARGUMENTS` is empty** → **Smart Suggestion Mode**:

1. Analyze current context (git status, file changes, project type)
2. Provide 3-5 most relevant command suggestions
3. Offer helpful prompt examples for common tasks
4. Give quick tactical recommendations

**If `$ARGUMENTS` contains topic** → **Deep Guidance Mode**:

1. Full project analysis with parallel context detection
2. Topic-specific comprehensive guidance
3. Detailed workflow explanations
4. Best practices and educational content

---

## Smart Suggestion Mode (No Arguments)

When called without arguments (`/claude:guru`), provides quick, actionable recommendations:

### Analysis Steps

1. **Check Git Status**:
   - Staged/unstaged changes
   - Current branch and tracking status
   - Recent commit patterns

2. **Identify Modified Files**:
   - File types (code, tests, docs, config)
   - Affected domains (frontend, backend, database)
   - Change scope and complexity

3. **Detect Project Context**:
   - Language/framework from config files
   - Available test frameworks
   - Existing workflows

4. **Generate Recommendations**:
   - List 3-5 most relevant commands
   - Provide helpful prompt examples
   - Suggest workflow sequences
   - Include rationale for each suggestion

### Output Format

```markdown
# Context Analysis

**Project**: [Detected project type]
**Branch**: [Current branch]
**Changes**: [Summary of changes]

## Recommended Commands

1. **[Command 1]** - [Why this command is relevant]
   ```bash
   /command:example
   ```

2. **[Command 2]** - [Why this command is relevant]

   ```bash
   /command:example
   ```

3. **[Command 3]** - [Why this command is relevant]

   ```bash
   /command:example
   ```

## Helpful Prompts

Try these prompts based on your current situation:

- "[Specific prompt example 1]"
- "[Specific prompt example 2]"
- "[Specific prompt example 3]"

## Quick Workflow

[Suggested command sequence for common next steps]

```

---

## Deep Guidance Mode (With Topic)

When called with a topic argument (`/claude:guru <topic>`), provides comprehensive guidance:

### 1. **Project Context Detection** (Parallel Analysis)

```text
# Detect project type and structure in parallel
Task("Analyze git status and recent activity")
Task("Detect project type from configuration files")
Task("Identify current development phase")
```

**Git Analysis**:

- Current branch name and status
- Uncommitted changes (staged/unstaged)
- Recent commits and patterns
- Remote tracking status
- Unmerged conflicts

**Project Type Detection**:

- `package.json` → Node.js/JavaScript/TypeScript project
- `requirements.txt` or `pyproject.toml` → Python project
- `Cargo.toml` → Rust project
- `pom.xml` or `build.gradle` → Java project
- `go.mod` → Go project
- `.specify/` → Spec-kit enabled project

**File Structure Analysis**:

- Test directories and coverage
- Documentation completeness
- Configuration files present
- Source code organization

### 2. **Intelligent Recommendation Engine**

Based on detected context, provide targeted guidance:

#### **Scenario: Uncommitted Changes**

```markdown
## Current Situation
You have 12 uncommitted changes across 8 files.

## Recommended Actions

1. **Review Changes**: Use `/review:code` to assess quality before committing
2. **Create Commit**: Use `/git:commit` for conventional commit with auto-generated message
3. **Run Tests**: Verify changes with `/workflows:run-lint-and-correct-all`

## Quick Commands
```

```bash
/review:code                    # Review your changes
/git:commit                     # Create conventional commit
/workflows:run-lint-and-correct-all  # Lint and fix issues
```

#### **Scenario: Feature Branch Development**

```markdown
## Current Situation
Branch: `feature/user-authentication` (5 commits ahead of main)

## Recommended Workflows

1. **Comprehensive Review**: `/workflows:run-comprehensive-review feature/user-authentication main`
2. **Security Audit**: `/workflows:run-security-audit` (auth-related changes detected)
3. **Create Pull Request**: `/git:pr "Add user authentication system"`

## Development Tips
- Authentication code requires extra scrutiny - use security-analyst
- Consider adding integration tests for auth flows
- Document API changes in OpenAPI/Swagger if applicable
```

#### **Scenario: Multiple Test Failures**

```markdown
## Current Situation
Recent test run shows failures in 3 test suites.

## Debug Strategy

1. **Quick Bug Fix**: `/fix:bug-quickly "test failure description" --test-first`
2. **Testing Analysis**: Use testing-analyst to assess coverage gaps
3. **Refactoring**: If tests reveal code smells, use `/refactor:apply`

## Testing Commands
```

```bash
/fix:bug-quickly "failing test name"  # Quick targeted fix
/workflows:run-comprehensive-review   # Full analysis including test quality
```

#### **Scenario: New to Project**

```markdown
## Getting Started

### Understand the Codebase
1. **Architecture Overview**: `/explain:architecture --format=diagram`
2. **Code Explanation**: `/explain:code` for specific components
3. **Documentation Check**: `/docs:sync` to ensure docs are current

### Setup Verification
```

```bash
# Check project dependencies
/guru dependencies

# Verify development environment
/guru environment

# Understand commit conventions
/guru git-workflow
```

```markdown
### Useful Resources
- See `.specify/spec.md` for current feature specifications (if speckit enabled)
- Check `CONTRIBUTING.md` for contribution guidelines
- Review `README.md` for setup instructions
```

### 3. **Topic-Specific Guidance**

When user specifies a topic, provide deep guidance:

#### **Topic: Git Workflow**

```markdown
## Git Workflow Guide

### Available Git Commands
- `/git:commit` - Conventional commits with auto-type detection
- `/git:push` - Safe push with validation
- `/git:pr` - Create pull requests (git-flow aware)
- `/git:complete` - Complete workflow: branch → commit → push → PR (git-flow aware)
- `/git-flow:feature` - Create feature branch from develop
- `/git-flow:release` - Create release branch with version management
- `/git-flow:hotfix` - Create emergency hotfix branch from main
- `/git-flow:finish` - Complete and merge current branch
- `/git-flow:status` - Display comprehensive Git Flow status

### Current Project Conventions
**Detected from recent commits:**
- Commit style: Conventional Commits (feat:, fix:, docs:)
- Branch naming: `feature/`, `bugfix/`, `hotfix/`
- PR requirements: Passing tests, linter compliance

### Example Workflows
```

```bash
# Feature development (Git-Flow)
/git-flow:feature new-feature
# ... make changes
/git:commit
/git:push
/git:pr

# Or complete workflow
/git:complete feature/new-feature
```

```markdown
### Best Practices
- Always review with `/review:code` before committing to main
- Use `/workflows:run-comprehensive-review` before creating PRs
- Run security audit for auth/API changes: `/workflows:run-security-audit`
```

#### **Topic: Git-Flow**

```markdown
## Git-Flow Workflow Guide

### Repository Mode Detection

**Detected Repository Mode:**
- Check: `git branch -a | grep develop`
- If develop exists: **Git-Flow mode**
- If not: **Conventional mode**

Current repository: [Analyze branches to determine mode]

### Git-Flow Commands

**Feature Development:**
- `/git-flow:feature <name>` - Create feature branch from develop
  - Branches from develop automatically
  - Sets up remote tracking
  - Ready for development

**Release Management:**
- `/git-flow:release <version>` - Create release branch
  - Auto-detects version from commits (or specify)
  - Updates version files (package.json, pyproject.toml, Cargo.toml)
  - Generates CHANGELOG.md
  - Creates PR to main

**Emergency Hotfixes:**
- `/git-flow:hotfix <name>` - Create hotfix from main
  - For production-critical bugs only
  - Branches from main
  - Quick deployment path

**Complete Workflows:**
- `/git-flow:finish` - Finish current feature/release/hotfix
  - Detects branch type automatically
  - Creates git tags (release/hotfix only)
  - Merges to appropriate branches
  - Deletes completed branch

**Status Monitoring:**
- `/git-flow:status` - Display comprehensive Git Flow status
  - Current branch info and type
  - Sync status with remote
  - Active branches overview
  - Recommendations

**Standard Operations (Git-Flow Aware):**
- `/git:commit` - Smart conventional commits
- `/git:push` - Safe push with validation
- `/git:pr` - Auto-targets correct base branch
- `/git:complete` - Complete feature workflow

### Workflow Sequences

**Feature Development:**
```

```bash
/git-flow:feature user-auth      # From develop (auto)
# Make changes
/git:commit                      # Logical commits
/git:pr                          # PR to develop (auto)
```

```markdown
**Release Process:**
```

```bash
# When develop ready:
/git-flow:release 1.2.0          # Create release
# QA tests, PR review, merge to main
/git-flow:finish                 # Tag, merge to develop
```

```markdown
**Emergency Hotfix:**
```

```bash
/git-flow:hotfix critical-bug    # From main
# Make fix
/git:commit && /git:pr           # PR to main
/git-flow:finish                 # Tag, merge to develop
```

```markdown
### When to Use Git-Flow

**Use Git-Flow if:**
- Team size: 5+ developers
- Scheduled releases (weekly, monthly, quarterly)
- Multiple environments (prod, staging, dev)
- Need formal version management
- Emergency hotfix capability required

**Use Conventional Commits if:**
- Small team (1-5 developers)
- Continuous deployment
- Feature-focused development
- No formal version management

### Next Steps
```

```bash
# Learn more:
# Read: /Users/thomasholknielsen/.claude/docs/user/git-flow-guide.md
# Practice: /git:branch feature/test
```

```markdown
### Common Questions

**Q: How do I switch to git-flow?**
A: Create develop branch: `git checkout -b develop && git push -u origin develop`

**Q: Which branch should I PR to?**
A: Commands auto-detect! feature/* → develop, release/hotfix/* → main

**Q: When should I create a release?**
A: When develop has enough features for a deployment cycle.
```

#### **Topic: Testing**

```markdown
## Testing Strategy

### Current Test Coverage
**Detected:**
- Test files: 42 test files found
- Test frameworks: Jest (frontend), Pytest (backend)
- Coverage tools: `jest.config.js`, `.coveragerc`

### Recommended Actions

1. **Assess Coverage**: Use testing-analyst to identify gaps
2. **Run Tests**:
```

```bash
npm test           # Run Jest tests
pytest tests/      # Run Python tests
```

```markdown
3. **Improve Quality**: `/workflows:run-comprehensive-review` includes testing analysis

### Testing Commands

- Use `/fix:bug-quickly --test-first` to create failing tests before fixing bugs
- Use testing-analyst for comprehensive test quality assessment
```

#### **Topic: Performance**

```markdown
## Performance Optimization

### Quick Assessment

Run performance analysis: `/workflows:run-optimization`

### Performance Workflow

1. **Analysis Phase**: 3 analysts run in parallel
   - performance-analyst: Bottleneck detection
   - database-analyst: Query optimization
   - frontend-analyst: Bundle size analysis

2. **Implementation Phase**: Main thread implements recommendations

3. **Validation Phase**: Benchmark improvements

### Performance Commands
```

```bash
/workflows:run-optimization              # Comprehensive optimization
/review:performance                      # Performance-focused review
```

```markdown
### Common Issues to Check

- N+1 queries in database code
- Large bundle sizes in frontend
- Inefficient algorithms in hot paths
- Missing indexes on database queries
```

### 4. **Argument Handling Guidance**

Provide clear examples of command argument patterns:

```markdown
## Command Argument Patterns (GNU-style)

### Flag Format Standards

Always use `--flag=value` format:
```

```bash
# ✅ Correct
/fix:bug-quickly --scope=auth-module --strategy=minimal

# ❌ Incorrect
/fix:bug-quickly --scope auth-module --strategy minimal
```

```markdown
### $ARGUMENTS Processing

Commands receive arguments as `$ARGUMENTS` variable:

- Positional args: Accessible as $1, $2, $3
- Named flags: Parsed from $ARGUMENTS string
- Boolean flags: Present/absent (e.g., `--test-first`)

### Common Argument Patterns

**Scope Limiting:**
```

```bash
/fix:bug-quickly --scope=<area>           # Limit search scope
/review:code --focus=<aspect>              # Focus review
/refactor:apply --target=<pattern>         # Target specific code
```

```markdown
**Strategy Selection:**
```

```bash
/fix:bug-quickly --strategy=<approach>     # Fix approach
/refactoring:apply --strategy=<method>     # Refactoring method
```

```markdown
**Output Control:**
```

```bash
/explain:code --depth=<level>              # Detail level
/docs:sync                            # Documentation workflow
```

```markdown
### Example Combinations
```

```bash
# Bug fix with specific scope and strategy
/fix:bug-quickly "TypeError in auth" --scope=auth-module --strategy=root-cause

# Code review with focus area
/review:code components/ --focus=performance

# Large-scale refactoring with validation
/refactor:large-scale --target=services/ --validate-each-step
```

### 5. **Interactive Prompt Suggestions**

Suggest specific prompts based on detected context:

```markdown
## Suggested Prompts

Based on your current project state, try these prompts:

### Review & Quality
```

```text
"Review the authentication changes for security vulnerabilities"
"Analyze test coverage and identify untested edge cases"
"Check for performance bottlenecks in the API layer"
```

```markdown
### Implementation
```

```text
"Implement input validation for the user registration endpoint"
"Add comprehensive error handling to the payment service"
"Refactor the UserController to follow SOLID principles"
```

```markdown
### Documentation
```

```text
"Document the new API endpoints with examples"
"Update the README with the latest setup instructions"
"Generate API documentation from the OpenAPI schema"
```

```markdown
### Git & Workflow
```

```text
"Create a commit for these authentication changes"
"Review my changes and prepare a pull request"
"Help me understand why these tests are failing"
```

## Explicit Constraints

**IN SCOPE**: Context analysis (git status, file changes, project type detection), command recommendations (3-5 with rationale), prompt suggestions, topic-specific guidance (git, git-flow, testing, performance), workflow sequences, best practices, educational content
**OUT OF SCOPE**: Command execution (only suggests, never executes), direct code modifications, agent invocation (recommends but doesn't spawn), project-specific business logic, user preference storage

## Agent Integration

- **Primary Specialist**: None - Direct implementation using Read, Grep, Glob, and Bash tools
- **Parallel Analysis**: Can spawn analysts for specific deep dives when requested

## Examples

### Example 1: Smart Suggestion Mode (No Arguments)

```bash
/claude:guru
```

**Output:**

```markdown
# Context Analysis

**Project**: Full-stack TypeScript (React + Node.js)
**Branch**: feature/checkout-flow (3 commits ahead of develop)
**Changes**: 7 files modified, 2 staged (payment integration code)

## Recommended Commands

1. **`/workflows:run-security-audit`** - Payment/checkout code detected
   ```bash
   /workflows:run-security-audit
   ```

   Security audit is critical for payment handling - checks PCI compliance patterns

2. **`/lint:correct-all`** - Clean up before committing

   ```bash
   /lint:correct-all
   ```

   Fix linting issues across all modified files

3. **`/workflows:run-comprehensive-review`** - Multi-perspective review

   ```bash
   /workflows:run-comprehensive-review
   ```

   Full review before creating PR (quality + security + performance)

4. **`/git:complete`** - Complete git workflow

   ```bash
   /git:complete "Implement checkout flow with payment integration"
   ```

   Automated: review → lint → commit → push → PR

5. **`/git:commit`** - Direct commit

   ```bash
   /git:commit
   ```

   If you've already reviewed - generates conventional commit message

## Helpful Prompts

Try these prompts based on your current situation:

- "Review the payment integration code for security vulnerabilities"
- "Add comprehensive error handling to the checkout flow"
- "Create unit tests for the payment service integration"
- "Document the new checkout API endpoints with examples"

## Quick Workflow

**Recommended sequence** for checkout/payment code:

```bash
/workflows:run-security-audit    # Security first for payment code
/lint:correct-all                # Clean up any issues
/git:complete "checkout flow"   # Complete git workflow
```

## Pro Tips

- Payment integration needs **extra security scrutiny**
- Consider PCI DSS compliance requirements
- Test error scenarios (payment failures, timeouts, etc.)

```

### Example 2: Deep Guidance Mode - Git Topic

```bash
/claude:guru git
```

**Output:**

```markdown
# Git Workflow Guide

## Current Git Status

- Branch: `feature/user-dashboard`
- Status: 12 uncommitted changes, 5 staged
- Remote: Up to date with origin/feature/user-dashboard
- Base: `develop` (8 commits behind)

## Recommended Git Workflow

### Step 1: Commit Current Work
```

```bash
/git:commit
```

```markdown
Will analyze changes and generate conventional commit like:
`feat(dashboard): add user analytics visualization`

### Step 2: Update from Base Branch
```

```bash
git fetch origin
git rebase origin/develop
```

```markdown
### Step 3: Review Before PR
```

```bash
/workflows:run-comprehensive-review feature/user-dashboard develop
```

```markdown
### Step 4: Create Pull Request
```

```bash
/git:pr "Add user analytics dashboard"
```

```markdown
## Detected Commit Conventions

**From recent commits:**

- Format: Conventional Commits (type(scope): description)
- Types used: feat, fix, docs, refactor, test
- Scopes: dashboard, api, auth, database

## Available Git Commands

- `/git:commit` - Auto-generated conventional commit
- `/git:branch [name]` - Create/switch branches
- `/git:push` - Push with safety checks
- `/git:pr [title]` - Create GitHub PR
- `/git:complete [branch]` - Complete flow: branch → commit → push → PR

## Git Best Practices for This Project

1. Always rebase from develop before creating PR
2. Run `/review:code` before committing to develop
3. Use `/workflows:run-comprehensive-review` before PR creation
4. Ensure tests pass: check CI status before merging
```

### Example 3: Deep Guidance Mode - Performance Topic

```bash
/claude:guru performance
```

**Output:**

```markdown
# Performance Optimization Guide

## Quick Performance Analysis

Run comprehensive optimization workflow:
```

```bash
/workflows:run-optimization
```

```markdown
## Performance Analysis Process

### Phase 1: Parallel Analysis

- **performance-analyst**: Bottleneck detection, algorithmic efficiency
- **database-analyst**: Query optimization, N+1 detection, indexing
- **frontend-analyst**: Bundle analysis, code splitting, asset optimization

### Phase 2: Implementation

Main thread implements recommended optimizations:

- Refactor inefficient algorithms
- Optimize database queries
- Implement code splitting
- Remove unused dependencies

### Phase 3: Validation

- Run benchmarks to measure improvements
- Validate no functionality regressions

## Performance Commands
```

```bash
/workflows:run-optimization              # Full optimization workflow
/review:performance                      # Performance-focused review
/refactor:apply --pattern=performance    # Apply performance patterns
```

```markdown
## Common Performance Issues

### Backend Performance

- **N+1 Queries**: Use database-analyst to detect
- **Missing Indexes**: Check slow query logs
- **Inefficient Algorithms**: Analyze algorithmic complexity

### Frontend Performance

- **Large Bundle Size**: Check for unused dependencies
- **No Code Splitting**: Implement lazy loading
- **Unoptimized Images**: Compress and lazy-load assets

### Database Performance

- **Slow Queries**: Add explain analyze to queries
- **Connection Pooling**: Configure properly
- **Missing Indexes**: Use database-analyst recommendations

## Performance Workflow Example
```

```bash
# Step 1: Analyze
/workflows:run-optimization

# Step 2: Review findings in .agent/context/
# - Read performance-analysis-*.md
# - Read database-analysis-*.md
# - Read frontend-analysis-*.md

# Step 3: Implement recommendations
# (Manual implementation based on analyst guidance)

# Step 4: Validate improvements
npm run test                # Ensure no regressions
npm run build              # Check bundle size reduction
```

## Integration Points

- **Follows**: Can be run at any time for context-aware guidance
- **Related Commands**:
  - `/review:code` - Code quality review
  - `/workflows:run-comprehensive-review` - Multi-perspective analysis
  - `/git:commit`, `/git:pr` - Git operations
  - `/explain:architecture`, `/explain:code` - Understanding codebase

## Quality Standards

- **Accuracy**: Recommendations based on actual project state analysis
- **Relevance**: Suggestions tailored to detected context
- **Actionability**: Provide specific commands and workflows
- **Clarity**: Clear explanations with examples
- **Completeness**: Cover common scenarios comprehensively

## Output

- Context-aware recommendations based on project analysis
- Specific command suggestions with example usage
- Workflow guidance tailored to current development phase
- Best practices and pro tips for the detected project type
- Clear next steps with copy-paste ready commands
