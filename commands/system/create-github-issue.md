---
description: "Create GitHub issues from tasks, TODOs, code comments, or direct input"
argument-hint: "[arguments]"
allowed-tools: Grep, Bash, Read, Write
---

# Command: Create GitHub Issue

## Purpose

Creates professional GitHub issues from multiple sources: direct input, tasks.md, code comments, or task lists. Interactive mode guides users through issue creation.

## Usage

```bash
/system:create-github-issue $ARGUMENTS
```

**Interactive Mode** (no arguments):

```bash
/system:create-github-issue
→ Prompts for: issue source, title, description, labels, milestone, assignee
```

**Arguments**:

- `$1` (--source): Source of items to convert (optional, triggers interactive if omitted)
  - `input`: Direct task list input (prompts for tasks)
  - `tasks-md`: Items from {project_root}/.agent/tasks.md
  - `code-comments`: TODO/FIXME/HACK/NOTE/BUG comments in codebase
  - `markdown`: Task lists from markdown files
  - `all`: All available sources
- `$2` (filter): Filter items to convert (priority, type, category) (optional, default: all)
- `$3` (--labels): GitHub issue labels to apply (optional)
- `$4` (--milestone): GitHub milestone to assign issues (optional)
- `$5` (--assignee): Default assignee for created issues (optional)
- `$6` (--comment-types): Comment types to include when source=code-comments (optional, default: TODO,FIXME,HACK,BUG)
- `$7` (--scope): File/directory scope for code comment search (optional, default: entire project)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = ""` - Interactive mode: prompts for input
- `$ARGUMENTS = "--source=input --labels=feature"` - Enter tasks directly, label as feature
- `$ARGUMENTS = "--source=tasks-md high --labels=bug,urgent"` - Convert high-priority tasks.md items
- `$ARGUMENTS = "--source=code-comments --comment-types=TODO,FIXME --labels=tech-debt"` - Convert TODO/FIXME comments
- `$ARGUMENTS = "--source=code-comments --scope=src/ --labels=refactor"` - Convert code comments in src/
- `$ARGUMENTS = "--source=all --milestone=v2.0"` - Convert all sources to v2.0 milestone

## Process

### Interactive Mode (No Arguments)

1. **Prompt for Source**:

   ```text
   How would you like to provide the issues?
   1. Enter tasks directly
   2. From tasks.md
   3. From code comments (TODO, FIXME, etc.)
   4. From markdown task lists
   5. From all sources
   ```

2. **Collect Input Based on Source**:

   **For "Enter tasks directly"**:

   ```text
   Enter your tasks (one per line, empty line to finish):
   > Implement user authentication
   > Add password reset functionality
   > Create user dashboard
   >
   ```

   **For other sources**: Prompt for filtering, scope, etc.

3. **Collect Metadata**:

   ```text
   Labels (comma-separated, optional):
   > feature, authentication

   Milestone (optional):
   > v2.0

   Assignee (optional):
   > @username
   ```

4. **Create Issues**: Generate GitHub issues using gh CLI

5. **Report Results**: Display created issue URLs

### For source=input

1. Parse $ARGUMENTS for GitHub issue options (labels, milestone, assignee)
2. Prompt user to enter tasks (multi-line input until empty line)
3. Parse each task line as separate issue title
4. Allow extended descriptions with `---` separator:

   ```text
   Task title
   ---
   Extended description
   Acceptance criteria
   ```

5. Create GitHub issues using Bash/gh CLI with specified metadata
6. Provide summary report with issue URLs

### For source=tasks-md

1. **ENFORCE LOCATION**: Read tasks from `{project_root}/.agent/tasks.md` only
2. Parse $ARGUMENTS for filtering and GitHub issue options
3. Filter task items based on specified criteria (priority, category)
4. Analyze filtered tasks for GitHub issue conversion
5. Create professional GitHub issues using Bash/gh CLI with labels and assignments
6. Update tasks.md to mark items as converted with issue links
7. Validate results and provide feedback with issue URLs

### For source=code-comments

1. Parse $ARGUMENTS for comment types, scope, and GitHub issue options
2. Search codebase using Grep for specified comment types (TODO, FIXME, HACK, NOTE, BUG)
3. Extract comment context:
   - File path and line number
   - Comment text and description
   - Surrounding code context (3 lines before/after)
   - Author from git blame (if available)
4. Analyze comments and group by similarity/theme
5. Create GitHub issues with:
   - Title: Comment text
   - Body: File location, line number, code context, related comments
   - Labels: Based on comment type (TODO→feature, FIXME→bug, HACK→tech-debt, BUG→bug)
6. Optionally create PR to remove converted comments or replace with issue links
7. Provide summary report with issue URLs and locations

### For source=markdown

1. Parse $ARGUMENTS for scope (directory/files) and GitHub issue options
2. Search for markdown files with task lists (- [ ] format)
3. Extract unchecked task items with file context
4. Create GitHub issues for each task
5. Optionally update markdown files with issue links
6. Provide summary report

### For source=all

1. Execute all source conversions sequentially
2. Deduplicate similar issues across sources
3. Provide consolidated report

**⚠️ LOCATION CONSTRAINT**: tasks.md operations MUST use `{project_root}/.agent/tasks.md` location only.

## Comment Type Mapping

| Comment Type | GitHub Labels | Priority | Description |
|-------------|---------------|----------|-------------|
| TODO | feature, enhancement | Medium | New functionality to implement |
| FIXME | bug, needs-fix | High | Known issues requiring fixes |
| HACK | tech-debt, refactor | Medium | Temporary solutions needing cleanup |
| BUG | bug, critical | High | Confirmed bugs in code |
| NOTE | documentation, info | Low | Important information or context |
| OPTIMIZE | performance, enhancement | Medium | Performance improvements |

## Agent Integration

- **Specialist Options**: quality-analyst can be spawned to analyze and categorize items for optimal GitHub issue structure

## Examples

### Interactive Mode

```bash
# No arguments - fully interactive
/system:create-github-issue

Claude: How would you like to provide the issues?
1. Enter tasks directly
2. From tasks.md
3. From code comments
4. From markdown task lists
5. From all sources

User: 1

Claude: Enter your tasks (one per line, empty line to finish):

User: Implement user authentication
User: Add password reset functionality
User: Create user dashboard
User:

Claude: Labels (comma-separated, optional):

User: feature, authentication

Claude: Milestone (optional):

User: v2.0

Claude: Creating 3 GitHub issues...
✓ Created #123: Implement user authentication
✓ Created #124: Add password reset functionality
✓ Created #125: Create user dashboard

All issues: https://github.com/org/repo/issues?q=milestone:v2.0+label:feature
```

### Direct Task Input

```bash
# Enter tasks directly with labels
/system:create-github-issue --source=input --labels=feature,auth
→ Prompts for task input
→ Creates issues with specified labels
```

### From tasks.md

```bash
# Convert high-priority tasks.md items as urgent bugs
/system:create-github-issue --source=tasks-md high --labels=bug,urgent

# Convert all tasks.md items to v2.0 milestone
/system:create-github-issue --source=tasks-md --milestone=v2.0

# Convert bug category tasks and assign to user
/system:create-github-issue --source=tasks-md bug --assignee=@username
```

### From Code Comments

```bash
# Convert all TODO and FIXME comments to GitHub issues
/system:create-github-issue --source=code-comments --comment-types=TODO,FIXME

# Convert code comments in src/ directory as tech debt
/system:create-github-issue --source=code-comments --scope=src/ --labels=tech-debt

# Convert only HACK comments with custom labels
/system:create-github-issue --source=code-comments --comment-types=HACK --labels=refactor,technical-debt

# Convert BUG comments as critical issues
/system:create-github-issue --source=code-comments --comment-types=BUG --labels=bug,critical --assignee=@lead
```

### From Markdown Task Lists

```bash
# Convert unchecked tasks from docs/ markdown files
/system:create-github-issue --source=markdown --scope=docs/ --labels=documentation

# Convert all markdown tasks to specific milestone
/system:create-github-issue --source=markdown --milestone=v1.0 --labels=planning
```

### Convert All Sources

```bash
# Convert everything to v2.0 release
/system:create-github-issue --source=all --milestone=v2.0

# Convert all sources with default labels
/system:create-github-issue --source=all --labels=backlog
```

## Direct Input Format

When using `--source=input` or interactive mode, you can provide tasks in multiple formats:

**Simple tasks** (one per line):

```text
Implement user authentication
Add password reset functionality
Create user dashboard
```

**Tasks with descriptions** (using `---` separator):

```text
Implement user authentication
---
Build JWT-based authentication with refresh tokens
- OAuth2 integration
- Session management
- Password hashing with bcrypt

Add password reset functionality
---
Email-based password reset flow
- Send reset link via email
- Token expiration (1 hour)
- Password strength validation
```

**Tasks with inline metadata** (using brackets):

```text
[P:high] Implement user authentication
[P:low] Add user dashboard
[A:@username] Fix authentication bug
```

## GitHub Issue Format

### For Code Comments

```markdown
**Title**: [FIXME] Validation logic needs error handling

**Body**:
Found in: `src/api/auth.ts:45`

```typescript
// Lines 42-48
export function validateUser(user: User) {
  // FIXME: Add proper error handling for invalid input
  return user.email && user.password;
}
```

**Context**: Authentication validation is missing comprehensive error handling.

**Related Comments**:

- src/api/auth.ts:67 - Similar validation issue
- src/api/users.ts:23 - Related error handling TODO

**Labels**: bug, needs-fix

```markdown

### For tasks.md Items

```markdown
**Title**: Implement user authentication system

**Body**:
**Priority**: High
**Category**: Feature
**Task ID**: TASK-012
**Description**:
Build JWT-based authentication with refresh tokens, password hashing, and session management.

**Acceptance Criteria**:

- [ ] JWT token generation
- [ ] Refresh token rotation
- [ ] Password hashing with bcrypt
- [ ] Session management

**Source**: .agent/tasks.md:12

**Labels**: feature, authentication
```

### For Direct Input

```markdown
**Title**: Implement user authentication

**Body**:
**Description**:
Build JWT-based authentication with refresh tokens
- OAuth2 integration
- Session management
- Password hashing with bcrypt

**Source**: Direct input

**Labels**: feature, authentication
**Milestone**: v2.0
```

## Output

Provides comprehensive report including:

- Number of items converted from each source
- GitHub issue URLs for all created issues
- Summary of labels and assignments applied
- Updated tasks.md with issue links (for tasks-md source)
- Optional: PR created to update code comments with issue references

## Best Practices

1. **Use interactive mode** for ad-hoc issue creation during development
2. **Start with code-comments source** to surface hidden technical debt
3. **Use --comment-types** to focus on specific work types
4. **Apply consistent labels** for filtering and organization
5. **Deduplicate manually** when using source=all to avoid duplicate issues
6. **Review generated issues** before closing to ensure context is clear
7. **Update original source** (code comments, tasks.md) with issue links for traceability

## Integration Points

**Works Well With**:

- `/system:get-github-issues` - Pull existing GitHub issues into work session
- `/system:find-comments` - Discover code comments before conversion
- `/system:create-task` - Capture tasks before converting to issues
- `/git:commit` - Commit updated files after conversion
- `/git:pr` - Create PR with issue references

**Follows Well**:

- Codebase audit or review workflows
- Sprint planning sessions
- Technical debt assessment
- Daily standup preparation
