---
description: "Branch management operations with safety checks and team workflows"
argument-hint: "[branch-name]"
allowed-tools: Bash, Read, Grep
---

# Command: Branch

## Purpose

Creates, manages, and switches git branches with intelligent naming and safety validation.

## Usage

```bash
/git:branch $ARGUMENTS
```

**Arguments**:

- `$1` (branch-name): Branch name (optional, auto-generated from changes if not provided)
- `$2` (--from): Base branch to create from (optional, defaults to current HEAD)
- `$3` (--switch): Switch to branch after creation (optional, default behavior)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "feature/user-authentication"` - Create and switch to feature branch
- `$ARGUMENTS = "hotfix/login-bug --from=main"` - Create hotfix from main branch
- `$ARGUMENTS = ""` - Auto-generate branch name from changes

## Process

1. **Analyze uncommitted files for type:**
   - Run `git diff HEAD --name-status` to get all uncommitted changes
   - Analyze staged and unstaged file changes only
   - Determine primary type from uncommitted file analysis
   - Never analyze commit history for type detection
   - Extract scope from consistent directory patterns
2. **Parse or generate branch name:**
   - If name provided: Extract type, validate format
   - If no name: Auto-generate from uncommitted file analysis
   - Format: `<type>/<description>` or `<type>/<scope>/<description>`
   - Validate type is conventional: feat, fix, docs, style, refactor, test, chore, perf, ci, build
3. **Generate branch name components:**
   - Type: From detection or explicit argument
   - Scope: From file paths if consistent (e.g., "api", "auth", "payments")
   - Description: From file changes or explicit argument
   - Convert to kebab-case, remove special characters
4. **Validate branch name:**
   - Check type is valid conventional commit type
   - Verify format matches: `<type>/<description>` or `<type>/<scope>/<description>`
   - Validate description uses kebab-case
   - Ensure uniqueness against existing branches
5. Validate working directory state
6. Create branch from current HEAD and switch to it
7. Report branch creation status and next steps

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned for handling git operations and coordination

## Examples

```bash
# Create branch with auto-generated name
/git:branch

# Create branch with specific name
/git:branch $ARGUMENTS
# where $ARGUMENTS = "feature/user-authentication"

# Create hotfix branch
/git:branch $ARGUMENTS
# where $ARGUMENTS = "hotfix/login-bug"
```

## Output

- Created branch name and base commit
- Confirmation of successful branch switch
- Working directory status after branch creation
- Guidance on next steps (commit, push, etc.)

## Integration Points

- **Follows**: Code changes, feature development initiation
- **Followed by**: /git:commit, code modifications
- **Related**: /git:push, /git:pr, /git:full-workflow

## Type Auto-Detection from Uncommitted Files

Analyzes `git diff HEAD --name-status` to determine branch type (same priority as commits):

1. **All documentation files** → `docs/`
2. **All test files** → `test/`
3. **Dependency files** → `chore/`
4. **CI configuration** → `ci/`
5. **Build configuration** → `build/`
6. **New files added** → `feat/`
7. **Files with fix/bug keywords** → `fix/`
8. **Performance files** → `perf/`
9. **Only formatting changes** → `style/`
10. **Default for code modifications** → `refactor/`

**Scope Detection:** Extracts scope from consistent directory patterns:

- `src/api/users.ts`, `src/api/auth.ts` → `feat/api/...`
- `src/auth/login.ts`, `src/auth/jwt.ts` → `feat/auth/...`
- Multiple different dirs → No scope → `feat/...`

## Quality Standards

- **Enforces conventional branch naming** - Uses type prefixes matching commit conventions
- **Auto-detects type from uncommitted files** - Analyzes file changes, not commit history
- Validates clean working state before branch creation
- Generates meaningful branch names from file analysis
- Follows conventional format: `<type>/<description>` or `<type>/<scope>/<description>`
- Ensures branch creation doesn't conflict with existing branches
- Validates branch names use kebab-case format
- Provides clear feedback on branch status and next actions
