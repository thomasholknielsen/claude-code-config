---
description: "Detect project languages and run all applicable linters with auto-fix in parallel"
allowed-tools: Task, Read, Write, Edit, Grep, Glob, Bash, WebFetch, WebSearch, mcp__sequential-thinking__sequentialthinking
---

# Command: Lint and Correct All

## Framework Structure (S-Tier Pattern)

### APE Framework (General Purpose)

**A**ction: Auto-detect project languages via Glob file scanning (*.md,*.py, *.js,*.ts, *.sh,*.yml, *.json), launch parallel domain analyst analysis (code-quality/typescript/python/react analysts - ANALYSIS ONLY), synthesize analyst recommendations in main thread, execute multiple linters concurrently via single-message parallel tool calls (markdownlint/ruff/eslint/shellcheck/yamllint/jsonlint with --fix flags), comprehensive quality report (auto-fixed issues, manual intervention required, TODO list generation)

**P**urpose: Maximize linting performance through heavy parallelization (both analysis via Task + implementation via concurrent Bash/Edit), provide comprehensive quality coverage across all project languages, enable zero-configuration workflow (auto-detection), enforce code quality standards consistently, integrate with git commit workflow as quality gate, reduce manual linting overhead through auto-fix

**E**xpectation: Languages detected (file counts per type), parallel analyst analysis launched (3 max concurrently - recommendations only), main thread executes all linters concurrently (single message with multiple Bash/Edit calls), comprehensive report (auto-fixed counts by language, manual intervention required with file:line, TODO list if needed), exit code indicates success/failure, ready-to-commit status, substantial performance improvement vs sequential execution

## Quality Standards (CARE)

**Target**: 85+ overall (Completeness >95% language coverage, Accuracy >90% auto-fix safety, Relevance >85% actionable reports, Efficiency varies by project size with substantial parallelization speedup)

## Explicit Constraints

**IN SCOPE**: Language auto-detection (7 languages: Markdown/Python/JS/TS/Shell/YAML/JSON), parallel analyst analysis (3 max - ANALYSIS ONLY via Task), main thread linter execution (concurrent Bash/Edit calls), auto-fix (safe formatting/style only), comprehensive reporting (fixed/manual counts), TODO list generation, git commit workflow integration, exclusion patterns (node_modules/.venv/dist/build)
**OUT OF SCOPE**: Custom linter configuration (respects existing configs), logic changes (formatting only), manual code review (auto-fix focus), single-language linting (use language-specific commands), linter installation (assumes installed), configuration file creation

## Purpose

Automatically detect project languages, run all applicable linters in parallel for maximum performance,
and provide a comprehensive quality report across the entire codebase.

## Core Parallelization Principle

**MAXIMIZE PARALLEL EXECUTION**: Both analysis (via Task) AND implementation (via concurrent tool calls) are heavily parallelized for optimal performance.

## Usage

```bash
/lint:correct-all
```

**No arguments required** - Fully automated workflow

## Process

1. **Language Detection**: Use Glob to scan for language-specific files
2. **Parallel Analysis**: Launch domain analysts concurrently for language-specific linting analysis
3. **Parallel Implementation**: Main thread executes multiple linters concurrently based on analyst recommendations
4. **Validation**: Verify fixes and report remaining manual issues

## Language Detection Matrix

**File Pattern → Lint Command Mapping:**

| Language   | File Patterns                  | Command             |
|------------|--------------------------------|---------------------|
| Markdown   | `*.md`                         | `/lint:markdown`    |
| Python     | `*.py`                         | `/lint:python`      |
| Shell      | `*.sh`, `*.bash`               | `/lint:shell`       |
| JavaScript | `*.js`, `*.jsx`                | `/lint:javascript`  |
| TypeScript | `*.ts`, `*.tsx`                | `/lint:typescript`  |
| YAML       | `*.yml`, `*.yaml`              | `/lint:yaml`        |
| JSON       | `*.json`                       | `/lint:json`        |

**Exclusion Patterns (all languages):**

- `.git/`
- `.trees/`
- `node_modules/`
- `.venv/`, `venv/`
- `dist/`, `build/`
- `__pycache__/`

## Agent Integration

**Critical Constraint**: **Subagents provide analysis ONLY - no implementation allowed**

- **Phase 1**: Domain analysts conduct linting analysis and return recommendations to main thread
- **Phase 2**: **Main thread synthesizes analyst findings and applies all auto-fixes**
- **Phase 3**: Main thread executes all linting fixes and validation

**Primary Agent**: code-quality-analyst - Orchestrates parallel linting analysis (advisory only)

**Parallel Domain Analysts** (3 concurrent based on detected languages - analysis only):

- code-quality-analyst - General code quality analysis, formatting issue detection, and style recommendations
- code-typescript-analyst - TypeScript-specific linting analysis and type safety recommendations (if TypeScript detected)
- frontend-react-analyst - React-specific pattern analysis and best practice recommendations (if React detected)
- code-python-analyst - Python linting analysis and PEP 8 compliance recommendations (if Python detected)

**Implementation Responsibility**: Main thread executes all linting and auto-fixes using Bash/Edit tools

**Execution Pattern**:

```python
# Phase 1: Parallel Linting Analysis (3 analysts max concurrently - ANALYSIS ONLY)
Task("code-quality-analyst: Analyze all general files (markdown, yaml, json, shell) and identify linting issues")
Task("code-typescript-analyst: Analyze TypeScript/JavaScript files and identify linting violations") # if TS/JS detected
Task("code-python-analyst: Analyze Python files for linting issues (ruff, black compliance)") # if Python detected
Task("frontend-react-analyst: Analyze React-specific patterns and identify violations") # if React detected

# Each analyst persists findings to .agent/context/{session-id}/ and returns recommendations

# Phase 2: Parallel Implementation (Main thread executes multiple linters concurrently)
# Single message with multiple concurrent operations for maximum performance:
Bash("markdownlint *.md --fix")        # Parallel linting
Bash("python -m ruff check . --fix")   # Parallel linting
Bash("npm run lint:typescript")        # Parallel linting
Bash("shellcheck **/*.sh")             # Parallel linting
Edit("file1.ts", old_ts, new_ts)       # Parallel file fix
Edit("file2.py", old_py, new_py)       # Parallel file fix
```

**Performance Benefit**: 6+ operations execute concurrently vs sequential execution

## Examples

### Example 1: Full-Stack Web Application

```bash
/lint:correct-all
```

**Process:**

```text
Detecting project languages...
✓ Found 45 TypeScript files
✓ Found 12 Python files
✓ Found 8 Markdown files
✓ Found 6 YAML files

Launching parallel linting analysis...
→ Task("code-quality-analyst: Analyze markdown and yaml files for linting violations")
→ Task("code-typescript-analyst: Analyze TypeScript files for linting issues")
→ Task("code-python-analyst: Analyze Python files for linting issues")

Analysts complete analysis through concurrent execution (significantly faster than sequential)
Main thread then applies all auto-fixes based on analyst recommendations

Results synthesized:
✓ TypeScript: 23 issues fixed, 2 remaining
✓ Python: 8 issues fixed, 0 remaining
✓ Markdown: 12 issues fixed, 0 remaining
✓ YAML: 3 issues fixed, 0 remaining

Summary:
✓ 46 issues fixed automatically
⚠ 2 issues require manual intervention

Remaining issues persisted to .agent/context/quality-analysis-*.md
```

### Example 2: Documentation Repository

```bash
/lint:correct-all
```

**Process:**

```text
Detecting project languages...
✓ Found 156 Markdown files
✓ Found 3 YAML files

Main thread running linters with auto-fix based on analyst recommendations...
→ /lint:markdown --fix (156 files)
→ /lint:yaml --fix (3 files)

Results:
✓ Markdown: 47 issues fixed, 0 remaining
✓ YAML: 2 issues fixed, 0 remaining

Summary:
✓ 49 issues fixed automatically
✓ All files now passing

No manual intervention required.
```

### Example 3: Multi-Language Monorepo

```bash
/lint:correct-all
```

**Process:**

```text
Detecting project languages...
✓ Found 128 TypeScript files
✓ Found 45 JavaScript files
✓ Found 23 Python files
✓ Found 12 Shell scripts
✓ Found 34 Markdown files
✓ Found 18 YAML files
✓ Found 15 JSON files

Main thread running linters with auto-fix based on analyst recommendations...
→ /lint:typescript --fix (128 files)
→ /lint:javascript --fix (45 files)
→ /lint:python --fix (23 files)
→ /lint:shell (12 files)
→ /lint:markdown --fix (34 files)
→ /lint:yaml --fix (18 files)
→ /lint:json --fix (15 files)

Results:
✓ TypeScript: 67 issues fixed, 3 remaining
✓ JavaScript: 34 issues fixed, 1 remaining
✓ Python: 12 issues fixed, 0 remaining
⚠ Shell: 5 issues found (manual fix required)
✓ Markdown: 28 issues fixed, 0 remaining
✓ YAML: 7 issues fixed, 0 remaining
✓ JSON: 4 issues fixed, 0 remaining

Summary:
✓ 152 issues fixed automatically
⚠ 9 issues require manual intervention

TODO list created with 9 items requiring manual fixes.
```

## Integration Points

### Pre-Commit Integration

Called by `/git:commit` before creating commits:

```text
/git:commit workflow:
1. Run /lint:correct-all
2. Stage auto-fixed files
3. If manual fixes required: report and abort
4. If all clean: proceed with commit
```

### CI/CD Integration

```yaml
# .github/workflows/quality.yml
- name: Lint and Correct All
  run: claude-cli /lint:correct-all

- name: Check for remaining issues
  run: |
    if [ -f .claude/.todos/TODO.md ]; then
      echo "Linting issues remain"
      exit 1
    fi
```

### Related Commands

**Upstream (calls this workflow):**

- `/git:commit` - Pre-commit quality gate
- `/workflows:run-cleanup-workflow` - Comprehensive cleanup
- `/review:code` - Code quality review preparation

**Downstream (this workflow calls):**

- `/lint:markdown` - Markdown linting
- `/lint:python` - Python linting
- `/lint:shell` - Shell script linting
- `/lint:javascript` - JavaScript linting
- `/lint:typescript` - TypeScript linting
- `/lint:yaml` - YAML linting
- `/lint:json` - JSON validation

**Complements:**

- `/clean:improve-readability` - Beyond linting fixes
- `/refactor:*` - Post-refactoring quality checks
- `/analyze:code-quality` - Detailed quality metrics

## Output Format

### Success Output (All Fixed)

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Lint and Correct All - Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Languages Detected: 5
Files Processed: 234

Auto-Fixed Issues: 89
  • TypeScript: 34
  • Python: 23
  • Markdown: 18
  • YAML: 8
  • JSON: 6

✓ All linting issues resolved automatically
✓ No manual intervention required
✓ Ready to commit
```

### Partial Success Output (Manual Fixes Required)

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Lint and Correct All - Action Required
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Languages Detected: 6
Files Processed: 187

Auto-Fixed Issues: 67
  • TypeScript: 28
  • Python: 19
  • Markdown: 12
  • YAML: 5
  • JSON: 3

⚠ Manual Intervention Required: 4
  • TypeScript: 2 (type errors)
  • Shell: 2 (logic issues)

TODO list created: .claude/.todos/TODO.md

Next Steps:
1. Review TODO list for required fixes
2. Fix remaining issues manually
3. Run workflow again to verify
4. Proceed with commit when all clear
```

## Quality Standards

### Auto-Fix Safety

**Safe Auto-Fixes (Applied Automatically):**

- Formatting and whitespace
- Import sorting and organization
- Semicolon insertion/removal
- Quote style consistency
- Trailing comma management
- Line length adjustments
- Indentation normalization

**Manual Review Required:**

- Logic changes
- Type errors
- Unused variables/imports (context-dependent)
- Structural issues
- Security vulnerabilities

### Comprehensive Coverage

- All project languages detected automatically
- No configuration required (respects existing configs)
- Parallel execution for maximum performance
- Unified reporting across all linters

### Cross-Platform Compatibility

- Works on Windows, macOS, Linux
- Uses pathlib for file operations
- Handles different line endings (CRLF/LF)
- Platform-agnostic linter detection

## Performance Characteristics

**Typical Execution Times:**

| Project Size  | Languages | Files | Duration |
|---------------|-----------|-------|----------|
| Small         | 1-2       | <50   | 5-10s    |
| Medium        | 3-4       | 50-200| 10-20s   |
| Large         | 5+        | 200+  | 20-40s   |
| Monorepo      | 7+        | 500+  | 40-90s   |

**Parallelization Benefit:**

- Sequential execution: Significantly longer for large codebases
- Parallel execution: Much faster through concurrent linter invocation
- **Speedup: Substantial improvement through parallelization**

## Error Handling

### No Languages Detected

```text
⚠ No supported languages detected in project

Supported languages:
  • Markdown (*.md)
  • Python (*.py)
  • Shell (*.sh, *.bash)
  • JavaScript (*.js, *.jsx)
  • TypeScript (*.ts, *.tsx)
  • YAML (*.yml, *.yaml)
  • JSON (*.json)

Check file extensions and project structure.
```

### Linter Not Available

```text
⚠ Python files detected but ruff not installed

Skipping Python linting...

Install required linter:
  pip install ruff

Then run workflow again.
```

### Partial Linter Failures

```text
✓ Markdown: Complete
✗ TypeScript: Linter failed
✓ Python: Complete

2 of 3 linters completed successfully.
Proceeding with available results...
```

## Best Practices

1. **Run Before Every Commit**: Integrate into `/git:commit` workflow
2. **CI/CD Quality Gate**: Fail builds on linting errors
3. **Incremental Adoption**: Start with auto-fix, gradually address manual issues
4. **Review Auto-Fixes**: Spot-check changes before committing
5. **Maintain Configs**: Keep linter configurations in version control
6. **Update Regularly**: Keep linter tools updated for latest rules
7. **Team Consistency**: Share linter configs across team

## Success Criteria

✅ All applicable linters executed successfully
✅ Auto-fixable issues resolved automatically
✅ Clear report of remaining manual issues
✅ TODO list generated for manual fixes
✅ Parallel execution completed efficiently
✅ Exit code indicates success/failure state
✅ Ready for commit (if no manual issues)

## Notes

- **Fully Automated**: No configuration or arguments required
- **Parallel Execution**: Maximum performance through concurrent linting
- **Comprehensive**: Covers all common programming languages
- **Safe**: Only applies auto-fixes that preserve functionality
- **Informative**: Clear reporting of what was fixed and what remains
- **Integrated**: Works seamlessly with git commit workflow

---

**Related Commands:**

- `/lint:all` - Detect and lint without auto-fix
- `/git:commit` - Calls this workflow pre-commit
- `/clean:improve-readability` - Broader code cleanup
- `/review:code` - Comprehensive code quality review
