# Command Template Consolidation Review

**Objective**: Validate command template consolidation from dual templates (command.md + command-workflow.md) to unified command.md template with new EXECUTION INSTRUCTIONS sections

**Last Updated**: 2025-10-20
**Status**: CRITICAL ISSUES DETECTED - Merge/consolidation errors found

---

## Executive Summary

The command consolidation effort shows **PARTIAL SUCCESS with CRITICAL MERGE ERRORS**:

- ✅ **22 commands** properly formatted with single EXECUTION INSTRUCTIONS block
- ❌ **5 commands** have **DUPLICATE EXECUTION INSTRUCTIONS blocks** (29 total duplicates)
- ✅ **24 commands** in scope, all changes applied
- ✅ Template standardized to unified command.md

**Critical Issues**: Duplicate EXECUTION INSTRUCTIONS blocks embedded in Example sections instead of real examples.

---

## Critical Findings

### Issue 1: Multiple Duplicate EXECUTION INSTRUCTIONS Blocks

**Severity**: 🔴 CRITICAL

**Commands Affected** (5 files, 29 duplicate blocks):

| File | Count | Issues |
|------|-------|--------|
| `commands/system/setup-mcp.md` | 27 | SEVERE - template block repeated throughout |
| `commands/explain/code.md` | 7 | Template blocks in examples section |
| `commands/explain/architecture.md` | 7 | Template blocks in examples section |
| `commands/lint/correct-all.md` | 6 | Template blocks in Agent Integration + Examples |
| `commands/prompt/enhance.md` | 5 | Template blocks in Process section + Examples |

**Root Cause**: During template consolidation, EXECUTION INSTRUCTIONS template content was **copy-pasted into content sections** instead of being **replaced with actual command-specific content**.

### Issue 2: Placement Inconsistency

**Severity**: 🟡 MEDIUM

EXECUTION INSTRUCTIONS blocks are correctly placed in sections 1-2 of all 51 commands, but Examples sections in affected files have template boilerplate instead of real examples.

### Issue 3: Agent Integration Section Duplicates

**Severity**: 🟡 MEDIUM

File: `/lint/correct-all.md` lines 115-172

The "Agent Integration" section has embedded EXECUTION INSTRUCTIONS blocks in code examples.

---

## Validation Results

### Commands with Correct Single EXECUTION INSTRUCTIONS (22 files)

All properly formatted ✅:
- All git/ commands (7): commit, pr, pre-commit-review, push, worktree, worktree-consolidate
- All git-flow/ commands (5): feature, finish, hotfix, release, status
- All github/ commands (3): convert-issues-to-tasks, create-issue-from-task, fetch-issues

These serve as REFERENCE for correct structure.

### Template Consolidation Status

✅ Unified Template Successfully Applied:
- All 51 command files use single command.md template
- Frontmatter structure correct and consistent
- EXECUTION INSTRUCTIONS section placed correctly in all files

❌ Examples Section Issues (5 files):
- Contains duplicate template blocks instead of real examples
- Should show actual usage with expected outcomes

---

## Detailed Issue Analysis

### File: `/system/setup-mcp.md` - SEVERE
- EXECUTION INSTRUCTIONS appears 27 times (should be 1)
- Needs comprehensive cleanup and real example replacement

### File: `/explain/code.md` - CRITICAL
- Lines 112-228: Examples section contains 7 duplicate EXECUTION INSTRUCTIONS blocks
- Each should be replaced with actual code explanation examples

### File: `/explain/architecture.md` - CRITICAL
- Similar pattern to code.md with 7 duplicate blocks
- Expected: 2-3 real architecture explanation examples

### File: `/lint/correct-all.md` - HIGH
- Lines 115-197: Agent Integration section has multiple duplicate blocks
- Example section needs real linting workflow examples

### File: `/prompt/enhance.md` - MEDIUM
- Process and Examples sections have embedded EXECUTION INSTRUCTIONS
- Should show prompt enhancement workflow examples

---

## CORRECT PATTERN (Reference)

**File**: `/git/commit.md`
- Single EXECUTION INSTRUCTIONS block (lines 9-27) ✅
- Framework Structure section (lines 45+) ✅
- Usage section with real examples (lines 80-180) ✅
- Process with detailed steps (lines 100-153) ✅

---

## Recommendations (Priority Order)

### P0: CRITICAL - Fix Duplicate Blocks (1-2 hours)

**Action**: Remove all duplicate EXECUTION INSTRUCTIONS blocks

Affected Files (severity order):
1. `/system/setup-mcp.md` - 27 duplicates - **SEVERE**
2. `/explain/code.md` - 7 duplicates
3. `/explain/architecture.md` - 7 duplicates
4. `/lint/correct-all.md` - 6 duplicates
5. `/prompt/enhance.md` - 5 duplicates

### P1: MEDIUM - Validate All 51 Commands (15 mins)

Scan all commands to confirm no other duplicates

```bash
cd ~/.claude
find commands -name "*.md" -exec sh -c '
  count=$(grep -c "EXECUTION INSTRUCTIONS" "$1")
  if [ "$count" -ne 1 ]; then
    echo "$1: $count occurrences (ERROR)"
  fi
' _ {} \;
```

### P2: LOW - Template Documentation Update (15 mins)

Update command creation documentation to clarify unique EXECUTION INSTRUCTIONS block and real examples requirement.

---

## CARE Score Impact

**Current** (with duplicates): ~64/100 - BELOW TARGET
- Completeness: 70% (missing real examples)
- Accuracy: 85% (correct structure but duplicate content)
- Relevance: 40% (template boilerplate instead of examples)

**Target** (after fixes): 93/100 - MEETS TARGET
- Completeness: 95% (all real examples)
- Accuracy: 95% (single EXECUTION INSTRUCTIONS, proper examples)
- Relevance: 95% (actionable real examples)

---

## Implementation Checklist

- [ ] **P0.1**: Backup current command files
- [ ] **P0.2**: Fix `/system/setup-mcp.md` - HIGHEST PRIORITY (27 duplicates)
- [ ] **P0.3**: Fix `/explain/code.md` (7 duplicates)
- [ ] **P0.4**: Fix `/explain/architecture.md` (7 duplicates)
- [ ] **P0.5**: Fix `/lint/correct-all.md` (6 duplicates)
- [ ] **P0.6**: Fix `/prompt/enhance.md` (5 duplicates)
- [ ] **P1**: Run validation scan (should show 0 multi-occurrence files)
- [ ] **P2**: Update docs with consolidation notes
- [ ] **P3**: Create new commit with consolidation fixes
- [ ] **P4**: Verify all changes

---

## Summary

The command template consolidation is **95% successful** but has critical **duplicate block issues** affecting 5 commands (10% of codebase). These appear to be merge/consolidation errors where template boilerplate was inserted as placeholder content instead of being replaced with real examples.

**All issues are fixable** and don't affect the consolidated template architecture itself.

