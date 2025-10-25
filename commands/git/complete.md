---
description: "Complete git workflow: create branch, logical commits, push, and create PR"
argument-hint: "[branch-name]"
allowed-tools: Bash, Read, Grep
---

# Command: Complete Git Workflow

## EXECUTION INSTRUCTIONS (START HERE)

### ⚠️ MANDATORY: Read This BEFORE Proceeding

**What this command does:** Execute complete git workflow end-to-end - create branch, group changes into logical commits by type, push, and create PR.

**Claude Code MUST execute this workflow:**
1. ✓ Auto-detect workflow mode (git-flow vs conventional commits)
2. ✓ Analyze uncommitted changes and group by type (feat/fix/docs/test)
3. ✓ Create branch from appropriate base (develop for git-flow, HEAD for conventional)
4. ✓ Create logical commits (one per type group)
5. ✓ Push with tracking (-u flag)
6. ✓ Create PR with appropriate base branch
7. ✓ Handle errors with clear manual fallback

**Claude Code MUST NOT:**
- ✗ Create single monolithic commit (must group by type)
- ✗ Skip any workflow steps silently
- ✗ Skip PR creation without error reporting

---

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


## VALIDATION & PREREQUISITES

**Before executing, Claude Code MUST validate:**

- [ ] Git repository exists and is initialized
- [ ] `gh` (GitHub CLI) is installed and authenticated
- [ ] At least one uncommitted change exists (git diff HEAD shows changes)
- [ ] Current branch is up-to-date with remote (no divergence)
- [ ] Write permissions exist on repository
- [ ] Network connectivity to GitHub API

**If any validation fails**: Stop immediately and report clearly what's missing:

```bash
# Check git repo
git rev-parse --git-dir 2>/dev/null || exit "❌ Not a git repository"

# Check gh CLI
command -v gh &> /dev/null || exit "❌ GitHub CLI not installed. Install from: https://cli.github.com/"

# Check gh authentication
gh auth status &> /dev/null || exit "❌ GitHub CLI not authenticated. Run: gh auth login"

# Check for changes
if ! git diff HEAD --quiet; then
  echo "✓ Uncommitted changes detected"
else
  exit "❌ No uncommitted changes to commit"
fi
```

---

## Workflow Options

| Option | Action | Recommendation |
|--------|--------|-----------------|
| **A** | Create draft PR for review before marking ready | **← Recommended** for team collaboration |
| **B** | Create ready PR immediately for merging | For simple hotfixes or confident changes |
| **C** | Push branch only, skip PR creation | When branch is WIP or awaiting external input |

Your choice (A/B/C)?

## Next Steps

| Step | Action | Details |
|------|--------|---------|
| 1 | Review created PR in browser | Check diff, CI status, and requested reviewers |
| 2 | Merge PR or request changes | Approve and merge, or address review feedback |
| 3 | Create next feature branch | Start work on next feature or bugfix |
| 4 | Monitor deployment status | Ensure changes deployed successfully |

What would you like to do next?

---

## IMPLEMENTATION FLOW

### Step 1: Pre-flight Validation
Validate gh CLI is installed and authenticated, git repository exists, uncommitted changes present, branch is up-to-date

### Step 2: Workflow Detection
Auto-detect workflow mode: if both `develop` and `main` branches exist → git-flow mode, otherwise → conventional commits mode

**Details:**
- Check: `git branch -a | grep -q "develop" && git branch -a | grep -q "main"`
- Determines base branch for feature creation and PR targeting

### Step 3: Analyze & Group Changes
Run `git diff HEAD --name-status`, group files by conventional commit type (feat, fix, docs, test, chore, perf, style, refactor, ci, build)

**Details:**
- Extract commit type from file paths using type detection priority
- Detect scope from file path context (e.g., `src/auth/` → `auth`)
- Result: Logical commit groups instead of monolithic commit

### Step 4: Create Branch
Use provided branch name or auto-generate from primary commit type, create from appropriate base branch

**Details:**
- If branch name provided: Use it as-is
- If not provided: Auto-generate from primary type and scope
- Git-Flow format: `feature/<description>` (from develop)
- Conventional format: `<type>/<description>` or `<type>/<scope>/<description>` (from HEAD)

### Step 5: Create Logical Commits
For each type group (feat, fix, docs, test, etc.):
1. Stage only files of this type
2. Detect scope from file paths
3. Generate conventional commit message: `<type>(<scope>): <description>`
4. Create commit
5. Report: `✅ <type>(<scope>): <description> (N files)`

### Step 6: Push with Tracking
Push all commits to origin with `-u` flag, enabling branch tracking for future operations

**Details:**
- Command: `git push -u origin <branch-name>`
- Reports: Total files, total commits pushed

### Step 7: Create PR with Error Handling
Auto-detect appropriate base branch, create PR, provide manual fallback if creation fails

**Details:**
- Git-Flow: feature/* → develop, others → main
- Conventional: main
- Check for existing PR before creation (no duplicates)
- PR title and description auto-generated from commits
- Detailed error handling with manual instructions

---

## USAGE

**Invocation:**
```bash
/git:complete [branch-name]
```

**Cross-Platform Note**: Works on Windows (PowerShell/WSL), macOS, Linux. All paths use forward slashes.

**Arguments:**

| Argument | Required | Description | Example |
|----------|----------|-------------|---------|
| `branch-name` | No | Custom branch name for the workflow. If not provided, auto-generated from primary commit type | `feature/auth`, `fix/login-bug`, `docs/api-guide` |

**$ARGUMENTS Examples:**

- `$ARGUMENTS = "feature/authentication"` - Use custom branch name in git-flow mode
- `$ARGUMENTS = "fix/dashboard-layout"` - Use custom branch name for bug fix
- `$ARGUMENTS = ""` - Auto-generate branch name from primary commit type

---

## EXAMPLES

**Example 1: Multi-Type Changes (Auto-branch)**

```bash
# Changes:
# - src/auth/*.ts (12 files) - features
# - docs/api.md (1 file) - documentation
# - tests/auth/*.test.ts (8 files) - tests

/git:complete

# Expected output:
✓ Checking GitHub CLI authentication...
✓ Analyzing 21 uncommitted files...
✓ Grouped into 3 logical commits
✓ Git-Flow mode detected (develop + main branches)

✅ Created branch: feature/authentication-system
✅ feat(auth): implement JWT authentication (12 files)
✅ docs: update API documentation (1 file)
✅ test: add authentication test coverage (8 files)
✅ Pushed to origin/feature/authentication-system (21 files, 3 commits)
✅ PR created: https://github.com/org/repo/pull/123
```

**Example 2: Single-Type Changes (Custom branch)**

```bash
# Changes:
# - docs/*.md (5 files) - documentation only

/git:complete docs/improve-readme

# Expected output:
✓ Checking GitHub CLI authentication...
✓ Analyzing 5 uncommitted files...
✓ Grouped into 1 logical commit
✓ Conventional commits mode detected (main only)

✅ Created branch: docs/improve-readme
✅ docs: improve README and documentation (5 files)
✅ Pushed to origin/docs/improve-readme (5 files, 1 commit)
✅ PR created: https://github.com/org/repo/pull/124
```

**Example 3: PR Creation Failure with Fallback**

```bash
/git:complete feature/payments

# Expected output:
✓ Checking GitHub CLI authentication...
✓ Analyzing 15 uncommitted files...
✓ Grouped into 2 logical commits

✅ Created branch: feature/payments
✅ feat(api): add payment endpoints (10 files)
✅ test: add payment integration tests (5 files)
✅ Pushed to origin/feature/payments (15 files, 2 commits)
❌ PR creation failed

Error: gh: authentication token expired

Possible causes:
1. GitHub CLI authentication expired - Run: gh auth login
2. Insufficient permissions - Check repository access
3. Branch protection rules require review

Manual PR creation:
  1. Visit: https://github.com/org/repo/compare/feature/payments
  2. Or run: gh pr create --web

✅ Branch pushed successfully: feature/payments
✅ Created 2 logical commits
```

---

## ERROR HANDLING

**Errors that might occur and how to handle them:**

| Error Scenario | Likely Cause | Solution |
|----------------|-------------|----------|
| `gh CLI not installed` | GitHub CLI missing from system | Install from https://cli.github.com/ and add to PATH |
| `gh CLI not authenticated` | Not logged into GitHub | Run: `gh auth login` and complete authentication flow |
| `No uncommitted changes` | Working tree is clean | Make changes to files, then run command again |
| `Not a git repository` | Command run outside git repo | Navigate to repository root and retry |
| `Branch already exists` | Branch name conflicts with existing branch | Provide different branch name or delete existing branch |
| `Push fails` | Network issue or permission denied | Check git remote, authentication, and network connectivity |
| `PR creation fails` | GitHub API error or branch protection rules | Check error message, run `gh auth login`, verify permissions |
| `No base branch detected` | Neither develop nor main branch found | Check git-flow setup or conventional commits setup |

**General Error Response Pattern:**
```
❌ Error: [Clear error message]

**Why:** [Explanation of root cause]

**How to fix:**
1. [Specific action 1]
2. [Specific action 2]

**Verify with:**
command-to-verify-fix
```

---

## OUTPUT FORMAT

**Claude Code MUST always provide:**

✅ **Status indicator**: ✅ Workflow Complete
✅ **Workflow mode**: Git-Flow or Conventional Commits detected
✅ **Branch info**: Branch name, commits created, files included
✅ **Commits created**: List with `✅ <type>(<scope>): <description> (N files)` format
✅ **Push confirmation**: `✅ Pushed to origin/<branch> (N files, M commits)`
✅ **PR result**: PR URL if successful, or error with manual fallback instructions
✅ **Next steps**: What to do after (review PR, cleanup, etc.)

---

## ROBUSTNESS & CONSTRAINTS

**IN SCOPE:**
- Git workflow orchestration (branch creation, commits, push, PR)
- Commit grouping by conventional type (feat, fix, docs, test, chore, etc.)
- Branch creation from appropriate base (develop in git-flow, HEAD in conventional)
- Conventional commit formatting with scope detection
- PR creation with error handling and manual fallback
- GitHub CLI integration and authentication validation
- Workflow mode auto-detection (git-flow vs conventional commits)

**OUT OF SCOPE:**
- Code implementation (developer responsibility)
- Git repository initialization (git init)
- Git configuration management (git config)
- Merge conflict resolution (manual resolution required)
- Git history rewriting (rebase, force-push)
- Complex branch strategies beyond git-flow and conventional commits

**Atomic Operations:**
- Workflow is sequential: validation → branch creation → commits → push → PR
- Either all steps succeed or operation fails at first error
- If validation fails: nothing is modified
- If branch creation fails: no commits attempted
- If push fails: PR creation skipped
- No partial states: all-or-nothing principle

**Cross-Platform Compatibility:**
- ✓ Works on: Windows (PowerShell/WSL), macOS, Linux
- ✓ Git operations: Cross-platform native git commands
- ✓ Paths: All use forward slashes `/` (Claude Code translates for platform)
- ✓ Shell commands: Bash syntax compatible with WSL on Windows

---

## INTEGRATION POINTS

- **Follows**: Code implementation, feature completion, bug fixes
- **Precedes**: Code review process, CI/CD pipeline execution
- **Related**: `/git:commit`, `/git:push`, `/git:pr` (atomic alternatives for step-by-step control)
- **Related**: `/git-flow:feature`, `/git-flow:hotfix`, `/git-flow:release` (git-flow specific workflows)

**Workflow Example - When to Use This Command:**
```
[Implement feature] → /git:complete [branch-name] → [Code Review] → [Merge to develop/main]
```

**Alternative - When to Use Atomic Commands:**
```
[Implement feature] → /git:commit "message" → /git:push → /git:pr "title"
```

---

## QUALITY STANDARDS

**Command succeeds when:**
- ✓ All validation checks pass before executing
- ✓ Workflow mode correctly auto-detected (git-flow or conventional)
- ✓ Branch created from appropriate base
- ✓ Changes grouped into logical commits by type
- ✓ Each commit follows conventional format
- ✓ All commits pushed to origin with tracking
- ✓ PR created successfully OR detailed error with manual instructions
- ✓ User receives clear output with PR URL or fallback steps
- ✓ No silent failures

**Quality Checklist:**
- [X] Frontmatter fields filled with real values (not placeholders)
- [X] Each section has concrete content, specific examples
- [X] Examples are realistic and runnable
- [X] Validation rules explicit and checkable
- [X] Error handling covers foreseeable failures
- [X] Output format matches examples specified
- [X] No silent failures - all errors reported clearly
- [X] Workflow is atomic - either fully succeeds or stops at first error
- [X] Next Steps table always provided (2-4 actionable options)
- [X] Ends with "What would you like to do next?" closing

---

## Next Steps

After git workflow completes successfully, suggested next actions:

| Option | Action | Description | Command |
|--------|--------|-------------|---------|
| **A** | Review PR | Visit PR page to add description and monitor reviews | Visit PR URL provided |
| **B** | Monitor CI/CD | **Recommended: Watch automated tests and checks** | Visit PR checks section |
| **C** | Request review | Ask team members for code review | Comment in PR with mention |
| **Other** | Custom | What you need next | Describe your next step |

What would you like to do next? Choose from the table above or describe your next step.

