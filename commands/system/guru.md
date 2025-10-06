---
description: "Context-aware intelligent assistant that analyzes your project and provides personalized guidance, workflow suggestions, and command recommendations"
argument-hint: "[topic]"
allowed-tools: Read, Glob, Grep, Bash(git:*), Bash(ls:*), Bash(find:*), Task
---

# Command: Guru

## Purpose

Provides intelligent, context-aware assistance by analyzing your current project state, git status, file structure, and recent activity to recommend relevant workflows, commands, and development strategies tailored to your specific situation.

## Usage

```bash
/guru [topic]
```

**Arguments**:

- `topic` (optional): Specific area for guidance (e.g., "git", "testing", "refactoring", "documentation")

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - General project analysis and recommendations
- `$ARGUMENTS = "git"` - Git workflow guidance based on current branch and changes
- `$ARGUMENTS = "testing"` - Testing strategy recommendations
- `$ARGUMENTS = "performance"` - Performance optimization suggestions

## Process

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
3. **Documentation Check**: `/workflows:run-docs-workflow` to ensure docs are current

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
- See `.specify/spec.md` for current feature specifications (if spec-kit enabled)
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
- `/git:branch` - Branch management with naming conventions
- `/git:push` - Safe push with validation
- `/git:pr` - Create pull requests
- `/git:full-workflow` - Complete workflow: branch → commit → push → PR

### Current Project Conventions
**Detected from recent commits:**
- Commit style: Conventional Commits (feat:, fix:, docs:)
- Branch naming: `feature/`, `bugfix/`, `hotfix/`
- PR requirements: Passing tests, linter compliance

### Example Workflows
```

```bash
# Feature development
/git:branch feature/new-feature
# ... make changes
/git:commit
/git:push
/git:pr "Implement new feature"

# Quick hotfix
/git:full-workflow hotfix/critical-bug
```

```markdown
### Best Practices
- Always review with `/review:code` before committing to main
- Use `/workflows:run-comprehensive-review` before creating PRs
- Run security audit for auth/API changes: `/workflows:run-security-audit`
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
/docs:generate --format=<type>             # Output format
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

## Agent Integration

- **Primary Specialist**: None - Direct implementation using Read, Grep, Glob, and Bash tools
- **Parallel Analysis**: Can spawn analysts for specific deep dives when requested

## Examples

### Example 1: General Project Guidance

```bash
/guru
```

**Output:**

```markdown
# Project Analysis: E-Commerce Platform

## Current Context

- **Project Type**: Full-stack TypeScript (React + Node.js)
- **Branch**: feature/checkout-flow (3 commits ahead of develop)
- **Uncommitted**: 7 files modified, 2 files staged
- **Spec-Kit**: Enabled (.specify/ detected)

## Immediate Recommendations

1. **Review Changes**: 7 uncommitted files suggest significant work
   → `/review:code` before committing

2. **Checkout Flow Feature**: Current branch indicates payment integration
   → Run `/workflows:run-security-audit` (sensitive data handling)
   → Ensure PCI compliance for payment processing

3. **Create PR Soon**: Branch is 3 commits ahead
   → `/git:commit` for current changes
   → `/git:pr` when ready for review

## Available Workflows

- `/workflows:run-comprehensive-review` - Multi-perspective review
- `/workflows:run-security-audit` - Security-focused analysis
- `/workflows:run-optimization` - Performance tuning

## Quick Commands
```

```bash
/review:code                              # Review uncommitted changes
/git:commit                               # Commit with conventional format
/workflows:run-security-audit             # Security audit for payment code
/git:pr "Implement checkout flow"         # Create pull request
```

```markdown
## Pro Tips

- Checkout flows need extra security scrutiny - use security-analyst
- Test payment integration thoroughly - consider `/fix:bug-quickly --test-first`
- Document API changes in current spec: `.specify/spec.md`
```

### Example 2: Git-Specific Guidance

```bash
/guru git
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
- `/git:full-workflow [branch]` - Complete flow: branch → commit → push → PR

## Git Best Practices for This Project

1. Always rebase from develop before creating PR
2. Run `/review:code` before committing to develop
3. Use `/workflows:run-comprehensive-review` before PR creation
4. Ensure tests pass: check CI status before merging
```

### Example 3: Performance Topic

```bash
/guru performance
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
