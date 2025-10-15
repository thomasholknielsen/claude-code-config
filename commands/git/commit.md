---
description: "Smart commit message generation with quality checks"
argument-hint: "[message]"
allowed-tools: Bash, Read, Grep, mcp__sequential-thinking__sequentialthinking
---

# Command: Commit

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Create conventional commit(s) with auto-detection of type from uncommitted files (docs → docs:, tests → test:, new files → feat:), optional batch mode for logical grouping by type, pre-commit linting with auto-fix, format validation (type prefix, scope extraction, 72-char limit)

**P**urpose: Maintain clean git history with conventional commit format compliance, atomic commits for single functionality, intelligent type detection from file analysis (not commit history), automated code quality enforcement via pre-commit linting

**E**xpectation: Single atomic commit (default) or multiple logical commits grouped by type (--batch mode), validated conventional format `<type>(<scope>): <description>`, all code passing linting checks, auto-generated messages if not provided, clear commit summaries with next steps guidance

## Analysis Methodology

### 1. Pre-Commit Linting: Run `/lint:correct-all`, auto-fix errors, stage fixed files, abort if critical errors remain

### 2. File Analysis: Execute `git diff HEAD --name-status`, analyze uncommitted files only (never commit history), group by type if --batch mode

### 3. Type Detection: Apply priority rules (docs files → docs:, test files → test:, new files → feat:, fix keywords → fix:, default → refactor:), extract scope from directory patterns

### 4. Message Generation/Validation: Parse provided message or auto-generate from type + file changes, validate conventional format, check 72-char limit

### 5. Commit Execution: Create single commit (default) or multiple commits grouped by type (--batch), report summaries with file counts

## Explicit Constraints

**IN SCOPE**: Conventional commit creation, type auto-detection from uncommitted files, pre-commit linting with auto-fix, batch commit grouping by type, commit message validation, scope extraction, amend support
**OUT OF SCOPE**: Pushing to remote (use /git:push), PR creation (use /git:pr), branch management (use /git-flow:*), merge operations, git history rewriting beyond amend

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% commit requirements, Accuracy >90% type detection, Relevance >85% conventional format, Efficiency <15s for typical commits)

## Purpose

Creates logical, atomic commits with intelligent message generation and quality validation.

## Usage

```bash
/git:commit $ARGUMENTS
```

**Arguments**:

- `$1` (message): Commit message (optional, auto-generated from changes if not provided)
- `$2` (--batch): Create multiple logical commits (optional)
- `$3` (--amend): Amend the last commit (optional)

**$ARGUMENTS Examples**:

- `$ARGUMENTS = "feat: add user authentication system"` - Single commit with message
- `$ARGUMENTS = "--batch"` - Multiple logical commits
- `$ARGUMENTS = "Fix typo --amend"` - Amend last commit

## Process

### Without --batch Flag (Single Commit)

1. **Pre-Commit Linting**: Run `/lint:correct-all` to ensure code quality
   - Auto-fix linting errors across all languages
   - Stage auto-fixed files automatically
   - Report any unfixable issues requiring manual intervention
   - Abort commit if critical linting errors remain
2. **Analyze uncommitted files for type detection:**
   - Run `git diff HEAD --name-status` to get all uncommitted changes
   - Analyze file paths and content changes (staged + unstaged)
   - Determine primary change type from uncommitted file analysis only
   - Never analyze commit history for type detection
3. **Parse or generate commit type:**
   - If message provided: Extract and validate type prefix (feat:, fix:, docs:, etc.)
   - If no message: Auto-detect type from uncommitted file analysis
   - Validate type against conventional commit types
   - Extract optional scope from message format: `<type>(<scope>):`
4. **Validate commit format:**
   - Ensure type prefix is valid: `<type>: <description>`
   - Or with scope: `<type>(<scope>): <description>`
   - Verify description starts with lowercase
   - Check subject line ≤ 72 characters
   - Validate type is one of: feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert
5. **Generate commit message if needed:**
   - Use detected type + description from file changes
   - Format: `<type>: <generated description>`
   - Or with scope: `<type>(<scope>): <generated description>`
6. Create single atomic commit with validated conventional format
7. Report commit summary and next steps

### With --batch Flag (Multiple Logical Commits)

**CRITICAL:** Groups changes by type and creates separate commits for each type.

1. **Pre-Commit Linting**: Same as single commit mode
2. **Analyze and group files by type:**

   ```bash
   # Group all uncommitted files by conventional type
   declare -A file_groups
   while IFS= read -r file; do
     type=$(detect_conventional_type "$file")
     file_groups["$type"]+="$file "
   done < <(git diff HEAD --name-only)
   ```

3. **Create commit for each type group:**
   - For each type (feat, fix, docs, test, chore, etc.):
     - Stage only files of this type
     - Detect scope from file paths in group
     - Generate commit message for this type
     - Create commit
     - Report commit created
4. **Result:** Multiple logical commits instead of monolithic commit

**Example Output:**

```
✅ feat(auth): implement JWT authentication (12 files)
✅ docs: update authentication documentation (3 files)
✅ test: add authentication test coverage (8 files)
```

## Agent Integration

- **Specialist Options**: architecture-analyst can be spawned for handling git operations and coordination

## Examples

```bash
# Automatic commit with generated messages
/git:commit

# Single commit with custom message
/git:commit $ARGUMENTS
# where $ARGUMENTS = "feat: add user authentication system"

# Batch commits with logical grouping
/git:commit $ARGUMENTS
# where $ARGUMENTS = "--batch"
```

## Output

- Generated commit messages for each logical unit
- Commit hashes and summaries
- Files included in each commit
- Guidance on next steps (push, PR creation, etc.)

## Integration Points

- **Follows**: /git-flow:feature, code modifications
- **Followed by**: /git:push, /git:pr
- **Related**: /workflows:git

## Type Auto-Detection from Uncommitted Files

Analyzes `git diff HEAD --name-status` to determine type (priority order):

1. **All documentation files** (`*.md`, `docs/**`) → `docs:`
2. **All test files** (`*.test.*`, `*.spec.*`, `tests/**`, `__tests__/**`) → `test:`
3. **Dependency files** (`package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`) → `chore:`
4. **CI configuration** (`.github/**`, `.gitlab-ci.yml`, `.circleci/**`) → `ci:`
5. **Build configuration** (`webpack.config.js`, `tsconfig.json`, `Makefile`, `vite.config.*`) → `build:`
6. **New files added** (git status: A) → `feat:`
7. **Files with fix/bug keywords** (path contains "fix", "bug", "patch", "hotfix") → `fix:`
8. **Performance files** (path contains "perf", "optimize", "cache", "speed") → `perf:`
9. **Only formatting changes** (whitespace/semicolons, no logic) → `style:`
10. **Default for code modifications** → `refactor:`

**Scope Detection:** Extract from consistent directory patterns (e.g., `src/api/` → `api`, `src/auth/` → `auth`)

## Quality Standards

- **Runs automated linting and fixes before commit** - Ensures code style consistency
- **Aborts commit if critical linting errors remain** - Maintains code quality gate
- **Enforces conventional commit format** - Validates type prefix and message structure
- **Auto-detects type from uncommitted files** - Analyzes file changes, not commit history
- Creates atomic commits focused on single functionality
- Generates clear, descriptive commit messages following conventions
- Groups related changes logically (features, fixes, refactoring)
- Validates no breaking changes are mixed with features
- Ensures commit messages are under 72 characters for subject line
- Follows conventional commit format: `<type>(<scope>): <description>`
- **Stages auto-fixed files automatically** - Includes linting fixes in commit
